# Project update: evidence after the September 23 adversarial review

**Decision:** there is new strict recovery and stronger evidence for targeted
capability work. There is still no basis for a universal compiler solver, broad
region independence or a model-performance ranking. This pass reads existing
receipts and code; it runs no sibling build, report refresh or promotion.

[Evidence and source identities](evidence.json) pin 2026-09-24 observations to
commits or working-tree hashes. The comparison baseline is ai_decomp
`e000ca43f380184385b7bb14be29266fb6c78dda`. These projects have different proof
scopes; the table does not combine their counts into a recovery percentage.

| Project | Change since the recorded baseline | Proof scope and qualification |
|---|---|---|
| Stunts | Reported game C **14 → 25 functions**, **834 → 1,090 bytes**; queue 602 SUPERVISOR → **585 SUPERVISOR + 5 MEDIUM** | Current validation reports PASS/HYBRID_EXACT and independently compiled/bound 25 functions. Current queue, census and validation fingerprints agree. Earlier audit found a stale validation fingerprint; the old stage count is also explicitly retained in the new native experiment note. |
| SimAnt | Committed progress at `105963ff` **517 → 520 game functions**, **55,123 → 56,136 bytes**; runtime unchanged at 77 members | +3 functions/+1,013 bytes: YardToMap, ConvertMonoMaskToTandy, ClearHistory. This is complete-member recovery, not executable closure. Current pinned validation reports 222 tests and cache replay. |
| Icy Tower | **209 → 210 FUNCTION_MATCH**, **41,876 → 43,012 matched bytes** in the same 253-function/125,641-byte report population | One new strict function, load_replay, adds 1,136 bytes. Byte completion is now **34.23%**. All 25 ledger report identities matched the inspected live reports, whose text matched the pinned committed reports. No prior FUNCTION_MATCH became nonexact. |
| Empires | No new matching evidence found | Portable HEAD is still `9f9adaf8`; worktree clean. Historical frozen tag remains `873d1df0`. Portable development and historical closure remain separate. |

The full source revisions are retained in the evidence record: SimAnt
`effd40611757871eb0add8c26c58f2c3d65e96d5`, Icy
`e3780ebdc01c4db7d1d6fef53bd4c4c89169d0ce`, and Stunts
`068ff2e67d7b0ef9865ec1a4d60651eb8c830d0d` **plus substantial dirty/untracked work**.
An unchanged Stunts HEAD is therefore not unchanged project state.

**Closing check at 05:55 UTC:** work continued during inspection. Icy advanced
one commit to `6c00daad4e6729b066fa47699f267a3fd9e7a0fa`; its complete report
population still has 210 matches/43,012 bytes. Stunts still reports 25 C functions/
1,090 bytes, but mapped functions rose again to **527** and the queue became
**576 SUPERVISOR + 8 MEDIUM**. That newer queue fingerprint no longer matches
the retained PASS validation fingerprint. Preserve the earlier coherent receipt;
do not call this later queue freshly whole-state verified. The additional mapping
increment is recorded as status only, without attributing an uninspected mechanism.

## Stunts: capability transfer now has measured strict yield

**PROJECT FACT — MSC5.0/5.1 mapping and binding diagnostics.** The native mapping
experiment moves 234 → 372 → 452 → 497 verified intervals through three narrow
repairs: literal `db 144` as a one-byte NOP; exact unprefixed CBW/CWD encodings;
and exact bare string-opcode aliases. Previously verified intervals keep their
start/end/hash. This adds **263 mappings and 112,875 bytes of code evidence**,
not recovered source. Its stage baseline of 234 differs from the earlier
status snapshot's 237 mapped-function count; retain those coordinates rather
than manufacturing one seamless series.

Nine tasks became MEDIUM; four then passed strict promotion for 28 bytes.
The remaining 72 partial mappings include 42 first disagreements on `db` versus
decoded `add`, often involving apparent embedded data. General acceptance of
`db 0` would conceal the distinction. Fifty rows still lack an address anchor.

A second bounded capability derives far-address aliases from verified target
extents and at least two independent relocated callers. The registry now has
136 reviewed addresses; 76 remaining supervisor tasks have all observed far-call
addresses reviewed. This proves addresses/frames, not historical PUBDEF names,
TU membership or source recoverability. The first far-wrapper promotions and
three later loop/multi-call cases used the existing far-call binder.

