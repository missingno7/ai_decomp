# Designing experiments that teach something

The [adversarial synthesis](../research/adversarial-synthesis-20260923.md)
adds region influence, fresh blocker capability and historical replay experiments.

The procedures below are **GENERIC METHOD** proposals grounded in the
[project trajectories](trajectories.md). Compiler effects remain **PROJECT
FACTS** at their cited source context.

1. Freeze the oracle and baseline: source/include identities, historical tool
   hashes, flags, unit composition/order, ABI, runner and verifier version.
   Reproduce the existing result before changing a variable. Define address
   coordinates and proof scope explicitly.
2. Describe the residue by dimension: opcode/operand/register/stack home,
   CFG/call count, extent/alignment, fixup target/frame/addend/order, private
   DATA/BSS/CONST, or neighboring regression. Keep uncertain decoder/binder
   output separate from observations.
3. State a hypothesis, predicted discriminating output and falsifier *before*
   compiling. "Try a different spelling" lacks a prediction. "Reversing these
   local declarations moves these two BP homes while preserving extent" is
   testable; Stunts' camera probe demonstrates the distinction.
4. Batch independent axes only when each has a useful interpretation without
   seeing the others. Keep sequential stages when the first result changes
   the next question: source/type → operand collapse → context → strict unit
   proof. Preserve every candidate and the compiler process count.
5. Compare candidate to parent and candidate to oracle. A parent delta isolates
   what the edit did; oracle correspondence evaluates relevance. Neither raw
   positional byte difference nor aligned similarity is strict acceptance.
6. Group equivalent effective outputs within a stated identity contract. Keep
   source hashes, full object hashes and normalized diagnostic identities
   distinct. Equal code alone does not collapse different fixup/layout results.
   Compilation failures have no output identity and form no equivalence class.
7. Preserve informative branches when dimensions trade off. Do not discard
   one candidate just because another is shorter if it preserves a different
   exact anchor or binding. Publish the matrix, not an unexplained "best" score.
8. Stop or change analysis level for a stated reason. Search convergence means
   the tested axes stopped distinguishing outcomes; budget-censored means work
   ended before that claim was justified. Tooling/evidence blocks are separate.
9. Run the project's strict verifier for any proposed promotion. Retain its
   scope, receipt, input fingerprint and freshness. Analysis tools never grant
   acceptance or erase unresolved obligations.

Sources: Stunts `worker-research.md`, `research_batch.py`, camera and batching
trajectories; SimAnt factory, FloodNestB and unit assembly trajectories; Icy
Tower draw/pass/context and storage-scope trajectories; Empires GAME/MUSIC and
fresh-acceptance records, all resolved by [catalog sources](../catalog/sources.json).

## Changing the analysis level

| Evidence after controlled tests | Useful next question | Existing precedent |
|---|---|---|
| Many spellings, same emitted object | Did the compiler canonicalize the varied axis? Which axis can change liveness/type/context? | SimAnt FloodNestB; Stunts output collapse |
| Body exact, binding/private data wrong | Is the isolated function missing unit ownership/selector context? | SimAnt scaffolded units |
| Body exact, relocation order wrong | Does the compile route or module grouping differ? | Empires MUSIC |
| Unchanged body changes with predecessor | Which predecessor/lifetime/compiler state separates outputs while preserving peers? | Icy HTTP/scroller |
| Repeated CFG spellings converge late | At which compiler pass is the needed distinction removed? | Icy `play` at `181r.csa` |
| Compiler rejects syntax or strict parser rejects an object | Is the feature available in the pinned version, or is support missing? | Stunts based-segment and B4/B6 cases |
| More exact anchors but extent still wrong | What distinct dimension remains? Does the proposed mechanism actually predict it? | Stunts camera; SimAnt alignment failures |

Compiler-pass inspection is appropriate only when available and informative for
that compiler. Do not import GCC pass names as explanations for MSC results.

The [minimal experiment contract](../experiments/README.md) records missing
information explicitly. An old receipt can be useful historical evidence without
inventing its absent prediction, falsifier, timing or parent identity.

## Comparing worker policies

Freeze the same evidence, tools, eligible task cohort and allowed runway;
record model/effort and independent seed/lineage, including failed launches.
Preregister native proof scope, stop rules and shared replica budgets. Report
strict outcomes alongside hypotheses, model requests, meaningful reasoning
rounds when identifiable, compiler processes, effective outputs and experiments
that discriminate a stated hypothesis. These counters are not interchangeable.

Separate preparation from recurring supervision/review, retain cached-token
buckets without double counting, and leave unpriced costs unknown. Historical
host timing is context, not a primary model comparison. Useful late solves and
mechanisms need receipts; zero new solves cannot estimate cost per new solve.
Search convergence is scoped to tested axes and evidence, not model exhaustion.
The [fleet review](../research/fleet/evaluation.md) derives an accounting
break-even and identifies what the small Stunts cohort cannot estimate.

Two to four redundant cheap workers are an experiment, not a throughput rule.
Use separate candidates and conversations, measure marginal output diversity
and cost, and cancel remaining branches only after equivalent-scope native
strict confirmation. Changing model or replica must not reset the task budget.
Link per-experiment records through optional `fleet_context`; aggregate terminal
task records through the separate [fleet contract](../experiments/fleet-results.md).

## Context, scope and response-map controls

Name edit, compile, measurement, protected and acceptance scopes separately.
Use [recovery scopes](recovery-levels.md) rather than assuming every experiment
is a function-local mutation. Hypotheses can concern evidence or a binder, not
only C spelling. A changed classifier requires a discriminating follow-up; it
is not automatically a discovered cause.

For regions, hash-bind source spans and retain possibly disjoint machine sets.
Unknown liveness or source-to-instruction correspondence stays unknown. Reproduce
the native whole-unit baseline and a no-op control before interpreting influence;
annotation/inlining changes can alter budgets without improving code. Two local
edits need a combined trial before assuming their effects compose. See the
[five-compile proposal](large-function-regions.md).

Prefer “empirical compiler response map” to “gradient.” Keep equal-output
observations across deliberately varied contexts, but do not reuse a cache or
proof across those contexts without its native identity contract. Compare
output vectors and protected-state losses, not just target similarity.

Stage/model comparisons require frozen tools/evidence and leakage controls;
a worktree alone exposes future Git history. The
[historical replay design](../docs/historical-replay.md) identifies exact
pre-mechanism snapshots and scores strict recovery separately from validated
mechanism fan-out. None has been executed here.
