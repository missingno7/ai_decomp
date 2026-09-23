# Matching-decompilation ecosystem: decisions for ai_decomp

Research snapshot: **2026-09-23**. Seven core upstream tools were inspected
beyond their READMEs at pinned commits. Additional OMF and research approaches
were followed where they answered a local requirement. These are source studies,
not installation benchmarks. No external tool was integrated and no sibling
project was modified or built. The [catalog index](../catalog/ecosystem/index.json)
links machine-readable capabilities and provenance; the
[capability matrix](ecosystem-capabilities.md) separates local evidence from
external support.

## Decision report

1. **Strongest existing components:** m2c for matching-aware C drafts;
   decomp-permuter for mechanical local search; decomp.me for a collaborative
   compiler bench; objdiff for typed object/code/data feedback; asm-differ for
   lightweight assembly triage; reccmp for old-MSVC/PDB reconstruction;
   Mizuchi for automated function-level agent orchestration. They solve
   different layers, so there is no defensible universal winner.
2. **A practical language/compiler-aware matching decompiler already exists
   within a narrower scope.** m2c encodes language, ABI and compiler idioms;
   a configured matching workflow can combine it with a compiler and search.
   No inspected system supplies all four projects' historical-x86 source,
   ABI, TU, private-data, relocation and final-link proof obligations.
3. **m2c is a strong source prior, not the whole inverse problem.** Reuse its
   analysis architecture and algorithms conceptually. A segmented-x86 port is
   substantial work and would still need experimental search and proof adapters.
4. **Mizuchi is close to the broad proposed architecture.** It already combines
   m2c, a real compiler, objdiff, Claude retries and background permuter. It is
   function-scoped; output clustering, mechanism-diverse state and TU/pass/link
   investigation are outside its implemented pipeline.
5. **Do not reinvent decomp-permuter's mechanics:** explicit source choices,
   AST mutation, weighted sampling, compiler workers, distributed execution and
   selected normalized-output deduplication. Adapting it is plausible, but the
   ELF scorer and C parser are material obstacles for OMF and segmented C.
6. **Best feedback depends on evidence:** objdiff provides the richest reusable
   object interface for Icy's COFF/x86; asm-differ/decomp.me already expose
   register/stack/aligned and previous/current/target views. reccmp supplies
   useful MSVC/PDB and stack/layout diagnostics. None replaces local acceptance.
7. **The important missing shared capability is causal experiment state:**
   context-compatible output classes, parent/candidate/oracle deltas over all
   proof dimensions, retained failures, hypothesis diversity and explicit
   escalation beyond local source spelling. Several pieces already exist
   locally; this is a composition gap, not a claim of novel algorithms.
8. **Reuse selectively:** evaluate objdiff as an optional diagnostic provider;
   reuse permuter mechanics only after a scorer/parser feasibility test;
   borrow decomp.me compiler recipes and feedback design. OMF disassembly already
   exists in binutils-omf, so inspect compatibility before writing another one.
9. **Learn from first:** m2c's representation/inference, Mizuchi's constrained
   tool and replay reports, reccmp's MSVC evidence, and research population/
   uncertainty strategies. None currently warrants a production dependency.
10. **Build the small common contract:** extend existing experiment metadata
    into a compact compiler-response view with typed evidence references,
    scope-preserving clustering and an escalation state. Keep historical
    runners, format parsers and strict verifiers with their owning projects.
11. **The direction is useful, but the broad idea is established.** Prior art
    includes evolutionary byte-equivalent search and recent AI/compiler-feedback
    systems. The local requirement that remains especially demanding is jointly
    reasoning over segmented ABI, TU/compiler route, data and ordered relocation
    evidence without weakening acceptance. “Compiler gradient” should mean an
    observed discrete response, not a derivative or guaranteed descent path.
12. **Highest-leverage next prototype:** a read-only replay of one archived
    SimAnt cohort and one Stunts cohort through a compact response envelope,
    extending the existing outcome matrix. Reproduce native output groups and
    strict statuses, expose parent/oracle changes, and measure handoff size and
    duplicate-trial recognition. The [prototype specification](../docs/compiler-response-prototype.md)
    defines the experiment and stop conditions. No integration was warranted
    before this measurement.

## Semantic recovery and historical matching are different objectives

This is a conceptual distinction, not a claim that every conventional tool
discards all compiler information. Semantic decompilers can use compiler idioms,
types, calling conventions and CFG evidence very effectively. Their output
objective often permits transformations that preserve behavior but erase source
choices relevant to exact recompilation. Matching asks for a source/context
preimage under a particular compiler process. Many historical sources can share
one artifact; a strict match does not identify original names or byte-neutral
source uniquely.

