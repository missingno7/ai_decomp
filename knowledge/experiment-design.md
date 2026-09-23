# Designing experiments that teach something

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
