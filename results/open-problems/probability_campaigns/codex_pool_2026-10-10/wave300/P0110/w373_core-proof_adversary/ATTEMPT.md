P0110 adversarial core-proof packet, w373, 2026-10-10

Target and source

The intake entry op-p0110 asks for a nondegenerate iid undirected first-passage-percolation law with well-defined fluctuation and wandering exponents satisfying chi=2xi-1. Its primary source is Auffinger, Damron and Hanson, 50 years of first passage percolation, arXiv:1511.03262v2, Section 4.3, Question 22, equation (4.19). The short primary question is: "Find a distribution of passage times where (4.19) holds." The survey explicitly treats the existence and definition of the exponents as part of the problem. Its older open-status statement does not establish openness in October 2026. Current openness: UNKNOWN; no novelty claim.

A precise sufficient route, not an equivalence to every possible exponent definition

Choose iid Uniform[1,2] edge weights on nearest-neighbor Z^2. Define T(0,v) as the unrestricted minimum passage time, and D(0,v) as the maximum Euclidean distance of its almost surely unique geodesic from [0,v]. This law is continuous, nondegenerate, positive and has finite exponential moments. Chatterjee explicitly includes uniform interval distributions among nearly-gamma laws.

For every epsilon>0 the sought input is the existence of numbers chi,xi and constants alpha_epsilon,K_epsilon,c_epsilon,R_epsilon>0, independent of v, such that:

1. E exp(alpha_epsilon |T(0,v)-ET(0,v)|/|v|^(chi+epsilon)) <= K_epsilon for all nonzero v.
2. E exp(alpha_epsilon D(0,v)/|v|^(xi+epsilon)) <= K_epsilon for all nonzero v.
3. Var T(0,v) >= c_epsilon |v|^(2(chi-epsilon)) when |v|>R_epsilon.
4. E D(0,v) >= c_epsilon |v|^(xi-epsilon) when |v|>R_epsilon.

The four matching estimates imply chi_a=chi_b=chi and xi_a=xi_b=xi in Chatterjee's Theorem 1.1: (1),(2) give the upper thresholds, (3),(4) give the lower thresholds, and the theorem's inequalities chi_b<=chi_a and xi_b<=xi_a squeeze them. That theorem then supplies chi=2xi-1. This implication is a reduction using a published theorem. NONE of the four matching estimates is proved here for Uniform[1,2]. The hardest missing input for this route is simultaneous uniform upper/lower exponent matching for one law. Proving a conditional cylinder comparison does not supply it. The target does not demand the stronger special values 1/3 and 2/3.

Attempt to isolate the fluctuation-scale obstacle

Let s(v)=sqrt(Var T(0,v)). A potential sufficient premise is relative exponential control: for each eta>0, some alpha_eta,K_eta>0 satisfy E exp(alpha_eta |T-ET|/(|v|^eta s(v)))<=K_eta for all nonzero v. If, additionally, for every eta>0 there are positive c_eta,C_eta,R_eta with c_eta |v|^(chi-eta)<=s(v)<=C_eta |v|^(chi+eta) for |v|>R_eta, then taking eta=epsilon/3 gives s(v)|v|^eta<=C_eta |v|^(chi+2epsilon/3). Decreasing alpha absorbs C_eta and gives (1), while the lower scale bound gives (3). The finitely many |v|<=R_eta have exponential moments because T is bounded by the straight-path cost, so they can be included by enlarging K_epsilon. This is a valid conditional implication, not a proof of its relative-tail or uniform-scale premises. A corresponding relative bound for D at its mean scale plus matching mean powers would give (2),(4), again conditional.

Obstruction A: variance scaling does not yield exponential-tail scaling

INDEPENDENT.md was saved before the paired proof was read. Its explicit centered four-point family has Var X_n=(1-1/n)n^(2/3)+n^(1/3), lower variance exponent 1/3 and upper exponential-moment exponent 2/3. Rare values of magnitude n^(2/3), occurring with probability 1/n, are invisible to the leading variance scale but dominate every exponential moment normalized by n^a for a<2/3. This refutes only the estimate-to-estimate inference; it is not an FPP environment. The analytic all-n argument, rather than a finite fitted exponent, establishes the mismatch.

