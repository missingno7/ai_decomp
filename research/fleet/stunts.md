# Stunts model-routing pilot: compact raw-data review

**Scope.** This is a `PROJECT FACT` extraction from the current Stunts working
tree, pinned below.  It analyses the completed, approved model-routing pilot
records only.  It neither establishes model capability in general nor reports
an invoice or portable wall-clock benchmark.

## Cohort and raw measures

`results.json` contains thirteen rows: five are failed preflight-only launches
with no trial result, and eight are completed matched runs.  The latter all use
high reasoning effort and form four Astra/Luna case pairs.  The inspected
matched cohort contains no Sol run; that is an absence in this particular
archive, not evidence about Sol.

| model | runs | hypotheses | requests | compiler processes | strict runs | within-run effective outputs | standard scenario |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-astra | 4 | 19 | 54 | 23 | 2 | 15 | $5.21717000 |
| gpt-6-luna | 4 | 25 | 67 | 27 | 2 | 15 | $0.08130442 |
| total | 8 | 44 | 121 | 50 | 4 | 30 | $5.29847442 |

The quoted dollar values are the report's alternative pricing scenarios, not
an actual bill.  On that scenario the Astra direct-worker total is 64.17 times
the Luna total.  Both models obtained strict acceptance for the two known
controls, `copy_string` and `rect_compare_point`; neither obtained strict
acceptance for `parse_shape2d_helper` or `unknown_libname_1`.  This is too
small and too control-heavy to rank models or support a cheap-fleet policy.
It does show that direct compiler work was only 50 process launches for 121
requests, so model/supervisor traffic was a material part of the experiment.

The sum of the eight run-local `unique_effective_outputs` counts is 30.  That
is not a cross-model unique count.  Within each case, the raw report's
case-scoped Astra/Luna union is 1, 3, 8, and 12 respectively (24 total), while
the within-run sums are 2, 4, 10, and 14.  Effective identities are scoped to
the historical profile/flags/context in the report; they are evidence for
compiler-output clustering, not a claim of globally unique machine code.
The retrospective separately records 40 identity-bearing trials, four trials
without an identity, ten within-run repeat occurrences, and six cross-arm
shared identities.  Per-trial audit identities must therefore not be
substituted for the result-level output counts.

The nested trial audits independently sum to the same 50 compiler processes as
the eight result summaries.  They contain four promoted outcomes, 11
diagnostic-compile-only outcomes, and 29 failed outcomes.  The latter includes
normal extent/byte mismatches as well as two omitted optional profiles, one
compiler error, one binding review requirement, and one unsupported object.
That is why the compact table records actual processes and result-level
clustering while keeping precompiler and tooling outcomes distinct from source
hypotheses.

## Cost and supervision boundary

The direct matched workers report $5.29847442 standard and $10.59694884 fast
scenarios.  Root supervision alone records 182 requests, 20,467,474 total
tokens, and a $26.25143 standard scenario ($52.50286 fast): 4.95 times the
direct standard scenario.  It has zero unpriced groups.  The complete
supervision/preparation aggregate, which includes that root group, contains
471 requests and 47,598,518 total tokens across ten groups, three of which are
unpriced, so its aggregate price is deliberately `null` in the raw record.
The known standard-scenario lower bound from direct workers plus root is
$31.54990442; an end-to-end cost and any direct-versus-supervisor ratio that
includes all preparation are unknown.  The archive explicitly calls the
actual invoice unknown.

This falsifies a simple conclusion that low direct worker price makes the
whole fleet cheap.  It does not falsify using a lower-priced worker for bounded
experiments: the pilot did not hold the candidate trajectory, supervision, or
target difficulty constant.  It provides no portable wall-time conclusion;
the raw elapsed times include a particular launcher/host setup.

## Separate bounded batching observation

The `batching-*` files are a separate Luna/high, `unknown_libname_1` comparison
and must not be combined with the eight-run pilot.  Under a four-hypothesis and
eight-compiler-process cap, sequential used 13 requests, four compiler
processes, four effective outputs, no strict success, and a $0.01465454 direct
standard scenario.  Batched used ten requests, three processes, two outputs,
no strict success, and $0.01242460.  It reduced requests and the direct price
scenario but explored fewer distinct effective outputs; candidate sets and
stop reasons differed.  It therefore establishes neither batching superiority
nor inferiority, but supports retaining output diversity and stopping reasons
as first-class batch feedback.

## Promotion/capsule safeguards in the native grinder

`tools/grind.py` requires an eligible task and a new hypothesis key, acquires
an exclusive `build/grind.lock`, then repeats those checks after locking.  It
snapshots the source and declared inputs before an experiment, treats an input
change during an error/failure as an error, archives diagnostics and reports,
refreshes state, and removes the lock in `finally`.  The transaction tests
inject canonical failure and unrelated-edit cases: they assert restoration of
the original manifest/plan/recipe, removal of stale exact acceptance and the
promotion lock, and detection without erasure of an unrelated user edit.
These are implementation and test facts, not independent historical-match
proof.  The current worker-research note additionally states that promotion is
serialized and followed by fresh whole-image acceptance; its current policy
mentions Luna as routine and Sol as supervisor, which is later project policy,
not a Sol cohort in this pilot.

## Decision for shared tooling

The strongest reusable observation is operational: record hypotheses,
requests, actual compiler processes, result-level effective-output clustering,
precompiler blocks, stop reason, and worker/supervisor usage separately.  A
fleet controller should use such records to decide whether to change search
dimensions or escalate analysis.  This small archive does not justify model
selection, fixed cost claims, or use of elapsed time across machines.

## Provenance

All source entries are immutable hashes of the inspected current working tree
at Stunts HEAD `068ff2e67d7b0ef9865ec1a4d60651eb8c830d0d`.  The tree has a
modified worker-research note; hashes make that retained evidence explicit.
The JSON companion supplies the machine-readable source manifest and exact
per-run compact extraction.  No source, oracle bytes, capsule paths, commands,
or output identities are copied here.
