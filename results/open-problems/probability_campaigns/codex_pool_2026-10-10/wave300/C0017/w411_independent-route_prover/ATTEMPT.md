# C0017: local boundary laws and a finite-gadget obstruction

2026-10-10, w411. Self-authored finite proofs; independent audit pending. This packet does not prove square-lattice conformal invariance.

The exact target and boundary assumptions are in STATEMENT_FOR_ADVERSARY.md. The primary Garban-Steif source is arXiv:1102.5761, Chapter II section 4, PDF page 26 (zero-based 25), printed page 24, immediately after Theorem II.2. It establishes the triangular-site crossing limit and describes the square-bond analogue as an open problem at the time of writing. Its SLE illustration concerns triangular percolation. The working target asks for both Cardy crossings and square-bond exploration convergence to SLE(6). Current openness remains UNKNOWN: arXiv:1112.2017v5 and arXiv:2409.03235v6 claim proofs, and neither has been mathematically certified in this packet.

Prior-attempt digest. Intake attempts.jsonl, line 17, C0017-A001 seeks a square-lattice parafermionic observable. It reports a missing discrete-analytic relation, not a proof. Its displayed q=1 spin 2/3 is not reused here. A spin convention and its defining equation would need a primary-source check before any correction. Targeted C0017 searches in the named H/I attempt directories and Lean directory found no further proof record. Team O's board contains C0018 and C0050 but no C0017 row at the read time. APPROACH_PRECOMMIT.md records this route before any peer proof was read.

Chosen route. Regard a small percolation gadget as a random partition of its boundary terminals. The outside world sees only this partition for an ordinary connectivity event. Transfer triangular-site limits through local replacements only if the full partition laws agree, or if the exact accumulated crossing defect vanishes. Pairwise terminal connection probabilities alone are inadequate. Bond-to-bond star-triangle transformations do not supply the triangular-site endpoint; Grimmett-Manolescu arXiv:1108.2784 proves equality of certain exponents conditional on their existence, and arXiv:1105.5535 proves box-crossing transfer, not this missing endpoint comparison.

L1 (saved first). For an independent three-arm bond star with probabilities p_a,p_b,p_c, the all-connected probability is p_a p_b p_c. The pair-only ab probability is p_a p_b(1-p_c), with two analogous expressions. If the all-connected probability is 1/2, all p_i are positive. Vanishing of all three pair-only probabilities forces all p_i=1, a contradiction. Hence it cannot implement a fair all-or-none three-terminal selector.

L2 (general finite obstruction, including deterministic edges). Let G be a finite undirected graph with k >= 3 distinct labeled terminals and mutually independent Bernoulli edges, with arbitrary probabilities in [0,1]. Let Pi be the partition of the terminals induced by open paths. If both the all-separated partition and the all-connected partition have positive probability, at least one strictly intermediate terminal partition has positive probability.

Proof. Delete edges of probability zero and contract every connected component of edges of probability one. All-separated positive probability means that no contracted component contains two distinct terminals. Each remaining optional edge has probability strictly between zero and one, so every assignment of those finitely many edges has positive probability. All-connected positive probability means that the graph of possible edges has a component containing every terminal. Take a tree connecting these terminals and prune all nonterminal leaves. Choose an edge of the resulting tree; each of its two sides contains a terminal, since a side with no terminal would contradict this pruning/minimality. Open precisely the tree edges except this chosen edge and close every other optional edge. The terminal partition has exactly two blocks. For k >= 3, it is strictly between all-separated and all-connected. Its probability is positive. Parallel edges and loops after contraction cause no difficulty: choose a tree edge as needed and assign all other optional edges closed.

Quantitative corollary. If the m optional edges all have probabilities in [epsilon,1-epsilon], where 0 < epsilon <= 1/2, the witnessing configuration has probability at least epsilon^m. For the selector law S_q putting mass q on all-connected and 1-q on all-separated, 0 < q < 1,

    d_TV(Law(Pi), S_q) >= min(q, 1-q, epsilon^m).

