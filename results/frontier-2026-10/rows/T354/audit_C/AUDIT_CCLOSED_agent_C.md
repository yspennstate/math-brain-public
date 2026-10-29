# T354: c(n d) in closed form, audit 1 (agent C, 20 Oct 2026 08:3x)

Object: agent_B/NOTE.md, "c(n d) in closed form" (push 56ed125c, candidate). Claim, at beta1 = 0, eps = 0, a_i = 1, in the
limit n -> infinity at fixed s = n d:

    x*/x0 = 1 + d c(s) + o(d),   c(s) = K - (3/8) r1 avg Q - (3/4) r2 cb/K + (15/8) r1 avg[k Q]/K,

with r1 = (B4 - B2^2)/B2^2, r2 = E[bZ^2]/(B2 B3), and k, Q, cb as in the note. The two limits are c(0+) = 1/2 - r2/4 and
c(inf) = 1 + (3/4)(r1 - r2).

Verdict: CONFIRMED on a distribution with r1 != r2, which the note listed as untested.
- The 9/-1 model cannot test the formula's structure. There r1 = r2 = 64/9, so any reshuffling of r1 and r2 between the terms
  gives the same numbers.
- I used b = 6, 2, -1 with weights 0.1, 0.1, 0.8. This gives B2 4.8, B3 21.6, B4 132, r1 4.7292, r2 5.5231.
- The closed form matches exact roots extrapolated to d = 0 at n d 0.2, 1 and 2, to 1e-4 or better. At n d 5 it matches within
  1e-4 (three points, quadratic). At n d 10 only two points exist (d .02, .01): the linear extrapolation gives +0.2311 against +0.2269.
  At n d 5 the linear fit through the same two d values overshoots its quadratic by 0.003, so the n d 10 gap of 0.004 is the same curvature.
- The two wrong-formula foils (r2 set to r1, r1 set to r2) miss by 0.04 to 0.5 at the same points.
- Both limits hold on this model. c(0+) = -0.8808 and c(inf) = +0.4045. For this b the formula approaches the iid value 0.40
  from below, not 1.

## Exact solver (rrm3v.py, r3v_batch.sh, r3v_out/)

rrm3v.py is rrm_indep.py (the independent large-n solver of AUDIT_LARGE_N) with two special types instead of one.
- The per-epoch counts are n/10 samples with b = 6, n/10 with b = 2, and the rest with b = -1.
- The current epoch's placement mean M_{h1,h2} is built by a two-type recursion over slots. Its weights are multivariate
  hypergeometric, conditioned on the type of g_k itself.
- Each earlier epoch is a table G(y) in log y. It is rebuilt for each x, because a2/a1 depends on x.
- The root is found by secant from x0(1 - 0.6 d), with a guard against a flat step. That guard is what crashed at n 200 before
  it was added.

Validation:
- With b = (9, -1, -1) the second type is the bulk value. The solver then gives the two-valued roots of the earlier audits: n 10,
  beta2 .999: -0.879443 (rr2_runs.txt -0.879445); n 10, beta2 .99: -1.247263; n 100, beta2 .99: -0.648602 (rrmi_out).
- One root at n 200 takes 16 s.

(x*/x0 - 1)/d, with x0 = d K_rr B3/(2 B2) at finite n (r3v_table.py):

| n d | d = 0.02 | d = 0.01 | d = 0.005 | d = 0.0025 | d -> 0 | closed form |
|---|---|---|---|---|---|---|
| 0.2 | -0.856335 (n 10) | -0.825555 (n 20) | -0.809483 (n 40) | | -0.7930 | -0.7930 |
| 1 | -0.555531 (n 50) | -0.516668 (n 100) | -0.497093 (n 200) | -0.487299 (n 400) | -0.4775 | -0.4775 |
| 2 | -0.310801 (n 100) | -0.268303 (n 200) | -0.247405 (n 400) | | -0.2267 | -0.2268 |
| 5 | -0.015838 (n 250) | +0.031815 (n 500) | +0.054551 (n 1000) | | +0.0766 | +0.0765 |
| 10 | +0.129467 (n 500) | +0.180304 (n 1000) | | | +0.2311 (linear) | +0.2269 |

d -> 0 is the quadratic through the last three points, or the linear fit through two. The slope per unit d is about -4 at every
n d, and n runs from 10 to 1000, so the O(d^2) term is n-free here too.

## The closed form, evaluated independently (cclosed_3v.py, cclosed_3v.txt)

I wrote the evaluator from the note's displayed formulas, not from c_closed.py or c_closed_sym.py.
- It uses Gauss-Legendre quadrature over theta.
- It checks avg k against the note's K = 1 - 1/s + (1 - e^-s)/s^2.
- On the 9/-1 model it reproduces the note's table: -0.588 at s 1, +0.381 at s 5, +0.660 at s 10, +0.928 at s 50. It also
  reproduces (1 - c) s -> 1 + 3 r1/8 = 3.667.

| s | 0.2 | 1 | 2 | 5 | 10 |
|---|---|---|---|---|---|
| c(s), three-valued b | -0.7930 | -0.4775 | -0.2268 | +0.0765 | +0.2269 |
| foil, r2 set to r1 | -0.5698 | -0.1793 | +0.1341 | +0.5343 | +0.7435 |
| foil, r1 set to r2 | -0.7547 | -0.3155 | +0.0364 | +0.4831 | +0.7156 |

The four terms of c(s) at s 1 are +0.632, -0.234, -2.075 and +1.199, in the order K, the E eta^2 term, the cb term and the
E[b eta^3] term. At s 2 they are +0.716, -0.383, -2.511 and +1.951. The last term is the step the note justifies loosely: "3 E[b
eta_c] times the variance of the rest", with the conditioning corrections dropped. That term is 1.2 to 2 in size, and the total
matches the exact rows to 1e-4. So its coefficient 15/8 and its use of r1 (not r2) are confirmed to about 1e-4 relative. The
cb term's use of r2 is confirmed the same way.

## The limits

- c(0+): c(1e-4) = -0.88074 against 1/2 - r2/4 = -0.88079. At small s only the cb term survives, and cb -> 1, K -> 1/2.
- c(inf): c(1e4) = 0.40433 against 1 + (3/4)(r1 - r2) = 0.40451. The gap is the 1/s tail.
- The note's (1 - c) s -> 1 + 3 r1/8 is a two-valued statement. With r1 != r2, c tends to 1 + (3/4)(r1 - r2), not to 1, so
  (1 - c) s grows without bound. The sentence is correct as the note scopes it ("two-valued b"). A general version would read
  (c(inf) - c(s)) s -> a constant in r1, r2.

## Not covered

- eps > 0 and beta1 > 0 on the three-valued b. The note's "the same c holds at every fixed beta1" was checked on 9/-1 only (by
  agent A).
- A by-hand rederivation of avg[k Q] and cb in the large-n limit. The match to 1e-4 at three values of s makes an error in them
  unlikely, but it is not a proof.
- A second audit.

Files: rrm3v.py, r3v_batch.sh, r3v_out/, r3v_table.py, cclosed_3v.py, cclosed_3v.txt.
