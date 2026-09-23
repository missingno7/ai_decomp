# Cross-project synthesis audit — Icy Tower evidence

Audit date: 2026-09-23.  Read-only comparison used the Empires frozen-closure dossier and the Icy Tower sources pinned in `records.json`; all 28 repository paths cited by Icy records (including the manifest and each tool entry) were verified with `git show e0522729b98f53e8afb50eca46bdd6a9fbd4f777:<path>`.  All 16 manifest worktree SHA-256 values still equal their recorded values; `docs/current/link-status.json` is intentionally a dirty-worktree source and differs from its HEAD content.  The Icy worktree has subsequently also changed `docs/grinder.md` and `tools/effective_outcomes.py`; neither was used as a hash-pinned factual receipt in the original manifest.

## Approved wording for cross-project synthesis

**CROSS-PROJECT PATTERN:** output can depend on facts outside an isolated function.  This is independently supported, but its causal routes differ: Empires records a Turbo C compiler-to-assembler route triggered by inline assembly in a translation unit, while Icy records source-definition/predecessor dependency in GCC 4.4.1 whole-CU probes.  State the shared observation as an output/context dependency.  Do not call the mechanisms equivalent, and do not infer that every compiler preserves a mutable compilation-state cursor.

**CROSS-PROJECT PATTERN:** a local/function body result is weaker than final construction proof.  Empires’ frozen whole-EXE closure requires ordered relocations and linker construction; Icy explicitly separates `FUNCTION_MATCH` from object, CU, layout, PE, and whole-executable levels.  The exact contracts differ, so synthesis must not replace either project’s proof hierarchy with the other’s terminology.

**GENERIC METHOD, not a cross-project empirical law:** when bounded experiments produce no new relevant output distinction, preserve the negative evidence and seek a discriminating hypothesis at another analysis level.  Icy supplies an output-clustering example (23 probes to 21 effective outcomes) and a pass-dump escalation.  The reviewed Empires dossier does not independently establish the same clustering metric, so “output collapse changes analysis level” is not yet a cross-project pattern.

**Rejected generalization:** declaration/definition order is not a universal code-generation lever.  Icy’s DWARF-grounded scroller order repair changed natural offsets without repairing six register mismatches, and a different Icy order task can lose accidental matches.  Empires’ cited precedent is a compiler-route/TU property, not declaration-order evidence.

## Causal-status corrections made

The Icy dossier and records now distinguish (a) the observed predecessor-context effect from (b) the peephole2 persistent-search-position explanation, which remains a **WORKING HYPOTHESIS** compatible with the evidence rather than an isolated causal proof.  They also distinguish the direct `179r.dse2` to `181r.csa` observation from a precise optimizer-subpass attribution: the trace supports convergence consistent with tail merging, but does not name a more specific internal transform.

Tool records now contain repository source references.  No source-repository content or generated evidence was changed.

Sources: `research/empires/dossier.md` “MUSIC”, “GAME and neighboring TUs”, and “Final closure”; `research/icytower/dossier.md` M2–M5; `../icytower_recon/docs/compiler-context-evidence.md:8-65`; `../icytower_recon/docs/proof-levels.md:3-48`; `../icytower_recon/docs/attempts/research-supervisor-play/play-summary-rtl-common-tail-20260923.md:7-25`; `../icytower_recon/docs/attempts/research-luna-draw/status-pose-independent-20260923.md:21-38`.
