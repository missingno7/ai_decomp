# Capability matrix: requirements and actual scope

Snapshot 2026-09-23. **D** = demonstrated in the cited local evidence;
**R** = required by its acceptance/workflow; **P** = partial or contextual;
**—** = not established by this study. An empty capability is not a claim
that the task is impossible. External “yes” never inherits a local proof scope.
The same row identifiers join the two tables. Sources:
[local evidence and manifest](../research/ecosystem/local-requirements.md),
[original project dossiers](comparison.md), and the pinned
[external studies](ecosystem.md#supporting-studies-and-reuse-constraints).

## Local requirements

| ID / capability | Empires | Stunts | SimAnt | Icy Tower |
|---|---|---|---|---|
| C1 Semantic C reconstruction | D, plus legitimate ASM | D | D | D |
| C2 Real compiler feedback loop | D, Turbo C2 | D, MSC5.x | D, MSC7 Win16 | D, TDM GCC4.4.1 |
| C3 Candidate batches | D, source/TU probes | D, controlled/adaptive cohort | D, bounded batches | D, source/context probes |
| C4 Source permutation | D, bounded hand-designed forms | D, declared axes | D, declaration/expression axes | D, source and scope overlays |
| C5 Structured diagnostic diff | D, module/link audits | D, islands/families/parent deltas | D, codegen and semantic fixups | D, instruction/CU/pass deltas |
| C6 Relocation-aware strict proof | D, ordered MZ relocations | R/D, OMF binding/image | R/D, OMF/NE member | R/D, COFF/PE refs |
| C7 Data/layout strict proof | D, full image/BSS ownership | R, hybrid acceptance | R/D, private contributions | R/D, static/BSS/ownership |
| C8 TU awareness | D, membership and route | R/P, bounded context escalation | D, selector/data unit assembly | D, whole-CU probes |
| C9 Version/profile awareness | D, hashes/flags/route | D, pinned production vs research profiles | D, assigned object profile | D, compiler/flags locked |
| C10 Historical compiler execution | D | D | D | D |
| C11 Cross-function effects | D, inline ASM changes neighbors | P, context an escalation axis | D, shared pool/data order | D, predecessor effects/protected peers |
| C12 Debug evidence | — in closure studied | — in cohort studied | D, MAPSYM identity (not full source types) | D, DWARF types/scope/order |
| C13 Project-specific compiler rules | D, scoped route/reloc observations | D, tested rules and failures | D, scoped declaration/ABI lessons | D, scope/TU/pass observations |
| C14 AI orchestration | D, archived agent/factory process | D, measured supervisor/model cohort | D, recovery factory | D, agent/probe workflow |
| C15 Effective-output classes | P, preserve probe artifacts | D, context-bound classes | D, raw OMF classes | D, normalized code/reloc identity |
| C16 Independent acceptance | D, frozen full closure | R/D, fresh hybrid receipts | R/D, fresh strict member receipts | R/D, scope ladder/preservation |

These columns are not maturity rankings. Empires has frozen closure while the
others retain active blockers; the evidence establishes different scopes.
“Project-specific rules” means retained observed mechanisms, not a trained model.

## External support against the same requirements

Abbreviations: **m2c**, **perm** = decomp-permuter, **dm** = decomp.me,
**asm** = asm-differ, **obj** = objdiff, **rec** = reccmp, **Miz** = Mizuchi.
“Delegated” means a supplied build/context script may implement it; the tool
does not independently model or prove it.

| ID | m2c | perm | dm | asm | obj | rec | Miz |
|---|---|---|---|---|---|---|---|
| C1 | Matching-aware C | Needs seed C | Editor + m2c | — | — | — | m2c + LLM |
| C2 | — | Yes | Yes | Build/watch | Build/watch | Already-built images | Yes |
| C3 | Multiple functions, not hypotheses | Finite + stochastic workers | Scratch/fork, no search | — | — | Report aggregation only | Sequential AI; background perm |
| C4 | No search | Rich AST/macros | Human edits | — | — | — | AI and perm |
| C5 | Analysis, no oracle | Weighted asm score | asm rows/three-way | Categories/three-way | Typed code/data/reloc rows | Image/stack/data reports | Text rows + counts |
| C6 | Symbolic asm only | Normalized reloc text | Platform reloc text | Platform reloc text | Object relocation policy | Image reloc support; relaxed effective match | No separate strict gate |
| C7 | Data inference only | — | .text-focused | Display-limited | Sections/data/BSS; not final link proof | Data/vtable/layout diagnostics | — |
| C8 | Declaration context | Delegated | Prepended source context | Delegated | Builds whole objects; delegated | Source/PDB entities | Header-like context |
| C9 | Compiler-family idioms | Family weights + script | Compiler IDs/flags | Build config | Build config | MSVC evidence assumptions | Compiler script/target |
| C10 | Does not execute | Script; ELF scorer | Several historical recipes | Delegated | Delegated | Delegated | Project script; ARM/MIPS/PPC adapters |
| C11 | Limited shared types | Not search state | User context only | — | Object symbols | PDB/entity matching | Prompt callers/examples |
| C12 | C context, not debug proof | Not central | Wrapper-specific line support | Objdump source/lines | DWARF/line support | PDB/CodeView central | Context-script responsibility |
| C13 | Static idiom rules | Static weights | Execution recipes | Static diff rules | Static format/arch rules | Static MSVC rules | No durable mechanism learning |
| C14 | — | — | — in inspected path | — | — | — | Claude agent |
| C15 | — | Selected normalized text hashes | Input cache only | — | — | — | Source-string dedup only |
| C16 | — | External required | Zero score/override | Diagnostic only | External required | Effective vs exact differs | Optional post-match script |

For C6/C7, none is established as an interchangeable implementation of any
local full acceptance gate. Objdiff is relocation-aware; this is stronger than
assembly-only comparison but weaker than claiming complete historical link
proof. Reccmp has executable-format readers; that does not imply a 16-bit OMF
object path or automatic historical-x86 source recovery. See
[diff implementation details](../research/ecosystem/diff-tools.md).
Objdiff's source-line support includes DWARF 1.1 and optional DWARF 2+ parsing;
it does not establish lexical-scope or ownership proof. See its pinned
[line-info reader](https://github.com/encounter/objdiff/blob/fba10a617154f19b3fc25c8817dc81f81d8489b5/objdiff-core/src/obj/read.rs#L743-L760).

## What “compiler gradient” can already contain

| Feedback dimension | Existing external implementation | Local addition that remains necessary |
|---|---|---|
| Aligned instruction differences | asm-differ, objdiff, reccmp, dm, Miz | Keep raw offset/decoder provenance and alignment uncertainty |
| Register-only differences | asm/perm penalties; obj argument mismatch; rec register-swap analysis | Distinguish correlated allocation families from isolated edits |
| Stack offsets | asm/perm scoring, obj operands, rec stack analysis | Stunts BP-home families; SimAnt exact segment/frame evidence |
| Branch/CFG correspondence | Branch target mapping/visualization in asm/obj; m2c reconstructs CFG | Correspondence is not a full semantic CFG equivalence proof; retain Icy path/pass evidence |
| Relocations/fixups | obj structured target/type/addend; OMF utility decoding; platform text normalizers | Ordered raw OMF/MZ and NE selector/offset obligations; binding authority |
| Data, symbols and size | obj sections/symbols/data/BSS; rec data/vtables/layout | Private contribution ownership and final linker extent |
| Score and previous candidate | asm/dm three-way; perm score/history of selected results | Explicit parent hash, changed axes, prediction/falsifier and residual deltas |
| Source-line correlation | Toolchain/debug-dependent asm/obj/rec support | DWARF lexical meaning and compiler pass evidence remain separate |
| History / deduplication | dm forks, Miz attempt reports, perm selected outputs | Full failed trajectories; context-compatible output classes; scoped negative lessons |

No single scalar should combine these into a proof. A local improvement can
regress another dimension or reveal a more useful causal mechanism despite a
worse score. A beam should retain such explained alternatives. The purpose of
the common response is to expose those tradeoffs compactly, not erase them.
