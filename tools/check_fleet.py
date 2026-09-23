"""Workspace-specific offline checks for the fleet study and archived replay."""
from collections import Counter
import hashlib
import json
from pathlib import Path

from fleet_report import canonical, summarize

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    errors = []

    def read(path):
        return json.loads((root / path).read_text(encoding='utf-8'))

    index = read('catalog/fleet/index.json')
    for entry in index['studies'] + index['censuses']:
        record = read(entry['record'])
        for source in record[entry['source_field']]:
            if len(source['sha256']) != 64 or (source['content_kind'] == 'git_blob' and len(source['ref']) != 40):
                errors.append(f'{entry["id"]}: incomplete source identity')
        if 'document' in entry and not (root / entry['document']).is_file():
            errors.append(f'{entry["id"]}: missing document')
    for artifact in index['artifacts']:
        if not (root / artifact).is_file():
            errors.append(f'Missing fleet artifact: {artifact}')

    simant = read('research/fleet/simant-job-census.json')
    rows = simant['rows']
    aggregate = simant['aggregate']
    digest = hashlib.sha256(json.dumps(rows, ensure_ascii=False,
                                     separators=(',', ':')).encode()).hexdigest()
    if digest != simant['rows_sha256']:
        errors.append('SimAnt sanitized census row hash differs')
    promoted = [r for r in rows if r['status'] == 'PROMOTED']
    expected = {'jobs': len(rows), 'status_counts': dict(Counter(r['status'] for r in rows)),
                'recorded_attempts': sum(r['attempt_count'] for r in rows),
                'promoted': len(promoted),
                'promoted_after_first_attempt': sum(r['attempt_count'] > 1 for r in promoted),
                'maximum_promoted_attempts': max(r['attempt_count'] for r in promoted)}
    for key, value in expected.items():
        if aggregate[key] != value:
            errors.append(f'SimAnt census aggregate differs: {key}')

    icy = read('research/fleet/icy-mechanical-census.json')
    outcomes = [outcome for source in icy['source_manifest'] for outcome in source['outcomes']]
    expected = {'summary_count': len(icy['source_manifest']), 'outcome_count': len(outcomes),
                'state_counts': dict(Counter(o['state'] for o in outcomes)),
                'kind_counts': dict(Counter(o['kind'] for o in outcomes)),
                'outcomes_missing_kind': sum(not o.get('kind') for o in outcomes)}
    if expected != icy['aggregation']:
        errors.append('Icy census aggregates differ from retained outcomes')

    replay = read('research/fleet/stunts-replay.json')
    source_path = root / 'research/fleet/stunts.json'
    source = json.loads(source_path.read_text(encoding='utf-8'))
    if replay.get('source_extraction_hash_kind') != 'canonical-json-v1':
        errors.append('Stunts replay needs a named metadata hash contract')
    if hashlib.sha256(canonical(source).encode()).hexdigest() != replay['source_extraction_sha256']:
        errors.append('Stunts replay source extraction hash differs')
    summary = summarize(replay)
    if summary != read('research/fleet/stunts-replay-summary.json'):
        errors.append('Saved Stunts fleet summary differs from current reducer')
    source = read('research/fleet/stunts.json')['matched_cohort']
    comparisons = [
        (summary['results'], source['matched_run_count']),
        (summary['strict_pass_results'], source['strict_success_run_count']),
        (summary['counters']['hypotheses']['known_sum'], source['sum_hypothesis_count']),
        (summary['counters']['model_requests']['known_sum'], source['sum_request_count']),
        (summary['counters']['compiler_processes']['known_sum'], source['sum_compiler_processes'])]
    if any(left != right for left, right in comparisons):
        errors.append('Stunts replay counts disagree with raw-derived extraction')
    return errors


if __name__ == '__main__':
    found = check()
    print(json.dumps({'authority': 'offline_metadata_integrity_only', 'errors': found}, indent=2))
    raise SystemExit(bool(found))
