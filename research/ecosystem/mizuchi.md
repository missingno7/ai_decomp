# Mizuchi: implementation-facing ecosystem dossier

**Classification.** This is an external-tool study, not a new reconstruction
result.  It was inspected at upstream commit
[`25eaef4214574cc20f376878dbc1b8099e97164e`](https://github.com/macabeus/mizuchi/tree/25eaef4214574cc20f376878dbc1b8099e97164e)
on 2026-09-23.  The public source was cloned read-only to this workspace's
ignored `.research-cache/mizuchi`; it was neither installed nor run.  Claims
labelled **EXTERNAL IMPLEMENTATION FACT** refer to that pinned tree.  The
benchmark numbers are **AUTHOR CLAIMS**, separated below from what the code
actually accepts.

## What it is

Mizuchi is a MIT-licensed TypeScript pipeline runner for *function-at-a-time*
matching decompilation in existing game-decompilation projects.  It does
implement the important forward loop: start from assembly (optionally through
m2c), obtain C, compile through a project-supplied script, compare an object
symbol with objdiff, and give an Anthropic Claude Agent SDK session the next
compiler/diff response.  It is therefore much closer to this workspace's
proposed search architecture than a semantic-only decompiler.

Its concrete success condition is narrower: the Mizuchi `ObjdiffPlugin` finds
the named symbol in a temporary candidate object and target object and gets an
instruction-row difference count of zero.  It does not independently assert
whole-object identity, relocation/fixup equality, static-data placement,
translation-unit identity, linker topology, or executable equality.  The
example configuration even sets `functionRelocDiffs: 'none'` for GBA.  That
does not make the tool unsuitable; it makes a project-specific strict gate an
essential downstream authority for Empires, Stunts, SimAnt, and Icy Tower.

## Actual pipeline and feedback

For each prompt directory, the loader requires `prompt.md`, a function name,
a target-object path, and already-extracted GAS assembly.  `runPipelines`
processes those prompts sequentially.  A user shell `getContextScript` runs
once and its stdout becomes a temporary context header, prepended to every
candidate.  This supports useful declarations, macros, and a generated
per-function `m2ctx` context; it does not reconstruct or compile an original
whole translation unit.

When m2c is enabled, the programmatic stages are
`m2c → compiler → objdiff`, followed on mismatch by an optional
decomp-permuter stage.  The m2c output, and either its compile error or full
objdiff text, is appended to Claude's first prompt if that phase did not
match.  The AI phase is sequential per target: `Claude → compiler → objdiff`,
up to `maxRetries` (25 by the example configuration).  The manager preserves
the Claude session and inserts a follow-up containing either compiler errors
or the object-diff report.  It retains the fewest-instruction-mismatch code
only as a reminder when the latest attempt is worse.  A three-attempt stall
test merely asks Claude to try a fundamentally different source strategy; it
does not classify a mechanism, select an analysis level, or maintain a beam.

During one Claude run, its only custom MCP tool compiles a supplied candidate,
prints its recovered assembly, and returns a scalar instruction count plus
INSERTION/DELETION/REPLACEMENT/OPCODE_MISMATCH/ARGUMENT_MISMATCH rows.  The
tool limit defaults to seven per retry.  This is a useful compact
candidate-vs-oracle feedback loop, but it is a formatted assembly comparison:
the row-to-string conversion deliberately discards displayed source-line
segments.  The independent compiler and objdiff plugins repeat the evaluation
after Claude submits code.

The configured default model is `claude-sonnet-4-6`; `model` is configurable.
The soft-timeout follow-up can override model and effort.  The runner exposes
only Claude's read/search tools plus that compile/diff tool, so its normal
search phase cannot edit the target project.  It records token/timing data,
timeouts, refusal/fallback and detected model downgrade in run reports.

## m2c and permuter integration, as implemented

The inspected Mizuchi Git tree pins its submodules to m2c
`a21c1dcd7255b176c032bb932f521846e98d4372` and decomp-permuter
`ec2efeebb33e2b1de81e39fbf7cbe3cd97350472`. Those differ from the current
upstream revisions in the separate [m2c/permuter study](m2c-permuter.md).
This section audits Mizuchi's wrappers; it does not assert that every current
upstream feature exists in those older dependencies. See the pinned
[vendor tree](https://github.com/macabeus/mizuchi/tree/25eaef4214574cc20f376878dbc1b8099e97164e/vendor).

Mizuchi's m2c wrapper invokes the vendored upstream m2c Python program with
one temporary GAS function, `--globals none`, and optional context.  Its
mapping supports only ARM/GBA, MIPS/MIPSel, and PowerPC platform families; it
has no x86, MSC, Turbo C, OMF, NE, COFF/PE or DOS compiler adapter.  It adds
one ARM UAL preprocessing workaround.  Mizuchi reuses m2c as an initial
single hypothesis, not as a multi-hypothesis source generator.

Its decomp-permuter wrapper writes a temporary context header, the candidate
function, target object, compiler script and an `objdump` wrapper that slices
the named symbol.  It forwards a compiler-type weight (`gcc`, `ido`, `mwcc`,
or `base`) and user flags such as `-j`/`-J`; defaults are 1,000 iterations, two
minutes, and `-j 4`.  An improved source is recompiled for objdiff in the
programmatic phase.  In the AI phase, a background permuter starts only after
a non-final candidate is no worse than the best *instruction count* so far;
it deduplicates only identical submitted C strings.  It may run until
cancelled (configured as 24 hours), and its result ends the foreground search
only on a perfect permuter match.  Improvements are reported but deliberately
not fed back to Claude.  This is a meaningful concurrency design, but neither
source variants nor compiled outputs are clustered by effective identity.

Mizuchi's persistent `claude-cache.json` is a cache of conversation nodes
keyed by a hash of the system prompt and follow-up text.  It records/replays
LLM responses and sessions; it is not a cross-case compiler-mechanism memory,
candidate-output database, or output deduplicator.  JSON/HTML run reports do
retain attempts, plugin results, timing and chat evidence, which is useful
provenance for a future importer.

## Architecture and format boundary

The configuration names GBA, NDS, 3DS, N64, GameCube/Wii, PlayStation
families, Win32, Switch, Android x86, IRIX, Saturn and Dreamcast.  That is
target selection/configuration, not proof that every family has a working
m2c/permuter/compiler recipe.  The repository supplies concrete m2c mappings
only for ARM/MIPS/PowerPC and concrete permuter `nm`/`objdump` selections for
ARM, MIPS, PowerPC and SuperH, with a generic system-tool fallback.  Compilation
itself is an arbitrary Bash script template, so a carefully isolated historical
x86 compiler *could* be put behind it in principle, but the wrapper also
unconditionally invokes host `cpp -P` and Bash.  No historical x86/MSC/Turbo
C configuration or test fixture is shipped.

Mizuchi hands full objects to objdiff-wasm, but the pipeline's own acceptance
code extracts one named function and reduces it to display instruction rows.
Symbol lookup and a GNU ld map parser serve targeting/indexing.  It has no
Mizuchi-owned model of OMF/NE/MZ fixups, COFF/PE ownership, data sections,
relocation order, linker state, debug-location proof, declaration order, or
compiler-pass state.  Its context script can hand the model headers and m2c
context, while the Atlas prompt builder can add target/callee declarations,
types, nearby matched examples and embeddings; these are project-codebase
context, not historical TU reconstruction.

## Comparison with local requirements

| Requirement demonstrated locally | Mizuchi support | Consequence |
| --- | --- | --- |
| Semantic C prior and real forward compiler | Strong, function-scoped | Reuse the idea of a constrained agent/compiler loop; provide historical compiler adapters locally. |
| Candidate-vs-oracle response | Partial | It supplies aligned textual instruction deltas and a count, but lacks the Stunts parent-vs-candidate families and SimAnt semantic-fixup dimensions. |
| Adaptive batches / beam state / output classes | Absent | Its retries are one Claude conversation; background permuter uses one source-string set and a best scalar score.  SimAnt/Stunts/Icy Tower need context-aware effective-output identities. |
| Relocation and link topology (Empires; Stunts) | No pipeline proof | Preserve raw/object/link gates outside any Mizuchi-like exploration layer. |
| Member data, private contributions, fixups (SimAnt) | No pipeline proof | A zero instruction count cannot be accepted as an OMF/NE member match. |
| DWARF lexical scope, predecessor/TU/pass escalation (Icy Tower) | Prompt/context only | Retain project diagnostic adapters and an explicit escalation state. |
| Compiler version/profile fingerprint | User-script responsibility | Record exact compiler, flags, runner and context in shared experiment identity. |
| Cross-function and whole-TU reasoning | Index/prompt aids only | Use its map/index context as inspiration, never as evidence of TU reproduction. |
| Independent strict acceptance | Optional post-match build only | The integrator runs after a local match; it cannot replace the owning project's strict acceptance receipt. |

The overlap is real: both approaches treat the compiler as an oracle and make
retries first-class.  The material gap is a *proof-aware experimental state*:
Mizuchi feeds one candidate's raw instruction report to a conversational model;
the local projects need parent/candidate/oracle deltas across code, fixups,
data, context and acceptance, grouped by effective compiler output and able to
escalate from source spelling to ABI, TU, binding or compiler-pass analysis.
That is a scope distinction, not a novelty claim—Mizuchi itself documents
duplicate Claude submissions, weak stall action, and unused partial permuter
results as current limitations.

## Benchmark evidence and limits

The author reports an average 74% match rate over six runs of 60 selected
functions (30 each from Sonic Advance 3 and Animal Forest), using Claude
Sonnet 4.6, three repetitions, and a 12-attempt cap.  The study selected ten
functions from each internally inferred difficulty percentile.  It restricted
SA3 to Thumb because m2c/agbcc worked there and Animal Forest to functions
where `m2ctx.py` could generate valid context.  These constraints, the small
sample, function-only metric, aggressive timeouts, API degradation, and
project/architecture specificity prevent treating 74% as a historical-x86
recovery rate or an end-to-end executable-closure rate.  The author reports
that m2c alone matched four Animal Forest functions per run, permuter matched
three to four per run, and no programmatic-only SA3 functions; those are
benchmark observations, not universal tool capabilities.

The most directly useful author-identified limitations agree with the code:
only one agent tool, a generic stall message, duplicate source submissions,
background permuter partial improvements unused, and no parallel function
pipeline.  The source processes prompts sequentially, corroborating the last
one independently of the post.

## Reuse decision

**Do not integrate Mizuchi as a shared acceptance system or assume it supports
our historical x86 projects.**  Its direct code reuse is legally possible
under MIT, but would introduce Node, Claude Agent SDK, objdiff-wasm and its
upstream submodules; that is disproportionate before an adapter trial.

**Learn from / potentially adapt behind an isolated experiment adapter:**

- the phase separation (initial deterministic seed, agent retry, post-match
  integration);
- cached, replayable agent conversations with model/timing provenance;
- a constrained compile-and-diff agent tool and explicit per-attempt budgets;
- background mechanical search that can abort foreground work on an exact
  result; and
- portable reports containing every attempt and the cause of a stop.

The shared component worth building remains the locally motivated
adapter-neutral experiment state: compiler/context fingerprint; source and
effective-output identities; parent/candidate/oracle structured deltas;
negative evidence; strict-proof status; and a declared escalation reason.
It can expose a Mizuchi-like compact instruction report to an AI without
reducing Empires/Stunts/SimAnt/Icy Tower acceptance to that report.  The
highest-leverage future prototype is therefore a **model-facing compact
compiler-response envelope layered on the existing effective-output matrix**,
tested with one archived SimAnt or Stunts cohort before any Claude/Mizuchi
adapter is selected.

## Sources

| Role | Pinned primary source |
| --- | --- |
| Upstream identity, license and user-facing configuration | [repository README](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/README.md), [example configuration](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/mizuchi.example.yaml), [MIT license](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/LICENSE) |
| Pipeline stages, retry and sequential target processing | [plugin manager](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugin-manager.ts#L167-L408), [registration](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/commands/run.tsx#L802-L847), [prompt loop](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugin-manager.ts#L590-L744) |
| Agent prompt, feedback, model defaults and cache | [Claude runner](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/claude-runner/claude-runner-plugin.ts#L60-L110), [feedback/stall](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/claude-runner/claude-runner-plugin.ts#L167-L286), [MCP compile/diff tool](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/claude-runner/claude-runner-plugin.ts#L680-L809), [retry choice](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/claude-runner/claude-runner-plugin.ts#L1751-L1855) |
| Function-level comparison boundary | [objdiff plugin](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/objdiff/objdiff-plugin.ts#L57-L183), [display-row comparison](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/shared/objdiff.ts#L104-L200) |
| Context, m2c and permuter adapters | [context plugin](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/get-context/get-context-plugin.ts#L41-L128), [m2c plugin](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/m2c/m2c-plugin.ts#L17-L129), [permuter plugin](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/plugins/decomp-permuter/decomp-permuter-plugin.ts#L30-L288), [toolchain map](https://github.com/macabeus/mizuchi/blob/25eaef4214574cc20f376878dbc1b8099e97164e/src/shared/decomp-permuter.ts#L21-L95) |
| Author benchmark and limitations (not independent validation) | [author benchmark post, 2026-03-10](https://gambiconf.substack.com/p/can-llms-really-do-matching-decompilation) — pipeline lines 40–89; sampling/model/budget lines 93–150; results lines 169–220; limitations lines 221–275 |
