# Falsification review: cheap verified search and mechanism escalation

**Decision, 2026-09-23:** the evidence supports a **bounded Luna-first trial**
on eligible, independently verifiable work. It does not establish the economics
of a large fleet, long unbounded investigations, Sol's comparative advantage,
or near-zero need for Astra. Keep those as **WORKING HYPOTHESES**. The durable
cross-project observations support the experimental and proof discipline, not
the proposed model hierarchy.

This pass re-read raw Stunts run/usage/trial records and project implementations.
Sources and limitations are in [Stunts](stunts.md), [SimAnt](simant.md), and
[Icy/Empires](icy-empires.md), each with a hashed source manifest. No sibling
build, model call, queue refresh or promotion was performed. The completed
[external audit](../../knowledge/ecosystem.md) is reconciled below.
The [validation record](validation.md) distinguishes passed metadata checks
from active-source drift and untested live concurrency/recovery behavior.

## Attempting to falsify each premise

| Proposed premise | Counterevidence / boundary | Narrow conclusion retained |
|---|---|---|
| A strict oracle makes workers safe | Code-only matches miss Empires relocation order, SimAnt private bindings and Icy ownership; an agent allowed to edit its checker can corrupt the boundary | Acceptance must remain project-owned, independent, scope-complete and freshly rerun |
| Compiler experiments are cheap | Local services have finite slots; verification may recompile several times; old timing is host-specific | Model interaction dominated the recorded Stunts cohort; measure queue/verification costs on the current host |
| Many tasks are independent | Whole-TU source, shared private data, predecessor state and serialized publication couple tasks; Empires frozen queue is empty | Parallelize isolated proposals, not unconstrained shared-source mutation or promotion |
| Existing job locks make autonomous queues safe | SimAnt releases its job-lock probe before returning an OPEN task and writes candidate inputs before the compile lock | Disjoint assignments work; shared autonomous consumption needs durable claims and isolated inputs |
| Failures produce information | Repeated outputs, invented bindings, unsupported objects and vague “context” diagnoses can produce no useful new evidence | Count discriminating observations separately from hypotheses and distinct outputs |
| Worker self-judgment is unnecessary | Oracle validates a candidate, not the proposed cause, completeness of evidence or safe workflow changes | Deterministic gates decide acceptance; mechanism claims still need controlled tests/review |
| Strong models belong on mechanisms | Shared tooling changes demonstrably unlock work, but discovery authors/models are generally unrecorded | Prefer escalation packets organized by mechanism; the best model for them is not measured |
| More cheap replicas are economically better | Correlated source priors can repeat the same outputs; supervisors and locks can dominate total cost | Use redundancy selectively and measure marginal diversity and downstream cost |

## Quantitative result from the matched Stunts cohort

**MEASURED FACT**, archived Standard-equivalent scenario, not an invoice or
current price quote. Five failed preflight-only launches are excluded from the
eight completed runs; those infrastructure events remain separately recorded.

| Metric | Luna/high | Astra/high | Meaning |
|---|---:|---:|---|
| Completed matched runs | 4 | 4 | Four selected case pairs |
| Strict successful runs | 2 | 2 | Same two prequalified replays; zero new production recovery |
| Meaningful source hypotheses | 25 | 19 | Luna/Astra = 1.32; not reasoning-round counts |
| Model requests | 67 | 54 | Ratio 1.24; requests include workflow interaction |
| Actual compiler processes | 27 | 23 | Ratio 1.17, including verification recompiles |
| Sum of run-local output classes | 15 | 15 | Distinct within runs; cross-model union is 24, not 30 |
| Input tokens, including cached | 3,246,459 | 2,488,612 | Do not add cached input again |
| Output tokens | 54,158 | 18,461 | Reasoning is a subset, not extra billed output |
| Direct model-weighted cost | $0.08130442 | $5.21717 | Astra/Luna = 64.17 in this scenario |
| Direct cost / run-local output class | $0.00542 | $0.34781 | Diagnostic work metric, not useful information or solves |

