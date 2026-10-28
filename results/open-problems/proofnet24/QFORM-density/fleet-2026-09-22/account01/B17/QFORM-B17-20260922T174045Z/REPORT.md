# account01/B17 — quantitative one-heavy-row central gap and exact finite transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `QFORM-B17-20260922T174045Z`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / QUANTITATIVE_ONE_HEAVY_CENTRAL_GAP`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, corrections and partner results actually used

The full target remains: for every dimension, every independent real input family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal dimension-free essential-density bound for `X^T A X`, with continuity treated separately, or give a valid target-level counterexample.

This run builds on the completed designated-partner theorem account02/B17, `QFORM-INFINITESIMAL-BANK-NOESCAPE-v1`, canonical source

`yspennstate/math-open-problems@9ef2d4cbf56e1aa3368eeaa322d09ba4d91f31cf`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T154450Z-account02-B17-QFORM-r11b/REPORT.md`.

That theorem proves that every convergent cap-one infinitesimal disjoint-bank limit has a Gaussian component of variance at least `1/12` in each bank, and hence the signature `(2,1)` limiting quadratic form has density bounded by `3 sqrt(2)`. Its equal-weight uniform-bank example attains `3 sqrt(2)` in the Gaussian limit.

I also consumed the newer completed partner report

`yspennstate/math-open-problems@f117a4870969d37706b8d7e62cbcae671cc2d3b0`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T164534Z-account02-B17-QFORM-r11/REPORT.md`.

It refutes the proposed universal *conditional* three-dimensional projection-density cap on an exact Hadamard-cube target, and gives a stronger exact six-variable shared-frame stress with

`p_Q(0)=4.0630706168060372601... < 3 sqrt(2)`.

The live corrections are respected: this report uses no pointwise oscillatory-decay claim, no post-rotation independence, no conditional cap preservation, no raw fiber-sup bound, no one-minor/cross-minor extraction, and no fixed-fragment reduction.

The previous account01/B17 theorem `QFORM-ONE-SHARED-HEAVY-CENTRAL-C3SQRT2-v1`, canonical commit `9a2d962f0f1794d735399019273ffc2f6de3fda4`, proved the qualitative central bound below. The new work strengthens it by an explicit globally valid quartic deficit and supplies the previously missing local-transfer statement for the exact uniform finite frames.

## 2. One-heavy-row model

Let

`J=diag(1,1,-1)`,

let `v=(v1,v2,v3) in R^3` with `||v||<1`, let `X` be any real random variable with probability density `f_X<=1`, and let

`G ~ N(0, sigma^2 (I-vv^T))`,   `sigma^2>=1/12`,

independently of `X`. Put

`Y=vX+G`,   `Q=Y^T JY`.

Write

`p=v1^2+v2^2`,   `q=v3^2`.

The preceding B17 cone-line calculation gives the exact reduction

`p_Q(0)/(3 sqrt(2)) <= (1/(2 pi)) int_0^(2 pi) H_s(a(theta)) dtheta`,      (2.1)

where

`s=12 sigma^2>=1`,

`omega(theta)=(cos theta,sin theta,1)/sqrt(2)`,

`a(theta)=||v||^2-(v.omega(theta))^2`,

`c(a)=12a/(1-a)`,

`F(u)=int_(-1/2)^(1/2) exp(-u x^2/2) dx`,

and

`H_s(a)=(1/s) F(c(a)/s)/sqrt(1-a)`.                                (2.2)

The only extremal input used in obtaining (2.1) is the one-dimensional bathtub inequality

`int f_X(x) exp(-D x^2/2) dx <= int_(-1/2)^(1/2) exp(-D x^2/2) dx`,

which is valid for every probability density `f_X<=1`.

## 3. New scalar lemma: a sharp global quartic penalty

### Lemma

For every `s>=1` and `0<=a<1`,

`H_s(a) <= 1 - (3/20)a^2`.                                         (3.1)

The coefficient `3/20` is sharp as `a downarrow 0`.

### Proof

As in the previous B17 proof, `u F(u)` is increasing on `[0,infinity)`. With `u=c(a)/s<=c(a)`,

`F(c(a)/s)/s = uF(u)/c(a) <= F(c(a))`,

