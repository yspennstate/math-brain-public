# P0050: an l2 marginal-gap criterion without a symmetry action

Label: proof of a sufficient criterion, pending w347. The condition is not established for every pair of distinct free and wired forest measures.

Let E={e_1,e_2,...} be countable and let mu,nu be laws on {0,1}^E. Assume indicators are pairwise negatively correlated under each law. Let delta_i=E_mu X_i-E_nu X_i>=0. If sum_i delta_i^2=infinity, then mu and nu are mutually singular. No invariant group action or ergodicity assumption is needed.

Proof. For S_N=sum_{i<=N} delta_i X_i and D_N=sum_{i<=N} delta_i^2, the difference of expectations is D_N. Nonnegative weights and nonpositive off-diagonal covariances imply

    Var_mu(S_N), Var_nu(S_N) <= sum_i delta_i^2 Var(X_i) <= D_N/4.

Let t_N be the midpoint of the two means. Chebyshev gives mu(S_N<=t_N)<=1/D_N and nu(S_N>t_N)<=1/D_N. Choose increasing N_j with D_{N_j}>=2^j. Both error sums are finite. The first Borel-Cantelli lemma therefore makes the measurable event "S_{N_j}>t_{N_j} for all sufficiently large j" have mu-probability one and nu-probability zero. This is mutual singularity.

This applies conditionally to free/wired spanning-forest indicators when their marginals are ordered and both indicator laws have negative pairwise correlations. The unresolved part is whether distinct forest laws on an arbitrary network must have a divergent squared marginal gap, or can be distinguished by another statistic. No converse is asserted. A constant positive gap on infinitely many edges is an immediate special case; the criterion also allows gaps tending to zero provided their squares are not summable.

Why the hypotheses matter. Two independent product Bernoulli laws that agree with parameter 1/2 on every coordinate except the first, where their parameters are 3/5 and 2/5, are distinct and satisfy the correlation and ordering assumptions but are equivalent, not singular. The density dmu/dnu is 3/2 when X_1=1 and 2/3 when X_1=0. Their squared marginal gap is 1/25, finite. Thus distinctness and negative correlation alone cannot complete the argument.

Prior attempt quoted: "This handles forest laws admitting such an ergodic common action. Arbitrary networks may lack it". The new criterion supplies a route without that common action and states its remaining measurable obstruction explicitly.