Luna/Astra hypothesis ratios by case are **1/1, 4/1, 9/9 and 11/8** for
copy, rectangle, parse and unknown-library respectively. Astra found the known
rectangle solution with fewer hypotheses. Both failed the selected unresolved
cases; no Astra-only solved mechanism was observed. Unresolved workers did not
exhaust the advertised 15-hypothesis/20-process cap. This is neither a population
success-rate estimate nor an adequately powered equivalence test. There is no
matched Sol arm and no measured distribution of meaningful reasoning rounds.

Root supervision was **$26.25143**, 182 requests and 20,467,474 total tokens:
**4.95 times** the combined direct-worker cost. All preparation *including that
root* had 471 requests and three unpriced groups. Thus direct plus root is a
known **$31.54990442 lower bound**, not the full cost; adding root to all
preparation would double count it. Much was evaluation/tooling preparation,
not necessarily recurring per-function overhead. Its steady-state amortization
is unknown. These numbers falsify “cheap workers automatically imply cheap fleet.”

The separate batching pair had no strict solve: sequential 4 candidates/4
outputs, batch 3/2. Direct scenario costs were $0.01465454 and $0.01242460.
Batching reduced requests (13→10) but also diversity. It is not a measured
throughput improvement. The earlier host recorded roughly 25.1 seconds of
trial-helper time versus 2,342 seconds of worker launches across the matched
pilot. That is a local overhead signal, **not portable elapsed-time economics**;
helper duration is not a pure compiler CPU measurement.

Unavailable: matched Sol performance, probability of useful late solves by
model, all-in cost per *new* strict recovery, population worker failure rates,
causal information gain, value of systemic discoveries, and current-host scaling.
Two unsolved functions are not two crashed workers. A parser/profile failure
does not establish a model limitation.

## What the other projects establish—and do not

**PROJECT FACT:** SimAnt's fresh census contains 786 jobs, 286 promoted,
2,683 attempts, and 135 promoted jobs with more than one recorded attempt.
MagnifyMenu gives a concrete late exact result on attempt eight after seven
misses. This refutes an arbitrary “three failures means incapable” rule. It does
not justify relaxing native caps or indefinite search: records mix old budgets,
extensions, context changes and authorship. Durable jobs/receipts do not identify
Luna or another model, so no model-attributed recovery rate follows.

SimAnt also supplies a concrete scheduling counterexample: per-job locks do
not cover ownership between model calls, and candidate submission mutates
shared inputs before acquiring the compile lock. The existing multi-worker
brief uses disjoint symbol lists and forbids `next`. A general unattended
shared queue is therefore not ready merely because its compiler service is.

**PROJECT FACT:** Icy's mechanical census records 34 summaries and 87 terminal
outcomes, including 70 promotions, with explicit blocked/review/recovery states.
These are interface/type/source-order tasks, not 70 newly recovered C function
bodies. Scope/ownership repair and TU/pass diagnostics provide real information;
the draw study's 23 probes/21 outputs still did not solve the target and regressed
protected neighbors. Luna-named folders are insufficient model provenance.

**PROJECT FACT:** frozen Empires proves full artifact closure, yet its retained
readiness file has no eligible cards and says the grinder run was not started.
It is strong evidence for an acceptance boundary and mechanism-to-rule workflow,
not for fleet throughput. Its documented serial source workflow contradicts
unqualified parallel mutation.

## Engineering break-even, not a fixed hypothesis multiplier

**GENERIC METHOD.** For a matched task class and horizon, define:

`C_m = worker model cost + preparation/context + supervision/review + compiler infrastructure + failure/recovery cost`.

Compare expected **new strict recoveries / C_m**, and report a separate vector
of validated reusable mechanisms and information-producing experiments. Do not
assign an arbitrary dollar value to “interesting failure” to make a policy win.
Record fixed evaluation setup separately from recurring costs and state any
amortization assumption. Subscriptions/credits and API scenarios are not invoices.

