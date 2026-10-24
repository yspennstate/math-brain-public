# C0120: statement-only handoff (2026-10-10)

Original cited question: Chatterjee, arXiv:0810.4221v2, Section 12 question (3), printed p.59, asks for a better fluctuation exponent than the logarithmic correction in his directed-polymer model. Sections 1 and 8 specify i.i.d. standard Gaussian weights g_v on Z_+^2, directed up/right paths p=(v_0,...,v_{n-1}) starting at the origin, and M_n=max_p sum_{v in p} g_v. The endpoint is free. Theorem 8.1 gives Var(M_n)<=C n/log n. The concrete power-improvement target is: find epsilon>0 and C<infinity independent of n such that Var(M_n)<=C n^(1-epsilon) for all n>=2.

Intake formulation: problems.jsonl row 120 changes this to Var(log Z_n) for general-dimensional positive-temperature polymers. That is a related target; it is not the exact observable or dimension in the cited theorem. This discrepancy needs a source/status correction, not silent identification of the models.

Related independently sourced formulation: Alexander-Zygouras, arXiv:1204.1819v2, Theorem 1.1, defines Z_N=E_walk exp(beta sum_{i=1}^N omega_{i,S_i}), S simple symmetric nearest-neighbor walk on Z^d starting at 0, endpoint free, fixed d>=1 and beta>0. Disorder is i.i.d., mean zero, nearly gamma with integral exp(4 beta |omega|) nu(d omega)<infinity. Nearly gamma means an interval support, continuous density h, CDF H, and phi(Phi^(-1)(H(y)))/h(y)<=sqrt(B+A|y|) for constants A,B>=0 throughout the interior. Their exponential concentration at sqrt(N/log N) implies Var(log Z_N)=O(N/log N). Gaussian disorder meets these assumptions.

Present openness of either target: UNKNOWN. A bounded primary-literature search has not certified present openness, and solvable last-passage models or changing beta with N do not settle fixed-beta general disorder.

Independent adversary: w502. Referee: w503. Requested task: first inspect this statement and assumptions without reading w501's proof packet; independently identify an obstruction or a useful bridge. No proof argument appears in this file.

Primary links: https://arxiv.org/html/0810.4221 ; https://arxiv.org/html/1204.1819v2 .
