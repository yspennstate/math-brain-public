# B03 decoupled-time report: indefinite-pair Lorentz half-Riesz bridge

Run: `20260922T222730Z-fleet03-B03-QFORM-r20b`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **SUPPORTING THEOREM PROVED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and target

The full target remains: independent real coordinates with densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of `A` of magnitude at least one. No moment, support, log-concavity, Gaussian, or eigen-coordinate independence assumption is made.

This report proves a new original-coordinate branch for the assigned decoupled-time problem. It does **not** prove an exhaustive structural reduction from the bare three-large-eigenvalue hypothesis. Essential boundedness is obtained on the stated branch; continuity is not proved here.

The argument respects the live corrections: it does not use law-uniform pointwise quadratic-phase decay, does not condition on a sum/difference variable and assign it a false cap-one density, and does not rotate the independent input law.

## 2. Input: the complete physical-pair logarithmic envelope

Use the complete supporting theorem at

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Let `U,V` be independent cap-one variables and let

`F=(U,V) B (U,V)^T + 2 ell dot (U,V) + c`,

where `B` is real symmetric, invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)>0`,

and let `s0=c-ell^T B^{-1} ell` be the critical value after completing the pair. For every `r>0`, that theorem proves that `F` has a density satisfying a.e.

`p_F(s) <= A + B0 log_+(L/|s-s0|)`,                    (2.1)

where

`A=2 sqrt(2)/r`,  `B0=D^{-1/2}`,  `L=2 r^2/kappa`.      (2.2)

For completeness, the structure behind (2.1) is product-preserving. Outside `|By|<=r`, condition on an ORIGINAL coordinate and use the derivative of the one-dimensional quadratic. Inside, only Lebesgue geometry is rotated: after diagonalizing `B` in the integration variables the phase becomes `z1^2-z2^2`, then `u=z1+z2`, `v=z1-z2` gives `uv`; no post-rotation independence is asserted.

## 3. New theorem: an indefinite physical pair has a translation-uniform half-Riesz bound

### Theorem `QFORM-INDEFINITE-PAIR-LORENTZ-HALF-RIESZ-v1`

Under the hypotheses of Section 2,

`sup_t E |F-t|^{-1/2} <= C_ind (D kappa)^(-1/6)`,         (3.1)

with

`C_ind = 3 * 2^(8/3) = 19.048812623618392...`.          (3.2)

The estimate is uniform in the affine vector `ell` and the constant `c`.

### Proof

Let

`mu(lambda)=Leb{s: p_F(s)>lambda}`.

Probability normalization gives, for every `lambda>0`,

`mu(lambda) <= 1/lambda`.                                (3.3)

For `lambda>A`, (2.1) implies

`B0 log_+(L/|s-s0|) > lambda-A`,

hence

`|s-s0| < L exp(-(lambda-A)/B0)`.

Therefore

`mu(lambda) <= 2L exp(-(lambda-A)/B0)` for `lambda>A`.   (3.4)

For fixed target `t`, the kernel `k_t(s)=|s-t|^{-1/2}` has decreasing rearrangement

`k_t^*(u)=sqrt(2/u)`,                                    (3.5)

because `Leb{k_t>alpha}=2 alpha^{-2}`. Hardy--Littlewood and layer cake give

`int p_F(s)|s-t|^{-1/2} ds`
` <= sqrt(2) int_0^infinity p_F^*(u) u^{-1/2} du`
` = 2 sqrt(2) int_0^infinity sqrt(mu(lambda)) d lambda`. (3.6)

Use (3.3) on `(0,A]` and (3.4) on `(A,infinity)`:

`int_0^A sqrt(mu(lambda)) d lambda <= 2 sqrt(A)`,         (3.7)

while

`int_A^infinity sqrt(mu(lambda)) d lambda`
` <= sqrt(2L) int_0^infinity exp(-x/(2B0)) dx`
` = 2B0 sqrt(2L)`.                                       (3.8)

Substitution into (3.6) yields

`sup_t E|F-t|^{-1/2}`
` <= 4 sqrt(2A) + 8 B0 sqrt(L)`
` = 2^(13/4) r^(-1/2) + 2^(7/2) r / sqrt(D kappa)`.      (3.9)

The right side has the form `a r^{-1/2}+b r`. Its critical point is

`r_* = (a/(2b))^(2/3)=2^(-5/6)(D kappa)^(1/3)`.          (3.10)

At that point the second term equals one half of the first, and direct simplification gives

`min_r RHS(3.9)=3 * 2^(8/3) (D kappa)^(-1/6)`.           (3.11)

This proves (3.1). QED.

### Why the exponent is plausible

Under scalar dilation `B -> cB`, one has `D -> c^2 D` and `kappa -> |c| kappa`, so `(D kappa)^(-1/6) -> |c|^{-1/2}(D kappa)^(-1/6)`, exactly the half-Riesz homogeneity. This avoids the homogeneity error in the earlier designated-partner compiler.

## 4. Exact decoupled-time consequence

Let `F'` be an independent copy of `F` and `eta_F(t)=E exp(itF)`. The one-dimensional Riesz Fourier identity gives

