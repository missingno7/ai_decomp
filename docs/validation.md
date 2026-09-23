# Initial-pass validation

The first extraction produced four project dossiers, 20 mechanism records,
14 recovery trajectories, 21 scoped negative-evidence records, 33 upstream tool
references and 104 source identities. The shared implementations are the
metadata experiment matrix and read-only provenance checker; the catalog
importer/checker are workspace maintenance tools.

Validation performed in `ai_decomp`:

- `python -m unittest discover -s tests -v`: five tests pass, covering domain
  separation, output collapse with independent proof, failed compiles, malformed
  acceptance/identity metadata, provenance drift, missing files and path bounds.
- `python tools/check_workspace.py`: no dangling catalog relations, missing
  record sources, duplicate IDs, broken local Markdown links or invalid synthetic
  experiment records.
- `python tools/experiment_matrix.py experiments/examples/synthetic.json`:
  three synthetic trials become two classes, with changed compiler context kept
  separate despite the same test digest. This is a utility test, not a compiler
  experiment.
- All JSON files parsed. Python source compiled successfully. The proposed JSON
  Schemas were parsed as JSON; no external JSON Schema validator was installed
  or run. The standard-library experiment validator enforces the tested contract.
- Immutable source references were read from their exact local Git commits.
  Checkout newline differences were checked before converting worker filesystem
  hashes to canonical Git-blob hashes.

The final [provenance check receipt](../research/provenance-validation.json)
records 104 checked identities: 96 verified and eight drifted live files.
The changing files are Stunts status, validation, supervisor instructions,
blockers and camera declaration-order notes; SimAnt production queue and
MagnifyMenu mechanism metadata; and Icy Tower link status. Their inspected
identities remain in the catalog, and their distilled findings remain in the
dossiers. The changed content was not silently substituted. Uncommitted source
contents are not archived by a hash alone.

The Stunts validation/status disagreement is preserved explicitly. Empires'
frozen closure is attributed to its source receipts and implementation, not a
new run here. No source-repository compile, refresh, acceptance, promotion or
production edit was performed. Source repositories continued changing through
other work during this pass.

Independent review narrowed GCC causal hypotheses, rejected universal
declaration-order/model/batching claims, corrected a live FloodNestB source
mistakenly attributed to a commit, and found metadata consistency cases now
covered by utility tests. See [principles](../knowledge/principles.md) and the
[Icy synthesis audit](../research/icytower/audit.md).
