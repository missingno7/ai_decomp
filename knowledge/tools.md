# Tool inventory

Generated from the authored research dossiers. Record IDs are stable within this initial catalog.
Sources resolve through [the provenance catalog](../catalog/sources.json); refs and content hashes are explicit.
Read the linked project dossier for the discovery context and limitations.

## empires-build

**PROJECT FACT — empires.** Strict source-to-executable acceptance

[Project dossier](../research/empires/dossier.md).

**Inputs:** production plan/source/toolchain/oracle metadata

**Outputs:** EXE and fingerprinted receipt

**Dependencies:** project compiler/linker/OMF/MZ stack

**Assumptions:** Empires exact MZ topology

**Reuse:** project_specific

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/build_production.py](source-index.md#empires-src-45cc7b345cd3)

## empires-probe-tu

**PROJECT FACT — empires.** Test contiguous whole-TU hypothesis

[Project dossier](../research/empires/dossier.md).

**Inputs:** module range, source overrides, compiler flags

**Outputs:** whole-run byte/binding report

**Dependencies:** project manifests/compiler runner/original EXE

**Assumptions:** Empires plan, _TEXT and private DATA model

**Reuse:** adapter_required

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/probe_tu.py](source-index.md#empires-src-869276ee9754)

## empires-probe-module

**PROJECT FACT — empires.** Single-module C/ASM probe

[Project dossier](../research/empires/dossier.md).

**Inputs:** owner and source override

**Outputs:** code/DATA/fixup comparison

**Dependencies:** project OMF binder and toolchain

**Assumptions:** Cannot alone bind two library/runtime cases

**Reuse:** adapter_required

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/probe_module.py](source-index.md#empires-src-de5f08712288)

## empires-relocation-audit

**PROJECT FACT — empires.** Separate code equality from relocation route mismatch

[Project dossier](../research/empires/dossier.md).

**Inputs:** production plan, MZ and optional fresh objects

**Outputs:** direction/provenance audit

**Dependencies:** project MZ and OMF readers

**Assumptions:** TC2/TASM/TLINK observed ordering

**Reuse:** project_specific

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/audit_relocation_topology.py](source-index.md#empires-src-0502ff01d23b)

## empires-audit-flags

**PROJECT FACT — empires.** Explain compiler route flags by source

[Project dossier](../research/empires/dossier.md).

**Inputs:** plan and source

**Outputs:** unexplained flag audit

**Dependencies:** project source parser/plan

**Assumptions:** TC2 -B/-k semantics

**Reuse:** conceptually_reusable

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/audit_tu_flags.py](source-index.md#empires-src-8ea8a1ea9951)

## empires-cache

**PROJECT FACT — empires.** Content-addressed research compilation

[Project dossier](../research/empires/dossier.md).

**Inputs:** owner, includes, lock, driver

**Outputs:** cached object/receipt or fresh compile

**Dependencies:** reconstruct.py and local compiler

**Assumptions:** Owner/includes assumptions, acceptance disables cache

**Reuse:** adapter_required

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/object_cache.py](source-index.md#empires-src-e3a07a74275b)

## empires-fingerprint

**PROJECT FACT — empires.** Construction-input provenance fingerprint

[Project dossier](../research/empires/dossier.md).

**Inputs:** known source/layout/recipes/tool trees

**Outputs:** SHA256 aggregate

**Dependencies:** reconstruct.py and project DATA recipe

**Assumptions:** Hard-coded construction closure

**Reuse:** conceptually_reusable

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/factory_inputs.py](source-index.md#empires-src-585f2f7689d1)

## empires-candidate

**PROJECT FACT — empires.** Bounded FAST check and promotion/block logging

[Project dossier](../research/empires/dossier.md).

**Inputs:** task card and edited source interval

**Outputs:** diagnostic, archived attempt or acceptance

**Dependencies:** project factory/runtime assembler

**Assumptions:** All runtime bytes, publics, ordered fixups and strictly fewer unresolved bytes

**Reuse:** project_specific

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/check_candidate.py](source-index.md#empires-src-120338389bca)

## empires-relocation-groups

**PROJECT FACT — empires.** Suggest minimum shared-compilation runs

[Project dossier](../research/empires/dossier.md).

**Inputs:** MZ relocations and owner manifest

**Outputs:** candidate recipes and constraints

**Dependencies:** project MZ/compiler probes

**Assumptions:** 512-byte header coordinate conversion, descending TC2 runs

**Reuse:** project_specific

**License review:** No top-level source-tool license found; reference only. No code copied.

**Sources:** [tools/discover_relocation_groups.py](source-index.md#empires-src-aaa17885ef43)

## stunts-coordinates

**PROJECT FACT — stunts.** checked explicit coordinate-space conversion

[Project dossier](../research/stunts/dossier.md).

**Inputs:** coordinate, named space, optional segment, decompression mapping

**Outputs:** load-image or named-space coordinate

**Dependencies:** Python dataclasses; local common.require

**Assumptions:** specific spaces/header/base and the assertion dependency must be supplied by an adapter

**Reuse:** adapter_required

**License review:** No repository LICENSE/COPYING/NOTICE found; reference only, no copying reviewed.

**Synthesis note:** Checked conversions are generic in concept; concrete spaces and common.require make the existing script adapter-dependent.

**Sources:** [tools/coordinates.py](source-index.md#stunts-src-a50e39e12237) (anchor 1-L48)

## stunts-diagnostics

**PROJECT FACT — stunts.** pure stream alignment, anchors, mismatch islands and operand-family diagnostics

[Project dossier](../research/stunts/dossier.md).

**Inputs:** target/candidate bytes, fixups, binding/context flags

**Outputs:** structured comparison and compact summary

**Dependencies:** Capstone 5.0.3; local common

**Assumptions:** x86 16-bit decoding and Stunts fixup meanings

**Reuse:** conceptually_reusable

**License review:** No repository LICENSE/COPYING/NOTICE found; reference only, no copying reviewed.

**Sources:** [tools/diagnostics.py](source-index.md#stunts-src-ad637d16775d) (anchor 23-L28); [tools/diagnostics.py](source-index.md#stunts-src-ad637d16775d) (anchor 410-L457)

## stunts-research-batch

**PROJECT FACT — stunts.** archive preregistered hypotheses, ceiling compiler launches, cluster effective outputs and compare candidates

[Project dossier](../research/stunts/dossier.md).

**Inputs:** Stunts context-index/card plus JSON manifest of 2-32 hypotheses/predictions/falsifiers

**Outputs:** private receipts, outcome matrix and pairwise diagnostic summary

**Dependencies:** Stunts compiler, MZ/oracle, context index/workflow/cards, diagnostics

**Assumptions:** Stunts evidence extent, recipe/snapshot/context-index and private build root

**Reuse:** adapter_required

**License review:** Untracked working-tree tool; no repository license found; reference only.

**Sources:** [tools/research_batch.py](source-index.md#stunts-src-1b46d38619e0) (anchor 67-L223); [docs/current/worker-research.md](source-index.md#stunts-src-3f7f26d672ca) (anchor 15-L17)

## stunts-check-candidate

**PROJECT FACT — stunts.** fresh FAST/staged/canonical candidate acceptance and promotion guard

[Project dossier](../research/stunts/dossier.md).

**Inputs:** task, candidate source, workflow snapshot

**Outputs:** receipt or archived failure

**Dependencies:** Stunts exact build, workflow and oracle

**Assumptions:** serial Stunts promotion and manifest locks

**Reuse:** project_specific

**License review:** No repository license found; reference only.

**Sources:** [tools/check_candidate.py](source-index.md#stunts-src-8d5b85ee6620) (anchor 13-L103)

## stunts-oracle

**PROJECT FACT — stunts.** find, hash, lock and materialize pristine oracle inputs

[Project dossier](../research/stunts/dossier.md).

**Inputs:** configured MCGA/oracle assets and lock file

**Outputs:** identity report and optional oracle materialization

**Dependencies:** Stunts assets, EXEPACK/MZ modules, layout lock

**Assumptions:** case-insensitive asset names and Stunts oracle layout

**Reuse:** adapter_required

**License review:** No repository license found; reference only.

**Sources:** [tools/oracle.py](source-index.md#stunts-src-c4ceae488459) (anchor 33-L76)

## stunts-inspect-object

**PROJECT FACT — stunts.** inspect OMF code/fixups and archive a private research receipt

[Project dossier](../research/stunts/dossier.md).

**Inputs:** OMF object, target bytes, Stunts evidence JSON

**Outputs:** research-object-inspection.json

**Dependencies:** Stunts omf reader/evidence/private-root policy

**Assumptions:** Microsoft OMF and Stunts segment semantics

**Reuse:** project_specific

**License review:** No repository license found; reference only.

**Sources:** [tools/inspect_object.py](source-index.md#stunts-src-2fc663b6dc57) (anchor 22-L25); [tools/inspect_object.py](source-index.md#stunts-src-2fc663b6dc57) (anchor 142-L252)

## stunts-probe-tu

**PROJECT FACT — stunts.** controlled translation-unit compiler probe

[Project dossier](../research/stunts/dossier.md).

**Inputs:** probe source and Stunts compiler/oracle context

**Outputs:** candidate/oracle comparison result

**Dependencies:** Stunts compiler.py and oracle.py

**Assumptions:** MSC runner and MZ oracle

**Reuse:** adapter_required

**License review:** No repository license found; reference only.

**Sources:** [tools/probe_tu.py](source-index.md#stunts-src-025bb1bafcdd) (anchor 1-L35)

## stunts-grind

**PROJECT FACT — stunts.** budgeted attempt archival and guarded serial promotion workflow

[Project dossier](../research/stunts/dossier.md).

**Inputs:** Stunts recovery candidate/card and command

**Outputs:** attempt ledger/report/promotion state

**Dependencies:** check_candidate, build_exact, reconstruction_factory, workflow

**Assumptions:** Stunts queue and recovery/candidates layout

**Reuse:** project_specific

**License review:** No repository license found; reference only.

**Sources:** [tools/grind.py](source-index.md#stunts-src-0099966f0e5d) (anchor 1-L113)

## simantw-codegen-grinder

**PROJECT FACT — simantw.** bounded source-variant compile/score/archive runner with compact raw-OMF compiler-response classes

[Project dossier](../research/simantw/dossier.md).

**Inputs:** spec, source/template, axes, flags

**Outputs:** candidate receipts, identities, comparisons, compiler_response classes

**Dependencies:** compiler, OMF/matcher, cache

**Assumptions:** MSC7 and SimAnt fixture/proof interfaces

**Reuse:** adapter_required

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/codegen_grinder.py](source-index.md#simantw-src-071808eb1c6d)

## simantw-codegen-cache

**PROJECT FACT — simantw.** identity-validated compiler cache

[Project dossier](../research/simantw/dossier.md).

**Inputs:** source/tool/compiler identity

**Outputs:** cached object/receipt

**Dependencies:** project compiler wrapper

**Assumptions:** SimAnt identity schema

**Reuse:** conceptually_reusable

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/codegen_cache.py](source-index.md#simantw-src-ebb8d5ca8d31)

## simantw-codegen-diff

**PROJECT FACT — simantw.** instruction-aligned candidate diagnostic distinct from acceptance

[Project dossier](../research/simantw/dossier.md).

**Inputs:** target/candidate code, bindings, closures

**Outputs:** feature categories and aligned diff

**Dependencies:** Capstone, project CFG/matcher data

**Assumptions:** 16-bit decode plus known LINK transforms

**Reuse:** adapter_required

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/codegen_diff.py](source-index.md#simantw-src-b9e6348f699a)

## simantw-compiler-service

**PROJECT FACT — simantw.** persistent isolated historical compiler request service

[Project dossier](../research/simantw/dossier.md).

**Inputs:** immutable request snapshots

**Outputs:** objects, receipts, worker state

**Dependencies:** DOSBox-X, Win3.x, MSC7 worker

**Assumptions:** SimAnt runner/mount/locks

**Reuse:** project_specific

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/compiler_service.py](source-index.md#simantw-src-7042abd78f7f)

## simantw-omf

**PROJECT FACT — simantw.** OMF record/member parser

[Project dossier](../research/simantw/dossier.md).

**Inputs:** OMF bytes

**Outputs:** records, module structure

**Dependencies:** none apparent

**Assumptions:** OMF variant used by MSC7

**Reuse:** adapter_required

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/omf.py](source-index.md#simantw-src-db3807d912fa)

## simantw-tu-assembly

**PROJECT FACT — simantw.** compose verified sources, declaration order, pool/data scaffolds, strict unit tests

[Project dossier](../research/simantw/dossier.md).

**Inputs:** component sources/topology/profile

**Outputs:** candidate TU, scaffold evidence, promotion inputs

**Dependencies:** SimAnt topology, matcher, compiler

**Assumptions:** MSC7 selector pools and MAPSYM

**Reuse:** project_specific

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/tu_assembly.py](source-index.md#simantw-src-c2fb20671d05)

## simantw-blocked-reclassification

**PROJECT FACT — simantw.** fresh current-profile blocker taxonomy

[Project dossier](../research/simantw/dossier.md).

**Inputs:** jobs, preserved candidates, topology/profile

**Outputs:** root-cause report and optional write-back

**Dependencies:** SimAnt workflow/matcher

**Assumptions:** project categories and sources

**Reuse:** conceptually_reusable

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/blocked_reclassification.py](source-index.md#simantw-src-58d39ac26e79)

## simantw-mirror-pairs

**PROJECT FACT — simantw.** derive/test constrained black-red source mirrors

[Project dossier](../research/simantw/dossier.md).

**Inputs:** preserved source, MAPSYM twin map, target

**Outputs:** derived candidate/asymmetry record

**Dependencies:** SimAnt symbols/compiler/matcher

**Assumptions:** verified mirrored naming/layout

**Reuse:** adapter_required

**License review:** reference only; repository license not established; do not copy

**Sources:** [tools/mirror_pairs.py](source-index.md#simantw-src-1d9821e62051) (anchor [77])

## icytower-dwarf-locations

**PROJECT FACT — icytower.** decode and annotate DWARF local locations

[Project dossier](../research/icytower/dossier.md).

**Inputs:** location lists, PC, frame/scopes

**Outputs:** location/scope annotations

**Dependencies:** DWARF expression format and project census

**Reuse:** adapter_required

**License review:** reference_only; inspect parser provenance before extraction

**Sources:** [tools/dwarf_locations.py](source-index.md#icytower-src-c196ae83cab0) (anchor 15-96); [README.md](source-index.md#icytower-src-c52e8cebd6cb) (anchor 98-103)

## icytower-compiler-probe

**PROJECT FACT — icytower.** bounded predecessor/type/flag compiler-context probes

[Project dossier](../research/icytower/dossier.md).

**Inputs:** target/function/peer/type/flag variant

**Outputs:** hash-bound compiler and RTL evidence

**Dependencies:** locked TDM GCC and Icy Tower build layout

**Reuse:** project_specific

**License review:** reference_only

**Sources:** [tools/compiler_probe.py](source-index.md#icytower-src-5691234f1115) (anchor 16-128); [docs/compiler-context-evidence.md](source-index.md#icytower-src-43f744d0a15f) (anchor 53-65)

## icytower-tu-context-probe

**PROJECT FACT — icytower.** full-CU overlay construction and focused comparison

[Project dossier](../research/icytower/dossier.md).

**Inputs:** TU/spec/order/bodies/statics/prototypes

**Outputs:** compiled overlay and comparison receipt

**Dependencies:** Icy Tower units, ledger, GCC build

**Reuse:** adapter_required

**License review:** reference_only

**Sources:** [tools/tu_context_probe.py](source-index.md#icytower-src-93277837d0f9) (anchor 28-422); [docs/compiler-context-evidence.md](source-index.md#icytower-src-43f744d0a15f) (anchor 38-51)

## icytower-source-order

**PROJECT FACT — icytower.** derive guarded source-order plans

[Project dossier](../research/icytower/dossier.md).

**Inputs:** DWARF unit ledger

**Outputs:** task plans

**Dependencies:** unique DWARF lines and Icy Tower schema

**Reuse:** conceptually_reusable

**License review:** reference_only

**Sources:** [tools/source_order.py](source-index.md#icytower-src-9f47c890bb6a) (anchor 9-107); [docs/compiler-context-evidence.md](source-index.md#icytower-src-43f744d0a15f) (anchor 38-51)

## icytower-effective-outcomes

**PROJECT FACT — icytower.** group output-equivalent experiment attempts

[Project dossier](../research/icytower/dossier.md).

**Inputs:** function attempt JSON

**Outputs:** effective output clusters

**Dependencies:** attempt record field schema

**Reuse:** conceptually_reusable

**License review:** reference_only; candidate for adapter-neutral manifest

**Sources:** [tools/effective_outcomes.py](source-index.md#icytower-src-4e248a49d0c7) (anchor 15-86); [docs/attempts/research-luna-draw/status-pose-independent-20260923.md](source-index.md#icytower-src-22231bb443b7) (anchor 21-38)

## icytower-instruction-alignment

**PROJECT FACT — icytower.** bounded decoded instruction correspondence

[Project dossier](../research/icytower/dossier.md).

**Inputs:** comparison rows

**Outputs:** alignment analysis

**Dependencies:** Icy Tower row schema and x86 records

**Reuse:** adapter_required

**License review:** reference_only

**Sources:** [tools/instruction_alignment.py](source-index.md#icytower-src-0b2777a52740) (anchor 9-58); [docs/production-line-audit.md](source-index.md#icytower-src-b2d9dc482859) (anchor 25-27)

## icytower-rtl-evidence

**PROJECT FACT — icytower.** normalize/compare compiler pass dumps

[Project dossier](../research/icytower/dossier.md).

**Inputs:** two dump trees

**Outputs:** changed-pass report

**Dependencies:** GCC dump naming/normalization

**Reuse:** conceptually_reusable

**License review:** reference_only

**Sources:** [tools/rtl_evidence.py](source-index.md#icytower-src-24b8112b067b) (anchor 8-29); [docs/attempts/research-supervisor-play/play-summary-rtl-common-tail-20260923.md](source-index.md#icytower-src-c517626b278f) (anchor 13-25)

## icytower-promote-function

**PROJECT FACT — icytower.** FAST diagnosis and strict, atomic proof promotion

[Project dossier](../research/icytower/dossier.md).

**Inputs:** target/function/current receipts

**Outputs:** diagnostic or published recovery state

**Dependencies:** full Icy Tower verifier, COFF/DWARF resolvers, locks

**Reuse:** project_specific

**License review:** reference_only; do not transplant gate

**Sources:** [tools/check_function.py](source-index.md#icytower-src-3f1ce3a5c386) (anchor 10-150); [tools/promote_function.py](source-index.md#icytower-src-1a800deb70fe) (anchor 19-128); [docs/proof-levels.md](source-index.md#icytower-src-0e77b5d3779f) (anchor 3-48)
