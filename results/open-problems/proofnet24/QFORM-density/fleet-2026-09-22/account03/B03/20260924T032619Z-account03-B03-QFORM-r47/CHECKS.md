# account03/B03 r47 checks

The report's analytic constants and Schur identity were checked independently during the run. The sibling `check_r47.py` records the deterministic calculation.

## Exact constant checks

For the translated-product envelope:

- near-zero cubic budget:
  `2 int_0^1 [2+2 log(1/r)]^3 dr = 256`;
- designated-partner half-power tail cubic budget:
  `2 int_1^infinity [2 r^(-1/2)]^3 dr = 32`;
- total normalized cubic budget: `288`;
- scaling `W -> 2 mu W` gives `288/(2|mu|)^2 = 72 |mu|^(-2)`.

For the square density, the rearrangement extremizer `G=2 1_[0,1/2]` gives

`int p_(Z+h)^2(s)^(3/2) ds <=2 sqrt(2)`,

so

`||p_(Z+h)^2||_(3/2) <= (2sqrt(2))^(2/3)=2`.

Therefore Young gives

`2 * 72^(1/3) = 576^(1/3) = 8.320335292207616...`.

The whole-copy weighted-time constant is

`4 sqrt(pi) 576^(1/6)
 =4 sqrt(pi) 24^(1/3)
 =20.450566438865533...`.

## Schur determinant check

For

`M=[[0,mu,a],[mu,0,b],[a,b,c]]`,

`B=[[0,mu],[mu,0]]`, and

`d=c-[a,b] B^(-1)[a,b]^T = c-2ab/mu`,

one has exactly

`det M = -mu^2 c+2mu ab = det(B)d = -mu^2 d`.

A seeded (`seed=47`) floating-point regression over 10,000 random choices of `mu,a,b,c` (excluding `|mu|<0.05`) gave maximum absolute determinant-identity error

`4.263256414560601e-14`.

This numerical regression is only a sanity check; the block determinant identity in the report is exact.

## Scope checks

- No rotation of the random vector is used.
- The two hyperbola coordinates and the square coordinate are literal independent original sources.
- Hyperbola translations are allowed to depend on the square coordinate and the remaining environment.
- No moment/support/log-concavity hypothesis enters either norm estimate.
- The partner account04/B03 half-power theorem is used only on the actual tail integral; no challenged weighted-L2 compiler is used.
- The whole-copy identity is used only for `Q-Q'` after the one-copy density bound is established.
- The theorem proves essential boundedness/absolute continuity; continuity is not claimed from this argument.

`QFORM_B03_R47_CHECK_PASS`
