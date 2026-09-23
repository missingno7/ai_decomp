"""Validate the separate ecosystem index and pinned source-study records.

Offline metadata integrity only; never executes an upstream tool or grants proof.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    errors = []
    index = json.loads((root / 'catalog/ecosystem/index.json').read_text(encoding='utf-8'))
    tools = {}
    for path in (root / 'research/ecosystem').glob('*.json'):
        data = json.loads(path.read_text(encoding='utf-8'))
        if not data.get('checked_date'):
            errors.append(f'{path.name}: missing inspection date')
        for tool in data.get('tools', []):
            ident = tool['id']
            if ident in tools:
                errors.append(f'Duplicate external tool: {ident}')
            tools[ident] = (tool, path.relative_to(root).as_posix())
            for field in ('name', 'repository', 'license', 'capabilities', 'findings', 'reuse_decision'):
                if not tool.get(field):
                    errors.append(f'{ident}: missing {field}')
            if not re.fullmatch('[0-9a-f]{40}', tool.get('commit', '')):
                errors.append(f'{ident}: expected full inspected commit')
            for finding in tool.get('findings', []):
                if finding.get('epistemic_class') not in {
                    'EXTERNAL IMPLEMENTATION FACT', 'AUTHOR CLAIM', 'INFERENCE', 'UNKNOWN'
                }:
                    errors.append(f'{ident}: unclassified finding')
                if not finding.get('sources'):
                    errors.append(f'{ident}: unsourced finding')
                for source in finding.get('sources', []):
                    if not source.get('url', '').startswith('https://'):
                        local = (root / source.get('path', '')).resolve()
                        if not (finding.get('epistemic_class') == 'INFERENCE'
                                and local.is_relative_to(root.resolve()) and local.is_file()):
                            errors.append(f'{ident}: missing source URL or valid local inference reference')
                    if '/blob/' in source.get('url', '') and not re.search(
                        r'/blob/[0-9a-f]{40}/', source['url']
                    ):
                        errors.append(f'{ident}: unpinned code URL')
    indexed = set()
    for entry in index['tools']:
        ident = entry['id']
        if ident in indexed:
            errors.append(f'Duplicate external index ID: {ident}')
        indexed.add(ident)
        if ident not in tools:
            errors.append(f'{ident}: index references missing study record')
            continue
        tool, path = tools[ident]
        if entry['record_file'] != path or entry['commit'] != tool['commit']:
            errors.append(f'{ident}: index and authored study disagree')
    if indexed != set(tools):
        errors.append('External index does not cover all studied tools')
    for entry in index['studies']:
        for field in ('document', 'records'):
            path = (root / entry[field]).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                errors.append(f'Missing or escaping ecosystem {field}: {entry[field]}')
    return errors


if __name__ == '__main__':
    result = check()
    print(json.dumps({'authority': 'metadata_integrity_only', 'errors': result}, indent=2))
    raise SystemExit(bool(result))
