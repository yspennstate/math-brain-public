# Independent derivation, saved before reading w384's proof

Worker w385, 2026-10-10. Source context: Ahlberg–Hoffman, arXiv:1609.02447, Theorem 2.1 and assumption A1; Dembin–Elboim–Peled, DOI 10.1007/s00039-024-00672-z, Theorems 1.2–1.3 and the discussion immediately after Theorem 1.3. No paired proof has been read.

## Exact finite witness reduction

Fix a configuration of finite nonnegative edge weights on the nearest-neighbor graph Z^2. Define T(u,v) as the infimum of weights of finite paths joining u to v. A geodesic here is a simple finite path attaining T(u,v); a bigeodesic is an injective nearest-neighbor path indexed by Z, every finite segment of which attains the corresponding T.

Let S_n={v: ||v||_infinity=n}, and let E_n be the event that some distinct u,v in S_n have a simple geodesic between them containing 0. The geodesic is allowed to leave the box. Then E_(n+1) is contained in E_n: start at 0 along each arm of a witnessing path, stop at its first visit to S_n, and take that subpath. Subpaths of a nonnegative-weight minimizing path minimize. Its two endpoints are distinct because the original path is simple.

The event that a bigeodesic contains 0 is exactly the intersection of E_n for all n. The forward implication uses the first shell hit in both directions. For the converse, choose a witness for each n and orient it by a fixed ordering of its two neighbors of 0. Each arm has at least n edges. For a fixed m, the centered 2m-edge segment has finitely many possibilities because the graph is locally finite. Successively select an infinite subsequence on which each centered segment stabilizes, and take the compatible union. The limit is injective: every pair of its vertices appears together in one simple finite witness. Every finite segment minimizes because it is eventually an identical subpath of witnesses in the unchanged configuration. Both arms are infinite. This proves the equivalence without a direction limit, moment condition, curvature condition, independence, or uniqueness assumption.

All E_n are measurable under a law on configurations: they are countable unions of equalities between a finite path sum and the countable infimum defining T. Hence P(0 lies on a bigeodesic)=lim_n P(E_n) by continuity from above. For a translation-invariant law, no bigeodesic anywhere follows exactly when this limit is zero, by a countable union over possible visited vertices.

## Hardest missing input in this route

Under iid atomless finite nonnegative weights with E[min(t_1,t_2,t_3,t_4)^2]<infinity, prove P(E_n)->0. The compactness reduction is elementary; this probability decay is the open input, not a consequence already established here.

The shell has 8n vertices. If q_n=max_{distinct u,v in S_n} P(0 lies on Geo(u,v)), then P(E_n)<=min(1, binomial(8n,2) q_n). Ahlberg–Hoffman's all-deterministic-sequences conclusion implies q_n->0 by selecting a maximizing deterministic pair at every n. It gives no rate sufficient for this union bound. The formal sufficient condition q_n=o(n^(-2)) is not viable under A1: the lower-bound derivation below shows that even q_n=o(n^(-1)) is impossible. Bounds controlling the union directly could suffice at a much slower marginal rate.

With the additional distributional and shape assumptions of Dembin–Elboim–Peled Theorem 1.2, the quoted marginal bound has exponent 1/16. Substitution yields a bound of order n^(31/16) log^2(n), capped at 1. It does not make P(E_n) vanish. Theorem 1.3 controls a restricted family of horizontal equal-height endpoints; arbitrary bigeodesic endpoints need not belong to that family.

## Independent candidate obstruction to endpoint selection

Let U be uniform on [0,1), M_n=2^n, J_n=floor(M_n U), and A_(n,k)={J_n=k} for 0<=k<M_n. Every P(A_(n,k))=1/M_n; their union is the full probability space at every n. Even conditionally on all coarser partitions, J_n is uniformly distributed among compatible refinements. However P(A_(n,J_n))=1. The indexed events are measurable; lack of measurability is not the reason for the failure. A uniform bound for deterministic indices cannot be substituted into a sample-selected index. This is an abstract inference counterexample, not an iid-FPP bigeodesic construction.

