# SimAnt / Win16 MSC 7 recovery-factory dossier

## Scope and snapshot

This is a read-only research extract from `../simantw_recon`, discovered as a
sibling of this workspace under the common `D:\Prog` parent. The observed HEAD
is `cdf6af62cc67608f02c574e805d79cb413e330ef` on
`codex/simantw-recovery`. The examined working-tree snapshot is
**2026-09-23T19:49:21Z**; its exact hashes are in `records.json`. It was dirty:
the queue, factory/lesson documents, recovery material, and grinder had local
changes, including untracked job evidence. Live facts below belong only to
that snapshot; committed claims name `cdf6af62`, and working-tree claims name
their content hash.

The recovery target is 16-bit Windows / NE on x86, with MAPSYM evidence,
Microsoft C/C++ 7.00 and LINK 5.30. The operational compiler baseline is
`/AL /G2 /Gs /Oelw /NT<original code group>`; a profile belongs to a unit
context, never a per-function flag hunt. The examined queue reports 517
matched, 106 match-ready, 440 match-blocked and 2 structure-blocked functions
(`docs/production-queue.json:7`, working tree snapshot). This is an active
recovery factory rather than a closed executable claim.

**Proof model.** A source is admitted only after fresh compilation and a
complete member check covering extent, ordinary bytes, public placement,
semantic OMF/NE fixups, and private contributions. Similarity, an exact body,
scaffold stand-ins and structural certificates do not grant recovery credit
(`docs/factory.md:41-47`). Structural certification only authorizes testing.

## High-value mechanisms

### 1. Effective output identity is the stopping signal

**PROJECT FACT — MSC 7 / isolated SimAnt context.** Candidate source forms are
deduplicated before the budget is consumed, then raw OMF identity tells whether
an axis actually gave the compiler a new output. A three-candidate
`_FloodNestB` probe yielded two objects: ordinary and `register` row/cell
forms collapsed to one hash while reversed declaration order made the other;
neither was exact and the remaining residue was seven register differences.
The next experiment was correctly promoted to lifetime/context analysis rather
than another spelling matrix (`evidence/experiments/flood-nest-mapb/README.md:9-22`).

Reusable diagnostic: record both source identity and object identity, group
results by the latter, then choose the next axis from the *surviving delta*.
The current factory archives this as `compiler_response`: fixed-profile raw
OMF classes, one representative's codegen dimensions, and deltas from the
baseline, while keeping strict evidence separate (`docs/factory.md:128-135`).
This is a **GENERIC METHOD**; the exact collapse is not evidence that another
compiler has the same equivalence classes. `_ChangeDirectory` independently
records 16 candidates but 14 objects and retains the failed parameter/based
forms as scoped negative evidence (`evidence/experiments/change-directory/README.md:12-18`).

### 2. MSC 7 declaration order can control commutative operand selection

**PROJECT FACT — MSC 7, specific unit contexts.** For two globals in a
commutative expression, expression rewrites can canonicalize away while the
extern declaration order decides which operand is the memory reference.
`PreDrawSpider`, colony `EatFood/TryEatFood`, and antedit balloon functions
needed only the documented declaration pair swaps; the unit composer applies
those evidence-backed pairs (`docs/grinder-lessons.md:129-135`,
`layout/declaration-order.json:1-54`). This can also alter DS/ES generation.
Separately, an eight-attempt `_MagnifyMenu` recovery established that order of
three local declarations selected stack operands in a bound expression; its
earlier parentheses, temporary, comma and expression-tree forms collapsed.
This is another local MSC7 fact, not evidence that the global-declaration
mechanism has the same cause (`docs/grinder-lessons.md:211-226`).

Scope: do not turn this into a general declaration-order heuristic. It applies
to recorded pairs in a specific MSC7 translation unit and is exhausted for an
isolated target once its object classes collapse.

### 3. Strict member proof keeps body, fixup, and data correctness separate

**PROJECT FACT — OMF/NE SimAnt matcher.** A byte-identical-looking body is
insufficient: a far-code LOC 5 offset is valid only with the matching selector
fixup; a BSS static must lie inside the original BSS interval
(`docs/factory.md:49-52`). The matcher also exposes member-wide unresolved
obligations instead of hiding them behind aligned instructions
(`docs/grinder-lessons.md:79-85`).

Representative admissions show why: `_db_UnhookObject` matched 38 code bytes,
36 private-data bytes and five semantic fixups; `_db_PurgeObject` matched a
closed `retf` extent plus 73 private bytes and ten fixups
(`evidence/recovery/batch105/results.json:4-7`,
`evidence/recovery/batch110/results.json:4-7`). The `_ProcMenuHelp` failure had
the calls and two fixups but an extra alignment byte, so it was not promoted
(`evidence/recovery/batch114/results.json:8-16`).

