# Ecosystem research validation — 2026-09-23

The pass adds six authored studies with structured records: m2c/permuter,
decomp.me, Mizuchi, diff tools, academic approaches and refreshed local
requirements. The [external index](../catalog/ecosystem/index.json) covers
eight implementation studies (the requested seven plus binutils-omf).
Academic approaches have a separate versioned register. The original four
project dossiers and 104-source local catalog were not regenerated.

Validation performed:

- Existing standard-library unit suite: **5 passed**.
- Workspace Markdown links, local catalogs, synthetic experiment fixture and
  external index/record integrity: **passed**.
- External records use full inspected commit IDs and classified, sourced
  findings. Core code claims were checked against implementation, not only
  READMEs. A second researcher reviewed the synthesis and corrected licensing
  and provenance wording.
- Fresh local requirement manifest: **12/12 identities verified**. Original
  catalog: **96/104 verified**, with the same eight already recorded live-file
  drifts. They remain explicit historical snapshots; no claim was silently
  retargeted. Full result: [validation receipt](../research/ecosystem/validation.json).
- Git whitespace check passed before commit. Cached upstream source is ignored
  and excluded from workspace Markdown validation; it is not a dependency.

`tools/check_ecosystem.py` validates offline metadata/index relationships and
pinned code links. It does not fetch URLs, prove a source claim, verify licenses
legally, run a compiler or certify an artifact. The checked repository revisions
describe the observed upstream state, not future releases or live service health.

No external executable, model, historical compiler, sibling build or acceptance
gate was run. No integration prototype or recovery-rate improvement is claimed.
Echo's paper artifact link was a placeholder at inspection; its reported
results remain author claims. Mizuchi's benchmark and every other unreplicated
performance claim are kept separate from implementation observations. The
[next prototype](compiler-response-prototype.md) supplies an explicit fidelity
test before adapters or orchestration dependencies are introduced.
