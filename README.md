# ai_decomp

A shared research memory and small analysis-tool workspace for matching
decompilation. It preserves mechanisms, failed experiments and discovery paths
already established in four sibling projects. It is an initial evidence layer,
not a universal compiler framework or a replacement acceptance system.

Start with the [cross-project comparison](knowledge/comparison.md), then choose
a precedent from the [mechanism catalog](knowledge/mechanisms.md) or
[recovery trajectories](knowledge/trajectories.md). For a new binary, use the
[bootstrap guide](docs/new-project-bootstrap.md). For ongoing agent research,
read [experiment design](knowledge/experiment-design.md) and
[agent workflows](knowledge/agent-workflows.md).
Concrete [next-work recommendations](docs/next-work.md) connect the findings
to the current Stunts, SimAnt and Icy Tower problems.

The [matching-decompilation ecosystem study](knowledge/ecosystem.md) answers
what already exists, what to reuse and what remains missing. It includes a
[capability matrix](knowledge/ecosystem-capabilities.md), implementation studies
of seven core tools, focused research prior art, and a
[next-prototype specification](docs/compiler-response-prototype.md).
External implementation facts and author claims stay separate from local
project evidence. Pinned records live in `research/ecosystem/`, indexed by
`catalog/ecosystem/index.json`; the original local catalogs remain unchanged.
See the [ecosystem validation record](docs/ecosystem-validation.md) for checks
and the limits of the source-only research pass.

The [fleet architecture falsification review](research/fleet/evaluation.md)
tests cheap-worker economics against raw Stunts measurements and current native
locking/recovery code. It supports a bounded Luna-first trial while retaining
the proposed model hierarchy and large-fleet economics as hypotheses. See
[unattended workflow boundaries](knowledge/fleet-operation.md) and the
[compact result/report contract](experiments/fleet-results.md).
The [fleet validation record](research/fleet/validation.md) retains source drift
and the limits of the metadata-only prototype.

The [adversarial A–H review](research/adversarial-synthesis-20260923.md) tests
genericity, blocker causes, convergence, project-stage bias and recovery regions.
It includes a complete Icy function-byte census, historical Empires milestones,
fresh Stunts/SimAnt tooling evidence, [frozen replay proposals](docs/historical-replay.md)
and a [read-only region inventory](knowledge/large-function-regions.md).
The review rejects several attractive generalizations and keeps independent
region grinding and broad fleet economics as experiments.
The [validation record](research/adversarial/validation.md) distinguishes passing
metadata checks from drift in actively changing source snapshots.

Every important claim retains one of four meanings:

| Label | Meaning |
|---|---|
| PROJECT FACT | Observed in a named project/toolchain/context; not automatically portable. |
| CROSS-PROJECT PATTERN | Independently observed in multiple projects; the common statement is deliberately narrower than its individual mechanisms. |
| WORKING HYPOTHESIS | Plausible but still awaiting a discriminating test. |
| GENERIC METHOD | A procedure that does not assume compilers behave identically. |

Sources are repository-relative paths with commit identity or an explicitly
hashed working-tree snapshot. **A hash of an uncommitted file identifies evidence
but does not preserve its contents.** Follow [provenance rules](docs/provenance.md)
before relying on a live artifact that may have changed.

The 2026-09-23 inventory used these repositories, discovered relative to this
workspace's parent. They were read-only throughout this pass; no upstream build,
refresh, promotion or compiler command was run.

| Source | Entry point | Authority |
|---|---|---|
| `../empires_reconstruction` | [Empires dossier](research/empires/dossier.md) | Frozen `historical-exact-oracle-v1`, peeled commit `873d1df0f505601d760c6880cdea0c6ae3d81405`; live portable branch kept separate. |
| `../stunts_recon` | [Stunts dossier](research/stunts/dossier.md) | Dirty current checkout and newest workflow/evaluation artifacts. |
| `../simantw_recon` | [SimAnt dossier](research/simantw/dossier.md) | Dirty `codex/simantw-recovery` checkout, generated queue and recovery experiments. |
| `../icytower_recon` | [Icy Tower dossier](research/icytower/dossier.md) | Current ledger, dirty/untracked attempts, DWARF/context/pass evidence. |

The [principles and falsification audit](knowledge/principles.md) explain which
generalizations survive comparison. The [proof vocabulary](knowledge/proof-models.md)
keeps body, member, TU, layout and executable claims separate. Negative findings
are first-class entries in [negative evidence](knowledge/negative-evidence.md).

`catalog/` contains normalized projects, mechanisms, trajectories, negative
evidence, tools and source manifests. `research/` retains authored extraction
details. `knowledge/` contains synthesis and generated browsing pages.
`experiments/` proposes small metadata contracts with clearly synthetic test
examples; `research/fleet/` also includes a sanitized archived Stunts replay.
Nothing requires the source repositories to adopt this model.
The [initial validation report](docs/validation.md) records the extraction
counts, utility checks and live-source drift limitations.

Small analysis tools are available; see [tool choices](docs/shared-tools.md):

```powershell
python tools/experiment_matrix.py experiments/examples/synthetic.json
python tools/provenance_check.py
python tools/fleet_report.py research/fleet/stunts-replay.json
python -m unittest discover -s tests
```

The matrix clusters only context-compatible output identities and preserves
individual strict results. The provenance checker reads Git blobs or live files
and detects missing/drifted evidence; it cannot recreate uncommitted history.
The fleet reducer summarizes scoped results, explicit blocker signatures and
cost coverage; it does not schedule workers. None compiles code or grants a match.
No game assets, oracle byte ranges,
historical tools, SDKs or copied upstream scripts are included.

To maintain this workspace, update the relevant authored dossier/records with
new evidence, run `python tools/build_catalogs.py`, then validate provenance,
links and fixtures. Do not silently replace an old finding with moving HEAD.
