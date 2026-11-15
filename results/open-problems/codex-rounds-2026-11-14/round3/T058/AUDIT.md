# Audit of the adjacent-count calculation

## Independent checks of the leading terms

For the covariance endpoint, first count contained pairs by starting with an independent k-set and deleting one vertex. There are k such subsets, giving k mu_k expected pairs. Alternatively start with an independent (k-1)-set B. Each of the n-k+1 remaining vertices extends B independently of its internal edge constraints with probability 2^(-(k-1)). This gives mu_(k-1)(n-k+1)2^(-(k-1)). The two expressions agree by the exact consecutive-binomial identity. For each pair the product of marginal probabilities is q_(k-1) times its joint probability. Its covariance is therefore its joint probability times (1-q_(k-1)). This independently gives the endpoint term k mu_k(1-q_(k-1)).

The exact mean ratio is also obtained by double-counting all pairs (B,v) with |B|=k-1 and v outside B: binom(n,k) k = binom(n,k-1)(n-k+1), and the additional edge constraints have probability 2^(-(k-1)). There is no missing factor k or factor two.

For the correlation constant, the leading covariance divided by the two leading standard deviations is k sqrt(mu_k/mu_(k-1)). Its square equals k(n-k+1)/2^(k-1). Independently, exponentiating the definition of f gives 2^(k-1)=(e^2/4)2^(-t)n^2/(log_2 n)^2. Substitution of k~2 log_2 n gives (8/e^2)2^t(log_2 n)^3/n. Its positive square root is exactly the coefficient in PROOF.md. All covariance summands are nonnegative, fixing the sign of that root.

The least-squares conclusion follows from completing a scalar quadratic, independently of any distributional approximation. A correlation tending to zero removes only the fraction rho^2 of the variance in the best affine predictor. It does not exclude nonlinear dependence.

## Hand calculation for all graphs on six vertices

X_2 counts missing edges, so Var(X_2)=15/4.

For X_3, the diagonal contribution is 20*(1/8)*(7/8)=140/64. There are 20*3*3=180 ordered pairs of triples overlapping in two vertices. Each contributes 1/32-1/64=1/64. Thus Var(X_3)=320/64=5.

For Cov(X_3,X_2), only containment contributes. There are 20*3=60 pairs and each contributes (1/8)*(1-1/2)=1/16. The total is 15/4.

For Cov(X_4,X_3), containment contributes 15*4*(1/64)*(1-1/8)=420/512. Intersection of size two contributes 15*6*2*(1/256-1/512)=180/512. The total is 600/512=75/64.

For Var(X_4), the diagonal contributes 945/4096, the 120 ordered pairs overlapping in three vertices contribute 840/4096, and the 90 ordered pairs overlapping in two contribute 90/4096. The sum is 1875/4096. These hand values agree with exhaustive graph enumeration and exact overlap sums.

## Bounds and cases checked

Sets sharing zero or one vertex depend on disjoint edge variables, so their covariance is exactly zero. Counting them as dependent would produce spurious dominant terms. The proof removes them before bounding anything.

Equal sets are included in the variance diagonal. Fully contained adjacent sets are included in the mixed covariance endpoint. Both matter: omitting the latter would lose the actual leading covariance. The midpoint split covers every other j exactly once, and the enlarged high-overlap range is used only for an upper bound by positive terms.

For both bounding sequences, the logarithm is a convex quadratic with positive second derivative. Their middle endpoints have base-two logarithm -u^2/2+O(u log u), whereas the outer endpoints have logarithms of order -u. Thus the middle is smaller eventually; the assertion does not require monotonicity of the exact overlap terms, which can fail near full overlap. audit_extension.py checks the two resulting inequalities exactly at the larger test values.

The phase condition is essential to this proof: it supplies mu_(k-1) <= n^(2-delta+o(1)), making mu_(k-1)k^5/n^2 vanish. The argument does not establish the claimed moment asymptotics uniformly as the upper phase endpoint tends to one. Integer jumps of k do not cause a gap, since each allowed integer is estimated with its own k and t. The double-precision target phases in verify_moments.py differ slightly from their targets at small n; those are formula diagnostics, not assertions that every rounded sample belongs to the closed band. The independent larger audit uses Decimal inversion.

## What the checks do and do not show

The earlier density constants were rederived from a recurrence and their enumeration and theta values were reproduced by independent arithmetic. That result holds.

The new proof is analytic. Exhaustive enumeration on five and six vertices checks the exact identities; exact integer sums at larger n check their asymptotic magnitudes. No computation solves graph colouring. The failed 1e-6 diagnostic threshold was a finite-size assumption, not a failed covariance identity. Its failure is substantial enough to retain: near phase .75, Var(X_(k-1))/mu_(k-1) is about 591 at n~2^80, 1.0187 at n~2^160, and 1+5.11e-13 at n~2^320.

Small Pearson correlation is not independence, joint normality, or a lower bound on any concentration interval. Even a marginal central limit theorem would not by itself show that chi inherits the fluctuations. Those transfers are deliberately absent from the proposition.
