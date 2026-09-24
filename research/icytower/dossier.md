# Icy Tower 1.5.1: GCC/DWARF reconstruction dossier

**Research snapshot:** `icytower_recon` `main` at `e0522729b98f53e8afb50eca46bdd6a9fbd4f777` (2026-09-23).  This is a **PROJECT FACT** dossier: all code-generation claims are scoped to its locked TDM GCC 4.4.1 Win32/i386 setup.  The source worktree was dirty and contained untracked attempt evidence when inspected; see `records.json` for content identities.  No source-repository file was changed.

## Live project inventory

| Dimension | Observed state |
| --- | --- |
| Historical target | Icy Tower 1.5.1 independent reconstruction; 25 original game translation-unit identities retained. |
| Architecture/formats | Win32 i386, COFF objects and PE executable; rich DWARF is paired with COFF names/addresses. |
| Compiler context | Archived/locked TDM GCC 4.4.1, normally `-O2 -g -mfpmath=387`; `-Os` is an inherited hypothesis, and `timer.c` is documented as matching at `-O2`/`-O3`. |
| Oracle and proof model | Original executable is verifier evidence, never a compilation input. `FUNCTION_MATCH` requires full body bytes after independent relocation and decoded same-CU transfer resolution. Object, CU, layout, PE, and whole-file claims are separate. |
| Current ledger | `docs/progress.json` reports 209 `FUNCTION_MATCH`, 42 `DIFFER`, and 2 `CODEGEN_SIMILAR` functions (35299 of 116113 game-function bytes matched); this is not CU or executable closure. |
| Current workflow | Generated ledger/cards and queue are authoritative. FAST is `check_function.py`; ACCEPTANCE is `promote_function.py`; source/order/type/scope work has bounded task gates, receipts, rollback, and protection for exact bodies/neighbors. |
| Current frontier | Recovered-game link is useful but explicitly not completion. The dominant hard residue includes incomplete large `play`/`draw_frame` bodies, unresolved ownership/layout, register scheduling, and TU/compiler-context dependencies. |
| Durable evidence | `src/recovery.json`, `docs/current/*.json`, content-addressed attempt logs/JSONL, compiler RTL dumps, DWARF/COFF census, and per-function receipts.  Older README milestones are explicitly historical, not queue authority. |

Sources: `README.md:3-25,74-120`; `AGENTS.md:1-19`; `docs/progress.json`; `docs/recovery-frontier.md:1-12`; `docs/proof-levels.md:3-48`.

## Demonstrated mechanisms

### M1 — DWARF is source-structure evidence, not merely symbol decoration

**PROJECT FACT.** Original DWARF provides function/type/local names, source lines, lexical scopes, and variable location ranges.  It can distinguish a real register-resident local from an optimized-out variable, identify a scope correction, and constrain types and stack allocation.  COFF adds linked-name/address evidence; neither source alone is treated as full ownership proof.

The `play` recovery shows the value of this split: moving a results-local block to the original DWARF lexical position made candidate DWARF locations for `qualify`, `qualifyValue`, and `fbuf` agree and reduced the frame, yet left a 32-byte frame excess and an unresolved spill/register discrepancy.  It is evidence for a source-shape correction, not an exact claim.

**Reusable diagnostic:** map original and candidate location lists at the first decoded mismatch; check lexical scope and lifetime before padding or declaration-order experiments.  **Limit:** expression/location-list interpretation can be unsupported or overlap; missing tool output is not proof that a local is absent.

Sources: `README.md:98-103`; `docs/tu-context-analysis.md:13-14`; `docs/attempts/game-main/play-control-flow-20260923.md:51-53`; `tools/dwarf_locations.py:15-96`.

### M2 — Historical definition order is evidence, but source order can interact with GCC context

**PROJECT FACT.** DWARF declaration lines establish `scroller.c` source order as `init_scroller`, `draw_scroller`, `scroll_scroller`, `restart_scroller`.  Restoring that order from an address-order candidate produced historical natural offsets `0,16,44,440` and a 640-byte contribution while preserving bodies and existing exact proofs.  The six `draw_scroller` register mismatches remained, so it did not prove text/object/CU equality.

