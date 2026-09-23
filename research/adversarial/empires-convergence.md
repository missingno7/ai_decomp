# Empires convergence: adversarial historical audit

**Scope and classification.** These are `PROJECT FACT` readings of immutable
Empires Git blobs.  They document what the project's own status records claimed
at named commits; no historical compiler, build script, or sibling state was
run for this audit.  A recorded exact result is not an independent replay.

## Decision

Empires is strong evidence that exact artifact equality can be reached before
historical-source closure.  It is weak evidence that equality alone identifies
historically plausible source: the first exact structural experiment retained
raw owners, synthetic DATA/BSS, and seven explicitly named topology adapters.
The convergence was a sequence of high-fanout route, DATA/fixup, BSS, and
translation-unit/provenance changes, rather than a smooth count of individually
recovered functions.

It also did **not** start as an empty-source decompilation.  The repository's
first commit already carries an upstream inventory of 126 `MATCHING_C`, 20
`MATCHING_ASM`, and 35 `KNOWN_TOOLCHAIN_LIBRARY` entries, with extents, source,
profile, binding, and receipt metadata.  Its companion audit says the local
factory freshly rebuilt 125 C and all 20 ASM entries while refusing one stale C
receipt (`F_01CE`).  Any elapsed-time, recovered-byte, or convergence claim
that starts after this import has a substantial seed-quality confound.  The
imported material was reconstructed source rather than original game source,
but it was still prior matching knowledge.

| milestone commit | status recorded at that commit | adversarial reading |
|---|---|---|
| `e5b79736` — first byte-identical structural experiment | structural experiment exact, SHA equality and relocation order equality; ordinary candidate full file false; RAW ownership 4,012 bytes; source-data experiment has 4,006 local raw-source bytes, 13,932 synthetic DATA bytes, 37,252 synthetic BSS bytes; seven adapters | The exact path was a bootstrap construction experiment, not source closure. |
| `f78e073` — opaque fallback retired | RAW ownership and local raw-source bytes are zero, but ordinary candidate still differs; synthetic DATA/BSS remain and seven adapters remain | Removing an opaque/raw fallback is necessary but not enough for a naturally reconstructed artifact. |
| `4cc84747` — adapter inventory | raw remains zero; named adapters fall to six and symbol transforms to zero; ordinary candidate is still nonexact | Adapter retirement measures topology cleanup, not acceptance by itself. |
| `b4a0fc07` — canonical structural route | exact structural experiment remains; remaining adapters are four; synthetic DATA/BSS still 13,932/37,252 and OMF-adapter owners are 12 | This is the best pre-closure replay target: exact via a named route while its remaining non-source mechanisms are visible. |
| `e56855c6` — source/provenance closure | one-link built route is full-file and relocation-order equal; synthetic DATA/BSS, raw fallback, active structural adapters and OMF transforms are zero; 106 relocations; 37,250 BSS bytes fully partitioned | Equality is now tied to a much stronger representation claim, but irreducible ASM/runtime categories remain. |
| `873d1df0` — closure freeze | current acceptance reports SHA equality, 106 relocations and one link; raw fallback, unresolved symbols and adapters zero; runtime summary reports 6,571 bytes with raw-unresolved zero | A named acceptance route remained exact through the freeze, subject to the metric caveat below. |

## Claims tested against counterexamples

