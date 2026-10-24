# QFORM account01/B13 r15 — fractional ridge synthesis and pivot-diffuse Schur branch

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260922T173038Z-account01-B13-qform-r15`.
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET BRANCH; FULL CONJECTURE OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and source pins

Full target: for every dimension, every independent real input with coordinate densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal finite density bound for `Q=X^TAX`, or give a valid counterexample.

This report uses, and re-derives the needed part of, the free-regularizer ridge estimate from

- `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

The designated partner result actually applied is account02/B13's exact bang-bang purification theorem

- `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`.

It says that for every fixed measurable kernel, in particular every quadratic slab indicator, the supremum over cap-one product densities equals the supremum over products of measure-one indicator sets, with no loss. The finite-union approximation is also exact at the supremum level. I use this at the end to turn the new analytic branch into an exact geometric product-set slab inequality.

The live corrections used here are: no law-uniform pointwise one-dimensional quadratic decay; no post-rotation independence; no use of an unrestricted fiber supremum or fabricated conditional cap; no selection of a single uniformly good local minor. The argument stays in original coordinates.

## 2. Starting characteristic-function estimate

Let `R` be an arbitrary quadratic form in independent cap-one coordinates. Let `I,J` be disjoint original-coordinate sets and `B` the `I x J` cross block of the matrix of `R`. For `gamma>0` define

`K = B B^T (gamma^2 I + B B^T)^(-1)`,
`theta = tr K`,
`D = det(I + B B^T/gamma^2)`.

For `1<=q<=2`, assume

`max_i K_ii <= q/2`.

The graph/BL estimate in the cited ridge report gives, without any hypothesis on the self blocks or outside couplings,

`|phi_R(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`,

where

`L_q = pi e sqrt(2/q)`.

This estimate itself does **not** require `theta>2q`; that stronger condition was only needed there to make `phi_R` integrable for a density bound.

Set

`beta = theta/(2q)`,
`t0 = [L_q/(2 gamma)] D^(-1/(2 theta))`.

