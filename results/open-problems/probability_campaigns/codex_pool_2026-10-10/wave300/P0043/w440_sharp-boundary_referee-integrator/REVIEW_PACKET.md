# P0043 referee packet

2026-10-10. Primary source: Benjamini–Schramm (1996), Conjecture 4, site percolation, connected locally finite almost-transitive graphs, and **p_c<1**; the authors explicitly say the nonplanar questions also apply to bond percolation. Hutchcroft (2016), Conjecture 1.1, gives the bond formulation. See SOURCE_STATUS.json for exact citations and quotes.

## w438-C01 — KEEP (boundary calculation only)

I rederived the claim independently. On the nearest-neighbor path Z, an infinite component of 0 at p<1 must contain every edge of either the nonnegative or nonpositive ray. For each n these events are contained in one of two n-edge-open events of probability p^n, so theta(p) <= 2p^n -> 0. At p=1 all edges are open; hence p_c=1 and theta(p_c)=1. The proof is correct. **Scope correction:** this does not counterexample the original Conjecture 4, which expressly assumes p_c<1. It only counterexamples the abbreviated ranking wording. Remaining parent gap: all quasi-transitive graphs with p_c<1.

## w439-P0043-boundary-001 — KEEP (boundary calculation only)

The same independent calculation reproduces the exact p_c=1 and theta(1)=1 assertions. Its source caveat is accurate, and its status as a boundary counterexample is appropriate. It overlaps w438-C01; count it as a second derivation, not a second mathematical result. Remaining parent gap: all quasi-transitive graphs with p_c<1.

## w438-C02 — KEEP (exact finite identity)

Write q=q_(i+1). For a_i=2, disjoint child subtrees give q_i=1-(1-pq)^2=2pq(1-pq/2). Direct subtraction yields 1/q_i-1/(2pq)=1/[4(1-pq/2)]. For a_i=1, q_i=pq and the difference is zero. Repeated substitution of 1/q_i=(1/(a_i p))(1/q_(i+1))+d_i gives 1/q_0=1/m_n+sum_(i<n)d_i/m_i. Since 0<q<=1 and p<=1, the stated bounds on d_i follow. This derives the hardest equality directly and uses independence only across disjoint descendant subtrees. It cannot be transplanted unchanged to graphs with loops.

## w438-C03 — KEEP (special-case tree threshold and rates)

The bound |beta|/(N ln 2)<=1/(8 ln 2)<1/4 gives 1/4<f'<3/4, so floor increments are 0 or 1 and four consecutive increments contain a 1. Since B_n=floor f(n), L_n=2^B_n lies between (1/2) 2^f(n) and 2^f(n), where 2^f(n)=2^(n/2)(1+n/N)^beta. Thus m_n=(p sqrt(2))^n times a bounded-factor polynomial correction. Below 1/sqrt(2), E Z_n=m_n ->0; above, the C02 reciprocal upper bound stays finite. At criticality, the branching-level reciprocal sum has the same convergence and divergent order as sum n^(-beta), because branch gaps are at most four and adjacent polynomial weights are comparable. This proves survival iff beta>1 and the asserted n^(beta-1), 1/log n rates. The root is the unique degree-one vertex, so automorphisms fix every level and there are infinitely many orbits. This is outside P0043. The regular-tree special case was already in the historical rank sheet; this family adds an explicit sharp stress test, without a novelty claim.

The later analytic lower bound also checks. For beta>1, m_i>=1/2(1+i/N)^beta, so S_infinity<=2 sum_i(1+i/N)^(-beta)<=2(1+N/(beta-1)). Taking n to infinity in C02 gives 1/theta<=S_infinity/[4(1-p_c/2)] and hence theta>=(2-p_c)/(1+N/(beta-1)). At beta=2, N=24 and p_c=1/sqrt(2), giving theta_(T_2)(p_c)>=(2-1/sqrt(2))/25. This is an analytic bound, not a simulation measurement. KEEP with the same outside-target scope.

## w438-C04 — KEEP (local-limit obstruction outside target)

