# Stunts reconstruction dossier

**Snapshot.** `stunts_recon` was read at `D:/Prog/stunts_recon`, discovered as a sibling of this workspace.  The live checkout was `main` at `068ff2e67d7b0ef9865ec1a4d60651eb8c830d0d` (2026-09-23).  It is substantially dirty: 620 tracked files have unstaged modifications and 16 files are untracked; there are no staged files.  This dossier cites working-tree content where indicated, with its observed SHA-256, rather than treating HEAD as the current workflow.  The cited live files were re-examined after a drift alert on 2026-09-23; validation fingerprints changed but the recorded PASS, 139-test, 11-active-function, and queue-count facts did not.  Source checkout was not modified.

## Current project state and proof model

This is DOS real-mode, 16-bit medium-model recovery using MSC 5.0/5.1 profiles (`/AM /O /Gs`); production pins MSC 5.1 but the historical version and flags are not uniquely proven.  The executable is an MZ/load-image reconstruction with OMF objects and binding/fixup checks.  Its oracle is pinned by SHA-256: the load image is 200,000 bytes.  The latest validation receipt records `HYBRID_EXACT`, 139 passing tests, and independent recompilation of 11 active C functions, while the separate generated status records `full_image_status: NOT_CURRENTLY_VERIFIED`; neither is a claim of complete recovery.  That status also records 408 matching C bytes, no matching ASM bytes, 725 pinned runtime bytes, 198,867 raw initialized bytes, and 158,205 unknown-classification bytes; 605 tasks remain in the supervisor queue. [status.json, lines 1-60; validation.json, lines 1-32]

The acceptance hierarchy is deliberately hybrid.  Candidate work is checked against pristine oracle input, object/fixup evidence, and fresh whole-image acceptance before serial promotion.  Research may preserve an informative compiled object even when a production parser/binder rejects it, but must not silently turn it into a match.  This distinction is active in the endurance corpus: the generic `OmfReader` could diagnose B4/LEXTDEF objects while the strict production reader rejected them. [worker-research.md, lines 3-17; endurance-001/handoff.md, lines 1-24]

The current workflow starts from a compact machine diagnosis, retains full artifacts, records a prediction and falsifier before compilation, then uses a bounded experiment or an adaptive next step.  A worker must reclassify the problem after two hypotheses yield the same effective compiler output and record whether a shared ceiling's per-case allocation can be reallocated.  Research-only batches archive all proposed sources first and report candidate-to-oracle anchors plus candidate-to-candidate byte/fixup effects; operand patterns are withheld when candidate fixups differ.  `grind.py` plus fresh whole-image validation remain the strict path. [worker-research.md, lines 9-17]

## Demonstrated mechanisms

### 1. Strict hybrid proof separates code generation from acceptance

**Type:** PROJECT FACT / GENERIC METHOD.  A candidate can be useful evidence without being a promotion.  Stunts retains raw oracle identity, compiler/object evidence, fixups and a whole-image receipt; its candidate checker guards against input drift and requires fresh staged and canonical builds. [status.json, lines 1-60; validation.json, lines 1-32; tools/check_candidate.py, lines 13-103]

**Scope.** The general method is reusable: keep source/code, relocation/binding and final acceptance as distinct dimensions.  Its MZ/OMF parser, historical MSC profile, and Stunts queue are not portable assumptions.

### 2. Effective-output identity is the unit of experiment progress

**Type:** PROJECT FACT / GENERIC METHOD.  The worker instructions explicitly say that a changed source hash or metadata is not progress; after two hypotheses collapse to the same effective output, switch analysis level. [worker-research.md, lines 13-17]  In the matched routing capsules, 44 hypotheses with 40 identity-bearing results collapsed to 24 case/model-deduplicated effective identities; ten repeats occurred within runs.  The identity includes profile and flags, so it is not an assertion of globally unique machine code. [batching-retrospective.md, lines 3-11]

**Reusable diagnostic.** Hash the complete emitted code/fixup/context result, group equal outcomes, and store what source axis was varied.  Use repetition to stop local spelling sweeps and inspect ABI, allocation, TU, binding or compiler evidence.

### 3. Candidate-to-candidate comparison can explain a local effect without claiming the repair

**Type:** PROJECT FACT / CONCEPTUALLY REUSABLE.  The `is_facing_camera` declaration-order probe changed only `dx1`/`dy0` declaration order.  It moved the predicted paired 32-bit BP homes, produced a consistent 11-site displacement mapping, and gained 35 protected target anchor positions.  It still emitted 194 bytes for a 200-byte target and first diverged at relative `+0x4A`; the report refuses to equate this allocation effect with a historical source reconstruction or acceptance. [declaration-order-20260923.md, lines 1-6]