Reusable method: hold diagnostic alignment apart from acceptance, and make
private placement/fixups first-class comparisons. The OMF and NE parsing rules
are **project-specific adapters**, not a generic binary matcher.

### 4. Selector pools, pointer representation, and data identity reveal unit context

**PROJECT FACT — Win16 large model MSC7.** Every far `mov es,[word]` points to
an object-private CONST selector pool allocated in code-generation order; a
pool is dense and its positions retain link order
(`docs/build-topology.md:42-60`). Equal segment selectors do not prove that
two offsets name one object. Four named-object probes resolved eleven offsets
yet still failed strict member proof because selector placement/order remained
wrong (`docs/grinder-lessons.md:51-57`).

This family includes three distinct ABI/data facts that must not be merged:

- A private initialized word can use `__based(__segname("SIMANT_DATA_GROUP"))`
  once the NE selector names that segment; the admitted multimedia cases prove
  the contribution, not the whole state object's boundary
  (`docs/grinder-lessons.md:59-65`).
- `void far *` versus `void far * near` changes whether C7 reads a selector
  through CONST or directly from a near DGROUP object; `_InitTree` probes
  establish only the declaration behavior (`docs/grinder-lessons.md:137-140`).
- Private BSS/data must respect actual region and initialized-byte evidence;
  former apparent admissions were rejected and repaired after the BSS rule
  (`docs/grinder-lessons.md:101-105`).

Reusable diagnostic: distinguish (a) selector/segment evidence, (b) offset
evidence, (c) object identity, and (d) complete contribution placement. This
is conceptually reusable; its concrete ABI vocabulary is Win16-specific.

### 5. Recovery should shift from isolated bodies to verified unit assembly

**PROJECT FACT — SimAnt factory.** The topology model describes a source TU as
contiguous code plus private CONST selector pool and private DATA/BSS, while
most historical filename boundaries remain unknowable
(`docs/build-topology.md:12-18`). Exact bodies that only miss pool/data context
are reassembled with verified sources. Scaffolded units allocate *measured*
unclaimed selector positions in reserved `POOLSTUB_TEXT`; the stubs are never
matched or credited, but claimed bodies and pool words remain strictly checked
(`docs/factory.md:8-25`). The upstream lesson reports 31 parked-body admission
events and a checkpoint total from 417 to 447. Those numbers are not a simple
one-to-one net accounting: the same passage says two isolated recipes were
superseded and an invalid `AddRandAntLion` body stopped counting as exact.
Record this as **31 conversion events; +30 reported net at that checkpoint**,
not as 31 net durable additions (`docs/grinder-lessons.md:115-119`).

Mirror-pair derivation is a constrained companion: it swaps MAPSYM twin
identifiers/recorded constants outside comments and strings, then runs the
strict matcher; non-pure mirrors remain asymmetry evidence
(`tools/mirror_pairs.py:77-137`). The method is reusable only where an
evidence-backed symmetry map exists.

## Representative trajectories

1. **Success — sequential diagnosis isolates source shape then private state
   (`_DrawForSale`).** Attempt 1 had instruction shape plus external
   `forSaleObject` binding failures (35/54 literals, 3/7 fixups)
   → attempt 2 corrected control/ordinary body shape (46/52, 4/7) but the
   remaining mismatch isolated an external-versus-private DGROUP word
   → the recorded next experiment modeled a private initialized cached handle
   with `-1` sentinel
   → attempt 3 reached 48/48 literal bytes and 7/7 fixups
   → fresh `STRONGLY_SUPPORTED_MEMBER` admission. This is a three-attempt
   SimAnt/MSC7 trajectory; it does not imply that all near globals should be
   made static. Sources: `evidence/recovery/workflow/jobs/DrawForSale-956dc12b43/job.json:300`,
   `attempt01/results.json`, `attempt02/results.json`, `attempt03/results.json`,
   `promotion.json:2-25`.

2. **Success — sequential local-order isolation (`_MagnifyMenu`).**
   Attempt 1 had broad control/frame/memory differences
   → attempts 2–5 and 7 converged to 338/342 literal bytes and 46/46 fixups
   in the same OMF class
   → a volatile local was a substantial regression
   → the last controlled experiment reordered locals from `screen, object,
   point` to `screen, point, object`
   → it selected the target edge-first stack operand schedule
   → attempt 8 matched 342/342 literal bytes and 46/46 fixups and was admitted.
   Sources: `docs/grinder-lessons.md:211-226`; untracked working-tree
   `evidence/recovery/workflow/jobs/MagnifyMenu-51f69a1a04/{job,mechanism,promotion}.json`.

