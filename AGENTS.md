# Working in ai_decomp

Read `README.md`, `docs/provenance.md`, and `knowledge/principles.md` first.
This workspace is a cumulative research memory and small analysis-tool layer.

- Discover reconstruction sources as siblings of this repository. During
  knowledge extraction, treat them as read-only: even a probe or report refresh
  can write build/state files. Owning-project work belongs in its own task.
- Preserve PROJECT FACT, CROSS-PROJECT PATTERN, WORKING HYPOTHESIS and GENERIC
  METHOD distinctions. Name the exact compiler/context and scope negatives.
- Pin source paths to immutable commits or inspected working-tree hashes.
  Never silently refresh a hash while retaining an old claim. A missing live
  artifact is an evidence-retention limitation, not permission to invent it.
- Edit authored `research/<project>/records.json` and dossiers, then regenerate
  catalogs with `python tools/build_catalogs.py`. Update synthesis separately.
- Keep assets, original bytes/source, historical tools and SDKs out. Review
  licensing and dependencies before copying upstream code; current tools here
  are original metadata-only implementations.
- Validate with `python -m unittest discover -s tests`,
  `python tools/check_workspace.py` and `python tools/provenance_check.py`.
  Distinguish test failures from expected drift in active-source snapshots.
  These checks never establish a new compiler or reconstruction result.
