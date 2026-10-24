# Exact and numerical checks for account01/B20 20260924T094629Z

These are arithmetic checks only; the theorem proof is in `REPORT.md`.

Partner constants from completed account02/B20 r51:

- `D0 = 9.530157744638501e-7`.
- `kappa0 = 6.075614261408114e-5`.

## Strong relative-edge gate

At `m=2^-6` and `|b|=(65/64)m`, with `|d|<=m`,

- determinant lower bound:
  `129/2^24 = 7.688999176025390625e-6 > D0`;
- minimum singular lower bound:
  `m/64 = 2^-12 = 6.103515625e-5 > kappa0`.

Ratios to the partner thresholds are approximately `8.06807` and `1.00459235`, respectively.

## Scalar-Schur diagonal gate

With `|b/a|<65/64`,

` s_min(L)>64/129`, where `L=[[1,b/a],[0,1]]`.

At `|a|>=2^-6`, `|s_j|>=2^-11`,

- `|a s_j|>=2^-17=7.62939453125e-6 > D0`;
- `s_min(B)>(64/129)^2 2^-11
   =1.2018508503094766e-4 > kappa0`.

For the same-sign (definite) pair, the direct two-dimensional area bound is

`pi/sqrt(2^-17)=pi*2^(17/2)=1137.3780321685...<1138`.

## Tetrad branch

`delta=2^-11`, `sigma=1-delta=2047/2048=0.99951171875`.

If the zero-diagonal Schur part has every row norm at most `sigma/2`, the proved Cauchy-Binet count gives

`W2 >= sigma^4/2 = 0.4990241525229351...`.

At `|a|>=2^-6`, account01/B19's aggregate tetrad theorem therefore gives

`8 sqrt(2)e^(1/4) |a|^-1/2 W2^-1/8
 <=126.7661780065...<127`.

## Physical-star threshold

If the pivot row has norm `<1/4`, then the Schur-to-physical correction is bounded by

`(65/64)(1/4)=65/256=1040/4096`.

The surviving Schur star is larger than

`sigma/2=2047/4096`.

Thus the actual physical row star is larger than

`2047/4096-1040/4096 = 1007/4096 = 0.245849609375`.

All inequalities have strict slack at the account02/B20 `kappa0` threshold.
