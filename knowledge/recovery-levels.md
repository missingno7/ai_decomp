# Recovery scopes, diagnostic claims and compiler responses

**GENERIC METHOD, narrowed by the [adversarial review](../research/adversarial-synthesis-20260923.md).**
A function is a convenient task boundary, not a complete explanation boundary.
Use a scope graph when the evidence requires it; do not replace every task
with an elaborate graph by default.

## A blocker belongs to an investigation state

The relevant identity is at least `(target, candidate source, compiler/build
context, available evidence, analysis tools, proof capability)`. A queue label
may also depend on policy and remaining budget. Preserve the old label and its
context when a fresh comparison changes the diagnosis.

SimAnt's 438-row fresh pass calls 75 historical labels no longer descriptive;
26 of 27 former TU-context rows freshly fall into its source-shape category.
The latter is itself triage, not a proof of semantic error. Stunts' census has
261 tasks with multiple categories. Icy's annotation placement can change a
reported byte deficit without establishing a machine-code change. These cases
rule out one stable causal blocker per function.

Keep five kinds of claim distinguishable within an existing experiment/handoff:

| Claim kind | Required content | Concrete example |
|---|---|---|
| Observed residue | Measurement, coordinate, comparison and scope | Two BP displacement differences in Stunts `rect_adjust_from_point` |
| Supported mechanism | Controlled intervention, predicted effect, controls and applicability | Camera declaration ordering explains 11 BP-home changes for one MSC5.1 context |
| Rejected mechanism | The particular hypothesis tested and its falsifying result | Moving the rectangle temporary first leaves the same output; not a rejection of every lifetime hypothesis |
| Unresolved dimension | What the measurements still cannot explain | Camera return topology and extent after stack homes are explained |
| Workflow/capability block | Missing tool/evidence/ownership/proof permission and responsible lane | Original OMF frame method unavailable from an MZ relocation alone; unsupported multi-public promotion |

Several entries may apply simultaneously. `REGISTER_ALLOCATION` without
controlled evidence is an observed pattern or suspected explanation, not a
causal certificate. A well-supported mechanism can explain only part of a
residue. Keep evidence-backed semantic mistakes separate from compiler effects:
Icy's uninitialized `playing` and wrong state-variable bindings do not become
“GCC context” merely because emitted code is far from the target.

The current fleet signature groups *reports worth reviewing*. It does not
upgrade repeated symptoms into mechanisms, and one lineage repeated across
tasks is not independent confirmation. No new mandatory taxonomy or automatic
classifier is introduced here. Existing `structured_delta`, facts and project
extensions can carry these distinctions until a real adapter needs more.

## A graph with useful default navigation

Expression ↔ source region ↔ function ↔ TU ↔ object/link topology is a useful
search navigation path. It is not the ownership tree of all evidence:

- SimAnt private selector/data obligations can connect several functions and
  an object independently of the current source edit's scope.
- A compiler profile is an experimental condition that can apply to a TU or
  recovered object; it is not automatically a parent of every function.
- Empires GAME's inline ASM selects a route that affects unchanged neighbors.
  Separately, MUSIC's route changes ordered fixup topology despite equal code.
- Icy lexical scopes reuse stack slots; data/lifetime relations cross source
  regions. Literal and BSS ownership can connect functions without call edges.
- A Stunts source edit can change call mode/fixups, creating a link obligation
  even when target extent stays at 16 bytes.

Represent the **edit scope**, **compile scope**, **measurement scope**,
**protected scope** and **acceptance scope** separately. Useful relations are
“reads/writes,” “owned by,” “compiled together,” “relocates to,” and “observed
to affect.” A relation should cite evidence and context. Unknown relations are
not absent edges. No shared global graph database is justified by this review.

An operational pivot is:

1. State what repeats or remains unexplained, with the current scope identity.
2. Check measurement and baseline validity before assigning a compiler cause.
3. Choose the smallest *different* question: width/semantic branch, local
   lifetime, region consumer, declaration visibility, TU predecessor, binding,
   compile route, object ownership, or parser support.
4. Predict which observations should change and which peers must remain exact.
5. Compile the evidence-supported enclosing unit through its native runner; retain
   every changed dimension and return to the narrowest useful scope afterward.

This is not “always escalate upward.” A SimAnt context-looking failure can
return to one wrong helper binding; an Icy global-looking frame mismatch can
return to a missing initialization. The next experiment selects the scope.

## A compiler response surface, not a smooth gradient

Prefer **empirical compiler response map** for recorded interventions and
effects. “Compiler gradient” is only a metaphor for informative feedback:
there is no derivative, continuity, scalar descent direction or monotonic score.

Stunts source/profile variants can collapse, or a local edit can fix stack homes
while leaving extent. SimAnt batches collapse to a few outputs. Icy equivalent
tails converge late in RTL, while a small body edit changes unrelated peers.
Empires switches discrete writer/assembler routes. Distinct outputs may be
irrelevant, and equal lengths may conceal different bindings.

An effective identity needs a scope and normalization contract. **Comparison
across contexts is allowed and often the experiment's purpose**: MSC5.0/5.1
equality is useful negative evidence about version discrimination. It does not
make those contexts interchangeable cache keys or authorize cross-context
promotion. Keep output-equality observations separate from context-equivalent
reuse groups; the existing experiment matrix implements the latter.

Sources: [Stunts](../research/adversarial/stunts.md),
[SimAnt](../research/adversarial/simant.md),
[Icy](../research/adversarial/icy-regions.md),
[Empires](../research/adversarial/empires-convergence.md).