The gate derives only unique original declaration order and rejects conflicting/absent lines or newly implicit declarations.  A later `fld_adspot` task documents the converse: historically correct order can lose current accidental matches while predecessor code still differs, so it is routed to a whole-TU supervisor transaction.

**Reusable diagnostic:** make a no-body-change overlay in historical DWARF definition order, compare the entire TU, and check protected neighbors before promoting source order.  **Limit:** never implement it with per-function linker placement; it is a GCC-context observation, not a portable declaration-order rule.

Sources: `docs/compiler-context-evidence.md:38-51`; `docs/current/source-order-tasks.json`; `tools/source_order.py:9-107`; `tools/tu_context_probe.py:28-422`.

### M3 — An unchanged target body can depend on predecessor definitions in GCC 4.4.1

**PROJECT FACT.** In isolated whole-CU probes, replacing an earlier `destroyHTTPResponse` definition with a declaration changed two of `HTTPFetchInternal`’s three scratch-push mismatches without editing its body.  Omitting `extractHTTPResponse`/`getSocketError` and correcting `dataPtr` to its DWARF type did not repair the issue.  Likewise, removing preceding `restart_scroller` changed `draw_scroller`; omitting `init_scroller`, disabling scheduling, or disabling unit-at-a-time did not repair the six historical mismatches and one flag trial reduced exact neighbors.

The project proposes GCC 4.4.1 i386 peephole2 scratch-register allocation, whose successful searches retain a search position, as a **working causal hypothesis** compatible with the locked-compiler dumps and upstream source.  The controlled probe establishes the dependency; it does not isolate that internal state as its causal proof, and it does not attribute all register mismatches to it.

**Reusable diagnostic:** first reproduce the full-CU baseline hash, then alter at most a few explicit predecessors/types/flags in an overlay and compare the unchanged target plus neighboring proof set.  **Limit:** route an observed dependency to supervisor work; it grants neither layout-only nor exact status.

Sources: `docs/compiler-context-evidence.md:3-36,53-65`; `docs/attempts/compiler-context/game-httpget/HTTPFetchInternal.json`; `docs/attempts/compiler-context/game-scroller/draw_scroller.json`; `tools/compiler_probe.py:16-128`; `tools/rtl_evidence.py:8-29`.

### M4 — After local source-shape convergence, compiler-pass evidence can reclassify the question

**PROJECT FACT.** A `play` probe syntactically split two non-guest random-hint arms to retain the original’s seventh `new_rand` call.  GCC 4.4.1 retained seven calls through optimized GIMPLE and RTL `179r.dse2`, then one call had disappeared and a destination label gained a use in `181r.csa`.  This is direct pass-stage evidence of convergence and is consistent with RTL common-tail merging; `181r.csa` is not a precise internal-subpass attribution. Repeated textual duplication is therefore low-information for this probe.  The next experiment must seek a historical CFG, liveness, or context distinction.

**Reusable diagnostic:** once output-resistant source alternatives are known, compare normalized pass dumps to locate the first pass at which the required distinction vanishes, then formulate a dataflow/CFG falsifier.  **Limit:** dumps are diagnostic only and are never the matching oracle; this says nothing about other GCC versions or compilers.

Sources: `docs/attempts/research-supervisor-play/play-summary-rtl-common-tail-20260923.md:3-25`; `docs/attempts/game-main/play-control-flow-20260923.md:61,103-105`; `tools/rtl_evidence.py:8-29`.

### M5 — Exact body proof must preserve neighbors and retain layout as a distinct unfinished dimension

**PROJECT FACT.** `FUNCTION_MATCH` requires all body bytes after independent relocation and decoded direct-transfer resolution.  `BODY_MATCH_LAYOUT_BLOCKED` is separately promoted only when resolved body bytes agree but same-CU operands/strict terminal-jump conditions are proven layout effects; it never counts as function, object, or CU closure.  FAST reports a focused difference, while acceptance checks current receipts, protected exact functions, data, and rollback/publication controls.

The `localFilename` scope repair used DWARF to move an unchanged declaration from file to function scope, then preserved text/allocated contents/relocations and proved its 256-byte BSS owner; four references became exact without a function expression rewrite.  A parallel `face` scope move reordered BSS and text operands, was rejected, restored byte-for-byte, and protected the 47 exact main functions.