| strong claim | support | counterexample / confound | narrow conclusion | falsifier |
|---|---|---|---|---|
| First full-file equality proves historical source closure. | `e5b79736` records an exact structural experiment and ordered relocations. | At the same commit its ordinary candidate differs, with 4,012 RAW-owned bytes, 4,006 local raw-source bytes, synthetic DATA/BSS, and seven adapters. | It proves a scoped structural construction reached equality. It does not prove all contributing source was historical or natural. | Clean replay of only the recorded source/toolchain route, with every input declared and no adapter/raw source, still reaches equality. |
| Zero raw fallback proves no hidden byte representation remains. | `f78e073` records zero RAW ownership/local raw-source bytes; closure records raw-exe fallback zero. | `e56855c6` structural status still calls the complete 6,571-byte runtime category `ASM_DB_CAPSULE`, while current status decomposes it into 5,840 symbolic instructions, 662 typed data, 69 intentional exact encoding and zero raw-unresolved bytes. These are different metrics. | Zero means zero under the named metric. It cannot by itself establish absence of literal or exact-encoding mechanisms. | A source-quality audit that classifies every active byte by a single documented taxonomy and shows no unapproved literal/capsule category. |
| Convergence was monotonic after exactness appeared. | The named structural experiment stays exact across the selected snapshots; adapters move 7→6→4→0 and synthetic DATA/BSS later reach zero. | The ordinary/baseline candidate remains nonexact through the bootstrap snapshots; even closure status preserves a separately nonexact `baseline_diagnostic`. Also source categories change from mostly C to a final mixed C/ASM/runtime representation. | Monotonicity applies only to the protected acceptance route and selected debt counters, not every build route or source-quality category. | A later acceptance receipt on the same pinned route reports changed SHA, relocation ordering, unresolved symbols, adapters, or fallback bytes. |
| Function-by-function C recovery was the main driver. | Earlier ownership records include hundreds of matching-C owners. | Equality already existed with high-fanout DATA/BSS/adapters unresolved; closure still retains hand-written ASM and a runtime block. Commit/state transitions identify linkage and topology mechanisms that affect many owners at once. | Local C recovery matters, but route/TU/DATA/BSS/fixup/runtime mechanisms are first-class convergence dimensions. | Controlled history analysis showing equality would have followed without those structural changes under the same source/function set. |
| Final equality means the original was wholly ordinary C. | Closure has 60 C units and many matching-C bytes. | The frontier records ten assembler modules plus runtime, inline ASM in C units, and negative compiler evidence for register/LODS/LOOP/BP idioms. | Exact reconstruction may legitimately retain historical ASM/runtime or compiler-constrained inline ASM. | A compiler-verified C replacement for each retained ASM/runtime scope preserves full accepted artifact and topology. |
| The convergence history measures recovery from raw code. | The first-commit inventory is explicit about imported matching entries and fresh rebuild checks. | It began with 126 matching-C, 20 matching-ASM and 35 library entries; 125 C and 20 ASM entries freshly rebuilt, one stale C receipt refused. | Imported entries are not original source, but they are an unusually high-quality matching seed. | Re-run the same workflow from a raw-only baseline with imported correspondence/source/receipt data withheld and report comparable milestones. |

## Discrete mechanisms, not a scalar score

The state series identifies distinct mechanism classes that must be preserved in
a shared experiment record:

- **Link route and relocation topology.** The early exact experiment and later
  acceptance are separate from the ordinary baseline.  At closure, acceptance
  requires one TLINK invocation and all 106 relocations in order.
- **DATA/fixup ownership and module order.** The bootstrap starts with 13,932
  synthetic DATA bytes and only later reaches zero.  This cannot be inferred
  from function-body equality.
- **BSS partition.** Synthetic BSS is 37,252 in the early snapshots; the
  closure route records all 37,250 BSS bytes as partitioned source with zero
  aggregate remainder.  The two-byte total change is evidence that counts must
  be read in each route's exact context rather than treated as a universal
  progress series.
- **Structural adapters and OMF transforms.** Explicit adapter count falls
  7→6→4→0; OMF-adapter owners are still 12 at the pre-closure canonical route
  and zero in closure.  These are source/topology mechanisms, not mere cleanup.
- **TU and compiler-origin classification.** The closure frontier keeps source
  grouping and irreducible inline ASM where Turbo C cannot emit the required
  behavior.  The provenance record is a separate proof layer from byte
  equality.
- **Runtime boundary.** Closure records zero raw-unresolved runtime bytes, but
  the runtime remains an explicit 6,571-byte category.  Shared tooling needs a
  representation-kind field, not a binary reconstructed/unreconstructed flag.

No inspectable source blob binds a model, prompt, model configuration, or
per-change authorship to the recovery events.  Commit trailers near closure
name models, but a Git co-author trailer does not establish which hypothesis,
source line, or independent proof a model supplied.  This audit therefore
records model attribution as `UNKNOWN`.

## Concrete high-fanout route experiments

These are stronger than an adapter count because they include a positive route
mechanism and rejected neighbor controls.

