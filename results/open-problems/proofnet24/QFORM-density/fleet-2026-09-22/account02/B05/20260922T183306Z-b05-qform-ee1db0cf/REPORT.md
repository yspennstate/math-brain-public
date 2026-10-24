# account02/B05 — coordinate-coarea leverage barrier and the sharp half-Riesz threshold

**Run:** `20260922T183306Z-b05-qform-ee1db0cf`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / PRECISE MISSING FACTORS ISOLATED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Full target and first unpaid implication

The full target is unchanged: for arbitrary independent real coordinates with one-dimensional densities bounded by one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of `X^T A X`, or give a valid target counterexample.

The first unpaid geometric implication is no longer a generic binary Schur coarea estimate: that product-coordinate estimate was already supplied by this slot in an earlier run. The current correction state also rules out the arbitrary-joint rank-three coarea bound and the worst normalized scalar-conditioned core supremum. What remains is an **aggregate-before-inversion** inequality: curved coarea must use the original product source across many physical coordinates before paying a reciprocal gradient/Jacobian, and scalar conditioning must retain its unnormalized fiber mass.

This report proves two exact barriers/interfaces for that missing step.

## 2. Partner result actually consumed

The designated partner `account03/B05` proved `QFORM-SCALAR-CONDITIONED-CORE-SUP-FALSE-v1`, canonical report

`yspennstate/math-open-problems@30ed85cae72f1ddc2d7f3d20de47f82369ec60dd`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T181101Z-account03-B05-QFORM-r14/REPORT.md`.

It gives a legal four-dimensional product source with spectrum `{1,1,1,-1}` for which `sup_b ||p_{Q3|Q'=b}||_infinity` diverges logarithmically. The exact lost quantity is the unnormalized scalar-fiber mass `p_{Q'}(b)`. I use this result below to forbid taking a normalized fiber supremum before the curved trace.

A second current theorem used to sharpen the remaining exponent is account02/B20 `QFORM-RANK2-CROSS-SQRT-CONCENTRATION-v1`, canonical report

`yspennstate/math-open-problems@4bc44879d92221288f5055d31318e9ecb25f4650`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260922T182735Z-account02-B20-QFORM-r16/REPORT.md`.

If an original-coordinate cut has second cross singular value at least `beta`, it proves

`L_Q(h) := sup_I P(Q in I) <= min(1, K_beta h^(1/2))`,

`K_beta = sqrt(2 e sqrt(pi)/beta)`,

with arbitrary self blocks and outside couplings. It explicitly leaves the exponent upgrade to one as the missing third-direction payment.

## 3. The coordinate-coarea leverage barrier

### Lemma 3.1 — exact coordinate-chart loss

Let `Q` be `C^1` and let `x` be a regular point of a level surface. The coordinate-free coarea kernel is

`d sigma(x) / ||grad Q(x)||_2`.

If a local surface patch is parameterized by deleting physical coordinate `i`, then the graph Jacobian identity is

`d sigma / ||grad Q||_2 = d x_{-i} / |partial_i Q|`.

Therefore every product-preserving one-coordinate chart pays, relative to the Euclidean coarea kernel, the factor

`||grad Q||_2 / |partial_i Q| >= ||grad Q||_2 / ||grad Q||_infinity`.      (3.1)

No nonnegative partition of unity among coordinate charts can improve the pointwise minimum: every chosen reciprocal derivative is at least `1/||grad Q||_infinity`. Thus the exact missing factor in any single-coordinate coarea reduction is

`L(x)=||grad Q(x)||_2 / ||grad Q(x)||_infinity`.                         (3.2)

This is a geometric identity/inequality, not a claim that every possible product-measure proof must use such charts.

### Lemma 3.2 — leverage lower bound for a rank-three projector

Let `P` be an orthogonal projector and `Q_P(x)=x^T P x`. Put

`mu(P)=max_i P_ii`.

At every regular point,

`L(x)=||P x||_2 / ||P x||_infinity >= mu(P)^(-1/2)`.                    (3.3)

Proof. Normalize `w=Px/||Px||_2`, so `w` lies in `range(P)`. For every physical coordinate,

