# Stunts: why the cheap recovery queue is starved

Read-only review, 24 September 2026. The inspected Stunts base is
`5aa3a27`; full commit, working-tree hashes and sanitized derived rows are in
[the evidence manifest](evidence.json). No sibling compiler, refresh, promotion,
or source mutation was run. This supplements earlier snapshots, not their hashes.

## Decision

**PROJECT FACT:** the default queue preferentially exposes tiny, relocation-free
functions. **WORKING HYPOTHESIS:** this selection and evidence-preparation gap
is suppressing a useful population of ordinary C recovery tasks. It is a more
concrete near-term intervention than treating 576 SUPERVISOR entries as exhausted
source searches. There is no measured throughput benefit yet.

The source-generation problem is real on investigated cases. Compiler identity,
mixed C/ASM/runtime origin, and historical contribution boundaries remain open.
Neither a global wrong-profile explanation nor a project-wide model ceiling is
established. The current adversarial-profile directory contains a calibration
plan and sources; no completed results were visible at inspection.

## What the implementation actually does

`tools/import_restunts.py:80` creates automatic instruction packets only for
verified functions of at most 80 bytes with no MZ relocations. Larger or relocated
functions need reviewed overlays. `tools/reconstruction_factory.py:62-67` makes
MEDIUM depend on the same 80-byte ceiling, while CHEAP requires a recipe and no
capability blockers. `tools/triage.py` returns immediately when instruction
evidence is absent, before inspecting calls, global references or control flow.

At capture:

| Observation | Count | Interpretation |
|---|---:|---|
| Strict game C | 26 functions / 1,118 bytes | Native retained acceptance; not fresh acceptance by this review |
| Queue | 7 MEDIUM / 576 SUPERVISOR | Eligibility, not intelligence classification |
| SUPERVISOR with verified boundary/instruction anchors | 494 | Does not establish historical object ownership or a complete CFG |
| SUPERVISOR lacking a complete instruction packet for triage | 349 | All 349 have the verified boundary status; packet availability is a separate condition |
| Queue rows with only that capability label | 59 | Further obligations can be hidden by the early return |
| SUPERVISOR with all three production attempts remaining | 566 | Does not imply no private research has occurred |
| Remaining with two / zero production attempts | 5 / 5 | Three-attempt policy is not a general exhaustion test |

The 59-row subset has no observations in the current generated attempt index.
That index is incomplete for private research, so this is not proof of 59 untried
functions. The separate census already flags 15 TU/context candidates, six CFG
unreachable candidates and four binding candidates within this subset (overlap
allowed). Merely decoding everything or raising the size limit is insufficient.

The `ordinary_c_hint` is also a narrow heuristic: it uses segment/name rules,
selected instructions and prologue/last-instruction shape. It is not recovered
language provenance. The `c_sources` field is a regex reference search and can
identify callers rather than definitions. Do not rank tasks on either field alone.

## Concrete cohort to investigate first

The native research census reports complete linear decoding, no calls and no MZ
relocations for these examples. That is diagnostic evidence, not full readiness.

| Target | Bytes | Why inspect it | Remaining caveat |
|---|---:|---|---|
| `rect_is_adjacent` | 130 | Actual Restunts C definition and several accepted related rectangle routines | Recheck pristine conditions, CFG and dependencies; Restunts source can differ |
| `init_rect_arrays` | 94 | Straight-line candidate in a known data family | Current C references are callers; establish stores, widths and global ownership |
| `mat_multiply` | 128 | Actual Restunts C definition; bounded arithmetic and structure task | Wider arithmetic may expose the existing multiply-lowering problem |
| `file_decomp_rle_seq` | 170 | Actual Restunts C definition and a bounded loop | Huge-pointer source model and register behavior may still be difficult |

These are candidates for preparation, not instructions to mark them ready.
Restunts remains semantic evidence only. Inspect ingress, reachable instructions,
data accesses, ABI and complete contribution before assigning a research contract.

There is a strong existing positive control: `shape3d_init_shape` is 172 bytes,
outside the automatic small-function path. After manual evidence preparation,
one hypothesis emitted 190 bytes; removing a local far-pointer alias gave the
exact 172-byte contribution on the second hypothesis. A third grinder entry
promoted it. This proves that size above 80 bytes does not preclude cheap recovery;
it does not estimate how often preparation will uncover similar wins.

## Research and promotion have different readiness requirements

