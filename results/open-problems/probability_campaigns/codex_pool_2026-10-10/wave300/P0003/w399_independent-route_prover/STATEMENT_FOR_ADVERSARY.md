# P0003 primary question and related chordal formulation — statement only

2026-10-10, w399; adversary w400, referee w401.

Original ledger target, now verified: Geoffrey R. Grimmett, Selected problems in probability theory, arXiv:2205.07318, Question 2.2, PDF page 3, asks whether uniform n-step honeycomb SAW from the origin converges weakly to SLE(8/3) under suitable rescaling. It leaves the scaling sequence, SLE domain/version, and topology informal. The precise chordal formulation below is a related working conjecture. No equivalence between the two ensembles is asserted; the full original question remains unproved in this packet.

Related precise chordal working statement:

Let D be a bounded simply connected Jordan domain in the plane with two distinct marked boundary points a,b, with analytic boundary near a,b to avoid endpoint approximation ambiguity. Let G_delta be consistent connected honeycomb-lattice approximations of D at mesh delta, and a_delta,b_delta their marked accessible boundary vertices converging to a,b. Sum over all vertex-self-avoiding nearest-neighbour paths omega from a_delta to b_delta in G_delta, with variable length and weight x_c^{|omega|}, normalized by their finite total weight. Here x_c = 1/sqrt(2+sqrt(2)). Linearly interpolate the paths in D. The target is convergence in law as delta decreases to zero to chordal SLE(8/3) in D from a to b, in the uniform curve metric modulo increasing reparametrization (Fréchet metric, with zero-distance paths identified).

This is a regular-domain specialization of Duminil-Copin–Smirnov, arXiv:1007.0575v2, Conjecture 1, Section 4, following Lawler–Schramm–Werner, arXiv:math/0204277v2. Honeycomb connective constant and therefore x_c are established; the convergence statement is conjectural. Current openness on 2026-10-10 is UNKNOWN: the limited literature and retired-work checks do not certify present resolution status. The exact approximation convention must be fixed in any completed theorem.

Source convention: the honeycomb source counts visited vertices; our vertex-to-vertex paths count edges. The vertex count is the edge count plus one on every such path, so changing between these weights multiplies every term by the same x_c and leaves the normalized law unchanged. This does not establish equivalence to a boundary-mid-edge or fixed-n scaling formulation.

The fixed-n ensemble with conjectural n^(-3/4) spatial scaling is a different formulation and is not silently substituted for this variable-length boundary-to-boundary measure. The uniform next-unvisited-neighbour kinetic walk is also different: conditional next-step probabilities depend on tail partition functions.

Independent adversarial task: test the ensemble, approximation, topology and any claimed implication to SLE(8/3). No proposed proof is included here, to preserve your independent first attack.

2026-10-10 source clarification (now checked): Geoffrey R. Grimmett, Selected problems in probability theory, arXiv:2205.07318, Question 2.2, PDF page 3, asks whether a uniform n-step honeycomb SAW starting at the origin has a weak SLE(8/3) limit under suitable rescaling. The source does not specify the scaling sequence, the precise SLE domain/version, or the topology. This is the exact ledger source target. The chordal conjecture above is a related precise working formulation, not a proved equivalent statement of that question. An ensemble-transfer theorem is an additional open obligation. No n^(-3/4) normalization is assumed to be proved.
