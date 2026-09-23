# What is worth sharing first?

The [tool catalog](../knowledge/tools.md) records inspected source paths,
inputs/outputs, dependencies, compiler/format assumptions and reuse classes.
All upstream tools are references only; local availability is not a copying
license. The two shared utilities below are new Python standard-library code
written for this workspace, with synthetic fixtures only.

| Operation | Best existing precedents | Decision |
|---|---|---|
| Context-scoped output grouping and outcome matrix | Stunts `research_batch.py`, SimAnt grinder/cache, Icy `effective_outcomes.py` | Implemented as `experiment_matrix.py`; accepts exported metadata, no compiler/parser coupling. |
| Provenance manifest verification | Empires construction fingerprints/cache; Stunts snapshot locks; Icy hash-bound receipts | Implemented `provenance_check.py`; verifies Git/live content identity only. |
| Candidate-parent-oracle structured delta | Stunts camera/family diagnostics and research batch; SimAnt `codegen_diff.py` | Contract provided in experiment records; decoder/binder-specific delta extraction remains local. |
| Instruction alignment/mismatch islands | Stunts detailed anchors/families; Icy bounded alignment; SimAnt diagnostic diff | Conceptual reuse or adapter extraction; do not normalize away strict obligations. |
| Whole-TU context probe | Empires route/group probes; Icy predecessor/source-order overlays; SimAnt composer | Share experimental recipe first; constructors and evidence semantics differ. |
| Compiler-pass comparison | Icy `rtl_evidence.py` | Valuable GCC-specific precedent, not yet independently shared across compilers. |
| Compiler batching/service | SimAnt persistent service; Stunts preregistered bounded batch | Preserve local runners; measure parity, isolation, startup and total costs before extraction. |
| Trajectory summary generation | All four attempt stores, but different detail/authority | Store compact authored chains now; automatic causal summarization risks unsupported stories. |
| OMF/COFF/NE/MZ/PE parsing and strict gates | Each project's verified parser/acceptance implementation | Keep project-local; shared language name or binary format name is insufficient abstraction evidence. |

No project has the universally "better" equivalent. Stunts is the stronger
precedent for diagnostic family/cost reporting; SimAnt for bounded service-backed
member recovery; Icy for DWARF/pass/context diagnosis; Empires for final ordered
link closure. Choose by proof problem and object format.

## Implemented utility contracts

`experiment_matrix.py INPUT.json` validates the proposed experiment records and
emits JSON on stdout. It clusters only successful outputs with matching project,
target, full compiler context and identity specification (scope, normalizer,
algorithm and digest). It retains every strict result and delta. Failed or
unknown compiles do not form a fake shared "null-output" class. Hash equality
does not imply semantic equivalence or acceptance. `--validate-only` checks the
contract without creating a matrix. See [experiment examples](../experiments/README.md).

`provenance_check.py` defaults to the local catalog and the workspace's common
parent. `--manifest` and `--parent` allow another compatible manifest/layout.
It reads exact Git commits or live files and reports drift/missing evidence;
path traversal outside a declared repository is rejected. It writes no source
repo, does not modify Git configuration, and performs no builds.

`build_catalogs.py` is deliberately a workspace-specific importer for the four
research handoffs. It is not classified as a shared decompilation utility.

## Next test with the highest expected value

**WORKING HYPOTHESIS.** Export a small matched set of real attempt metadata from
Stunts, SimAnt and Icy into the proposed schema using read-only adapters. Compare
the matrix against each project's native equivalence classes, including identical
code/different-fixup and same-output/different-context controls. Then measure
whether the handoff reduces repeated hypotheses and supervisor cost. Do this
before extracting a runner or expanding the schema. Any adapter writes should
be reviewed by the owning project; this pass does not change those repos.
