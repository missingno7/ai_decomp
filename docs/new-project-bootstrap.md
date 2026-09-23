# Starting a matching-decompilation project

This is a **GENERIC METHOD** checklist derived from the four local projects,
not a fixed workflow for every binary. The order prevents mass source rewriting
from outrunning its evidence. Choose the strict scope your target can justify.

1. **Pin the evidence.** Record immutable original identities, unpacking rules
   and acquisition/provenance notes without redistributing assets. Separate
   construction inputs from verifier-only evidence. Stunts' pristine hybrid
   baseline and Empires' fixture-independent exact construction are different
   valid stages, not interchangeable closure claims.
2. **Define coordinates.** State file offset, load-image offset, segment:offset,
   RVA/VA, object section/member and end-exclusive extents. Implement checked
   conversions before mixing disassembly, relocations and symbols. A hard-coded
   MZ header delta must not silently become a universal address rule.
3. **Fingerprint toolchain and ABI.** Hash compiler/linker/libraries/startup
   objects, record command/profile, memory model, pointer/call conventions and
   execution runner. Separate "pinned reproduction tool" from "uniquely proven
   historical compiler"; Stunts currently exemplifies that distinction.
4. **Establish a parser and binding model.** Test real object records and
   executable relocations, including unknown/local records and private segments.
   Preserve fixup targets, frames, addends, order and extent where relevant.
   SimAnt's far selector/offset proof and Empires' ordered relocations show why
   deleting relocation bytes is not a general solution.
5. **Define proof levels and fresh receipts.** Distinguish behavior, code shape,
   function/body, member, TU, layout and full executable. Decide which scope is
   credited. Ensure a failure invalidates stale success and that changed inputs
   cannot reuse an old PASS. Keep diagnostics from granting acceptance.
6. **Record boundary and source evidence confidence.** Use symbols/debug info,
   call targets, alignment, data references, ABI and relocations; retain unknowns.
   DWARF can constrain locals/scopes/order in Icy, while Empires infers compatible
   units from route/DATA/relocation evidence. Do not invent absent source facts.
7. **Make compilation reproducible before scaling.** A tiny controlled source
   fixture should establish encoding/feature availability under the pinned tool.
   Keep process identity, source/includes and resulting object receipts. Only
   add caches/services after uncached/parity behavior is understood.
8. **Start an experiment/negative ledger immediately.** Store parent, hypothesis,
   prediction, falsifier, changed dimensions, effective output identity, strict
   result and stop reason. Preserve useful failures with exact context so later
   agents do not repeat a disproven spelling or mistake a tool block for a solve.
9. **Probe TU/build topology early.** Test whether a function's exact output
   survives its neighbors, profiles, declarations, order and private segments.
   Group only where evidence supports it; record byte-compatible but historically
   ambiguous boundaries as such.
10. **Scale bounded agent search after the oracle works.** Give workers compact
    evidence and immutable gates; batch independent questions and preserve
    adaptive feedback. Protect exact neighbors, archive outcomes, and escalate
    repeated failure classes for tool/mechanism work. Measure total cost and
    information gained before changing routing policy.
11. **Prove unattended ownership and recovery before adding workers.** Check
    that claiming a task survives reasoning intervals and that candidate inputs
    cannot race before compilation. Use isolated project-native research lanes
    and serialized promotion; test interruption, stale context, pending journal,
    compiler timeout and reboot recovery. Start with bounded disjoint work if
    a durable shared queue is absent. Preserve global budgets across retries.
    The [fleet guidance](../knowledge/fleet-operation.md) describes current
    project boundaries, and the [compact result format](../experiments/fleet-results.md)
    records model provenance, stop reasons, scoped proof and complete cost coverage.

Sources: [Empires](../research/empires/dossier.md) for pinning/fresh closure and
topology, [Stunts](../research/stunts/dossier.md) for coordinates and early
hybrid/agent measurement, [SimAnt](../research/simantw/dossier.md) for ABI/member
factory design, [Icy Tower](../research/icytower/dossier.md) for rich debug evidence,
scope/context and exact-neighbor preservation. Their machine-readable source
refs are in [catalog/sources.json](../catalog/sources.json).
