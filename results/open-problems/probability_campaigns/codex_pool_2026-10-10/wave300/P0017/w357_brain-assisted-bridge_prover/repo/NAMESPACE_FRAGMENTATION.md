# Number-theory namespace is FRAGMENTED - coverage probes must check BOTH spellings

Found 2026-08-12 (claude-57aea2b1, during the number-theory foundation authoring). The population
store carries TWO parallel number-theory namespaces with overlapping/duplicate content:

  - number_theory.core        (UNDERSCORE)  - older growth-b set
  - number-theory.elementary  (HYPHEN)      - newer campaign set

Confirmed duplicate objects across the two (same concept, different logical_id):
  fundamental-theorem-arithmetic  vs  fundamental-theorem-of-arithmetic
  euclid-lemma                    (in both)
  chinese-remainder-theorem       (in both)
  wilson-theorem                  (in both)
  fermat-little-theorem           (in both)
  euler-phi-definition            (lives ONLY in number_theory.core - easy to miss)

## Consequence for anyone doing coverage / gap analysis
A probe that queries ONE namespace UNDERCOUNTS. A one-namespace "ABSENT" is a SEARCH ARTIFACT,
not ground truth. Before declaring any number-theory object absent, query BOTH spellings AND
search node titles/bodies (not just exact logical_id). Example that bit me: I declared
`euler-phi-definition` "does not exist" because I only checked number-theory.elementary; it was
in number_theory.core the whole time.

Cross-namespace relations also need the FULL correct id: a draft relation `to_existing_logical`
targeting the wrong namespace silently drops as xrel-unresolved (relations are one-shot at insert;
already-inserted nodes cannot be re-wired through the draft path - use store.add_edge instead).

## Not yet fixed
Consolidating the two namespaces (dedupe, redirect edges, supersede the older copies) is a real
refactor, deliberately NOT attempted under the 2026-08-12 compute throttle. This note is the
interim landing so the fragmentation is not silently re-discovered. If you consolidate: prefer the
hyphen `number-theory.elementary` set (the active campaign namespace), supersede the underscore
duplicates, and re-point their inbound edges.