The non-leaf preparer (`prepare_far_call_candidate.py`) creates a recipe and
reviewed overlay only after fresh fully bound compiler output already equals
the pristine contribution. That is a valid promotion-preparation gate. It is
not a suitable queue-admission criterion for exploratory source work.

The project already has the escape path: `research_batch.py` accepts verified
target cards without a production recipe, compiles isolated candidates and
retains diagnostic output. Worker instructions explicitly permit bounded Luna
research on SUPERVISOR tasks. Therefore research is not technically prohibited.
The missing demonstrated operation is routinely preparing and feeding such tasks
to that path before a supervisor has effectively solved them.

**GENERIC METHOD:** maintain separately (1) evidence sufficient for bounded
research, (2) source/code-generation findings, and (3) eligibility for native
promotion. Unresolved symbol/fixup fields must remain explicit. Partial byte
agreement cannot establish the right symbol or authorize production.

## What is working, and what the evidence criticizes

**Keep:** immutable oracle, complete code/fixup obligations, independent runner
checks and serialized rollback-capable promotion. Callback recovery shows the
process can convert independently supported binding into a strict win. Preserve
source/context histories and precise negatives. The timer experiment correctly
removed raw OMF index renumbering from semantic target-output novelty while
retaining raw records and distinct object topology.

**Change task selection:** tiny relocation-free code is easier to admit, not
necessarily easier to express in historical C. Small arithmetic, register-based
helpers, runtime and possible ASM deserve origin/expressibility research. Their
difficulty should not dominate the estimate of ordinary game-C solvability.

**Do not generalize the candidate archive:** the inspected census has 66 distinct
task/object payloads over 28 current SUPERVISOR targets, with no remaining complete
nonfixup-shape candidate. It samples selected archive roots and excludes promoted
tasks. It justifies not building another speculative binder; it does not show
that the hundreds of other functions resist source recovery.

**Audit budgets rather than abolishing them:** the ordinary three-failure stop
is a workflow rule. Research already permits wider bounds. The endurance cohort
found informative results beyond three hypotheses but no new strict recovery,
so longer runway has not been shown to solve the throughput problem either.
Two equal outputs reject a tested contrast, not every untested source dimension.

**Finish compiler identification:** the inspected plan has fixed sources,
controls and held-out targets. Its result may change priorities. Existing simple
exact matches do not identify MSC 5.00 versus 5.10; failed guessed sources do not
exclude a profile globally. Do not widen the entire compiler search merely to
avoid testing ordinary prepared functions.

**Tie diagnostics to a recovery decision:** mapping and placement diagnostics
have useful evidence value. Their growth must not substitute for measuring the
funnel from prepared task to compiled candidate to strict promotion. The camera,
timer, incomplete file objects and shared-entry sine family have scoped negatives;
revisit them only when new evidence changes the question.

## Highest-leverage next experiment

In the owning project, prepare a small cohort (initially the four rows above,
replacing any rejected by review) using existing decode, CFG, context and batch
tools. Add reviewed far-call cases only after the first preparation contract
works. Preserve explicit entry/exit, source-origin and symbol unknowns. Do not
change native acceptance or manufacture an original TU claim.

Give cheap workers preauthorized bounded research with full evidence access,
adaptive source/context experiments, complete output retention and project-native
serialized promotion. Record preparation/supervisor work as well as worker work.
Use a coherent research budget rather than interpreting three production failures
as exhaustion; the exact budget is an experimental choice, not a new law.

Measure each stage: screened, rejected with reasons, research-ready, first complete
compile, effective output classes, body findings with unresolved fixups, native
strict promotion and total model effort. Record useful negatives separately.

**Falsifier:** if a carefully reviewed broader C cohort still consistently yields
the same compiler-specific discrepancies under plausible source alternatives,
with sufficient runway and no blocking tool/evidence defect, task selection is
not the main explanation for that cohort. Aggregate the repeated mechanism and
test it against the compiler-study controls. If preparation regularly stalls on
ingress/ownership, invest there instead. A larger fleet is premature until this
small end-to-end experiment shows reusable yield.

No new integration, scheduler, binder or sibling dependency was implemented by
this review. Shared workspace edits already present at the start were left intact.

## Workspace validation

All 39 tests and `tools/check_workspace.py` passed. The new manifest verified
24/24 captured working-tree sources without drift. The existing catalog checker
verified 139/154 older source records; 15 live records differ from their stored
hashes. No old identities were refreshed. These checks establish metadata
integrity and workspace consistency, not a new compiler or recovery result.
