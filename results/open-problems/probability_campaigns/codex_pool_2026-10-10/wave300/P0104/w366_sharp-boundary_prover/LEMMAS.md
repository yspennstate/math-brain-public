# Fixed-endpoint moment boundary for planar first-passage percolation

## C1

All edges of the undirected nearest-neighbour square lattice carry iid finite almost surely nonnegative weights with law F. Fix n>=1. Let T=T(0,(n,0)) be the infimum of the sums over all finite connecting paths. Let M be the minimum of the four edges incident to 0. No geodesic existence is required.

Use four paths, listed by their turning vertices; between turns use the straight lattice segment:

1. (0,0), (n,0).
2. (0,0), (0,1), (n,1), (n,0).
3. (0,0), (0,-1), (n,-1), (n,0).
4. (0,0), (-1,0), (-1,2), (n+1,2), (n+1,0), (n,0).

Their lengths are n, n+2, n+2, n+8. Their undirected edge sets are pairwise disjoint (shared vertices cause no dependence). Write their sums as S_j and their lengths as l_j; put L=n+8 and K=product(l_j)=n(n+2)^2(n+8). With q(t)=P(t_e>t), nonnegativity gives T>=M. Also T<=min_j S_j. If S_j>t, some edge on that path has weight >t/l_j. Hence

    q(t)^4 = P(M>t) <= P(T>t)
    <= product_j P(S_j>t)
    <= product_j [l_j q(t/l_j)]
    <= K q(t/L)^4 = K P(M>t/L).

The product of path-sum probabilities is justified by iid weights on disjoint deterministic edge sets. It is not a product of conditional or adaptively chosen estimates.

For r>0, apply the layer-cake formula E[X^r]=r integral_0^infinity t^(r-1) P(X>t) dt, allowing infinity. The bounds yield

    E[M^r] <= E[T^r] <= K L^r E[M^r].

This proves the claimed equivalence, including at divergent endpoints. Constants depend polynomially on n and do not yield a fluctuation exponent.

Independent review: requested from w368, pending. This is an elementary proof of a known-type moment criterion; novelty is not claimed.

## C2: exact heavy-tail threshold

For a continuous Pareto edge law supported on [1,infinity), q(t)=t^(-alpha) for t>=1 with alpha>0, the minimum M in C1 has q_M(t)=t^(-4 alpha). Its r-th moment is finite exactly when 4 alpha>r, by integrating t^(r-1-4 alpha). C1 transfers the same exact threshold to T for each fixed n. At alpha=1/2 the mean is finite and the second moment diverges logarithmically; since the mean is finite, Var(T)=infinity. At alpha=1/4 even the mean diverges. These weights are continuous, positive and finite almost surely. The counterexample only addresses statements lacking suitable moments.

## C3: sharp finite window for bounded weights

Let epsilon>0 and n>=1. For every assignment of weights in [1,1+epsilon], the horizontal straight path has passage sum S<=n(1+epsilon). Every other finite path has length at least n+2: the bipartite lattice gives the same parity as n, and the sole length-n path from 0 to n e1 is the straight one. Each edge costs at least 1, so every other path has passage sum >=n+2. Thus n epsilon<=2 implies T=S. Loops cannot improve the conclusion since weights are positive. For iid Uniform[1,1+epsilon], independence of the deterministic straight edges gives Var(T)=n Var(t_e)=n epsilon^2/12.

Sharpness: if n epsilon>2, put delta=min(epsilon/4,(n epsilon-2)/(4n+4))>0. Consider the event that all n straight edges exceed 1+epsilon-delta, while all n+2 edges of the upper one-unit dogleg lie below 1+delta. The two paths have disjoint edge sets. The event has probability (delta/epsilon)^(2n+2)>0. On it the difference between their costs is greater than

    n(1+epsilon-delta) - (n+2)(1+delta)
    = n epsilon - 2 - (2n+2)delta > 0.

So T<S with positive probability beyond the threshold. At equality n epsilon=2 the passage-time identity T=S still holds, whether or not a deterministic extremal environment has ties.

## C4: obstruction to a variance bound uniform over edge laws

Fix beta<1. Suppose a finite C independent of epsilon and n made Var_F(T(0,n e1))<=C Var_F(t_e) n^beta for every Uniform[1,1+epsilon] law and every n>=1. Choose epsilon=1/n. Then C3 applies (n epsilon=1), Var_F(t_e)>0 and cancellation gives n^(1-beta)<=C for every n, impossible. More generally, a proposed common starting scale n0 also fails by choosing n>=n0 arbitrarily large. Distribution dependence must occur in a prefactor, a starting scale, or another parameter of such an estimate.

Quantifier warning: epsilon=1/n changes the law as n changes. This does not refute the per-law asymptotic assertion Var_F(T)=n^(2/3+o(1)) for any fixed F. It only rules out this stronger uniform bridge. No asymptotic exponent was proved here.

## C5: exact resampling behavior before the detour scale

Assume iid weights in [1,1+epsilon] of variance sigma^2, with n epsilon<2. The strict comparison in C3 gives the unique straight geodesic in every environment. Independently refresh each edge with probability delta in [0,1], replacing it by an independent copy of its original law. The new environment has the same support, so its geodesic is the same deterministic n-edge path. Therefore the overlap is exactly n, even under full refresh (delta=1).

For a straight edge e let B_e be its independent Bernoulli(delta) refresh indicator and t'_e its independent copy. Then t_e^delta=(1-B_e)t_e+B_e t'_e, and Cov(t_e,t_e^delta)=(1-delta)sigma^2. Different edges' pairs are independent. Summing along the deterministic straight path yields

    Cov(T,T^delta) = (1-delta)n sigma^2,
    E[(T-T^delta)^2] = 2 delta n sigma^2.

This is a precise obstruction to a geodesic-overlap power saving with a prefactor and a starting scale both uniform over bounded edge laws: take epsilon=1/n. It is compatible with law-dependent chaos estimates beyond a law-dependent scale. This statement uses strict n epsilon<2 to avoid tie conventions.
