# Diff and oracle tools for matching work

External implementation study, inspected 2026-09-23.  This note concerns
comparison and feedback tools, not source recovery.  The checked revisions are
`asm-differ` `0dd09af8f8008f1f880327cf0aca3b26d2562ea2`, `objdiff`
`fba10a617154f19b3fc25c8817dc81f81d8489b5`, and `reccmp`
`e91a51bfadfbb600adfdc750589ac40ae9742883`.  Claims about the four local
projects are separately marked **PROJECT FACT** and cite their frozen research
records; external implementation observations are **EXTERNAL IMPLEMENTATION
FACT**. No upstream binary was executed, dependency installed, or implementation
vendored into the tracked workspace; ignored source checkouts were inspection inputs.

## Decision

**objdiff is the strongest reusable comparison *interface* for Icy Tower's
COFF/x86 object-level diagnostic loop.**  It decodes x86, reads COFF through
the Rust `object` backend, represents code/data/BSS symbols and relocations,
returns instruction rows with argument and branch correspondence, and has a
one-shot structured API.  Its MIT-or-Apache-2.0 license permits an optional
out-of-process adapter.  This is a recommendation to evaluate an adapter, not
to make it an acceptance oracle: the local Icy proof also requires CU context,
DWARF-scope/ownership reasoning and its strict protected-neighbor gate.

**asm-differ is immediately useful as a viewer and a design reference, not a
proof component.**  Contrary to the common shorthand that it is only a
MIPS/PPC tool, current upstream has limited `x86` and `i686` settings and
parses several 16/32-bit relocation spellings.  Its x86 implementation is a
textual `objdump` processor which recognizes `ret`, branch names and a bounded
set of ELF/COFF/OMF-like relocation strings; it is not an OMF parser or an MZ,
NE or PE verifier.  It can show a saved previous compile in a three-way view,
classify same-mnemonic register and stack differences, and output JSON, but it
does not retain experiment histories or establish equality.

**reccmp is the closest comparator for old MSVC Win32 reconstruction, but its
notion of an “effective match” must be kept outside strict historical proof.**
It pairs original/recompiled entities using source annotations and the
recompiled PDB/CV dump, compares functions, data, vtables, imports and layout
in PE/NE/MZ images, and deliberately discounts selected operand-order and
register-allocation differences.  That makes its feedback unusually useful for
triage of a 32-bit MSVC project, but the semantic normalizations are not
interchangeable with byte/fixup/relocation equality.  Its AGPL-3.0 license also
requires a separate licensing decision before copying or linking its
implementation into this workspace.

None of the three is a source-hypothesis generator, knows a historical compiler
by model/version, chooses retries, runs a multi-candidate search, deduplicates
compiler outputs, or models translation-unit construction as a search state.
They supply diagnostic feedback around a human-controlled build loop.

## Capability and feedback comparison

| Dimension | asm-differ | objdiff | reccmp |
|---|---|---|---|
| Primary purpose | Assembly diff viewer for matching projects | Object-file code/data diff and project progress UI | Original/recompiled image comparison for annotated decompilation projects |
| Architectures implemented | MIPS, PPC, ARM32, AArch64, SH2/4, m68k, x86/i686 (README calls x86 limited) | ARM/64, MIPS, PPC, SuperH, x86/x86-64 | Current comparison path is old 32-bit x86 MSVC; PE reader rejects non-i386 for its normal code path |
| Language/compiler knowledge | None; configurable disassembler/build command | No source-language model; C/C++ symbol demangling and compiler-format accommodations | C++/old MSVC focused; PDB/CV, annotations, MSVC symbol matching and type/vtable rules |
| Formats/evidence | Whole binaries, `.o`, or ELF symbol path through external `objdump`; relocation interpretation is architecture/text-parser dependent | Relocatable objects, including ELF and COFF representations exposed by `object`; not MZ/NE/OMF | PE, NE and MZ image readers; recompiled PDB/CV dump and source annotations; not an OMF object comparator |
| Compile loop / retries | Optional `make`, file watch and target/current/previous three-way display; no candidate generation/retry control | Configured build target/base, source watch and re-diff; no candidate search | Compares already-built images; aggregate combines saved reports, not compiler attempts |
| Candidate score | Weighted stack (1), register (5), reorder (60), insertion/deletion (100) penalties | Patience-aligned score: immediate 1, register 5, replacement 60, insert/delete 100; percentage | Function/data/vtable ratios plus “effective match” after semantic fixes |
| Structured feedback | JSON rows, source lines where objdump provides them, branch visualization and current/previous score | Typed instruction rows, argument mismatch indices, branch from/to, symbols, data and relocation diff records; CLI/WASM bindings | Raw aligned assembly/text diffs and reports; stack comparator, data/vtable/exports/roadmap tools |
| Relocations/data/layout | Rewrites selected relocation text for display; no raw ordering/complete object proof | First-class relocation target/type/addend diff and data/BSS/section diff; configuration can relax function relocation checks | Reads PE/NE/MZ relocation-bearing images and compares data/layout; function “effective” normalizations are intentionally less strict |
| Automation / AI / batch / dedup | Watch automation only; no AI, batch search or output clustering | Build/watch/UI/report automation only; no AI, batch search or output clustering | Report aggregation chooses best accuracy across samples; no AI, compiler retries or equivalent-output clustering |
| Translation-unit context | Build command only | Project builds objects; context is delegated to build system | PDB/source paths and annotations identify entities; it does not synthesize or vary a TU |
| License/reuse | Unlicense/public domain dedication | MIT OR Apache-2.0 | AGPL-3.0 |

