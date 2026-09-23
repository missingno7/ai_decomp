"""Read-only verification of reference manifests; original ai_decomp stdlib tool."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def contained(root, relative):
    if not isinstance(relative,str) or not relative or Path(relative).is_absolute():
        raise ValueError('Expected nonempty relative path')
    path = (root/relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Path escapes declared root')
    return path

def check(sources, parent):
    results = []
    for source in sources:
        try:
            repo = contained(parent,source['repository'])
            path = contained(repo,source['path'])
            if source['content_kind'] == 'working_tree':
                blob = path.read_bytes()
            elif source['content_kind'] == 'git_blob':
                if not re.fullmatch('[0-9a-f]{40}',source['ref']):
                    raise ValueError('Git source must use an immutable full commit ID')
                blob = subprocess.check_output(['git','-c',f'safe.directory={repo.as_posix()}',
                    '-C',str(repo),'show',source['ref']+':'+source['path']],stderr=subprocess.PIPE)
            else:
                raise ValueError('Unknown content kind')
            digest = hashlib.sha256(blob).hexdigest()
            status = 'verified' if digest == source['sha256'] else 'drifted'
            results.append({'id':source['id'],'status':status,'actual_sha256':digest})
        except (OSError,ValueError,KeyError,subprocess.CalledProcessError) as error:
            results.append({'id':source.get('id'),'status':'unavailable','reason':str(error)})
    return {'format':'ai-decomp-provenance-check-v1','authority':'reference_integrity_only',
            'checked':len(results), 'verified':sum(r['status']=='verified' for r in results),
            'results':results, 'limitation':'Hash/ref verification is not independent reproduction of a compiler claim.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=ROOT/'catalog/sources.json')
    parser.add_argument('--parent',type=Path,default=ROOT.parent)
    args=parser.parse_args()
    try:
        report=check(json.loads(args.manifest.read_text(encoding='utf-8')),args.parent.resolve())
    except (OSError,ValueError) as error:
        parser.exit(2,f'Cannot read manifest: {error}\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['verified']==report['checked'] else 1)

if __name__=='__main__': main()
