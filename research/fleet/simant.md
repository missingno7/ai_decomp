# SimAnt fleet falsification audit

**PROJECT FACT — observed 2026-09-23.** This is a read-only snapshot of the
active `simantw_recon` checkout at `105963ffe35ee4e801f8e1e56ea207cc3b16ee81`.
The sources and receipts named in [the companion JSON](simant.json) are live
working-tree bytes identified by SHA-256. They are evidence of this checkout,
not a claim about a future run. No SimAnt build, compiler, model, queue refresh,
or promotion was run for this audit.

## What the receipts establish

The job ledger contained 786 jobs: 286 `PROMOTED`, 472 `ESCALATED`, 24
`SUPERSEDED_BY_TU`, two `OPEN`, and two `NEEDS_REVISION`. It recorded 2,683
attempts. Of the 286 promoted jobs, 135 (47.2%) needed more than one recorded
attempt; the largest recorded successful count was 11. These are ledger counts,
not a controlled model success rate: jobs differ in size, source provenance,
human involvement, retry budget and date, and old records may be superseded.
The sanitized per-job [census](simant-job-census.json) pins the 786 observed
`job.json` paths and hashes with status and attempt count, so these aggregates
can be recomputed without copying candidates or target bytes.

There is a concrete recent late recovery. `_MagnifyMenu` was created on
2026-09-23, had seven one-candidate `NO_COMPLETE_MATCH` attempts, and reached
`STRONGLY_SUPPORTED_MEMBER` on attempt eight. Its promotion records a fresh
MSC 7.00 compilation under `/AL /G2 /Gs /Oeglw /NTANTEDIT_MODULE`; its code
contribution is 472 bytes, of which 342 non-relocation literal bytes compare
equal and 46/46 fixups are validated separately, then it enters the independent
promotion path. The final experiment was a declaration-order question for
local points and rectangles. This supports a narrow conclusion: bounded,
evidence-changing iterations can recover a member late in a sequence. It does
not show that a particular model discovered the change.

The September-20 handoff calls the IsItWall pilot a validated workflow test:
eight generated variants, a fresh admission and transactional promotion, with
the cache replay rechecking comparisons. The newer validation receipt reports
216 passing tests, an eight-candidate cache replay, five exact candidates in
that replay, and a four-worker stress result of 400 jobs in 50.53 seconds with
eight environment launches. These are infrastructure/parity measurements, not
an overnight recovery throughput or model-quality benchmark.

There is no `Luna`, provider, model-version, prompt digest, token count or
agent identity in the inspected job schemas, results or compiler receipts. The
receipt binds source, source hash, flags, MSC worker implementation and timing;
it cannot bind who wrote the source. The handoff says explicitly that no
particular cheap model had been benchmarked. References to a “cheap model” are
operating instructions, while a `sonnet` brief is likewise a prompt filename.
Therefore any attribution of these promotions to Luna is **unsupported by the
durable evidence inspected**. A future fleet record needs a model-run envelope
linked to the submission digest if that attribution matters.

## What supports unattended bounded work

The workflow is materially safer than an unbounded loop. It limits a normal job
to eight attempts, 96 variants per attempt and 192 candidates total (unless a
recorded extension changes the attempt count); rejects a repeated semantic
experiment digest; records the pending output and PID before compilation; and
uses atomic replace writes. A compare-and-commit check stops an attempt whose
job state changed while it ran. An exact tested source is recompiled without
the cache for promotion, whose OMF/member proof checks code scope, public
placement, literal contributions, semantic fixups, private contributions and
the complete proposed manifest. Core changes use a PREPARED/COMMITTED journal;
restart either reconciles a committed promotion or rolls back a prepared one.

Locking is practical for several grinders on one shared filesystem. A short
OS file lock serializes queue allocation, refreshes and core transactions.
Each job has a nonblocking per-job lock, held through compilation, so separate
jobs can compile concurrently. Startup sees a `RUNNING` job whose job lock is
free as interrupted and escalates it rather than silently rerunning it. The
compiler service has a separate service lock, immutable source snapshots,
implementation signatures, heartbeats, up to four isolated persistent
Win3.1/DOSBox C7 workers, 96-job worker recycling and interruption receipts.

**Allocation boundary caveat.** `grind.py next` does not retain a claim while
the selected worker reasons. It briefly tests whether the active job lock is
free, releases the global lock, and `inspect`/`next_task` returns the same
`OPEN` or `NEEDS_REVISION` job without an owner, lease, or state transition.
Two autonomous workers can therefore receive the same active job between
commands. Worse, `grind.py test` copies an external candidate to the shared
job `candidate.c` and writes the shared `submission.json` *before* taking the
per-job lock. The lock serializes `run_attempt`, but it does not prevent a
second worker from replacing those inputs while the first waits or compiles.
The native parallel claim is sound for separately assigned symbols; the
`sonnet-grinder-brief` makes that assignment an external operational rule and
forbids its parallel workers from calling `next`. It is not a safe autonomous
ownership protocol.

This is not yet a complete overnight fleet controller. There is no durable
global cost/token/time budget, fair scheduler, lease/heartbeat per job owner,
cross-host coordinator, retry policy for a stalled model, or durable model-run
provenance. `recover_interrupted_attempts` infers interruption from a free file
lock, not from a verified owner process/lease. The service preserves queued or
interrupted evidence and fails callers, but does not itself choose a new source
hypothesis. The documented worker limit is four, while the direct `Win31Worker`
class does not constitute a global machine-wide resource governor. These are
implementation-scope absences, not evidence that a specific crash loses proof.

## Mechanism feedback that moves work downward

The machinery does distinguish a useful structural finding from another local
rewrite. A topology diagnosis with an otherwise matching body automatically
parks the job as `DATA_LAYOUT` and asks for grouped private bindings/TU work.
The documented `_vocMciClose` case preserves a body match but rejects the
single-function source because three private words belong to a wider
`GR_MODULE` data block; it was later superseded by a TU promotion. That is a
real downstream path from a compiler response to a tool-level TU experiment.
The factory also carries profile, unit context, known relocations and declared
reconstruction rules in the worker packet, rather than treating all errors as
source spelling problems.

The records also falsify careless escalation. `_UpdateEditIfBufInvalid` had a
correct body but a provisional `_DrawEdit` binding; a fresh profile/context
retest identified an unnamed same-segment helper at a different offset. Calling
that residue “needs more TU context” would have hidden a wrong symbolic
binding. Conversely `_win_DrawBitMap` retained the semantics across four
isolated source forms and reported an optimizer anchor-choice residue, with a
specific whole-TU or profile experiment next. The system records these as
different causes, but the taxonomy is still rule-based: it has no learned
causal model that proves a semantic error versus context from one score.

## Implication for shared tooling

Reuse the evidence contract, immutable candidate/receipt binding, job
transaction pattern and structured escalation vocabulary as project-specific
precedents. Do not call the current workflow an autonomous Luna fleet or use
its job outcomes as model evaluation. The shared layer should add a separate
run/worker provenance record, atomic job claiming with a lease and
candidate-isolated attempt inputs, global budget semantics, and a
candidate-parent-oracle outcome table that can retain effective-output clusters
without weakening each project's independent acceptance gate.
