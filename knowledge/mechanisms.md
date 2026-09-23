# Mechanisms

Generated from the authored research dossiers. Record IDs are stable within this initial catalog.
Sources resolve through [the provenance catalog](../catalog/sources.json); refs and content hashes are explicit.
Read the linked project dossier for the discovery context and limitations.

## empires-route-context

**PROJECT FACT — empires.** Inline ASM selects a whole-TU assembler route

[Project dossier](../research/empires/dossier.md).

**Signature:** A plain-C member needs -B to match; replacing a predecessor ASM instruction with an intrinsic changes neighbors.

**Causal mechanism:** Turbo C restarts the entire unit through TASM on encountering inline ASM; branch relaxation differs from the native writer.

**Distinguishing experiments:** Whole GAME.C probe with BOOTSEED asm sti; Intrinsic substitution breaks TURNLOOP/LVLDRV; HITTEST -B probe supplies a boundary

**Negative alternatives:** Do not invent arbitrary per-function -B flags; Byte-neutral grouping does not establish unique historical membership

**Scope:** Pinned Empires Turbo C/TASM route only.

**Reusable diagnostic:** Hold target body constant; change context or compilation route and measure every affected member.

**Related tools:** [empires-probe-tu](tools.md#empires-probe-tu), [empires-audit-flags](tools.md#empires-audit-flags)

**Related trajectories:** [empires-game-tu](trajectories.md#empires-game-tu)

**Sources:** [docs/current/tu-structure.md](source-index.md#empires-src-f4a5acd7f619); [docs/current/closure-frontier.md](source-index.md#empires-src-e7eb7bf0084c)

## empires-ordered-relocations

**PROJECT FACT — empires.** Ordered relocations distinguish compiler routes and TU hypotheses

[Project dossier](../research/empires/dossier.md).

**Signature:** Same code can fail whole-image proof because relocation order differs.

**Causal mechanism:** Observed TLINK output retains object/FIXUPP order; native Turbo C descending order differs from ordinary TASM ascending order.

**Distinguishing experiments:** MUSIC native C recovery eliminates ordering accommodation; SLOTS/SLOTCOPY relocation order rejects merging

**Negative alternatives:** A same-code ASM representation is not automatically the historical route; Zero/one relocation gives no direction evidence

**Scope:** Empires toolchain and measured objects; not a rule for MSC OMF or GCC COFF.

**Reusable diagnostic:** Compare code, semantic binding and ordered topology separately before source-shape search.

**Related tools:** [empires-relocation-audit](tools.md#empires-relocation-audit)

**Related trajectories:** [empires-music](trajectories.md#empires-music), [empires-final-freeze](trajectories.md#empires-final-freeze)

**Sources:** [tools/audit_relocation_topology.py](source-index.md#empires-src-0502ff01d23b); [docs/current/tu-structure.md](source-index.md#empires-src-f4a5acd7f619); [src/MUSIC.C](source-index.md#empires-src-f826913e70b3); [layout/production-plan.json](source-index.md#empires-src-52636fd94b2d)

## empires-tu-constraints

**PROJECT FACT — empires.** DATA continuity and incompatible declarations constrain TU boundaries

[Project dossier](../research/empires/dossier.md).

**Signature:** A proposed shared unit cannot preserve all exact members.

**Causal mechanism:** One recovered unit emits contiguous private DATA and requires mutually compatible declaration views.

**Distinguishing experiments:** HUD..ANIMFRAM rejected for noncontiguous DATA; BOARD/GAME a74a2 2-D versus flat views; KEYIRQ handler interrupt view conflict

**Negative alternatives:** Adjacency alone is insufficient; Equal bytes for a merged run need not uniquely recover filenames

**Scope:** Observed source/data model in Empires; apply analogous constraints only after format-specific verification.

**Reusable diagnostic:** Probe full candidate unit, private segments, all member bytes and bindings.

**Related tools:** [empires-probe-tu](tools.md#empires-probe-tu)

**Related trajectories:** [empires-game-tu](trajectories.md#empires-game-tu)

**Sources:** [docs/current/tu-structure.md](source-index.md#empires-src-f4a5acd7f619)

## empires-asm-provenance

**PROJECT FACT — empires.** Compiler probes distinguish retained ASM from unrecovered C

[Project dossier](../research/empires/dossier.md).

**Signature:** Framed functions or fragments resist ordinary C shapes.

**Causal mechanism:** Recorded prologue/register/flag protocols and controlled probes establish compiler incompatibilities in specific cases.

**Distinguishing experiments:** 28 standalone plus eight contextual byte-negation probes; FLAGS pseudo-register adds pushf/pop; Sound C wrappers introduce SI saves

**Negative alternatives:** An ASM reconstruction is not evidence of original ASM authorship

**Scope:** Finite experiments support the current provenance decision, not mathematical impossibility of all C.

**Reusable diagnostic:** Record exact unsupported behavior and retain minimal evidenced ASM; reclassify if a later probe succeeds.

**Related tools:** [empires-probe-module](tools.md#empires-probe-module)

**Related trajectories:** [empires-negation](trajectories.md#empires-negation)

**Sources:** [docs/current/closure-frontier.md](source-index.md#empires-src-e7eb7bf0084c); [docs/current/tu-structure.md](source-index.md#empires-src-f4a5acd7f619); [docs/current/asm-provenance.md](source-index.md#empires-src-73ad44eed692)

## empires-fresh-acceptance

**PROJECT FACT — empires.** Research cache and fresh acceptance have different proof contracts

[Project dossier](../research/empires/dossier.md).

**Signature:** An old successful receipt could survive a failed or changed build.

**Causal mechanism:** Builder invalidates success first, checks input identities and plan, disables cache for acceptance, verifies full EXE and ordered relocations.

**Distinguishing experiments:** Source inspection of build_production and object_cache; Frozen acceptance receipt

**Negative alternatives:** A RESEARCH build or previous PASS is not fresh ACCEPTANCE

**Scope:** Implemented Empires contract; freshness is useful elsewhere but exact gate must stay project-specific.

**Reusable diagnostic:** Bind success to input fingerprint and proof scope, explicitly record cache/freshness and invalidation.

**Related tools:** [empires-build](tools.md#empires-build), [empires-cache](tools.md#empires-cache), [empires-fingerprint](tools.md#empires-fingerprint)

**Related trajectories:** [empires-final-freeze](trajectories.md#empires-final-freeze)

**Sources:** [docs/current/status.json](source-index.md#empires-src-9fd4ecf8eeed); [tools/build_production.py](source-index.md#empires-src-45cc7b345cd3); [tools/object_cache.py](source-index.md#empires-src-e3a07a74275b)

## stunts-hybrid-proof-separation

**PROJECT FACT — stunts.** Useful compiler/object evidence and strict recovery are different states; promotion requires immutable oracle inputs and fresh whole-image proof.

[Project dossier](../research/stunts/dossier.md).

**Scope:** Method is reusable; Stunts MZ/OMF and queue contracts are not.

**Related tools:** [stunts-check-candidate](tools.md#stunts-check-candidate)

**Related trajectories:** [stunts-matched-luna-astra-routing](trajectories.md#stunts-matched-luna-astra-routing)

**Sources:** [docs/current/validation.json](source-index.md#stunts-src-751997278a68) (anchor 1-L32); [tools/check_candidate.py](source-index.md#stunts-src-8d5b85ee6620) (anchor 13-L103); [recovery/corpus/endurance-001/handoff.md](source-index.md#stunts-src-794e153ccdd3) (anchor 1-L24)

## stunts-effective-output-convergence

**PROJECT FACT — stunts.** After two source hypotheses yield the same profile/context-aware effective output, move to a different analysis level; changed source text is not progress.

[Project dossier](../research/stunts/dossier.md).

**Scope:** Observed in Stunts; identity definition includes recipe context.

**Related tools:** [stunts-research-batch](tools.md#stunts-research-batch)

**Related trajectories:** [stunts-unknown-libname-batch-v-sequential](trajectories.md#stunts-unknown-libname-batch-v-sequential)

**Sources:** [docs/current/worker-research.md](source-index.md#stunts-src-3f7f26d672ca) (anchor 13-L17); [recovery/evaluation/model-routing/batching-retrospective.md](source-index.md#stunts-src-cb6b11074fad) (anchor 3-L11)

## stunts-candidate-pair-diagnostics

**PROJECT FACT — stunts.** Candidate-vs-candidate deltas can isolate a coherent BP-home allocation effect without asserting source causality or acceptance.

[Project dossier](../research/stunts/dossier.md).

**Scope:** The declaration-order result is one MSC 5.1 source/profile case.

**Related tools:** [stunts-diagnostics](tools.md#stunts-diagnostics)

**Related trajectories:** [stunts-camera-declaration-and-return-negative](trajectories.md#stunts-camera-declaration-and-return-negative)

**Sources:** [recovery/experiments/is_facing_camera/declaration-order-20260923.md](source-index.md#stunts-src-435992191ca3) (anchor 1-L6); [tools/diagnostics.py](source-index.md#stunts-src-ad637d16775d) (anchor 227-L457)

## stunts-mismatch-islands-with-contradictions

**PROJECT FACT — stunts.** Report anchors, islands, operand mappings, contradicting uses and residuals separately; a pattern is not variable identity or a repair.

[Project dossier](../research/stunts/dossier.md).

**Scope:** Implementation assumes x86-16 decoding but evidence discipline is portable.

**Related tools:** [stunts-diagnostics](tools.md#stunts-diagnostics)

**Related trajectories:** [stunts-camera-declaration-and-return-negative](trajectories.md#stunts-camera-declaration-and-return-negative)

**Sources:** [docs/current/near-match-families.md](source-index.md#stunts-src-2facbd66586a) (anchor 9-L15); [tools/diagnostics.py](source-index.md#stunts-src-ad637d16775d) (anchor 410-L457)

## stunts-capability-and-binding-boundaries

**PROJECT FACT — stunts.** Pinned compiler syntax limits and strict parser/binder omissions can be demonstrated blockers, distinct from a source-search or model limitation.

[Project dossier](../research/stunts/dossier.md).

**Scope:** MSC 5.10 named based-segment and Stunts B4/B6 cases only.

**Related trajectories:** [stunts-matched-luna-astra-routing](trajectories.md#stunts-matched-luna-astra-routing)

**Sources:** [recovery/corpus/endurance-001/handoff.md](source-index.md#stunts-src-794e153ccdd3) (anchor 1-L24); [docs/current/supervisor-instructions.md](source-index.md#stunts-src-331d37292052) (anchor 15-L16)

## simantw-effective-output-collapse

**GENERIC METHOD — simantw.** Cluster bounded candidate searches by compiler-output identity and use surviving deltas to choose the next analysis level.

[Project dossier](../research/simantw/dossier.md).

**Symptom:** Several source spellings provide no new OMF object.

**Causal mechanism:** Established only as output equivalence in the recorded compiler/context, not semantic equivalence.

**Experiments:** FloodNestB: three candidates, two raw OMF classes; ordinary/register collapsed; reversed declaration order differed but did not match. The current archive emits compiler_response with raw-OMF classes and representative deltas.

**Scope:** Portable process; classes are compiler/context-specific.

**Reusable diagnostic:** Hash source and raw object; group comparison outcomes by object hash; stop exhausted axes.

**Related tools:** [simantw-codegen-grinder](tools.md#simantw-codegen-grinder), [simantw-codegen-cache](tools.md#simantw-codegen-cache)

**Related trajectories:** [simantw-flood-nest-mapb-effective-output-failure](trajectories.md#simantw-flood-nest-mapb-effective-output-failure)

**Sources:** [evidence/experiments/flood-nest-mapb/README.md](source-index.md#simantw-src-faf185b1fa1d) (anchor 9); [docs/factory.md](source-index.md#simantw-src-28415d4f6c1c) (anchor 128)

## simantw-msc7-declaration-order

**PROJECT FACT — simantw.** Recorded MSC7 declaration order can select operands after source expression form has converged: global extern order for documented unit pairs, and local stack order for MagnifyMenu.

[Project dossier](../research/simantw/dossier.md).

**Symptom:** Expression rewrites collapse while one declaration order changes the selected memory/stack operand.

**Causal mechanism:** Two separately scoped MSC7 observations; do not assume identical causation.

**Experiments:** Recorded global before/after pairs; MagnifyMenu's final local reorder after seven controlled attempts and collapsed expression variants.

**Scope:** Only evidence-backed pairs and unit/function contexts; no general compiler rule.

**Reusable diagnostic:** Try an explicit, bounded declaration-order pair after semantic shape converges.

**Related tools:** [simantw-tu-assembly](tools.md#simantw-tu-assembly), [simantw-codegen-grinder](tools.md#simantw-codegen-grinder)

**Related trajectories:** [simantw-magnify-menu-local-order-success](trajectories.md#simantw-magnify-menu-local-order-success), [simantw-flood-nest-mapb-effective-output-failure](trajectories.md#simantw-flood-nest-mapb-effective-output-failure)

**Sources:** [docs/grinder-lessons.md](source-index.md#simantw-src-97d9aa655d43) (anchor 129); [docs/grinder-lessons.md](source-index.md#simantw-src-97d9aa655d43) (anchor 211); [layout/declaration-order.json](source-index.md#simantw-src-4caa686b51f6) (anchor 1)

## simantw-complete-member-proof

**PROJECT FACT — simantw.** A body match is not a recovery: OMF/NE semantic fixups, private data, placement and full member extent remain acceptance obligations.

[Project dossier](../research/simantw/dossier.md).

**Symptom:** Aligned instructions can coexist with wrong selector, data or member extent.

**Causal mechanism:** Strict member matcher validates entire contribution and loader obligations.

**Experiments:** db_UnhookObject/db_PurgeObject complete matches; ProcMenuHelp rejected for one alignment byte.

**Scope:** Acceptance principle portable; exact OMF/NE rules project-specific.

**Reusable diagnostic:** Report body diagnostics separately from unresolved member obligations.

**Related tools:** [simantw-codegen-diff](tools.md#simantw-codegen-diff), [simantw-omf](tools.md#simantw-omf)

**Related trajectories:** [simantw-draw-for-sale-sequential-private-state-success](trajectories.md#simantw-draw-for-sale-sequential-private-state-success)

**Sources:** [docs/factory.md](source-index.md#simantw-src-28415d4f6c1c) (anchor 41); [evidence/recovery/batch105/results.json](source-index.md#simantw-src-47f5c8a50659) (anchor 4); [evidence/recovery/batch114/results.json](source-index.md#simantw-src-db1245e440b9) (anchor 8)

## simantw-selector-pool-and-pointer-evidence

**PROJECT FACT — simantw.** Private CONST selector pools and pointer representation expose object/TU context, but equal selector or offset evidence alone does not establish object identity.

[Project dossier](../research/simantw/dossier.md).

**Symptom:** Exact bodies fail because selector spacing/order or far/near/based spelling differs.

**Causal mechanism:** Per-object first-use selector pool plus Win16 ABI and private DGROUP contributions.

**Experiments:** Named far-object probes; multimedia based-segment admissions; InitTree far-pointer contrast.

**Scope:** Win16 MSC7 ABI/object model only.

**Reusable diagnostic:** Separate segment selector, offset, identity, and whole-contribution evidence.

**Related tools:** [simantw-tu-assembly](tools.md#simantw-tu-assembly)

**Related trajectories:** [simantw-draw-for-sale-sequential-private-state-success](trajectories.md#simantw-draw-for-sale-sequential-private-state-success)

**Sources:** [docs/build-topology.md](source-index.md#simantw-src-d047b00272c6) (anchor 42); [docs/grinder-lessons.md](source-index.md#simantw-src-97d9aa655d43) (anchor 51)

## simantw-scaffolded-unit-assembly

**PROJECT FACT — simantw.** Measured noncredited stand-ins can reconstruct missing selector-pool order so independently exact claimed bodies are admitted with strict checks.

[Project dossier](../research/simantw/dossier.md).

**Symptom:** Body is exact except unresolved selector/private binding contributions in an incomplete object.

**Causal mechanism:** Unit composer reproduces observed pool order and retains claimed-member proof.

**Experiments:** 31 conversion events reported; checkpoint total moved from 417 to 447 while supersessions/removals make that a +30 net, not one-to-one accounting.

**Scope:** Requires trustworthy topology/selector evidence and strict claimed-member matching; does not recover stand-ins or unique historical filenames.

**Reusable diagnostic:** Classify exact-body binding blockers and assemble an evidence-bounded unit.

**Related tools:** [simantw-tu-assembly](tools.md#simantw-tu-assembly), [simantw-blocked-reclassification](tools.md#simantw-blocked-reclassification), [simantw-mirror-pairs](tools.md#simantw-mirror-pairs)

**Sources:** [docs/factory.md](source-index.md#simantw-src-28415d4f6c1c) (anchor 8); [docs/grinder-lessons.md](source-index.md#simantw-src-97d9aa655d43) (anchor 115)

## icytower-dwarf-source-structure

**PROJECT FACT — icytower.** DWARF function/type/local/lexical-scope/location evidence constrains source reconstruction and can distinguish scope/lifetime issues from absent code.

[Project dossier](../research/icytower/dossier.md).

**Symptom:** A candidate has stack/register residue or an apparent missing-local/source-scope discrepancy.

**Discriminating experiment:** Compare original and candidate locations/lexical ranges at the first decoded mismatch; make only a scope-constrained overlay when a declaration fact is independently evidenced.

**Negative alternatives:** Absent/overlapping/unsupported location expression is unknown, not an optimized-out-local conclusion.

**Scope:** Icy Tower DWARF-rich Win32/GCC context; unsupported or overlapping location expressions remain unknown.

**Diagnostic:** Compare original/candidate DWARF locations and lexical scope at the first decoded mismatch.

**Related tools:** [icytower-dwarf-locations](tools.md#icytower-dwarf-locations), [icytower-promote-function](tools.md#icytower-promote-function)

**Related trajectories:** [icytower-localfilename-scope](trajectories.md#icytower-localfilename-scope)

**Sources:** [README.md](source-index.md#icytower-src-c52e8cebd6cb) (anchor 98-103); [docs/attempts/game-main/play-control-flow-20260923.md](source-index.md#icytower-src-e48ebf518372) (anchor 51-53); [tools/dwarf_locations.py](source-index.md#icytower-src-c196ae83cab0) (anchor 15-96)

## icytower-historical-definition-order

**PROJECT FACT — icytower.** Original DWARF declaration order restored scroller natural offsets while target register mismatch remained unresolved.

[Project dossier](../research/icytower/dossier.md).

**Symptom:** Function extents/order differ despite retained body source, or a source-order task is proposed from executable address order.

**Discriminating experiment:** Build a no-body-change full-CU overlay in unique DWARF definition order and compare target, full contribution, and exact neighbors.

**Negative alternatives:** Historical order did not repair draw_scroller’s six register differences; another order task can lose accidental matches while predecessor code differs.

**Scope:** GCC 4.4.1 full-CU source order; no per-function linker placement.

**Diagnostic:** Whole-CU historical-order overlay with body and exact-neighbor preservation checks.

**Related tools:** [icytower-source-order](tools.md#icytower-source-order), [icytower-tu-context-probe](tools.md#icytower-tu-context-probe), [icytower-promote-function](tools.md#icytower-promote-function)

**Related trajectories:** [icytower-scroller-order](trajectories.md#icytower-scroller-order)

**Sources:** [docs/compiler-context-evidence.md](source-index.md#icytower-src-43f744d0a15f) (anchor 38-51); [docs/current/source-order-tasks.json](source-index.md#icytower-src-5603b15defea); [tools/source_order.py](source-index.md#icytower-src-9f47c890bb6a) (anchor 9-107)

## icytower-predecessor-context-dependency

**PROJECT FACT — icytower.** Changing earlier definitions can change an unchanged downstream target body in GCC 4.4.1 diagnostic full-CU probes.

[Project dossier](../research/icytower/dossier.md).

**Symptom:** Register/instruction residue persists after local body hypotheses converge, while a target body is textually unchanged.

**Discriminating experiment:** Reproduce a full-CU baseline hash, then omit one explicit predecessor or vary one type/flag and compare target bytes and protected neighbors.

**Negative alternatives:** HTTPFetchInternal peer/type alternatives and draw_scroller init/scheduling/unit-at-a-time trials did not repair their target residue; one trial caused collateral regressions.

**Scope:** Observed for HTTPFetchInternal and draw_scroller; neither the observed dependency nor the causal hypothesis is a universal register-mismatch attribution.

**Diagnostic:** Baseline-hash full-CU peer omission/type/flag overlays, then target and neighbor comparison.

**Related tools:** [icytower-compiler-probe](tools.md#icytower-compiler-probe), [icytower-tu-context-probe](tools.md#icytower-tu-context-probe), [icytower-rtl-evidence](tools.md#icytower-rtl-evidence)

**Related trajectories:** [icytower-scroller-order](trajectories.md#icytower-scroller-order), [icytower-draw-frame-predecessor](trajectories.md#icytower-draw-frame-predecessor)

**Sources:** [docs/compiler-context-evidence.md](source-index.md#icytower-src-43f744d0a15f) (anchor 8-36,53-65); [docs/attempts/compiler-context/game-httpget/HTTPFetchInternal.json](source-index.md#icytower-src-c4d4e6eddf66); [docs/attempts/compiler-context/game-scroller/draw_scroller.json](source-index.md#icytower-src-13acb948125f)

## icytower-pass-stage-convergence

**PROJECT FACT — icytower.** A play source split retained seven calls through 179r.dse2; at 181r.csa one call disappeared and the surviving label gained a use, leaving CFG/liveness/context rather than spelling as the next hypothesis.

[Project dossier](../research/icytower/dossier.md).

**Symptom:** Original/candidate call multiplicity differs after source duplication, and local spelling variants are no longer informative.

**Discriminating experiment:** Compile the production-equivalent TU with diagnostic dumps; compare GIMPLE/RTL around both arms to locate the first observed convergence stage.

**Negative alternatives:** Explicit duplicated non-guest hint arms still emit six final calls; a more precise optimizer-subpass cause and the historical non-merging distinction are not established.

**Scope:** GCC 4.4.1 diagnostic dump result, not matching proof or generic pass behavior.

**Diagnostic:** Locate first divergent/convergent normalized compiler pass after source variants stop separating.

**Related tools:** [icytower-rtl-evidence](tools.md#icytower-rtl-evidence), [icytower-tu-context-probe](tools.md#icytower-tu-context-probe), [icytower-effective-outcomes](tools.md#icytower-effective-outcomes)

**Related trajectories:** [icytower-play-pass-stage-convergence](trajectories.md#icytower-play-pass-stage-convergence)

**Sources:** [docs/attempts/research-supervisor-play/play-summary-rtl-common-tail-20260923.md](source-index.md#icytower-src-c517626b278f) (anchor 7-25); [tools/rtl_evidence.py](source-index.md#icytower-src-24b8112b067b) (anchor 8-29)

## icytower-body-layout-neighbor-separation

**GENERIC METHOD — icytower.** Keep resolved body proof, relocation/owner proof, same-CU layout, and collateral exact-neighbor preservation as separate acceptance dimensions.

[Project dossier](../research/icytower/dossier.md).

**Symptom:** A body is byte-equal under resolved relocations but layout operands, ownership, or neighboring contributions remain unresolved or differ.

**Discriminating experiment:** Run before/after contribution and protected-neighbor comparison, then require the explicit layout-blocked claim only when its narrow proof contract holds.

**Negative alternatives:** Masked equality, size proximity, link closure, or a scope change that reorders BSS/text do not establish the needed proof level.

**Scope:** The terminology and implementation are project-specific; separation of evidence is portable process advice.

**Diagnostic:** Before/after contribution plus protected-neighbor comparison; require explicit layout proof for a layout-blocked body.

**Related tools:** [icytower-promote-function](tools.md#icytower-promote-function), [icytower-instruction-alignment](tools.md#icytower-instruction-alignment)

**Related trajectories:** [icytower-localfilename-scope](trajectories.md#icytower-localfilename-scope)

**Sources:** [docs/proof-levels.md](source-index.md#icytower-src-0e77b5d3779f) (anchor 3-48); [docs/storage-scope-evidence.md](source-index.md#icytower-src-6ab42ab0e653) (anchor 11-46); [tools/promote_function.py](source-index.md#icytower-src-1a800deb70fe) (anchor 19-128)
