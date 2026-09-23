# Which project is the useful precedent?

This comparison is a 2026-09-23 research snapshot, not a ranking. Every table
entry is a **PROJECT FACT** or an explicitly qualified absence of evidence.
Full provenance and current/frozen distinctions are in the four dossiers:
[Empires](../research/empires/dossier.md), [Stunts](../research/stunts/dossier.md),
[SimAnt](../research/simantw/dossier.md), [Icy Tower](../research/icytower/dossier.md).

| Dimension | Empires | Stunts | SimAnt | Icy Tower |
|---|---|---|---|---|
| Compiler | Hash-pinned Turbo C 2.0, TASM 1.0, TLINK 2.0 | Production MSC 5.1; 5.0/5.1 profiles studied; unique historical identity not yet proved | MSC 7.00, LINK 5.30, object/unit profiles | Locked TDM GCC 4.4.1 |
| Platform | DOS real mode / 8086-compatible | DOS real mode / 16-bit medium model | Win16 / x86 large model | Win32 / i386 |
| Formats | OMF → MZ | OMF → MZ/load image | OMF → NE | COFF → PE |
| Debug/source evidence | Publics, route signatures, relocations, private DATA; no DWARF/SYM authority in reviewed closure | Recovery cards, object/disassembly evidence; no comparably rich source-debug basis in reviewed workflow | MAPSYM/.SYM identifiers plus code/data/selector topology | Rich original DWARF types, locals, lexical scopes, declaration lines, locations; COFF linkage |
| Acceptance scope | Whole exact EXE, 106 ordered relocations, fresh one-TLINK construction | Strict hybrid full image with untouched oracle-backed remainder; per-candidate binding proof | Complete claimed member: extent/publics/bytes/semantic fixups/private contributions | Resolved function bytes; object/CU/layout/PE/full-file levels separate |
| Recovery snapshot | Frozen historical closure; 71 modules, no structural adapters | 408 matching C bytes, 11 active C functions; large raw remainder | 516 matched, 109 ready, 438 blocked, 2 structural in live queue | 209 function matches; 35,299/116,113 game-function bytes; no whole-EXE closure claim |
| Startup/batching | Native DOS runner + research cache; uncached acceptance | Bounded preregistered research batches; one paired batching trial | Persistent isolated DOSBox-X service; 400-candidate local benchmark 50.53 s | Whole-CU overlay probes and effective-outcome grouping |
| Timing comparability | No common benchmark | Worker/compiler/supervisor costs must stay distinct | Service throughput is a local benchmark, not isolated process startup latency | No common benchmark |
| TU/layout evidence | Inline ASM route, ordered FIXUPPs, word alignment, private DATA and conflicting declarations | Early TU probes; current camera residue may require context, not proved cause | Selector pools, private DATA/BSS/CONST, profiles, scaffolded units | DWARF source order, predecessor context, lexical lifetime, natural emission offsets |
| Dominant blockers | None for frozen closure; some historical naming/grouping uncertainty remains | Source convergence, ABI/compiler feature/parser boundaries, limited useful feedback | Predominantly source-shape; smaller ABI/context/layout subgroups | Large incomplete bodies, lifetime/register/CFG/pass effects, context and ownership/layout |
| Mature precedent | Adapter-free historical closure and fresh acceptance | Measuring agent economics; mismatch families; candidate-vs-candidate evidence | Recovery factory, strict OMF/NE members, bounded variants, compiler service | DWARF-guided scope/order changes, compiler-pass diagnosis and neighbor preservation |

Use Empires when body bytes match but ordered link topology does not, or when
remaining ASM needs a provenance decision. Use SimAnt when a body needs an
object's selector/private-data context or a factory needs bounded attempt memory.
Use Icy Tower when historical debug evidence contradicts lexical scope/order or
an unchanged function responds to earlier definitions. Use Stunts when choosing
how to measure agent cost, batch independent hypotheses, or distinguish a
compiler effect from actual progress toward the oracle.

The counts above have different denominators and proof meanings. Never combine
them into a recovery percentage or use them to rank projects or models.

Stunts' live receipts require particular care: the re-inspected validation file
reports PASS/HYBRID_EXACT, while generated status still says
`NOT_CURRENTLY_VERIFIED`. The dossier retains both facts and the distinct
fingerprints; this workspace does not resolve that disagreement into a claim
that the latest dirty tree is freshly accepted.
