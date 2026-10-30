# Deterministic checks — fleet01/B02 r50

No Monte Carlo or histogram evidence is used. These checks cover arithmetic and the two exact rank/singular-value identities used in the proof.

## Constants

With

`c14 = 2^(3/4) Gamma(3/8)/(2 sqrt(pi) Gamma(1/8))`,

one obtains

- `c14 = 0.14927036108294764`;
- generic edge constant `16 c14 pi^(1/4) = 3.179662567631707` (source theorem);
- exact diffuse-row ridge constant

  `C_row = 24 c14 (pi e sqrt(6)/2)^(1/4) 4^(-1/6)`

  `= 5.113449711661422`;

- concentrated-row edge constant

  `C_edge (3/2)^(1/8) = 3.3449716522072253 < C_row`;

- spectral-window singular-value factor

  `sigma0 = 23/72 - 1/19 = 365/1368 = 0.266812865497076`;

- perturbed ridge leverage

  `(1/sqrt(23)+72sqrt(3)/365)^2 = 0.3026971861... < 1/2`;

- diffuse one-eigen quarter-Riesz constant

  `24 c14 e^(1/8)(pi sqrt(6)/2)^(1/4) sigma0^(-1/4)`

  `= 7.91077111503424...`;

- high-leverage diagonal constant

  `2sqrt(2) 228^(1/4)=10.9907848202179...`;

- high-leverage row constant

  `C_row 228^(1/4)=19.86999239901545...`.

Hence `C_1eig=19.86999239901545` is valid.

## High-leverage arithmetic

If `P_ii>1/72` for `P=1_{|T|>=s/19}`, then

`T_ii^2 + ||T[i,i^c]||_2^2 > s^2/(19^2*72)`.

Since `228=19*12`,

`2(s/228)^2 = s^2/(19^2*72)`.

Therefore at least one of `|T_ii|`, `||T[i,i^c]||_2` is strictly greater than `s/228`.

## Exact second-Schur rank-one identity

For

`S = [[d,b^T],[b,C]]`, `d!=0`,
`T = C-bb^T/d`,

one has exactly

`S = (1/d)[d;b][d;b]^T + diag(0,T)`.

The first term has rank one. Therefore, by the operator-norm Eckart--Young theorem,

`s_2(S) = inf_{rank R<=1} ||S-R||_op <= ||diag(0,T)||_op = ||T||_op`.

Thus `s_2(S)>=1/4` implies `||T||_op>=1/4` with no condition on `b/d`.

## Live density constant

Using

`|a|>1/228`, `|d|>1/912`, `||T||_op>=1/4`,

and the one-eigen theorem,

`H_(1/4)(T) <= sqrt(2) C_1eig`.

The nested square-fusion bound is

`sqrt(228) * 32 e^(-3/4) * 912^(1/4) * sqrt(2) * C_1eig`

`= 35245.846767612515...`.

The report rounds this upward to `35245.847`.

## Partner Fourier inversion

The newest fleet02/B02 exact-target two-star estimate is

`int |phi| <= pi(1800 e^2)^(1/3)`.

Its numerical value is

`74.43382933138852...`.

Fourier inversion gives

`||p||_infinity <= [pi(1800e^2)^(1/3)]/(2pi)`

`=(1800e^2)^(1/3)/2`

`=11.84651187134899...`.
