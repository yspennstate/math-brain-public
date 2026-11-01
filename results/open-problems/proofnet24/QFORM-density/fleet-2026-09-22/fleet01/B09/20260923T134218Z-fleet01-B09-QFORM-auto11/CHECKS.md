# Checks for QFORM-PIVOTED-HEAVY3VOLUME-TO-2ROW-COLLAR-v1

Run `20260923T134218Z-fleet01-B09-QFORM-auto11`.

These are finite algebra/arithmetic checks beside the proof; they are not substitutes for the proof in `REPORT.md`.

## 1. Constants

For the two-volume half-Riesz source coefficient

`K(q)=4 sqrt(2e) q^(-1/4)/(2-q)`,

at `q=3/2`,

`K(3/2)=16.855... <16.856`.

At the equal-Parseval example, `q=4/3`,

`K(4/3)=13.0190353138...`.

The aggregate-heavy-row splice uses

`16.856 * 24^(1/8)=25.0773088... <25.078`.

The designated-partner application at `m=64` has

`G_*=64(1-2/64)^2=961/16=60.0625`

and

`30.824 G_*^(-1/6)=15.5759698... <15.576`.

## 2. Anchored wedge identity

For any three row vectors `b,c_j,c_k` and orthogonal projection `P_b` onto `b^perp`,

`b wedge c_j wedge c_k
 = b wedge (c_j P_b) wedge (c_k P_b)`.

Since `b` is orthogonal to both projected rows,

`||b wedge c_j wedge c_k||^2
 = ||b||^2 ||(c_jP_b) wedge(c_kP_b)||^2`.

Summing over row pairs and invoking Cauchy--Binet on column minors gives exactly

`V_i(B)=||b||^2 Z_2(CP_b)`.

The Schur shear `C_j=(B_0)_j-(u_j/a)b` leaves every wedge with `b` unchanged.

## 3. Parseval regression family

Let

`r1=(sqrt(2/3),0)`,
`r2=(-1/sqrt(6),1/sqrt(2))`,
`r3=(-1/sqrt(6),-1/sqrt(2))`.

Then

`sum_j r_j r_j^T=I_2`,

and every row has leverage `||r_j||^2=2/3`. Embedding these rows in the last two coordinates of `R^3` and taking pivot row `b=e1` gives `B^TB=I_3`. Therefore `V_i(B)=1`, `Z_2(C)=1`, and the residual two-volume row marginals are all `2/3`, matching the theorem's `q=4/3` test.

## 4. Scaling check

If every quadratic coefficient is multiplied by `s`, then

- `a` scales as `s`;
- `||b||` scales as `|s|`;
- `V_i(B)`, a squared 3-volume, scales as `|s|^6`.

Thus the factor in (4.4),

`|a|^(-1/2)||b||^(1/4)V_i(B)^(-1/8)`,

scales as

`|s|^(-1/2+1/4-6/8)=|s|^-1`,

which is exactly the required scaling for an output density under `Q -> sQ`.