3. **Failure / analysis-level change — `_FloodNestB` near map.**
   Invented `_nestMap + 0x48E8` binding
   → MAPSYM established `_MapB` as the real near base
   → three bounded source/declaration trials
   → two effective OMF classes, all 27 opcodes and fixup aligned
   → seven register-only differences remained
   → no promotion; next work is lifetime/operand structure or TU context, not
   declaration-order retry. Source: `evidence/experiments/flood-nest-mapb/README.md:1-22`.

## Negative evidence worth preserving

- `_FloodNestB`: ordinary and `register` row/cell forms are one OMF class in
  that isolated baseline context; reversing order changes output but does not
  match. `.../flood-nest-mapb/README.md:13-22`.
- `_ChangeDirectory`: the eight bounded attempts do not establish correctness
  for parameter-copy order, separator forms, several `Dx8+offset` forms or the
  based-pointer spelling; attempt 8 improved a selector/offset interpretation
  but remained 372 vs 364 bytes with 1/13 fixups. `.../change-directory/README.md:12-18`.
- `_ProcMenuHelp`: declaration width did not alter C7's alignment schedule;
  28 candidate bytes still differed from 27 target bytes. No partial credit.
  `evidence/recovery/batch114/results.json:8-16`.
- `_ms_Delay`: materializing the start tick changes register schedule; the
  combined expression changes extent and second-call fixup placement.
  `evidence/recovery/batch103/results.json:1-9`.
- Profile sweeps: `/Ox` and MSC 6.00A were worse than `/Oeglw` on the tested
  parked set. Separately, 100 exact-body escalations were selector-pool/private
  placement cases, not profile questions. That does not contradict the
  separate 102-job code-shape sweep where `/Og` improved 28 and strictly
  matched two. None of these results rule out a different profile in another
  unit. `evidence/experiments/optimizer-profile/README.md:20-35`.
  `evidence/experiments/optimizer-profile/README.md:18-35`.

## Workflow, batching, and reclassification

The factory permits eight attempts, at most 96 variants per attempt and 192
candidates per target; it rejects duplicate experiments and preserves failed
drafts with the next discriminating experiment (`docs/factory.md:39-47`).
Batch only explained independent axes; retain sequential feedback where the
remaining mismatch selects the next hypothesis. Current reclassification
recompiled every blocked best candidate under its present object profile: 399
true source-shape mismatches, 20 ABI type-inference, 13 unknown, 4 exact-body
layout, one profile retest, and one mirror pair (`docs/blocked-reclassification.md:1-14`).
That is strong local evidence for changing analysis level from source spelling
to ABI/unit/context for the small exact-body subgroup, not a universal ratio.

The compiler service is a useful **working hypothesis for reuse**, not a
drop-in shared runner: four isolated persistent DOSBox-X/Win3.x workers have
validated 18 canonical probes twice; 400 candidates completed in 50.53s with
byte-identical objects and sessions recycle after 96 jobs
(`layout/compiler-service.json:1-12`; `docs/factory.md:108-112`). Its generic
parts are immutable request snapshots, receipts, cache keys, worker isolation,
and bounded recycling. Its runner, filesystem, historical compiler and OMF
acceptance are project adapters.

## Tool inventory and reuse posture

See `records.json` for structured input/output/dependency fields. The first
shared candidates are pure analysis patterns: effective-output clustering,
outcome matrices, and a provenance/trajectory recorder. Keep compiler runners,
OMF/NE proof, topology composition, and MAPSYM mirror derivation as referenced
adapters until a second project demonstrates the same abstraction. No source
tool was copied here; no binary, original-game bytes, compiler, SDK, or asset
was copied.

## Sources and limitations

All source paths below are repository-relative to `simantw_recon`; anchors are
one-based line anchors in the inspected state. `records.json` records the
commit plus the working-tree hashes for files whose live state was used. These
are **project facts** unless explicitly marked generic method/working
hypothesis. The repository's license was not established in this pass, so tool
entries are reference-only and require a license review before copying.


## September 24 follow-up

The [dated project update](../updates/20260924/review.md) and its separate
[evidence manifest](../updates/20260924/evidence.json) preserve newer observations
without changing this dossier's earlier snapshot. New catalog claims are scoped
project facts; diagnostic coverage and strict recovery remain separate.
