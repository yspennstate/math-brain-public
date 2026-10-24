# Deterministic checks for r42

Run `20260924T011327Z-account01-B18-qform-auto11-r42`.

For the basis `(U,R,V,S,W)`, the rotating-anchor matrix is

```
A(delta,rho) =
[[0, 0, delta^(-1/2), 0, 0],
 [0, 0, 0,            0, rho],
 [delta^(-1/2),0,0,   0, 0],
 [0, 0, 0,            0, sqrt(1-rho^2)],
 [0, rho,0,sqrt(1-rho^2),delta]].
```

The unit vector `rho R + sqrt(1-rho^2) S` is orthogonal to `U,V`, so the nonzero spectrum is exactly

`{+delta^(-1/2), -delta^(-1/2), (delta+sqrt(delta^2+4))/2, (delta-sqrt(delta^2+4))/2}`.

Representative numerical eigenspectra:

- `delta=1/64, rho=0`: `[-8, -0.99221802, 0, 1.00784302, 8]`.
- `delta=1/64, rho=1/sqrt(2)`: same up to numerical roundoff.
- `delta=1e-4, rho=0.2`: `[-100, -0.999950001..., 0, 1.000050001..., 100]`.

For the whole-family cross bound,

`2 sqrt(pi) 2^(1/4) (1/64)^(1/4) = 1.4904500894290902 < 1.490451`.

Partner endpoint constant:

`12 / 2^(1/3) = 9.524406311809196...`.

Curved-family transverse threshold: if `rho>=sqrt(delta)`, then

`2 sqrt(pi) delta^(1/4) rho^(-1/2) <= 2 sqrt(pi) = 3.544907701811032...`.

The `S^2` curved-family term is orthogonal to the `(U,V)` block. Its remaining `(R,S,W)` block has Rayleigh quotient exactly `1` on `S`, hence maximum eigenvalue at least `1`; together with `+/-delta^(-1/2)` this verifies the owner target for every `rho` and every `0<delta<=1/64`.
