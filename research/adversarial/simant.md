# SimAnt stage-confounding and blocker-reclassification audit

**PROJECT FACT — current live snapshot.** The primary classification report was
generated at 2026-09-23T20:27:39+02:00 from 438 `MATCH_BLOCKED` functions, not
from every historical attempt or all recovery work. It recompiles each
preserved candidate under the *current* assigned object profile and retains the
old taxonomy only as `previous_blockers`. Thus its useful claim is about the
then-current candidate/tool/context combination, not a retrospective measure of
the model that wrote any candidate.

## What the fresh pass changes

The report counts 399 `TRUE_SOURCE_SHAPE_MISMATCH`, 20
`ABI_TYPE_INFERENCE`, 13 `UNKNOWN`, four `BODY_EXACT_LAYOUT_BLOCKED`, one
`PROFILE_CONTEXT_RETEST`, and one `MIRRORED_SOURCE_PAIR`; it says 75 historical
labels no longer describe their fresh category. That numerator is a rule-based
comparison to the prior label (excluding `UNKNOWN`), not 75 demonstrated model
mistakes and not an accuracy score. Seventeen rows have multiple historical
blockers. For example, the `SRand*` rows carried both register-allocation and
private-layout labels but freshly fail ordinary instruction shape; `_ClearBuffer`
carried string, frame and register labels but also freshly fails source shape.
A label therefore records a prior investigation state rather than a single
causal variable.

Four previously blocked candidates have an exact instruction body with only
pool/private placement obligations: `_win_SetObjBitmap`, `_ClearHistory`,
`_PauseGame`, and `_SetPause`. This is a *residue* class, not a solved source:
the current policy routes it to unit/scaffold admission. `_GstrR`, previously
registered as a register-allocation blocker after six attempts, instead has a
matched counterpart and is tagged as a mechanically derivable mirror. The one
profile retest, `_MakeNewTailR`, had a `PRIVATE_CONST_LAYOUT` history but its
old `/Oelw` profile is now `/Oeglw`; the fresh run still reports a source-shape
residue. It shows why a profile change must be recorded even when it does not
produce a solve.

The opposite direction matters more. Twenty-seven rows previously labelled as
translation-unit context (including its older `_REQUIRED` spelling) now split
into 26 `TRUE_SOURCE_SHAPE_MISMATCH` and one `UNKNOWN`, not a TU/scaffold
candidate. A correct body does not prove that all remaining misses are context.
Likewise, `_UpdateEditIfBufInvalid` retained a correct body while a fresh
retest exposed a provisional `_DrawEdit` symbol binding to the wrong
same-segment target. A context explanation would have concealed a binding
error. These classifications are deterministic triage rules over the current
comparison; they are useful experiment selectors, not causal proofs.

## Shared unlocks are stage effects, not model scores

The documented expert blocker pass moved the progress counter from 230 to 243
matched game functions and reports 13 promotions. Its stated family grouping is
six dialog functions after reconstructing two private arrays, four map-stencil
functions, two yard-private-state functions, and `_GSetAttrib` after restoring
a common store. The same record preserves a counterexample: the four-member
contiguous map TU was rejected by public anchors; only a three-member
H/knob/penny contribution was strongly supported and `GrabMap` remained a
body/control-flow blocker. A shared binding is not itself a shared source
recovery.

These gains mix semantic correction, named binding, private DATA/BSS ownership,
profile context, unit composition, and stronger admission tooling. They are
not a counterfactual in which the same agent and candidate set ran before and
after one change. The later `_MagnifyMenu` case from the fleet census is
independently valuable but similarly limited: seven one-candidate misses then
a strict eighth-attempt promotion by a declaration-order experiment. The census
was captured later (2026-09-23T20:33:47Z) and counts 786 jobs/2,683 attempts;
it is a different population from the 438 reclassification rows. Neither the
ledger nor compiler receipts identify a model/provider, so historical commit
text referring to “Luna investigations” cannot attribute the late solve.

## Stage boundary and future leakage

`4c5270d4c5b8c6f0f8cccf6626c8fe9d262c5019` is the first commit that added
both `tools/build_topology.py` and `tools/tu_assembly.py`. Its exact parent,
`b3b04b8ef9351b64e7c32546d92e5f050d17c546`, has the compiler, grinder,
strict matcher/gate, workflow, factory docs and validation receipt but lacks
those two build-context tools and `blocked_reclassification.py`. The latter
first appears in the later reclassification stage. A replay asserted to be
pre-topology must use the parent commit's tools, inputs and available context;
feeding it later unit manifests, profile assignments, named pool/binding rules,
or later recovered neighbours would leak future analysis. It can still replay
the historical source/receipt where committed, but it cannot infer missing
untracked artifacts or model authorship.

## Candidate transfers to Stunts

| Kind | Candidate transfer | Boundary |
|---|---|---|
| Mechanism | Treat a static old label as falsifiable: rerun the preserved candidate under the currently evidenced compiler/TU context before choosing a new source axis. | MSC7 profile changes and OMF selector/private-data residue are not GCC causes. |
| Method | Maintain stage-tagged `previous`, `fresh result`, `context signature`, and a triage outcome: semantic/source shape, ABI, binding, layout/TU residue, tool failure, or unknown. Demand a discriminating follow-up. | This is a procedure, not a claim that a fresh result proves causality. |
| Tool | Reuse the *contract* of source-bound frozen-body manifests and a context-retest report. Stunts already has a blocker census and TU-context tooling; assess its existing fields before adding a duplicate adapter. | Do not import SimAnt Python or its taxonomy as a dependency. |
| Assumption to test | A Stunts near-match may become exact under a predecessor/TU/pass context, but a wrong symbolic binding or semantic common-epilogue omission can present similarly. | Require its own source, compiler, and acceptance evidence. |

The shared workspace should compare experiments only within a stated stage and
context signature. Model evaluation needs durable run provenance and a frozen
tool/evidence bundle; recovery ledgers alone cannot distinguish model ability
from supervisor analysis, changing target knowledge, or a newly available
admission route.
