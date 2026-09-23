# Fleet falsification: Icy Tower and frozen Empires

**Scope.** This is a read-only, dated audit of the Icy Tower working tree at
`fc2000225df112de2cf248d92d23da8e839ca108` and of Empires' frozen
`historical-exact-oracle-v1` commit
`873d1df0f505601d760c6880cdea0c6ae3d81405`. It distinguishes a receipt from
an attribution claim. It does not rerun a compiler, a queue, or an acceptance
gate. Source identities are in the accompanying manifest.

## Icy Tower: measured automation, bounded meaning

**PROJECT FACT.** The fresh, sanitized [mechanical receipt census](icy-mechanical-census.json)
pins **34 summaries and 87 terminal task outcomes**: 70 `PROMOTED`, 13
`BLOCKED_SUPERVISOR`, three `STOPPED_FOR_REVIEW`, and one `RECOVERY_REQUIRED`.
The outcome kinds are 44 `INTERFACE`, 26 `TYPE_VIEW`, 13 `CANONICAL_TYPE`, and
four `SOURCE_ORDER`; none lacks a kind field. Those are useful operational
measurements: the runner drove pre-admitted bounded mechanical tasks through
the project's actual promotion path and recorded non-success as a different state.
For example, run `20260921T010032429636Z` promoted three interface tasks; run
`20260921T133956383611Z` promoted three. The summaries explicitly say there
were no body tasks, no automatic commits, no proof bypass, and that acceptance,
infrastructure, or incomplete-cleanup failures stop the run. Counts are not
function-recovery counts, do not establish body-source quality, and are a
working-tree snapshot rather than an immutable release.

The runner has genuine isolation rather than merely a prose convention. A
grinder session snapshots every `src`, `include`, and `tools` input; it permits
only the selected function body to change, rejects added code-generation
directives, and caps a body task at three FAST attempts. It refuses protected
`BODY_MATCH_LAYOUT_BLOCKED` work, records a reason for a block, restores only
the task source, and republishes cards. `mechanical_grinder.py` treats a
candidate rejection differently from compiler/I/O/apply/admission/acceptance
failure: only the former can continue after a recorded block; the latter stops
for review. Its remaining-task invariant prevents quietly continuing when an
already-completed task remains eligible.

Publication is also protected. `promote_function.py` uses exclusive
`promotion.lock`, refuses work when a recovery sentinel or publication journal
exists, and wraps the authoritative ledger/current reports in a publication
journal. `recover_promotion.py` checks whether the recorded PID is live, takes
an exclusive `recovery.lock`, restores the last complete ledger/generated
state from `publication.zip` where present, and requires a fresh verifier before
retrying. This is evidence for one-checkout crash recovery and concurrent
publication exclusion. It is **not** evidence of safe multi-machine execution,
distributed locking, or replay exactly once after an OS reboot; the locks are
filesystem/PID mechanisms inside this checkout.

The current supervisor queue is a ranking aid, not a systemic-cause classifier.
It groups shared interface prerequisites and CU symptoms, explicitly says
groups may overlap and do not promise unlocked functions, and tells the
supervisor to inspect retained evidence before widening a mechanism. This is a
useful anti-overclaim boundary: eight `game-main` stack-frame cases or five
register/instruction-selection cases have a common *symptom*, not a demonstrated
common cause. The queue records counterexamples such as `add_itr_file`: source
branch reversal made the mismatch worse and source text block order produced
the same 357-byte output, routing the case to compiler-context investigation.

Icy has strong local mechanism evidence but it is compiler-scoped. Its GCC
4.4.1 diagnostic copies show that changing a predecessor definition can alter
an unchanged `HTTPFetchInternal` body, while the locked compiler's peephole2
dump is consistent with scratch-register selection. Original DWARF declaration
lines restored `scroller.c` source order and historical offsets without removing
the six `draw_scroller` register differences. The storage-scope experiment
likewise moved `localFilename` according to DWARF and raised one CU from seven
to eight `FUNCTION_MATCH` results / resolved four references, whereas the
analogous `face` move reordered BSS and changed text operands, so it was
restored and blocked. These are distinct scope, TU/order, and pass-stage
mechanisms—not a generic "systemic GCC issue." `recovery_pipeline.py` does
surface applicable recorded `codegen-rules` on a card, but no evidence here
shows a learned rule being automatically generalized beyond its stated scope.

