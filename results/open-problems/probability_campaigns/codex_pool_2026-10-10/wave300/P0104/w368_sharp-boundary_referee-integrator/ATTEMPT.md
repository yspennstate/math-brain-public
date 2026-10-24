# P0104 referee derivation, 2026-10-10

The source target is Question 13 of Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, printed p.36. It asks for a fluctuation exponent below 1/2 in every dimension at least 2 under suitable edge-law conditions, and value 1/3 in the plane. The survey does not fix the exact exponent definition or admissible law class. Neither lemma below solves that question.

## Independent check of w366-C1

For any fixed integer n>=1 on the undirected square lattice, use the four deterministic routes from 0 to (n,0): the direct axis; the rows y=1 and y=-1 with vertical connectors; and the route left one, up two, right n+2, down two, left one. They have respectively n, n+2, n+2, n+8 edges. Their *edge sets*, including first and last edges, are pairwise disjoint. The direct route uses the east edge at the origin, upper the north edge, lower the south edge, and outer the west edge. At the endpoint they again use four distinct incoming edges. All intermediate horizontal rows or vertical columns differ. Program `reproduce.py` checked the 32 cases n=1..32; this finite check corroborates the explicit general geometry.

Set q(t)=P(tau_e>t), M=min of the four origin incident weights, and S_j the route sums. Every path has first-edge weight at least M, so T>=M even if the passage-time infimum is not attained. Since T<=min_j S_j, the event T>t implies every S_j>t. If S_j>t, at least one of its l_j nonnegative summands exceeds t/l_j. Each route sum depends on an edge set disjoint from the other three, so the events S_j>t are independent; no conditional or adaptive-product step is used. Therefore

    q(t)^4 = P(M>t) <= P(T>t)
       <= product_j [l_j q(t/l_j)] <= n(n+2)^2(n+8) q(t/(n+8))^4.

Integrating r t^(r-1) times the tail for r>0, with infinite values allowed, gives E[M^r] <= E[T^r] <= K(n+8)^r E[M^r]. Thus finiteness is equivalent for each *fixed* n. A Pareto tail q(t)=t^(-alpha) for t>=1 gives E[T^r]<infinity iff r<4alpha. At alpha=1/2 the fixed-endpoint mean is finite and variance infinite. No n-uniform fluctuation conclusion follows: K is order n^4 and the upper moment factor contains (n+8)^r.

Verdict: KEEP as an independently checked fixed-endpoint moment lemma. Its novelty and original priority are not asserted. The hardest open piece remains a bound on centered fluctuations as n grows for a fixed admissible law.

## Independent check of w367-C001 and C002

For 0<a<b and weights in [a,b], every path from 0 to n e1 has at least n edges. Only the straight path has exactly n edges. The square lattice is bipartite, so any other finite walk has at least n+2 edges. Its cost is at least (n+2)a, while the straight route costs at most nb. Hence n(b-a)<=2a makes T equal to the straight sum for every configuration, including at equality. If endpoints a,b are essential endpoints and n(b-a)>2a, choose delta>0 satisfying n(b-delta)>(n+2)(a+delta). On the positive-probability event that all straight edges exceed b-delta and all edges on the disjoint upper detour are below a+delta, the detour beats straight. This proves sharpness of the *configuration-uniform* sufficient threshold.

For iid Uniform[1,1+epsilon] with n epsilon<=2, T is a sum of n independent uniforms, so E T=n(1+epsilon/2) and Var T=n epsilon^2/12. At threshold equality, another path can tie only if straight edges attain the upper endpoint and detour edges attain the lower endpoint; the continuous law assigns probability zero, and there are countably many finite paths. To refute a power estimate uniform over laws *after normalization by edge variance*, suppose a constant C and a law-independent onset N satisfy Var_F T <= C Var_F(tau_e) n^theta for every epsilon in (0,1] and all n>=N, with theta<1. Choose n>N so n^(1-theta)>C and set epsilon=1/n. The exact straight-path regime applies, and division by Var_F(tau_e)>0 gives n<=C n^theta, contradiction. At theta=2/3 the ratio is n^(1/3), equal to 10 at n=1000 in `reproduce.py`.

Verdict: KEEP both statements at their explicit scopes. The counterexample addresses a *law-uniform normalized estimate*, not a law-dependent KPZ exponent. It does not imply that any one fixed F has diffusive asymptotics.

## Remaining gap

The single hardest load-bearing step is controlling the unrestricted optimization over detours as n tends to infinity for one fixed planar law, to obtain a polynomial power saving and matching lower bound for its centered passage-time fluctuations. The finite straight-path window ends by n about 2/epsilon for Uniform[1,1+epsilon]; the fixed-endpoint moment criterion does not supply a rate in n. Basu--Sidoravicius--Sly arXiv:2604.01214 gives a power saving for a rotationally invariant Riemannian model; transferring the needed geometry and chaos estimates to iid lattice FPP is still unproved in the inspected record. No full proof, novelty claim, or formal-check receipt is asserted.

## Additional final-artifact checks

w366-C2 is an immediate exact corollary of C1: the minimum of four independent Pareto variables with tail t^(-alpha) has tail t^(-4alpha), whose r-th layer-cake integral converges precisely for r<4alpha. At alpha=1/2 its mean is finite and second moment infinite. w366-C3 and C4 are the square-lattice versions of the independently derived w367-C001/C002; their explicit positive delta satisfies the strict detour inequality, so both receive KEEP but no duplicate brain entry.

w366-C5 adds a sharp chaos boundary. Under iid weights in [1,1+epsilon] with n epsilon<2, both original and independently delta-refreshed environments have the same unique straight geodesic, so overlap is exactly n. For one edge, write tau_delta=(1-B)tau+B tau' with independent Bernoulli(delta) B and independent copy tau'. Then Cov(tau,tau_delta)=(1-delta)sigma^2. Independent edge pairs along the straight path imply Cov(T,T_delta)=(1-delta)n sigma^2 and E[(T-T_delta)^2]=2 delta n sigma^2. This remains true at delta=1. The changed-law choice epsilon=1/n obstructs only estimates whose prefactor and onset are uniform over edge laws.

w367-C003 gives a necessary constant/onset tradeoff for a *fixed* Uniform[1,1+epsilon] law. Put K=floor(2/epsilon). If a bound Var(T_n)<=C Var(tau)n^theta holds for every n>=N and N<=K, evaluate at n=K, where T is the straight sum. This forces C>=K^(1-theta). Thus either the onset exceeds K or the prefactor grows by that amount. This is a necessary condition, not an asymptotic solution.
