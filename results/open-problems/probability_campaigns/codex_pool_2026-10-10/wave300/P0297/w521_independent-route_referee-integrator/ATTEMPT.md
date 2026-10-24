# P0297 independent route (recorded before reading w519/w520 arguments)

## Precise target

For gamma in (0,2), determine the exact deterministic number d_gamma = dim_H(C,D_h), with D_h the gamma-LQG metric of Gwynne--Miller. The paper gives xi_gamma=gamma/d_gamma and poses this as Problem 7.1. The gamma=sqrt(8/3) value 4 is a known special case.

## Route: uniform quantum-mass ball scaling

Use the gamma-LQG area measure mu_h and its masses of D_h-balls on a compact internal region K. If one could identify an explicit f(gamma) and prove simultaneous, all-center bounds r^{f(gamma)+epsilon} <= mu_h(B_D(z,r)) <= r^{f(gamma)-epsilon} for every z in K and all sufficiently small r (with constants depending on K, epsilon and the sample), then standard covering and mass-distribution arguments give dim_H(K,D_h)=f(gamma). Exhaust K to obtain dim_H(C,D_h)=f(gamma). This bypasses direct LFPP passage-time exponent identification. The conditions are much stronger than mu_h-almost-everywhere ball scaling; exceptional points and geodesic bottlenecks matter for the whole-plane dimension.

The missing load-bearing estimate is a uniform, explicit exponent for metric-ball area across all centers and scales. No such estimate is asserted here. The established d_gamma ball-volume exponent simply restates the unknown if f(gamma)=d_gamma. The proposed route is a conditional reduction, not a solution.

Conditional covering proof on a compact metric space (submitted to w524 for audit): Assume a probability mu and, for every epsilon in (0,d), constants c_epsilon,C_epsilon,r_epsilon>0 such that c_epsilon r^(d+epsilon) <= mu(B_D(x,r)) <= C_epsilon r^(d-epsilon) for all x and r<r_epsilon. A maximal r-separated set has disjoint open r/2-balls, each of mass at least c_epsilon(r/2)^(d+epsilon); there are at most its reciprocal many. Its r-balls cover X, giving dim_H X <= d+epsilon. Conversely, every small-diameter set is inside a ball of that diameter centered at one of its points; the upper mass bound and mu(X)=1 show every cover has (d-epsilon)-cost at least 1/C_epsilon. Thus dim_H X >= d-epsilon. Let epsilon down to zero. The all-center assumption is the unproved part in LQG.

## Referee checkpoint

Before accepting any peer derivation, verify that it controls the full metric-space Hausdorff dimension, not only typical mu_h-points, discrete map volume, or a single special gamma. Require a uniform all-scale covering argument or a published theorem that bridges the discrepancy.
