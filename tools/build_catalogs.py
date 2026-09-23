"""Normalize the four authored research extracts without flattening their claims.

Read-only access to siblings; writes derived catalogs and reference pages here.
This is a workspace-specific importer, not a proposed universal adapter API.
"""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOS = {'empires':'empires_reconstruction','stunts':'stunts_recon',
         'simantw':'simantw_recon','icytower':'icytower_recon'}

def dump(path, value):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def git(repo, *args):
    return subprocess.check_output(['git','-c',f'safe.directory={repo.as_posix()}',
                                   '-C',str(repo),*args], stderr=subprocess.PIPE)

def split_source(value):
    if isinstance(value, dict): return copy.deepcopy(value)
    match = re.match(r'^(.*?)(?:#L|:)(\d+(?:-L?\d+)?(?:,\d+(?:-L?\d+)?)*)$', value)
    return {'path':match[1],'anchor':match[2]} if match else {'path':value}

def source_nodes(node):
    if isinstance(node, dict):
        if 'path' in node and ('ref' in node or 'sha256' in node): yield node
        for value in node.values(): yield from source_nodes(value)
    elif isinstance(node, list):
        for value in node: yield from source_nodes(value)

def main():
    catalogs = {k:[] for k in ('projects','mechanisms','trajectories','negative-evidence','tools')}
    all_sources = {}
    for project, repo_name in REPOS.items():
        repo = ROOT.parent / repo_name
        data = json.loads((ROOT/'research'/project/'records.json').read_text(encoding='utf-8-sig'))
        p = data['project']
        head = p['head']
        default_ref = p.get('evidence_ref',head)
        manifests = {}
        for node in source_nodes(data): manifests.setdefault(node['path'],copy.deepcopy(node))

        def resolve(value):
            citation = split_source(value)
            path = citation['path']
            meta = dict(manifests.get(path,{}), **citation)
            state = meta.get('state','')
            working = meta.get('working_tree',False) or meta.get('ref') == 'working-tree' or state in ('modified_worktree','untracked_worktree') or 'untracked' in state
            ref = 'working-tree' if working else meta.get('ref', default_ref)
            if ref == 'HEAD': ref = head
            # Missing manifest entry (usually a tool) is attributed by actual status.
            if path not in manifests and 'ref' not in citation:
                dirty = git(repo,'status','--porcelain','--untracked-files=all','--',path).strip()
                working = bool(dirty)
                ref = 'working-tree' if working else default_ref
            key = (project,path,ref)
            ident = project+'-src-'+hashlib.sha256((path+'@'+ref).encode()).hexdigest()[:12]
            if key not in all_sources:
                claimed = meta.get('sha256')
                # A snapshot's stored hash survives later changes or deletion.
                # Verification of present availability belongs to provenance_check.
                blob = b'' if working and claimed else ((repo/path).read_bytes() if working else git(repo,'show',f'{ref}:{path}'))
                digest = claimed if working and claimed else hashlib.sha256(blob).hexdigest()
                if not working and claimed and claimed != digest:
                    lf = blob.replace(b'\r\n',b'\n')
                    newline_hashes = {hashlib.sha256(lf).hexdigest(),hashlib.sha256(lf.replace(b'\n',b'\r\n')).hexdigest()}
                    if claimed not in newline_hashes:
                        live=(repo/path).read_bytes()
                        if hashlib.sha256(live).hexdigest()!=claimed or live.replace(b'\r\n',b'\n')!=lf:
                            raise ValueError(f'Claimed clean evidence differs from Git blob beyond line endings: {project}/{path}')
                # Active sibling agents may change files while this importer runs.
                # Keep the inspected identity; the checker reports later drift.
                all_sources[key] = dict(id=ident, project=project, repository=repo_name,
                    path=path, ref=ref, base_commit=head if working else ref,
                    content_kind='working_tree' if working else 'git_blob', sha256=digest,
                    inspected_worktree_sha256=claimed if claimed and claimed != digest else None,
                    retention='Hash identifies but does not archive uncommitted content' if working else 'Retrieve with git show <ref>:<path>')
            return {'source_id':ident, 'anchor':meta.get('anchor',meta.get('anchors'))}

        # Retain inventory sources even when not cited by a particular mechanism.
        for path, meta in manifests.items(): resolve(meta)
        project_record = copy.deepcopy(p)
        project_record.update(id=project,repository=repo_name,dossier=f'research/{project}/dossier.md',
                              snapshot_date='2026-09-23')
        project_record['sources'] = [resolve(m) for m in manifests.values()]
        catalogs['projects'].append(project_record)
        for category, source_category in [('mechanisms','mechanisms'),('trajectories','trajectories'),
                                          ('negative-evidence','negatives'),('tools','tools')]:
            for index, raw in enumerate(data[source_category]):
                row = copy.deepcopy(raw)
                original_id = row.get('id', Path(row.get('path',str(index))).stem)
                ident = original_id if original_id.startswith(project+'-') else project+'-'+original_id.replace('_','-')
                cited = row.get('sources',row.get('evidence',[]))
                if not cited and category == 'tools':
                    cited = [{'path':part.strip()} for part in row['path'].split('+')]
                sources = [resolve(s) for s in cited]
                kind = row.get('epistemic_class',row.get('claim_kind',row.get('kind','PROJECT FACT')))
                kinds = kind if isinstance(kind,list) else [kind]
                kinds = [k.replace('_',' ') for k in kinds]
                # A mechanism with a portable diagnostic still records a scoped observation.
                epistemic = 'PROJECT FACT' if 'PROJECT FACT' in kinds else kinds[0]
                row.update(id=ident,project=project,epistemic_class=epistemic,sources=sources,
                           dossier=f'research/{project}/dossier.md',original_record_id=original_id)
                row.pop('evidence',None)
                if category == 'tools':
                    row['reuse'] = row.get('reuse',row.get('reuse_classification',row.get('classification')))
                    if project == 'stunts' and row['path'] == 'tools/coordinates.py':
                        row['reuse'] = 'adapter_required'
                        row['synthesis_note'] = 'Checked conversions are generic in concept; concrete spaces and common.require make the existing script adapter-dependent.'
                catalogs[category].append(row)
    # Curated navigation links preserve the project-specific mechanism distinctions.
    tool_ids = {t['id'] for t in catalogs['tools']}
    trajectory_map = {
        'empires-route-context':['empires-game-tu'],
        'empires-ordered-relocations':['empires-music','empires-final-freeze'],
        'empires-tu-constraints':['empires-game-tu'],
        'empires-asm-provenance':['empires-negation'],
        'empires-fresh-acceptance':['empires-final-freeze'],
        'simantw-effective-output-collapse':['simantw-flood-nest-mapb-effective-output-failure'],
        'simantw-msc7-declaration-order':['simantw-magnify-menu-local-order-success','simantw-flood-nest-mapb-effective-output-failure'],
        'simantw-complete-member-proof':['simantw-draw-for-sale-sequential-private-state-success'],
        'simantw-selector-pool-and-pointer-evidence':['simantw-draw-for-sale-sequential-private-state-success'],
        'simantw-scaffolded-unit-assembly':[],
        'stunts-hybrid-proof-separation':['stunts-matched-luna-astra-routing'],
        'stunts-effective-output-convergence':['stunts-unknown-libname-batch-v-sequential'],
        'stunts-candidate-pair-diagnostics':['stunts-camera-declaration-and-return-negative'],
        'stunts-mismatch-islands-with-contradictions':['stunts-camera-declaration-and-return-negative'],
        'stunts-capability-and-binding-boundaries':['stunts-matched-luna-astra-routing'],
        'icytower-dwarf-source-structure':['icytower-localfilename-scope'],
        'icytower-historical-definition-order':['icytower-scroller-order'],
        'icytower-predecessor-context-dependency':['icytower-scroller-order','icytower-draw-frame-predecessor'],
        'icytower-pass-stage-convergence':['icytower-play-pass-stage-convergence'],
        'icytower-body-layout-neighbor-separation':['icytower-localfilename-scope'],
    }
    for row in catalogs['mechanisms']:
        original_tools = row.get('related_tools',row.get('tool_ids',[]))
        row['related_tool_names'] = original_tools
        candidates = [t if t in tool_ids else row['project']+'-'+t.replace('_','-') for t in original_tools]
        row['related_tools'] = [t for t in candidates if t in tool_ids]
        if not row['related_tools']:
            # Same-source links are safe; do not invent equivalent tools by keyword.
            cited={s['source_id'] for s in row['sources']}
            row['related_tools']=[t['id'] for t in catalogs['tools'] if t['project']==row['project'] and cited.intersection(s['source_id'] for s in t['sources'])]
        row['related_trajectories']=trajectory_map.get(row['id'],[])
    for row in catalogs['trajectories']:
        row['mechanisms']=[m['id'] for m in catalogs['mechanisms'] if row['id'] in m['related_trajectories']]
    for key, rows in catalogs.items(): dump(f'catalog/{key}.json',rows)
    dump('catalog/sources.json',list(all_sources.values()))
    source_by_id={s['id']:s for s in all_sources.values()}
    source_lines=['# Source index','',
        'These identities pin the inspected evidence. A local-file link opens the current file and may differ from the cited snapshot.',
        'For immutable content use the stated commit with `git show COMMIT:path` in the named sibling repository.',
        'Working-tree hashes identify observations but do not archive their contents.','']
    for source in all_sources.values():
        source_lines += [f'## {source["id"]}', '',
            f'**Repository:** `{source["repository"]}`', '', f'**Path:** `{source["path"]}`', '',
            f'**Ref:** `{source["ref"]}`; base commit `{source["base_commit"]}`', '',
            f'**Content:** {source["content_kind"]}; SHA-256 `{source["sha256"]}`', '',
            f'[Current local file (may differ)](../../{source["repository"]}/{source["path"]})', '']
    (ROOT/'knowledge'/'source-index.md').write_text('\n'.join(source_lines),encoding='utf-8')
    for category,title in [('mechanisms','Mechanisms'),('trajectories','Recovery trajectories'),
                            ('negative-evidence','Scoped negative evidence'),('tools','Tool inventory')]:
        lines = [f'# {title}', '', 'Generated from the authored research dossiers. Record IDs are stable within this initial catalog.',
                 'Sources resolve through [the provenance catalog](../catalog/sources.json); refs and content hashes are explicit.',
                 'Read the linked project dossier for the discovery context and limitations.', '']
        if category in ('mechanisms', 'negative-evidence'):
            lines.extend(['The [later adversarial review](../research/adversarial-synthesis-20260923.md) adds context-qualified blocker, convergence and region evidence without replacing these historical entries.', ''])
        for row in catalogs[category]:
            title = row.get('name',row.get('claim',row.get('statement',row.get('purpose',row['id']))))
            lines.extend([f'## {row["id"]}', '', f'**{row["epistemic_class"]} — {row["project"]}.** {title}', '',
                          f'[Project dossier](../{row["dossier"]}).', ''])
            for key in ('signature','symptom','causal_mechanism','experiments','discriminating_experiment','distinguishing_experiments','negative_alternatives',
                        'hypothesis','conditions','result','outcome','scope','limitation','diagnostic','reusable_diagnostic',
                        'inputs','outputs','dependencies','assumptions','reuse','license_review','synthesis_note'):
                if key in row:
                    value = row[key]
                    lines += [f'**{key.replace("_"," ").capitalize()}:** '+ ('; '.join(map(str,value)) if isinstance(value,list) else str(value)), '']
            steps = row.get('steps',row.get('chain',row.get('sequence',[])))
            if steps: lines += [' → '.join(steps), '']
            for related, filename in [('related_tools','tools'),('related_trajectories','trajectories'),('mechanisms','mechanisms')]:
                if row.get(related):
                    lines += ['**'+related.replace('_',' ').capitalize()+':** '+', '.join(f'[{ident}]({filename}.md#{ident})' for ident in row[related]),'']
            lines += ['**Sources:** '+ '; '.join(
                f'[{source_by_id[s["source_id"]]["path"]}](source-index.md#{s["source_id"]})'+
                (f' (anchor {s["anchor"]})' if s.get('anchor') else '') for s in row['sources']), '']
        dest = ROOT/'knowledge'/f'{category}.md'
        dest.parent.mkdir(exist_ok=True)
        dest.write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({k:len(v) for k,v in catalogs.items()}|{'sources':len(all_sources)},indent=2))

if __name__ == '__main__': main()
