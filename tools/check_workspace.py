"""Check catalog references, local Markdown links and synthetic experiment data."""
import json
import re
from pathlib import Path
from experiment_matrix import validate

ROOT=Path(__file__).resolve().parents[1]

def main():
    errors=[]
    catalogs={p.stem:json.loads(p.read_text(encoding='utf-8')) for p in (ROOT/'catalog').glob('*.json')}
    sources={s['id'] for s in catalogs['sources']}
    ids={kind:{r['id'] for r in rows} for kind,rows in catalogs.items()}
    for kind,rows in catalogs.items():
        if len(ids[kind])!=len(rows): errors.append(f'Duplicate IDs in {kind}')
        for row in rows:
            for ref in row.get('sources',[]):
                if ref['source_id'] not in sources: errors.append(f'{row["id"]}: dangling source')
            for field,target in [('related_tools','tools'),('related_trajectories','trajectories'),('mechanisms','mechanisms')]:
                for ident in row.get(field,[]):
                    if ident not in ids[target]: errors.append(f'{row["id"]}: dangling {ident}')
            if kind in ('mechanisms','trajectories','negative-evidence','tools') and not row.get('sources'):
                errors.append(f'{row["id"]}: missing sources')
    for path in ROOT.rglob('*.md'):
        if any(part in {'.git', '.research-cache', '__pycache__'} for part in path.relative_to(ROOT).parts):
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',path.read_text(encoding='utf-8-sig')):
            if re.match(r'^[a-zA-Z]+://',target) or target.startswith('#'): continue
            file=target.split('#')[0].strip('<>')
            if file and not (path.parent/file).exists(): errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
    for path in (ROOT/'experiments/examples').glob('*.json'):
        validate(json.loads(path.read_text(encoding='utf-8')))
    ecosystem_path=ROOT/'catalog/ecosystem/index.json'
    if ecosystem_path.exists():
        from check_ecosystem import check
        errors.extend(check(ROOT))
    print(json.dumps({'catalog_counts':{k:len(v) for k,v in catalogs.items()},'errors':errors},indent=2))
    raise SystemExit(bool(errors))

if __name__=='__main__': main()