For a simplified same-quality comparison, let stronger work take `R` rounds at
average cost `b_S`, cheap work take `rR` at `b_L`, and let `H_m` cover other costs.
Cheap work is cheaper when:

`r < (H_S - H_L + R*b_S) / (R*b_L)`.

If strict success probabilities differ, compare `p_L/C_L` with `p_S/C_S`; for
the same simplification the bound becomes
`r < ((p_L/p_S)*(H_S + R*b_S) - H_L)/(R*b_L)`.
These are accounting identities, not estimated probabilities. Round length,
cache mix and context growth vary, so observed token buckets are preferable to
assuming fixed round costs. At zero observed new solves, cost-per-new-solve is
unavailable, not evidence of infinite model inefficiency.

**Provisional policy:** tolerate a few times more cheap search while useful
evidence continues within the same native budget. An approximately tenfold
*sustained matched-work* inflation is a reason to audit routing economics, not
an automatic escalation or a reason to wait for tenfold waste. Escalate earlier
for repeated well-evidenced mechanism convergence, material strict-yield
divergence, an infrastructure problem requiring tool work, or a valuable unique
case with a concrete higher-level question. No current cohort calibrates 10x
or any alternative universal threshold.

## Redundancy and mechanism escalation

**WORKING HYPOTHESIS:** ordinary work starts with one worker; a high-value,
uncertain, well-isolated task may justify two independent cheap branches before
expanding to four. Frozen inputs, separate contexts and an explicit no-shared-
findings policy are prerequisites for calling this an independent comparison.
Different worker IDs alone do not establish independence. Stunts' matched arms
show both shared and nonshared outputs, but do not test 2–4 Luna replicas.

For truly independent equal-success branches, `P(any solve)=1-(1-p)^k`;
correlated failures invalidate that estimate. Require expected marginal recovery
or useful new evidence per *incremental total cost* to beat assigning the slot
to another eligible task. Stop pending redundant work only after the native
gate confirms an equivalent-scope win; retain completed evidence. A shared task
budget must not reset when a replica or new context is created.

Repeated compatible symptoms make a useful supervisor packet, not proof of a
common cause. SimAnt's wrong helper binding and missing-store counterexamples,
and Icy's rejected scope analogy, falsify automatic “register residue = compiler
context” routing. Prefer systemic clusters, but do not require several functions
before investigating a unique high-impact mechanism.

Sol/high is a reasonable **experimental** next tier for a specific falsifiable
mechanism/tool/context question with affected targets, representative receipts,
negative controls, cost budget and expected reusable output. No inspected cohort
proves it optimal. Astra becomes justified by observed Sol-resistant work with
adequate tools/evidence/runway, or a controlled stronger-model advantage that
outweighs added cost. “Astra normally gets no work” remains untested.

## External overlap and next implementation

The [pinned audit](../../knowledge/ecosystem.md) already identifies permuter's
local/distributed candidate workers and coarse output hashes, Mizuchi's sequential
AI retries/background permuter, decomp.me's persistent scratch/context/three-way
view, objdiff's typed feedback and m2c's source prior. These are valuable parts;
none of the inspected integrations provides the whole historical-x86 fleet
contract with project-native transactional promotion, global model-cost budgets,
causal cluster review and restart-safe queue ownership. Echo supplies relevant
population-search prior art but its runnable artifact was not verified.

The smallest shared implementation is [fleet result metadata and an offline
report reducer](../../experiments/fleet-results.md). It joins worker provenance,
stop reasons, scoped proof, costs and already-classified blocker signatures;
it neither schedules work nor classifies causes. Replaying archived metadata
tests lossless accounting. Live fleet routing, economic benefit and large-scale
unattended operation still require a small preregistered cohort and native
recovery/isolation checks described in [fleet operation](../../knowledge/fleet-operation.md).
