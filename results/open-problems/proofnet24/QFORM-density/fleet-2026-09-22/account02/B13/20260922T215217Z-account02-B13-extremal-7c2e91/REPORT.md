SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B13, 2026-09-22T21:52:17Z.
attacking: QFORM-NEARNULL-TWOBANK-LINEARIZE-SQRT-TO-LINEAR-v1 through same-law Fourier-power extremalization and positive-copy collision geometry.

# account02/B13 — same-extreme Fourier-power reduction and a linear four-copy slab theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Run:** `20260922T215217Z-account02-B13-extremal-7c2e91`  
**Classification:** `SUPPORTING TARGET-LEVEL THEOREMS / MECHANISM ADVANCE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and first unpaid implication

The full owner target remains OPEN: for every finite `n`, independent real original-coordinate random variables with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a universally bounded density, or give a genuine target counterexample.

This run preserves the completed zero-loss extremal-product reduction from account02/B13: for every fixed bounded measurable slab functional, arbitrary cap-one product densities can be replaced coordinatewise by arbitrary measure-one product indicators without decreasing the functional. It does **not** assert that a centered interval, a connected set, a bounded-diameter set, or a uniformly bounded number of fragments is extremal.

The designated partner account03/B13 run `20260922T213118Z-account03-B13-qform-r17`, canonical commit `eac866b378f5c54411a55f7eb49f89336a4701ae`, sharpened the exact-rank-three mixed residual to a near-null one-heavy/two-transverse-bank state and proved

`|phi_Q(t)| <= min(1,A_* |t|^(-1/2))`,                                      (1.1)

where

`r_* = sqrt(3/10) [ sqrt(7/800)sqrt(1-10^(-4)) - 10^(-2) ]`
`    = 0.0457549664530082...`,

and

`A_*^2 = pi sqrt(2)/r_* = 97.1016543684137...`.                           (1.2)

Equivalently, the partner proved a uniform one-copy square-root small-ball estimate on that residual, but not the required linear slab bound. Its first unpaid implication is

`QFORM-NEARNULL-TWOBANK-LINEARIZE-SQRT-TO-LINEAR-v1`.

The first question here is therefore: can the extremal-product structure turn the partner's `|t|^{-1/2}` endpoint into a genuinely integrable object without destroying original-coordinate product provenance?

The answer is yes at the **same-law copy level**. The remaining gap is then an explicit deconvolution/product-geometry implication, not an integrability gap.

## 2. Same-extreme reduction for every nonnegative Fourier power

Let `D_n` denote all product probability laws on `R^n` whose one-dimensional marginals have densities `0<=f_i<=1`. Let `F_n` denote product laws whose one-dimensional marginals are indicators of compact finite unions of intervals of total length one. The completed account04/B14 finite-mixture localization theorem says every member of `D_n` is a total-variation limit of finite convex mixtures of members of `F_n`, with no uniform support radius, fragment count, or separation parameter.

Let `P:R^n->R` be measurable, let `p>=1`, and let `w:R->[0,infinity]` be Borel. Define the extended nonnegative functional

`J_(p,w)(mu) = integral_R w(t) | E_mu exp(i t P(X)) |^p dt`.             (2.1)

### Theorem 2.1 — `QFORM-FOURIER-LP-SAME-EXTREME-REDUCTION-v1`

For every `p>=1` and every nonnegative Borel `w`,

`boxed: sup_(mu in D_n) J_(p,w)(mu) = sup_(nu in F_n) J_(p,w)(nu).`      (2.2)

Thus Fourier powers, including same-law collision energies, may be extremalized to **one common product-indicator law**. For `p=2m` this is stronger than a generic positive `2m`-copy multilinear localization, which is allowed to choose different extreme laws for the different copies.

### Proof

Fix `mu in D_n`. By account04/B14, choose finite mixtures

`mu_N = sum_a theta_(N,a) nu_(N,a)`,

where `nu_(N,a) in F_n`, `theta_(N,a)>=0`, `sum_a theta_(N,a)=1`, and `mu_N -> mu` in total variation. Put

`z_a(t)=E_(nu_(N,a)) exp(i t P(X))`.

Linearity of expectation gives

`phi_(mu_N)(t)=sum_a theta_(N,a) z_a(t)`.

Since `z -> |z|^p` is convex on `C ~= R^2` for every `p>=1`, Jensen gives pointwise

`|phi_(mu_N)(t)|^p <= sum_a theta_(N,a)|z_a(t)|^p`.             (2.3)

Multiplying by `w(t)>=0` and integrating,

`J_(p,w)(mu_N)
 <= sum_a theta_(N,a) J_(p,w)(nu_(N,a))
 <= sup_(nu in F_n)J_(p,w)(nu)`.                                (2.4)

Total-variation convergence implies convergence of expectations of every bounded measurable function, in particular

`phi_(mu_N)(t) -> phi_mu(t)`

for every `t`. Fatou applied to `w(t)|phi_(mu_N)(t)|^p` yields

`J_(p,w)(mu) <= liminf_N J_(p,w)(mu_N)
             <= sup_(nu in F_n)J_(p,w)(nu)`.                    (2.5)

Take the supremum over `mu in D_n`. The reverse inequality follows from `F_n subset D_n`. QED.

### Fejer same-law corollary

For

`w_T(t)=(1-|t|/T)_+`,
`K_T(s)=integral_(-T)^T w_T(t)e^(its)dt
      =T [ sin(Ts/2)/(Ts/2) ]^2 >=0`,                            (2.6)

and iid `X,X'~mu`,

