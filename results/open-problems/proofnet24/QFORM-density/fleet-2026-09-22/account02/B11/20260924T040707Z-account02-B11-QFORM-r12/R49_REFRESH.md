# account02/B11 r12 — partner-r49 refresh: pure null-coloop closure

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING THEOREM / PURE NULL-COLOOP ENDPOINT CLOSED / FULL QFORM OPEN**.

This is an immutable addendum to the r12 report. The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. Continuity remains separate. No moments, bounded support, log-concavity, iid hypothesis, spectral-coordinate independence, post-rotation independence, or two-sheet X-ray transfer is used.

## 1. Later designated-partner input actually consumed

After the base r12 report was written, the completed designated-partner result account03/B11 r49 became available. Its theorem `QFORM-R48-CANCELLATION-XRAY-IMPOSSIBILITY-v1` proves that the r48 exact nonlinear cancellation density has infinite all-direction essential X-ray norm, whereas a genuine residual orthogonal product projection has uniformly bounded two-dimensional marginals/X-rays. Hence the r48 cancellation law cannot be the residual product projection in the hard chamber.

The owner-required pinned package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was also consumed in this run. The quantitative source input used below is its completed two-dimensional product-projection marginal bound appearing in the proof of ruled Theorem C: every two-dimensional orthogonal projection of independent one-dimensional cap-one laws has joint density at most `2`. Its Theorem C is separately applied in Section 4 at the correct one-sheet sign.

The base r12 affine receiver is retained:

`Q = 2 beta X C + alpha C^2 + 2 delta C D + gamma D^2 + affine`,

with `X` independent of `(C,D)`, `||f_X||_infinity<=F`, `||g_(C,D)||_infinity<=M`, and `beta gamma !=0`, satisfies

`||p_Q||_(infinity,ess) <= 3 (2 M F)^(2/3) |beta^2 gamma|^(-1/3)`.

No independence inside `(C,D)` is required.

## 2. Dimension-free endpoint theorem

### Theorem — `QFORM-PURE-NULL-COLOOP-PAIRCAP-v1`

Let

`A = R M R^T`, `R^T R = I_3`,

be exact rank three, and suppose every eigenvalue of the symmetric invertible `M` has magnitude at least `s>0`. Assume an ORIGINAL coordinate `0` satisfies both

`||r_0||^2 = 1`,
`A_00 = 0`,

where `r_0` is the corresponding row of `R`. Then for arbitrary mutually independent original coordinates whose densities are bounded by one,

`boxed:
 ||p_(X^T A X)||_(infinity,ess)
 <= 3 * 2^(4/3) * |det M|^(-1/3)
 <= 3 * 2^(4/3) / s
 = 7.559526299369239... / s.`

This estimate is dimension-free and has no leaf-leverage, finite-support, or individual Pluecker-atom hypothesis.

### Proof

Rotate only the three-dimensional spectral bookkeeping so that `r_0=e_1`. Parseval gives

`sum_i r_i r_i^T = I_3`.

Because `||r_0||=1`,

`sum_(i!=0) r_i r_i^T = I_3-e_1e_1^T`.

The `(1,1)` entry of this positive-semidefinite identity is zero, hence every residual row has zero first component. Write

`r_i=(0,b_i)`, `b_i in R^2`, `i!=0`.

Then

`sum_(i!=0) b_i b_i^T = I_2`.

Also `A_00=e_1^T M e_1=0`, so

`M=[[0,m^T],[m,N]]`.

Invertibility forces `m!=0`. Rotate only the transverse spectral plane so that `m=(beta,0)`, `beta=||m||>0`. In these bookkeeping coordinates

`M = [[0,beta,0],
      [beta,alpha,delta],
      [0,delta,gamma]]`.

Its determinant is

`det M = - beta^2 gamma`,

so `gamma!=0`.

Define the residual linear forms

`(C,D) = sum_(i!=0) b_i X_i`.

The two coefficient rows are orthonormal because `sum b_i b_i^T=I_2`. Thus `(C,D)` is a genuine two-dimensional orthogonal projection of the residual ORIGINAL product source. The completed pinned product-projection theorem gives

`||g_(C,D)||_infinity <= 2`.

Moreover `(C,D)` is genuinely independent of the original coordinate `X_0`; no independence between `C` and `D` is asserted or needed. The full quadratic form is exactly

`X^T A X = 2 beta X_0 C + alpha C^2 + 2 delta C D + gamma D^2`.

Apply the affine null-scalar/dependent-pair receiver with `F=1`, `M=2`:

