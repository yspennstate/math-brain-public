Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum is the owner's requested preference, not authenticated runtime telemetry here.

# P0434 / P01-A — corrected compact proof of the two-record finite-law theorem

**PROVED PARTIAL relative to Scully–Harchol-Balter–Scheller-Wolf (2020), Conjecture 8.1.** This file supersedes the same-run `T101100Z` exposition, which contains one harmless LaTeX escape typo in the exceptional-face estimate. The mathematics and the exact checker are unchanged.

## Theorem

Let `X` have positive finite support. If the increasing-envelope M-SERPT rank has at most two strict internal record jumps, then for every stable load `rho<1`,

`E[T_MS] <= 2 E[T_G]`.

The zero/one-record cases and the aligned two-record case were proved in preceding R7-04 reports. It remains only to prove the case of two M-SERPT records `b1<b2` in which Gittins skips `b1` and, by the inherited final-record theorem, uses `b2`.

## Exact three-block formulas

Write the M-SERPT block masses as

`p=P(X<=b1)`, `q=P(b1<X<=b2)`, `r=P(X>b2)`,

and set `s=p+q`, `t=q+r`. Let

`m_j=E[X wedge b_j]`, `V_j=E[(X wedge b_j)^2]`,

`a=1-lambda m_1`, `b=1-lambda m_2`, `c=1-rho`.

Then `1>a>b>c>0` and

`Q_MS = lambda/2 * [p V1/a + q V2/(ab) + r V3/(bc)]`,

`R_MS = M1 + M2/a + M3/b`.

In the skipped-first Gittins topology, the Proposition-4.7 waiting lower surrogate is

`Qbar_G = lambda/2 * [s V2/b + r V3/(bc)]`.

Since `Q_G>=Qbar_G` and `R_G>=mu:=E[X]`, it suffices to prove

`H := 2 Qbar_G - Q_MS + 2 mu - R_MS >= 0`.

## Topology coordinates

Set `x=1-a=lambda m1`, `y=1-b=lambda m2`, and define the two SERPT record margins

`f = p rho - x`, `e = s rho - y`.

The first record is strict, so `0<f<p rho`. Because `b1` lies in the Gittins valley ending at `b2`, its endpoint chord satisfies

`(m2-m1)/q <= m2/s`,

or equivalently

`d := s x - p y = p e - s f >= 0`.

Also `m2>m1`, hence `e<q rho+f`. The skip condition automatically implies the second record is above the first because

`e/f >= s/p > r/t`, with `s t - p r = q>0`.

Normalize the complete domain by

`p=P`, `q=(1-P)Q`, `r=(1-P)(1-Q)`, `rho=R`,

`f=P R F`,

`e=R[(P+(1-P)Q)F + (1-P)Q(1-F)E]`,

where `P,Q,R,F in (0,1)` and `E in [0,1)`. Then exactly

`a = 1 - P R (1-F)`,

`b = 1 - R(1-F)[P+(1-P)Q(1-E)]`,

`a-b = R(1-P)Q(1-F)(1-E)>0`,

`d = P(1-P)Q R(1-F)E >= 0`.

## Exact waiting rearrangement

Direct algebra yields

`2 Qbar_G - Q_MS = lambda/2 * [ k V2/(ab) + p(V2-V1)/a + r V3/(bc) ]`,

where

`k = s a - d = 2 s a - q - p b`.

This coefficient is positive. Indeed `y>x` gives `d<q x`, while the strict first record gives `x<p`; therefore

`k > s - x(s+q) > s - p(s+q) = p r + q(q+r) > 0`.

Since `V2>=V1`,

`2 Qbar_G-Q_MS >= lambda/2 [k V2/(ab)+r V3/(bc)]`.

## Cauchy reduction

Let `q_j=lambda M_j`, so `q1+q2+q3=rho`, and put `u=q1+q2`. Blockwise Cauchy gives

`lambda^2 V3 >= q1^2/p + q2^2/q + (rho-u)^2/r`,

and because `y=q1+q2+r lambda b2`,

`lambda^2 V2 >= q1^2/p + q2^2/q + (y-u)^2/r`.

Hence `lambda H >= B(q1,q2)`, where

`B = 2rho - q1 - q2/a - (rho-u)/b`

`    + k/(2ab)[q1^2/p+q2^2/q+(y-u)^2/r]`