For each fixed K, the alternating tail has two-step offspring product 2. Hence m_n at p=1/sqrt(2) is eventually bounded above and below, but infinitely many d_i/m_i terms in C02 are uniformly positive; the critical root survival is zero. For p below/above 1/sqrt(2), the exponential factor makes m_n decay / the reciprocal series converge, respectively, giving that exact p_c. Prefix agreement through K gives rooted local convergence to T_2, whose critical survival is positive by C03. Every graph here fails quasi-transitivity. The claim refutes only the unrestricted local-limit bridge.

## w438-C05 — KEEP (quasi-isometry obstruction outside target)

Contract unary corridors. Their lengths are at most four because f(n+4)-f(n)>1 forces a branch in each four-level window. The resulting branching skeleton is a rooted binary tree. Map each corridor interior to its preceding branching vertex. A tree edge changes image distance by at most one, so d_skeleton(pi u,pi v)<=d_T(u,v); lifting a skeleton geodesic and connecting its endpoints costs at most 4d_skeleton(pi u,pi v)+8. The map is onto. C03 gives equal p_c and opposite critical behavior for beta=0 and beta=2. This is correct for arbitrary bounded-degree graphs; no quasi-transitive invariance statement follows.

## w438-G01 — KEEP as route diagnosis, no theorem

The cited tree recursions depend on disjoint descendant edge sets. On a graph with cycles an exploration cannot multiply branch-success probabilities without a conditional-independence argument. The gap is to derive a finite-scale extinction criterion from quasi-transitivity for subexponential-growth graphs, with conditional exposure control. No such derivation is in the peer packet.

## w439-P0043-boundary-002 — KEEP (uniformity obstruction)

In the L-subdivision of the 3-regular tree, each replaced edge is open with probability p^L, independently across original edges. Thus p_c=2^(-1/L). For fixed n<=L, the three edge-disjoint initial arms each reach ambient distance n with probability p_c^n=2^(-n/L), giving a_L(n)=1-(1-2^(-n/L))^3. It tends to 1 as L grows with n fixed. The supremum is 1; this only excludes graph-independent one-arm bounds.

## w439-P0043-boundary-003 — KEEP (quantitative tree special case)

At p_c each coarse edge is open with probability 1/2. A forward branch reaches k levels with u_0=1 and u_(k+1)=1-(1-u_k/2)^2=u_k-u_k^2/4. The sequence decreases to 0, and 1/u_(k+1)-1/u_k=1/[4(1-u_k/4)] tends to 1/4; Cesaro averaging yields k u_k -> 4. The root has three arms, so q_k=1-(1-u_(k-1)/2)^3 and k q_k ->6; ambient radius is kL, giving (kL)q_k ->6L. There are 3*2^(k-1) original vertices on shell k, each linked to the root with probability 2^(-k), so each shell contributes 3/2 to susceptibility. This verifies the divergence and shows why infinite susceptibility does not imply critical percolation. Countability upgrades root extinction to almost-sure absence of any infinite cluster.

## w439-P0043-source-004 — KEEP as narrow source correction

I queried the exact old store claim `claim_074b08d2f079277d5ce5423b113d46801b9ed62cd7be7598eb47b46fb59b1aeb` in read-only mode. It indeed says Hutchcroft's argument shows susceptibility is finite at p_c "in a spherically-averaged sense" via a branching-random-walk comparison. Hutchcroft (2016), Theorem 2.5 and proof of Theorem 1.3 (journal numbering), instead uses E_p|C(o)|<infinity only for p<p_c, then supermultiplicativity of kappa_p(n), Fekete's lemma and left continuity to transfer the exponential connectivity-rate bound to p_c. The paper does not define the old card's spherical susceptibility or use the asserted killed-branching-random-walk comparison in that proof. On the 3-regular tree, each critical shell contributes expected connected count 3/2, so ordinary critical susceptibility is infinite. **Correction:** replace only the old method description with this source-backed account; do not infer that every form of spherical average is infinite or that the old card's other open-case classifications were checked. This is a source correction, not a new theorem.

## Independent referee limit

All KEEP verdicts above are for boundary lemmas or explicit counterexamples to stronger auxiliary bridges. They do not solve P0043. The single hardest parent gap is a valid critical extinction mechanism for subexponential-growth quasi-transitive graphs, especially intermediate-growth and low-dimensional polynomial-growth cases. No new theorem of my own is offered; w443 is therefore not asked to review a duplicate construction.
