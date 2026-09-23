"""Read-only Icy region evidence inventory; no compiler, source edit or proof.

This deliberately narrow adapter distinguishes merged-source line spans from
historical machine intervals. It does not equate those coordinate systems,
infer liveness, or treat an unobserved influence as no effect.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def interval_coverage(intervals, size):
    """Measure a half-open interval view without double-counting overlap."""
    if type(size) is not int or size < 0:
        raise ValueError('Invalid containing extent')
    spans = sorted(intervals)
    cursor = covered = overlapping = 0
    gaps = []
    for lo, hi in spans:
        if type(lo) is not int or type(hi) is not int or not 0 <= lo < hi <= size:
            raise ValueError('Interval outside containing extent')
        if lo > cursor:
            gaps.append([cursor, lo])
        overlapping += max(0, min(cursor, hi) - lo)
        covered += max(0, hi - max(cursor, lo))
        cursor = max(cursor, hi)
    if cursor < size:
        gaps.append([cursor, size])
    return {'covered_bytes': covered, 'overlap_bytes_counted_with_multiplicity': overlapping,
            'gaps': gaps, 'extent_bytes': size}


def source_regions(function, spans, line_count):
    rows = []
    prior_end = 0
    for span in spans.values():
        if not isinstance(span, list) or len(span) != 2 or any(type(n) is not int for n in span):
            raise ValueError('Expected inclusive integer source-line pair')
    for tag, span in sorted(spans.items(), key=lambda item: item[1][0]):
        if not isinstance(span, list) or len(span) != 2:
            raise ValueError('Expected inclusive source-line pair')
        lo, hi = span
        if type(lo) is not int or type(hi) is not int or not 1 <= lo <= hi <= line_count:
            raise ValueError('Source span outside retained merged body')
        if lo <= prior_end:
            raise ValueError('Merged-source edit spans overlap')
        prior_end = hi
        rows.append({'id': function + ':source:' + tag, 'tag': tag,
                     'coordinate': 'retained_merged_body_lines_inclusive',
                     'spans': [[lo, hi]], 'line_count': hi - lo + 1,
                     'machine_membership': None, 'live_ins': None, 'live_outs': None,
                     'entry_edges': None, 'exit_edges': None,
                     'diagnostic_state': 'REGION_UNRESOLVED'})
    return rows


def machine_regions(census):
    extent = census['historical_size']
    intervals = [(r['start_offset'], r['end_offset']) for r in census['regions']]
    coverage = interval_coverage(intervals, extent)
    calls = census['historical_callees']
    rows = []
    for index, region in enumerate(census['regions']):
        lo, hi = region['start_offset'], region['end_offset']
        sites = [c for c in calls if lo <= c['offset'] < hi]
        rows.append({'id': f'play:machine:{index:02}', 'label': region['label'],
                     'coordinate': 'original_function_byte_offsets_half_open',
                     'ranges': [[lo, hi]], 'bytes': hi - lo,
                     'call_site_count': len(sites),
                     'call_kinds': dict(Counter(c['kind'] for c in sites)),
                     'named_calls': sorted({c['name'] for c in sites if c.get('name')}),
                     'authority': 'retained_census_annotation_not_independent_CFG_proof'})
    return {'regions': rows, 'coverage': coverage,
            'call_kinds_from_json': dict(Counter(c['kind'] for c in calls)),
            'retained_census_candidate_size': census['current_size'],
            'candidate_size_scope': 'historical_census_baseline_not_current_report',
            'data_reference_count': len(census['data_references']),
            'reported_stack_slot_count': census['stack_frame']['distinct_ebp_slots_referenced'],
            'multi_named_slot_count': sum(len(s.get('dwarf_candidates', [])) > 1
                                          for s in census['stack_frame']['slots']),
            'slot_read_write_counts_are_liveness': False}


def inventory(root, observations, base_commit):
    if not re.fullmatch('[0-9a-f]{40}', base_commit):
        raise ValueError('Expected full observed base commit; source hashes still identify working-tree inputs')
    root = root.resolve()
    sources = []

    def read(relative, json_data=True):
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise ValueError('Input escapes declared repository')
        raw = path.read_bytes()
        sources.append({'id': f'icy-region-{len(sources):02}', 'repository': root.name,
                        'path': relative, 'content_kind': 'working_tree', 'ref': base_commit,
                        'sha256': hashlib.sha256(raw).hexdigest()})
        return json.loads(raw) if json_data else raw.decode('utf-8-sig')

    ledger = read('src/recovery.json')
    entry = ledger['src/main.c']
    report = read(entry['verified_report'])
    report_consistent = entry.get('verified_report_identity', {}).get('sha256') == sources[-1]['sha256']
    functions = []
    for name in ('play', 'draw_frame'):
        prefix = f'docs/attempts/game-main/{name}-merged.c'
        spans = read(prefix + '.regions.json')
        body = read(prefix, json_data=False)
        evidence = read(f'docs/current/function-evidence/main/{name}.json')
        function = next(f for f in report['functions'] if f['name'] == name)
        line_count = len(body.splitlines())
        try:
            regions = source_regions(name, spans, line_count)
            span_validation = {'status': 'in_bounds_only_not_identity_verified'}
        except ValueError as error:
            regions = None
            span_validation = {'status': 'invalid_for_observed_body', 'reason': str(error)}
        functions.append({'function': name,
                          'current_function_report': {k: function[k] for k in
                              ('original_size', 'candidate_size', 'status', 'source_body_sha256')},
                          'retained_merged_body_sha256': sources[-2]['sha256'],
                          'declared_source_spans': spans, 'body_line_count': line_count,
                          'source_regions': regions, 'source_span_validation': span_validation,
                          'source_span_freshness': 'unverified_sidecar_has_no_bound_body_hash',
                          'dwarf_lexical_blocks': len(evidence.get('lexical_blocks', [])),
                          'dwarf_locals': len(evidence.get('locals', [])),
                          'dwarf_regions_with_multiple_ranges': sum(
                              len([r for r in b.get('range_list', {}).get('entries', [])
                                   if r.get('kind') == 'range']) > 1
                              for b in evidence.get('lexical_blocks', []) if b.get('range_list')),
                          'historical_to_candidate_region_map': None})
    machine = machine_regions(read('docs/attempts/game-main/play-census.json'))
    if observations.get('format') != 'ai-decomp-region-observations-v1':
        raise ValueError('Unknown observation format')
    for observation in observations['observations']:
        if not observation.get('evidence') or not observation.get('limitations'):
            raise ValueError('An influence observation needs evidence and limitations')
    return {'format': 'ai-decomp-icy-region-inventory-v1', 'authority': 'research_inventory_only',
            'ledger_report_identity_equal': report_consistent, 'functions': functions,
            'play_machine_view': machine, 'reported_influences': observations['observations'],
            'unobserved_influence': 'unknown_not_zero', 'source_manifest': sources,
            'limitations': ['No compilation, source editing, liveness inference or promotion.',
                           'Historical machine chunks and merged-source regions are distinct views.',
                           'A source span does not establish an instruction set, SESE region or independent task.',
                           'Reported influences are curated evidence, not automatically inferred causes.',
                           'Equal byte budgets do not prove equal code; annotation/inlining can distort attribution.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--icy-root', type=Path, required=True)
    parser.add_argument('--observations', type=Path, required=True)
    parser.add_argument('--base-commit', required=True, help='Full observed base commit, not a claim that inputs are clean')
    args = parser.parse_args()
    try:
        result = inventory(args.icy_root, json.loads(args.observations.read_text(encoding='utf-8')), args.base_commit)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f'Cannot inventory region evidence: {error}\n')
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