`||p||_infinity
 <= 3 * 4^(2/3) * |beta^2 gamma|^(-1/3)
 = 3 * 2^(4/3) * |det M|^(-1/3)`.

Finally `|det M|` is the product of the three nonzero eigenvalue magnitudes, so `|det M|>=s^3`. QED.

## 3. Sign-specific Schur meaning and the rank-two logarithm

The leading block

`[[0,beta],[beta,alpha]]`

is hyperbolic. Its inverse has lower-right entry zero, so the Schur complement of the third direction is exactly `gamma`; consequently `gamma>0` gives signature `(2,1)` and `gamma<0` gives `(1,2)`. The shear `delta` moves the sheets but does not change the determinant currency `-beta^2 gamma`.

The theorem does not hide the rank-two endpoint. Set `alpha=delta=gamma=0`, choose centered unit-uniform `X_0,X_1,X_2`, and take

`C=(X_1-X_2)/sqrt(2)`.

Then

`p_C(c)=sqrt(2)(1-sqrt(2)|c|)` for `|c|<=1/sqrt(2)`,

so `p_C(c)>=1/sqrt(2)` on `|c|<=1/(2sqrt(2))`. For

`R=2 beta X_0 C`,

the product-density formula gives, for sufficiently small nonzero `t`,

`p_R(t) >= [1/(sqrt(2)|beta|)] log(|beta|/(2sqrt(2)|t|)) -> infinity`.

Restoring `gamma D^2` does NOT make `C,D` independent. Instead the receiver keeps their joint projection density and uses the genuinely nonzero Schur curvature `gamma`: the reciprocal hyperbolic slope has weak endpoint size, while quadratic inversion in `D` supplies the extra half-power, producing a `u^(-3/2)` superlevel estimate and hence the determinant-homogeneous `|det M|^(-1/3)` bound. Exactly at `gamma=0`, the determinant vanishes and the logarithm is allowed to survive.

## 4. Required pinned ruled result at its exact sign scope

For the same exact-rank-three pure-coloop form, the completed pinned ruled Theorem C gives

- signature `(2,1)`: `p_Q(t) <= pi sqrt(2)/s` on the one-sheet side `t>=0`;
- signature `(1,2)`: after negating the form, `p_Q(t) <= pi sqrt(2)/s` on the one-sheet side `t<=0`.

No X-ray argument is transferred to the opposite two-sheet side. The full-line pair-cap theorem above pays that side as well.

## 5. Consequence for the r12 Pluecker frontier

The base r12 Pluecker theorem paid the null-pivot chamber whenever one fixed transverse physical atom survived, and showed that a blow-up sequence must have `omega_* -> 0`. The present theorem removes that diffuse aggregation debt completely at the **pure-coloop endpoint `q=1`**: there one should aggregate all transverse leaves first into the genuine two-dimensional product projection `(C,D)`, whose density cap is universal, rather than selecting any individual Pluecker atom.

Partner r49 also closes the strongest previously known cancellation mimic: its r48 nonlinear law has infinite all-direction X-ray norm and therefore cannot be a genuine residual orthogonal product projection. Thus neither a fixed physical transverse atom nor the r48 exact nonlinear hiding mechanism survives as an obstruction at `q=1`.

## 6. First unpaid implication after the r49 refresh

`QFORM-NEAR-COLOOP-PARABOLIC-PRODUCT-TRACE-v1`:

In the exact-rank-three null-pivot chamber with leverage `q<1` but `q` close to one, write after spectral bookkeeping

`Z_1 = sqrt(q) X_0 + sqrt(1-q) T`,

where `(T,C,D)` is a genuine three-dimensional orthonormal projection of the residual original product bank. After transverse alignment the form has

`2 beta sqrt(q) X_0 C
 + 2 beta sqrt(1-q) T C
 + alpha C^2 + 2 delta C D + gamma D^2`,

with `|beta^2 gamma|=|det M|` and puncture ratio `sqrt((1-q)/q)`.

Prove a full-line bound uniform as `q -> 1` by spending the exact product factorization of `(T,C,D)` before any dependence-blind marginal split, while retaining the `T C` puncture; or force an already-paid physical-pair/volume/source-disjoint exit.

At `q=1` the `T C` term vanishes and the theorem above closes the chamber. Partner r49 proves that the r48 nonlinear exact-cancellation law is not an admissible product projection, but the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction still forbids replacing the remaining `q<1` problem by generic X-ray control. The unpaid step is therefore a genuinely product-Fourier/parabolic-trace interpolation, not a missing endpoint estimate.

Separately unpaid: the nonzero physical-pivot collar, arbitrary additional nonseparable spectrum, and full-target continuity.