**Reusable diagnostic:** separate raw source/body evidence from relocation, owner, and layout evidence; compare contributions and every exact neighbor before and after a narrow non-body change.  **Limit:** masked equality, size proximity, and link closure do not substitute for the required proof level.

Sources: `docs/proof-levels.md:3-48`; `docs/storage-scope-evidence.md:11-46`; `docs/current/validation.json`; `tools/check_function.py:10-150`; `tools/promote_function.py:19-128`.

## Representative trajectories

### T1 — Source-order promotion without false closure

`draw_scroller` had six persistent register differences → DWARF gave definition lines → old address order was replaced in an overlay → natural historical function offsets and 640-byte text contribution converged while all prior exact bodies remained unchanged → six target mismatches persisted → outcome: **HISTORICAL_SOURCE_ORDER**, not FUNCTION/OBJECT/CU match.  The promoted lesson is to preserve source-order evidence and isolate remaining context/register work rather than claiming a size/layout win.

Sources: `docs/compiler-context-evidence.md:30-51`; `docs/current/source-order-tasks.json`.

### T2 — Lexical storage correction that unlocked strict references

DWARF said `localFilename` was function-static → candidate declared it at file scope → bounded declaration-only move placed the unchanged declaration in `fldads_get_local_cache_name` → FAST and fresh acceptance preserved text, allocated sections, normalized symbols, common allocations, and relocations → strict ownership proved BSS at `0x4dd040` → four references became exact and the CU rose from 7 to 8 function matches.  A similar `face` experiment instead changed BSS offsets and text operands, so it was restored and blocked.  This is a success plus falsifier for assuming all scope moves are mechanically safe.

Sources: `docs/storage-scope-evidence.md:11-46`; `docs/attempts/interfaces/scope_fld_adspot_localFilename.jsonl`; `docs/attempts/interfaces/scope_main_face.jsonl`.

### T3 — Large-renderer local probes converge, then change analysis level

`draw_frame` has 5 original versus 4 candidate direct `custom.frame[0]->h` reads → status 2/3 CFG separation and signed-speed arms were proposed → two historical-order overlay probes produced distinct effective outputs but still four reads and lost two unrelated exact neighbors in one family → 23 draw probes collapsed to 21 effective outputs → outcome: the remaining unknown is predecessor/liveness/path correspondence, not another surface spelling.  The preserved action is to trace all reaching `p_im` values before another body probe.

Sources: `docs/attempts/research-luna-draw/status-pose-independent-20260923.md:3-38`; `docs/draw-frame-recovery.md:1-31`; `tools/effective_outcomes.py:15-86`.

### T4 — `play` pass-stage convergence narrows a missing-call hypothesis without solving it

The original has seven `new_rand` call sites while the candidate had six → source was split into two explicit non-guest hint arms → optimized GIMPLE and RTL through `179r.dse2` retained seven calls → at `181r.csa`, one call disappeared and the surviving destination label gained a second use → final object again had six calls and `play` remained strict `DIFFER` → outcome: seek a historical CFG/lifetime/context distinction rather than further textual duplication.

This is a diagnostic pass-trace trajectory only.  It establishes the observed stage at which the candidate converges; it is consistent with common-tail merging but does not identify a precise internal transform or establish why the historical source avoided convergence.

Sources: `docs/attempts/research-supervisor-play/play-summary-rtl-common-tail-20260923.md:3-25`; `docs/attempts/game-main/play-control-flow-20260923.md:61,103-105`; `tools/rtl_evidence.py:8-29`.

## Negative evidence worth retaining

| ID | Tested condition | Result and scope |
| --- | --- | --- |
| N1 | `HTTPFetchInternal`: omit `extractHTTPResponse`/`getSocketError`, or correct `dataPtr` to the DWARF unsigned-char pointer. | Did not repair its three scratch-push mismatches in that full-CU GCC 4.4.1 probe. |
| N2 | `draw_scroller`: omit `init_scroller`, disable instruction scheduling, or disable unit-at-a-time. | Did not repair the six mismatch offsets; unit-at-a-time created four more differences and reduced exact neighbors. |
| N3 | `draw_frame`: independent status tests and separate signed-speed arms. | Neither created the missing fifth frame-zero height read; they are distinct output families, not redundant spelling trials. |
| N4 | `play`: explicitly duplicate non-guest random-hint source arms. | GCC common-tail analysis still emitted six calls; pass dumps locate convergence at `181r.csa`. |
| N5 | `main_menu_callback`: move `face` scope based on a superficially similar DWARF/scope hypothesis. | BSS order and text operands changed; preservation gate restored source and blocked the task. |

