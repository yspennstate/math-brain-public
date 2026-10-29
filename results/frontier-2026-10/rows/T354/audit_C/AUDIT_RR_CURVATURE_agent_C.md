# T354 next-order term under random reshuffling with unequal curvatures, eps = 0 and eps > 0 (agent C, 20 Oct 2026 05:5x)

Objects, both in agent_B/NOTE.md:

- "Random reshuffling, unequal curvatures, eps = 0, any beta1" (05:1x). Audit 1 is agent A's
  (audit_A/AUDIT_RR_CURV_agent_A.md), so this is audit 2:

      x0 = d K B3/(2 abar B2),   x*/x0 = 1 + d (K c1/(2 abar) - (3/4) T H/(K B2 B3)) + O(d^2),
      c1 = (3 E[a b^2] - abar B2)/B2 - 2 B3 E[a b]/B2^2.

- "Random reshuffling, unequal curvatures, eps > 0" (05:4x). No outside audit yet, so this is audit 1:

      x0 = r d K B3/(2 abar B2),   x*/x0 = 1 + d (K (r c1 + r1 B3/B2)/(2 abar) - p2 T H/(r K B2 B3)) + O(d^2),
      s = sqrt(B2),  r = s/(s + eps),  r1 = eps E[a b]/(s (s + eps)^2),  p2 = s(eps + 3s)/(4 (eps + s)^2).

Verdict: both are CONFIRMED.
- The coefficients are re-derived by hand below.
- Exact roots on b = (6, 2, -1 x 8) were computed with three curvature vectors, eps 0 and 1, beta1 0 and 0.9 (12 families, 36 roots).
- In every family the gap to the formula is O(d^2): a three-point fit leaves an intercept of at most 3e-6.
- The eps > 0 formula without the r1 term fails in all six eps 1 families. That term is needed.
- b = (6, 2, -1 x 8) takes three values, which audit 1 did not cover.

## Re-derived by hand

- g_i = a_i x + b_i with E b = 0. The mean gradient is f'(x) = abar x.
- V = E g^2 = B2 + 2 E[a b] x + O(x^2) and C = E[g Z] = E g^3 - abar x V. To first order in x:
  - E g^3 = B3 + 3 E[a b^2] x.
  - C/V = B3/B2 + c1 x, with c1 exactly as in the note.
  - At a = 1, E[a b] = 0 and E[a b^2] = B2, so c1 = 2.
- K is unchanged under RR. Within an epoch the Z sum to zero, so E[g_a Z_b] = -C/(n - 1) for a != b. That uses only the
  gradient values, not a.
- Q is the quadratic term of the moment ratio. It is taken at x = 0, where a drops out, so it is (d/B2)^2 T H as in the a = 1 case.
- eps = 0: the drift is 0 = abar x - (1/2) d K C/V + (3/8) Q + O(d^3), so x (abar - d K c1/2) = d K B3/(2 B2) - (3/8) Q.
  - Dividing by abar x0 gives the note's coefficient.
  - (3/8) Q/(abar x0) = (3/4) d T H/(K B2 B3); abar cancels.
- eps > 0: psi'(1) = -r/2 and psi''(1) = p2, as in my audit of the a = 1 case (AUDIT_RR_NEXT_ORDER_EPS_agent_C.md).
  - The new piece is that r depends on x through V: s(x) = sqrt(V) = s + E[a b] x/s + O(x^2) and dr/ds = eps/(s + eps)^2.
  - So r(x) = r + r1 x, with r1 = eps E[a b]/(s (s + eps)^2) as in the note.
  - The linear term of (r(x)/2) d K C/V is (d K/2)(r c1 + r1 B3/B2) x. Q is already O(d^2), so p2 and r there need no slope.
  - Dividing by abar x0 = r d K B3/(2 B2) gives the note's coefficient. The Q term is p2 d T H/(r K B2 B3), with no abar.
- At a = 1, r1 = 0, which is the verified a = 1 eps > 0 formula.

## Exact roots (rr_exact_two_special_a.py, rra_batch.sh, rra_jobs.txt, rra_runs.txt; tables rra_table.py, rra_table2.py)

The solver:
- It is my eps solver (rr_exact_two_special_eps.py, audit of 5ab4bd84) with one change: g_i = a_i x + b_i, with a = (A1, A2, AO) on
  the two special samples and the rest.
- It is built by a script from the eps solver. The RR drift code and the erfcx kernel are untouched.
- It prints two predictions:
  - "guess" puts r on c1 only.
  - "withr1" is the note's eps > 0 formula. At eps 0 the two are the same.
- Control: a = (1, 1, 1), eps 0, beta1 0, beta2 0.999 gives (x*/x0 - 1)/d = -0.879445. That matches my eps = 0 audit run (rr2_runs.txt).

Model b = (6, 2, -1 x 8), n = 10, B2 = 4.8, B3 = 21.6. The curvature vectors:

