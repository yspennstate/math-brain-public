# fleet03/B06 r31 finite checks

These are sanity checks only; the proof is symbolic in `REPORT.md`.

## Constants

- `16 sqrt(30) = 87.63560920082658`.
- `2 sqrt(2 pi) = 5.0132565492620005`.
- For the collar `c>63/64`, the extra factor `c^(-1/2)` is `<sqrt(64/63)`.

For `delta in {1,1/4,1/16,1/64,1/256}`, the target-family all-level constants from the rank-two half-Riesz branch and the opposite-sign fleet04 square branch are respectively:

| delta | same-sign discriminant bound | opposite-sign square bound |
|---:|---:|---:|
| 1 | 74.2750278581 | 4.2489551137 |
| 1/4 | 118.1375110677 | 6.7581392595 |
| 1/16 | 173.9995332363 | 9.9537654558 |
| 1/64 | 248.8639385924 | 14.2364363231 |
| 1/256 | 352.9693735087 | 20.1918608151 |

The growth is the expected `delta^(-1/4)` near the exact-null boundary.

## Determinant identity

For 5,000 random pairs `u,v in R^7`, a random nonzero `k` and signed nonzero `d`, an orthonormal basis `P` of `span{u,v}` was constructed, with `a=P^T u`, `b=P^T v` and

`Lambda=k^2 aa^T-d bb^T`.

The exact identity checked was

`det Lambda = -k^2 d [ ||u||^2 ||v||^2-(u.v)^2 ]`.

Maximum normalized floating-point discrepancy was

`8.25087191502045e-14`.

## Target-family spectrum

For 200 logarithmically spaced `delta` values from `1e-8` to `1e4`, the matrices

`B_plus=[[delta,sqrt(1+delta),0],[sqrt(1+delta),0,0],[0,0,1]]`,
`B_minus=[[delta,sqrt(1+delta),0],[sqrt(1+delta),0,0],[0,0,-1]]`

were checked numerically against the exact spectra

`spec(B_plus)={1+delta,-1,1}`,
`spec(B_minus)={1+delta,-1,-1}`.

Maximum absolute eigenvalue discrepancy was

`4.547473508864641e-13`.

Symbolically, the characteristic polynomials factor as

`-(lambda-1)(lambda+1)(delta-lambda+1)`

and

`-(lambda+1)^2(delta-lambda+1)`.

## Exact-null mechanism warning

At `delta=0`, the crude conditional root-density bound reduces to a multiple of `E|U|^{-1}`. For any admissible scalar `U` whose density is positive on a neighborhood of zero (for example a centered uniform law), this expectation diverges logarithmically. Therefore the nonzero-pivot proof cannot be extended to the exact-null coupled case merely by setting `delta=0`; the endpoint requires the probability-normalized root selector/extra curvature mechanism used in the exact-null source theorem or a new product-structure argument.
