# Checks for affine convolution localization and extreme-law rigidity

Programme QFORM-DENSITY-3EIG-20260922, account02/B14, run 20260923T220530Z-account02-B14-QFORM-auto11.

## C1. Affine-mixture conditioning check
For fixed theta, `Z^T B Z + a(theta)^T Z + c(theta)` has exactly the same quadratic block `B`; only affine data change. The definition of `Lambda_B(mu)` takes a supremum over all affine data, so conditioning and integrating gives the same constant. No normalization of a localized active law occurs.

## C2. Convolution expansion check
For `X=Z+Y`,
`X^T B X + ell^T X + c = Z^T B Z + (ell+2 B Y)^T Z + (Y^T B Y+ell^T Y+c)`.
Thus arbitrary vector additive noise is a random-affine mixture after conditioning on `Y`. No moment of `Y` is used.

## C3. Mollification lower-semicontinuity check
If `mu_epsilon -> mu` in total variation, then for every fixed affine coefficient and every fixed bounded open interval `I` of positive length the corresponding pushforward interval probabilities converge. Hence for any `R<Lambda_B(mu)` choose one fixed test with ratio `>R`; the same test has ratio `>R-o(1)` under `mu_epsilon`. Therefore `Lambda_B(mu) <= liminf Lambda_B(mu_epsilon)`. Together with convolution monotonicity this proves exact convergence. No division by a TV error at an interval length tending to zero is used.

## C4. Extreme L1 identity check
For `f=1_E`, `|E|=1`, and any cap-one probability density `h`,
`||h-f||_1 = int_E(1-h)+int_{E^c}h = 2(1-int_E h)`.
With `h=g*nu`, Tonelli makes this exactly the `nu`-average of the same expression for translated `g`. Thus the identity is equality, not Jensen or an estimate.

## C5. Exact rigidity check
If `g*nu=1_E`, the average in C4 is zero, so `tau_y g=1_E` for `nu`-a.e. `y`. If two such shifts differ by nonzero `t`, then `1_E` is translation-invariant by `t` a.e. Since `1_E in L1` and its Fourier transform equals one at zero and is continuous, it is nonzero on a neighbourhood of zero; invariance gives `(exp(-it xi)-1) hat{1_E}(xi)=0` there, forcing `t=0`. Hence `nu` is a point mass.

## C6. Comb geometry check
For `E_N = union_{j=1}^N [4j,4j+1/N]`, any interval of length one meets at most one tooth. Therefore a translated unit-interval density has overlap at most `1/N` with `E_N`, giving exact L1 error at least `2(1-1/N)`. Smoothing `f_N` by a compact probability mollifier preserves the cap one and converges in L1, so the triangle-inequality smooth obstruction is valid.

## C7. Fixed-source D5 scope
The fixed source `FOURIER_ROUTE_REPORT.md` at `e5f71d79eff325201dd0274053d20268ce65b837` states the proved D5 bound `5 sqrt(2e) e_5(M^T M)^(-1/10)` for a disjoint cross block with no marginal condition; the global source conventions allow arbitrary self blocks and affine terms. Conditioning on translation/environment labels preserves the active cross block `M`, so the source theorem applies fibrewise with one constant. Numerically `5 sqrt(2e)=11.658219907985622`.

## C8. Fixed-source Theorem A scope
The same fixed source `COUNTEREXAMPLE_SEARCH.md` proves Theorem A for all eigenvalues of a three-dimensional matrix of modulus at least `sigma`, with affine terms allowed. For `A=I_3`, `sigma=1`, hence `||p_Q||_infinity <= 6 sqrt(pi)=10.634723105433096`. This applies to both the comb laws and their smooth cap-preserving mollifications.

## C9. Target/correction audit
No moments, support diameter, connected support, log-concavity, post-rotation independence, normalized fragment cap, pointwise oscillatory decay, or continuity are assumed. The comb construction is an obstruction to a proof reduction only, not a QFORM counterexample. The full conjecture remains open.
