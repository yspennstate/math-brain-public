# Deterministic checks — fleet01/B09 r34

Run: `20260924T094640Z-fleet01-B09-QFORM-auto11-r34`

## 1. Adjugate-star exterior identity

For 1000 seeded random real symmetric matrices

`B=[[a,c],[c,b]]`

and random `2 x 5` real matrices `M`, form

`H=adj(B) M`.

For every column pair `J={j,k}`, check

`det(H[:,J]) = det(B) det(M[:,J])`.

Maximum absolute floating-point discrepancy: `1.4210854715202004e-14`.

The aggregate identity

`sqrt(det(H H^T)) = |det B| sqrt(det(M M^T))`

was checked on the same instances. Maximum absolute floating-point discrepancy: `1.7391903889274474e-13`.

These are exact algebraic identities; the regression is only a typo/sign check.

## 2. New-theorem target example

For

`Q_*=2X^2+2Y^2+4XZ_1+2YZ_2`,

`B=diag(2,2)`, `det B=4`, `M=diag(2,1)`, and `Delta=2`.

Thus the theorem currency is `|det B| Delta=8` and

`2^(5/4) pi sqrt(3) * 8^(-1/4) = pi sqrt(6)`

`= 7.695298980971184...`.

The matrix splits into the two blocks

`[[2,2],[2,0]]`, `[[2,1],[1,0]]`,

with spectra

`{1+sqrt5,1-sqrt5}` and `{1+sqrt2,1-sqrt2}`.

Hence exactly three eigenvalues have modulus greater than one.

## 3. Designated fleet02/B09 application

For the Walsh-flat `m=8` family in REPORT Section 7, after the legal hub-only shear the mixed rows are

`rho_i=(w_i,2c_i,2d_i)`.

Orthonormality gives

`G=diag(1,4,4)`, `det G=16`,

and flatness gives normalized leverage

`w_i^2+c_i^2+d_i^2=3/8`.

Fleet02/B09 `QFORM-JOINT-HUB-CAP-MIXEDFRAME-v1` with `h=2,r=1,lambda=1,M=1` yields

`(5/3) 2^(2/5)=2.1991798512881573...`.

The exact leaf direction `w` is an eigenvector of eigenvalue `1`. The compression to `span{e_1,c}` is `[[1,2],[2,0]]` with eigenvalues `(1+-sqrt17)/2`, so the full matrix has at least three eigenvalues of modulus at least one.

## 4. Scope checks

- No source-coordinate rotation is used probabilistically.
- No conditional density cap is asserted after a sum/difference conditioning.
- No cross minor alone is promoted to an `L^infinity` conclusion.
- Same-remainder curvature is arbitrary in the new definite-pair theorem because it is retained by the fleet03/B09 r47 receiver.
- Continuity is not claimed for the new theorem; only essential boundedness and a linear interval bound are inherited.
- The fleet02/B09 mixed-frame application does have a continuous density because its characteristic function is `L^1`.