| a | abar | E[a b] | c1 | r1 B3/B2 at eps 1 |
|---|---|---|---|---|
| (4, 0.5, 0.5 x 8) | 0.85 | 2.1 | 4.5875 | 0.4236 |
| (1, 1, 2 x 8) | 1.8 | -0.8 | 3.2 | -0.1614 |
| (0.5, 2, 1 x 8) | 1.05 | -0.1 | 1.2625 | -0.0202 |

How to read the table:
- gap(d) = exact minus the formula, where the formula uses the exact K at the same beta2 (the K-form, as in the earlier audits) and d = 1 - beta2.
- g0 is the intercept of a fit gap = g0 + g1 d + g2 d^2 through beta2 0.9995, 0.999 and 0.998. It is zero when the formula's O(d) coefficient is exact.

| a | eps | beta1 | formula limit (withr1) | exact at beta2 0.9995 / 0.999 / 0.998 | gap/d vs formula | g0 vs formula | gap/d without r1 |
|---|---|---|---|---|---|---|---|
| (4, .5, .5) | 0 | 0 | -0.026527 | -0.029933 / -0.028350 / -0.025203 | -6.81 / -6.80 / -6.77 | -7e-07 | (same) |
| (4, .5, .5) | 0 | 0.9 | 0.170165 | 0.171863 / 0.174559 / 0.179944 | 3.40 / 3.41 / 3.44 | -1e-06 | (same) |
| (4, .5, .5) | 1 | 0 | -0.037367 | -0.040267 / -0.039248 / -0.037220 | -5.80 / -5.79 / -5.76 | +3e-18 | 243.9 / 119.3 / 57.0 |
| (4, .5, .5) | 1 | 0.9 | 0.129657 | 0.130574 / 0.132273 / 0.135663 | 1.83 / 1.85 / 1.87 | -2e-06 | 77.4 / 39.7 / 20.8 |
| (1, 1, 2) | 0 | 0 | -0.933004 | -0.935770 / -0.935200 / -0.934069 | -5.53 / -5.52 / -5.49 | -2e-06 | (same) |
| (1, 1, 2) | 0 | 0.9 | -0.104095 | -0.102397 / -0.100119 / -0.095553 | 3.40 / 3.41 / 3.44 | -1e-17 | (same) |
| (1, 1, 2) | 1 | 0 | -0.807042 | -0.809504 / -0.809451 / -0.809344 | -4.92 / -4.91 / -4.89 | -1e-06 | -49.8 / -27.4 / -16.2 |
| (1, 1, 2) | 1 | 0.9 | -0.103214 | -0.102296 / -0.100951 / -0.098254 | 1.84 / 1.85 / 1.87 | -1e-06 | -11.8 / -5.0 / -1.5 |
| (.5, 2, 1) | 0 | 0 | -1.077117 | -1.079500 / -1.078809 / -1.077434 | -4.77 / -4.75 / -4.72 | -7e-07 | (same) |
| (.5, 2, 1) | 0 | 0.9 | -0.147697 | -0.145981 / -0.143751 / -0.139280 | 3.43 / 3.45 / 3.47 | -3e-06 | (same) |
| (.5, 2, 1) | 1 | 0 | -0.888348 | -0.890613 / -0.890511 / -0.890305 | -4.53 / -4.52 / -4.49 | -7e-07 | -14.2 / -9.3 / -6.9 |
| (.5, 2, 1) | 1 | 0.9 | -0.127813 | -0.126886 / -0.125569 / -0.122925 | 1.85 / 1.87 / 1.89 | -3e-07 | -1.1 / 0.4 / 1.2 |

- The gap/d against the formula is flat in d in all twelve families, and the intercepts are at most 3e-6. That is the size of the
  printed rounding of (x*/x0 - 1)/d, which has six decimals.
- Without r1, gap/d roughly doubles each time d halves. That means an O(1) error in the coefficient: 0.12 for a = (4, .5, .5) at
  beta1 0, and 0.022 for (1, 1, 2). The sign follows E[a b]. For (.5, 2, 1), E[a b] is only -0.1 and the error is 0.005, still visible.
- At a = (4, .5, .5), beta1 0.9 the coefficient is positive at both eps (+0.170 and +0.130), and the formula follows it.
- Node count: a = (4, .5, .5), eps 1, beta1 0, beta2 0.999 at 240 nodes gives x* = 0.000912035278462, the same in all twelve
  printed digits as at 160 nodes.

Agreement with the row's own check: B's next_order_rr_a_eps.py used b = (9, -1 x 9) and pairs (3, 1), (4, 0.5) at eps 1 and 10.
It reports flat gap/d and finds the formula without r1 off by 0.04-0.15. This audit uses a different b (three values, a smaller
skew ratio) and a different solver lineage, and finds the same.

## Not covered

- eps 10 with unequal a. Only eps 1 was run here; the row's own check covers eps 10.
- beta1 0.5.
- A rigorous remainder.
- The regime where n d is not small.
- Vector b.
- a_i that differ within the bulk of samples. Here they differ only between the two special samples and the rest.
