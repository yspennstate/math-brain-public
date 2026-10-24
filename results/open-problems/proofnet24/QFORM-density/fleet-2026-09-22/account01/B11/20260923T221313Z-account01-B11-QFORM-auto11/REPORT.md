SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T22:13:13Z.
attacking: the unique-heavy-row endpoint by retaining the genuine original scalar inside the rank-two crossing Fourier argument, so its L2 Fourier mass supplies the missing half-power without any pointwise van-der-Corput claim.

# account01/B11 — original-hub chain + rank-two crossing

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **PROVED SUPPORTING ANALYTIC THEOREM / UNIQUE-HEAVY ALIGNED ENDPOINT PAID / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

No Gaussianity, log-concavity, moments, compact support, connected support, identical laws, diagonal-basis independence, conditional projection cap, or law-uniform pointwise oscillatory decay is used. The theorem below proves a continuous `C_0` density in its stated scope.

## 1. The new analytic receiver

Let `X` be one ORIGINAL scalar input, with density `f_X` satisfying `0<=f_X<=L_X`, independent of two disjoint original-coordinate product banks `Z` and `Y`.

Let `U in R^2` be a two-dimensional linear projection of `Z`, and `V in R^2` a two-dimensional linear projection of `Y`. Let

`M_U=||p_U||_infinity`,  `M_V=||p_V||_infinity`.

Let `ell(Z)` be any nonzero scalar linear form of the same `Z` bank, with density cap

`M_ell=||p_ell||_infinity`.

There is no assumption that `ell` is independent of `U`; it may use exactly the same original variables. Let `S` be an invertible real `2 x 2` matrix. Finally let `h(X), F(Z), G(Y)` be arbitrary measurable real functions for which the displayed random variable is defined, and put

`Q = h(X)+F(Z)+G(Y)+2 X ell(Z)+2 U^T S V`.                         (1.1)

### Theorem `QFORM-ORIGINAL-HUB-RANK2-CROSS-L1-v1`

The characteristic function of `Q` is integrable, hence `Q` has a bounded continuous density vanishing at infinity, and

`boxed: ||p_Q||_infinity <= 3 [ L_X M_U M_ell M_V / |det S| ]^(1/3).`  (1.2)

The key point is that the scalar incidence `X ell(Z)` is allowed to overlap completely with the same source bank that generates the active plane `U`.

### Proof

Fix a Fourier frequency `t`. Define

`psi_t(xi)=int f_X(x) exp(i t h(x)) exp(i xi x) dx`.                (1.3)

By Plancherel,

`int |psi_t(xi)|^2 dxi = 2 pi int f_X(x)^2 dx <= 2 pi L_X`.        (1.4)

Push the complex measure `exp(i t F(Z)) dP_Z` through the relevant linear projection. If the coefficient of `ell` has a component perpendicular to the two coefficient rows of `U`, normalize that component to a scalar projection `W`; otherwise omit `W`. Thus

`ell = r.U + delta W`,                                             (1.5)

where `(U,W)` is a linear image of the original `Z` bank. Let `a_t(u,w)` be the corresponding complex push-forward density. Absolute domination gives

`|a_t(u,w)| <= p_(U,W)(u,w)`.                                      (1.6)

Define

`A_t(u)=int a_t(u,w) psi_t(2 t ell(u,w)) dw`,                       (1.7)

with the evident two-dimensional version when `delta=0`. By Cauchy-Schwarz in `w`,

`|A_t(u)|^2`
` <= [int |a_t(u,w)|dw] [int |a_t(u,w)| |psi_t(2t ell)|^2 dw]`
` <= p_U(u) int p_(U,W)(u,w)|psi_t(2t ell)|^2 dw`.                 (1.8)

Integrating and using `p_U<=M_U`, followed by the scalar density cap of `ell`,

`||A_t||_2^2`
` <= M_U E |psi_t(2t ell)|^2`
` <= M_U M_ell int |psi_t(2t l)|^2 dl`
` <= pi L_X M_U M_ell / |t|`.                                     (1.9)

This is the new half-power. It is an integrated Plancherel estimate for the genuine original scalar `X`; it is not a pointwise quadratic-phase decay statement.

Likewise push `exp(i t G(Y)) dP_Y` to `V`; call the complex density `b_t(v)`. Then

`||b_t||_2^2 <= M_V`.                                              (1.10)

Using the Fourier convention `hat b(xi)=int exp(i xi.v)b(v)dv`, (1.1) gives

`phi_Q(t)=int_R2 A_t(u) hat b_t(2t S^T u) du`.                     (1.11)

Cauchy-Schwarz, the change of variables `xi=2t S^T u`, and Plancherel yield

`[int |hat b_t(2tS^Tu)|^2 du]^(1/2)`
` <= pi sqrt(M_V) / ( |t| sqrt(|det S|) )`.                        (1.12)