**Scope.** This is evidence for one MSC 5.1 source/profile and one stack-home mechanism.  It does not establish that declaration order is generally causal, nor resolve result/return lowering, extent, or TU context.

### 4. Mismatch islands and operand families are evidence summaries, not source causality

**Type:** PROJECT FACT / GENERIC METHOD.  The diagnostic engine aligns decoded streams, preserves anchors, reports islands, separates fixups, and only promotes a BP/register family when mappings are one-to-one with consistent widths and no contradictions. [tools/diagnostics.py, lines 227-457]  The project documents that such patterns are observed operand relations, not variable identity, dataflow, or a source repair; segment/frame roles and uncertain branch destinations stay separate. [near-match-families.md, lines 9-15]

**Reusable diagnostic.** Represent positive evidence, contradicting uses, and ungrouped residuals separately.  A byte-perfect body remains insufficient when an unresolved fixup, symbol, extent or layout mismatch exists.

### 5. Compiler availability and binding can be concrete blockers rather than model failure

**Type:** PROJECT FACT.  `sub_35DE6` needed same-CODE-segment table access; tested near/far externals chose DS/DGROUP-related forms, while named based-segment spellings were rejected by pinned MSC 5.10.  The endurance handoff calls this a compiler-generation capability boundary, not a Luna failure.  Other endurance objects contained local-symbol B4/B6 records that the generic research reader parsed but the strict production reader intentionally rejected. [endurance-001/handoff.md, lines 1-24; supervisor-instructions.md, lines 15-16]

**Scope.** Do not infer an MSC 7, Turbo C, GCC, or another OMF reader result.  The portable lesson is to record the exact unsupported feature and preserve its object evidence rather than consuming source-search budget.

## Representative trajectories

### Matched Luna/Astra routing pilot — controlled, but not a capability ranking

Identical frozen manifests and high reasoning were used for four pairs.  Both models got strict whole-image receipts for the two prequalified solvable replays (`copy_string`, `rect_compare_point`) and neither solved the two unresolved cases.  Direct Standard-equivalent worker scenarios were $5.21717 Astra versus $0.08130442 Luna, but root supervision added $26.25143 plus unpriced auto-review traffic.  The recorded decision retains Luna/high first with evidence-driven escalation because no Astra-only solve was observed, while explicitly refusing an equal-capability claim. [model-routing/decision.md, lines 1-29; model-routing/results.json, lines 1-2956]

The important failure interpretation is procedural: two Luna trials were precompiler-blocked by an omitted profile, and Astra's QuickC BAKPAT event was tooling-blocked; neither is a model failure.  None of the unresolved runs reached the 15-hypothesis/20-process cap.  This is a compact cost/decision trajectory, not a repository solve-rate estimate. [model-routing/decision.md, lines 18-29]

### `unknown_libname_1` bounded batch versus adaptive sequence — efficiency signals without a recovery result

Two Luna/high workers began from the same archived attempt and caps.  The sequential lane made four candidates/four outputs; the predeclared batch made three/two outputs.  The batch used 23% fewer requests, 9% less wall time, and 15% less direct worker cost, but it produced half as many unique outputs and neither arm matched strictly.  The batch's identities were a subset of sequential identities. [batching-decision.md, lines 1-28]

The durable conclusion is conditional: batch a small set of independent evidence-backed alternatives, deduplicate their effects, and preserve adaptive sequencing where each result changes the next question.  One target, different candidate sets and no strict successes cannot estimate an optimal batch size or recovery throughput. [batching-decision.md, lines 20-28]

### `is_facing_camera` — stack-home discovery, retained six-byte gap, then a targeted negative fixture

The initial symptom was a 200-byte target versus repeated 194-byte ordinary-C outputs.  Declaration ordering explained the paired BP-home permutation, but not the branch/return gap.  A controlled negative-polarity follow-up held that ordering fixed: it made a third 194-byte output, retained the corrected BP homes, lost two late anchors, and did not produce AL/CBW.  Separately, two MSC 5.1 fixtures compared early return with an explicit trailing zero-return label.  They emitted identical 38-byte contributions, retaining AL/CBW while canonicalizing the zero path first; the label theory was refuted under those exact fixtures. [declaration-order-20260923.md, lines 1-17; boolean-return-placement/README.md, lines 1-7]

