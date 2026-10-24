# Dimension-descent bootstrap for a diagonal-heavy physical pivot

This addendum applies the fresh account02/B09 target reduction to an actual induction inequality and removes another part of the remaining synthesis branch.

## Source-pinned inputs

- account02/B09 `QFORM-PIVOT-OFFDIAG-STABLERANK-v1` and its target-level diagonal-heavy reduction: `yspennstate/math-open-problems@77d71ed8bbd7f8a3fd40958e54b5bf658163c27a`.
- account02/B04 / account03/B04 square-coarea mechanism: `yspennstate/math-open-problems@b129377880c18fe011dd4513282f2e0b60e412e0`, which records

`||p_[a(X+m(Y))^2+R(Y)]||_inf <= H_3 |a|^(-1/2) ||p_R||_3^(3/4),`

with `H_3=8 sqrt(2)/3^(3/4)`, for one untouched original cap-one coordinate `X` and arbitrary measurable shift `m(Y)`.

The current `1/39` spectral-window/heavy-coordinate theorem supplies a physical coordinate with `max(|a|,||b||_2)>=1/312` in every still-unpaid target matrix.

## Theorem — `QFORM-DIAGHEAVY-MODERATE-PIVOT-DESCENT-v1`

Fix a proposed universal induction constant `C`. Let `A` be an `n x n` target matrix, choose an original coordinate `k`, and write

`A=[[a,b^T],[b,C_0]],   a!=0,`

with scalar Schur complement

`S=C_0-bb^T/a`.

Assume

`|a|>=1/312,       ||b||_2<=|a|,`

and put

`c_* = 2/(3+sqrt(5)).`

If

`|a|<c_*`,

then `S` has at least three eigenvalues of modulus at least `c_*`. Consequently, if the full QFORM density bound `C` is already known in all dimensions `<n`, then

`||p_(X^T A X)||_inf <= K sqrt(C),`

where

`K = H_3 sqrt(312/c_*).`

In particular the branch is closed by induction whenever

`C >= K^2 = 6656(3+sqrt(5))/sqrt(3) < 20122.`

### Proof

Completing the square in the original physical coordinate gives

`X^T A X = a (X_k + a^(-1)b^T Y)^2 + Y^T S Y,`

with `X_k` independent of the original-coordinate vector `Y`.

The exact congruence is

`A = L diag(a,S) L^T,`

where

`L=[[1,0],[b/a,I]].`

Under `||b||/|a|<=1`, the largest squared singular value of `L` is at most

`||L||^2 <= (3+sqrt(5))/2 = c_*^(-1).`

Since the target hypothesis gives `s_3(A)>=1`, singular-value monotonicity under multiplication yields

`s_3(diag(a,S)) >= c_*.`

But `|a|<c_*`, so the scalar block cannot supply any of the first three singular values at level `c_*`; therefore `S` has at least three singular values, equivalently three eigenvalues in modulus, at least `c_*`.

By the induction hypothesis applied to `S/c_*`, the residual quadratic variable

`R=Y^T S Y`

has density bounded by `C/c_*`. Since every density has `L^1` norm one,

`||p_R||_3 <= (C/c_*)^(2/3).`

The square-coarea theorem, with the exact shift `m(Y)=a^(-1)b^T Y`, now gives

`||p_Q||_inf
 <= H_3 |a|^(-1/2) ||p_R||_3^(3/4)
 <= H_3 sqrt(312/c_*) sqrt(C)
 = K sqrt(C).`

If `C>=K^2`, then `K sqrt(C)<=C`, closing the induction step. Finally

`K^2 = [128/(3 sqrt(3))] * 312 * (3+sqrt(5))/2
     = 6656(3+sqrt(5))/sqrt(3)
     <20122.`

No post-rotation independence is used: the only completed square is the original coordinate `X_k`, and the residual induction is on the original product vector `Y`. QED.

## Consequence for the live synthesis branch

Combine this descent with account02/B09. After the `1/39` spectral-window branch, suppose the heavy coordinate is diagonal-dominant, so `|a|>=1/312` and `||b||<=|a|`. Then:

1. if `|a|<c_*`, the new dimension-descent theorem pays the branch for any global induction constant `C>=20122` (assuming the other branches are also bounded by `C`);
2. if `|a|>=c_*` and the Schur offdiagonal stable rank is at least `24`, account02/B09 pays the branch directly (`<340`);
3. therefore the only diagonal-heavy state still requiring new structural mathematics has a **strong physical pivot** `|a|>=c_*` and **low Schur offdiagonal stable rank** `<24`.

Together with the separate offdiagonal-heavy coordinate case, this sharpens the first unpaid implication to:

`QFORM-STRONG-PIVOT-LOW-SCHUR-SR-OR-HEAVYBANK-v1` — close either an offdiagonal-heavy physical coordinate, or a diagonal-heavy physical pivot with `|a|>=2/(3+sqrt(5))` whose Schur offdiagonal stable rank is `<24`, using a product-preserving grouped-coordinate/ridge/hyperbolic mechanism. The same-square and negative-half-moment corrections require retaining an independent third smoothing resource.

This is a conditional induction component, not a full proof. Full QFORM remains OPEN.