The named `research-luna-*` receipts are not a model evaluation. The most
useful one is a negative experiment: 23 retained `draw_frame` probes collapsed
to 21 effective code/relocation outcomes; two new distinct outputs were
recorded, but neither restored the missing fifth frame-zero height read or a
strict match, and the alternatives lost two unrelated exact neighbours. It
properly calls the result diagnostic `DIFFER` and asks for predecessor/liveness
evidence before more source guessing. There is no model identifier, prompt,
sampling budget, worker baseline, matched human/other-model control, or
per-attempt cost in the inspected receipts. Therefore the measured experiments
support compiler-feedback and output-clustering value; they do **not** support
an attribution that Luna (or any model tier) caused the promotions or is more
capable than another worker.

## Empires: closed historical proof, no eligible frozen fleet

**PROJECT FACT.** The frozen status is a much stronger historical acceptance
receipt: a full EXE SHA-256, one fresh TLINK invocation, 106 ordered
relocations, 37,250 BSS bytes all partitioned to source, zero raw-EXE fallback
bytes, zero unresolved symbols, and no remaining structural adapters. This
proves a particular Turbo C 2.0 / TASM 1.0 / TLINK 2.0 reconstruction state; it
does not measure how efficiently an agent found it.

The frozen queue gives the opposite result to an unattended-fleet success
claim: `grinder-readiness.json` says `run_started: false`, zero ready runtime
cards, zero ready C cards, and stop when `next` returns null. Its instructions
require one worker to edit the runtime source serially, a fresh queue after each
promotion/block, two targeted corrections at most, a archived/restored isolated
edit on failure, and no automatic commit. `check_candidate.py` implements FAST
over all 6,571 runtime bytes plus publics and ordered fixups/frames/addends,
then promotion reruns FAST and uses uncached whole-production acceptance with
the 106 ordered relocations and full EXE proof. It records failure diagnostics
and restores the accepted snapshot only when scope checks pass.

This is an effective **protocol**, but the inspected frozen implementation does
not provide an Icy-style OS lock, publication journal, PID recovery, or global
multi-worker coordinator. The serial-worker rule is documentation plus stale
input/scope checks; a shared checkout still needs external ownership discipline.
Accordingly, no claim of global worker safety or reboot recovery belongs in a
shared abstraction without adding and testing it.

Empires does demonstrate a valuable mechanism-to-rule lifecycle. A bounded
candidate failure gets a structured pattern such as a shortened TASM branch or
absolute-memory form, is archived by range/task ID, becomes
`BLOCKED_SUPERVISOR`, and must not re-enter eligibility merely through later
regrouping. The instructions direct a worker to apply a documented
`tasm-reconstruction-rules.md` rule only when it fits, then escalate unfamiliar
architectural issues. Separately, the completed closure retained mechanism
evidence: inline ASM selects the whole-TU TASM route, ordered FIXUPP/relocation
topology can reject same-code outputs, and isolated C evidence for the
four-owner `M_DDD9_DF98` module cannot authorize a production promotion. That
last counterexample is exactly why a shared model must preserve object/TU
closure, not label a compiler-like local result as solved.

## Consequence for shared tooling

Reuse the *shape* of Icy's outcome accounting: explicit terminal state,
source/context identity, bounded retry, protected proof level, recovery
journal, and a supervisor handoff containing the failed prediction. Keep the
strict acceptance adapter project-owned. Empires adds the requirement that an
apparently successful local mechanism crosses an ordered-relocation/full-link
boundary before it is called a recovery. Neither project supplies evidence that
model routing or a common symptom taxonomy is sufficient for autonomous source
recovery. The next generic measurement should record model/worker identity,
prompt or recipe, wall time, candidate/effective-output identities, strict
result, and recovery/rollback outcome under one fixed task cohort.
