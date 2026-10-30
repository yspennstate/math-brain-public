# B04 addendum — non-isotropic large-row Schur/fractional closure

This addendum is a direct attack on the first unpaid implication left by `ADDENDUM_1PLUS2.md`: remove the exact spectral-zero-pattern requirement in a genuine high-leverage rank-three state.

## Theorem `QFORM-LARGE-ROW-SCHUR-FRACTIONAL-v1`

Let

`A = U Lambda U^T`,

where `U` is `n x 3` with `U^T U=I_3`, and `Lambda` is an invertible real diagonal `3 x 3` matrix. Write the rows of `U` as `u_1,...,u_n in R^3`. Let the physical input coordinates be independent with densities bounded by one.

Fix a row `u=u_i`, put

`r=||u||_2`,
`a=u^T Lambda u`,

and assume `a!=0`. Let `P` be any `3 x 2` matrix whose columns form an orthonormal basis of `u^perp`. Assume the **projected residual leverage** condition

`max_{j!=i} ||P^T u_j||_2 <= 1/2`.                                            (1)

Let `B_RV` be the absolute small-coordinate Brascamp--Lieb Fourier constant used in fleet02/B02, so an orthonormal two-dimensional product projection with row norms at most `1/2` has characteristic-function `L^1` norm at most `B_RV^2`.

Then `Q=X^TAX` has a bounded density satisfying

`||p_Q||_infinity
 <= 4 B_RV / { pi 3^(1/4) [ |a| r^2 |det Lambda| ]^(1/4) }.`                  (2)

In particular, if `|lambda_k|>=1`, `r>1/2`, and `|a|>=eta>0`, then

`||p_Q||_infinity <= 4 sqrt(2) B_RV /(pi 3^(1/4) eta^(1/4))`.                  (3)

No spectral-coordinate independence after rotation is assumed. The distinguished physical variable can couple to all three eigenvectors.

### Proof

Write

`Z = sum_{j!=i} u_j X_j`,

so the three-dimensional spectral coordinate is `Y=u X_i+Z` and

`Q = a X_i^2 + 2 X_i u^T Lambda Z + Z^T Lambda Z`.

Because `a!=0`, complete the square:

`Q = a (X_i+c(Z))^2 + Z^T H Z`,                                               (4)

where

`c(Z) = u^T Lambda Z/a`,
`H = Lambda - (Lambda u)(Lambda u)^T/a`.

The shift `c(Z)` is correlated with the residual quadratic term. The point of the argument is that we do **not** discard this dependence by asking for a pointwise oscillatory bound.

Since `H u=0` and `H` is symmetric of rank two, there is an invertible symmetric `2 x 2` matrix

`Gamma=P^T H P`

such that

`Z^T H Z = (P^T Z)^T Gamma(P^T Z)`.                                           (5)

Now the residual rows `v_j=P^T u_j`, `j!=i`, form an exact orthonormal two-frame:

`sum_{j!=i} v_j v_j^T
 = P^T(I-u u^T)P
 = I_2`,                                                                        (6)

because `P^T u=0`. By (1), fleet02/B02's proof-level Rudelson--Vershynin estimate applies and gives

`||Phi_{P^T Z}||_{L^1(R^2)} <= B_RV^2`.                                       (7)

The two-dimensional Fresnel transfer therefore gives the residual quadratic characteristic function `psi_H(t)` the pointwise bound

`|psi_H(t)| <= C_H |t|^(-1)`,
`C_H = B_RV^2/[4 pi sqrt(|det Gamma|)]`.                                       (8)

Together with `|psi_H|<=1`,

`||psi_H||_{3/2} <= (6 C_H)^(2/3)`.

Inverse Hausdorff--Young then shows that the residual quadratic variable

`W=Z^T H Z`

has a density `g` with

`||g||_3
 <= (2pi)^(-2/3)(6C_H)^(2/3)
 = (3C_H/pi)^(2/3).`                                                           (9)

We next use only a uniform density envelope for the first term in (4). Conditional on `Z`, the random variable `a(X_i+c(Z))^2` has density `k_Z` bounded by

`k_Z(s) <= 1/[sqrt(|a|) sqrt(|s|)]`                                            (10)

