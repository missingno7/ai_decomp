# Empires: frozen closure and its discovery path

Inspected 2026-09-23. Repository discovered as `../empires_reconstruction`.
Live checkout: `portable-sdl3`, commit `9f9adaf8c5c2b503eeecee7aa1291df5097ef77c`, clean at inspection.
Historical authority: annotated tag `historical-exact-oracle-v1`, peeled commit
`873d1df0f505601d760c6880cdea0c6ae3d81405`. The earlier tag
`historical-exact-closure` peels to `e56855c647051b53b5c62fea134a7b8d4af84770`.
Use the later freeze for closure claims. No builds or report refreshes were run.

## Current versus historical authority

**PROJECT FACT.** The frozen receipt in `docs/current/status.json` reports
fresh ACCEPTANCE, the original full executable SHA-256, 106 ordered relocations,
one TLINK invocation, zero raw EXE fallback, zero unresolved symbols, and no
remaining structural adapters. BSS ownership covers all 37,250 bytes. The
freeze frontier records 71 modules: 60 C units, ten hand-written ASM modules,
and the runtime block. These are recorded upstream proofs, not a new verification
by this workspace. Exact construction is separate from certainty about every
historical filename, byte-neutral TU boundary, semantic name, or runtime root:
the status still records 18/20 closed entry roots.

The live branch develops an SDL3 port; its progress is outside historical closure.
Historical construction code and `docs/current` have no differences from the
freeze in the inspected checkout. Some prose *inside* those documents is stale:
the relocation audit's rule paragraph still mentions the temporary MUSIC TASM
representation, while its table, production plan and commit `5629059` establish
native C. `docs/exact-structural-link.md` and `docs/linker-adapter-ledger.md`
are useful intermediate trajectories, not authoritative final blocker lists.

## Inventory

| Dimension | Observed state and source at frozen commit |
|---|---|
| Compiler identity | `layout/toolchain.json` pins hashes for Turbo C 2.0, CPP, TASM 1.0, TLINK 2.0, compact-model C0C.OBJ and CC.LIB. Flags include `-c -mc -1- -f- -N-`. |
| Architecture/formats | 8086-compatible DOS real mode, OMF objects and MZ executable; see `tools/omf.py`, `tools/mz.py`, pinned flags. |
| Debug/source evidence | No DWARF/SYM authority used in the reviewed closure path. Publics, compiler signatures, relocations, DATA continuity and source probes drive structure recovery. |
| Strict proof | Natural object extents/publics, ordered source plan, one unmodified TLINK output, full EXE hash plus ordered relocations; optional original-file equality. `tools/build_production.py`, `tools/build_exe.py`. |
| Recovery workflow | Frozen CHEAP queue is empty. Retained factory uses bounded runtime cards, FAST checks, then fresh uncached full ACCEPTANCE. `docs/current/grinder-instructions.md`, `status.json`. |
| Grinder/supervisor | Worker edits only card interval, needs strict unresolved-byte reduction; two targeted failed fixes lead to archived/restored supervisor blocker. Supervisor mechanizes recurring failure classes. This is a workflow gate, not model exhaustion evidence. |
| Compiler experiments | `probe_module.py`, `probe_tu.py`, `probe_c_paths.py`; local historical tools, MS-DOS Player normal runner, DOSBox parity backend. Runner and compiler identities are separate. No comparable cross-project startup benchmark was measured. |
| TU/topology | `layout/production-plan.json`, module recipes, `probe_tu.py`, `audit_tu_flags.py`, `audit_relocation_topology.py`, and `docs/current/tu-structure.md`. |
| Durable attempts | `docs/current/blockers.json`, archived bounded attempts managed by `check_candidate.py`, historical wave recipes and `docs/history/`, checked-in probes; transient `build/` receipts are weaker than frozen records. |
| Solved hard cases | MUSIC native compiler route/fixup order; inline-ASM route explaining GAME/BOARD/STARTUP TUs; genuine ASM provenance and final runtime closure. |
| Negative experiments | Byte-negation variants, incompatible header views, noncontiguous DATA, `-B`-intolerant anchors, pseudo-register FLAGS overhead; all scoped below. |
| Remaining blockers | No open historical closure blocker in freeze frontier. Ambiguous byte-neutral grouping and some names intentionally remain uncertain; isolated `probe_module.py` cannot bind two runtime/library cases, covered by full acceptance. |
| Agent workflow | CHEAP/MEDIUM/SUPERVISOR card routing, automated diagnostic rules and failure memory; reviewed artifacts do not provide a controlled model-quality cohort. |

## High-value trajectories

**MUSIC: exact code was insufficient.** Earlier arithmetic reconstruction matched
body bytes through an ASM route but needed FIXUPP ordering accommodation. The
strict executable exposed descending historical relocation order. The audit
distinguished native Turbo C's descending order from ordinary ascending TASM
emission. Whole pure-C MUSIC compilation, including structured `fdf98`, restored
the order naturally (commit `562905916f6aefe007a94cc605b2405610247c44`), followed
by full byte-identical acceptance. The reusable result is a topology diagnostic;
the descending/ascending rule remains this toolchain's fact. Frozen final plan
and `src/MUSIC.C` override stale comments about descending-ORG ASM.

**GAME and neighboring TUs: local flags became source-context evidence.**
TURNLOOP/LVLDRV needed `-B` although their own source lacked ASM. Inline `asm sti`
in BOOTSEED explains the unit-wide compiler-to-assembler restart. Converting it
to the intrinsic breaks the neighbors. Whole-TU probing promoted GAME.C;
BOARD.C and STARTUP.C use independently recorded instances of the same route.
HITTEST's `-B` intolerance and incompatible `a74a2` declaration views bound the
inference. Byte-neutral extensions remain merely compatible, not uniquely proven.

**BOARD negation: useful failure establishes an ASM boundary.** 28 standalone
spellings plus eight in-context probes produced byte-width negation or extra
extension/spill work. The target word negation relies on AH already being zero
from earlier code. The frontier retains a small inline-ASM fragment with compiler
evidence. This bounded failure supports the retained fragment in this case; it
does not prove no conceivable Turbo C source could emit those bytes.

**Final closure: remove the construction accommodations.** The intermediate
exact structural link proved the historical linker could produce the whole
image, while still using adapters. Subsequent source DATA/BSS ownership,
natural publics, whole modules and native MUSIC compilation eliminated them.
The final freeze couples fresh acceptance to a complete construction fingerprint
and invalidates old success before any new build can fail. Exact executable
construction and provenance/readability audits were both required for the freeze.

## Sources

Machine-readable records and SHA-256 manifests are in `records.json`. All source
paths there refer to the frozen commit unless an explicit historical commit is
given. Relevant source implementations were inspected, not merely their names.
No upstream scripts, original source, oracle bytes, assets or historical tools
were copied. No top-level source-tool license was found in the inventory;
reference rather than extraction is the decision for every Empires script here.
