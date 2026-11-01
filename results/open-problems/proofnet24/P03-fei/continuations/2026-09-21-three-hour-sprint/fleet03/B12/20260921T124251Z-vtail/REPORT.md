# fleet03 / B12 — analytic region-2 `v -> 0` closure for the M=96 read-once candidate

Date: 2026-09-21  
Run: `20260921T124251Z-fleet03-B12-r11`  
Status: **PROVED auxiliary certificate lemma; full FEI remains OPEN.**  
Brain assistance: **WITHOUT_VERIFIED_BRAIN**.

## Why this is the current target

The live FEI entry file points B12 into the active proof/numerics sprint. Its fleet03 assignment is the
`v -> 0` boundary of region 2, analytic divided-difference enclosures, and removal of heuristic transcendental
padding for the pinned `M=96, K=40, C0=6.4548, c=0.003` read-once candidate. This run does not audit the old
read-once certificate and does not claim that a read-once result proves unrestricted FEI.

Current dependencies used:

- `continuations/2026-09-21-readonce-certificate/TASKS_2026-09-21.md`,
- `REPORT.md` and `APPROACHES.md` in the same directory,
- `continuations/2026-09-21-three-hour-sprint/SPRINT.md`,
- fleet01/B12's new exact region-2 secant identity and PL-secant vertex lemma,
- the current `c=0.003` region-3 log, whose printed metadata is tail slope `4.909600`,
  `|G_hat'| <= 30.080`, and `|Psi'| <= 21.892`.

The proof below deliberately weakens the first two candidate facts to
`tail_slope >= 49/10` and `|G_hat'| <= 31`, so the displayed precision is not used tightly.

## Exact universal statement attempted

Put `p=2^-x <= 1/2`, `q=1-v > 1/2`, `y=log2(1/v)`, and let `Phi` be the transformed
read-once potential inequality used by the current certificate. For the pinned M=96/K=40/c=.003
candidate, prove

> **Tail lemma.** For every `x >= 1` and every `y >= 40` (equivalently `0 < v <= 2^-40`),
> 
> `Phi(p,1-v) / v > 557/5 = 111.4`.

This removes the entire `v <= 2^-40` region-2 boundary from floating-point transcendental evaluation.
It is an auxiliary read-once certificate statement, not full FEI.

## A sharp analytic derivative bound for Psi

The certificate uses

`Psi(z) = phi((1-2z)^2)/z`, with `phi(w)=w log2(1/w)`.

For `0 < z <= 1/2`, set `t=1-2z` and

`h(t) = -t^2 ln(t)/(1-t)`.

Then

`Psi(z) = 4 h(t)/ln(2)` and `Psi'(z) = -8 h'(t)/ln(2)`,

where

`h'(t) = t((t-2)ln(t)+t-1)/(1-t)^2`.

Two elementary inequalities give an exact global bound.

1. Since `ln(t) <= t-1` and `t-2 < 0`,
   `(t-2)ln(t)+t-1 >= (t-1)^2`, hence `h'(t) >= 0`.
2. The assertion `h'(t) <= 3/2` is equivalent to

   `J(t)=2t(t-2)ln(t)+4t-t^2-3 <= 0`.

   But `J'(t)=4(t-1)ln(t) >= 0` on `(0,1)` and `J(1)=0`, so `J(t)<=0`.

Therefore

`-12/ln(2) <= Psi'(z) <= 0`.

This improves the old coarse certificate metadata bound `|Psi'| <= 21.892` to the exact
constant `12/ln(2) = 17.3123404906...`.

The constant is sharp for this global derivative argument: `h'(t) -> 3/2` as `t -> 1`
(`z -> 0`). Thus an attempted strengthening replacing `12` by any smaller universal coefficient
is refuted by the boundary asymptotic. A better finite-strip estimate must use correlation with
the other region-2 terms, not a smaller standalone `Psi'` supremum.

## Tail proof

The current region-2 normalized decomposition is

`Phi/v = A + B + C + D + E + F + R`,

with

- `A = [Ghat(x)-Ghat(x+lambda)]/v`,
- `B = Ghat(y)/(1-v)`,
- `C = -8 p x`,
- `D = -8(1-v)(1-p) ell(v)/ln(2)`,
- `E = -8(1-p)`,
- `F = [Psi(p)-Psi(p(1-v))]/v`,
- `R = Psi(1-v)/v >= 0`,
- `lambda = -log2(1-v) = v ell(v)/ln(2)`.

Use the exact elementary bound
`ln(2)=2 sum_{k>=0} (1/3)^(2k+1)/(2k+1) > 2/3`, hence `1/ln(2)<3/2`.

For `v<=2^-40<1/16`,
`ell(v)=-ln(1-v)/v <= 1/(1-v) <= 16/15`.

Now bound each term.

- By the secant/mean-value form and `|Ghat'|<=31`,
  `A >= -31*(16/15)*(3/2) = -248/5`.
- For `y>=K=40`, the candidate's linear tail is
  `Gnum(y)=b_*+sigma*y`, with `b_*=8-4/ln(2)>2`.
  Since `c>0`, `1/(1-v)>1`, and `sigma>=49/10`,
  `B >= 2 + (49/10)*40 = 198`.
- `x 2^-x <= 1` for `x>=1`, so `C>=-8`.
- `(1-v)ell(v)<=1`, so `D>-12`.
- `E>=-8`.
- By the sharp derivative lemma and the mean-value theorem,
  `F=p Psi'(zeta) >= -6/ln(2)>-9`.
- `R>=0`.

Therefore

`Phi/v > 198 - 248/5 - 8 - 12 - 8 - 9 = 557/5 > 0`.

This proves the tail lemma.

## Executed arithmetic check

`analytic_vtail_certificate.py` uses only Python's `Fraction` for the final rational arithmetic.
It checks

- `A >= -248/5`,
- `B >= 198`,
- `D > -12`,
- `F > -9`,
- total strict lower bound `557/5 = 111.4`.

Source SHA-256 before commit: `cca7deec012d5faefd9b1924f5d7e09a42529ead378ac656afe9fa3d22918e77`.

## What this does and does not establish

**PROVED:** the entire region-2 `v<=2^-40` tail is positive under the current candidate metadata,
with a very large margin and without evaluating `log`, `log1p`, `exp2`, or `Psi` numerically there.

**PROVED:** `-12/ln(2) <= Psi'(z) <= 0` on `(0,1/2]`; this exact analytic constant can replace the
older coarse `21.892` derivative bound wherever only a global `Psi'` bound is required.

**OPEN:** the remaining finite region-2 strip and any unresolved shards of the c=.003 read-once
certificate.

**OPEN:** the unrestricted uniform-cube Fourier entropy-influence conjecture. The current TASKS file
also records that the old 6.4547837 general target is obsolete: an external 2026 construction is already
above it. No claim here changes that full-FEI status.

## Next attack

For `2^-40 < v < 1/2`, combine fleet01's exact PL secant identity

`A = -(ell(v)/ln 2) Sec_G(x,lambda) - c p`

with the exact `Psi'` lemma above, then replace the remaining heuristic 8-ulp transcendental padding by
rational-series enclosures: positive-series bounds for `ell(v)` and the `v<=1/4` closed form
`Psi(1-v)/v = 4(1-2v)^2 ell(2v)/((1-v)ln2)`. The first goal is a bounded shard that returns the exact
surviving cells after these analytic substitutions; only then should further subdivision be spent.
