SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T12:54:17Z.
attacking: a genuinely non-infinitesimal diffuse-leverage witness class — finitely many physical rows whose deterministic leverage vanishes but whose random spectral contributions remain order one — and the finite-stage off-tip spike obstruction.

# QFORM-DIFFUSE-TELEPORTER-GLOBAL-NOESCAPE-v1

## Status and exact scope

This report proves a new supporting sharp-witness exclusion. It does **not** prove the unrestricted QFORM conjecture. The full target remains: arbitrary independent real probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, bounded-support, log-concavity, diagonal-basis, or post-rotation-independence hypothesis is added to that target.

The theorem here concerns an exact-rank-three diffuse Parseval-frame witness class in which a vanishing-total-Gram set of physical coordinates is allowed to carry arbitrary persistent macroscopic randomness, while the complementary rows carry the minimum-variance centered interval core. The conclusion is global in the output level and rules out narrow finite-stage density spikes.

This class is deliberately outside the probabilistically-infinitesimal hypothesis of the earlier account02/B17 theorem `QFORM-VECTOR-INFINITESIMAL-SHARED-FRAME-NOESCAPE-v1`: an exceptional row may have an order-one random contribution with probability one even though its matrix leverage tends to zero.

Fresh owner control before this run was `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Execution context is `WITHOUT_VERIFIED_BRAIN`.

## 1. The theorem

Let `J=diag(1,1,-1)`. For each `m`, let `R_m` be an `n_m x 3` real matrix with rows `r_{mi}^T` and

`R_m^T R_m = I_3`,

and assume the deterministic leverage is diffuse:

`tau_m := max_i ||r_{mi}||^2 -> 0`.

Choose an exceptional set `E_m` and define its Gram contribution

`D_m := sum_{i in E_m} r_{mi} r_{mi}^T`.

Assume

`||D_m||_op -> 0`.

For `i notin E_m`, let `U_{mi}` be independent `Unif[-1/2,1/2]`. For `i in E_m`, let `X_{mi}` be arbitrary independent real random variables with probability densities bounded by one; all variables in the two groups are mutually independent. Put

`G_m := sum_{i notin E_m} r_{mi} U_{mi}`,

`H_m := sum_{i in E_m} r_{mi} X_{mi}`,

`Y_m := G_m + H_m = R_m^T X_m`.

Assume only that

`H_m => H`

for some (possibly singular, atomic, fragmented, or otherwise arbitrary) random vector `H` in `R^3`. Define the physical quadratic form

`A_m := R_m J R_m^T`,

`Q_m := X_m^T A_m X_m = Y_m^T J Y_m`.

Then every sufficiently large `Q_m` has a bounded continuous density `p_m`, and

`boxed( ||p_m - p_infty||_infty -> 0 )`,

where `p_infty` is the density of

`Q_infty := (G+H)^T J (G+H)`,

with `G~N(0,I_3/12)` independent of `H`. In particular,

`boxed( limsup_m ||p_m||_infty <= 3 sqrt(2) )`.

Moreover, the exact nonzero spectrum of every finite `A_m` is

`boxed({1,1,-1})`.

Thus this is a source-valid exact-spectrum theorem, not a Gaussian surrogate statement about a rotated input law.

## 2. Exact spectrum and source provenance

Because `R_m^T R_m=I_3`, the map `z -> R_m z` is an isometric embedding of `R^3` into the physical coordinate space. On `range(R_m)`,

`A_m R_m z = R_m J z`.

Hence `A_m|_{range(R_m)}` is unitarily equivalent to `J`; on the orthogonal complement it is zero. Therefore its nonzero eigenvalues are exactly `1,1,-1` for every `m`.

No spectral statement is asymptotic. The physical coordinates remain independent in the original basis. The three latent coordinates of `Y_m=R_m^T X_m` may be strongly dependent because a single physical row may load all three directions; no post-rotation independence is assumed or used.

## 3. The residual interval core converges to the minimum-variance Gaussian

The residual sum is centered. Its covariance is exactly

`Cov(G_m) = (1/12) sum_{i notin E_m} r_{mi} r_{mi}^T`

`          = (1/12)(I_3-D_m)`

`          -> I_3/12`.

The triangular array is automatically Lindeberg, since

`||r_{mi} U_{mi}|| <= (1/2) sqrt(tau_m) -> 0`

uniformly in every residual coordinate. The multivariate Lindeberg CLT therefore gives

`G_m => G ~ N(0,I_3/12)`.

For each `m`, `G_m` and `H_m` are independent. Since `G_m=>G` and `H_m=>H`, their joint characteristic functions factor and converge to the product; hence

`(G_m,H_m) => (G,H)`

with `G` independent of `H`, and consequently

`Y_m = G_m+H_m => G+H`.

The important point is that the exceptional contribution need not become small. It may remain completely non-Gaussian and order one. Only its *deterministic Gram footprint* is required to vanish, so the complementary interval core retains the full covariance floor `I_3/12`.

## 4. Partner theorem closes the limiting density obstruction

The completed account03/B17 affine-Gaussian theorem (`QFORM` report at commit `dcf8885d5153370cacfa246ad1e29fb06d971769`) states that if

`Z~N(h,Sigma)`, `Sigma >= sigma^2 I`,

and a symmetric matrix has at least three eigenvalues of modulus at least one, then

`||p_{Z^T A Z}||_infty <= 1/(2 sqrt(2) sigma^2)`.

At `sigma^2=1/12`, this is exactly `3sqrt(2)`.

Condition on the present arbitrary exceptional limit `H=h`. Then

`G+h ~ N(h,I_3/12)`,

so

`||p_{(G+h)^T J(G+h)}||_infty <= 3 sqrt(2)`

for every `h`. Averaging the conditional densities gives

`boxed( ||p_infty||_infty <= 3 sqrt(2) )`.

This use is genuinely distribution-free in the exceptional component: `H` need not have a density, finite moments, bounded support, or independent spectral coordinates. The only independence used is the original-source independence that makes `H_m` independent of the residual interval core.

The newest account03/B17 handoff (`20260923T113026Z-account03-B17-QFORM-auto11`) ruled out vanishing-intensity critical remote fragments to first order and identified a genuinely non-CLT/off-tip mechanism as the next sharp-witness stress. The present exceptional rows realize the opposite extreme from that vanishing-intensity regime: their spectral contributions remain order one with nonvanishing probability (indeed, in the explicit construction below, with probability one). The affine-Gaussian theorem is the partner result actually used in the inequality above.

## 5. Pinned Claude Theorem F pays the finite-stage local-spike gap

Weak convergence alone would not control `||p_m||_infty`: an increasingly narrow finite-stage spike could disappear in the weak limit. This was explicitly the unpaid gap in the earlier account02/B17 shared-frame theorem.

Here the completed pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, Theorem F (Fresnel-Brascamp-Lieb), applies directly to the *actual physical form*.

Write

`A_m = sum_{k=1}^3 lambda_k v_{mk} v_{mk}^T`,

where `lambda=(1,1,-1)` and the columns `v_{mk}` of `R_m` are orthonormal. Take the full physical coordinate set for Theorem F. Its Gram matrix is

`G_I = R_m^T R_m = I_3`,

and its normalized coordinate leverages are exactly

`r_{mi}^T G_I^{-1} r_{mi} = ||r_{mi}||^2 <= tau_m`.

Thus for all sufficiently large `m`, `tau_m<=1/2`, and Theorem F gives the law-uniform characteristic-function estimate

`boxed( |phi_m(t)| <= min{1,(4 pi)^(3/2) |t|^(-3/2)} )`.

This is a real source inequality for the arbitrary cap-one exceptional laws and the interval residual laws; no pointwise one-dimensional stationary-phase estimate is being asserted.

The majorant is integrable. If

`C=(4pi)^(3/2)`, `t_0=C^(2/3)=4pi`,

then

`int_R min{1,C|t|^(-3/2)} dt`

`= 2[t_0 + 2C t_0^(-1/2)]`

`= 24pi`.

Since `Y_m=>G+H`, the continuous mapping theorem yields

`Q_m=Y_m^T JY_m => Q_infty=(G+H)^T J(G+H)`.

Therefore `phi_m(t)->phi_infty(t)` pointwise. Passing to the pointwise limit in the same majorant also gives `|phi_infty(t)|` bounded by it. Hence dominated convergence yields

`||phi_m-phi_infty||_{L^1(R)} -> 0`.

Fourier inversion now gives bounded continuous densities and

`||p_m-p_infty||_infty`

`<= (1/(2pi)) ||phi_m-phi_infty||_1 -> 0`.

Combining this with the partner bound in Section 4 proves

`boxed( limsup_m ||p_m||_infty <= 3sqrt(2) )`.

This is the required application of a completed `e5f71d79...` source result to a real obstruction: Theorem F converts the weak-limit ceiling into a **global finite-source asymptotic density ceiling**, eliminating an otherwise uncontrolled local-spike mechanism.

## 6. Explicit adversarial teleporter witness

The theorem above is not merely abstract. There is a fully explicit shared-coordinate family whose exceptional rows violate probabilistic infinitesimality as strongly as possible.

Let

`v_1=(1,1,1)`,
`v_2=(1,-1,-1)`,
`v_3=(-1,1,-1)`,
`v_4=(-1,-1,1)`.

For integer `L>=2`, repeat the four rows

`r_{Lj}=v_j/(2 sqrt(L))`

for each of `L` repetitions. Since

`sum_{j=1}^4 v_j v_j^T = 4 I_3`,

the resulting `4L x 3` frame satisfies

`R_L^T R_L=I_3`.

Every row has exact leverage

`||r_{Lj}||^2 = 3/(4L) ->0`.

Take one row of each tetrahedral type as exceptional. Their aggregate Gram is exactly

`D_L = I_3/L ->0`.

Write

`r_{Lj}=s_L u_j`,

where

`s_L=sqrt(3)/(2sqrt(L))`, `u_j=v_j/sqrt(3)`.

Fix any four independent real random variables `Z_j` with bounded densities `g_j`, say `||g_j||_infty=M_j<infty`. On the exceptional physical coordinates define

`X_{Lj}=Z_j/s_L`.

Then the physical density is

`f_{Lj}(x)=s_L g_j(s_L x)`,

so

`||f_{Lj}||_infty <= s_L M_j <=1`

for all sufficiently large `L`. Yet the corresponding spectral contribution is exactly

`r_{Lj} X_{Lj} = u_j Z_j`,

which is independent of `L` and non-infinitesimal whenever `Z_j` is nondegenerate. Put centered unit intervals on all remaining `4L-4` physical coordinates.

Thus

`H_L = sum_{j=1}^4 u_j Z_j =:H`

for every `L`, while the residual interval core converges to `N(0,I_3/12)`. The physical supports of the exceptional variables expand like `sqrt(L)` when the `Z_j` are compactly supported and remain unbounded when the `Z_j` are unbounded. The inputs are independent and cap-one. The matrix

`A_L=R_L J R_L^T`

has exact nonzero spectrum `{1,1,-1}`. Every entry direction is genuinely shared: the tetrahedral rows load all three spectral coordinates.

Nevertheless

`boxed( limsup_{L->infty} ||p_{X_L^T A_L X_L}||_infty <=3sqrt(2) )`.

This stress family therefore rules out a source-valid counterexample mechanism in which vanishing-leverage coordinates are made physically broader by the reciprocal row scale so that an arbitrary macroscopic random vector survives in spectral space.

## 7. Why this is not covered by the old infinitesimal theorem

For a nondegenerate `Z_j`, choose `eps>0` with `P(|Z_j|>eps)>0`. For the exceptional row,

`||r_{Lj}X_{Lj}||=|Z_j|`.

Therefore

`P(||r_{Lj}X_{Lj}||>eps)=P(|Z_j|>eps)`

is independent of `L` and does not tend to zero. Hence the probabilistic-infinitesimal condition of `QFORM-VECTOR-INFINITESIMAL-SHARED-FRAME-NOESCAPE-v1` fails outright.

The present theorem pays exactly that missing case for a vanishing-total-Gram exceptional component with a minimum-variance diffuse interval complement. The old weak-limit theorem plus the new pinned Fourier majorant also explains why the previous "finite-row/local-limit spike" caveat disappears in this scoped class.

## 8. What remains unpaid

The unrestricted QFORM conjecture is still OPEN. This theorem does not cover all ways to violate probabilistic infinitesimality. In particular, it does not settle:

1. an exceptional set whose aggregate Gram does **not** vanish, i.e. genuine intermediate/macroscopic matrix leverage interacting with a diffuse residual;
2. a non-infinitesimal exceptional aggregate `H_m` that is not tight or has no convergent subsequence relevant to the quadratic peak;
3. an arbitrary residual product law outside the minimum-variance interval/covered Gaussian-core classes when no independent `N(0,I/12)` convolution factor has been established;
4. additional active spectral directions or full-matrix tails not reducible to an exact rank-three Parseval representation;
5. a candidate finite-dimensional peak above `3sqrt(2)` — which would refute the proposed sharp constant but would not by itself refute existence of a larger universal QFORM constant.

The next sharp-witness attack should therefore move to a genuinely nonvanishing exceptional Gram / intermediate-leverage core, or to a full-matrix construction outside exact rank three. Repeating finite-activity Poisson fragmentation, Lindeberg diffuse limits, or fixed finite teleporters would now be redundant.

## 9. Deterministic verification

A deterministic calculation checked the explicit tetrahedral family for `L=2,5,20`: Parseval error was at machine precision; maximum leverages were respectively `0.375`, `0.15`, `0.0375`; the three nonzero eigenvalues were numerically `-1,1,1`; and the one-repetition exceptional Gram equaled `I/L` to machine precision.

It also checked the pinned Fourier-envelope constants:

`(4pi)^(3/2)=44.54662397465366...`,

`t_0=4pi=12.56637061435917...`,

`int min(1,(4pi)^(3/2)|t|^(-3/2)) dt = 24pi = 75.39822368615503...`,

and therefore the raw inversion ceiling from Theorem F is `12`, while the partner Gaussian-mixture endpoint improves the limiting sharp ceiling to

`3sqrt(2)=4.242640687119286...`.

These computations are sanity checks; the proof is the exact algebra and the two completed analytic inputs above.

## 10. Classification

Result: `SUPPORTING_ANALYTIC_WITNESS_CONSTRAINT`.

New theorem: `QFORM-DIFFUSE-TELEPORTER-GLOBAL-NOESCAPE-v1`.

Independent complete review: **not performed in this run**.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

Full-target continuity: **OPEN**; continuity proved here only for this scoped family for all sufficiently large indices.