`    + r/(2bc)[q1^2/p+q2^2/q+(rho-u)^2/r]`.

We can minimize over all real `q1,q2`, enlarging the feasible domain. Define

`H0 = c k + a r > 0`.

At fixed `u`, exact square completion gives

`B_*(u) = 2rho-u/a-(rho-u)/b`

`         + k(y-u)^2/(2abr) + (rho-u)^2/(2bc)`

`         + H0 u^2/(2abc s) + p(1-a)u/(a s)`

`         - p q (1-a)^2 b c/(2 a s H0)`.

Its leading coefficient is

`A2 = H0/(2 a b c r s) > 0`.

Thus only its discriminant matters.

## Discriminant certificate

If `Delta` is the discriminant of `B_*`, exact simplification gives

`Delta = - P0(p,q,a,b,c)/(a^2 b^2 c^2 s r)`

for a polynomial `P0`. Under the cube normalization above, call the resulting polynomial `Pcube(P,Q,R,F,E)`. It has multidegree `(6,4,6,4,4)` and 1475 nonzero power-basis terms.

Its exact tensor Bernstein expansion on `[0,1]^5` has 6125 coefficients: 4397 positive, 1727 zero, and one negative. The smallest positive coefficient is `1/1350`; the unique negative coefficient is `-1/300` at multi-index `(4,4,3,0,4)`.

That coefficient lies in the single face slice `Q=1,F=0,E=1`. Group the whole slice:

`Pcube = Q^4 (1-F)^4 E^4 G(P,R) + Rem`,

where every Bernstein coefficient of `Rem` is nonnegative. Exact factorization gives

`G(P,R)=R(1-R) J(P,R)`,

with

`J = P^5 R^4 - 2P^5 R^3 - 8P^4 R^4 + 14P^4 R^3 - 2P^4 R^2 + P^4 R`

`    + 8P^3 R^4 - 3P^3 R^3 - 16P^3 R^2 + P^3 R`

`    - 14P^2 R^3 + 20P^2 R^2 + 4P^2 R`

`    + 7P R^2 - 12P R - R + 2`.

For `J`, an exact `32 x 32` dyadic Bernstein subdivision certifies positivity on 1022 cells. The only two uncertified cells are `(30,31)` and `(31,31)`, both inside `U=1-P<=1/16`, `V=1-R<=1/16`.

There

`J(1-U,1-V)`

`= -U^5V^4 + 2U^5V^3 - 2U^5V + U^5`

`  -3U^4V^4 + 8U^4V^3 - 8U^4V^2 + 3U^4V`

`  +14U^3V^4 - 23U^3V^3 + 9U^3V^2`

`  -14U^2V^4 + 15U^2V^3 - U^2V^2`

`  +3UV^4 - 3UV^3 + V^4 + V^3`.

With `delta=1/16`, weighted AM-GM and Young's inequality dominate all eight negative monomials by

`A U^5 + B V^3`,

where exactly

`A=303109/327680<1`,

`B=11453771/26214400<1`.

Therefore

`J(1-U,1-V) >= (1-A)U^5+(1-B)V^3 >=0`.

So `J>=0` on the whole square, hence `G>=0`, `Pcube>=0`, and therefore `Delta<=0`. In the strict topology the nonnegative Bernstein remainder has positive terms, so `Delta<0` and `B_*(u)>0`. The chord-tie boundary is covered by the same weak inequalities.

Consequently `H>=0`, and

`2E[T_G]-E[T_MS] >= H >=0`.

This proves the skipped-first case and hence the theorem.

## Exact check and consequence

The exact checker and archived output are

- `research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T101000Z__P0434_two_record_skip_checker.py`
- `research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T101000Z__P0434_two_record_skip_checker.out`

The output ends `ALL_EXACT_CHECKS_PASS`. It also checks the inherited skipped-first witness `X in {1,2,4,8}`, masses `(1/20,11/20,1/4,3/20)`, `rho=19/20`, for which the new target equals exactly

`60274143/1767050 > 0`.

Therefore any finite-support counterexample to Conjecture 8.1 must have **at least three strict internal M-SERPT record jumps**. Since the final record is always shared with Gittins, the remaining finite obstruction is a longer prefix rank-mismatch chain. This is the correct next interface with P01-B's Stieltjes prefix-rectangle program.