This trajectory changed analysis level from declaration/local layout to independently supported boolean-return or TU/compiler-context evidence.  The supervisor keeps the family blocked; the two scoped negatives are not evidence that all control-flow spellings are equivalent in MSC. [supervisor-instructions.md, lines 9-13]

## Negative evidence worth carrying forward

1. **No Astra-first task class is established.** The matched four-pair pilot has no Astra-only solve; the two successes were prequalified replays and no new C bytes were recovered. [model-routing/decision.md, lines 1-29]
2. **Worker direct cost is not end-to-end economics.** The pilot's supervisor scenario exceeded cheap worker cost, and auto-review traffic was unpriced.  Cost claims must include supervisor, cached input, output and handoff overhead. [model-routing/decision.md, lines 18-29; worker-research.md, lines 39-45]
3. **Batching has no demonstrated recovery-throughput advantage.** Its one pair saved requests/time/cost but found fewer identities and zero strict matches. [batching-decision.md, lines 13-28]
4. **An explicit trailing zero-return label did not move MSC 5.1's epilogue in the two fixtures.** Both 38-byte contributions were identical; do not re-run that exact source axis as a camera solution. [boolean-return-placement/README.md, lines 1-7]
5. **The corrected camera declaration order plus tested negative polarity still missed.** It retained 194 rather than 200 bytes, lost two late anchors and did not produce AL/CBW; this excludes that polarity form only. [declaration-order-20260923.md, lines 13-17]
6. **Same-output source rewrites are not new evidence.** The endurance cohort records source-level convergence repeats and cross-profile repeats; only context-bound effective identities count as different outcomes. [endurance-001/handoff.md, lines 1-24]
7. **Pinned MSC 5.10 did not accept the tested named based-segment forms.** This excludes those spellings in the documented `sub_35DE6` conditions, not every way of expressing a CODE-segment access. [endurance-001/handoff.md, lines 1-24]

## Tool inventory and reuse judgment

No `LICENSE*`, `COPYING*`, or `NOTICE*` file was found in the Stunts source inventory.  All entries below are references only: do not copy code until provenance/licensing is resolved.

| Tool | Class | Why it matters | Main limits |
|---|---|---|---|
| `tools/coordinates.py` | adapter_required | Explicit conversions between declared address spaces, with range checks. | Its concrete spaces/header/base values and `common.require` dependency need an adapter. |
| `tools/diagnostics.py` | conceptually_reusable | Pure candidate/oracle stream alignment, anchors, islands, operand patterns and compact summaries. | Capstone 5.0.3, x86-16 decoder, Stunts fixup semantics. |
| `tools/research_batch.py` | adapter_required | Archives preregistered candidates, enforces a process ceiling, deduplicates effective outputs, and reports candidate-to-oracle and candidate-to-candidate deltas. | Imports Stunts context index/cards, MZ parsing, workflow snapshots and compiler recipes. |
| `tools/check_candidate.py` | project_specific | Fresh FAST/staged/canonical acceptance with scope/manifest locks. | Stunts build, queue and serial-promotion policy. |
| `tools/oracle.py` | adapter_required | Locates, hashes, locks and optionally materializes pristine oracle input. | MCGA assets, EXEPACK/MZ workflow and `layout/oracle.lock.json`. |
| `tools/inspect_object.py` | project_specific | OMF object inspection and private research receipts, including local Microsoft records. | Stunts OMF evidence schema/private-root policy. |
| `tools/probe_tu.py` | adapter_required | Compiles a controlled TU probe and checks oracle evidence. | Stunts compiler runner and MZ oracle; the probe pattern is portable. |
| `tools/grind.py` | project_specific | Budget accounting, attempt archival and guarded promotion orchestration. | Stunts candidates, cards, queue, exact build and workflow snapshots. |

The first viable shared extraction is a pure-data effective-output/experiment-matrix library: explicit input identity, profile/context-aware effective identity, predeclared hypotheses/predictions/falsifiers, pairwise deltas and stop classification.  Keep historical compiler runners, MZ/OMF parsers, binder modes, queue policies and acceptance gates as adapters.

## Sources and freshness

`records.json` is the machine-readable dossier.  Its source manifest stores each cited source's repository-relative path, ref (`HEAD` or `working-tree`), SHA-256, working-tree flag/status and useful line anchors.  In particular, the live generated status/workflow documents and two untracked research artifacts are recorded by working-tree hashes; their content may not be reconstructed from `068ff2e` alone.
