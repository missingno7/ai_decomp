# Bounded fleet operation and mechanism escalation

**Status:** experimental routing policy plus **GENERIC METHOD** workflow
guidance, supported at the narrower strength in the
[falsification review](../research/fleet/evaluation.md). A large Luna/high fleet,
Sol's economic superiority on mechanisms, and exceptional-only Astra use remain
**WORKING HYPOTHESES**. No fleet or recurring automation was started by this study.

## Routing without confusing function difficulty and mechanism difficulty

| Queue role | Provisional worker | Entry and exit conditions |
|---|---|---|
| NORMAL_RECOVERY | One Luna/high | Native eligible task, sufficient evidence, isolated candidate, strict gate; retain native attempt caps |
| RESEARCH | Luna/high with an explicit wider budget if the project permits | Falsifiable unfamiliar hypothesis; frozen evidence and broader analysis levels, not unlimited repeats |
| REDUNDANT_RESEARCH | Initially two independent cheap branches; up to four only if justified | High value/uncertainty, meaningful alternative approaches, shared total task budget; compare marginal diversity |
| SYSTEMIC_CLUSTER | Trial Sol/high | Compatible scoped recurrence or a single high-impact mechanism question; compact representative evidence and a reusable deliverable |
| EXCEPTIONAL_UNRESOLVED | Consider Astra with a bounded experiment | Adequate tools/evidence/runway, documented Sol-resistant mechanism, or controlled evidence that stronger reasoning changes strict yield economically |

These are shared routing labels, not a replacement for native queue states.
An ordinary task is not a function count or instruction-count cutoff. No
function goes upward solely because three attempts failed. Conversely, do not
wait for several functions to fail before escalating a unique build/ABI problem
that blocks much work. Missing tools/evidence should go to the responsible
maintenance/research process, not be charged as model inability.

