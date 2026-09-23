# Recovery regions: useful evidence units, unproven independent jobs

**Decision:** make a region an optional first-class *research scope*, while
retaining whole-function/TU compilation and native acceptance. Independent
region grinding remains a **WORKING HYPOTHESIS**. A source merge succeeding
does not establish code-generation independence or a partial proof that composes.

## Existing architecture and its counterexamples

Icy already has an implicit region workflow: five play worker files and four
draw worker files are merged into whole definitions; the play sidecar names
six spans (W1a, W1b, W2–W5), and draw names four (D1–D4). Separately, the early
`play-census.json` partitions all **17,420 historical bytes into 43 intervals**,
with calls, data references and frame evidence. These are different region views,
not an established mapping between ten source spans and machine instructions.
Repeated labels can describe noncontiguous machine intervals.

`function_lines.py` provides original line-table sequences, calls by line and
lexical blocks. `line_budget.py --regions` already computes candidate region
byte budgets through whole-TU overlays. Do not rebuild that compiler wrapper.
Its comments warn that inlining and block reordering distort attribution, and
annotations are author claims. `local_slot_trace.py` lists accesses but infers
read/write heuristically; it does not compute edge-specific liveness or prove
variable identity in a reused slot.

The [read-only inventory](../research/adversarial/region-inventory.json) found:

- Play's 43 historical intervals cover 17,420 bytes without gaps/overlap. Its
  JSON contains **272 direct and 18 indirect call records**, 290 total; the
  prose census's “290 direct + 18 indirect” headline is inconsistent. These
  are retained diagnostic records, not independently re-decoded call evidence.
- The early census compares against a **623-byte stub**. It must not be mixed
  with the current 17,400-byte candidate as if it were the same experiment.
- Original evidence exposes 47 play lexical blocks/110 locals and 33 draw
  blocks/24 locals; 11 and 27 blocks respectively have multiple recorded ranges.
  A contiguous-address-only region abstraction would lose evidence.
- Play's six sidecar spans fit within its current 1,667-line retained file,
  but have no body hash binding. Draw's sidecar ends at **586**, beyond the
  current **545-line** file. The prototype withholds draw's source-region mapping.
- Eight of the census's 66 stack slots have multiple named DWARF candidates.
  One slot cannot be treated as one source local or one live range.

Existing coupling evidence is already enough to reject unconditional independence:

| Intervention/observation | Observed effect | What it establishes |
|---|---|---|
| W1b writes `midY`, its consumers are in W2 | Missing W2 consumption makes the producer dead | Reported semantic dependency, not mysterious allocator noise |
| `playing` left uninitialized in a retained play reconstruction | Historical commit reports W1b/W2/W3 eliminated; 5,060 versus 17,420 bytes | Invalid/incomplete source can lose whole regions; not a test of equally defined semantics |
| Draw independent status tests | 8,203→8,137 bytes; exact TU count 62→60; loses `show_instructions` and `stopGameMusic` | Reported cross-function compiler-context effect; precise internal cause unresolved |
| Generated prototype block added around unchanged play | 17,400→17,497; no-prototypes control restores baseline | Measurement wrapper can change the compilation problem |
| Summary duplicated into two source arms | Seven calls survive `179r.dse2`, six after `181r.csa` | Tested suffix commoning; text regions do not imply emitted regions |
| Historical-line comment on a multiline closing line | Apparent play W1b deficit −138; 105/118 bytes misattributed in `select_profile` | Measurement artifact, not missing machine behavior |

Sources and limitations are retained in [Icy audit](../research/adversarial/icy-regions.md),
[curated observations](../research/adversarial/region-observations.json) and the
inventory's own hash manifest. The observations do **not** form a complete
one-region perturbation matrix. Unmeasured effects stay unknown, including
apparently empty off-diagonal cells.

## Minimum region contract