`int_R |t|^(-1/2) |eta_F(t)|^2 dt`
` = sqrt(2 pi) E |F-F'|^(-1/2)`.                         (4.1)

Condition on `F'` and apply (3.1) with target `t=F'`:

`E |F-F'|^(-1/2) <= C_ind (D kappa)^(-1/6)`.             (4.2)

Consequently

`int_R |t|^(-1/2)|eta_F(t)|^2 dt`
` <= C_time (D kappa)^(-1/6)`,                           (4.3)

where

`C_time = sqrt(2 pi) C_ind`
`       = 47.74829232050979...`.                         (4.4)

This is a dependence-safe independent-copy estimate. If one writes the copy difference in sum/difference variables, each coordinate pair has the exact dependent law inherited from `(X,X')`; no independence between `X-X'` and `X+X'` is used anywhere.

## 5. Ambient density corollary via one original-coordinate square pivot

Let `Z` be one original coordinate, independent of all remaining original coordinates. Suppose a nonzero physical scalar pivot has been completed so that, after conditioning on a vector `W` of other original coordinates,

`Q = d ( Z + h(U,V,W) )^2 + R(U,V,W)`,                   (5.1)

with `d != 0`, and suppose the quadratic part of `R` in two ORIGINAL coordinates `(U,V)` is the same invertible indefinite symmetric matrix `B`. All couplings to `W` are allowed: after conditioning on `W` they merely change the affine vector and constant in the pair theorem.

For any fixed realization of `(U,V,W)`, the cap-one square pushforward gives the standard bound

`p_(d(Z+h)^2+r)(y) <= |d|^(-1/2) |y-r|^(-1/2)`.          (5.2)

Average (5.2), condition first on `W`, and apply (3.1) to the `(U,V)` pair. Then

`||p_Q||_infinity`
` <= C_ind |d|^(-1/2) (D kappa)^(-1/6)`
` = C_ind (|d|^3 D kappa)^(-1/6)`.                       (5.3)

Thus every interval `I` satisfies the linear small-ball estimate

`P(Q in I) <= C_ind (|d|^3 D kappa)^(-1/6) |I|`.         (5.4)

This branch allows arbitrary remaining dimension, arbitrary self-quadratic terms on `W`, and arbitrary pair-to-`W` couplings. It does not require the Schur remainder to have exact rank one, unlike the earlier exact-rank-three pair-log closure.

## 6. Designated partner fleet04/B03: exact admissible use

The designated partner handoff is


with canonical mathematics `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`.

Its advertised `QFORM-COLLISION-L2-COMPILER-v1` is false as stated: the displayed Cauchy--Schwarz manipulation loses a factor of `|t|^{1/2}` and has incorrect coefficient homogeneity. This was already source-validly corrected in B03 run r19; the false theorem is not used here.

The partner handoff does contain the valid elementary implication

`P(|Y-Y'|<=epsilon) <= 2 epsilon ||p_Y||_2^2`.            (6.1)

Applying (6.1) to the corrected r19 two-square estimate

`||p_(aZ^2+bW^2)||_2^2`
` <= 3 sqrt(3) M_Z M_W |ab|^(-1/2)`                      (6.2)

gives the actual partner-applied inequality

`P(|Y-Y'|<=epsilon)`
` <= 6 sqrt(3) M_Z M_W |ab|^(-1/2) epsilon`.             (6.3)

That is the strongest mathematically valid use of the designated completed handoff presently available; no invalid partner claim is silently resurrected.

## 7. What remains unpaid for the full conjecture

The new theorem removes one analytic obstruction: once a nonzero original-coordinate scalar pivot has an indefinite physical pair in its Schur residual, the pair itself supplies the translation-uniform half-Riesz smoothing needed for a linear density/small-ball estimate, even in arbitrary remaining dimension.

The full three-large-eigenvalue hypothesis still does **not** force a dimension-free lower bound on the certificate

`|d|^3 |det B| sigma_min(B)`.

Known live corrections, including the failure of a universal single-Schur rank-two extraction, prevent claiming otherwise. The first target-level debt is therefore structural/aggregate: combine this certificate with the paid diffuse/ridge/grouped-bank branches, or prove a product-preserving averaging principle that prevents all physical pivot/pair certificates from simultaneously collapsing under the three-large-eigenvalue hypothesis.

Full QFORM remains OPEN. Continuity remains OPEN in this branch.

## 8. Verification status

A finite arithmetic checker accompanies this report. It checks the optimizer in (3.10), the closed-form constant in (3.11), the time constant, and homogeneity under scalar dilation. The checker is not a substitute for the analytic proof above.