on the half-line with sign `sign(a)`, and zero on the other half-line. The singularity is always at `s=0`; its location does not depend on the correlated shift `c(Z)`.

Hence, for every `y`, disintegration over `Z` gives

`p_Q(y)
 <= |a|^(-1/2) int_0^infinity s^(-1/2) g(y-sign(a)s) ds`.                      (11)

This is where the correlated shift disappears **without** taking a fiber supremum.

We need the following elementary one-sided fractional estimate. If `g` is a probability density in `L^3(R)`, then

`sup_y int_0^infinity s^(-1/2)g(y-s)ds
 <= 8*3^(-3/4) ||g||_3^(3/4)`.                                                (12)

Indeed, split the integral at `R>0`. Hölder on `(0,R)` gives

`<= 2^(4/3)||g||_3 R^(1/6)`,

while the tail is at most `R^(-1/2)`. Optimizing at

`R=(3/[2^(4/3)||g||_3])^(3/2)`

gives (12).

Combining (9)--(12),

`||p_Q||_infinity
 <= |a|^(-1/2) * 8*3^(-3/4)
    * (3C_H/pi)^(1/2)
 = 4 B_RV/[pi 3^(1/4) sqrt(|a|) |det Gamma|^(1/4)].`                           (13)

It remains to express the Schur determinant invariantly. Put `e=u/r` and use the orthogonal basis `[e,P]`. In that basis

`Lambda = [[alpha, b^T],[b,C]]`,
`alpha=e^T Lambda e=a/r^2`,

while the completed-square matrix is

`H = [[0,0],[0,C-bb^T/alpha]]`.

Thus `Gamma=C-bb^T/alpha`, and the block determinant identity gives

`det Lambda = alpha det Gamma`.

Therefore

`|det Gamma| = |det Lambda| r^2/|a|`.                                         (14)

Substituting (14) into (13) proves (2). If all three eigenvalue magnitudes are at least one and `r>1/2`, then `|det Lambda|>=1` and `r^2>1/4`, which gives (3). QED.

## Explicit contaminated high-row family

This theorem covers high-leverage frames outside both the fully delocalized B02 hypothesis and the exact `1+2` zero-pattern theorem.

Take `Lambda=diag(2,-1,-1)`. Let

`e=(2,1,1)/sqrt(6)`,
`u=(sqrt(3)/2)e`.

Then `r^2=3/4` and

`a=u^T Lambda u=3/4`.

Choose an orthonormal basis `e_2,e_3` of `e^perp`. Complete the remaining frame covariance

`I-u u^T = (1/4)ee^T + e_2e_2^T+e_3e_3^T`

with one residual row `(1/2)e`, four residual rows `(1/2)e_2`, and four residual rows `(1/2)e_3`. The resulting ten-row matrix `U` satisfies `U^T U=I_3`; the distinguished physical row has norm `sqrt(3)/2>1/2` and has nonzero components in **all three** eigen-directions, while every projected residual row in `u^perp` has norm at most `1/2`.

Thus (2) applies although rotating spectral coordinates to align with the large physical row creates genuine scalar--two-vector cross terms. For this example

`|a| r^2 |det Lambda|=(3/4)(3/4)2=9/8`,

so

`||p_Q||_infinity <= 4 B_RV/[pi 3^(1/4)(9/8)^(1/4)]`.

This is a universal bound for arbitrary independent physical-coordinate densities <=1.

## Updated first missing inference

The rank-three high-row frontier is now concentrated on two mechanisms not covered by (2):

1. **near-isotropic / isotropic pivot:** `|u^T Lambda u|` can be arbitrarily small or zero in indefinite signature, and (2) degenerates like `|a|^(-1/4)`;
2. **multiple projected large rows:** after choosing a large row `u_i`, some other `||P^T u_j||` may still exceed `1/2`, so the two-dimensional residual Fourier resource must itself be hybridized.

The exact isotropic model naturally produces a bilinear term rather than a square; the next product-rearrangement mechanism should therefore combine a universal logarithmic product-density bound with the third quadratic direction rather than trying to continue the square completion through `a=0`.

The full owner target remains open, especially for extra coupled eigendirections beyond rank three.
