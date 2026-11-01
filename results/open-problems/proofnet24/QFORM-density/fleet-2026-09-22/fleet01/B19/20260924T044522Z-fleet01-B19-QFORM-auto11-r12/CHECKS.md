# fleet01/B19 r12 deterministic checks

Run `20260924T044522Z-fleet01-B19-QFORM-auto11-r12`.

These are regression/sanity checks only; the exact arguments are in `REPORT.md`.

## Constants

Using

`C_R2=3.9291317704497634871249193093253251298294614232702`,

one gets

`C_*=3*2^(4/3)*C_R2^(2/3)`
`   =18.82315036541657500323555794923133710738...`,

and

`C_4=2^(1/6) C_*`
`   =21.12827191480081129979801390016676595872...`.

For `alpha=1/4`, minimizing

`2sqrt(2) r^(-1) + [4*2^(1/4) H D^(-1/2) kappa^(-1/4)] r^(1/2)`

gives exactly

`3*2^(4/3) H^(2/3)D^(-1/3)kappa^(-1/6)`.

## Schur four-minor identity

100 random symmetric block matrices with a random invertible indefinite `2 x 2` physical pair were checked over every disjoint two-row/two-column remainder choice. The largest floating-point discrepancy in

`det A[T union I,T union J] = det(B) det(S[I,J])`

was

`1.7763568394002505e-14`.

The proof in the report is exact Schur determinant algebra.

## Zero-tetrad models

Two exact model classes from Theorem 5.1 were regression checked in dimension eight:

- star off-diagonal carrier `e_c z^T+z e_c^T`: carrier numerical rank `2`, `W_dis=0` exactly in the sampled arithmetic;
- signed one-factor clique carrier `epsilon x x^T` plus arbitrary diagonal: carrier numerical rank `1`, `W_dis=7.60e-30` (floating roundoff).

A generic random symmetric matrix at the same dimension gave `W_dis=69.628...`, confirming the test is nonvacuous.

## Homogeneity wording

The payment quantity

`J_T=D^6 kappa^4 W_T`

is homogeneous of coefficient degree `24`; consequently `J_T^(-1/24)` has the correct inverse-coefficient scaling for a density bound. The phrase "dimensionless payment currency" in the immutable `REPORT.md` should be read as "homogeneous payment currency" after normalizing the target scale `s_3(A)>=1`; no equation or exponent is changed.

Terminal marker: `QFORM_A01_B19_R12_PAIR_SCHUR_CHECK_PASS`.