The user's 10x notion is a useful **audit alarm** for sustained matched-work
inflation. It is not a stop rule, a measured threshold, or permission to ignore
low-information repeats. Compare incremental expected strict yield and useful
validated information per total cost; see the break-even equations in the
[review](../research/fleet/evaluation.md#engineering-break-even-not-a-fixed-hypothesis-multiplier).

## Worker loop and global run budget

One worker handles a sequence of bounded tasks, with an atomic project-owned
claim and private candidate inputs or externally preassigned disjoint jobs.
On an eligible task it records
the current source/compiler/evidence context, predicts a discriminating result,
compiles independent variants when useful, compares parent and oracle evidence,
and groups outputs under the native identity contract. Continue while the next
experiment can distinguish a live hypothesis and native budgets permit it.
After an exact candidate, queue project-native promotion; after a scoped block,
archive the result. Release ownership and take the next eligible task.

Solving or blocking one function does not terminate an otherwise healthy run.
Do terminate or pause the affected lane when a global budget is exhausted,
infrastructure fails, no eligible work remains, or a native review/recovery
condition requires attention. Do not turn a task-local budget into a new budget
by switching workers, resetting conversation or recreating a capsule.

A future controller needs a durable global ledger for model/token/process
budgets, stable task/result IDs, ownership and checkpoint reconciliation. The
new shared reducer does **not** implement that controller. Initially choose
concurrency from verified isolation and measured compiler/promotion capacity,
not from the number of cheap model calls affordable. Parallelism can lower
latency while increasing total work, lock contention and supervisor cost.

## Project-native readiness

Source-code inspection and existing tests/receipts establish the following
boundaries. They are not new fault-injection results.

| Project | Existing support | Safe scope / remaining prerequisites |
|---|---|---|
| SimAnt | Per-job compile locks, short global allocation/core lock, isolated compiler-service requests, pending attempt receipts and transaction journal | Parallel workers require externally disjoint assignments. `next` does not claim OPEN jobs, and `test` writes shared candidate inputs before its job lock. A shared autonomous queue needs durable claims and candidate-isolated submission. Retain native caps and fresh member admission; global model budget/watchdog also missing |
| Icy Tower | Continuous mechanical queue, bounded source session, protected-input snapshots, promotion/recovery locks, publication journal and restore path | Already supports guarded serial mechanical work. Parallel research needs separate overlays/checkouts; same checkout is not a general multi-body worker pool. Interface promotions are not body solves |
| Stunts | Frozen disposable research capsules; grinder exclusive lock; source/input snapshots; serial fresh hybrid promotion and rollback tests | Parallel research with separate candidates is plausible; production remains serial. Procedural capsule access restrictions are not an adversarial filesystem sandbox; stale-lock/reboot ownership needs explicit testing |
| Empires frozen closure | Serial instructions, scoped candidate snapshots, archive/restore, fresh uncached full-link acceptance | No eligible frozen work and no demonstrated fleet. Do not run several mutating workers against the shared runtime source; no inspected OS-level promotion journal/lock equivalent |

Evidence: [SimAnt implementation audit](../research/fleet/simant.md),
[Icy/Empires audit](../research/fleet/icy-empires.md),
[Stunts transaction audit](../research/fleet/stunts.md).

For a first unattended night, operate only lanes with native tested recovery and
isolation. SimAnt's autonomous `next` allocation is excluded until its ownership
gap is fixed; externally disjoint assignments are a narrower option. Limit
unverified lanes to isolated research and queued proposals.
An unresolved native recovery sentinel blocks that lane; another isolated lane
may continue if its evidence and resources are unaffected. Routine experiments
need no repeated human approval, while production exceptions remain subject to
the owning project's existing rules.

## Evening, restart, and morning protocol

Before a run, the owning project refreshes strict state, checks pending
transactions, records the queue/evidence/toolchain fingerprint and advertises
only eligible work. The runner snapshots a total budget and concurrency limit.
Verify ownership across model reasoning intervals, not just compiler calls:
a lock-protected attempt does not imply an exclusively claimed task. Until a
durable claim exists, use externally disjoint task lists or a single allocator.
Research lives in project-appropriate worktrees, overlays, capsules or separate
candidate files. Do not impose one mutation mechanism on all four projects.

During a run, save the candidate and experiment request before compilation;
write a terminal result only after artifacts are durable. Full logs stay local.
Normal source mismatch, useful negative evidence and blocked work are archived
and release the slot. Never silently continue after a failed native publication
or incomplete rollback. Model context may restart from a compact checkpoint;
the native task budget and negative history must survive it.

| Interruption | Required recovery behavior |
|---|---|
| Worker disappears / partial experiment | Inspect ownership plus pending receipts; preserve source/logs; mark interrupted or censored. No absent-output “equivalence class” |
| Compiler hangs or fails | Bound timeout; stop/recycle only the owning isolated compiler worker through its native path; retain tooling failure separately |
| Machine reboots | Reconcile native journals and pending work before reissuing; PID/file age alone does not prove safe ownership on every platform |
| Branch or source context becomes stale | Keep research evidence; rebuild the candidate under current protected context before production credit |
| Promotion lock held | Queue/back off within budget; do not delete a live lock. Recover a stale lock only using the project's ownership/recovery procedure |
| One redundant branch matches | Confirm native strict scope; cancel pending replicas at safe boundaries, archive in-flight results; do not stop unrelated compiler jobs |

Morning output should report distinct workers, tasks/targets and result records;
strict pass scopes and actual native promotions separately; useful observations;
search-converged, tooling/evidence/production-blocked, systemic-suspected,
budget-censored and interrupted counts; full cost coverage including unknown
review/infra costs; compatible blocker groups with reported lineage/seed counts;
and at most a few justified next investigations. Outcome tags may overlap
(a budget-censored task can yield useful evidence), so do not sum them as if
they were disjoint. Stable stop reasons are a separate disjoint count.

## Compact supervisor packet and downward capability lifecycle

Send Sol a blocker packet, not every transcript: context/profile/ABI domain,
affected tasks, representative parent/oracle deltas, output classes, tested
axes and falsifiers, missing evidence, protected peers, native strict scope,
one discriminating next question, resource budget and expected reusable artifact.
Do not merge “register mismatch” across compilers, memory models or incompatible
TUs. Repeated observations from one inherited conversation are one lineage,
not several independent discoveries.

After a discovery: retain the causal hypothesis and controls; validate it under
the original compiler; test a second affected case and a negative case when
available; state its applicability and counterexamples; encode the reusable
part as a diagnostic, bounded generator, context field, rule or deterministic
tool; test preservation/strict gates; version it; then put it in worker packets.
Reopen blocked work through the native new-evidence path. Retire or narrow the
rule when it fails outside its supported scope.

The process is already evidenced by SimAnt's declaration/TU/binding rules,
Icy's card diagnostics and scope/context tools, Empires' TASM/TU/link rules,
and Stunts' mismatch/binding diagnostics. **Model authorship is not established**
for most of these. The supported principle is to amortize validated discoveries,
whoever makes them. Repeated manual intervention is a workflow opportunity when
the mechanism can safely be encoded—not every subtle judgment must become code.

The [fleet metadata contract](../experiments/fleet-results.md) implements only
the shared representation and offline summary. Native execution, leases,
transactions, budgets and promotion remain project-owned until a live trial
demonstrates a narrower reusable boundary.

## Adversarial constraints on task size and escalation

The [new review](../research/adversarial-synthesis-20260923.md) does not strengthen
the model hierarchy into a fact. Icy has a selected large-function tail; Empires
had imported matching source; SimAnt blocker categories change under fresh context.
These populations do not estimate worker intelligence or failure rates.

A fleet report should distinguish observed residue clusters from supported causal
mechanisms and capability blocks, including context/freshness and lineage. A model
supervisor receives compatible evidence and a falsifiable mechanism question;
repetition of an old classifier label is insufficient. Preserve earlier labels
when a fresh report changes them. Do not silently relabel historical failures.

Regions can reduce context presented to a worker while retaining whole-function/TU
compilation. Their independence and safe merge boundaries remain unproven. Current
Icy sidecars are not job leases, instruction ownership or promotion certificates.
Do not expand fleet parallelism on the assumption that all giant functions have
independent regions. Use [influence controls](large-function-regions.md) first.
