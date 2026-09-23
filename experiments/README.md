# Minimal experiment and trajectory contract

This is a **GENERIC METHOD** proposal used only in `ai_decomp`. Existing
projects need not change their stores. It models an experiment's information,
not one compiler's internal behavior. See [schema.json](schema.json) and the
deliberately [synthetic fixture](examples/synthetic.json).

The validator checks self-reported metadata consistency, not the truth of a
compiler/verifier receipt. An `accepted` stop requires a strict pass; a strict
pass requires successful compilation and a scoped output identity. External
verification without a captured compile belongs in project extensions until
that provenance can be exported explicitly.

| Field | Meaning |
|---|---|
| `id`, `project`, `target` | Stable attempt identity and explicit target/proof coordinate context. |
| `compiler_context` | Identity plus toolchain/profile/flags/source/include/TU/order/ABI/runner facts; unknowns explicit. The matrix compares the full object. |
| `parent_candidate` | Parent identity/reference, or null when genuinely unavailable. |
| `hypothesis`, `prediction`, `falsifier` | Preregistered research question and observable separating outcomes. For historical imports, explicitly say "not recorded" rather than inventing them. |
| `changed_dimensions` | The source/context axes intentionally varied. |
| `compiler_process` | Status, process count, invocation/receipt, timing/cache info when known. No identity on a failed compile. |
| `effective_output_identity` | SHA256 algorithm/digest, scope and versioned normalizer; null if no trustworthy output identity. Raw object and normalized code/fixup identities remain different contracts. |
| `structured_delta` | Separate `candidate_vs_parent`, `candidate_vs_oracle`, `protected_neighbors` and unresolved dimensions; project extensions allowed. No universal scalar similarity. |
| `strict_result` | pass/fail/not_run/unknown, verifier, scope and receipt; freshness and unresolved obligations in extensions. |
| `facts_learned` | Observations with epistemic label, context and source references. |
| `stop_reason` | accepted, promotion_candidate, budget_censored, search_converged, tooling_blocked, evidence_blocked, production_blocked, systemic_mechanism_suspected, hypothesis_rejected, continue, unknown. |
| `fleet_context` | Optional run/task/result/lineage IDs connecting this experiment to a terminal fleet handoff. |
| `artifacts` | Repository-relative path + immutable ref/hash, content kind and role. No embedded oracle bytes. |
| `extensions` | Project-specific fields; preserve semantics rather than forcing a lossy common denominator. |

A trajectory records `id`, `project`, `target`, `epistemic_class`, `steps`,
`outcome`, `sources`, `limitations` and optional `experiment_ids`/`mechanisms`.
Each step separates observation from interpretation and links an attempt when
one is available. An authored summary may lack a historical preregistration;
the catalog does not fabricate it.
The proposed new-record contract is [trajectory-schema.json](trajectory-schema.json);
the extracted catalogs preserve their original authored chains rather than
pretending they were preregistered under this schema.

The representation fits the reviewed cases as follows:

| Case | Core contract | Necessary extension / unavailable evidence |
|---|---|---|
| Empires MUSIC | compiler route, whole-module parent, body-vs-topology delta, final executable receipt | Ordered relocation sequence contract; exact historical per-attempt process timing not recovered. |
| Stunts camera | declaration axis, BP-home parent delta, anchor/extent oracle delta, failed strict result | Operand-family correspondence and hybrid acceptance context; research parser support differs from production. |
| SimAnt DrawForSale | sequential parent attempts, source/binding hypotheses, literal/fixup deltas, admitted member | Private initialized DATA ownership, segment selector/fixup semantics and job-budget counters. |
| Icy source-order/scope | whole-CU baseline, order or scope axis, neighbor/contribution delta, partial or strict function result | DWARF evidence, natural emission offsets, ownership certificate, protected peer proof set. |

No real attempts are imported into the utility yet: the catalogs preserve their
original evidence instead. Synthetic fixture hashes and receipts are explicitly
test data, not recovery claims. The next validation is a lossless read-only
adapter for a small matched real cohort.

The separate [fleet-result contract](fleet-results.md) summarizes terminal tasks
and accounting rather than individual compiler experiments. Its real Stunts
replay does not imply those attempts have been losslessly imported into this
matrix. `promotion_candidate` requires a strict pass; only the fleet record
additionally distinguishes a reported native promotion receipt from
a candidate. Neither offline validator authenticates that receipt itself.


## Scope and diagnosis extensions

The [adversarial review](../research/adversarial-synthesis-20260923.md) narrows
how records should be interpreted. Within `extensions`, an optional
`research_scope` can hold `edit`, `compile`, `measurement`, `protected` and
`acceptance` references, with context-qualified dependency/evidence edges.
A source region is one possible edit scope; compilation usually stays larger.
Unknown edges and live interfaces must remain null or explicitly unknown.

Within `facts_learned` or a project extension, distinguish `observed_residue`,
`supported_mechanism`, `rejected_mechanism`, `unresolved_dimension` and
`workflow_capability_block`, each with evidence and applicability. Multiple kinds
may coexist. These are recommended extension meanings, not a new mandatory
classifier or a migration of old receipts. `REGISTER_ALLOCATION` alone conveys
an observed/suspected dimension, not a causal finding.

Use candidate-parent and candidate-oracle deltas as an empirical response map.
Cross-context output equality can be a valuable observation while still being
ineligible for context-equivalent cache/group reuse. Retain that distinction.
Region states, byte budgets and repeated blocker signatures grant no new strict
acceptance. See [scope guidance](../knowledge/recovery-levels.md).