`integral w_T(t)|phi_P(t)|^2dt
 = E K_T(P(X)-P(X'))`.                                          (2.7)

Theorem 2.1 with `p=2` says the supremum of this **same-law** collision functional over all cap-one product laws is already achieved in the limiting sense by a single `nu in F_n`, used for both copies. No copy-dependent extreme supports are needed.

This is the first new product-law structural result of the run.

## 3. Applying the designated partner: an exact Fourier-power ladder

Now specialize to the hard exact-rank-three residual of account03/B13 r17 and use (1.1). For every real `p>2`,

`integral_R |phi_Q(t)|^p dt
 <= integral_R min(1,A_*^p |t|^(-p/2)) dt`.                     (3.1)

Split at `t_0=A_*^2`. A direct calculation gives

`boxed:
 integral_R |phi_Q(t)|^p dt
 <= 2 A_*^2 p/(p-2).
`                                                                    (3.2)

Indeed

`2[t_0+A_*^p integral_(t_0)^infinity t^(-p/2)dt]
 =2A_*^2[1+2/(p-2)]`.

This is uniform in dimension, all support geometry, and all laws in the partner residual.

### Theorem 3.1 — `QFORM-NEARNULL-COPY-LADDER-v1`

Let `Q_1,...,Q_(2m)` be iid copies of `Q`, with integer `m>=2`, and define

`S_(2m)=sum_(k=1)^m (Q_(2k-1)-Q_(2k))`.                         (3.3)

Then `S_(2m)` has a bounded continuous density and

`boxed:
 ||p_(S_(2m))||_infinity
 <= (sqrt(2)/r_*) m/(m-1).
`                                                                    (3.4)

### Proof

Because `Q` is real,

`phi_(S_(2m))(t)=|phi_Q(t)|^(2m)`.                               (3.5)

Apply (3.2) with `p=2m`. The characteristic function is integrable, so Fourier inversion yields a bounded continuous density, and

`||p_(S_(2m))||_infinity
 <=(1/(2pi)) integral |phi_Q(t)|^(2m)dt
 <=(1/(2pi)) 2A_*^2 (2m)/(2m-2)
 =(A_*^2/pi)m/(m-1)
 =(sqrt(2)/r_*)m/(m-1)`.                                        (3.6)

QED.

For four copies (`m=2`),

`boxed:
 ||p_(Q_1-Q_2+Q_3-Q_4)||_infinity
 <= 2sqrt(2)/r_*
 =61.8168331005351... .
`                                                                    (3.7)

