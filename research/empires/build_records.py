"""Recreate this authored extraction's metadata from immutable local Git objects."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parent / 'empires_reconstruction'
REF = '873d1df0f505601d760c6880cdea0c6ae3d81405'

def git(*args):
    return subprocess.check_output(['git', '-c', f'safe.directory={REPO.as_posix()}', '-C', str(REPO), *args])

sources = {}
def src(path, anchor='', ref=REF):
    key = f'{ref}:{path}'
    if key not in sources:
        data = git('show', key)
        sources[key] = {'repository': 'empires_reconstruction', 'path': path, 'ref': ref,
                        'sha256': hashlib.sha256(data).hexdigest(), 'state': 'frozen_git_blob'}
    return dict(sources[key], anchor=anchor)

tu = src('docs/current/tu-structure.md')
front = src('docs/current/closure-frontier.md')
status = src('docs/current/status.json')
topology = src('tools/audit_relocation_topology.py')
plan = src('layout/production-plan.json')
workflow = src('docs/current/grinder-instructions.md')
supervisor = src('docs/current/supervisor-instructions.md')
toolchain = src('layout/toolchain.json')
music = src('src/MUSIC.C', ref='562905916f6aefe007a94cc605b2405610247c44')

def mechanism(ident, name, signature, causal, distinguishing, negatives, scope, diagnostic, related, evidence):
    return dict(id=ident, name=name, epistemic_class='PROJECT FACT', projects=['empires'],
                compiler='Turbo C 2.0 / TASM 1.0 / TLINK 2.0', signature=signature,
                causal_mechanism=causal, distinguishing_experiments=distinguishing,
                negative_alternatives=negatives, scope=scope, reusable_diagnostic=diagnostic,
                automated=True, related_tools=related, sources=evidence)

mechanisms = [
 mechanism('empires-route-context', 'Inline ASM selects a whole-TU assembler route',
 'A plain-C member needs -B to match; replacing a predecessor ASM instruction with an intrinsic changes neighbors.',
 'Turbo C restarts the entire unit through TASM on encountering inline ASM; branch relaxation differs from the native writer.',
 ['Whole GAME.C probe with BOOTSEED asm sti', 'Intrinsic substitution breaks TURNLOOP/LVLDRV', 'HITTEST -B probe supplies a boundary'],
 ['Do not invent arbitrary per-function -B flags', 'Byte-neutral grouping does not establish unique historical membership'],
 'Pinned Empires Turbo C/TASM route only.', 'Hold target body constant; change context or compilation route and measure every affected member.',
 ['empires-probe-tu','empires-audit-flags'], [tu,front]),
 mechanism('empires-ordered-relocations', 'Ordered relocations distinguish compiler routes and TU hypotheses',
 'Same code can fail whole-image proof because relocation order differs.',
 'Observed TLINK output retains object/FIXUPP order; native Turbo C descending order differs from ordinary TASM ascending order.',
 ['MUSIC native C recovery eliminates ordering accommodation', 'SLOTS/SLOTCOPY relocation order rejects merging'],
 ['A same-code ASM representation is not automatically the historical route', 'Zero/one relocation gives no direction evidence'],
 'Empires toolchain and measured objects; not a rule for MSC OMF or GCC COFF.',
 'Compare code, semantic binding and ordered topology separately before source-shape search.',
 ['empires-relocation-audit'], [topology,tu,music,plan]),
 mechanism('empires-tu-constraints', 'DATA continuity and incompatible declarations constrain TU boundaries',
 'A proposed shared unit cannot preserve all exact members.',
 'One recovered unit emits contiguous private DATA and requires mutually compatible declaration views.',
 ['HUD..ANIMFRAM rejected for noncontiguous DATA', 'BOARD/GAME a74a2 2-D versus flat views', 'KEYIRQ handler interrupt view conflict'],
 ['Adjacency alone is insufficient', 'Equal bytes for a merged run need not uniquely recover filenames'],
 'Observed source/data model in Empires; apply analogous constraints only after format-specific verification.',
 'Probe full candidate unit, private segments, all member bytes and bindings.', ['empires-probe-tu'], [tu]),
 mechanism('empires-asm-provenance', 'Compiler probes distinguish retained ASM from unrecovered C',
 'Framed functions or fragments resist ordinary C shapes.',
 'Recorded prologue/register/flag protocols and controlled probes establish compiler incompatibilities in specific cases.',
 ['28 standalone plus eight contextual byte-negation probes', 'FLAGS pseudo-register adds pushf/pop', 'Sound C wrappers introduce SI saves'],
 ['An ASM reconstruction is not evidence of original ASM authorship'],
 'Finite experiments support the current provenance decision, not mathematical impossibility of all C.',
 'Record exact unsupported behavior and retain minimal evidenced ASM; reclassify if a later probe succeeds.',
 ['empires-probe-module'], [front,tu,src('docs/current/asm-provenance.md')]),
 mechanism('empires-fresh-acceptance', 'Research cache and fresh acceptance have different proof contracts',
 'An old successful receipt could survive a failed or changed build.',
 'Builder invalidates success first, checks input identities and plan, disables cache for acceptance, verifies full EXE and ordered relocations.',
 ['Source inspection of build_production and object_cache', 'Frozen acceptance receipt'],
 ['A RESEARCH build or previous PASS is not fresh ACCEPTANCE'],
 'Implemented Empires contract; freshness is useful elsewhere but exact gate must stay project-specific.',
 'Bind success to input fingerprint and proof scope, explicitly record cache/freshness and invalidation.',
 ['empires-build','empires-cache','empires-fingerprint'], [status,src('tools/build_production.py'),src('tools/object_cache.py')])
]

trajectories = [
 dict(id='empires-music', name='MUSIC: body equality to native relocation topology', epistemic_class='PROJECT FACT', project='empires', outcome='success',
      steps=['Exact arithmetic code through ASM still needed relocation accommodation', 'Inspect historical descending relocation run', 'Distinguish native writer from assembler route', 'Recover whole pure-C MUSIC including structured fdf98', 'Native descending FIXUPPs restore strict topology', 'Full EXE acceptance succeeds; encode topology audit'],
      mechanisms=['empires-ordered-relocations'], sources=[src('docs/exact-structural-link.md'),src('docs/linker-adapter-ledger.md'),music,plan,status]),
 dict(id='empires-game-tu', name='GAME: local -B mismatch becomes whole-TU evidence', epistemic_class='PROJECT FACT', project='empires', outcome='success',
      steps=['TURNLOOP/LVLDRV need assembler-shaped bytes', 'Local flags lack a source explanation', 'Group with BOOTSEED inline asm sti', 'Replacing ASM with intrinsic breaks neighbors', 'Whole-TU probe exact', 'Promote GAME.C, retain incompatible declaration/route boundaries'],
      mechanisms=['empires-route-context','empires-tu-constraints'], sources=[tu,front,plan]),
 dict(id='empires-negation', name='BOARD byte negation: bounded negative result', epistemic_class='PROJECT FACT', project='empires', outcome='negative',
      steps=['Target neg ax uses already-zero AH', 'Try 28 standalone source forms', 'Observe neg al or extension/spill sequence', 'Try eight context-preserving probes', 'No tested C route removes extra work', 'Retain evidenced inline ASM fragment under strict full acceptance'],
      mechanisms=['empires-asm-provenance'], sources=[front,src('docs/history/probes/neg-ax-forms.C')]),
 dict(id='empires-final-freeze', name='Exact structural output to adapter-free source closure', epistemic_class='PROJECT FACT', project='empires', outcome='success',
      steps=['Historical TLINK produces exact image with accommodations', 'Replace copied DATA and aggregate BSS with source contributions', 'Replace injected publics and metadata with natural source declarations', 'Use whole modules and native MUSIC route', 'Fresh uncached acceptance plus provenance and topology audits', 'Freeze historical-exact-oracle-v1'],
      mechanisms=['empires-fresh-acceptance','empires-ordered-relocations'], sources=[src('docs/exact-structural-link.md'),src('docs/linker-adapter-ledger.md'),front,status,plan])
]
negatives = []
for ident,hypothesis,conditions,result,limitation,evidence in [
 ('negation','Ordinary C spelling can produce the observed neg ax fragment without extra work','Pinned TC2 BOARD fragment; 28 standalone + eight context probes','Tested routes emit neg al or add extension/spills','Not an exhaustive impossibility proof',[front]),
 ('intrinsic','Replace BOOTSEED asm sti with intrinsic without changing peers','GAME TU and pinned TC2 route','TURNLOOP/LVLDRV cease matching','Specific route/context; not an objection to intrinsics generally',[tu]),
 ('merge-data','HUD through ANIMFRAM form one recovered TU','Observed private DATA ownership/components','PROMPTS and DLGELOST DATA are not contiguous','Depends on evidenced DATA ownership',[tu]),
 ('merge-view','BOARD and GAME share a single common a74a2 declaration','Tested 2-D/flat declaration views','No tested single view preserves both exact members','Byte-neutral extensions elsewhere remain possible',[tu]),
 ('flags','Pseudo-register FLAGS replaces BIOS immediate flag protocol for free','TC2 INT16 helpers','pushf/pop adds instructions','Specific flag-return protocol',[front])]:
    negatives.append(dict(id='empires-negative-'+ident, epistemic_class='PROJECT FACT', project='empires', hypothesis=hypothesis,
                          conditions=conditions, result=result, limitation=limitation, sources=evidence))

tools=[]
for ident,path,purpose,inputs,outputs,deps,assumptions,reuse,alternative in [
 ('build','tools/build_production.py','Strict source-to-executable acceptance','production plan/source/toolchain/oracle metadata','EXE and fingerprinted receipt','project compiler/linker/OMF/MZ stack','Empires exact MZ topology','project_specific','Consult SimAnt for member proof; do not replace this full-image gate'),
 ('probe-tu','tools/probe_tu.py','Test contiguous whole-TU hypothesis','module range, source overrides, compiler flags','whole-run byte/binding report','project manifests/compiler runner/original EXE','Empires plan, _TEXT and private DATA model','adapter_required','Icy Tower predecessor/order probes cover different compiler-state questions'),
 ('probe-module','tools/probe_module.py','Single-module C/ASM probe','owner and source override','code/DATA/fixup comparison','project OMF binder and toolchain','Cannot alone bind two library/runtime cases','adapter_required','SimAnt strict member verifier has richer Win16 fixup semantics'),
 ('relocation-audit','tools/audit_relocation_topology.py','Separate code equality from relocation route mismatch','production plan, MZ and optional fresh objects','direction/provenance audit','project MZ and OMF readers','TC2/TASM/TLINK observed ordering','project_specific','No generic direction rule across compilers'),
 ('audit-flags','tools/audit_tu_flags.py','Explain compiler route flags by source','plan and source','unexplained flag audit','project source parser/plan','TC2 -B/-k semantics','conceptually_reusable','A compiler-specific context audit is preferable to shared flag rules'),
 ('cache','tools/object_cache.py','Content-addressed research compilation','owner, includes, lock, driver','cached object/receipt or fresh compile','reconstruct.py and local compiler','Owner/includes assumptions, acceptance disables cache','adapter_required','SimAnt persistent service addresses startup cost differently'),
 ('fingerprint','tools/factory_inputs.py','Construction-input provenance fingerprint','known source/layout/recipes/tool trees','SHA256 aggregate','reconstruct.py and project DATA recipe','Hard-coded construction closure','conceptually_reusable','Shared provenance manifest can separate enumeration from hashing'),
 ('candidate','tools/check_candidate.py','Bounded FAST check and promotion/block logging','task card and edited source interval','diagnostic, archived attempt or acceptance','project factory/runtime assembler','All runtime bytes, publics, ordered fixups and strictly fewer unresolved bytes','project_specific','Stunts/SimAnt handoff and variant tools have different contracts'),
 ('relocation-groups','tools/discover_relocation_groups.py','Suggest minimum shared-compilation runs','MZ relocations and owner manifest','candidate recipes and constraints','project MZ/compiler probes','512-byte header coordinate conversion, descending TC2 runs','project_specific','Concept of evidence-derived grouping transfers, implementation does not')]:
    tools.append(dict(id='empires-'+ident, project='empires', path=path, purpose=purpose, inputs=inputs, outputs=outputs,
                      dependencies=deps, assumptions=assumptions, reuse=reuse, alternative=alternative,
                      license_review='No top-level source-tool license found; reference only. No code copied.', sources=[src(path)]))

record = dict(project=dict(id='empires', repository='empires_reconstruction', head=git('rev-parse','HEAD').decode().strip(),
              branch=git('branch','--show-current').decode().strip(), dirty=False, evidence_ref=REF,
              evidence_tag='historical-exact-oracle-v1', state='frozen historical closure; live portable branch',
              compiler='Turbo C 2.0 / TASM 1.0 / TLINK 2.0', architecture='16-bit DOS real mode',
              formats=['OMF','MZ'], proof='Full executable SHA256, 106 ordered relocations, one fresh TLINK; no structural adapters',
              workflow='Historical queue closed; retained bounded FAST -> fresh ACCEPTANCE factory',
              sources=[toolchain,status,front,workflow,supervisor]),
              mechanisms=mechanisms, trajectories=trajectories, negatives=negatives, tools=tools,
              sources=list(sources.values()))
(Path(__file__).parent/'records.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
