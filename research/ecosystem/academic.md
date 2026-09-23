# Search, uncertainty and language-aware reconstruction: actionable prior art

Checked 2026-09-23. Paper descriptions are **AUTHOR CLAIM**, not reproduced
benchmarks. Source observations are **EXTERNAL IMPLEMENTATION FACT**. Proposed
applications are **INFERENCE**. [academic.json](academic.json) records scope,
versions, availability and reuse decisions. No paper's aggregate result is a
forecast for MSC/Turbo C game reconstruction.

## Echo: direct overlap, artifact not verified

[Echo v1, 2026-09-16](https://arxiv.org/html/2609.18706v1) describes learned C
generation plus compiler/configuration search, parallel sampling, a top-k
candidate pool, rule mutation, assembly-diff-conditioned neural refinement and
optional reasoning-model refinement. Its matching criterion normalizes assembly
addresses/names; it is not raw executable, relocation-order or TU-layout equality.
The experiments use x86 GCC/LLVM targets; the configuration space spans GCC 3–16
and Clang 7–21. The paper reports improved matching, but these are author results.
Its Open Science section links a literal `anonymous.4open.science/xxxx`
placeholder; this inspection could not verify an executable artifact, checkpoint
set or implementation license. Treat it as architectural prior art, not an
available dependency. Candidate diversity, source novelty and top-k retention
do not establish compiler-output clustering or calibrated source probabilities.

**Decision:** learn the separation of proposal, refinement and configuration
search. The broad compiler-forward-model plus AI-search idea is already described;
local proof-preserving causal feedback remains a narrower engineering question.

## BED: byte-equivalent evolution predates LLM agents

[Schulte et al., BED, 2018, full paper](https://www.cs.unm.edu/~eschulte/data/bed-full.pdf)
uses known compiler/flags, human-source excerpts, mutation/crossover, recompilation
and disassembly similarity. Mismatch regions guide fragment retrieval;
instruction-wise lexicase selection preserves candidates useful on different
regions. Delta debugging reduces accumulated source bloat. The reported
19-program experiment reaches byte equivalence in 4 cases without decompiler
seeds and 10 with them, combining optimized/unoptimized runs. Limitations include
many evaluations, database quality and no evaluated struct-declaration recovery.
This is concrete prior art for population search against a compiler oracle,
not evidence of turnkey historical game/TU recovery.

The [SEL manual](https://grammatech.github.io/sel/Introduction.html) identifies BED
as an application and documents ancestry, adaptive mutation and multi-objective
selection. The inspected [SEL tree](https://github.com/GrammaTech/sel/tree/6916d5d31385ed15f3f722b653aab77e715cb1b1)
contains generic evolution infrastructure, but this pass found no named BED
runner to reproduce the paper. Its [license](https://github.com/GrammaTech/sel/blob/6916d5d31385ed15f3f722b653aab77e715cb1b1/LICENSE)
is GPL-3.0-or-later. Learn diversity-preserving selection; do not import a large
Lisp/Clang stack without a demonstrated advantage.

## PyLingual: uncertainty can drive a real decompiler

Inspected commit `f001a75992316500ef1b3e37cf0a239a62182ef0`, GPL-3.0.
This Python bytecode system is useful architectural evidence rather than a
native-C component. Its [decompiler](https://github.com/syssec-utd/pylingual/blob/f001a75992316500ef1b3e37cf0a239a62182ef0/pylingual/decompiler.py#L379-L432)
tries alternative segmentation predictions when a reconstructed code object
fails compilation or verification. It retranslates affected statements,
reconstructs control flow, compiles and checks, then rolls back failed choices.
The [search strategy](https://github.com/syssec-utd/pylingual/blob/f001a75992316500ef1b3e37cf0a239a62182ef0/pylingual/segmentation/segmentation_search_strategies.py#L108-L166)
orders boundary changes using model uncertainty; the caller uses depth two and
a configurable top-k budget. Thus practical multi-hypothesis decompilation
exists, although these are segmentation alternatives rather than calibrated
probabilities over historical C constructs.

The [verifier](https://github.com/syssec-utd/pylingual/blob/f001a75992316500ef1b3e37cf0a239a62182ef0/pylingual/equivalence_check.py)
compares normalized instruction/code-object and CFG evidence, including exception
tables; preprocessing removes or changes selected bytecode details. It is not
literal `.pyc` identity. The [documented interface](https://github.com/syssec-utd/pylingual/blob/f001a75992316500ef1b3e37cf0a239a62182ef0/README.md)
uses the target CPython version, supports 3.6 onward and can trust available
line-table segmentation. There is no x86 ABI, OMF fixup, native linker or TU
equivalent-output grouping in this path. Learn uncertainty-localized retries
and deterministic verification; do not port its bytecode implementation.

## Closely related methods with different objectives

- [AutoDecompiler v1, 2026-06-15](https://arxiv.org/abs/2606.16162v1) trains
  multi-turn refinement using compilation and execution feedback. The stated
  outcome is behavioral re-executability, not historical artifact equality.
  Relevant lesson: feedback interpretation can be trained, but recompilability
  is an insufficient acceptance metric. Implementation and license were not
  audited here; reference only.
- [STOKE](https://github.com/StanfordPL/stoke) searches x86-64 instruction programs
  stochastically and separates cost from equivalence verification. Its authors
  describe it as a research prototype rather than a general-purpose tool;
  code is Apache-2.0. It synthesizes/optimizes assembly, not historical C through
  MSC/Turbo C. Learn stochastic exploration and independent validation; do not
  deploy it as our source generator.
- [Szalinski, PLDI 2020](https://www.mwillsey.com/papers/pldi-szalinski) uses
  equality saturation and inverse transformations to recover structured CAD
  programs. It demonstrates retaining many equivalent representations, not a
  native matching decompiler. Semantic equivalence classes and identical
  compiler-output classes answer different questions. Porting an e-graph adds
  rewrite-rule and extraction-cost obligations; no current local need justifies
  an integration. Implementation/license not audited.
- [Decompile-Diverge v1, 2026-09-04](https://arxiv.org/html/2609.05370v1)
  reports behavioral divergence in outputs that compile and pass supplied tests.
  Its fuzzing-based comparison supports retaining unresolved evidence and an
  independent checker instead of trusting plausible LLM repairs. Its metric
  is behavioral, not our artifact proof; benchmark results were not reproduced.

## Search boundary and interpretation

The focused searches covered matching/recompilable decompilation, inverse
compilation, source recovery using compiler feedback, neural decompilation,
stochastic superoptimization, equality saturation, C synthesis from assembly,
compiler provenance and multiple source hypotheses. Followed references led to
BED/SEL, Echo, PyLingual and the methods above. Conventional readability-oriented
surveys were excluded. No practical system was established in this pass that
jointly provides calibrated historical C hypotheses, segmented x86 type/ABI
reasoning, full TU/compiler-pass search and ordered OMF/NE/MZ proof. That is a
bounded search result, not a universal nonexistence or novelty claim.

**INFERENCE.** Maintain ranked hypotheses with evidence and falsifiers. Model
token probabilities, segmentation confidence, beam scores and percentages of
matching instructions are not interchangeable probabilities that the original
author wrote a construct. Do not publish invented 50/30/20 historical-source
probabilities. Group by output only within a fixed context/proof scope, while
retaining source alternatives that might separate in another TU. Preserve
diversity across mechanism classes, not just scalar best score.
