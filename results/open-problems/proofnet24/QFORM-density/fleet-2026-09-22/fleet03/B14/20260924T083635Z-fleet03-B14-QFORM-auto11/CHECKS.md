# Checks for fleet03/B14 20260924T083635Z

## Algebra check

Let `B=B_*`, so `B=B^T` and `B^2=I`. With `Y_U=U+t_U`, `Y_Z=Z+t_Z`,

`Q_t = Y_U^T B Y_U + 2 Y_U^T C Y_Z + Y_Z^T D Y_Z`.

Set `s=B C Y_Z`. Then

`(Y_U+s)^T B (Y_U+s)`
`=Y_U^T B Y_U + 2Y_U^T B(B C Y_Z) + Y_Z^T C^T B B B C Y_Z`
`=Y_U^T B Y_U + 2Y_U^T C Y_Z + Y_Z^T C^T B C Y_Z`.

Therefore

`Q_t=(Y_U+B C Y_Z)^T B(Y_U+B C Y_Z)+Y_Z^T(D-C^TBC)Y_Z`.

The Schur boundary is `b_t(z)=(z+t_Z)^T S(z+t_Z)`, `S=D-C^TBC`.

## Translation dichotomy check

If `S!=0`, then the degree-two polynomial `b_t` has quadratic coefficient matrix `S`, independent of `t`. Hence it is nonconstant for every deterministic translation. Since `Z` has an absolutely continuous joint law, `b_t(Z)` is atomless.

If `S=0`, then `b_t` is identically zero for every translation.

## Rank check in the flat branch

With `B` invertible and `S=D-C^TB^{-1}C`, the triangular congruence

`T=[[I,-B^{-1}C],[0,I]]`

gives

`T^T A T = diag(B,S)`.

Hence `rank(A)=rank(B)+rank(S)`. For `B=B_*` and `S=0`, `rank(A)=3`.

## Target-class check

`spec(B_*)={1,1,-1}`. Since `B_*` is a principal submatrix of `A`, Cauchy interlacing gives at least two eigenvalues of `A` greater than or equal to one and at least one eigenvalue less than or equal to minus one. Thus every ambient extension lies in the exact owner target.

## Partner application check

Designated partner `fleet04/B14` r10 source:
`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

For `B_*`, `sigma_min_abs=1`, so the partner inequality becomes

`||p_Q||_infinity <= 6 sqrt(pi) = 10.634723105433096...`.

Designated partner `fleet04/B14` r11 source path:
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T071645Z-fleet04-B14-atomless-boundary-r11/REPORT.md`.

Its reflection majority-sheet height is

`pi sqrt(2) = 4.442882938158366...`.

## Sheetwise continuity check

For `S!=0`, partner r11 gives `p_+ in C_0`; the completed fixed-matrix theorem gives `p in C_0`. Since the minority measure is `Law(Q)-nu_+`, `p_-=p-p_+` is a continuous density. As a density of a positive measure it is nonnegative a.e.; continuity makes it nonnegative everywhere, hence `p_-<=p` pointwise.

For `S=0`, every sheet boundary is zero. The majority density has right trace `E h_Z(0)` and vanishes to the left. The full density is continuous. Therefore the minority density, which equals the full density on the negative side, has left trace equal to the same number. The bound `E h_Z(0)<=pi sqrt(2)` follows from the partner uniform kernel height.

## Source-match check

Existing source matches explicitly retained rather than relabelled:

- fleet01/B14 zero-tax Schur completion (`20260923T231306Z-fleet01-B14-QFORM-auto11`);
- existing B15 fact that nonconstant polynomial pushforwards of absolutely continuous laws are atomless;
- fleet04/B14 moving-boundary theorem and physical-triple theorem;
- fleet04/B15 same-constant fixed-matrix `C_0` compiler.

A targeted code search for the combined terms `atomless` and `D-C^T B_* C` returned zero matches before publication. This is only a duplicate-work check, not a claim of literature novelty.

## Scope check

No moment, bounded support, connected support, log-concavity, identical-law, Gaussian, compact-fragment or post-rotation independence assumption is used. Full QFORM remains open because the bare spectral hypothesis does not provide a uniformly conditioned physical reflection block.
