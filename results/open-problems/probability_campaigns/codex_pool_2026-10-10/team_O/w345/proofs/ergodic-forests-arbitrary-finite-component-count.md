# P0048: Invariant ergodic spanning forests can have every finite component count

Label: proof; author checked only. Independent audit: PENDING w347.

For each integer k>=2, the Cayley graph G_k of Z with generators {+1,-1,+k,-k} has a deterministic translation-invariant spanning forest with exactly k components. Keep exactly the length-k edges. Its point-mass law is ergodic under translations. Thus translation invariance and ergodicity alone cannot exclude any finite component count greater than one.

Assumptions: k is an integer at least two; G_k has both length-one and length-k edges; Only length-k edges are retained

Each retained component is one residue class modulo k, with edges between consecutive elements of that class. It is a bi-infinite path and hence has no cycle. Every integer belongs to exactly one of these k residue classes, so the forest spans G_k and has k components. Translation by one permutes the classes and preserves the whole edge set, proving invariance. A point-mass probability measure assigns every measurable event probability zero or one, and is therefore ergodic. The earlier k=2 example is its first instance. None of these deterministic forests is asserted to be a free uniform spanning forest.

Limits: This refutes a proposed inference from ergodicity, not the one-or-infinity classification for the actual FUSF law. It adds no nonunimodular FUSF counterexample.

Existing card: math:probability.core:open-problem-p0048-one-or-infinitely-many-free-forest-components-without-unimodularity
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:5467
