import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from fleet_report import summarize


def fixture():
    return {'format': 'ai-decomp-fleet-results-v1', 'run_id': 'synthetic',
            'results': [{'id': 'a', 'task': {'project': 'test', 'target': 'f', 'seed_id': 'seed', 'context_id': 'ctx'},
                         'worker': {'id': 'w1', 'lineage_id': 'l1', 'model': 'synthetic', 'effort': 'high'},
                         'stop_reason': 'budget_censored', 'analysis_level': 'source',
                         'strict_result': {'status': 'unknown'}, 'promotion': {'status': 'not_requested'},
                         'counters': {'hypotheses': 3, 'unique_effective_outputs': 2},
                         'tokens': {'input': 100, 'cached_input': 80, 'output': 10, 'reasoning_output': 7},
                         'artifacts': ['synthetic:test-only'], 'blocker': None}],
            'costs': [{'id': 'c1', 'role': 'worker', 'amount': '0.01', 'unit': 'USD', 'basis': 'synthetic-v1', 'result_ids': ['a']}]}


class FleetReportTests(unittest.TestCase):
    def test_replay_is_idempotent_and_unknowns_stay_unknown(self):
        data = fixture()
        data['results'].append(copy.deepcopy(data['results'][0]))
        data['costs'].append(copy.deepcopy(data['costs'][0]))
        out = summarize(data)
        self.assertEqual(out['results'], 1)
        self.assertEqual(out['duplicate_cost_records_ignored'], 1)
        self.assertEqual(out['strict_statuses'], {'unknown': 1})
        self.assertEqual(out['counters']['compiler_processes']['unknown_results'], 1)
        self.assertEqual(out['costs'][0]['roles']['worker']['known_amount'], '0.01')
        self.assertIn('supervisor', out['costs'][0]['unreported_roles'])
        self.assertEqual(out['tokens']['output']['known_sum'], 10)

    def test_conflicting_replay_is_rejected(self):
        data = fixture()
        altered = copy.deepcopy(data['results'][0])
        altered['stop_reason'] = 'search_converged'
        data['results'].append(altered)
        with self.assertRaisesRegex(ValueError, 'Conflicting'):
            summarize(data)

    def test_candidate_and_promotion_need_distinct_receipts(self):
        data = fixture()
        row = data['results'][0]
        row['stop_reason'] = 'promotion_candidate'
        with self.assertRaises(ValueError):
            summarize(data)
        row['strict_result'] = {'status': 'pass', 'scope': 'function', 'verifier': 'synthetic', 'receipt': 'synthetic-proof'}
        row['promotion'] = {'status': 'queued'}
        self.assertEqual(summarize(data)['promotions'], {'queued': 1})
        row['stop_reason'] = 'accepted'
        with self.assertRaises(ValueError):
            summarize(data)
        row['promotion'] = {'status': 'promoted', 'receipt': 'synthetic-proof'}
        with self.assertRaises(ValueError):
            summarize(data)
        row['promotion'] = {'status': 'promoted', 'receipt': 'synthetic-native-transaction'}
        self.assertEqual(summarize(data)['promotions'], {'promoted': 1})
        replica = copy.deepcopy(row)
        replica['id'] = 'b'
        data['results'].append(replica)
        summary = summarize(data)
        self.assertEqual(summary['promotions'], {'promoted': 2})
        self.assertEqual(len(summary['distinct_reported_promotion_transactions']), 1)

    def test_redundant_strict_passes_do_not_multiply_targets(self):
        data = fixture()
        a = data['results'][0]
        a['strict_result'] = {'status': 'pass', 'scope': 'member', 'verifier': 'synthetic', 'receipt': 'proof-a'}
        a['stop_reason'] = 'promotion_candidate'
        b = copy.deepcopy(a)
        b['id'] = 'b'
        b['worker']['id'] = 'w2'
        b['strict_result']['receipt'] = 'proof-b'
        data['results'].append(b)
        out = summarize(data)
        self.assertEqual(out['strict_pass_results'], 2)
        self.assertEqual(len(out['strict_target_scopes']), 1)

    def test_clusters_preserve_domains_and_lineages(self):
        data = fixture()
        a = data['results'][0]
        a['blocker'] = {'signature': {'compiler_profile': 'profile', 'abi': 'near16',
            'analysis_level': 'source', 'mismatch_family': 'register', 'context_domain': 'isolated',
            'diagnostic_version': 'v1'}, 'evidence': ['synthetic:delta']}
        for ident, abi in [('b', 'near16'), ('c', 'far16')]:
            b = copy.deepcopy(a)
            b['id'] = ident
            b['worker']['id'] = ident
            b['blocker']['signature']['abi'] = abi
            data['results'].append(b)
        out = summarize(data)
        self.assertEqual(len(out['blocker_clusters']), 2)
        largest = max(out['blocker_clusters'], key=lambda c: len(c['result_ids']))
        self.assertEqual(len(largest['workers']), 2)
        self.assertEqual(len(largest['reported_lineages']), 1)
        self.assertEqual(largest['recurrence'], 'repeated_same_lineage')

    def test_cost_bases_and_unpriced_cost_remain_separate(self):
        data = fixture()
        data['costs'] += [{'id': 'c2', 'role': 'worker', 'amount': '9', 'unit': 'USD', 'basis': 'other-scenario'},
                          {'id': 'c3', 'role': 'review', 'amount': None, 'unit': 'USD', 'basis': 'synthetic-v1'}]
        out = summarize(data)
        self.assertEqual(len(out['costs']), 2)
        partial = next(c for c in out['costs'] if c['basis'] == 'synthetic-v1')
        self.assertFalse(partial['listed_items_priced'])
        self.assertEqual(partial['roles']['review']['unknown_items'], 1)

    def test_invalid_counter_token_and_nonfinite_cost_rejected(self):
        for field, value in [('counters', {'hypotheses': True}),
                             ('tokens', {'input': 3, 'cached_input': 4})]:
            data = fixture()
            data['results'][0][field] = value
            with self.assertRaises(ValueError):
                summarize(data)
        data = fixture()
        data['costs'][0]['amount'] = 'NaN'
        with self.assertRaises(ValueError):
            summarize(data)

    def test_malformed_accounting_and_nested_records_are_rejected(self):
        for field in ('strict_result', 'promotion', 'blocker'):
            data = fixture()
            data['results'][0][field] = []
            with self.assertRaises(ValueError):
                summarize(data)
        data = fixture()
        del data['costs'][0]['amount']
        with self.assertRaises(ValueError):
            summarize(data)


if __name__ == '__main__':
    unittest.main()