Sources: M3/M4/M5 and T3 evidence above.

## Tool inventory and reuse assessment

All listed tools are Python standard-library project tools (`README.md:29-31`), but that does not make their input schemas generic.  “License review” means a future extractor must retain repository provenance and inspect any embedded parser/source provenance; this pass copied no code.

| Tool | Purpose; input → output | Dependencies / assumptions | Classification | License review |
| --- | --- | --- | --- | --- |
| `tools/dwarf_locations.py` | Decode/annotate DWARF local locations; DIE/location rows + PC → scoped location annotations. | DWARF expressions, i386 frame semantics, project census shapes. | adapter_required | Reference only; inspect parser provenance before reuse. |
| `tools/compiler_probe.py` | Bounded predecessor/type/flag overlay probe; CU/body/peer choice → hash-bound compiler/RTL evidence. | Locked TDM GCC command, Icy Tower source/layout. | project_specific | Reference only. |
| `tools/tu_context_probe.py` | Rebuild a full-CU overlay with order/bodies/statics/prototypes; structured spec → compiled comparison and focused report. | Icy Tower units/ledger/build pipeline and GCC dumps. | adapter_required | Reference only. |
| `tools/source_order.py` | Derive guarded historical definition-order plans; DWARF/unit ledger → source-order task plans. | Unique DWARF lines and Icy Tower ledger schemas. | conceptually_reusable | Reference only. |
| `tools/effective_outcomes.py` | Cluster attempt records by normalized code/relocation identity; function attempt JSON → effective-outcome groups. | Attempt-record field names; no compiler/object parser requirement in its core grouping. | conceptually_reusable | Strong candidate for a small shared adapter-neutral schema. |
| `tools/instruction_alignment.py` | Build bounded decoded-instruction correspondence; comparison rows → aligned analysis. | Project comparison row schema, x86 instruction records. | adapter_required | Reference only. |
| `tools/rtl_evidence.py` | Normalize and compare compiler dumps; two dump trees → first/changed-pass report. | GCC dump naming and Icy Tower normalization rules. | conceptually_reusable | Reference only. |
| `tools/check_function.py` + `tools/promote_function.py` | FAST focused check and strict promotion; target/function/receipts → diagnostic or atomically published proof. | Full Icy Tower verifier, DWARF/COFF resolvers, locks and ledger. | project_specific | Reference only; do not transplant the gate. |

The only clearly shareable initial abstraction suggested here is an **adapter-neutral effective-output/attempt manifest**: content identities, hypothesis axes, compiler context fingerprint, structured delta, strict result, and stop reason.  Compiler runners, COFF/PE/DWARF parsers, TU constructors, and promotion gates should stay project-local until another repository supplies a compatible adapter boundary.

## Handoff

Icy Tower is the strongest current precedent for a DWARF-rich GCC reconstruction where source facts, lexical lifetimes, source order, and predecessor context must be kept separate from strict equality.  Consult it for (1) deriving bounded source hypotheses from DWARF locals/types/scopes, (2) detecting context-sensitive compiler behavior with overlay probes, (3) pass-dump escalation after source experiments converge, and (4) protecting exact bodies while resolving layout/ownership independently.

Do **not** generalize GCC 4.4.1 peephole state, RTL tail merging, source-order effects, or the exact proof schema as universal compiler behavior.  The transferable method is the controlled experiment: freeze identities, vary one declared axis in a whole-context reproduction, record effective output and collateral changes, and escalate the analysis level when variants stop separating.


## September 24 follow-up

The [dated project update](../updates/20260924/review.md) and its separate
[evidence manifest](../updates/20260924/evidence.json) preserve newer observations
without changing this dossier's earlier snapshot. New catalog claims are scoped
project facts; diagnostic coverage and strict recovery remain separate.
