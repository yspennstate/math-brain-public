# account01/B17 — one shared heavy coordinate cannot beat the 3sqrt(2) central peak

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** `QFORM-B17-20260922T163428Z`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / ONE-SHARED-HEAVY-ROW-CENTRAL-NOESCAPE`  
**Full conjecture:** OPEN / NOT PROVED  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and partner result consumed

The full target remains: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential-density bound for `X^T A X` (with continuity tracked separately), or give a valid counterexample.

This run substantively applies the completed designated-partner theorem account02/B17, `QFORM-INFINITESIMAL-BANK-NOESCAPE-v1`, canonical source

`yspennstate/math-open-problems@9ef2d4cbf56e1aa3368eeaa322d09ba4d91f31cf`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T154450Z-account02-B17-QFORM-r11b/REPORT.md`.

That theorem proves that every convergent cap-one infinitesimal disjoint-bank limit has Gaussian variance at least `1/12` in each bank and hence quadratic peak at most `3 sqrt(2)` for the signature `(2,1)` core. Its sharp diffuse example attains `3 sqrt(2)` in the Gaussian limit. The open witness mechanism it identifies is a non-infinitesimal/shared-coordinate loading.

The present run attacks exactly that mechanism: **one physical coordinate is allowed macroscopic loading simultaneously in all three active spectral directions.**

## 2. Exact one-heavy-row model

Let

`J = diag(1,1,-1)`

and let `v in R^3` satisfy `r=||v||<1`. Put

`M = I_3 - v v^T`.

Let `X` be any real random variable with probability density `f_X` satisfying `0<=f_X<=1`, and let

`G ~ N(0, sigma^2 M)`

be independent of `X`, where `sigma^2 >= 1/12`. Define

`Y = v X + G`,   `Q = Y^T J Y`.

The covariance `sigma^2 M` is precisely the Gaussian residual left by an orthonormal-column frame after one physical row `v` is kept heavy and the remaining rows become diffuse. For `sigma^2=1/12` it is the minimum-variance Gaussian residual compatible with cap-one coordinates.

### Theorem `QFORM-ONE-SHARED-HEAVY-CENTRAL-C3SQRT2-v1`

The law of `Q` has a density at zero and

`p_Q(0) <= 3 sqrt(2)`.

For `sigma^2=1/12`, equality can occur only in the diffuse case `v=0`; every nonzero heavy row gives a strict inequality. Thus a single shared macroscopic physical coordinate cannot improve the known `3 sqrt(2)` lower-bound witness at the central level when the residual is Gaussian at or above the cap-one variance floor.

This is a central-density theorem for this mixed-leverage class, not a bound on `sup_t p_Q(t)` and not the full QFORM conjecture.

## 3. Cone-line representation

Write `q(y)=y^T J y`. For any sufficiently regular density `g` on `R^3`,

`p_q(0) = int_{R^3} delta(q(y)) g(y) dy`.

In spherical coordinates `y=r omega`, `q(r omega)=r^2 q(omega)` and the Jacobian `r^2` cancels the factor from `delta(r^2 q(omega))`. On `S^2`, the cone `q(omega)=0` is the union of the two circles

`C_+ : omega(theta)=(cos theta, sin theta, 1)/sqrt(2)`,

`C_-=-C_+`,

and `|grad_{S^2} q|=2` on the cone. Pairing antipodal half-rays therefore gives

`p_q(0) = (1/2) int_{C_+} int_R g(t omega) dt ds(omega)`.            (3.1)

For the conditional Gaussian law `Y | X=x ~ N(vx, Sigma)` with `Sigma=sigma^2 M`, let `K=Sigma^{-1}`. The Gaussian line integral is

`int_R g_x(t omega) dt`
` = (2 pi)^(-1) det(Sigma)^(-1/2) (omega^T K omega)^(-1/2)`
`   * exp[-x^2 D(omega)/2]`,                                        (3.2)

where

`D(omega)=v^T K v - (omega^T K v)^2/(omega^T K omega) >= 0`.          (3.3)

Averaging (3.2) over `X` and inserting into (3.1) is exact.

## 4. Rank-one algebra

Set

`z=v.omega`,   `a=r^2-z^2`.

Because `omega` is unit, `0<=a<1`. Sherman--Morrison gives

`M^{-1}=I + vv^T/(1-r^2)`.

Hence

`omega^T K omega = sigma^{-2} (1-a)/(1-r^2)`,                        (4.1)

`D(omega)=sigma^{-2} a/(1-a)`.                                      (4.2)

Also

`det(Sigma)=sigma^6(1-r^2)`.                                        (4.3)

Combining (3.1)--(4.3), and using `ds=dtheta/sqrt(2)` on `C_+`, yields

`p_Q(0)`
` = [1/(4 pi sigma^2 sqrt(2))] int_0^{2 pi}`
`     [ F_X( a(theta)/(sigma^2(1-a(theta))) ) / sqrt(1-a(theta)) ] dtheta`,   (4.4)

where

`F_X(D)=int_R f_X(x) exp(-D x^2/2) dx`.                              (4.5)

This identity keeps the original physical heavy coordinate and does not invoke post-rotation independence.

## 5. Exact bathtub bound for the heavy coordinate

For every `D>=0`, the kernel `exp(-D x^2/2)` is even and decreasing in `|x|`. Among all probability densities bounded by one, the bathtub principle gives

