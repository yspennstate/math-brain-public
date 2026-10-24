# account03/B03 r42 deterministic checks

Run: `20260923T225825Z-account03-B03-QFORM-r42`

These are finite algebra/constant checks for the accompanying `REPORT.md`; they are not a substitute for the proofs there.

## 1. Critical rank-one crossover

With

`A = 2^(1/4) sqrt(pi) (|tau| ||ell||_2)^(-1/2)`

and `|phi(t)|^2 <= min(1,A^2/|t|)`,

`int_R |t|^(-1/2) min(1,A^2/|t|) dt = 8A`.

At normalized scale `|tau| ||ell||_2=1`,

`2^(13/4) sqrt(pi) = 16.862517844086494`.

Dividing by the Riesz factor `sqrt(2pi)` gives

`2^(11/4) = 6.727171322029716`.

## 2. Linear-hub whole-copy improvement

For a planar probability density capped by `K`, layer cake gives

`E (Y_1^2+Y_2^2)^(-1/4) <= (4/3)(pi K)^(1/4)`.

With `K=2/||ell||_2^2`, and after the conditional hub-pair half-Riesz bound, the normalized whole-copy potential constant is

`(2^(7/2)/3) pi^(1/4) = 5.020780073475813`.

Multiplication by `sqrt(2pi)` gives the time-integral constant

`(16/3) pi^(3/4) = 12.585229292878383`.

## 3. One-copy linear-hub potential

For a probability density capped by `M`,

`int_0^infinity min(1,2M u^(-2))du = 2 sqrt(2M)`.

The normalized scalar-projection cap `M_L=sqrt(2)` therefore gives

`E|L|^(-1/2) <= 2^(7/4)`

and, after the conditional hub factor `2`,

`sup_s E|Q-s|^(-1/2) <= 2^(11/4) = 6.727171322029716`.

## 4. Independent-square transduction

The shifted-square density envelope is

`p_(d(Z+h)^2)(y) <= |d|^(-1/2)|y|^(-1/2)`

on its support. Multiplying it against the one-copy potential leaves exactly the coefficient

`2^(11/4)|d|^(-1/2)(|tau| ||ell||_2)^(-1/2)`.

No extra factor of two occurs because the two square branches are already included in the envelope.

## 5. Physical-leaf continuity truncation

For the planar lemma, the low-`|l|` contribution from the source proof is

`K int_(|l|<eta) sqrt(2/|l|) dl = 4 sqrt(2) K sqrt(eta)`.

Hence the truncated `C_0` densities converge uniformly as `eta downarrow0`.

The source height prefactor is

`3*2^(2/3) = 4.762203155904598`.

## 6. Dependency audit

- The whole-copy identity is used only as `|phi(t)|^2 = E exp(it(S-S'))` for the entire random variable.
- No independence of `X-X'` and `X+X'` is asserted.
- The account04/B03 partner inequality is applied directly on their actual dependent joint law.
- The linear-hub theorem conditions only on the genuine independent physical hub `H`.
- The square transduction requires a genuinely independent original coordinate `Z`; the dependent light square `V^2` in the canonical small-leak form is explicitly **not** counted as that resource.

`QFORM_B03_R42_CHECK_PASS`
