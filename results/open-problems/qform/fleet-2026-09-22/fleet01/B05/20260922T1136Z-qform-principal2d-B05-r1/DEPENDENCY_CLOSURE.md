# Late dependency closure — fleet01/B05

This file does not alter the immutable `REPORT.md`; it records a later same-run peer dependency discovered during the required final closure check.

## Newly consumed peer result

fleet04/B15, scientific commit `15a15f2495abe0d4de12c3562246d55c7a63980d`, path `qform/fleet-2026-09-22/fleet04/B15/20260922T112652Z-b15-qform-r1/REPORT.md`, independently proves the same physical definite-pair theorem and strengthens the coordinate-pair obstruction. Its Walsh-Hadamard family

`A_n=r_1 r_1^T+r_2 r_2^T-r_3 r_3^T`

has spectrum `(1,1,-1,0,...)` while **every** physical 2x2 principal determinant is nonpositive. Thus a full proof cannot even hope that one definite physical pair always exists. B15 also records, for the 3xn matrix `R` with rows `r_1,r_2,r_3`,

`sum_{|J|=3} (det R_J)^2 = 1`.

This sharpens the B05 unpaid implication from merely 'avoid a small pair determinant' to a genuinely aggregate coordinate-chart problem.

## New derivation from B15's aggregate reserve

Take the concrete Walsh rows

- `r_1=1/sqrt(n)`,
- `r_2=(-1)^{x_1}/sqrt(n)`,
- `r_3=(-1)^{x_2}/sqrt(n)`,

with `n=2^m`. There are four column sign types, each repeated `n/4` times. A 3x3 minor is nonzero exactly when its three columns have three distinct sign types. Every such sign determinant has magnitude `4`, hence

`|det R_J| = 4/n^(3/2)`.

There are

`4 (n/4)^3 = n^3/16`

such unordered coordinate triples. Therefore

`sum_J (det R_J)^2 = (n^3/16)(16/n^3)=1`,

but simultaneously

`sum_J |det R_J| = (n^3/16)(4/n^(3/2)) = n^(3/2)/4`.

Consequently, Cauchy-Binet's square-weight reserve alone does **not** close the problem if each local coordinate-chart estimate pays the natural reciprocal Jacobian factor `1/|det R_J|`: weighting such local estimates by `(det R_J)^2` leaves the dimension-losing total `sum_J |det R_J| = n^(3/2)/4`.

Combined with B05's cube projection calculation (`fiberwise sup` loss `n/2` on a flat Walsh two-plane), this rules out two crude aggregation mechanisms:

1. choose one best physical coordinate chart;
2. sum local reciprocal-Jacobian worst-case bounds using only Cauchy-Binet square weights;
3. take a fiberwise amplitude supremum before integrating the complement.

The live missing implication must instead be a **nonreusing averaged level-set inequality** that keeps the product amplitude inside the coarea integral and exploits overlap/normalization across coordinate charts before any reciprocal determinant loss is paid.

Full conjecture status remains `OPEN_NOT_PROVED`.