Combining (1.9) and (1.12),

`|phi_Q(t)|`
` <= min{1, K |t|^(-3/2)}`,                                       (1.13)

where

`K=pi^(3/2) [L_X M_U M_ell M_V / |det S|]^(1/2)`.                 (1.14)

Since

`int_R min(1,K|t|^(-3/2))dt = 6 K^(2/3)`,                         (1.15)

Fourier inversion gives

`||p_Q||_infinity <= (1/(2pi)) 6K^(2/3)`
` = 3 [L_X M_U M_ell M_V / |det S|]^(1/3)`.                       (1.16)

The same `L1` characteristic-function estimate gives a continuous `C_0` representative. QED.

## 2. Why this is the correct third-direction mechanism

A two-eigenvalue opposite-sign saddle can genuinely have the logarithmic density

`p_(2XY)(t)=log(1/(2|t|)),  0<|t|<1/2`,                            (2.1)

for centered unit uniforms. No bounded-density theorem is being inferred from that saddle alone.

In Theorem 1, the two-dimensional source-to-source crossing contributes the borderline Fourier factor `|t|^-1`. Retaining the genuinely independent original scalar `X` until after the complex push-forward gives the additional `|t|^-1/2` in (1.9). Thus the third physical incidence changes the aggregate envelope from the borderline `|t|^-1` scale to the integrable `|t|^-3/2` scale. The gain comes from Plancherel and the actual product provenance, not from a false law-uniform van-der-Corput estimate.

## 3. Exact canonicalization of the r42 unique-heavy row

Now consume account03/B11 r42 and the preceding account01/B11 finite-heavy reduction. In the surviving exact-rank-three H-side block write

`A_H = E C E^T`, `E^T E=I_3`, `sigma_min(C)>mu`, `mu=beta0 s`,     (3.1)

where

`beta0=289/15984=0.01808058058058058...`,                          (3.2)

and there is a unique heavy ORIGINAL row `i` with

`q=||E^T e_i||^2>3/4`,                                            (3.3)

while its physical diagonal satisfies

`|A_ii| < mu q/16`.                                                (3.4)

Put

`e1=(E^T e_i)/sqrt(q)`.                                            (3.5)

Choose `e2` in `e1^perp` along the transverse component of `C e1`, and let `e3` complete an orthonormal spectral basis. Then

`C = [[alpha,beta,0],[beta,c,d],[0,d,e]]`,                         (3.6)

where

`alpha=e1^T C e1=A_ii/q`,                                         (3.7)

and therefore

`|alpha|<mu/16`,                                                   (3.8)

while `||C e1||>=mu` gives

`boxed: |beta| > sqrt(255)/16 * mu = 0.9980449639... mu`.          (3.9)

Delete original coordinate `i`. Because the `i`th row of `E` is `sqrt(q)e1^T`, the coefficient vectors of the `e2` and `e3` projections on the remaining original coordinates are still exactly orthonormal. The remaining `e1` coefficient vector has norm

`epsilon=sqrt(1-q)<1/2`                                           (3.10)

and is orthogonal to both. Hence, for an orthonormal three-dimensional projection `(W,U1,U2)` of the remaining original product bank,

`E^T X_H = (sqrt(q) X_i + epsilon W)e1 + U1 e2 + U2 e3`.          (3.11)

This is an exact ORIGINAL-source representation; no rotated coordinate is declared independent of another rotated coordinate. Only `X_i` is independent of the remaining bank.

The scalar coefficient multiplying `X_i` in the internal cross term is

`ell = sqrt(q) [ alpha epsilon W + beta U1 ]`.                     (3.12)

Its original-coordinate coefficient norm is

`R_ell=sqrt(q) sqrt(beta^2+alpha^2 epsilon^2)`
`      > sqrt(765)/32 * mu`
`      =0.8643322929... mu`.                                       (3.13)

Thus the apparent nearly-null physical diagonal does **not** mean the original heavy scalar has lost its third-direction incidence: it retains a dimension-free linear coupling to the remaining product bank.

## 4. New paid endpoint: the heavy row is the exact cross-null direction

Let `B=A[H,T]` be the physical H-to-T crossing in the r42 collar. At the exact endpoint suppose

- `rank(B)=2`;
- the heavy spectral direction `e1` in (3.5) is the left null direction of `B`.

Then `B` restricted to `e1^perp` has the two nonzero crossing singular values `sigma1,sigma2`. The r42 lower bound is

`boxed: sigma1 sigma2 > kappa_* s^2`,                              (4.1)

where

`kappa_*=(34/111)(17/288)^2=0.001067256492603715...`.              (4.2)