| Evidence or choice | Readable semantic recovery may accept | Historical matching requirement demonstrated locally |
|---|---|---|
| Width, signedness, near/far representation | Equivalent explicit casts/operations after lifting | SimAnt selector/offset/operand lowering must agree with actual MSC7 ABI and bindings |
| Declaration order and lifetime | Rename/reorder locals if behavior is unchanged | SimAnt MagnifyMenu's local order changes stack-operand selection |
| Lexical static scope | Any equivalent storage arrangement | Icy DWARF plus BSS ownership and protected neighbors constrain scope |
| Source CFG | Simplify branches or merge equivalent tails | Icy `play` needs analysis of where the compiler merges a source distinction |
| Compiler/version/optimization | Source can compile under a modern environment | Project-pinned historical profile is part of the forward experiment |
| Function order / TU membership | Analyze functions independently | Icy predecessor effects and Empires whole-TU assembler route |
| Data/private state and relocations | Display symbolic references | SimAnt private contributions/fixups; Empires ordered relocations and one-link output |
| Compiler-pass state | Usually hidden in semantic IR | Icy pass evidence can explain convergence; mechanism remains compiler-scoped |

These examples are **PROJECT FACTS**, sourced in the
[fresh local extraction](../research/ecosystem/local-requirements.md) and its
hash manifest. They are not universal rules for every compiler. The full
[proof vocabulary](proof-models.md) keeps FUNCTION, MEMBER, TU and whole-image
claims separate.

## AI versus deterministic work

**INFERENCE from the studies and local evidence.** Deterministic tools should
own decoding, explicit CFG/symbol/fixup facts, compiler execution, receipts,
grouping and exact acceptance. An LLM is a useful proposer and experiment
selector: likely historical idioms, alternative types/CFG/lifetimes, interacting
residuals and the next uncertainty worth testing. It may suggest a binding or
TU explanation; the suggestion remains a hypothesis until deterministic evidence
and controlled compilation support it.

m2c demonstrates that useful source knowledge need not be learned. Mizuchi
demonstrates an operational LLM loop. The [research study](../research/ecosystem/academic.md)
documents population search and uncertainty-directed alternatives. None shows
that a model can certify a historical artifact by looking at it. Stunts' small
matched cohort supports investigating interaction cost; it does not establish
that model intelligence never matters. Batching should cover independent axes;
later batches still depend on earlier compiler responses.

## Where the proposed pipeline already exists

| Stage | Existing external capability | Existing local capability / missing common boundary |
|---|---|---|
| Binary/object facts | objdiff; asm-differ; reccmp; OMF utilities | Project parsers already own strict historical semantics |
| Language/source hypothesis | m2c; Mizuchi; research learned/source-population methods | Historical x86 agents and project-specific lessons |
| Compile candidate forms | permuter; decomp.me; Mizuchi | Authentic project services and profile receipts |
| Adaptive batch / search state | Permuter enumeration/random walks; research populations | SimAnt/Stunts bounded batches; no shared mechanism-diverse controller |
| Structured response | Rich objdiff records; asm-differ categories/three-way view | Local fixup/island/TU/pass facts lack a common model-facing envelope |
| Output equivalence classes | Permuter selected normalized-disassembly hashes | Raw/context-bound identities and existing ai_decomp matrix; preserve scope |
| Escalation and memory | User prompts/config, agent conversations | Local mechanism/negative catalogs and scoped source→ABI→TU/pass escalation |
| Acceptance | Tool-specific match conventions | Independent member/link/image verifiers; deliberately not centralized |

The proposed architecture is sensible if each adapter states what it observed,
what it normalized, what it did not check and which authority issued a strict
verdict. A source hash, a normalized instruction hash, a raw object hash and a
full executable receipt must never become one undifferentiated “match” field.

## Supporting studies and reuse constraints

- [m2c and decomp-permuter](../research/ecosystem/m2c-permuter.md): inference,
  transformations, search, scoring, deduplication and x86 feasibility.
- [decomp.me](../research/ecosystem/decomp-me.md): compiler recipes, DOS/OMF,
  context and three-way feedback; manual match override caveat.
- [Mizuchi](../research/ecosystem/mizuchi.md): actual pipeline, model, retries,
  feedback, limitations and author benchmark scope.
- [Diff/oracle tools](../research/ecosystem/diff-tools.md): objdiff, asm-differ,
  reccmp and binutils-omf, including normalized-match boundaries.
- [Research and multi-hypothesis approaches](../research/ecosystem/academic.md):
  actionable prior art, artifact availability and metric distinctions.
- [Local requirements](../research/ecosystem/local-requirements.md): current
  evidence with separate immutable/fingerprinted provenance.

Licenses are recorded at the inspected revision, not as permission to redistribute
historical compilers: m2c GPL-3.0-only; permuter/decomp.me/Mizuchi MIT; objdiff
MIT OR Apache-2.0; asm-differ Unlicense; reccmp AGPL-3.0; binutils-omf's inspected
OMF reader GPL-2.0-or-later (the fork's other components need their own review).
Mizuchi's optional m2c submodule retains m2c's GPL license despite the runner's MIT license.
Prefer separately invoked optional tools and original
metadata code. Review dependency and copied-code licenses before any integration;
this pass copied no upstream implementation into the tracked workspace.