Minimal repair: prove a direct bound for E_n, or a conditional bound for each proposed selector given a sigma-field that makes that selector measurable, or a valid finite-cover estimate with its entropy paid. Merely claiming endpoint measurability, uniform deterministic estimates, or an arbitrarily dense direction net is insufficient.

## Further independent obstruction: the maximum-pair union route cannot work

This addition was saved before reading w384's proof route. Assume A1, so geodesics are almost surely unique and the deterministic time constant mu is a norm. Write c_star=min_{||x||_infinity=1} mu(x)>0, c=c_star/2, and K=2 mu(e_1)+1. Fix an integer C>=2 with cC>K. Let a_n=(-n,0), b_n=(n,0), and gamma_n=Geo(a_n,b_n).

By the radial shape theorem and translation invariance, P(T(a_n,b_n)<=Kn)->1. By the uniform shape theorem and translation invariance, with probability tending to one, T(a_n,w)>=c ||w-a_n||_infinity for every w with ||w-a_n||_infinity>=Cn. These two events need not be independent; their intersection G_n still has probability tending to one by the union bound on their complements.

On G_n no vertex w of gamma_n can satisfy ||w-a_n||_infinity>=Cn: its prefix is a geodesic, so T(a_n,w)<=T(a_n,b_n)<=Kn, whereas the lower bound would give T(a_n,w)>=cCn>Kn. The path must cross the line x=0 at some (0,y) with |y|<=Cn. Consequently

  sum_{y=-Cn}^{Cn} P((0,y) lies on Geo((-n,0),(n,0))) >= P(G_n)=1-o(1).

Translation invariance equates each summand to P(0 lies on Geo((-n,-y),(n,-y))). Both of these endpoints lie in S_r for r=max(n,|y|), hence each summand is at most q_r. Therefore

  (2n+1) q_n + 2 sum_{r=n+1}^{Cn} q_r >= 1-o(1).             (LB)

In particular, for all large n some r in [n,Cn] obeys q_r>=1/(2(2Cn+1))>=1/(6Cr). The r so obtained are unbounded. Thus q_r is not o(1/r), and especially cannot be o(1/r^2). Along that unbounded subsequence the raw upper bound min(1,binomial(8r,2)q_r) is exactly 1 for sufficiently large r. Seeking better maximum-pair estimates alone cannot make this raw shell union bound prove no bigeodesics. This is an obstruction to that argument, not positive probability of E_n and not existence of a bigeodesic.

Every dependency is explicit: existence and uniqueness, stationarity, a positive norm time constant, and the uniform/radial shape theorem. Neither independence of the two shape events nor strict curvature is used. The source supplies these A1 inputs; the crossing/counting deduction is written here for independent referee verification.

## Further independent consequence: potential bigeodesic arms have direction limits

This addition was also saved before reading w384's proof route. Under Ahlberg–Hoffman A1, choose a deterministic countable dense set D of differentiability directions of the deterministic limit shape. Such a set exists because a planar convex body's boundary has at most countably many nondifferentiable points. For each d in D, Theorem 2.2(b) excludes a bigeodesic having d in its direction set. Intersect these countably many probability-one events.

For an injective nearest-neighbor ray (v_k), every bounded vertex set is visited finitely often, so |v_k| tends to infinity. Consequently the successive differences of v_k/|v_k| tend to zero. Its cluster set C in the unit circle is nonempty, compact, and connected: if C split into two disjoint compact pieces, take disjoint neighborhoods with positive separation. Infinitely many transitions between the neighborhoods and vanishing step sizes force infinitely many points outside both; a convergent subsequence gives a cluster point outside C, a contradiction. A connected subset of the circle with two distinct points contains a nonempty open arc and hence a point of D. Therefore either arm of a potential bigeodesic, on the simultaneous probability-one event above, has a singleton cluster set and thus a direction limit.

This excludes wandering direction arcs, not bigeodesics themselves. The two singleton limits can depend on the environment and need not be captured by D. Nor is antipodality of those limits proved here: a nonsmooth norm can have equality in its triangle inequality for noncollinear vectors. The outstanding all-direction or all-endpoint exclusion remains explicit.

NEXT: audit w384's candidate and the recent primary manuscript's selector/label step against these independently saved reductions.
