"""Validate and cluster exported experiment metadata. Never compiles or grants proof.

Original stdlib implementation for ai_decomp; no upstream source copied.
Identity semantics belong to the exporting project, not this analysis layer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

REQUIRED = {
    'id', 'project', 'target', 'compiler_context', 'parent_candidate', 'hypothesis',
    'prediction', 'falsifier', 'changed_dimensions', 'compiler_process',
    'effective_output_identity', 'structured_delta', 'strict_result', 'facts_learned',
    'stop_reason', 'artifacts',
}
STOP_REASONS = {'accepted', 'budget_censored', 'search_converged', 'tooling_blocked',
                'evidence_blocked', 'hypothesis_rejected', 'continue', 'unknown'}

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)

def validate(rows):
    if not isinstance(rows, list):
        raise ValueError('Input must be a JSON array of experiment records')
    seen = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f'Row {index}: expected an object')
        missing = REQUIRED - row.keys()
        if missing:
            raise ValueError(f'Row {index}: missing {sorted(missing)}')
        for field in ('id', 'project', 'target', 'hypothesis', 'prediction', 'falsifier'):
            if not isinstance(row[field], str) or not row[field].strip():
                raise ValueError(f'Row {index}: {field} must be nonempty text')
        if row['id'] in seen:
            raise ValueError(f'Duplicate experiment ID: {row["id"]}')
        seen.add(row['id'])
        for field in ('changed_dimensions', 'facts_learned', 'artifacts'):
            if not isinstance(row[field], list):
                raise ValueError(f'{row["id"]}: {field} must be an array')
        for field in ('compiler_context', 'compiler_process', 'structured_delta', 'strict_result'):
            if not isinstance(row[field], dict):
                raise ValueError(f'{row["id"]}: {field} must be an object')
        context = row['compiler_context']
        if not isinstance(context.get('identity'), str) or not context['identity'].strip():
            raise ValueError(f'{row["id"]}: missing compiler context identity')
        if row['parent_candidate'] is not None and not isinstance(row['parent_candidate'], str):
            raise ValueError(f'{row["id"]}: parent_candidate must be text or null')
        process = row['compiler_process']
        if process.get('status') not in ('success', 'failed', 'not_run', 'unknown'):
            raise ValueError(f'{row["id"]}: invalid compiler status')
        strict = row['strict_result']
        if strict.get('status') not in ('pass', 'fail', 'not_run', 'unknown'):
            raise ValueError(f'{row["id"]}: invalid strict status')
        if strict['status'] in ('pass', 'fail') and not all(isinstance(strict.get(k),str) and strict[k].strip() for k in ('scope', 'verifier', 'receipt')):
            raise ValueError(f'{row["id"]}: strict result needs scope, verifier and receipt')
        if row['stop_reason'] not in STOP_REASONS:
            raise ValueError(f'{row["id"]}: invalid stop reason')
        identity = row['effective_output_identity']
        if strict['status'] == 'pass' and (process['status'] != 'success' or identity is None):
            raise ValueError(f'{row["id"]}: strict pass requires successful compilation and output identity')
        if row['stop_reason'] == 'accepted' and strict['status'] != 'pass':
            raise ValueError(f'{row["id"]}: accepted stop requires strict pass')
        if identity is not None:
            if process['status'] != 'success':
                raise ValueError(f'{row["id"]}: output identity requires successful compilation')
            if not isinstance(identity, dict) or not all(isinstance(identity.get(k),str) and identity[k].strip() for k in ('algorithm', 'digest', 'scope', 'normalizer')):
                raise ValueError(f'{row["id"]}: incomplete output identity')
            if identity['algorithm'] != 'sha256' or not re.fullmatch('[0-9a-f]{64}', identity['digest']):
                raise ValueError(f'{row["id"]}: expected lowercase SHA256 output identity')
        canonical(row)  # Also rejects nonfinite values.
    return rows

def matrix(rows):
    """Group only comparable successful outputs; unknowns/errors stay separate."""
    validate(rows)
    groups = defaultdict(list)
    unclustered = []
    for row in rows:
        identity = row['effective_output_identity']
        if identity is None:
            unclustered.append({'id': row['id'], 'compiler_status': row['compiler_process']['status'],
                                'reason': 'No output identity; no equivalence inferred'})
            continue
        key = canonical({'project': row['project'], 'target': row['target'],
                         'context': row['compiler_context'], 'identity': identity})
        groups[key].append(row)
    clusters = []
    for key, members in sorted(groups.items()):
        strict = [m['strict_result'] for m in members]
        clusters.append({'cluster_id': hashlib.sha256(key.encode()).hexdigest(),
                         'comparison_domain': json.loads(key), 'experiments': [m['id'] for m in members],
                         'source_trials': len(members), 'strict_results': strict,
                         'strict_metadata_varies': len({canonical(s) for s in strict}) > 1,
                         'deltas': {m['id']: m['structured_delta'] for m in members}})
    return {'format': 'ai-decomp-outcome-matrix-v1', 'authority': 'analysis_only',
            'experiments': len(rows), 'identified_outputs': sum(len(g) for g in groups.values()),
            'effective_classes': len(clusters), 'clusters': clusters, 'unclustered': unclustered,
            'limitation': 'Equal identity means equal exported output under this scope; never equal semantics or strict acceptance.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    try:
        rows = json.loads(args.input.read_text(encoding='utf-8'))
        result = {'valid': True, 'experiments': len(validate(rows))} if args.validate_only else matrix(rows)
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, f'Invalid experiment input: {exc}\n')
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