### asm-differ

**EXTERNAL IMPLEMENTATION FACT.** `diff.py` accepts `-o` objects, ELF symbol
mode, sections, source/line-number display, configured `make`, filesystem
watching, current-vs-previous/base three-way modes, and color/plain/HTML/JSON
output.  Its scoring explicitly separates stack displacement and likely
register-allocation penalties from reordering and insertion/deletion.  Its
x86 processor normalizes a bounded collection of relocation records such as
`R_386_*`, `dir32`, `DISP32`, `OFF16/32`, `OFFPC16/32`, `SEG`, `FAR16` and
`WRTSEG`; it ignores a listed set of 16-bit floating-point fixups.  This proves
useful display support, not semantic OMF fixup comparison or ordered fixup
proof.  Sources: [CLI/modes](https://github.com/simonlindholm/asm-differ/blob/0dd09af8f8008f1f880327cf0aca3b26d2562ea2/diff.py#L131-L395),
[score](https://github.com/simonlindholm/asm-differ/blob/0dd09af8f8008f1f880327cf0aca3b26d2562ea2/diff.py#L3663-L3789),
[x86 processor](https://github.com/simonlindholm/asm-differ/blob/0dd09af8f8008f1f880327cf0aca3b26d2562ea2/diff.py#L2068-L2238),
[x86 settings](https://github.com/simonlindholm/asm-differ/blob/0dd09af8f8008f1f880327cf0aca3b26d2562ea2/diff.py#L3037-L3154).

For Stunts or SimAnt, the potentially reusable part is a *presentation* of
aligned bytes/instructions and candidate-parent-oracle three-way state.  It
cannot replace Stunts' strict OMF/binding gate or SimAnt's semantic OMF/NE
fixups and private contributions (**PROJECT FACT**: `research/stunts/dossier.md`
lines 7-11, 33-43; `research/simantw/dossier.md` lines 71-89).  Its permissive
license permits borrowing ideas or optional process-level use, but this
workspace should not import its parser as if it understood these formats.

### objdiff

**EXTERNAL IMPLEMENTATION FACT.** Objdiff's core creates matched symbol and
section diffs for code, data, BSS and common sections.  It returns typed rows
with operation/argument mismatch kind and branch origin/destination, plus
relocation type, target symbol and addend.  Code comparison checks relocation
flags, target/name/address policy and addends; the project configuration can
explicitly relax those checks, so acceptance users must lock the strict setting
rather than infer strictness from a high percentage.  It watches configured
source files and invokes the configured build, but each invocation compares a
base object rather than scheduling alternatives.  Sources:
[object diff model](https://github.com/encounter/objdiff/blob/fba10a617154f19b3fc25c8817dc81f81d8489b5/objdiff-core/src/diff/mod.rs#L20-L145),
[code/relocation comparison](https://github.com/encounter/objdiff/blob/fba10a617154f19b3fc25c8817dc81f81d8489b5/objdiff-core/src/diff/code.rs#L56-L157),
[relocation policy](https://github.com/encounter/objdiff/blob/fba10a617154f19b3fc25c8817dc81f81d8489b5/objdiff-core/src/diff/code.rs#L299-L384),
[x86 implementation](https://github.com/encounter/objdiff/blob/fba10a617154f19b3fc25c8817dc81f81d8489b5/objdiff-core/src/arch/x86.rs),
[build/watch schema](https://github.com/encounter/objdiff/blob/fba10a617154f19b3fc25c8817dc81f81d8489b5/config.schema.json#L42-L85).

This makes an Icy COFF object adapter the highest-value external experiment:
it could provide a machine-readable comparator with aligned x86 operands,
branches, relocations, symbols and data without reimplementing a UI.  The
adapter must report raw object identities alongside objdiff's normalized
feedback and preserve the local acceptance boundary.  It does not cover
SimAnt's OMF/NE, Empires' OMF/MZ ordered relocation closure, or Stunts' OMF
reader/binding evidence.  Objdiff uses a generic object-file backend rather
than an OMF reader; no OMF support was found in its current source tree.

### reccmp

**EXTERNAL IMPLEMENTATION FACT.** Reccmp builds an entity database from the
original/recompiled images, source annotations, and a recompiled PDB processed
by `cvdump`; it matches functions, variables, vtables, imports/exports and
section data before producing reports.  Its function comparator may mark a
non-byte-identical function effective after explicit operand/compare order and
register-swap analysis.  That is a conscious semantic-progress convention,
not strict recompilation equality.  The separate aggregate command combines
saved accuracy reports and can diff reports, but does not retain source
candidates or compile/retry them.  Sources:
[PDB-driven setup](https://github.com/isledecomp/reccmp/blob/e91a51bfadfbb600adfdc750589ac40ae9742883/reccmp/compare/core.py#L302-L352),
[comparator routing](https://github.com/isledecomp/reccmp/blob/e91a51bfadfbb600adfdc750589ac40ae9742883/reccmp/compare/core.py#L411-L444),
[effective-match fixes](https://github.com/isledecomp/reccmp/blob/e91a51bfadfbb600adfdc750589ac40ae9742883/reccmp/compare/asm/fixes.py#L473-L535),
[register swap test](https://github.com/isledecomp/reccmp/blob/e91a51bfadfbb600adfdc750589ac40ae9742883/reccmp/compare/asm/swap.py#L45-L79),
[aggregate](https://github.com/isledecomp/reccmp/blob/e91a51bfadfbb600adfdc750589ac40ae9742883/reccmp/tools/aggregate.py#L16-L191),
[formats](https://github.com/isledecomp/reccmp/tree/e91a51bfadfbb600adfdc750589ac40ae9742883/reccmp/formats).

Its PE/NE/MZ readers make it a useful study reference for SimAnt's executable
side, but current source does not make it an OMF object/fixup comparator.  It
may be valuable as a separate AGPL tool for a future old-32-bit-MSVC project
with a recompiled PDB; it is not a candidate library dependency for
`ai_decomp`.  In particular, Stunts' mismatch islands/families and SimAnt's
strict raw/semantic fixup distinctions should be preserved as diagnostic and
proof layers rather than collapsed into reccmp's effective-match boolean.

### binutils-omf: an OMF diagnostic dependency, not a proof engine

**EXTERNAL IMPLEMENTATION FACT.** Decomp.me's current MS-DOS platform pins the
`decompals/binutils-omf` v0.4 release tools `omf-nm` and
`omf-objdump --no-objects`; its Dockerfile pins the release archive checksum.
The inspected upstream fork at `f1b7e688723c883f61b6573e9f0cab12624dc320`
has an i386 OMF BFD reader with `FIXUPP`/`FIXUPP386` decoding, target methods
for SEGDEF/GRPDEF/EXTDEF/explicit frames, and frame methods. It therefore
offers a credible external **disassembly/symbol diagnostic** for old x86 OMF
objects, unlike objdiff's present OMF gap. Sources:
[decomp.me platform](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/platforms.py#L86-L95),
[pinned release](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/Dockerfile#L116-L125),
[FIXUPP reader](https://github.com/decompals/binutils-omf/blob/f1b7e688723c883f61b6573e9f0cab12624dc320/bfd/i386omf.c#L1193-L1425).

The inspected `i386omf.c` source is GPL-2.0-or-later and should remain an
invoked external diagnostic if evaluated. Do not copy/link its parser into this
workspace. The presence of a BFD relocation view does not prove its output preserves raw
FIXUPP record order, private contributions, target/frame semantics or
linker-visible topology required by Stunts, SimAnt, and Empires. Test those
properties against a known local object corpus before relying on it for more
than decoded instructions/symbol names. The fork is a large mixed-license
binutils distribution, so a future redistribution decision needs a complete
component-level license audit rather than this reader-file observation.

## What this adds to the local requirements

**PROJECT FACT.** Local requirements exceed a function percentage.  Stunts
uses context-bound effective output identities, candidate-to-parent-to-oracle
deltas, decoded mismatch islands/families and an OMF/MZ binding boundary.
SimAnt requires OMF/NE private contributions and semantic fixups; Empires
requires ordered MZ relocations and link/TU route closure; Icy Tower separately
proves COFF code/data/relocations, DWARF scope/source order, whole-CU
predecessor effects and protected neighbors.  Sources: respective dossiers
listed above; Empires `research/empires/dossier.md` lines 37-63; Icy
`research/icytower/dossier.md` lines 37-66, 116-125.

The missing shared capability is therefore not another diff display.  It is an
adapter-neutral **structured compiler-response record**: immutable compiler/TU
context; source hypothesis axes; raw code, relocation/fixup, data/layout and
symbol identities; candidate-vs-parent-vs-oracle aligned deltas; effective
output clustering; protected-neighbor effects; and a strict result kept
independent from score/semantic normalization.  Existing diff tools can feed
some fields, but none supplies the record, performs multi-hypothesis selection,
or escalates from source spelling to ABI/TU/build hypotheses.
