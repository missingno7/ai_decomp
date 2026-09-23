# m2c and decomp-permuter: matching-oriented upstream study

**External snapshot:** 2026-09-23. Read-only upstream checkouts inspected:
[m2c 708d2d2](https://github.com/matt-kempster/m2c/tree/708d2d2cb2698f091a92492b328f73b24209f72d) and
[decomp-permuter 059609d](https://github.com/simonlindholm/decomp-permuter/tree/059609d4aec73eb0650726772954e1ad575825f8).
No upstream program was executed or vendored into the tracked workspace.
Ignored public-source checkouts were used only for inspection.

## Decision

m2c is a strong matching-aware source-draft generator. It is not an inverse-compilation search loop: it deterministically turns GNU-as text plus C context into C; it neither compiles candidate source nor scores an oracle. Decomp-permuter is a strong mechanical local exploration layer: it mutates or enumerates variants of supplied C, compiles every uncached candidate through a project command, and scores resulting disassembly. Neither is a full historical matching-decompilation system.

Do not vendor either. m2c is GPL-3.0-only. Decomp-permuter is MIT, but its built-in scoring normalizes object disassembly and cannot replace the SimAnt OMF/fixup/private-data proof or Stunts' context-bound hybrid acceptance. Its mechanics could justify an isolated, license-reviewed compatible experiment; it must remain behind project acceptance adapters.

## Capability matrix

| Dimension | m2c | decomp-permuter | Relevance |
|---|---|---|---|
| Purpose | Deterministic matching-oriented GNU-as assembly-to-C decompiler. | Existing-C permutation, compile and normalized-disassembly ranking. | Initial prior versus late local search. |
| Architectures | MIPS/MIPSEL/MIPSEE, PPC, ARM/GBA, SH2/SH4 in target dispatcher. | Docs: MIPS, PPC, ARM32. Code also has ELF EM_386 x86 settings. | Neither handles 16-bit segmented x86/OMF. x86 scorer plumbing is not MSC/Turbo C support. |
| Languages/formats | C, partial C++; GNU as input; optional asm data/rodata/bss and preprocessed C context. No binary/object input. | C AST; limited C++ textual escape hatches. Requires base.c, target.o, compile.sh, TOML. Built-in reader requires ELF. | OMF/NE/MZ, COFF, linker topology require adapters. |
| Compiler knowledge | Target labels IDO/GCC/MWCC/SHC; per-architecture ABI and patterns encode idioms; never invokes compiler. | Arbitrary compiler via compile.sh; ido/mwcc/gcc only choose transformation weights. | Neither models MSC 5/7 or Turbo C. |
| Compilable output / loop | valid-syntax is best-effort C with macros; no recompile, retries, score or candidates. | Emits C candidates and compiles every uncached source; finite enumeration or indefinite random retries. | Permuter already solves mechanical compiler exercise. |
| Oracle feedback | CFG/debug/source only. | Mnemonic alignment with stack/branch/register/reorder/insertion/deletion penalties; zero is equality of normalized rendered instruction text. | Useful diagnostic, not strict proof. |
| Relocs/data/layout | Symbolic asm/data can inform declarations/initializers; no relocation-table or link proof. | Rewrites printed instruction using objdump relocation text; no raw relocation type/count/order, data, private contribution, or layout comparison. | Empires/SimAnt obligations stay outside both. |
| TU/context | Parses declaration context and modest cross-function output/type narrowing; no build/link/TU model. | One target function; compiler command can use project headers but search has no TU state. | Cannot model Icy predecessor/pass or Empires route/topology. |
| Batch/dedup/history | Multiple functions only; no candidate batch/dedup. | Multiprocessing and optional permuter@home; source-score cache (max 100k), selected normalized-objdump hash dedup; selected outputs retain source/score/source diff. | Keep ai_decomp full context-aware response history. |
| AI/automation | No AI; automatic analysis under supplied context. | No AI; automatic enumeration/randomization, human supplies axes/reviews. | AI can choose uncertainty axes and interpret structured evidence. |
| License/reuse | GPL-3.0-only. | MIT. | Learn from m2c; consider isolated permuter adapter only. |

## m2c: architecture, inference, and x86 boundary

**EXTERNAL IMPLEMENTATION FACT.** run() selects an architecture, parses one or more GNU-as files into AsmData, parses/caches C context into a type map, narrows call outputs, builds a flow graph, performs preliminary translation passes for type inference, and prints type/global/function C
([main.py:123-317](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/main.py#L123-L317)).
There is no compiler execution in this pipeline.

Its CFG stage builds blocks/nodes, duplicates premature returns, computes graph relations/input uses, and invokes architecture processing/IR simplification
([flow_graph.py:1746-1783](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/flow_graph.py#L1746-L1783)).
Architecture modules supply instruction semantics and compiler/architecture patterns, for example
[MIPS](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/arch_mips.py#L770),
[PPC](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/arch_ppc.py#L701), and
[ARM](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/arch_arm.py#L1028).

Types derive from supplied declarations plus inferred stack/access evidence: build_typemap() parses the supplied context
([c_types.py:827](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/c_types.py#L827)).
stack-structs deliberately offers a human-editable stack name/type round-trip
([main.py:429-434](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/main.py#L429-L434)).
The code notes type output may need ABI/compiler dependence
([types.py:1110](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/types.py#L1110));
output type/source is therefore a hypothesis, not proof of historical spelling.

### What the source reconstruction actually does

The internal type representation is a union-find constraint object, rather than
a one-shot width guess. Its unifier intersects possible kind, signedness and
size, recursively unifies compatible pointer/function targets, rejects
incompatible arrays/structs/enums and prevents a newly inferred recursive
struct ([types.py:204-306](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/types.py#L204-L306)).
Translation seeds the function type from context or an unknown function,
uses the target ABI for argument locations, propagates register values along
the dominator tree, then infers a return register and unifies parameter types
with observed incoming argument values
([translate.py:4833-4921](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/translate.py#L4833-L4921)).
That is useful constraint accumulation, not recovery of declaration order or
historical lexical lifetime.

Memory accesses furnish another constraint source. An address access asks the
pointed-to type for an offset and access size; an unknown struct can add a
non-overlapping unknown field at that offset, while known fields win and
overlap pruning deliberately degrades questionable inferred fields
([types.py:437-613](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/types.py#L437-L613),
[types.py:1354-1462](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/types.py#L1354-L1462)).
After block translation, a late pass uses dereference-offset maps to turn an
unambiguous offset-zero access into a pointer type
([translate.py:4239-4261](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/translate.py#L4239-L4261)).
These mechanisms explain both why m2c benefits from supplied headers and why
it should not be treated as a source-of-truth type oracle.

Control structuring is also concrete, not merely pretty-printing. The CFG
classifies each terminating block as return, direct/conditional branch or
register-indirect switch and resolves a jump table from symbolic asm data
([flow_graph.py:928-1100](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/flow_graph.py#L928-L1100)).
It computes dominators, postdominators and natural-loop backedges
([flow_graph.py:1232-1360](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/flow_graph.py#L1232-L1360)).
The emitter then collapses reducible conditional DAGs through four
AND/OR/negation topologies into an if/else condition
([if_statements.py:629-766](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/if_statements.py#L629-L766)),
recognises guarded/irregular compare-tree plus jump-table switches, detects
natural-loop backedges as do/while candidates, and falls back to labeled gotos
when the graph is irreducible or structuring fails
([if_statements.py:769-975](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/if_statements.py#L769-L975),
[if_statements.py:1166-1428](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/if_statements.py#L1166-L1428)).

The compiler knowledge is specific and inspectable. Examples include a MIPS
IDO unrolled-copy recogniser which converts alignment- and ISA-specific load/
store loops into a fictive memcpy operation
([arch_mips.py:544-770](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/arch_mips.py#L544-L770)),
MIPS GCC sqrt-call patterns in the target pattern list
([arch_mips.py:1349-1372](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/arch_mips.py#L1349-L1372)),
and a PPC CodeWarrior struct-copy recogniser for a load/load/store/store
sequence documented for GameCube/Wii MW versions
([arch_ppc.py:490-566](https://github.com/matt-kempster/m2c/blob/708d2d2cb2698f091a92492b328f73b24209f72d/m2c/arch_ppc.py#L490-L566)).
This is exactly the boundary to learn from: compiler idioms become auditable,
testable rewrite rules. They do not transfer to 16-bit MSC simply because they
have the same high-level construct.

The reusable design is the separation among parsed asm/data, typed symbolic instruction IR, CFG, target class, iterative inference and source emission. Architecture-bound work is parser/decoder, calling ABI, stack semantics, endianness, branch/delay-slot rules, jump table and compiler patterns. A realistic historical x86 port needs 16/32-bit x86 parsing, far/near and segment-aware ABIs, flags/partial registers, x87/runtime patterns, OMF symbols/fixups, and MSC/Turbo C patterns. Even then it would still lack compiler-oracle feedback, TU/link proof and multi-hypothesis search.

**INFERENCE.** For our compiler set, an LLM combined with deterministic x86/OMF evidence is likely the more economical source prior than a wholesale m2c port. That requires a measured trial; it is not a claim that m2c ideas are irrelevant.

## decomp-permuter: what it already solves

### Variant generation and search

**EXTERNAL IMPLEMENTATION FACT.** Manual PERM macros encode finite alternatives: general choices, variables, once-only choices, line swaps, integers, ignored/pretended text, and randomization regions
([parse.py:79-94](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/perm/parse.py#L79-L94)).
Finite seed spaces are sampled in shuffled order; random regions repeat indefinitely
([eval.py:11-33](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/perm/eval.py#L11-L33)).

The weighted AST passes include temporaries/expression expansion, internal/external/function type variants, statement/declaration reorder, casts, conditions/inequalities, algebraic/assignment rewrites, blocks/empty statements, inlining, aliases and declaration padding
([randomizer.py:2592-2630](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/randomizer.py#L2592-L2630)).
Compiler-specific knowledge is weights, not a learned compiler model
([default_weights.toml](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/default_weights.toml)).
Most passes aim at semantic preservation, but no formal guarantee exists: types, order and arithmetic are intentionally changed, and reorder checks are syntactic/limited
([randomizer.py:1366-1511](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/randomizer.py#L1366-L1511)).
Treat every candidate as an experiment.

This is stochastic local search, not directed beam search. Default keep probability 0.6 sometimes mutates the preceding candidate; otherwise it restarts. It has no mechanism database, learned proposal distribution, or structured compiler-gradient interpreter
([permuter.py:168-222](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/permuter.py#L168-L222)).
The upstream README explicitly cautions that randomization can find nonsensical accidental register-allocation improvements
([README.md:94-116](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/README.md#L94-L116)).

### Compile loop, scoring, and proof limits

The compiler wrapper writes temporary C and calls bash compile.sh input.c -o output.o
([compiler.py:9-61](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/compiler.py#L9-L61)).
This is the important reusable seam. But the built-in scorer selects architecture from an ELF header
([objdump.py:285-300](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/objdump.py#L285-L300));
raw OMF cannot enter it unchanged.

The scorer aligns mnemonics (difflib or Levenshtein) and weights stack/branch difference 1, operand/register 5, reordering 60, insertion/deletion 100
([scorer.py:11-19](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/scorer.py#L11-L19),
[scorer.py:57-326](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/scorer.py#L57-L326)).
It hashes normalized rendered objdump text. Its reader consumes a relocation line only to modify the prior printed instruction and set has_symbol
([objdump.py:630-686](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/objdump.py#L630-L686)).
Thus score zero is emphatically not raw object / fixup / data / link equality.

-j starts multiprocessing workers and -J enables permuter@home
([main.py:416-592](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/main.py#L416-L592)).
It caches source scores up to 100,000 and deduplicates selected non-zero outputs by normalized objdump hash; zero-score variants deliberately remain distinct
([permuter.py:203-258](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/permuter.py#L203-L258)).
Only selected candidates persist as source, score and source diff
([main.py:118-143](https://github.com/simonlindholm/decomp-permuter/blob/059609d4aec73eb0650726772954e1ad575825f8/src/main.py#L118-L143));
it does not retain a full trajectory of failures.

## Comparison with Stunts and SimAnt

Decomp-permuter already solves candidate materialisation, real-compiler exercise, finite combination enumeration, stochastic mutation, local/distributed scheduling, scalar filtering and one coarse output equivalence class. It could be a mechanical layer when an agent provides evidence-bounded axes.

It does not supply the demonstrated local requirements: profile/TU-bound effective identities; candidate-versus-parent and candidate-versus-oracle deltas across code and fixups; complete failed-experiment history; a mechanism-diverse beam; escalation from source spelling to ABI/TU/context; or strict independent acceptance. SimAnt raw OMF/fixup/private contribution distinctions and Stunts batch-versus-adaptive evidence therefore must remain first-class adapter outputs.

**Reuse decision:** learn from m2c analysis architecture. For decomp-permuter, reuse explicit finite variants, seed provenance, worker scheduling and optional normalized asm diagnostics only behind a new adapter. Do not deploy it unmodified for OMF/NE, historical link topology, or unguided source search. No local integration is implemented by this study.

## Provenance

All external links are immutable GitHub permalinks at inspected commits. Local comparisons rely only on pre-existing research/simantw/dossier.md and research/stunts/dossier.md; sibling projects were not refreshed, built, or modified.
