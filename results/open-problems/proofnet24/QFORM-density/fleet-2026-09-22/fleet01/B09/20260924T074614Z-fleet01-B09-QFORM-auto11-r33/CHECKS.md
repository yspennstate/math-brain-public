# r33 deterministic checks

These checks are regression support, not proof evidence.

## Cauchy--Binet / basis-star regression

A random `9 x 4` real row matrix was generated. With `G=X^T X`,

- `det G = 1452.402989342367`;
- for every row `i`, the identity
  `det G-det(G-x_i x_i^T)=det G * x_i^T G^-1 x_i`
  agreed to maximum absolute error `7.96e-13`;
- direct summation of squared `4 x 4` basis determinants containing `i` agreed with the same quantity to maximum absolute error `6.82e-13`.

## Rank-one two-frame regression

For random unit `v in R^8` and random `c in R^8`,

`T=det([[<v,v>,<v,c>],[<c,v>,<c,c>]])`

was compared to

`sum_(i<j)(c_i v_j-c_j v_i)^2`.

Both were exactly `5.5191968333381745` at displayed precision. For every row, the edge-star sum agreed with `T*leverage_i` to maximum absolute error `4.44e-16`. The leverage sum was `2.0`, as required.

For the same random frame, the ordered probability that two independently sampled Pluecker edges are disjoint was `0.37544042736459915`, lying in `[0,1]` as used in `Omega=lambda^2 T^2 rho <= lambda^2 T^2`.

## Live packet constants

For `omega=13/48`:

- `3*2^(4/3)*omega^(-1/6) = 9.39819019528223`;
- `(1/2)*sqrt(omega) = 0.2602082499332666`;
- `2*omega^(-1/4) = 2.772390914471511`.

For `eta=1/2`:

- paid constant `=11.84097765795169`;
- star currency threshold `=0.1301041249666333`.

## Designated-partner application

For

`Q_8=2(U+V)^2+2UY_0+2VY_1+8 Z^2`,

where `Z` denotes the deterministic square-mode direction only for spectral bookkeeping, the active coefficient matrix eigenvalues were computed as

`[-1, -0.236067977499789..., 1, 4.23606797749979..., 8]`,

namely `{-1,2-sqrt(5),1,2+sqrt(5),8}`. Thus four eigenvalues have absolute value at least one. The fleet02/B09 r19 constant is

`6*8^(-1/3)=3`.

STATUS: PASS.
