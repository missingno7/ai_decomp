# Compact fleet result contract and offline reducer

**GENERIC METHOD; prototype implemented in ai_decomp only.**
[fleet-schema.json](fleet-schema.json) describes a run envelope containing bounded
task results and a separate cost ledger. [fleet_report.py](../tools/fleet_report.py)
validates it and emits a JSON morning-summary foundation. It reads one file,
writes stdout and never launches workers, executes compilers, accesses siblings,
selects a model, changes a queue or promotes source.

This is the smallest common representation justified by the
[fleet review](../research/fleet/evaluation.md). It complements individual
[experiment records](README.md), which can reference a fleet `run_id`, `task_id`,
`result_id` and `lineage_id` through optional `fleet_context`.

| Group | Required semantics |
|---|---|
| Run/result identity | Stable run and result IDs; one terminal record per bounded task investigation. Identical reimports are ignored and counted; conflicting reused IDs are rejected |
| Task identity | Project, target, frozen seed and compiler/source-context identifiers. Unknown identities must be explicitly labeled; they do not justify cross-context clustering |
| Worker provenance | Worker, reported lineage, exact model and reasoning effort; use `unknown` when absent. A lineage tracks shared search history, not a fresh worker name |
| Stop reason | `accepted`, `promotion_candidate`, `search_converged`, `budget_censored`, `tooling_blocked`, `evidence_blocked`, `production_blocked`, `systemic_mechanism_suspected`, `interrupted`, `cancelled_redundant`, `unknown` |
| Strict result | `pass/fail/not_run/unknown`; pass/fail includes scope, verifier and receipt. Metadata does not verify the referenced receipt |
| Promotion | Separate `not_requested/candidate/queued/promoted/blocked/unknown`; exact candidate/queued/promoted requires a strict pass. `accepted` requires native promotion. A promoted result needs a distinct native transaction reference; a common bundle may use distinct anchors |
| Counters | Hypotheses, requests, meaningful reasoning rounds, compiler processes, run-local unique outputs, information-producing experiments; absent/null stays unknown. A request is not automatically a reasoning round |
| Tokens | Input including cached subset; output including reasoning subset. Do not add subset buckets to their totals. Optional accounting extensions can retain cache writes, retries and rate details |
| Cost ledger | Stable usage-group ID, role, amount or null, currency/unit, immutable price/scenario basis and optional result links. Roles are worker, supervisor, preparation, review, infrastructure |
| Blocker | Optional explicit project-classified signature: compiler profile, ABI, analysis level, mismatch family, context comparison domain and diagnostic version; evidence references required |
| Artifacts/extensions | Full logs remain at references with source-manifest identity. Preserve native status, partial/censored metrics, human contributions and missing attribution rather than guessing |

The stop reason explains why this investigation ended. It does not say that the
worker should terminate its whole nightly run. Production/workflow blocked is
different from a source failure, and a suspected systemic cause is still a
hypothesis. Native blocking and reissue rules remain authoritative.

## What the reducer guarantees

The reducer rejects conflicting result/cost IDs, invalid or nonfinite counters
and costs, impossible token subsets and proof/promotion metadata contradictions.
It exposes all strict statuses separately so an unknown is not counted as a
failure. Repeated strict passes on one project/target/context/scope count as
multiple result receipts but one target scope; they never become additional
production promotions. `promotions` counts result statuses; the separate
`distinct_reported_promotion_transactions` deduplicates project/transaction
references. Even a distinct reference is only reported metadata, not proof
that a new production change occurred.

Costs with different bases/currencies remain separate. Unknown items remain
unknown and omitted accounting roles are listed. `listed_items_priced` means
only that the *listed* entries have amounts, not that the run has full coverage.
Do not include a root subtotal as well as an all-preparation subtotal containing
the same root. Assign IDs from raw usage groups to make duplicate import visible.
The reducer cannot detect semantic double counting disguised with different IDs.

It groups blocker signatures only when project and all signature fields agree.
It labels single reports, repeats within one lineage and cross-lineage reports
separately. None proves a shared cause or independence. The summary does not
automatically send clusters to Sol. A supervisor should inspect representative
evidence and choose a falsifiable mechanism question.

The sum of `unique_effective_outputs` is deliberately named within-result work;
it is not cross-run novelty. Use [experiment_matrix.py](../tools/experiment_matrix.py)
with complete context/output identities for that separate operation. Missing
histories cannot be repaired by summing counters. Distinct outputs and information-
producing experiments are separate metrics.

## Real archived replay

```powershell
python tools/fleet_report.py research/fleet/stunts-replay.json
python -m unittest discover -s tests
```

The [Stunts replay](../research/fleet/stunts-replay.json) imports the eight
matched runs from the [raw-derived extraction](../research/fleet/stunts.json).
It preserves 44 hypotheses, 121 model requests, 50 compiler processes and 30
summed run-local output classes. The independent case-union count of 24 stays
in the source study; the reducer does not infer it. Four strict pass results
represent two target scopes. They are historical capsule replay candidates,
not four new production promotions. Unsolved runs have unknown final strict
status rather than invented full-scope failed receipts.

Model requests are known; meaningful reasoning rounds and information-producing
experiment counts are unavailable. Costs retain the archived Standard scenario,
root supervision and an explicitly unpriced remainder. They are not an invoice.
Worker-reported source-form exhaustion maps to `search_converged` with that
limited interpretation; it is not model exhaustion. Full source/receipt paths
remain in the owning project's hash-pinned report.

The replay's extraction identity uses `canonical-json-v1`: sorted keys, compact
separators, ASCII escaping, UTF-8 bytes and SHA-256. This makes the local metadata
link insensitive to Git line endings. It does not normalize any oracle/object
identity or change the raw source-file hashes retained by the study.

The replay demonstrates accounting fidelity and conservative missing-data
handling. It does **not** measure better model routing, recovery throughput,
supervisor savings, independent replica value or crash-safe scheduling. Tests
cover idempotence, conflicting IDs, proof/promotion separation, repeated target
wins, blocker domain/lineage separation, unknown costs and invalid token counts.

## Fields still needed for an actual controller

Native adapters must supply claim/lease ownership, remaining global/task budget,
checkpoint and cancellation boundaries, evidence freshness, protected peer/TU
sets, promotion journals and recovery policy. Those are not implemented by this
representation. A future live cohort should record tool errors, interrupted
workers and useful late solves with denominators; one optimistic aggregate
must not become a model failure-rate estimate. The next test is a bounded native
pilot with equal tools/evidence/runway and complete worker/supervisor accounting,
not deployment of a generic distributed scheduler.