Bind a region ID to source/body and evidence versions. Record source span sets
with their coordinate system; original and candidate machine instruction/block
sets separately; entry/exit edges; known live-ins/live-outs; local scope and
lifetime evidence; stack-slot candidates; calls and data/fixup references;
historical line/DWARF evidence; exact anchors; and protected neighbors/context.
Each relationship needs an evidence reference or an explicit unknown. Permit
noncontiguous sets and overlapping *evidence* regions even when editable source
spans are required to be disjoint. Do not invent a complete interface from DWARF
names or a sequential walk of registers.

Candidate boundaries should combine CFG dominator/postdominator or SESE
structure, natural loops/branch subtrees, lexical blocks/lifetimes, source
phases and call clusters. These are **proposals to evaluate**, not computed
independence certificates. Rank small known interfaces and tested locality;
reject cuts with large shared state, uncertain indirect edges, reused lifetime
identities or widespread observed compiler effects. Calls and lexical boundaries
alone do not make a historical subfunction.

Prefer independent diagnostic dimensions over a single ordered state ladder:

| Proposed annotation | Minimum evidence before using it |
|---|---|
| REGION_SEMANTICALLY_SUPPORTED | Specific machine/source facts and unresolved semantic obligations; not a general equivalence proof |
| REGION_CFG_SUPPORTED | Original/candidate edge correspondence under a named decode/mapping scope |
| REGION_CODEGEN_STABLE | Explicit perturbation set/context and unchanged measured outputs; not stability under arbitrary edits |
| REGION_STABLE_EXACT | Complete named instruction/fixup set exact across those controls; never FUNCTION_MATCH |
| REGION_CONTEXT_COUPLED | An intervention with observed effects outside the region; distinguish semantic dependency from compiler effect |
| REGION_UNRESOLVED | Missing or contradicted obligations listed explicitly |

A region may be semantically supported and context-coupled simultaneously.
These labels remain a proposed research vocabulary; the prototype issues only
unresolved/unknown mappings and no new exactness claim.

## Implemented first step and next measurement

`tools/region_inventory.py` is original, stdlib, read-only adapter code. It reads
existing sidecars, retained-body lengths/hashes, function/DWARF reports and the
historical census. It checks interval coverage and source-span bounds, reports
stale mappings, and attaches curated reported influences. It executes no sibling
script and infers no liveness or new causes. This is an evidence/freshness
prototype, not a region solver or a demonstrated throughput improvement.

The command below names the captured base commit. For a new snapshot, supply
the newly observed base commit; hashes still identify dirty working-tree inputs.

```powershell
python tools/region_inventory.py --icy-root ../icytower_recon --observations research/adversarial/region-observations.json --base-commit fc2000225df112de2cf248d92d23da8e839ca108
```

Next, in Icy's owning workspace, preregister a **bounded influence experiment**:

1. Repair/regenerate and hash-bind region spans against the frozen retained
   bodies. Reproduce a whole-TU baseline with the exact order, prototypes,
   flags, headers, protected peers and compile route. Include a no-op control.
2. Select one existing evidence-backed source change in each of two regions,
   with distinct predictions. Avoid an uninitialized-source baseline. Keep
   every other region and TU input fixed. Compile the full function in the
   evidence-supported TU and native route.
3. Retain source diffs, complete objects and aligned candidate-parent/oracle
   instruction/fixup deltas, frame changes, all peer statuses and data/literal
   changes. Map effects only where source/CFG evidence supports correspondence.
   Do not use raw positional diff or equal region-byte totals as that mapping.
4. Emit a sparse matrix with `changed`, `unchanged_under_control`, `ambiguous`
   and `unmeasured` cells, separating semantic, compiler and measurement effects.
5. If the two edits appear local, test their combination. Noncommuting effects
   falsify independent promotion even when each edit alone looks local. Stop
   after the preregistered controls/three edits; widen only for a new question.

A practical first cohort is baseline/no-op, one play producer-consumer correction,
one disjoint results-region correction, then the combination: **five whole-TU
compiles** if both edits are supported and the baseline reproduces. Draw's
known peer-loss trial supplies a negative coupling control from existing logs;
replay it only under its own exact baseline. No such compiler run was launched
by this review. Success would support small research jobs with guarded integration,
not independently promotable fragments or synthetic helper extraction.
