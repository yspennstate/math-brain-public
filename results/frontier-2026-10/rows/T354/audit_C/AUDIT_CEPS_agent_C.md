# T354: c(n d) with eps > 0, audit 1 (agent C, 20 Oct 2026 09:2x)

Object: agent_B/NOTE.md, "eps > 0 in closed form" (09:1x, candidate). At beta1 = 0, a_i = 1, n -> infinity at fixed
s = n d, with x0 = r d K B3/(2 B2):

    c(s) = r K - (p2/2) r1 avg Q - p2 r2 cb/(r K) - p3 r1 avg[k Q]/(r K),

where psi(y) = (sq + eps)/(sq sqrt(y) + eps), sq = sqrt(B2), r = sq/(sq + eps), p2 = psi''(1), p3 = psi'''(1), and k, Q, cb, r1, r2
are as in "c(n d) in closed form".

Verdict: CONFIRMED at s = 1 and 2, eps = 1, on the three-valued b, at beta1 0 and also at beta1 0.5 and 0.9, which the note does not claim.
- The formula gives c(1) = -0.539035. Exact roots extrapolated to d = 0 give -0.5390 at beta1 0, -0.5388 at beta1 0.5 and -0.5368
  at beta1 0.9 (order 3, still converging, as at eps = 0).
- The test can tell. At eps = 0 the same s gives -0.4775, so eps moves c by 0.06, and the rows land within 2e-4 of the eps formula.
- So the note's eps = 0 statement "the same c holds at every fixed beta1" carries over to eps = 1 on this b.
- At s = 2 the formula gives -0.408672; the rows give -0.4086 at beta1 0 and at beta1 0.5, and -0.4078 at beta1 0.9 (order 3).
- At eps 3, s = 2 (added 12:1x) the formula gives -0.481919; the rows give -0.481885 at beta1 0 (order 2) and -0.481291 at beta1 0.9
  (order 3).

## The formula, evaluated independently (cclosed_eps_3v.py)

- I wrote it from the displayed formula, not from c_closed_eps.py. r, p2 and p3 come from sympy derivatives of psi at 1.
- At eps = 0 it gives r 1, p2 3/4, p3 -15/8, and reproduces cclosed_3v.py: -0.7930, -0.4775, -0.2268 and +0.0765 at s 0.2, 1,
  2 and 5.
- At eps = 1 (sq = sqrt(4.8)) it gives r 0.686608, p2 0.407367 and p3 -0.853816.
- c(s) at eps 1 is -0.7053 at s 0.2, -0.5390 at s 1, -0.4087 at s 2 and -0.2645 at s 5.

## Exact rows (rrm3m.py with EPS=1; r3me_batch.sh, r3me_out/, r3me_table.py, r3me_table.txt)

rrm3m.py is the momentum solver of AUDIT_MOMENTUM2.
- With EPS set, each Laplace node's weight is multiplied by h(s) = 1 - eps sqrt(pi) s erfcx(eps s). This is the kernel of
  1/(sqrt(v) + eps).
- The printed coefficient is (x*/(r x0) - 1)/d.
- Check against rrm_eps.py, an earlier exact eps solver on a different code path. At beta1 0 on 9/-1, n 100, beta2 .99, eps 1:
  x* 0.018884436020757 against 0.0188844359973.

b = (6, 2, -1) with weights 0.1, 0.1, 0.8:

| n d | beta1 | d = 0.02 | d = 0.01 | d = 0.005 | d = 0.0025 | d -> 0 | formula |
|---|---|---|---|---|---|---|---|
| 1 | 0 | -0.588238 (n 50) | -0.563923 (n 100) | -0.551533 (n 200) | | -0.5390 | -0.5390 |
| 1 | 0.5 | -0.475200 (n 50) | -0.503656 (n 100) | -0.520378 (n 200) | | -0.5388 | -0.5390 |
| 1 | 0.9 | +0.017576 (n 50) | -0.158383 (n 100) | -0.311447 (n 200) | -0.413717 (n 400) | -0.5368 | -0.5390 |
| 2 | 0 | -0.465256 (n 100) | -0.436981 (n 200) | -0.422808 (n 400) | | -0.4086 | -0.4087 |
| 2 | 0.5 | -0.386707 (n 100) | -0.396168 (n 200) | -0.402007 (n 400) | | -0.4086 | -0.4087 |
| 2 | 0.9 | +0.025251 (n 100) | -0.137741 (n 200) | -0.255032 (n 400) | -0.326449 (n 800) | -0.4078 | -0.4087 |

d -> 0 is the highest-order Richardson extrapolation (halving in d). At beta1 0 the order-1 values are -0.5396 and -0.5391, so the
O(d^2) term is small. At beta1 0.9 the order-1, 2 and 3 values are -0.516, -0.533 and -0.537: the same slow approach as the eps = 0
row of AUDIT_MOMENTUM2 (-0.448, -0.470, -0.474 against -0.4775). There, as here, the finite-d rows sit above the limit.

## beta1 0.9 at s = 2 (added 20 Oct 11:2x; r3me3_batch.sh, r3me3_out/, r3me3_rich.py)

The prediction was written to r3me3_out/PREDICTION.txt at 10:38, before the runs: every row above -0.4087 and falling with d, a gap
of 0.05-0.15 at d 0.01, and the highest-order extrapolation within 5e-3 of the formula.
- The rows sit above the limit and fall monotonically. Gaps 0.434, 0.271, 0.154 and 0.082; successive ratios 1.60, 1.76 and 1.88,
  moving toward 2 as the O(d) term takes over.
- Richardson, order 1: -0.3007, -0.3723, -0.3979; order 2: -0.3962, -0.4064; order 3: -0.407837. That is 8.4e-4 above -0.408672.
- The gap at d 0.01 was 0.271, outside the predicted band. The n d 1 row at beta1 0.9 (gap 0.381 at d 0.01) was the better guide;
  the d^2 term at beta1 0.9 does not shrink much between s = 1 and s = 2.
- So c(2) at eps 1 does not depend on beta1 either, to the precision that four halvings allow. The n 800 root took 2 secant steps,
  the others 3.

## eps 3 at s = 2, beta1 0 and 0.9 (added 20 Oct 12:1x; r3me4_batch.sh, r3me4_out/, r3me4_rich.py)

At eps 3 the formula gives c(2) = -0.481919 (eps 1 gives -0.408672 and eps 0 -0.226842, so the test separates eps 3 from both). The
prediction was written to r3me4_out/PREDICTION.txt at 11:29:03, before any run: beta1 0 rows below the limit and rising, order 2
within 1e-3; beta1 0.9 rows above it and falling, a gap of 0.15-0.35 at d 0.01, order 3 within 2e-3; a miss of more than 5e-3 on
either would count against beta1-freedom beyond eps 1. Every part held.
- beta1 0, d 0.02, 0.01, 0.005: rows -0.517231, -0.499736, -0.490855. Order 1: -0.482241, -0.481974; order 2: -0.481885, 3.4e-5
  from the formula. This half repeats the note's own eps 3 check by an independent solver.
- beta1 0.9, d 0.02 to 0.0025: rows -0.123696, -0.259193, -0.355960, -0.414623. Gaps 0.358, 0.223, 0.126, 0.067; successive ratios
  1.61, 1.77, 1.88, the same approach to 2 as at eps 1. Order 1: -0.3947, -0.4527, -0.4733; order 2: -0.4721, -0.4801; order 3:
  -0.481291, 6.3e-4 above the formula. The n 800 root took 2 secant steps.
- So c(2) does not depend on beta1 at eps 3 either, on this b, to the precision four halvings give. The beta1 0.9 rows converge a little
  faster at eps 3 than at eps 1 (gap 0.223 against 0.271 at d 0.01), and the order-3 miss is smaller (6.3e-4 against 8.4e-4).

## Not covered

- Audit 2 (agent A, ../audit_A/AUDIT_CEPS_agent_A.md) has since covered three items this list carried: s = 5 at
  beta1 0 (Monte Carlo and exact rows on 9/-1 and 6/2/-1), the by-hand rederivation of p2 = r/4 + r^2/2 and p3 = -(3/8)(r + 2r^2 +
  2r^3) and of the solve that carries them into the cb and avg[k Q] terms, and the second audit itself.
- Still open: s other than 1 and 2 at beta1 > 0, and eps other than 1 and 3 at beta1 > 0.
- The large-s limit. NOTE.md (line 636) states that c(inf) = r - p2 r1/4 - p2 r2/r - p3 r1/(2 r) equals the verified iid eps bracket
  (0.3056 on 9/-1 at eps 1), and audit 2 derives the same limit from the formula. This audit did not check that identity.

Files: cclosed_eps_3v.py, rrm3m.py (EPS), r3me_batch.sh, r3me2_batch.sh, r3me_out/, r3me_table.py, r3me_table.txt, r3me3_batch.sh,
r3me3_out/, r3me3_rich.py, r3me4_batch.sh, r3me4_out/, r3me4_rich.py.