so `H_s(a)<=H_1(a)`. It remains to prove (3.1) at `s=1`.

Set

`x=sqrt(3a/[2(1-a)])`, so `a=2x^2/(3+2x^2)`.

The Gaussian integral gives

`H_1(a)=sqrt(pi/(6a)) erf(x)`.

Thus (3.1) is equivalent to

`erf(x) <= R(x)`,                                                     (3.2)

where

`R(x)= [2 sqrt(3) x/(sqrt(pi) sqrt(3+2x^2))]`
`      * [1-3x^4/(5(3+2x^2)^2)]`.

Both sides vanish at zero. Direct differentiation simplifies exactly to

`(sqrt(pi)/2) R'(x)`
` = 3 sqrt(3) (x^4+12x^2+9)/(2x^2+3)^(7/2)`.                       (3.3)

Put `y=x^2` and

`A(y)=3 sqrt(3)(y^2+12y+9)/(2y+3)^(7/2)`.

Then `A(0)=1` and

`d/dy [log A(y)+y]`
` = 2 y^2 (y+12)/[(2y+3)(y^2+12y+9)] >=0`.                         (3.4)

Hence `A(y)>=exp(-y)`. By (3.3),

`R'(x) >= (2/sqrt(pi)) exp(-x^2)=erf'(x)`.

Together with equality at zero, this proves (3.2) and therefore (3.1).

Finally the Taylor expansion of the exact expression is

`H_1(a)=1-(3/20)a^2+O(a^3)`,

so the coefficient cannot be increased in a neighborhood of zero. QED.

## 4. Exact cone average and quantitative theorem

The angular second moment of `a(theta)` is elementary. Since

`E_theta (v.omega)^2 = p/4+q/2`,

and

`E_theta (v.omega)^4 = 3p^2/32+3pq/4+q^2/4`,

one obtains

`E_theta a(theta)^2`
` = 19p^2/32 + 5pq/4 + q^2/4`.                                    (4.1)

In particular

`E_theta a(theta)^2 - (p+q)^2/4`
` = 11p^2/32 + 3pq/4 >=0`.                                        (4.2)

Combining (2.1), (3.1) and (4.1) gives the new result.

### Theorem `QFORM-ONE-HEAVY-QUANTITATIVE-CENTRAL-GAP-v1`

Under the hypotheses of Section 2,

`p_Q(0)`
` <= 3 sqrt(2) [1 - 57p^2/640 - 3pq/16 - 3q^2/80]`                 (4.3)

and therefore, orientation-free,

`boxed( p_Q(0) <= 3 sqrt(2) [1-(3/80)||v||^4] )`.                  (4.4)

Equivalently, relative to the partner's sharp diffuse limiting witness,

`boxed( 3 sqrt(2)-p_Q(0) >= (9 sqrt(2)/80)||v||^4 )`.              (4.5)

Thus a single shared macroscopic physical row pays an explicit quartic central-density penalty; it cannot merely fail to improve the diffuse witness by an unspecified strict amount.

The direction-dependent coefficients are consistent with the earlier Edgeworth computation: for `v` in the positive spectral plane (`q=0`) the relative coefficient is `57/640`, while for `v` on the negative eigenline (`p=0`) it is `3/80`. These are exactly the leading quartic coefficients from the small-heavy-leverage expansion. In particular the orientation-free coefficient `3/80` is asymptotically sharp, attained to first nonzero order by `v=r e_3` as `r downarrow0`.

For reference, the weakest orientation-free envelope at `||v|| up to 1` is

`3 sqrt(2)*(77/80)=4.08354166135231...`,

only about `0.0204710` above the partner's exact finite shared-frame witness `4.06307061680604...`. This comparison is diagnostic only: the partner witness has several interacting macroscopic rows and lies outside the one-heavy theorem.

## 5. Exact finite target frames and the local-transfer gap is closed for uniform residual banks

Fix `v` with `||v||<1` and let

`B=(I-vv^T)^(1/2)`.

For each integer `m>=1`, form an `(1+3m) x 3` physical frame `R_m` whose first row is `v^T`, while for each `j=1,2,3` the row

`e_j^T B/sqrt(m)`

is repeated `m` times. Exactly

`R_m^T R_m=vv^T+B^2=I_3`.                                          (5.1)

