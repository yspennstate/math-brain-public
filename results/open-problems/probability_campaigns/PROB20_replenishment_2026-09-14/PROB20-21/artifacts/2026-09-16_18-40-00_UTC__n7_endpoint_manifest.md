# PROB20-21 n=7 endpoint coverage manifest

Status: PARTIAL for the frozen metric. This artifact certifies only two endpoint noise intervals for every seven-bit Boolean function; it does not certify the middle interval and does not move the frozen dimension beyond n=6.

## Frozen source reduction

The source-valid Courtade--Kumar one/two-coordinate compression family `S_7` is reconstructed exactly. The checker verifies:

- `|S_7| = 44315`;
- frozen sorted-mask SHA-256 `9caace4fb804076a20a55c2e0b9fb3e1f860a7a7629f788a9e42fe1c1e77a50d`;
- the previously proved dual involution has `22225` orbits;
- balanced nondictators: `1006`.

The hash agrees with the independently archived prior n=7 checker `2026-09-16_17-29-11_UTC__n7_symmetry_extremizer_scan.py`.

## Certified low-noise interval

Full interval:

`alpha in [0, 1/131072]`.

### Biased functions

After output complementation, every nonbalanced seven-bit Boolean function has `p=P(f=1) <= 63/128`. Since `I(f(X);Y) <= H(f(X))`, the Courtade--Kumar defect obeys

`[ln 2 - h(alpha)] - I(f(X);Y) >= ln 2 - h(alpha) - h(63/128)`.

Binary entropy is increasing on `[0,1/2]`. Exact rational logarithm enclosures at `alpha0=1/131072` give the uniform lower bound

`> 2.4544928363351194e-05` nats.

### Balanced nondictators

For a cube point `y`, let `d_y` be the number of sensitive coordinate flips, and let `e_y=P(f(X) != f(y) | Y=y)`. For `alpha <= alpha0`, `e_y <= 7 alpha < 1/2`, while the disjoint event of exactly one sensitive flip gives

`e_y >= d_y alpha (1-alpha)^6`.

Put `c=(1-alpha)^6` and `L=ln(1/alpha)`. Since `h(z) >= z ln(1/z)`,

`H(f(X)|Y) >= alpha c [ AS(f) L - E_y(d_y ln d_y) ]`.

Also `h(alpha) <= alpha(L+1)`, hence the defect is at least

`alpha * [ (c AS(f)-1)L - c E_y(d_y ln d_y) - 1 ]`.

For `alpha <= alpha0`, `c >= c0=(1-alpha0)^6` and `L >= L0=17 ln 2`. Moreover `L0>ln 7`, so the bracket is increasing in `c`; the exact enumeration also gives `c0 AS(f)-1>0`, so it is increasing in `L`. Thus it suffices to test `c0,L0`.

The exact checker evaluates the local degree distribution of all 1006 balanced compressed nondictators, with rigorous rational logarithm enclosures. It finds

- `min AS = 37/32`, at mask `15555555555555555555555555555557`;
- minimum normalized defect bracket lower bound `0.5426196140382018`, at the same mask.

Therefore the full low-noise interval is certified.

## Certified high-noise interval

Full interval:

`alpha in [67/135, 1/2]`, equivalently `rho=1-2 alpha in [0,1/135]`.

Use `{-1,+1}` coding. Let `mu=E f`, `V=1-mu^2`, `W1=sum_i fhat({i})^2`, `Delta=V-W1`, and `M=2^7-1=127`. Write `g=T_rho f=mu+r`.

The following sufficient lemma is checked algebraically. Cauchy--Schwarz gives

`||r||_infty <= q := rho sqrt(M V)`

and Parseval gives

`E r^2 <= rho^2 W1 + rho^4 Delta`.

For `psi(t)=ln2-h((1+t)/2)`, Taylor's formula and `psi''(t)=1/(1-t^2)` yield

`E psi(mu+r)-psi(mu) <= E r^2 / [2(1-(|mu|+q)^2)]`

whenever `|mu|+q<1`; while `psi(rho)>=rho^2/2`. Hence the Courtade--Kumar defect is nonnegative if

`(1-rho^2) Delta >= 2 |mu| q + q^2`.

With

`L=(1-rho^2)Delta - M rho^2 V`,

it suffices that `L>0` and

`L^2 - 4 mu^2 rho^2 M V > 0`.

Both conditions become weaker as `rho` decreases, so endpoint verification at `rho0=1/135` certifies the whole interval.

The exact S7 checker verifies over every nonconstant nondictator:

- `min Delta = 15/512`;
- `min L = 111121/4976640 > 0`, worst mask `15555555555555555555555555555555`;
- `min [L^2-4 mu^2 rho0^2 M V] = 45393431101/5572562780160000 > 0`, worst mask `00000000000000000000000000000001`.

Therefore the entire high-noise endpoint interval is certified.

## Remaining n=7 interval

Uncertified continuous middle interval:

`alpha in [1/131072, 67/135]`.

No metric credit beyond n=6 is claimed.

## Executed artifacts and hashes

- `2026-09-16_18-40-00_UTC__n7_endpoint_certificate.py`
  SHA-256 `c410e6fec5438d75252f034b4da6d087cc61a49c6795662e58c13bd9c220dcb6`
- `2026-09-16_18-40-00_UTC__n7_endpoint_certificate.out`
  SHA-256 `c8ad42d04b3ecbacb736d41461a9e0253d657360b58cd79af11b299c129dfb95`

The output ends with `PROB20-21 N=7 ENDPOINT CERTIFICATE: PASS`. The script uses exact integer/Fraction arithmetic for all finite comparisons and a rational atanh-series enclosure for logarithms. Floating conversions are printed only for human-readable margins.