The next concrete gap was mixed far CALL plus DGROUP data offsets. An unchanged
object was compared against historical LINK in two link orders **within each**
MSC5.00/5.10 profile. All four receipts report complete 32-byte equality and one
MZ relocation; compiler object hashes differ between profiles. The native binder
adds only the bounded `external-far-call-dgroup-offset16-v1` shape. Independent
original callers/setters establish data addresses; candidate operand values are
not used to invent them. `free_sdgame2` (18 bytes) and `locate_text_res` (52)
then pass fresh whole-image promotion. Ordered fixups and MZ entries remain
obligations, including descending-order cases.

**Counterexample to “finish the binder and unlock the queue”:** the current
archive samples 64 distinct task/object payloads across 28 unresolved tasks.
Sixty have the wrong extent. Of four equal-size candidates, only
`set_frame_callback` has all nonfixup bytes exact with a complete single-public,
zero-other-contribution shape. It still needs independently reviewed data and
callback offset/base binding. These selected archives do not estimate the
historical object-mode population or promise a broad unlock.

Sources: native `recovery/experiments/systemic-capabilities-20260923.md`,
`code-address-leverage-20260924.md`, `far-wrapper-promotions-20260924.md`,
`mixed-far-data-link-20260924.md`, `candidate-shape-census-20260924.md`, actual
mixed LINK JSON, promotion receipts and inspected resolver/binder code, all
hash-pinned in the evidence record.

## SimAnt: some “layout” blockers were source identity or tool issues

**PROJECT FACT — MSC7 Win16.** `_ClearHistory` was one of the four body-exact,
layout-blocked rows in the previous audit. A sibling `_HistUpdate` packet supplied
MAPSYM names for nine 64-word PACK arrays. Replacing invented names preserved
the established code shape and admitted the whole member: 299 code bytes,
182/182 ordinary literals and **84/84 fixups**, with no issues. Its promotion
uses **no TU or scaffold**. This is an especially useful counterexample to
treating a layout-shaped residue as proof that larger TU assembly is necessary.

`_ConvertMonoMaskToTandy` required a reviewed singleton component profile, but
not simply “use the latest/best source with the new profile.” The newer source
still missed 16 code bytes under the assigned `/Oeglw`; the preserved older
probe source then passed, adding 221 code bytes with 11/11 fixups. Candidate
ranking is conditional on compiler context. Discarding earlier source branches
after choosing a local winner would have lost the useful candidate.

The fresh classifier now explicitly applies native `tu_assembly.body_exact`.
Its 499 blocked rows contain 446 source-shape, 22 ABI, 21 unknown,
**four SOURCE_BINDING_INELIGIBLE**, five body-exact/layout and one mirror case.
The four include `_UpdateEditIfBufInvalid`, `_ScrollEditWindow`,
`_ToggleMapCursor` and `_GiveLesson`: opcode agreement was insufficient because
resolved bindings were wrong. This is a correction to triage, not a relaxed
matcher. The new 499-row population and 102 changed historical labels are not
directly comparable to the earlier 438-row/75-label population as accuracy rates.

There is also a discrete, high-fan-out **diagnostic** repair. Direct near-call
destinations wrap at 16-bit IP; the old decoder-facing representation sometimes
reported a linear address beyond the segment. Normalizing these calls resolves
**85 previously unnamed calls across 31 callers**, with unnamed near calls
falling 148 → 63. Total near calls stay 2,155. A separate direct-jump audit found
no corresponding out-of-range case, so the repair was not generalized blindly.

Finally, final linked near CALL does not uniquely imply a C `near` declaration.
The bounded LINK `NOP; PUSH CS; CALL near` evidence motivates reviewing 39
declarations across 23 jobs. A controlled GetMyInitialRandDir near→far change
corrects extent/opcodes but still fails four fixups. This improves diagnosis,
not recovery count.

Sources: pinned `docs/progress.json`, ClearHistory/ConvertMonoMaskToTandy native
promotion receipts, `evidence/orchestration/luna-foreman-checkpoint.md`,
`near-call-ip-wrap/README.md`, `call-abi-audit/README.md`, classifier and analysis
implementation. The progress comparison starts at the prior study's recorded
commit, not an invented synchronized four-project timestamp.

## Icy: a source-backed neighbor repair now yields a strict target match