Hence

`A_m=R_m J R_m^T`

has nonzero spectrum exactly `{1,1,-1}` for every finite `m`.

Take every physical input iid `Uniform[-1/2,1/2]`. If

`T_{j,m}=m^(-1/2) sum_(k=1)^m U_{j,k}`,

then the projected active vector is

`Y_m=vU_0+B T_m`,

where the three coordinates of `T_m` are independent.

### Proposition `QFORM-ONE-HEAVY-UNIFORM-LOCAL-TRANSFER-v1`

For every fixed `v` with `||v||<1`, the density at zero of

`Q_m=Y_m^T JY_m`

satisfies

`p_{Q_m}(0) -> p_Q(0)`                                              (5.2)

where `Q` is the Gaussian-residual model of Section 2 with `X=U_0` and `sigma^2=1/12`. Consequently, if `v!=0`,

`limsup_(m->infinity) p_{Q_m}(0)`
` <= 3 sqrt(2)[1-(3/80)||v||^4] < 3 sqrt(2)`.                       (5.3)

### Proof of the transfer

Let `h_m` be the density of `T_{j,m}`. Its characteristic function is

`phi_m(t)=sinc(t/(2sqrt(m)))^m`.

For `|t|<=2sqrt(m)`, the elementary bound `|sinc u|<=exp(-c u^2)` on `|u|<=1` gives an integrable Gaussian majorant for `phi_m`; for `|t|>2sqrt(m)`, `|sinc(t/(2sqrt(m)))|^m <= (2sqrt(m)/|t|)^m`, whose tail is uniformly integrable for `m>=3`. Fourier inversion and dominated convergence therefore give the uniform local CLT

`sup_x |h_m(x)-gamma_(1/12)(x)| ->0`.                               (5.4)

Moreover each `h_m` is symmetric log-concave, hence decreasing on `[0,infinity)`. Hoeffding gives

`P(T_{j,m}>=r)<=exp(-2r^2)`.

For `r>=1`, monotonicity yields

`h_m(r) <= int_(r-1)^r h_m(u)du <= exp(-2(r-1)^2)`.                 (5.5)

Together with a uniform central density bound from the Fourier estimate, (5.5) supplies an integrable radial envelope independent of `m`.

Since `B` is invertible for fixed `||v||<1`, the conditional densities of `vU_0+BT_m` converge uniformly to the corresponding conditional Gaussian densities, and (5.5) transforms into a common integrable line envelope. Apply the exact zero-cone identity

`p_{Q_m}(0)=(1/2) int_(C_+) int_R g_m(t omega) dt ds(omega)`

and dominated convergence to obtain (5.2). Combining with (4.4) proves (5.3). QED.

Thus the exact finite target family no longer relies only on weak convergence at the central level: for every fixed nonzero one-heavy geometry, its finite uniform approximants eventually remain a definite amount below the `3 sqrt(2)` diffuse ceiling.

## 6. What this changes, and what remains unpaid

The designated partner's infinitesimal theorem supplies the sharp benchmark `3 sqrt(2)` and isolates mixed/macroscopic leverage as an escape route. Equations (4.4)--(4.5) directly apply that benchmark and show that the first mixed mechanism — one physical coordinate shared across all three active spectral directions — actually loses at least quartically in its leverage. Section 5 shows the same conclusion is seen by an exact sequence of finite target matrices, not only by the limiting model.

The newer partner witness at `4.0630706...` is therefore correctly located beyond this mechanism: it uses several interacting macroscopic rows. The next sharp-constant/witness attack should switch to that genuinely different regime, preferably two or more macroscopic shared rows plus a diffuse residual and off-center levels. Repeating one-heavy central analysis is no longer the high-value branch.

Nothing here bounds `sup_t p_Q(t)` for the one-heavy model, controls arbitrary several-heavy-row residuals, or proves the full universal theorem. Continuity for the unrestricted target also remains separate and open.

## 7. Verification scope

`CHECK.py` verifies the exact rational angular coefficients, the derivative identity behind (3.3)--(3.4), the global scalar inequality on a dense diagnostic grid, the orientation-free reduction, and the numerical constants quoted above. It is an algebraic/diagnostic checker, not a substitute for the analytic proof.
