# Fleet study validation

The 2026-09-23 pass changed only `ai_decomp`. It did not run sibling compilers,
refresh queues, start models or promote reconstruction source. The
[machine-readable validation](validation.json) preserves source-check results.

- `python -m unittest discover -s tests`: **13 passed**. The new reducer tests
  cover duplicate imports, conflicting IDs, proof/promotion scope, replicated
  wins/transactions, blocker domains/lineage, cost coverage and invalid counts.
- `python tools/check_workspace.py`: no errors. This includes local links,
  existing catalogs/fixtures, the external index and the new fleet checks.
- `check_fleet.py` reproduces the saved Stunts summary, compares its core totals
  with the raw-derived extraction, and recomputes both sanitized censuses.
- New source manifests/censuses: **855 of 858 entries verified**, three live
  SimAnt job records drifted during the pass. Entries can repeat the same source
  across a study and its census; this is not 858 distinct files.
- Original source catalog: **95 of 104 verified**, nine active-file drifts.
  The earlier catalog and its historical validation record were not rewritten.

The SimAnt counts describe its captured census, not an atomic live database or
the latest state after subsequent workers changed jobs. Icy counts similarly
describe retained mechanical summaries. No drift was repaired by substituting
new measurements into old claims. One truncated Stunts policy digest was
corrected after re-reading that policy; the correction is recorded in its study.

The checks establish metadata consistency and reference integrity. They do not
authenticate every receipt, rerun a historical proof, measure fleet economics,
test OS-reboot recovery, or validate concurrent autonomous allocation. The
SimAnt claim/input-isolation gap is an implementation finding, not a fault-
injection experiment.