Then for all `t`,

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`.

## 3. New theorem: fractional ridge half-Riesz certificate

### Theorem QFORM-FRACTIONAL-RIDGE-HALF-RIESZ-v1

Under the preceding hypotheses, if only

`theta > q`,

then

`sup_s E |R-s|^(-1/2)`
` <= 2 sqrt(e) (2/q)^(1/4) gamma^(-1/2)`
`    * [theta/(theta-q)] D^(-1/(4 theta))`.

In particular, since `log D >= theta`,

`sup_s E |R-s|^(-1/2)`
` <= 2 e^(1/4) (2/q)^(1/4) gamma^(-1/2) theta/(theta-q)`.

This is a genuine gain over the density criterion: the effective ridge dimension threshold drops from `theta>2q` to `theta>q`.

### Proof

With Fourier convention `hat f(t)=int exp(itx)f(x)dx`, the one-dimensional Riesz kernel satisfies, in tempered distributions,

`widehat{|x|^(-1/2)}(t) = sqrt(2 pi) |t|^(-1/2)`.

Because `beta>1/2` is exactly `theta>q`, the weighted transform

`|t|^(-1/2) phi_R(t)`

is absolutely integrable. Hence the convolution of the law of `R` with `|.|^(-1/2)` is a bounded continuous function and Fourier inversion gives

`E|R-s|^(-1/2)`
` <= 1/sqrt(2 pi) int_R |t|^(-1/2)|phi_R(t)| dt`.

Using the envelope above,

`int_R |t|^(-1/2) min(1,(t0/|t|)^beta) dt`
` = 2[ int_0^t0 t^(-1/2)dt + t0^beta int_t0^infinity t^(-beta-1/2)dt ]`
` = 4 sqrt(t0) beta/(beta-1/2)`.

Since `beta/(beta-1/2)=theta/(theta-q)`, substitution of `t0` yields

`4/sqrt(2pi) * sqrt(L_q/(2gamma))`
` = 2 sqrt(e) (2/q)^(1/4) gamma^(-1/2)`,

which proves the first bound. Finally `log(1+x)>=x/(1+x)` summed over the singular-value ratios gives `log D>=theta`, and therefore `D^(-1/(4theta))<=e^(-1/4)`. QED.

## 4. New theorem: one physical pivot plus a fractional-ridge Schur bank gives a density

Let `i` be an original physical coordinate with

`a=A_ii != 0`,
`b=A_{i,-i}`,
`S=A_{-i,-i}-b b^T/a`.

Then

`Q = a (X_i + b^T X_{-i}/a)^2 + X_{-i}^T S X_{-i}`.

Conditioning on `X_{-i}=y`, the shift in `X_i` does not change its density cap. The elementary square change of variables gives, for every `t`,

`p_{Q | X_{-i}=y}(t)`
` <= |a|^(-1/2) |t-y^T S y|^(-1/2)`.

Therefore

`||p_Q||_infinity`
` <= |a|^(-1/2) sup_t E |X_{-i}^T S X_{-i}-t|^(-1/2)`.

Apply the preceding fractional-ridge theorem to **any** original-coordinate cross block `B=S[I,J]`, with all remaining coordinates retained as arbitrary self/outside terms. If

`max diag K_gamma <= q/2`, `theta_gamma>q`,

then

`||p_Q||_infinity`
` <= 2 sqrt(e) (2/q)^(1/4) (|a| gamma)^(-1/2)`
`    * theta_gamma/(theta_gamma-q) D_gamma^(-1/(4theta_gamma))`.

This is the branch theorem `QFORM-PIVOT-FRACTIONAL-RIDGE-v1`. It preserves every original-coordinate product law and permits arbitrary higher-rank quadratic curvature in the Schur remainder. No rotation of the independent inputs occurs.

## 5. Two-eigenvalue spectral-window half-Riesz theorem

The three-eigenvalue spectral-window density theorem can now be repeated one order lower because only a half-Riesz bound is required.

### Theorem QFORM-TWO-EIGEN-SPECTRAL-WINDOW-RIESZ-v1

Let `S` be symmetric and suppose it has at least two eigenvalues with absolute value at least `sigma>0`. Let `P` project onto all eigenspaces of `S` with `|lambda|>=sigma/64`. If

`max_i P_ii <= 1/32`,

then for independent cap-one inputs

`sup_t E |X^T S X-t|^(-1/2)`
` <= [64 sqrt(2) e^(1/4)/sqrt(13)] sigma^(-1/2)`
` < 32.233 sigma^(-1/2)`.

### Proof

Write `S=S_H+E`, where `||E||<=sigma/64` and `S_H=U Lambda_H U^T` on the window. MSS two-part frame partitioning with row norms squared at most `1/32` gives a partition `I,J` with

`(7/32) I <= U_I^T U_I, U_J^T U_J <= (25/32) I`.

Thus the window cross block `B0=S_H[I,J]` has at least two singular values at least `(7/32)sigma`. After adding `E[I,J]`, the full cross block `B=S[I,J]` has

`s_2(B) >= (7/32-1/64)sigma = 13 sigma/64 =: s`.

As in the cited ridge-window proof, `range(B0)=range(U_I)` and its projection has diagonal at most `1/7`. Choose

`gamma=s/sqrt(2)`.

The perturbative ridge-leverage estimate gives

`max_i K_ii <= (1/sqrt(7)+sqrt(2)/13)^2 < 1/2`.

The two singular values at least `s` contribute

`theta >= 2 s^2/(gamma^2+s^2)=4/3>1`.

Apply the fractional-ridge theorem with `q=1`. Since `theta/(theta-1)<=4`,

`sup_t E|X^T S X-t|^(-1/2)`
` <= 8 e^(1/4) 2^(1/4) gamma^(-1/2)`
` = 64 sqrt(2)e^(1/4)/sqrt(13) * sigma^(-1/2)`.

QED.

## 6. Consequence for the full three-large-eigenvalue problem: pivot-diffuse Schur branch

Assume now the owner target `s_3(A)>=1`. For a nonzero physical pivot `a=A_ii`, write `rho=||b||_2/|a|` and use the Schur complement `S` above. The exact shear factorization is

`A = L^T diag(a,S)L`,
`L = [[1, b^T/a],[0,I]]`.

Since `||L||<=1+rho`, singular-value ideal inequalities give

`s_3(diag(a,S)) >= s_3(A)/||L||^2 >= (1+rho)^(-2) =: sigma`.

The scalar block `a` can account for at most one singular value of `diag(a,S)`, so `S` has at least two eigenvalues of absolute value at least `sigma`.

Therefore, if the spectral projection of `S` onto

`|lambda(S)|>=sigma/64`

has maximum physical-coordinate leverage at most `1/32`, then

`||p_Q||_infinity`
` < 32.233 / sqrt(|a| sigma)`
` = 32.233 (1+rho)/sqrt(|a|)`.

This is `QFORM-PIVOT-DIFFUSE-SCHUR-v1`.

It is a genuine arbitrary-dimensional target branch: all additional eigenvalues, self interactions and couplings are retained. The only extra condition is the stated diffuse Schur-window leverage.

## 7. Actual application of account02/B13's extremal-product theorem

For every matrix in the preceding branch and every interval `J`, account02/B13's exact purification identity gives

`sup_{0<=f_i<=1, int f_i=1} P_f(Q in J)`
` = sup_{|E_i|=1} |{x in prod_i E_i : Q(x) in J}|`.

Since the analytic proof above gives the density bound for every cap-one product law, it follows equivalently that every product of measure-one sets satisfies the geometric slab inequality

`|{x in prod_i E_i : Q(x) in J}|`
` < 32.233 (1+rho)/sqrt(|a|) * |J|`

on the pivot-diffuse Schur branch. By the same partner theorem, the supremum is unchanged if every `E_i` is a bounded finite union of intervals. This is an actual use of the designated partner theorem in the new inequality, with zero constant loss.

## 8. What changed and what remains unpaid

Old missing implication: the free-regularizer ridge argument needed effective dimension `theta>2q`, so a rank-two cross bank could not by itself pay a density. This blocked the natural `one physical square + two-dimensional aggregate remainder` route.

New implication proved here: after one genuine physical square is kept, the remainder only needs a **half-Riesz** bound, and the exact same ridge graph estimate requires only `theta>q`. Consequently a diffuse two-eigenvalue Schur window is enough.

The remaining full-target obstruction is now sharper. A still-unpaid form must avoid this branch at every useful nonzero physical pivot: after Schur complementation, its two-eigenvalue window must have a coordinate with leverage greater than `1/32`, or the pivot resource `|a|/(1+rho)^2` must become quantitatively negligible. This is an original-coordinate high-leverage/zero-pivot grouped-aggregation problem, not a residual rank-two fractional-trace problem.

Suggested next implication:

`QFORM-HIGH-LEVERAGE-SCHUR-ITERATION-v1`: from failure of `QFORM-PIVOT-DIFFUSE-SCHUR-v1`, use the resulting concentrated Schur-window coordinate to produce either (a) a second physical pivot with controlled shear resource, or (b) a grouped bilinear/null-ray bank already covered by the completed aggregate theorems, without replacing product provenance by a conditional density cap.

Full conjecture remains **OPEN / NOT PROVED**. This report does not claim continuity in the new branch beyond what separately follows if a later argument establishes an integrable characteristic function.
