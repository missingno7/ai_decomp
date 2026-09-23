import copy
import unittest

from tools.experiment_matrix import matrix

def record(ident='a'):
    return {'id': ident, 'project': 'synthetic', 'target': 'f',
            'compiler_context': {'identity': 'fixture-context', 'flags': ['-O1']},
            'parent_candidate': None, 'hypothesis': 'fixture', 'prediction': 'same output',
            'falsifier': 'different output', 'changed_dimensions': ['spelling'],
            'compiler_process': {'status': 'success'},
            'effective_output_identity': {'algorithm': 'sha256', 'digest': 'a'*64,
                                           'scope': 'object+fixups', 'normalizer': 'none'},
            'structured_delta': {}, 'strict_result': {'status': 'not_run'},
            'facts_learned': [], 'stop_reason': 'continue', 'artifacts': []}

class MatrixTests(unittest.TestCase):
    def test_collapse_retains_individual_proof(self):
        a, b = record(), record('b')
        b['strict_result'] = {'status':'fail','scope':'member','verifier':'fixture','receipt':'fixture://failed'}
        result = matrix([a,b])
        self.assertEqual(result['effective_classes'], 1)
        self.assertTrue(result['clusters'][0]['strict_metadata_varies'])
        self.assertEqual(len(result['clusters'][0]['strict_results']), 2)

    def test_domains_never_coalesce(self):
        rows = [record()]
        for i, change in enumerate(('project','target','context','scope','normalizer')):
            r = record(str(i))
            if change in ('project','target'): r[change] = 'different'
            elif change == 'context': r['compiler_context']['flags'] = ['-O2']
            else: r['effective_output_identity'][change] = 'different'
            rows.append(r)
        self.assertEqual(matrix(rows)['effective_classes'], 6)

    def test_failures_and_unknown_outputs_are_not_classes(self):
        a,b = record(),record('b')
        for r in (a,b):
            r['effective_output_identity'] = None
            r['compiler_process']['status'] = 'failed'
        result = matrix([a,b])
        self.assertEqual(result['effective_classes'], 0)
        self.assertEqual(len(result['unclustered']), 2)

    def test_rejects_false_identity_and_unproven_pass(self):
        for mutation in ('failed','digest','proof','duplicate','false_accept','pass_without_compile','scope_type','receipt_type'):
            a = record()
            rows = [a]
            if mutation == 'failed': a['compiler_process']['status'] = 'failed'
            elif mutation == 'digest': a['effective_output_identity']['digest'] = 'close enough'
            elif mutation == 'proof': a['strict_result'] = {'status':'pass'}
            elif mutation == 'false_accept': a['stop_reason'] = 'accepted'
            elif mutation == 'pass_without_compile':
                a['compiler_process']['status'] = 'failed'
                a['effective_output_identity'] = None
                a['strict_result'] = {'status':'pass','scope':'member','verifier':'fixture','receipt':'fixture://pass'}
            elif mutation == 'scope_type': a['effective_output_identity']['scope'] = True
            elif mutation == 'receipt_type': a['strict_result'] = {'status':'pass','scope':'member','verifier':'fixture','receipt':True}
            else: rows.append(copy.deepcopy(a))
            with self.assertRaises(ValueError): matrix(rows)

if __name__ == '__main__': unittest.main()
