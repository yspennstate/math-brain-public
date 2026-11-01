# Stress refinement: exact rank-two / zero-kernel-curvature no-pivot family

This refinement was found after the main report and before finalization. It strengthens the diagnostic stress test and corrects an overinterpretation of the orthogonal-row example in the main report: the orthogonal-row family there is target-valid and the new theorem applies, but its three physical cross rows have rank three, so the pre-existing three-hub theorem also supplies a receiver. The theorem itself and its proof are unchanged.

Here is a sharper family on which the three-row cross rank is exactly two, the prior rank-two kernel-curvature currency is exactly zero, and the newest projected-crossing currency on the natural two-hub split is exactly zero, while the new entangled-scalar theorem remains uniform.

Let `u,v in R^m` be flat orthonormal Walsh vectors. Use original physical coordinates

`H1,H2,Z,Y_1,...,Y_m`.

Fix `k>=1` and put

`c=k^-4`.

Define the symmetric matrix by

`A_H1,H1 = -c`,
`A_Z,Z = c`,
`A_H1,Y = k u^T`,
`A_H2,Y = k v^T`,
`A_Z,Y = k u^T`,

with every other coefficient zero. Equivalently,

`Q = -c H1^2 + c Z^2
     +2k H1<u,Y> +2k H2<v,Y> +2k Z<u,Y>.`                         (R.1)

## Exact spectrum

The `H2`--`v` plane contributes eigenvalues `-k,+k`. On the orthogonal invariant space spanned by `H1,Z,u`, the matrix is

`[[-c,0,k],
  [0,c,k],
  [k,k,0]]`.

Its characteristic polynomial is exactly

`-lambda (c^2+2k^2-lambda^2)`.

Hence its eigenvalues are

`0, -sqrt(c^2+2k^2), +sqrt(c^2+2k^2)`.

Thus the full matrix has four eigenvalues of modulus at least `k>=1`.

## Arbitrarily deep physical no-pivot regime

The only nonzero physical diagonals are `-c,+c`. Every physical `2x2` principal determinant has magnitude at most

`max{c^2,k^2/m}`.

Given any `0<tau<1`, choose first `k>tau^-1/4`, so `c<tau`, and then choose a Walsh order `m>k^2/tau`. Then every physical diagonal and every physical `2x2` principal determinant has modulus `<tau`, while the four large eigenvalues remain.

## Why the main current rank routes vanish

The cross block from the three physical coordinates `(H1,H2,Z)` to the leaf bank `Y` is

`M = [k u^T; k v^T; k u^T]`.

It has exact rank two. Therefore the direct three-hub singular-value product has `s_3(M)=0`.

The unit left-kernel vector is

`n=(1,0,-1)/sqrt(2)`.

The physical `3x3` self block is `diag(-c,0,c)`, hence the prior B01 rank-two cross/kernel-curvature currency is exactly

`n^T A[H1,H2,Z] n = (-c+c)/2 = 0`.

So `QFORM-RANK2-CROSS-KERNEL-CURVATURE-L4-v1` is exactly at its unpaid endpoint on this family.

For the newest projected-crossing theorem, take two hubs `{H1,H2}`, light `I={Z}`, `J=Y`. The hub slope matrix is

`B=k[u^T;v^T]`,

while the residual `Z`--`Y` row is `k u^T`, already in `row(B)`. Therefore

`C = k u^T(I-P_row(B)) = 0`,

so every projected crossing volume `Z_ell` vanishes. The new grouped projected-crossing theorem is correctly inapplicable on this split.

## New theorem remains uniform

Apply `QFORM-TWOHUB-ENTANGLED-SCALAR-L4-v1` with

`H=(H1,H2)`,
`B=k[u^T;v^T]`,
`F(H)=-c H1^2`,
`R(Y)=0`,
`q(Y)=2k<u,Y>`,
`c=k^-4`.

Then

`D=det(BB^T)=k^4`,
`D|c|=1`.

Hence for every cap-one product input law

`boxed: ||p_Q||_infinity <= (15/4)12^(1/5) = 6.164069360689596...`,

and the density is continuous and vanishes at infinity.

This is the preferred stress family for the new compiler: exact rank-two physical crossing, exact zero kernel curvature, exact zero projected crossing after removing the two-hub slope rowspace, arbitrarily small local pivots, but a uniform density estimate from frequency-averaged scalar curvature before the aligned `Z`--`Y` interaction is conditioned away.

Full QFORM remains OPEN.