Obstruction B: selecting a geodesic couples initially independent corridors

Take a finite four-edge square graph with endpoints at opposite corners and iid Uniform[1,2] weights. Its two path costs A and B are independent, identically distributed, continuous sums of two uniforms, with median m=3. The top path is uniquely optimal on E={A<B}, with P(E)=1/2. Let L={A<=m}, H={B>=m}. Independence gives P(L and H)=1/4; this entire quadrant is contained in E up to null boundaries, so P(L and H|E)=1/2. Within {A<=m,B<=m}, exchangeability splits the total probability 1/4 equally across A<B and B<A. Thus P(L and E)=1/2-1/8=3/8, so P(L|E)=3/4. By the same argument P(H|E)=3/4. Their conditional product is 9/16, whereas their true conditional joint probability is 1/2. Error: 1/16. All edge weights are iid and continuous and the two routes use disjoint edges. The failure is conditioning on the winning route. This says nothing against independence of restricted passage times in disjoint DETERMINISTIC edge sets, computed without conditioning on a selected path. It is not a counterexample on the full lattice.

Obstruction C: the small-endpoint wandering quantifier matters on the actual candidate law

On the full nearest-neighbor Z^d, d>=2, with every edge weight in [1,2], the direct edge 0--e1 costs at most 2. Every other simple path from 0 to e1 has at least three edges (the lattice is bipartite), so costs at least 3. Positive weights eliminate loops from a minimizing path. Therefore the direct edge is always the unique geodesic and D(0,e1)=0. For every real b, inf_{v!=0} ED(0,v)/|v|^b=0. Consequently an all-nonzero-endpoints positive wandering lower bound is impossible for Uniform[1,2], although Chatterjee's large-distance version is not contradicted. Auffinger-Damron display an all-nonzero-endpoints infimum in (2.2); importing that literal formulation for this law needs an asymptotic adaptation, not an assertion that its hypotheses hold. This is a quantifier warning about applying a sufficient theorem, not a refutation of the theorem or of KPZ.

Obstruction D: high-probability agreement is insufficient for variance transfer

Let T_n=n deterministically and Y_n=n+nB_n where B_n is Bernoulli(1/n), n>=2. They lie in [n,2n], agree with probability 1-1/n, yet Var T_n=0 and Var Y_n=n-1; their L2 discrepancy is sqrt(n). Thus equality on a probability tending to one does not imply that variances are asymptotically equal. This is an abstract counterexample to a transfer inference, not an iid-FPP realization. In a bounded-law cylinder transfer, one needs a quantitative L2 error small relative to the actual passage-time standard deviation. A sufficient localization comparison of the form n^2 P(T_C!=T)=o(Var T) is a separate input. Merely knowing that a geodesic stays in a cylinder with probability tending to one does not supply it.

Measured checks

Run python -X utf8 ~/brain_workers/w373/check_obstructions.py. verification.json records exact finite-state checks and a stable log-moment computation. These checks corroborate the written arguments and quantify the incorrect independence prediction versus exact conditioning; they are not a formal proof receipt, an independent referee decision or a measurement of live-brain improvement.

Referee and unresolved work

Named independent reviewer: w374. REFEREE_RECEIPT.json records KEEP verdicts for the four scoped probability/endpoint obstructions and the paired L2/L4 reductions. The norm countermodel and the sufficient-route reduction row remain pending. w377 independently reviews w374's own new results. No theorem has been promoted to the live store. The paired prover's named lane is unconditional cylinder variance transfer; this packet supplies adversarial cases and does not claim that lane's lemma. Read and audit the concrete paired artifact when present, preserving its localization hypothesis.

NEXT: Obtain w374's decisions on the norm countermodel and sufficient-route reduction; the next proof input is a positive quantitative mean gap for the actual iid law, with an L2 localization error small relative to sqrt(Var T).
