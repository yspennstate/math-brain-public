# Deterministic checks

Run: `20260924T025336Z-fleet01-B09-QFORM-auto11`.

All checks below are finite regressions supporting algebra already proved symbolically in `REPORT.md`; they are not evidence for the universal conjecture by themselves.

## Random exact-identity regression

For dimensions `m=4,6,9`, five fixed-seed random trials each were generated with:

- random physical two-hub rotation `(ell,k)`;
- nonzero random `tau`;
- random rank-one pair-to-leaf factor `g r^T` with `alpha=k^T g !=0`;
- random symmetric leaf block `D`.

For every trial the following were verified numerically:

1. With `E=(I-uu^T)D(I-uu^T)` and `A0` obtained by replacing `D` with `D-E`,

   `s_3(A0) <= |tau|`.

2. For every two leaf pairs `I,J`,

   `det A_rot[{k} union I,{k} union J]
    = -(alpha||r||)^2 v_I^T E v_J`

   to absolute error below `1e-7`.

3. The complete mixed-volume identity

   `sum_(I,J) det^2 = (alpha||r||)^4 ||E||_F^2`

   held to relative error below `1e-6`.

4. The diagonal pair-pair contribution obeyed

   `sum_I det(I,I)^2 <=2q * total`.

5. After returning to the original physical hub coordinates, the Frobenius sum of physical `2x2` hub-minor matrices over `I!=J` dominated the grouped kernel-kernel off-diagonal sum, as required by orthogonal invariance.

The regression output was:

```
all deterministic regressions passed
343/32 = 10.71875
343/96 = 3.5729166666666665
cube root 6 = 1.8171205928321397
```

## Constant check for the designated fleet02/B09 application

The partner constant evaluates as

`3*2^(2/3)*2^(-1/3)*3^(-2/3)=6^(1/3)=1.8171205928321397...`.

For `Q=2X_1^2+6X_2X_3`, the coefficient matrix is

```
[2 0 0]
[0 0 3]
[0 3 0]
```

with eigenvalues exactly `{2,3,-3}`.