If either extreme partition has zero probability, testing that singleton event gives q or 1-q. Otherwise test the set of intermediate partitions, whose selector mass is zero and whose gadget mass is at least epsilon^m. This is a finite-budget bound, not a bound uniform as m grows. No claim is made that approximation by growing gadgets is impossible.

L3 (exact replacement identity). Let S_1,...,S_N be finite state spaces, with probability laws mu_i and nu_i, and let F: product S_i -> [0,1]. Define H_i on all coordinates except i to use nu_j for j < i and mu_j for j > i, independently. Then

    E_product(nu) F - E_product(mu) F
      = sum_i E_H_i [ sum_s (nu_i(s)-mu_i(s)) F(s, X_-i) ].

For osc_i(X_-i) the range of F(s,X_-i) over the union of the two local supports,

    |E_product(nu) F - E_product(mu) F|
      <= sum_i d_TV(mu_i,nu_i) E_H_i osc_i.

For a crossing indicator, osc_i is the indicator that the exterior is sensitive to some admissible local state change. These sensitivity events need not be independent across i.

Proof. Telescope the N+1 product laws having their first j coordinates drawn from nu and their remaining coordinates from mu. Adjacent laws have the same exterior marginal H_i; their local state is independent of that exterior. Conditioning on the exterior gives the displayed finite sum. The local signed measure has total mass zero. Subtract the minimum of the local values of F; its positive mass is d_TV and its negative mass is -d_TV. The absolute local sum is bounded by d_TV times the oscillation. Average and use the triangle inequality. This proves the factorization actually used, and does not multiply conditional estimates over replacement locations.

L4 (three pair tests can all pass while a crossing test fails). Let S be the fair three-terminal selector. Let T be an independent three-arm star with the same arm probability s=1/sqrt(2). For every pair of terminals, P_S(a~b)=P_T(a~b)=1/2. Add the same deterministic exterior wiring identifying a and c on one target boundary arc, with b on the other. The crossing event is (a~b) OR (c~b). Its probability is 1/2 under S and

    1 - 1/(2 sqrt(2))

under T. The discrepancy is (2-sqrt(2))/4 > 0, about 0.1464466094.

Proof. In the star, the pair connection probability is s^2=1/2 and the triple connection probability is s^3=1/(2 sqrt(2)). The intersection of the two pair connection events is exactly triple connection. Inclusion-exclusion gives 2s^2-s^3. In the selector, either event occurs precisely when the selector is open. The exterior is a deterministic connection a--c and is independent of both local gadgets. This is a finite crossing counterexample to inference from matched pair marginals; it says nothing against continuum universality.

Attempt to close the target. An exact fixed-gadget bond-to-selector replacement is ruled out by L2. A comparison relying only on pair marginals is ruled out by L4. The remaining route is to build a genuine mesh-dependent comparison between square bonds and triangular sites and control the signed sum in L3. Equality of the critical threshold, self-duality, or bond-to-bond exponent universality gives none of those signed cancellations.

To expose the scale of a possible estimate, suppose, as an explicit additional hypothesis, a comparison used O(delta^-2) bulk blocks, had local total-variation defect O(delta^beta), and all its hybrid exteriors had sensitivity probability O(delta^(5/4-eta)) for some fixed eta > 0. L3 would give a bulk bound O(delta^(beta-3/4-eta)), which tends to zero if beta > 3/4+eta. This is only algebra under stated assumptions. The four-arm value 5/4 is not asserted for square bonds or for those hybrid laws; boundary blocks require a separate bound. A constant local defect leaves this crude upper bound non-vanishing, so it cannot prove convergence. A diverging upper bound is not a lower bound on the actual crossing discrepancy.

Single hardest remaining gap: construct a valid comparison having the actual square-bond and triangular-site endpoint laws, and prove its total signed crossing defect tends to zero, with boundary/exploration conditioning controlled. No such comparison estimate is proved here. Even a crossing-only estimate would leave interface tightness and SLE(6) identification to justify. Consequently C0017 remains unresolved in this packet.

Next concrete proof step: derive the local signed defect for a specified common planar cell construction, and check whether cancellation survives deterministic exterior wiring a--c. Do not assume that matching pair probabilities is enough.
