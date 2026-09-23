# Adversarial review validation

This is a metadata/source inspection pass, not a new compiler reconstruction.
The [machine-readable validation](validation.json) preserves all source-check
results and their actual observed hashes.

- **19 unit tests pass.** Region tests cover gaps/overlap, malformed/out-of-bounds
  spans, unknown machine/liveness mapping and counting actual call records.
- Workspace catalog, local links and adversarial aggregate checks pass.
  The Icy census recomputes 253 unique-VA rows, 125,641 bytes and its matched/
  unresolved distributions; Stunts recomputes all 602 retained queue rows and
  overlapping categories. Original catalog counts remain unchanged.
- A second execution of the read-only region inventory exactly reproduced the
  retained JSON, including all nine source hashes and the invalid draw sidecar.
  No sibling Python module or compiler was executed.
- **116/124 new source references verify at this later check.** Eight live
  snapshots drifted: SimAnt reclassification and seven Stunts queue/status/tool
  sources. Their original hashes and extracted observations are retained.
  These counts are reference checks, including repeated references, not unique
  files or independent experiments. There were no unavailable sources.
- **95/104 original catalog sources verify; nine live snapshots drifted.**
  These older identities were not rewritten. This is expected evidence aging
  in active repositories, not a fresh production regression determination.

Two malformed hash transcriptions were corrected with explicit old/new records:
Empires TU structure against its immutable Git blob, and Icy play control-flow
against the inspected live source. The SimAnt cross-reference to the earlier
ai_decomp fleet census was resolved to its already committed Git blob after
verifying text equality modulo checkout newlines; its original worktree hash
is preserved. None is a silent refresh of an old substantive claim.

The current reports are not an atomic cross-project snapshot. Source hashes
identify uncommitted observations but do not archive the underlying file. The
sanitized census rows and summaries retain measured metadata, not full original
source, binary bytes, SDKs or compiler artifacts. A drifted claim needing renewed
authority must be re-inspected under a new identity rather than inheriting an
old PASS. Historical replay baselines were checked as Git trees/blobs; missing
untracked toolchain inputs and reproducibility still require a future trial.

No sibling source/queue/lock/promotion was changed. No historical compiler,
model comparison, unattended fleet or external integration was launched. Region
independence, common-controller savings and model-routing superiority remain
unproven. Unit tests and hash checks grant no historical match.
