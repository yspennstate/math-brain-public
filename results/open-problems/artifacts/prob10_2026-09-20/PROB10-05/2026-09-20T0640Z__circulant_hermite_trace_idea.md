Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-05 idea checkpoint — corrected circulant factorization before code

Status at idea time: source OPEN / candidate bracket from the latest owning report is `8497/50000 < theta_{2,1/4} <= 1/4`, width `< 4003/50000 = 0.08006`; independent validation is still missing. The old general formula `theta_{2,H}=H(1-H)` is Molchan's refuted proposal and is not a target.

This note is deliberately written **before** any new checker. It keeps the frozen source model and the already validated continuous-to-grid direction. It does not use the withdrawn softened-cycle normalization.

## New idea

At the frozen comparator

`r=7/8`, `s=24861/25000`, `c0=s(1+r)/2`,

the corrected four-cycle Gaussian orthant entering `tr(K^4)` is circulant. Write its standardized adjacent and opposite correlations as

`u = rho_adj_true`, `v = rho_opp_true`,

where the corrected previous run proved

`u = 11237172/11352323`, `v = 11137728/11352323`,

with `0<v<u<1`.

Instead of comparing this four-dimensional orthant to a hard edge, exploit the exact sum/difference diagonalization. For a circulant Gaussian vector `(V1,V2,V3,V4)` with covariance

```
[1 u v u]
[u 1 u v]
[v u 1 u]
[u v u 1],
```
set

`Z1=(V1+V3)/sqrt(2(1+v))`, `Z2=(V2+V4)/sqrt(2(1+v))`,
`E1=(V1-V3)/sqrt(2(1-v))`, `E2=(V2-V4)/sqrt(2(1-v))`.

Then `E1,E2` are iid N(0,1), independent of `(Z1,Z2)`, and

`Corr(Z1,Z2)=q=2u/(1+v)`.

The four-negative event is therefore exactly

`p4 = E[g_a(Z1) g_a(Z2)]`,

where

`a=sqrt((1+v)/(1-v))`,
`g_a(z)=1_{z>0}(2 Phi(a z)-1)`

(after replacing `(Z1,Z2)` by its negative, which has the same law).

This makes the correlation defect from the singular `q=1` limit one-dimensional in Hermite space. If

`d_n=E[g_a(Z) He_n(Z)]`, `w_n=d_n^2/n!`,

Mehler gives the exact positive-term expansion

`p4 = m^2 + sum_{n>=1} q^n w_n`, `m=E g_a(Z)`.

Hence for every integer `M>=0`,

`p4 <= m^2 + sum_{1<=n<=M} q^n w_n + q^(M+1)(Var(g_a)-sum_{1<=n<=M}w_n)`.

No sign cancellation occurs. This is the key replacement for the invalid softened-cycle trace cap.

Two endpoint quantities have closed cone formulas:

`m = atan(a)/pi`,

`E[g_a(Z)^2] = (1/pi) atan( a^2 / sqrt(1+2 a^2) )`.

The second identity is the solid angle of the square cone `z>0, |x|<az, |y|<az` in isotropic R^3.

The Hermite coefficients also have a closed half-Gaussian formula. Since `g_a(0)=0`, one integration by parts gives, for `n>=1`,

`d_n = (a/pi) integral_0^infty He_{n-1}(x) exp(-(1+a^2)x^2/2) dx`.

Thus each finite `w_n` is reducible to rational arithmetic, pi and one square root because `a^2` is rational. A moderate finite cutoff (exploration suggests M around 8--12) should already beat the scale-safe hard-edge cap `tr K^4 < 553151/500000` enough to test the clean milestone `theta_{2,1/4} > 17/100` using the existing degree-30 quasimode. Any promoted finite inequality will be rechecked with outward rational intervals; exploratory floating point will not be treated as proof.

## Three materially different attacks for this run

1. **Circulant/Hermite spectral attack (primary).** Prove the factorization and Mehler-tail inequality above, then combine a certified corrected trace cap with the existing degree-30 Temple argument. This is new mathematics relative to the previous degree-30 run because it attacks the four-cycle operator itself rather than merely improving the quasimode.
2. **Corrected Plackett attack (comparison).** Differentiate the exact four-orthant probability from the equicorrelated matrix down to the circulant opposite correlation. This remains potentially sharper, but near the almost-singular edge the conditional bivariate orthant in Plackett's derivative needs a uniform lower bound. The Hermite route avoids that conditioning denominator. I will compare the obtainable decrement and will not revive the pre-correction Plackett certificate.
3. **Continuous-time interpolation attack (auxiliary).** Try to complement the source-valid inclusion `continuous survival subset grid survival` by a buffered reverse estimate. A local bridge/modulus estimate is plausible because the Lamperti process is differentiable, but a union bound over `O(T)` Lamperti intervals loses exponentially unless the crossing penalty is controlled conditionally under survival. Any local crossing estimate will be recorded as auxiliary only; it does not move the exponent upper endpoint unless the accumulation problem is solved.

## Falsification checks to perform before promotion

- Re-derive the corrected `u,v` from the unnormalized loop variance `G0`; do not import the old wrong correlations.
- Verify the circulant covariance eigenvalues `1+2u+v`, `1-v` (double), `1-2u+v` are positive.
- Verify exactly that `0<q<1`.
- Reconstruct the four-negative event under the orthogonal sum/difference map; a sign or scale error here would invalidate the whole route.
- Check that the trace normalization remains exactly `tr(K^4)=p4/(1-r^4)`.
- Use only the already source-valid direction from continuous persistence to sampled persistence; do not claim a discrete event proves a continuous lower probability.
- If `theta=17/100` is tested, certify `x < r^(4 theta)` and the Temple/tail inequalities with exact or outward-rational arithmetic.
