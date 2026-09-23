# Icy Tower hard-tail region audit

**PROJECT FACT — working-tree snapshot.** `game-main` has 82 functions and 64,715 original bytes. 63 `FUNCTION_MATCH` functions total 11,708 bytes; 18 `DIFFER` plus one `CODEGEN_SIMILAR` total 53,007 bytes. Mean size is 789.21 and median 177. The denominator is every `functions[]` entry's `original_size`, so these are function-body diagnostics, not object/CU proof.

`play` is 17,420 bytes and `draw_frame` 8,518: 25,938 bytes or 40.08% of the denominator. Both remain `DIFFER`: candidates are 17,400/8,203 and have 16,145/7,788 differing offsets. The next unequal sizes are `init_game` 5,788, `main_menu_callback` 3,741 and `do_replay_menu` 2,661. Counts therefore conceal byte concentration but do not prove a common mechanism.

**Whole-project correction.** Across the 25 current report files with a
`functions[]` array there are 253 functions / 125,641 original bytes: 209
`FUNCTION_MATCH` / 41,876 bytes and 42 `DIFFER` plus two `CODEGEN_SIMILAR` /
83,765 bytes. Matched functions have mean 200.36 and median 86 bytes; non-exact
functions have mean 1,903.75 and median 1,104.5 bytes.
The top 1/2/5/10 non-exact functions account for 20.80/30.97/46.79/62.76% of
that 83,765-byte non-exact denominator. Top five are `play`, `draw_frame`,
`init_game`, `main_menu_callback`, and `draw_replay_selector` (3,726). This is
a report-snapshot distribution, deduplicated by one entry per report
`functions[]` row; it intentionally excludes cards, overlays and historical
reports.

## Actual region metadata

`play-merged.c.regions.json` maps only source-line spans: W1a 70–145, W1b
146–283, W2 284–577, W3 578–963, W4 964–1246, W5 1247–1651. Draw maps D1
21–142, D2 143–364, D3 365–477, D4 478–586. The W1–W5 and D1–D4 files are
separate source copies; their file sizes are not machine-byte allocations.
The earlier absence claim was wrong. `play-census.json` stores 43 historical
regions with original offset spans, descriptions, direct/indirect calls, data
references, loops and stack-frame evidence; 2416–2602 is explicitly unlabeled.
This is machine-side historical region accounting, though it is not a candidate
edit-region-to-output influence matrix. `annotation-gaps.md` records a real
cross-region relation: midY is written in W1b and read only in W2, so it is dead
until W2 is sufficiently reconstructed. `function_lines.py` derives original
DWARF line-table sequences as guidance. An adapter should expose both region
systems and mark their mapping unknown unless a perturbation receipt proves it.

The earlier ancestry statement was wrong and is withdrawn. Verified Git parents
are `0b0269ce` → `d51f194d2cb370b513029f930f5577acf137b2d2`, while
`524a8a21347b2a410fbe8bb9764a0a3958177000` → `72267b1f6e53040e6aa4b50460145524cf71bcfb`;
the latter is not an ancestor of the atomic TU_CONTEXT commit. Keep `524a8a`
only for its documented negative: an uninitialized `playing` local let GCC
delete play's whole main loop. It is not cited here as a pre-transaction replay
baseline. Replay suitability for the verified `d51f194` line requires its own
file/acceptance inventory.

Region-local attribution is unsafe without declared TU context. The draw status/pose evidence records 23 probes, 21 effective code/relocation outputs, and a distinct independent-status result, yet it retained four rather than five direct frame-zero reads and lost two unrelated exact neighbours. Play probes repeatedly held 62/82 functions exact while both hard-tail bodies remained `DIFFER`. A default-prototype context changed an unchanged play body from 17,400 to 17,497; the `--order current --no-prototypes` control reproduced 17,400. A viewer must record function/overlay/pass scope and input identity before interpreting a delta.

The frozen `b6cabab0` pass receipt gives a specific GCC 4.4.1 mechanism. A two-arm high-score split retained seven `new_rand` calls through optimized GIMPLE and RTL `179r.dse2`; one disappeared at `181r.csa` as non-guest paths converged on a common suffix. Final play stayed 17,429 bytes with six calls against seven original. This establishes common-tail convergence for that tested equivalent suffix, not the historical source distinction or a precise internal subpass. Further spelling-only duplication is low-information until CFG/liveness evidence provides a surviving distinction.

The independent frozen init-game context receipt tested six saved TU probes: a retained earlier complete `init_game` and two trailing-call controls all gave one effective `load_character` output and the same scratch-register sequence. It stops without a historical discriminator. That falsifies unbounded predecessor-spelling search, not all context work.

A read-only prototype may store `{report_ref,function,original_size,candidate_size,status,difference_offset_count,first_difference,difference_class,source_hash,context_receipt_ref}` with optional `region_id`, `effective_identity`, `whole_tu_exact/total`, `neighbour_losses`, and `pass_stage`. It must retain `scope` (`function`, `overlay_TU`, `diagnostic_pass`) and identities, and never ingest source/object bytes or promote from size/count.
