"""Summarize exported bounded-worker results; never schedules, compiles or promotes.

Original stdlib metadata reducer. Claimed receipts and blocker classifications
remain the exporting project's responsibility. Equal signatures suggest review,
not a proven shared compiler mechanism or independent replication.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path

FORMAT = 'ai-decomp-fleet-results-v1'
STOPS = {'accepted', 'promotion_candidate', 'search_converged', 'budget_censored',
         'tooling_blocked', 'evidence_blocked', 'production_blocked',
         'systemic_mechanism_suspected', 'interrupted', 'cancelled_redundant', 'unknown'}
COUNTERS = ('hypotheses', 'model_requests', 'reasoning_rounds', 'compiler_processes',
            'unique_effective_outputs', 'information_experiments')
TOKENS = ('input', 'cached_input', 'output', 'reasoning_output')
SIGNATURE = ('compiler_profile', 'abi', 'analysis_level', 'mismatch_family',
             'context_domain', 'diagnostic_version')


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def require_text(data, keys):
    if not isinstance(data, dict):
        raise ValueError('Expected an object')
    for key in keys:
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'Missing nonempty {key}')


def nullable_counts(data, keys):
    if not isinstance(data, dict):
        raise ValueError('Expected counter object')
    for key in keys:
        value = data.get(key)
        if value is not None and (type(value) is not int or value < 0):
            raise ValueError(f'{key}: expected nonnegative integer or null')


def unique_records(rows, label):
    seen = {}
    for row in rows:
        require_text(row, ('id',))
        if row['id'] in seen and canonical(seen[row['id']]) != canonical(row):
            raise ValueError(f'Conflicting {label} ID: {row["id"]}')
        seen[row['id']] = row
    return list(seen.values())


def validate(data):
    canonical(data)  # Reject nonfinite numbers, including in extension fields.
    if not isinstance(data, dict) or data.get('format') != FORMAT:
        raise ValueError(f'Expected format {FORMAT}')
    require_text(data, ('run_id',))
    if not isinstance(data.get('results'), list) or not isinstance(data.get('costs'), list):
        raise ValueError('results and costs must be arrays')
    rows = unique_records(data['results'], 'result')
    for row in rows:
        require_text(row, ('analysis_level',))
        require_text(row.get('task'), ('project', 'target', 'seed_id', 'context_id'))
        require_text(row.get('worker'), ('id', 'lineage_id', 'model', 'effort'))
        if row.get('stop_reason') not in STOPS:
            raise ValueError(f'{row["id"]}: invalid stop reason')
        strict = row.get('strict_result', {})
        if not isinstance(strict, dict):
            raise ValueError('strict_result must be an object')
        if strict.get('status') not in {'pass', 'fail', 'not_run', 'unknown'}:
            raise ValueError('Invalid strict status')
        if strict['status'] in {'pass', 'fail'}:
            require_text(strict, ('scope', 'verifier', 'receipt'))
        promotion = row.get('promotion', {})
        if not isinstance(promotion, dict):
            raise ValueError('promotion must be an object')
        if promotion.get('status') not in {'not_requested', 'candidate', 'queued', 'promoted', 'blocked', 'unknown'}:
            raise ValueError('Invalid promotion status')
        if row['stop_reason'] in {'accepted', 'promotion_candidate'} or promotion['status'] in {'candidate', 'queued', 'promoted'}:
            if strict['status'] != 'pass':
                raise ValueError('Exact candidate/promotion requires scoped strict pass')
        if row['stop_reason'] == 'accepted' and promotion['status'] != 'promoted':
            raise ValueError('accepted requires native promotion, not just a candidate')
        if promotion['status'] == 'promoted':
            require_text(promotion, ('receipt',))
            if promotion['receipt'] == strict['receipt']:
                raise ValueError('Use distinct verifier/promotion record references (or distinct bundle anchors)')
        nullable_counts(row.get('counters', {}), COUNTERS)
        tokens = row.get('tokens', {})
        nullable_counts(tokens, TOKENS)
        for subset, total in [('cached_input', 'input'), ('reasoning_output', 'output')]:
            if tokens.get(subset) is not None and tokens.get(total) is not None and tokens[subset] > tokens[total]:
                raise ValueError(f'{subset} must be a subset of {total}')
        if not isinstance(row.get('artifacts'), list) or not row['artifacts']:
            raise ValueError('A result needs artifact references')
        blocker = row.get('blocker')
        if row['stop_reason'] == 'systemic_mechanism_suspected' and blocker is None:
            raise ValueError('Systemic suspicion needs a scoped blocker signature')
        if blocker is not None:
            if not isinstance(blocker, dict):
                raise ValueError('blocker must be an object or null')
            require_text(blocker.get('signature'), SIGNATURE)
            if blocker['signature']['analysis_level'] != row['analysis_level']:
                raise ValueError('Blocker and result analysis levels disagree')
            if not isinstance(blocker.get('evidence'), list) or not blocker['evidence']:
                raise ValueError('A suspected blocker needs evidence references')
    costs = unique_records(data['costs'], 'cost')
    for cost in costs:
        require_text(cost, ('role', 'unit', 'basis'))
        if cost['role'] not in {'worker', 'supervisor', 'preparation', 'review', 'infrastructure'}:
            raise ValueError('Invalid accounting role')
        if 'amount' not in cost:
            raise ValueError('Cost needs an amount or explicit null')
        amount = cost.get('amount')
        if amount is not None:
            if isinstance(amount, bool):
                raise ValueError('Invalid cost amount')
            try:
                number = Decimal(str(amount))
            except InvalidOperation as error:
                raise ValueError('Invalid cost amount') from error
            if not number.is_finite() or number < 0:
                raise ValueError('Cost must be nonnegative and finite')
        result_ids = cost.get('result_ids', [])
        if not isinstance(result_ids, list) or any(ident not in {r['id'] for r in rows} for ident in result_ids):
            raise ValueError('Cost references unknown result')
    return rows, costs


def coverage_sum(rows, field, key):
    values = [r.get(field, {}).get(key) for r in rows]
    return {'known_sum': sum(v for v in values if v is not None),
            'known_results': sum(v is not None for v in values),
            'unknown_results': sum(v is None for v in values)}


def summarize(data):
    rows, costs = validate(data)
    groups = defaultdict(list)
    for row in rows:
        if row.get('blocker') is not None:
            groups[canonical({'project': row['task']['project'],
                              'signature': row['blocker']['signature']})].append(row)
    clusters = []
    for key, members in sorted(groups.items()):
        lineages = sorted({m['worker']['lineage_id'] for m in members})
        recurrence = ('single_report' if len(members) == 1 else
                      'repeated_same_lineage' if len(lineages) == 1 else
                      'cross_lineage_reports_independence_unverified')
        clusters.append({'domain': json.loads(key), 'result_ids': [m['id'] for m in members],
                         'targets': sorted({m['task']['target'] for m in members}),
                         'workers': sorted({m['worker']['id'] for m in members}),
                         'reported_lineages': lineages,
                         'seeds': sorted({m['task']['seed_id'] for m in members}),
                         'report_count': len(members), 'lineage_count': len(lineages),
                         'recurrence': recurrence,
                         'evidence': [e for m in members for e in m['blocker']['evidence']],
                         'authority': 'suspected_recurrence_not_proven_mechanism'})
    accounting = defaultdict(list)
    for cost in costs:
        accounting[(cost['basis'], cost['unit'])].append(cost)
    cost_summary = []
    for (basis, unit), entries in sorted(accounting.items()):
        by_role = {}
        for role in sorted({e['role'] for e in entries}):
            selected = [e for e in entries if e['role'] == role]
            by_role[role] = {'known_amount': str(sum((Decimal(str(e['amount'])) for e in selected if e.get('amount') is not None), Decimal(0))),
                             'unknown_items': sum(e.get('amount') is None for e in selected)}
        cost_summary.append({'basis': basis, 'unit': unit, 'roles': by_role,
                             'listed_items_priced': all(e.get('amount') is not None for e in entries),
                             'unreported_roles': sorted({'worker', 'supervisor', 'preparation', 'review', 'infrastructure'} - set(by_role))})
    strict = [r for r in rows if r['strict_result']['status'] == 'pass']
    # Repeated replicas remain separate results but do not multiply target wins.
    strict_targets = sorted({(r['task']['project'], r['task']['target'],
                             r['task']['context_id'], r['strict_result']['scope']) for r in strict})
    transactions = sorted({(r['task']['project'], r['promotion']['receipt'])
                           for r in rows if r['promotion']['status'] == 'promoted'})
    return {'format': 'ai-decomp-fleet-summary-v1', 'run_id': data['run_id'],
            'authority': 'metadata_summary_only',
            'results': len(rows), 'duplicate_result_records_ignored': len(data['results']) - len(rows),
            'duplicate_cost_records_ignored': len(data['costs']) - len(costs),
            'workers': len({r['worker']['id'] for r in rows}),
            'targets': len({(r['task']['project'], r['task']['target']) for r in rows}),
            'stops': dict(sorted(Counter(r['stop_reason'] for r in rows).items())),
            'strict_pass_results': len(strict), 'strict_target_scopes': [list(t) for t in strict_targets],
            'strict_statuses': dict(sorted(Counter(r['strict_result']['status'] for r in rows).items())),
            'promotions': dict(sorted(Counter(r['promotion']['status'] for r in rows).items())),
            'distinct_reported_promotion_transactions': [list(t) for t in transactions],
            'counters': {key: coverage_sum(rows, 'counters', key) for key in COUNTERS},
            'tokens': {key: coverage_sum(rows, 'tokens', key) for key in TOKENS},
            'costs': cost_summary, 'blocker_clusters': clusters,
            'limitations': ['Receipts, independence and blocker classifications are not verified here.',
                            'Unique-output counter sum is within-result work, not cross-result novelty.',
                            'Reasoning tokens are a subset of output; cached input is a subset of input.',
                            'Cost bases are never combined; absent cost items are not known zero costs.',
                            'No scheduling, automatic escalation or production mutation.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    try:
        result = summarize(json.loads(args.input.read_text(encoding='utf-8')))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f'Invalid fleet metadata: {error}\n')
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
