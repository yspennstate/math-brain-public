# account01/B03 r41 deterministic checks

Status: PASS for the algebra and constants listed here. These checks are not numerical evidence for the full conjecture.

## Exact constants

- Interpolated physical-pair envelope constant: `2^(5/3)=3.174802103936399...`.
- Bathtub coefficient at exponent `2/3`: `3*2^(2/3)=4.762203155904598...`.
- After the Rogozin--Ball cap `M<=sqrt(2)/||beta||_2`, the fractional moment coefficient is exactly `6`:
  `3*2^(2/3)*(sqrt(2))^(2/3)=6`.
- Rank-one overlap-two coefficient:
  `C_rank1=6*2^(5/3)=19.048812623618396...`.
- Posterior whole-copy weighted-time coefficient:
  `4*sqrt(pi*C_rank1)=30.943460646273696...`.

The last number corrects the harmless decimal typo `30.9427` in the first immutable REPORT commit; the exact formula `4 sqrt(pi C_rank1)` in that report is correct and this file is the canonical decimal value.

## Rank-one mixed-minor identity regression

For 1000 fixed-seed random tests, choose a random orthonormal pair `(v,w)`, a nonzero scalar `lambda`, set `B=lambda v v^T`, and choose random external columns `c_i,c_j` and scalar `a_ij`. Direct `3 x 3` determinants were compared with

`det [[B,c_j],[c_i^T,a_ij]] = -lambda (w^T c_i)(w^T c_j)`.

Maximum normalized discrepancy was `<5.6e-16`.

## Derivative identity

For the level-curve parametrization in the report,

`x'(y)=v-(lambda/ell)y w`,

orthonormality gives exactly

`||x'(y)||_2^2=1+(lambda y/ell)^2`.

Thus the two area-formula partitions used in the proof require no condition-number or support input.

## Scaling check

The final rank-one bound has coefficient scale

`(|lambda| ||beta||_2^2)^(-1/3)`.

Since

`J2=lambda^2[(sum beta_i^2)^2-sum beta_i^4] <=lambda^2 ||beta||_2^4`,

we have

`(|lambda| ||beta||_2^2)^(-1/3) <= J2^(-1/6)`.

This has the correct quadratic-form scaling: multiplying the whole matrix by `c` multiplies `J2` by `|c|^6` and the density bound by `|c|^-1`.

Terminal marker: `QFORM_B03_R41_RANK1_J2_CHECK_PASS`.
