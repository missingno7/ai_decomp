# September 24 update validation

- 19 tests pass; workspace catalog/reference/link checks pass.
- Regeneration adds six scoped mechanisms and two negative findings: 26 mechanisms,
  23 negatives and 120 sources. Every original 104 source record is unchanged.
- Three previously implicit tool citations are now explicitly pinned to their
  previously published working-tree identities; current Git cleanliness no longer
  silently replaces them with an older committed blob.
- Catalog provenance: 109/120 verified, no unavailable sources.
  The remaining live files have drifted; their old hashes remain recorded.
- Dated update provenance: 92/98 verified, no unavailable
  sources. See the [full results](validation.json) for live drift rather than
  treating regenerated files as a reconstruction regression.
- The Icy same-population comparison checks all 253 original VAs and 125,641
  function bytes; exactly one status becomes FUNCTION_MATCH, adding 1,136 bytes.
  Initial 25 report hashes match ledger references and Git/live text agrees.
- Stunts' initial queue/census/validation fingerprints agree. Its later closing
  queue advances beyond the retained validation fingerprint while strict ownership
  counters remain unchanged. Both states are retained separately.

No sibling build, compiler, test suite, regeneration, queue mutation or promotion
was invoked. This is inspection of recorded evidence, not independent reproduction
of native acceptance. New machine-readable observations contain metadata only,
not original source, machine bytes, tools or SDKs. Pinned Git evidence is retrievable;
working-tree hashes identify observations but do not archive the underlying file.
