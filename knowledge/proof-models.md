# Proof models and shared vocabulary

This glossary is a **GENERIC METHOD** for interpreting records. Project-specific
definitions override the convenient shared terms. Provenance: the proof/workflow
sections of all four [project dossiers](comparison.md), especially Empires
`build_production.py`, Stunts `check_candidate.py`, SimAnt `docs/factory.md`,
and Icy Tower `docs/proof-levels.md`.

| Term | Shared use and differences that matter |
|---|---|
| Oracle | Immutable evidence target plus coordinate/identity contract. Empires uses full EXE and relocation metadata; Stunts a pristine hybrid baseline; SimAnt member/NE evidence; Icy original PE/DWARF/COFF evidence. |
| Strict match | Only the named project gate at the stated scope. Never shorthand for an alignment score. |
| Function match | In Icy, all function bytes after independently resolved relocations/direct transfers. Other projects may require additional member contributions before granting credit. |
| Body match | Code-level equality under declared resolution. Does not imply correct private data, selector pools, fixups, neighbors or link layout. |
| Object/member match | Complete claimed contribution: public/extent/code/bindings/private segments as applicable. SimAnt member admission is stronger than aligned code; a scaffolded unit does not recover unclaimed stubs. |
| TU/CU match | Full compilation-unit contribution under that project's proof contract; exact functions or historical source order do not imply it. |
| Whole-executable closure | Full output identity and required structure from reconstructed inputs. Empires has frozen adapter-free historical closure. Stunts HYBRID_EXACT deliberately includes an unrecovered raw remainder. |
| Effective output identity | Identity of output under an explicit scope/normalizer/context. Raw object hashes and normalized code+relocation hashes answer different questions. |
| Binding | Interpretation connecting symbolic target/owner to an independently established address or contribution. |
| Fixup / relocation | Object/link/load adjustment with format-specific site, target, frame, addend and ordering semantics. Empires ordered MZ relocations must not be sorted away; SimAnt far selectors/offsets require semantic pairing. |
| Production lane | Authoritative acceptance, credit and publication path; usually serialized or guarded. |
| Isolated research lane | Bounded experiments and artifacts without promotion authority. An informative parser-supported object can remain production-blocked. |
| Budget-censored | Stopped for cost/time/process policy before justified convergence; not a model failure. |
| Search-converged | Tested axes exhausted their discriminating output classes under this fixed context; not all possible source search exhausted. |
| Tooling-blocked | Required compiler/parser/runner/proof capability is unavailable or unsupported. |
| Evidence-blocked | Cannot justify a next source/context/binding claim from available evidence. |
| Compiler context | Toolchain, profile, ABI, headers/declarations, TU members and order, driver/runner and relevant state; body text alone is insufficient. |
| Hypothesis batch | Preregistered, bounded, independently interpretable alternatives; not an undirected Cartesian explosion. |
| Mismatch dimension | Separately measured residue such as allocation, opcode, extent, CFG, fixup identity, private-data placement or peer regression. |
| Exact anchor | An exact correspondence under a diagnostic contract; useful positive evidence, not necessarily historical variable identity or a complete proof. |

**CROSS-PROJECT PATTERN.** Useful proof forms constitute multiple dimensions,
not a universal linear score. A function can gain source-order evidence without
gaining byte equality, or match bytes while losing binding or neighbor proof.

For each strict result record the verifier, input identities, scope, receipt,
freshness/cache policy and remaining obligations. Keep diagnostic and promotion
states distinct. No shared tool in this workspace is authorized to translate
another project's status into acceptance.


The [historical convergence audit](../research/adversarial/empires-convergence.md)
adds an important distinction: an exact construction with declared structural
adapters is a different claim from natural source/topology closure. Preserve route,
raw/synthetic ownership, adapter inventory and intentional ASM/runtime categories.
A later source-quality claim does not retroactively change an earlier exact receipt.

A **recovery region** is a research coordinate set, potentially noncontiguous.
REGION_STABLE_EXACT requires a named instruction/fixup set and controls; it is not
FUNCTION_MATCH and does not compose into one without the native whole-scope proof.
Source-span bounds, byte budgets and DWARF names establish neither code equality
nor liveness. See [region obligations](large-function-regions.md).
