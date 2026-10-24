# Rigor check — account03/B15 r13

## A. Scaling

Let `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Then `Q=(s/K^2)Qtilde`. Therefore

- density height scales by `K^2/s`;
- `C_0` is preserved under the output dilation;
- the half-potential scales by `K/sqrt(s)`:

`E|Q-a|^(-1/2)=(K/sqrt(s)) E|Qtilde-(K^2/s)a|^(-1/2)`.

PASS.

## B. Same-height passage from interval domination to a continuous representative

The fixed-instance affine theorem supplies a canonical `p in C_0` for every fixed `rank(A)>=3` instance. If the same law satisfies `mu(I)<=M|I|` for every interval, then `p<=M` almost everywhere. Were `p(t0)>M`, continuity would give an open interval on which `p>M`, contradicting interval domination after integration. Hence `||p||_infinity<=M` pointwise. No inference `L^infinity => continuity` is made.

PASS.

## C. Sharpened nine-direction constant

Using `q2=1733/2500`, `qc=73777/50000`:

`10*(22/7+4*q2+2*(4+4*qc)) = 1125249/4375 =257.199771428571...`.

Adding the unit half-potential tail:

`1129624/4375 =258.199771428571...`.

Multiplying by the outer scalar-pivot factor ten:

`2259248/875 =2581.997714285714...`.

Since

`2582 - 2259248/875 =2/875>0`,

the strict `<2582` comparison is exact. The other source branches remain `<2400`, `<32`, and `<251`, so this is the maximum.

PASS.

## D. Eight-direction collar constants

Take

`kappa=1/6400`,

`delta_*=(1-3sqrt(2)/80-1/100)^2-(sqrt(1/10000+1/100)+3sqrt(2)/80)^2`.

Direct evaluation gives

`delta_*=0.8543351401911338...`.

The account01/B11 extraction gives

`E2 >= (sqrt(2)*delta_*/27)*kappa
    =6.99196957216563e-6...`.

With

`C2=8 sqrt(e) 2^(-1/8)=12.0950725707965...`,

one obtains

`C2*E2^(-1/8)=53.3376082498547...<53.338`.

PASS.

## E. Half-potential to interval concentration

For an interval `I` of length `ell` with midpoint `a`, on `{Q in I}`,

`|Q-a|<=ell/2`, hence

`|Q-a|^(-1/2)>=(ell/2)^(-1/2)`.

Therefore

`P{Q in I} <= [sup_a E|Q-a|^(-1/2)] sqrt(ell/2)`.

At `H<53.338`, this is `<37.716 sqrt(ell)` because

`53.3376082498547/sqrt(2)=37.7153844857438...`.

PASS.

## F. Scope check

The nine-direction `C_0` theorem retains arbitrary dimension, signature, remaining spectrum, affine terms and arbitrary independent rough coordinate densities bounded by `K`. It does not add moments, support assumptions, log-concavity, Gaussianity, exact rank, coordinate rotation, or leverage conditions.

The eight-direction statement does **not** claim a uniform height. It records fixed-instance `C_0 cap L^infinity` plus a universal half-potential/square-root interval bound in the unresolved collar. The step from square-root concentration to linear concentration is explicitly left open.

PASS.
