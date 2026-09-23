"""Validate retained adversarial metadata; no sibling access or proof inference."""
from collections import Counter
import json
from pathlib import Path
import re
import statistics


def check(root):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def read(relative):
        return json.loads((root / relative).read_text(encoding='utf-8'))

    index = read('catalog/adversarial/index.json')
    for path in index['artifacts']:
        require((root / path).is_file(), 'Missing adversarial artifact: ' + path)
    for item in index['records']:
        record = read(item['path'])
        sources = record['source_manifest']
        require(len({s['id'] for s in sources}) == len(sources), item['path'] + ': duplicate source ID')
        for source in sources:
            require(bool(re.fullmatch('[0-9a-f]{64}', source['sha256'])), source['id'] + ': invalid SHA256')
            require(bool(re.fullmatch('[0-9a-f]{40}', source['ref'])), source['id'] + ': missing full base/commit')
            require(source['content_kind'] in ('git_blob', 'working_tree'), source['id'] + ': unknown provenance kind')

    census = read('research/adversarial/icy-function-census.json')
    rows, total = census['rows'], census['aggregate']
    require(len({r['va'] for r in rows}) == len(rows), 'Icy: duplicate function VA')
    require(len(rows) == total['functions'], 'Icy: function denominator mismatch')
    require(sum(r['original_size'] for r in rows) == total['original_bytes'], 'Icy: byte denominator mismatch')
    require(dict(Counter(r['status'] for r in rows)) == total['status_counts'], 'Icy: status totals mismatch')
    for key, exact in [('matched', True), ('nonexact', False)]:
        sizes = [r['original_size'] for r in rows if (r['status'] == 'FUNCTION_MATCH') == exact]
        expected = total[key]
        require((len(sizes), sum(sizes), statistics.mean(sizes), statistics.median(sizes)) ==
                (expected['functions'], expected['bytes'], expected['mean_size'], expected['median_size']),
                'Icy: ' + key + ' distribution mismatch')
    sizes = sorted((r['original_size'] for r in rows if r['status'] != 'FUNCTION_MATCH'), reverse=True)
    for n, result in total['unresolved_concentration'].items():
        require(sum(sizes[:int(n)]) == result['bytes'], 'Icy: concentration mismatch')
    require(all(r['ledger_hash_matches_observed'] for r in census['report_references']),
            'Icy: census did not capture ledger-consistent reports')

    stunts = read('research/adversarial/stunts.json')
    rows, metrics = stunts['census_rows'], stunts['metrics']
    require(len(rows) == metrics['census_count'], 'Stunts: census count mismatch')
    require(len({r['id'] for r in rows}) == len(rows), 'Stunts: duplicate target')
    require(dict(Counter(r['boundary_status'] for r in rows)) == metrics['boundary_states'],
            'Stunts: boundary counts mismatch')
    categories = Counter(c for r in rows for c in r['categories'])
    require(dict(categories) == {k: v['tasks'] for k, v in metrics['overlapping_category_counts'].items()},
            'Stunts: overlapping category counts mismatch')
    require(sum(len(r['categories']) > 1 for r in rows) == metrics['multiple_categories_count'],
            'Stunts: multi-category count mismatch')

    inventory = read('research/adversarial/region-inventory.json')
    observations = read('research/adversarial/region-observations.json')
    require(inventory['reported_influences'] == observations['observations'], 'Region observations differ from inventory')
    known = {s['id'] for s in observations['source_manifest']}
    require(all(set(o['evidence']) <= known for o in observations['observations']), 'Region influence has unknown source')
    require(inventory['unobserved_influence'] == 'unknown_not_zero', 'Region unknown influence lost')
    for function in inventory['functions']:
        require(function['historical_to_candidate_region_map'] is None, 'Unproven region map introduced')
        if function['source_span_validation']['status'] == 'invalid_for_observed_body':
            require(function['source_regions'] is None, 'Invalid region sidecar was treated as a mapping')
    coverage = inventory['play_machine_view']['coverage']
    require(coverage['covered_bytes'] == 17420 and not coverage['gaps'] and
            coverage['overlap_bytes_counted_with_multiplicity'] == 0, 'Historical play region coverage changed')
    require(sum(r['bytes'] for r in inventory['play_machine_view']['regions']) == coverage['covered_bytes'],
            'Historical play region totals mismatch')
    require(all(re.fullmatch('[0-9a-f]{40}', s['commit']) for s in
                read('research/adversarial/historical-replay.json')['snapshots']), 'Replay commit not immutable')
    return errors


if __name__ == '__main__':
    problems = check(Path(__file__).resolve().parents[1])
    print(json.dumps({'authority': 'retained_metadata_consistency_only', 'errors': problems}, indent=2))
    raise SystemExit(bool(problems))