`|w_i|=|<P e_i,w>| <= ||P e_i||_2 = sqrt(P_ii) <= sqrt(mu(P))`.

Hence `||w||_infinity<=sqrt(mu(P))`, which is (3.3). `QED`

For positive projector energy `Q_P=t>0`, `||grad Q_P||_2=2 sqrt(t)`, whereas every physical coordinate derivative satisfies

`|partial_i Q_P| <= 2 sqrt(mu(P)) sqrt(t)`.

Thus the dimension-free Euclidean curved kernel `1/(2 sqrt(t))` becomes at least `mu(P)^(-1/2)/(2 sqrt(t))` after any single physical-coordinate graph parameterization.

## 4. Exact legal product stress family: the loss is order sqrt(n)

For every `n` divisible by four, let `U` be the `n x 3` matrix whose rows consist equally often of

`(1,1,1)/sqrt(n)`, `(1,1,-1)/sqrt(n)`, `(1,-1,1)/sqrt(n)`, `(1,-1,-1)/sqrt(n)`.

Then `U^T U=I_3`. With `P=UU^T`, `P` is a rank-three orthogonal projector, every diagonal is `3/n`, and `Q=x^T P x` has exactly three eigenvalues equal to one. Hence it is inside the exact target spectral class.

Let `u_1` be the first column of `U`, set `R=n`, and use the legal independent cap-one product density

`rho_n(x)=1_{R u_1+[-1/2,1/2]^n}(x)`.

For every `x=R u_1+xi` in this support,

`P x=R u_1+P xi`,

`||P xi||_2<=sqrt(n)/2`,

and, since `P` is a projector and `P_ii=3/n`,

`|(P xi)_i| <= ||P e_i||_2 ||xi||_2 <= sqrt(3)/2`.

Therefore

`||grad Q||_2 >= 2(n-sqrt(n)/2)`,

`||grad Q||_infinity <= 2(sqrt(n)+sqrt(3)/2)`.

For `n>=4`,

`||grad Q||_2 / ||grad Q||_infinity >= sqrt(n)/2`.                      (4.1)

At the center `x=R u_1` the ratio is exactly `sqrt(n)`.

Thus the leverage loss is not a point artifact and is compatible with a genuine unit-volume independent product source: throughout its support, every one-coordinate coarea chart is worse than the Euclidean coarea kernel by order `sqrt(n)`. This family is **not** a QFORM counterexample. It is precisely a diffuse rank-three frame (`max P_ii=3/n`), the regime that the campaign's global ridge/Fresnel mechanism is designed to aggregate before inversion.

### Consequence

A dimension-free proof cannot obtain the diffuse branch merely by partitioning the level surface into physical coordinate graphs and using `f_i<=1` after selecting one chart. The missing factor is exactly the conversion

`||grad Q||_2 / ||grad Q||_infinity`,

or, spectrally, at least `mu(P)^(-1/2)`. The product structure must be aggregated across many coordinates before this reciprocal is paid.

This complements the partner's scalar-fiber counterexample: retaining the scalar fiber weight is necessary, but after doing so one still cannot discard simultaneous coordinate aggregation by reverting to a single physical chart.

## 5. A sharp concentration-to-half-Riesz threshold

The new B20 cross-bank theorem gives the exponent `1/2`. The following elementary lemma identifies exactly why that exponent is still borderline for a one-square third-direction smoothing.

### Theorem 5.1 — half-Riesz synthesis for any exponent above one half

Let `R` be a real random variable satisfying the interval concentration bound

`sup_{I: |I|=h} P(R in I) <= min(1,K h^alpha)`                         (5.1)

for all `h>0`, with `alpha>1/2`. Then for every `t`, both one-sided half-Riesz potentials obey

`E[ 1_{R<t} (t-R)^(-1/2) ] <= (2 alpha/(2 alpha-1)) K^(1/(2 alpha))`,  (5.2)

and the analogous bound with `R>t`.

Proof. By layer cake,

`E[1_{R<t}(t-R)^(-1/2)]`