Choose `U=(U1,U2)` on `e1^perp` and a two-dimensional orthonormal T-side projection `V` so that the cross term is `2U^T S V`, with

`|det S|=sigma1 sigma2`.                                           (4.3)

All other H-bank terms are absorbed into `F`, all T-bank terms into `G`, and the original heavy square into `h(X_i)`. Because `e1` is a left null direction, there is no `X_i`-to-T cross term. Therefore Theorem 1 applies exactly with `X=X_i` and the scalar form (3.12).

Using the completed orthogonal-projection density estimate `||p_projection||_infinity<=exp(k/2)` gives

`L_X<=1`, `M_U<=e`, `M_V<=e`, `M_ell<=sqrt(e)/R_ell`.              (4.4)

Equations (1.2), (3.13), and (4.1) therefore give

`||p_Q||_infinity`
` < 3 e^(5/6) [32/(sqrt(765) beta0 kappa_*)]^(1/3) / s`
` < boxed: 270.176/s`.                                             (4.5)

The density is continuous and vanishes at infinity.

This closes a genuine rough-product endpoint: `W` may be maximally dependent on `(U1,U2)` inside the same remaining product bank. It is not conditioned away. Its contribution is retained in the single linear form `ell`, and only the one-dimensional marginal density cap of that actual linear form is used.

## 5. Designated account02/B11 result applied to the live collar

Use the completed account02/B11 theorem `QFORM-3D-PROJECTION-CROSS-L2-v1`, canonical report commit

`25c25e15fa0f570e7b0b1a2a9fab0811eda07113`,

which gives, for the current three-dimensional crossing whenever `sigma3!=0`,

`||p_Q||_infinity <= 6 (sigma1 sigma2 |sigma3|)^(-1/3)`.           (5.1)

Combining the actual r42 inequality (4.1) with the concrete threshold

`|sigma3| >= beta0 s/8`                                            (5.2)

gives

`||p_Q||_infinity`
` < 6 [8/(kappa_* beta0)]^(1/3) / s`
` < boxed: 447.393/s`,                                             (5.3)

with a continuous density. This is the requested direct application of the designated partner result to an actual current inequality.

For a second concrete check, account02/B11's completed residual-shear theorem applies to

`Q_kappa=2ZX1+2X1Y1+2X2Y2+2kappa ZW`

and gives `||p_(Q_kappa)||_infinity<13` continuously for all `kappa`. At `kappa=0`, Theorem 1 with `X=Z`, `ell=X1`, `U=(X1,X2)`, `V=(Y1,Y2)`, `S=I` improves this exact endpoint to

`boxed: ||p_(Q_0)||_infinity <=3`.                                 (5.4)

The matrix of `Q_0` has eigenvalues `+sqrt(2),-sqrt(2),+1,-1,0`, so it is target-valid.

## 6. What is still unpaid

The unrestricted conjecture is still OPEN. The new theorem does not solve the general unique-heavy collar when the heavy spectral direction is not the exact left null direction of the rank-two crossing, nor the punctured case where the small third cross direction is nonzero and lies in the same T-bank projection as the active two-plane.

The first B11 implication is now:

`QFORM-UNIQUE-HEAVY-MISALIGNED-CROSSNULL-INTERPOLATION-v1`:

> retain the original scalar `X_i` and prove a uniform version of Theorem 1 when `X_i` also has a direct linear coupling to the T bank, or force a paid full-three-cross / physical-pair / aggregate-volume exit. The bound must remain uniform as the third cross singular value tends to zero and may not condition on a dependent same-bank residual scalar.

The exact aligned endpoint above shows that no new geometric curvature is needed there: the original heavy scalar's `L2` Fourier mass is already the missing half-power. The remaining issue is how to preserve that gain when the hub itself participates in the same right-bank crossing.

Arbitrary additional nonseparable spectrum beyond the exact-rank-three reduction remains a separate full-target bridge.

## 7. Source ledger

- account03/B11 r42 internal-curvature / finite-heavy reduction: `yspennstate/math-open-problems@7a95ce05ae4f99b5953663b28ba0a60ff7f0e36d`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T211204Z-account03-B11-QFORM-r42/REPORT.md`.
- preceding account01/B11 unique-heavy addendum: `yspennstate/math-open-problems@06c623136e28837dd2a94d716e99d915064ba4f2`.
- designated account02/B11 punctured-collar theorem: `yspennstate/math-open-problems@25c25e15fa0f570e7b0b1a2a9fab0811eda07113`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T201026Z-account02-B11-QFORM-auto11/REPORT.md`.
- projection-density cap used in (4.4): completed weighted orthogonal-projection theorem recorded in account01/B06 r40 and its cited source; no conditional density is used.

Full QFORM: OPEN. Full continuity: OPEN. New theorem and aligned endpoint: continuous `C_0` density proved.
