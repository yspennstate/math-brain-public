# Deterministic checks — fleet01/B09 20260923T144451Z

These are algebraic/arithmetic regressions for `QFORM-TWOHUB-PUNCTURED-THREEVOLUME-STABILITY-v1`. They are supporting checks, not substitutes for the proof in `REPORT.md`.

## A. Deletion Gram identity

For `G=C^T C` and physical row `c_i^T`, deletion gives

`G_i=G-c_i c_i^T`.

The determinant lemma yields

`det G_i=det G * (1-c_i^T G^{-1}c_i)=Delta(1-ell_i)`.

Thus the theorem's denominator vanishes exactly at a physical coloop (`rank C_(i)<2`).

## B. Puncturing is physical

For each leaf `i`, the augmentation matrix is

`M_i=A[{h1,h2,i}, L\{i}]`.

Hence every minor in

`V_i=sum_{T subset L\{i}, |T|=3} det A[{h1,h2,i},T]^2`

uses disjoint row/column coordinate sets. In particular the proof does not use the tempting but invalid full-row wedge that would allow coordinate `i` simultaneously as a moved row and as a cross column.

The punctured least-squares distance satisfies

`delta_i^2=min_u sum_{j!=i}(D_ij-c_j^T u)^2`.

The Gram Schur complement then gives the exact equality

`V_i=Delta(1-ell_i) delta_i^2`.

## C. Frobenius block constant sqrt(2)

With `P` an orthogonal projection and `Q=I-P`, for symmetric `S`,

`S-PSP=PSQ+QSP+QSQ`.

The three displayed blocks are pairwise Frobenius-orthogonal, while `||PSQ||_F=||QSP||_F`. Therefore

`||S-PSP||_F^2=2||PSQ||_F^2+||QSQ||_F^2`

and

`||SQ||_F^2=||PSQ||_F^2+||QSQ||_F^2`.

Consequently

`||S-PSP||_F^2<=2||SQ||_F^2`.

This is the origin of the theorem's factor `sqrt(2)`; the cruder triangle inequality would give `2`.

## D. Four-leaf exact regression

Take rows of `C` to be

`c1=(1,0), c2=(0,1), c3=(1,0), c4=(0,1)`.

Then `G=2I`, `Delta=4`, and all four leverages equal `1/2`.

Let `D12=D21=1`, all other entries zero. Punctured least squares gives

`delta_1^2=delta_2^2=1/2`,
`delta_3^2=delta_4^2=0`.

Therefore

`V1=V2=4*(1/2)*(1/2)=1`,
`V3=V4=0`,
`V=2`.

The coarse theorem gives

`||E||_F<=sqrt(2V/(Delta(1-q)))`
`=sqrt(4/(4*1/2))=sqrt(2)`.

The projected construction has

`M=[[0,1/4],[1/4,0]]`

and produces an error with exact squared Frobenius norm `3/2`, so the claimed bound holds strictly in this regression.

## E. Partner application arithmetic

For the cross matrix `M_s` in REPORT section 7,

`M_s^T M_s=diag(s^2,1,1)`.

Hence the symmetric cross-only matrix `[[0,M_s],[M_s^T,0]]` has nonzero eigenvalues

`+s,-s,+1,-1,+1,-1`.

There are four selected `3x3` minors. Each determinant has absolute value `s/2`, so each squared determinant is `s^2/4` and their total selected mass is

`Z=s^2`.

The fleet02/B09 theorem coefficient becomes

`5*2^(4/5)*sqrt(e) * s^(1/5) * (s^2)^(-1/5)`
`=5*2^(4/5)*sqrt(e) * s^(-1/5)`.

Numerically

`5*2^(4/5)*sqrt(e)=14.352952309262982...`.

At `s=32`, `32^(1/5)=2`, hence

`14.352952309262982.../2=7.176476154631491...<7.177`.

No histogram, Monte Carlo estimate, or distributional extremality claim is used anywhere in these checks.