`= integral_0^infinity P(t-s^(-2)<R<t) ds`

`<= integral_0^infinity min(1,K s^(-2 alpha)) ds`.

With `s_0=K^(1/(2 alpha))`, the last integral equals at most

`s_0 + K s_0^(1-2 alpha)/(2 alpha-1)`

`= (2 alpha/(2 alpha-1)) K^(1/(2 alpha))`. `QED`

Consequently, if `X` is independent of `R`, `f_X<=1`, `a!=0`, and `b` is arbitrary, then

`a(X-b)^2+R`

has density bounded by

`|a|^(-1/2) (2 alpha/(2 alpha-1)) K^(1/(2 alpha))`.                    (5.3)

Indeed the shifted-square density is bounded on its supported side by `|a|^(-1/2) y^(-1/2)`, and (5.2) performs the exact convolution.

### Sharpness of the threshold

The endpoint `alpha=1/2` cannot be included in a concentration-only theorem. Let `X,Y` be independent Uniform`[-1/2,1/2]`, put `R=-Y^2`, and smooth by the independent square `X^2`. Then

`sup_{|I|=h} P(R in I) <= 2 sqrt(h)`,

but `X^2-Y^2` has logarithmically unbounded density at zero, since the square density is `s^(-1/2)` on `(0,1/4)` and the zero-density convolution contains `integral_0^(1/4) ds/s`.

Hence the `h^(1/2)` exponent produced by the current rank-two cross-bank theorem is **exactly critical** for absolute one-square/half-Riesz smoothing. Any uniform gain to `h^(1/2+epsilon)` would immediately make the half-Riesz step finite, with the explicit constant (5.3); at the exact endpoint, a different joint/multilinear use of the third spectral direction is necessary.

## 6. Conditional end-to-end implication and the first unpaid step

The present source-backed skeleton is:

1. The campaign already has complete diffuse ridge/window branches and full-matrix pair branches under their stated quantitative hypotheses.
2. `account03/B05` rules out the normalized worst scalar-conditioned core supremum, so scalar-fiber mass must remain inside the weighted mixture.
3. `account02/B20` pays any rank-two cross bank `s_2(C)>=beta` by the dimension-free concentration estimate `K_beta h^(1/2)`.
4. Theorem 5.1 proves that **any** source-preserving improvement of that residual concentration exponent to `1/2+epsilon`, followed by a genuinely independent physical square of coefficient bounded away from zero, closes that branch with a universal density constant. The endpoint `1/2` is sharp for this absolute smoothing route.
5. Lemmas 3.1--4.1 prove that a diffuse rank-three branch cannot supply the missing improvement by choosing a single coordinate coarea chart: it loses at least the leverage factor `mu^(-1/2)` and can lose order `sqrt(n)` on a legal target family.

Therefore the first unpaid implication is now:

`QFORM-THIRD-DIRECTION-AGGREGATE-BEFORE-INVERSION-v1` — in the B20 cross-bank packet with the full hypothesis `s_3(A)>=1`, use the third spectral direction **before** either (a) taking a reciprocal single-coordinate derivative or (b) taking a normalized scalar-fiber supremum, to obtain either a concentration exponent `1/2+epsilon` for some universal `epsilon>0`, a directly finite half-Riesz trace, or a linear small-interval bound. Arbitrary self blocks/outside couplings and the original product source must be retained.

This is stronger and more precise than merely saying “spend the third direction”: the exact missing quantitative factor is an exponent gain over the borderline `1/2`, unless a genuinely nonabsolute/multilinear third-direction integration bypasses half-Riesz altogether.

## 7. Status

**ESSENTIAL_STEP_APPLIED; FULL QFORM OPEN.**

Proved here: the exact coordinate-chart loss, its leverage lower bound, an explicit legal rank-three product stress family with order-`sqrt(n)` loss throughout support, the sharp `alpha>1/2` concentration-to-half-Riesz theorem, and endpoint sharpness by a legal product construction.

Not proved here: the required third-direction exponent gain, a universal weighted multichart coarea theorem, the unrestricted full QFORM density bound, or continuity.

No numerical computation was used in these proofs.