**PROJECT FACT — locked TDM-2 GCC4.4.1 -O2.** Local type/declaration variants for
`load_replay` had collapsed. Holding its typed target body fixed, restoring
evidenced selected-row behavior in incomplete `draw_replay_selector` changed
the target from DIFFER to FUNCTION_MATCH. Controls distinguish that effect
from double-type changes alone, which did not solve the target. The accepted
whole-TU transaction also restores DWARF buffer scopes and historical selected-row
call ordering, preserves the six prior exact replay functions and adds the
1,136-byte target. The selector itself remains DIFFER.

This is stronger than earlier observations that arbitrary predecessor changes
perturb an unchanged target: an evidence-backed neighbor repair now produces an
accepted win. It still does **not** identify the precise internal GCC cause.
A separate research branch reported 9/15 exact but altered ownership/context
outside the safe production path; the accepted branch had 7/15. A bigger exact
count in a different research context is not automatically the better promotion.

Source evidence can improve without a new strict function. The profile TU now
supports a narrow late declaration/header block after an unchanged exact anchor.
The early-header control regresses `profile_data_page_advanced`; the late block
preserves all 11 exact profile functions while repairing typed interfaces.
Both selectors remain DIFFER. Implementation inspection confirms that production
planning rejects arbitrary `research_base` overlays and requires an unchanged
FUNCTION_MATCH anchor. This operationalizes a previously documented gate gap;
it does not prove the exact historical include position.

Compiler-pass diagnosis has become more precise, without yielding a play match.
The three explicit two-predecessor collision forms collapse to two effective
outputs. All preserve 63 exact peers but fail to retain the third selector read:
candidate `084t.pre` replaces the dispatch reload with a PHI of predecessor
values. The historical pattern might instead involve late duplication of a
switch-generated check; that remains an inference. Candidate pass dumps are not
historical pass traces. The proposed universal peephole-cursor explanation also
fails: some observed divergences originate in tree passes or IRA input.

The external cursor witness reports only visible successful choices; hidden
failed searches can reset state, and the local GCC source copy is not proven to
match locked cc1. Its 59 identical visible predecessor choices do not prove the
actual cursor at function entry or explain all register residues. No production
compiler modification or flag change is supported by this evidence.

## Emerging patterns, with strength and limits

**CROSS-PROJECT PATTERN:** a repeated evidence/tool defect can hide otherwise
useful recovery opportunities. Stunts' byte-qualified mapping repairs and
SimAnt's IP-wrap correction are independent examples with measured diagnostic
fan-out. Only Stunts' cited mapping stage measures subsequent strict promotions;
do not credit all newly mapped/named code as recovered source.

**CROSS-PROJECT PATTERN, strengthened:** body-local similarity is insufficient
for choosing the next task. Named ownership resolves SimAnt's apparent layout
block; bounded binding enables Stunts promotions; an incomplete neighbor's
source-backed repair enables Icy's target match. The shared procedure is to
identify the missing obligation and test it. Their compiler mechanisms differ.

**GENERIC METHOD:** retain source/context pairs and rejected alternatives.
SimAnt's older source wins under a new reviewed profile; Icy's higher-count
research branch is not production-admissible. A single scalar “best candidate”
is an unsafe archive policy. An adaptive multi-context beam may help, but its
economic benefit remains a **WORKING HYPOTHESIS**.

**Not established:** that an autonomous cheap fleet is now economically optimal.
New foreman records explicitly attribute work to Luna and show disjoint assigned
tasks, refill, review and serial promotion. They also contain a 19-target batch
with eight distinct compiled candidates and zero wins, and nine fresh reviews
stopping before compilation. These are useful evidence/tool stops, not model
exhaustion. No matched stronger-model arm or complete model/supervisor cost
trace establishes comparative efficiency. Generic crash-safe queue ownership
and independent region jobs remain unproven.

## What to do with this evidence

1. **Stunts:** inspect the one currently source-shaped callback candidate's
   ownership and historical LINK obligations before any binder expansion.
   Otherwise target source/TU or remaining mapping evidence; do not generalize
   binder support from a large SUPERVISOR count.
2. **SimAnt:** review the five native-body-eligible rows for independently named
   data before assuming scaffolds. Keep source/profile pairs and prior branches;
   do not automatically reissue all near-prototype warnings.
3. **Icy:** prioritize historically supported neighbor/interface corrections
   with protected-peer transactions. Keep pass-level negatives to stop redundant
   spelling search. Region independence needs the planned influence experiment;
   the new neighbor-mediated win is evidence of coupling, not independence.

The new catalog entries are scoped project facts. The shared principles are
narrowly strengthened; earlier hashes, negative trials and uncertainty remain.