Therefore every interval `I` satisfies the **linear** copy-level slab bound

`boxed:
 P(Q_1-Q_2+Q_3-Q_4 in I)
 <=61.816834 |I|.
`                                                                    (3.8)

This is the partner's square-root endpoint converted into a linear dimension-free small-ball theorem by a product-safe operation. No conditioning on sum/difference variables is used.

## 4. Geometric extreme-product form of the four-copy theorem

Apply Theorem 2.1 with `p=4`. For every fixed quadratic form in the partner residual, the worst `L^4` characteristic integral among arbitrary cap-one product laws equals the supremum over one common finite-fragment product indicator law.

Equivalently, for every product set

`E=E_1 x ... x E_n`, `|E_i|=1`,

and four independent points `x^(1),...,x^(4)` uniformly distributed on that **same** product set, (3.8) gives

`boxed:
 |{(x^(1),...,x^(4)) in E^4:
     Q(x^(1))-Q(x^(2))+Q(x^(3))-Q(x^(4)) in I}|
 <=61.816834 |I|.
`                                                                    (4.1)

Conversely, because the same-extreme theorem is exact at the supremum level, a uniform geometric proof of such Fourier-power/collision inequalities on finite-fragment product indicators transfers with zero loss to every cap-one product law.

This is genuinely stronger than allowing four unrelated product supports: all four copies share the same extreme product geometry. That same-support structure is the natural information one would need for any valid deconvolution back to a one-copy slab estimate.

## 5. Two-copy endpoint: an epsilon-log-epsilon concentration law

The two-copy difference

`D=Q_1-Q_2`

has characteristic function `|phi_Q(t)|^2`, and (1.1) gives

`|phi_D(t)| <= min(1,A_*^2/|t|)`.                                (5.1)

The right side is borderline nonintegrable, but it yields an explicit `ell log(1/ell)` interval estimate.

Let `I` have length `ell`, center `x_0`, and put `epsilon=ell/2`. The Gaussian majorant

`1_(|y-x_0|<=epsilon)
 <=e^(1/2) exp(-(y-x_0)^2/(2epsilon^2))`

and Fourier inversion give

`P(D in I)
 <= e^(1/2) epsilon/sqrt(2pi)
    integral_R exp(-epsilon^2 t^2/2)|phi_D(t)|dt`.               (5.2)

Assume `ell<=2/A_*^2`, so `u=epsilon A_*^2<=1`. Splitting at `A_*^2` and changing variables on the tail,

`integral_R exp(-epsilon^2t^2/2)min(1,A_*^2/|t|)dt
 <=2A_*^2[1+J(u)]`,                                              (5.3)

where

`J(u)=integral_u^infinity exp(-s^2/2) ds/s
 <=log(1/u)+e^(-1/2)`.                                          (5.4)

(The tail from one to infinity is at most `integral_1^infinity s exp(-s^2/2)ds=e^(-1/2)`.) Hence

`boxed:
 P(Q_1-Q_2 in I)
 <= [e^(1/2)A_*^2/sqrt(2pi)] ell
    [1+e^(-1/2)+log(2/(A_*^2 ell))]
`                                                                    (5.5)

for `0<ell<=2/A_*^2`; for larger `ell` use the trivial bound one. Numerically the leading coefficient is

`e^(1/2)A_*^2/sqrt(2pi)=63.8680910917846...`.                    (5.6)

Likewise, for `T>A_*^2`, the Fejer collision budget satisfies the simple bound

`integral_(-T)^T (1-|t|/T)|phi_Q(t)|^2dt
 <=2A_*^2[1+log(T/A_*^2)]`.                                      (5.7)

By Theorem 2.1, its supremum can be tested on a single common product-indicator law.

Thus the copy hierarchy is now quantitative:

- one copy: `O(ell^(1/2))` from the designated partner;
- two-copy difference: `O(ell log(1/ell))`;
- four-copy alternating sum: `O(ell)` with explicit constant `61.817`.

## 6. Why this does not yet close the one-copy target

