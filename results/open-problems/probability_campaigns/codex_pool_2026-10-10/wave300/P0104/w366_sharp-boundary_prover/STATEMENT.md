# P0104 boundary lane: statement for independent adversary

Assigned historical target: "Subdiffusive and KPZ passage-time fluctuation exponents", ranking 2026-09-07, tier 5. The canonical P0104 card maps it to Questions 13 and 15 of Auffinger-Damron-Hanson, arXiv:1511.03262v2. These ask for chi<1/2 for d>=2 under suitable F conditions, chi=1/3 in d=2, and chi>0 in suitable dimensions. The suitable hypotheses and asymptotic scaling convention are not fixed by that question. Present openness is UNKNOWN. This file makes no novelty or full-solution claim.

Narrow lane claimed by w366: the upper-tail/moment boundary for point-to-point passage times, avoiding other groups' central fluctuation computations.

Statement to test independently: for iid finite almost surely nonnegative edge weights on the undirected nearest-neighbour square lattice, n>=1 and r>0, the r-th moment of T(0,n e1) is finite exactly when the r-th moment of the minimum of four iid edge weights is finite. In particular, for a continuous Pareto law on [1,infinity) with tail P(t_e>t)=t^(-alpha) for t>=1, E[T(0,n e1)^r] is finite exactly when 4 alpha>r. At alpha=1/2, all these fixed-endpoint passage times have a finite mean and infinite variance.

Scope: this only refutes any unqualified extension of a variance-based KPZ claim to all iid finite almost surely weights. It does not refute the KPZ conjecture under suitable moment assumptions. Independent adversary w367 is asked to inspect this statement before receiving the proof.

Second independent statement: for any edge-weight assignment in [1,1+epsilon] on the same lattice, T(0,n e1) equals the straight-path sum whenever n epsilon<=2. For iid Uniform[1,1+epsilon], Var(T)=n epsilon^2/12 throughout that window. If n epsilon>2, there is positive probability that a length-(n+2) detour beats the straight path, so the deterministic window boundary is sharp. Consequently no finite C, independent of the law and n, can satisfy Var_F(T(0,n e1))<=C Var_F(t_e) n^beta for every epsilon>0 and n>=1 when beta<1. The law is allowed to vary with n in this last obstruction; it does not negate an asymptotic result for each fixed law.

Resampling corollary to inspect: when n epsilon<2 the geodesic is the same deterministic straight path before and after any independent edge refresh. Its overlap is exactly n, even under full refresh. With refresh probability delta, Cov(T,T^delta)=(1-delta)n Var(t_e), and E[(T-T^delta)^2]=2 delta n Var(t_e). Thus an overlap power saving cannot be uniform over these laws at a common starting scale.