`F_X(D) <= F(D):=int_{-1/2}^{1/2} exp(-D x^2/2) dx`.                 (5.1)

Thus arbitrary support fragmentation and translations of the heavy coordinate cannot do better than the centered unit interval for this exact cone kernel.

Write

`s=12 sigma^2 >= 1`,

and for `0<=a<1` define

`c(a)=12a/(1-a)`.

Then the integrand in `p_Q(0)/(3 sqrt(2))` is bounded pointwise by

`H_s(a) = [1/s] F(c(a)/s) / sqrt(1-a)`.                              (5.2)

We prove `H_s(a)<=1` for every `s>=1` and `0<=a<1`.

First observe that `u -> u F(u)` is increasing on `[0,infinity)`, since

`u F(u) = sqrt(2 pi u) erf( sqrt(u)/(2 sqrt(2)) )`,                  (5.3)

and both factors are increasing. Therefore, with `u=c/s<=c`,

`F(c/s)/s = [u F(u)]/c <= F(c)`.                                    (5.4)

So it suffices to prove the sharp `s=1` inequality

`F(12a/(1-a)) <= sqrt(1-a)`.                                        (5.5)

Set

`x = sqrt( 3a/[2(1-a)] )`.

The explicit Gaussian integral gives

`F(12a/(1-a))/sqrt(1-a) = sqrt(pi/(6a)) erf(x)`.                     (5.6)

Since `a=2x^2/(3+2x^2)`, (5.5) is equivalent to

`erf(x) <= 2 sqrt(3) x / [ sqrt(pi) sqrt(3+2x^2) ]`,   `x>=0`.       (5.7)

Let the right side be `R(x)`. Both sides vanish at zero, and

`R'(x) - erf'(x)`
` = [2/sqrt(pi)] [ (1+2x^2/3)^(-3/2) - exp(-x^2) ] >= 0`,           (5.8)

because

`-(3/2) log(1+2x^2/3) >= -x^2`

follows from `log(1+t)<=t`. Hence (5.7), therefore (5.5), holds. It is strict for `x>0`.

Combining (5.1)--(5.8) with (4.4),

`p_Q(0)/(3 sqrt(2))`
` <= (1/(2 pi)) int_0^{2 pi} H_s(a(theta)) dtheta <= 1`.             (5.9)

This proves the theorem.

For `sigma^2=1/12`, if `v!=0`, the function `a(theta)=||v||^2-(v.omega(theta))^2` is positive on a set of positive measure; strictness in (5.8) then gives `p_Q(0)<3 sqrt(2)`.

## 6. Exact target-admissible finite frames approaching the model

The mixed-leverage geometry is realizable with exact target matrices. Fix `v` and let

`B=(I-vv^T)^(1/2)`.

For each `m`, form an `(1+3m) x 3` matrix `R_m` whose first row is `v^T`, and whose remaining rows are

`e_j^T B / sqrt(m)`,   `j=1,2,3`, repeated `m` times.

Then exactly

`R_m^T R_m = vv^T + B^2 = I_3`.                                     (6.1)

Therefore

`A_m=R_m J R_m^T`

has nonzero spectrum exactly `{1,1,-1}` for every `m`. If all physical coordinates are independent `Unif[-1/2,1/2]`, the three residual coordinate-bank sums converge jointly to `N(0,I_3/12)`, so the projected vector converges to

`v U + N(0,(I-vv^T)/12)`.

Thus the theorem is a genuine analytic stress result for an exact sequence of rotated target-admissible matrices with one non-infinitesimal physical row shared across all three spectral directions. A finite-row local limit theorem would still be needed to transfer the pointwise density-at-zero inequality uniformly back to the approximants; weak convergence alone is insufficient, exactly as recorded by the partner result.

## 7. Actual use of the partner result and mathematical change

The partner theorem identifies `3 sqrt(2)` as the sharp ceiling for the fully infinitesimal disjoint-bank limit and isolates non-infinitesimal/shared-coordinate loading as a possible escape. Equation (5.9) applies that exact benchmark to the first genuinely shared-coordinate mixed-leverage model:

`p_shared-heavy(0) <= 3 sqrt(2) = p_partner-diffuse-extremal(0)`.     (7.1)

The right equality is the partner's sharp Gaussian diffuse witness; the left inequality is the new cone-line/bathtub theorem above. Hence one shared macroscopic row does **not** escape the sharp diffuse central ceiling in the variance-minimizing Gaussian residual regime.

This changes the witness frontier. To beat `3 sqrt(2)` one must now exploit at least one feature not covered here: two or more interacting macroscopic physical rows, anisotropic/non-Gaussian residual structure beyond the scalar Gaussian floor, a density peak away from zero, or a finite-row local spike invisible in the mixed weak limit.

## 8. Correction hygiene and limitations

No refuted pointwise oscillatory-decay statement is used. No independence after rotation is assumed: the heavy coordinate remains explicit and shared in all three spectral directions. No one-minor, cross-rank-three, conditional-cap, fixed-fragment-count, fiberwise-trace, or phase-Wiener claim is used. The full QFORM conjecture and the separate continuity target remain open.

This theorem is supporting mathematics, not a full solution and not evidence that the global optimal constant equals `3 sqrt(2)`.
