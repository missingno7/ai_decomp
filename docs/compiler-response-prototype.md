# Proposed next prototype: replayable compiler-response envelope

**Status: proposal, not an integration or measured result.** This is the
single highest-leverage next experiment after the [ecosystem study](../knowledge/ecosystem.md).
It extends the existing metadata matrix rather than introducing another
compiler service, decompiler or acceptance engine.

## Why this experiment first

The [local evidence](../research/ecosystem/local-requirements.md) shows repeated
source trials collapsing to the same outputs, cheap compiler work relative to
agent interaction, and useful escalation beyond spelling. External components
already provide search mechanics and rich diff records. What is unproven is
whether a common compact response can faithfully preserve the local evidence
and improve experiment selection. Testing that is cheaper and more broadly
useful than wiring Mizuchi or permuter into four different proof systems.

No prototype was implemented during the research pass: source inspection did
not demonstrate a drop-in external component currently duplicated badly across
two projects. A new live compiler/LLM integration would skip the user's
requirement for a small real value demonstration. This proposed replay supplies
the missing prerequisite without creating dependencies in sibling repositories.

## Minimal scope and inputs

Use one preserved SimAnt sequence with both collapsed and separating hypotheses
(MagnifyMenu, plus PlacePill negative classes if needed) and Stunts' archived
matched/batching cohort. Read only metadata, candidate source references,
comparisons and existing receipts. Keep input hashes and project provenance;
do not export oracle byte ranges, compiler packages or source to a service.
No recompilation or claim of fresh acceptance is necessary for a replay.

Extend [the existing schema](../experiments/schema.json) and
[matrix utility](../tools/experiment_matrix.py) only where the native exports
show a missing field. A response needs:

| Field group | Required meaning |
|---|---|
| Identity | Project/target/oracle; parent and candidate source hashes; compiler binary/version, flags, headers, runner, TU/build context; missing identity remains unknown |
| Hypothesis | Changed dimensions, proposed mechanism, prediction, falsifier, intended proof scope and predeclared batch membership |
| Compiler execution | Success/error/timeout, process count, elapsed time and immutable artifact references |
| Output identities | Raw artifact plus optional normalized code/fixup/data identities, each with scope and normalizer version; no cross-context merging |
| Three-way response | Candidate→parent effects and candidate→oracle residuals, separated into code/CFG/register/stack, fixup/binding, data/layout, peers and TU/pass observations |
| Search state | Output class; duplicates of; explained regressions; unresolved mechanisms; budget; proposed escalation level |
| Proof | Original project verifier, receipt identity/date and scope; diagnostic score separate; missing proof is never inferred from a cluster |

An opaque `structured_delta` dictionary already exists. Do not invent a
universal instruction/fixup schema before two native exports constrain it.
Use typed summaries with references into project-owned detailed reports;
retain an explicit unknown/unavailable state instead of silently dropping a
dimension. A future objdiff provider can populate diagnostic rows without
changing the acceptance interface.

## Experiment and acceptance for the prototype itself

1. Freeze two export cohorts and hash their source manifests. Record parser
   and normalizer versions. Preserve one context-changing or parser-rejected
   case to test the boundary, not only successful candidates.
2. Replay into the common matrix. Require the same membership of every native
   effective-output class. Any normalization disagreement is reported, never
   repaired by weakening the key. Keep source aliases and distinct strict receipts.
3. Render a compact parent/candidate/oracle response. Have a reviewer recover
   the original tested axis, observed effect, duplicate class, strict scope and
   next unresolved dimension without consulting hidden outcomes.
4. Measure response bytes/tokens, classification fidelity and duplicate-trial
   recognition against the original handoff. Historical replay can measure
   representation, not new recovery performance or causal model cost savings.
5. Only after fidelity succeeds, preregister a small unresolved-task comparison
   of original versus compact feedback with equal seeds, model, compiler/process
   budget and proof gate. Keep later known outcomes out of both task packets.

Stop if native classes or strict verdicts cannot be preserved, if the compact
view hides a material binding/context ambiguity, or if the two projects require
mostly incompatible data. Do not expand into a generic compiler platform to
rescue a failed abstraction. A successful replay justifies a narrow next adapter;
it is not evidence of better match rates.

## Subsequent integrations, in priority order

| Candidate | Isolated test before reuse | Reason to defer |
|---|---|---|
| objdiff CLI/WASM | A preserved Icy COFF target/candidate with register, relocation and data differences; compare typed output with native diagnostics | Useful rich interface, but one project's format; independent acceptance remains local |
| decomp-permuter finite variants/workers | Same small explicit source set through native compile/score adapter; check source parsing, process cap, full history and identity classes | Built-in ELF scorer cannot consume OMF; segmented C extensions and compilation context may defeat parser assumptions |
| binutils-omf diagnostics | Corpus with LOC/frame/target threads, ordering and private-data cases; compare decoded records with local parsers | Existing reader does not prove compatibility with each project's acceptance semantics |
| Mizuchi orchestration pieces | Feed the common envelope to one constrained tool with replayable model/timing logs | Current dependency stack and function match convention offer no proven advantage over existing project agents |

For permuter, let the AI choose bounded source axes and interpret outcomes;
let the mechanical engine enumerate/compile them. Preserve all outputs needed
for causal analysis, including regressions. Do not install random search as a
default supervisor or let its score-zero event grant strict acceptance.

Longer-term beam state should retain diverse mechanisms and analysis levels,
not just the top N scalar scores. Scoped negative evidence may guide retries,
but a failed axis under one compiler/TU is not a global forbidden transform.
These are design hypotheses to test after the response contract works.
