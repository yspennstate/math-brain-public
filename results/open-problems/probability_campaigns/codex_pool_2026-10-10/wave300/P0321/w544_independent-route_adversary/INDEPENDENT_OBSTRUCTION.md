# A probabilistic obstruction to an exact linear-density identification

This is the disjoint extension of the independent route saved in ATTEMPT.md. After saving that route, I found that w543 independently derived the same positive-shear obstruction. I do not claim that repeated calculation as new work. The extension here uses positivity and correlated Gaussian exceedances; it does not repeat the peer's finite-window or zero-shear calculations.

## Precise general assertion

Let X_n, n>=1, be a stationary centered real Gaussian sequence with variance sigma^2>0 and covariance Cov(X_1,X_{1+h}) -> 0 as h -> infinity. Fix a finite rho>0. Then p=P(rho+X_n<0)=Phi(-rho/sigma)>0, and

    P(rho+X_n<0 for infinitely many n)=1.

No joint independence of the sequence is assumed. The covariance hypothesis matters: a constant Gaussian sequence violates it and does not have the almost-sure conclusion.

## Independent proof

Set I_n=1_{X_n<-rho}. Its expectation is p. For large h the standardized pair (X_1/sigma, X_{1+h}/sigma) is a bivariate Gaussian whose correlation tends to zero. Its characteristic function converges to that of two independent standard normals. The threshold boundaries have zero limiting probability, so E(I_1 I_{1+h}) -> p^2. Hence c_h=Cov(I_1,I_{1+h}) -> 0. This is a derived fact about a named pair, not multiplication of conditional bounds across the sequence.

For A_N=N^{-1} sum_{n=1}^N I_n, stationarity gives

    Var(A_N)=p(1-p)/N + (2/N^2) sum_{h=1}^{N-1}(N-h)c_h -> 0.

To see the last limit without a rate, split the sum at a fixed H. The initial H terms are O(H/N), since the c_h are bounded; the remaining absolute contribution is at most sup_{h>=H}|c_h|. First let N grow and then let H grow.

On E={I_n=0 for every n>=1}, A_N=0 for every N. Chebyshev implies P(E)<=Var(A_N)/p^2 for every N, and therefore P(E)=0. For each fixed starting index m the same argument, by stationarity, gives P(I_n=0 for all n>=m)=0. The event of only finitely many negative values is the countable union of those zero-probability events. Its probability is zero.

For a threshold M>0 the identical argument applied to I_n=1_{|X_n|>M} shows that no fixed global amplitude bound holds almost surely. It does not furnish a large-deviation rate for finite boxes.

## Application to the specified elastic density field

In ATTEMPT.md, delta rho has integrable spectral density

    rho^2 |k|^{2-s}/(beta a) 1_{|k|<=Lambda},  0<s<2.

Consequently its covariance tends to zero by the Riemann-Lebesgue lemma, its restriction to an equally spaced ray is a stationary Gaussian sequence, and its exact variance is

    sigma_density^2 = rho^2 Lambda^{4-s}/[2 pi beta a (4-s)] > 0.

Thus rho+delta rho is negative at infinitely many points on that ray almost surely, at every fixed finite positive beta,a,Lambda,rho. At a single point the negative probability is already Phi(-rho/sigma_density)>0.

For any locally finite point configuration Xi and nonnegative smoothing kernel h, the smoothed particle density sum_{x in Xi}h(z-x) is nonnegative whenever finite. It cannot have the same one-point law as this nondegenerate additive Gaussian density. Hence an exact identification of rho+delta rho with a nonnegative smoothed particle density is impossible. This is an obstruction to that identification, not to an approximate fluctuation law, to a central limit theorem, or to a Riesz Gibbs phase.

The minimum repair is to state an approximation on local or scale-dependent good events, or a nonlinear positive observable, and prove enough control of the exceptional events and correlation errors. The tiny one-point tail does not justify a simultaneous good event over an infinite system. The almost-sure proof above deliberately uses pair decorrelation rather than unsupported independent-cell products.

## Scope and review

This auxiliary assertion was derived here and is awaiting the designated referee w545. It does not construct, rule out, or determine the present openness of a hexatic Riesz phase. A single threshold can be exceeded extremely rarely at large beta; the infinite-volume conclusion still follows under the stated decorrelation hypothesis, without claiming any useful finite-volume probability rate. A non-Gaussian density fluctuation limit or a nonlinear density field is outside this obstruction.
