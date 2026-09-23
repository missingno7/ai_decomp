# Provenance and maintenance

**GENERIC METHOD.** Preserve the claim's observed state rather than silently
retargeting it to current HEAD. Every normalized source entry names a sibling
repository, relative path, immutable commit or working-tree content identity,
and the snapshot's base commit. Citations retain line/section anchors where
available; these are navigation aids, not a substitute for content identity.

`catalog/sources.json` distinguishes:

- `git_blob`: SHA-256 of the exact blob returned by `git show COMMIT:path`.
  Annotated tag objects are peeled to commits. Empires closure uses the later
  frozen oracle tag, not the live SDL3 branch or the earlier closure tag.
- `working_tree`: SHA-256 of the observed bytes, with the base commit recorded.
  The hash cannot recover uncommitted content after it disappears. Reinspect
  drifted evidence or ask its owning project to archive it; never claim Git
  alone contains it.
- `inspected_worktree_sha256`, when present: the original worker's filesystem
  identity differs from the immutable Git blob identity, potentially due to
  checkout newline conversion. The source checker verifies the declared blob;
  it does not conflate two byte hashes.

Project dossiers are authored synthesis; catalog browsing pages are generated
from those records. The importer normalizes schema vocabulary, preserves the
original project record ID and resolves sources. It is workspace maintenance
code, not a generic compiler adapter. Regenerating it reads siblings and writes
only `ai_decomp/catalog` and `ai_decomp/knowledge`.

Run `python tools/provenance_check.py` to verify recorded blobs/live files. A
pass establishes reference integrity, not fresh historical compilation. This
pass inspected upstream receipts and code; it did not rerun any source-project
acceptance. Published counts are snapshots and may age immediately.
The source repositories were actively changing during extraction. The importer
preserves inspected live hashes even if a later read differs; the checker reports
that drift rather than silently rehashing the old claim or demanding an atomic
freeze across unrelated projects.

When adding a record:

1. Inspect current generated state and relevant attempt artifacts, then identify
   whether each document is current, frozen, or superseded. Code/table/receipt
   disagreement is a finding to preserve; see stale MUSIC prose in Empires.
2. Retain the hypothesis, control/context, measured effect, rejected alternative,
   outcome and limitation. Missing intermediate evidence stays missing.
3. Pin sources before synthesizing a pattern. A cross-project pattern needs
   independent observations; an experimental procedure is a generic method.
4. Test an apparent generalization against another project's contradictory or
   absent evidence. Keep compiler-specific causes even when symptoms match.
5. Review dependencies, assumptions, provenance and licensing before copying
   any code. This pass references all upstream tools and implements only new
   metadata utilities. No upstream license grant is inferred from local access.

The four source repositories remain their owners' production workspaces.
Recommendations here do not authorize changing their sources, queues, manifests,
tools or evidence. Research-only compiler wrappers may still write `build/`;
none were invoked by this extraction.
# External ecosystem research

The separate `research/ecosystem/` records distinguish **EXTERNAL IMPLEMENTATION
FACT**, **AUTHOR CLAIM**, **INFERENCE** and **UNKNOWN**. Code studies pin a full
upstream commit and source path/anchor; paper studies pin a revision/DOI and
state artifact availability. Readable studies link those primary sources.
`catalog/ecosystem/index.json` indexes these records without changing the
original local-project catalog schema or its historical snapshots.

Public source checkouts in ignored `.research-cache/` are temporary inspection
inputs, not vendored dependencies or preserved evidence. No upstream program
is executed merely to inspect it. License statements belong to the inspected
revision; compiler packages and data require separate provenance. A source
audit cannot establish that a hosted service or historical compiler recipe
currently runs successfully.

New local evidence used in the ecosystem comparison has its own manifest in
`research/ecosystem/local-requirements.json`; it does not silently refresh
earlier dossier hashes or receipts. A worktree hash identifies but does not
archive content. Use the report date, context and proof scope when comparing
claims from different snapshots.