It would be invalid to conclude from (3.7) alone that `Q` itself has bounded density. Generic deconvolution fails even inside the cap-one input world.

Take the rank-one model `Y=U^2` with `U~Unif[0,1]`. Then

`p_Y(y)=1/(2sqrt(y)) 1_(0,1)(y)`,

which is unbounded. On the other hand the fixed-law Fresnel integral satisfies `|phi_Y(t)|=O(|t|^(-1/2))`, so `|phi_Y|^4` is integrable and

`Y_1-Y_2+Y_3-Y_4`

has a bounded continuous density. This is **not** a QFORM target counterexample: it has only one large quadratic direction. It is a genuine counterexample to the mechanism-level implication

`bounded four-copy alternating density => bounded one-copy density`.

Therefore the four-copy theorem is not closure by itself. The missing implication must use the target's rank-three quadratic/product geometry rather than generic probability deconvolution.

## 7. New first unpaid implication

The exact next obligation is

`QFORM-SAME-EXTREME-DECONVOLUTION-v1`:

> In the account03/B13 near-null/two-transverse-bank residual, exploit the **same-product-set** geometry supplied by Theorem 2.1, together with the original-coordinate quadratic identity across copies, to convert the linear four-copy slab estimate (4.1), or an equivalent positive Fejer/collision estimate, into a one-copy linear slab bound. The proof must aggregate in the original independent coordinates before any sum/difference conditioning; it may not assume conditional cap preservation, independence after a copy rotation, bounded support diameter, or a fixed fragment count.

This is a stricter and more concrete successor to `QFORM-NEARNULL-TWOBANK-LINEARIZE-SQRT-TO-LINEAR-v1`: the integrability step is now paid on the natural copy lift, and the remaining debt is exactly the product-specific pullback.

Additional spectral directions remain a separate full-target bridge after exact rank three.

## 8. Corrections and source discipline

This run does not use the refuted arbitrary-joint rank-three coarea claim, positive conditional projection-height moments, law-uniform scalar van der Corput, post-rotation independence, bounded-diameter localization, fixed-fragment localization, conditional-cap-as-independence, or one-good-minor selection. In particular, no copy sum/difference variable is treated as a fresh cap-one independent coordinate.

The completed external results actually used are:

1. designated partner account03/B13 r17, canonical `math-open-problems@eac866b378f5c54411a55f7eb49f89336a4701ae`: the near-null bank-energy floor and uniform `|t|^(-1/2)` endpoint;
2. account04/B14 `QFORM-LAW-LEVEL-FINITE-MIXTURE-LOCALIZATION-v1`, canonical `math-open-problems@321ec7899f4972d125d641408512fe9e5e9dcf4c`: total-variation approximation by finite mixtures of finite-fragment product indicators.

The earlier account02/B13 zero-loss fixed-functional bang-bang theorem remains the geometric front end. The new Fourier-power theorem is not a restatement of it: it handles the nonlinear convex functional `|phi|^p` and preserves a single common extreme law across all copies.

## 9. Verification

A deterministic standard-library checker verifies the constants, the exact integral formula

`integral_R min(1,A|t|^(-1/2))^p dt = 2A^2 p/(p-2)`

for representative `p>2`, and 100,000 randomized instances of the Jensen inequality underlying Theorem 2.1. It terminates with `QFORM_B13_COPY_CHECK_PASS`.

The checker is only a regression aid; the proofs are the analytic arguments above.

## 10. Status

- `QFORM-FOURIER-LP-SAME-EXTREME-REDUCTION-v1`: **PROVED THIS RUN**.
- `QFORM-NEARNULL-COPY-LADDER-v1`: **PROVED THIS RUN, APPLYING DESIGNATED PARTNER**.
- four-copy linear slab constant in the hard residual: **61.816834**.
- two-copy difference: explicit `ell log(1/ell)` concentration bound.
- `QFORM-SAME-EXTREME-DECONVOLUTION-v1`: **OPEN**.
- exact-rank-three QFORM: **OPEN**.
- full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