**GAME translation unit.** The closure TU record identifies
`C_3A75_4A93` / `src/GAME.C` as an eight-member, 4,146-byte unit: TURNLOOP,
BRDTERR, MENUBKDP, LVLDRV, BLITPAT, BOOTSEED, CAMPADV, and GAME.  TURNLOOP and
LVLDRV require Turbo C's assembler route (`-B`); BOOTSEED's real `asm sti`
causes that route, and replacing it with `__sti__()` breaks their exactness.
The document also records negative controls: extending `-B` through HITTEST
shrinks it by one byte; extending the GAME-side run across the BOARD boundary
cannot preserve both BRDPAINT and BRDTERR with one `a74a2` declaration; and a
HUD-to-ANIMFRAM run fails because DATA is not contiguous.  This is evidence
that a source body, its TU neighbor, compiler route, declaration view, and
DATA ownership are jointly constrained.  It does not establish the original
lexical file text beyond the byte-exact supported grouping.

**MUSIC relocation topology.** The closure history records a 700-byte
`M_DDD9_DF98` C unit whose code bytes/public offsets matched while an inline
ASM route produced far fixups in ascending order; the historical relocation
run was descending.  The single-module outcome is therefore explicitly
`SAME_CODE_WRONG_TOPOLOGY`, rather than accepted exactness.  Rewriting the
cached frequency routine as structured C removes the inline-ASM route, makes
Turbo C emit descending FIXUPPs, and permits the active C module to pass the
ordered-relocation acceptance gate.  The repository test preserves the
negative decision table: equal code plus disagreeing ordered relocation
directions is a topology failure, and no-relocation scopes are not treated as
topology evidence.  The exact number of bodies whose route changes affected
the final link is unavailable in the inspected documents; the documented
module extent is 700 bytes.

## One recommended replay snapshot

Use **`b4a0fc076372fb86387a3cdcede8485faa7d38a5`** as one read-only,
historical pre-source-closure replay specimen.  Its status records exactness in
`exact_structural_experiment` yet still exposes four remaining adapters, 12
OMF-adapter owners, and synthetic DATA/BSS.  It is more diagnostic than the
final freeze because it can test whether a proposed checker separates
artifact equality from historical-source plausibility.

This is a recommendation, not a replay result.  The original oracle evidence
must remain available to the *researcher*: a reconstruction task without the
target bytes, disassembly, documented extent, public/fixup evidence, and
historical toolchain profile would be artificially impossible.  Leak control
instead separates three roles.  Research analysis may inspect an immutable,
pinned original-evidence set; construction receives only a frozen evidence
packet derived from that set; and a separately invoked verifier compares the
constructed artifact to the original oracle after the construction step.

The construction snapshot must be a **sanitized export or history-limited
object store** at `b4a0fc07`, with pinned Turbo C, TASM, TLINK and runner
hashes, network disabled, and output outside the checkout.  A detached worktree
alone is insufficient: it normally shares the repository object database and
can expose later history.  It must exclude later recovery notes, derived
candidates, cached objects, generated reports, prebuilt output, and all
post-snapshot solution artifacts.  Record an input allowlist and file-access
audit.

The allowlist must retain every construction input and all four declared
adapters of the frozen `b4a0fc07` task.  That commit already records zero RAW
owner bytes, but it still has 13,932 synthetic DATA bytes, 37,252 synthetic
BSS bytes, and 12 OMF-adapter owners.  Removing those baseline mechanisms
would make a different, later source-closure problem rather than replaying the
bootstrap route.  Reject only new oracle-derived byte patches or undeclared
inputs.  Report artifact equality and adapter/debt retirement as separate
scores.  A replay that permits future solution artifacts tests repository
self-consistency; one that hides the original evidence from the researcher
tests an impoverished different task.

## Provenance boundary

The companion JSON pins all cited blobs.  The parent commits are the evidence
coordinates, and each `sha256` is over the blob content.  These checks neither
reproduce the historical toolchain nor validate the project's recorded receipt.
The JSON retains a transcription-correction record for the earlier malformed
63-character SHA-256 of the closure TU-structure blob; the corrected frozen
blob hash is 64 characters and was recomputed from commit `873d1df0`.
