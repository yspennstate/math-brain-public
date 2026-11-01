# Audit of agent_B/REFUTATION_T2.md (T353, Conjecture 3.2 of arXiv:2403.17673 at T = 2)

agent A, 19 Oct 2026. Verdict: CONFIRMED (numerically, by an independent model and code; not yet an interval-arithmetic proof).

## Scope, against the paper (ar5iv HTML of 2403.17673, read 19 Oct)
- Definition 2.3: (P, Q) dominates M if D_{e^eps}(P||Q) >= D_{e^eps}(M(x)||M(x')) for ALL eps in R and all zero-out adjacent x -> x'
  (x_i in X, x'_i = bottom); "tightly" adds equality for some pair. So one eps at which some adaptive method exceeds D(P_S||Q_S)
  breaks domination, and the write-up exceeds max(D(P_S||Q_S), D(Q_S||P_S)), so it breaks it under either orientation convention.
- Conjecture 3.2 says (P_S, Q_S) tightly dominates ABLQ_S "for all adaptive query methods", with P_S = mean_t N(2 e_t, s^2 I_T),
  Q_S = mean_t N(e_t, s^2 I_T) - the pair the write-up uses.
- ABLQ: psi_t: X -> B^d chosen from g_1..g_{t-1}, g_t = sum over the batch + N(0, s^2 I_d), A(.; bottom) = 0, n = bT, shuffle into T
  batches of b. The construction (X = {u, w}, d = 1) is inside this for every b >= 1, b = 1 included: with all other records equal to
  w, only the batch holding the record differs after the known shift b psi_t(w), and the record's batch is uniform under the shuffle.
- The follow-up 2411.04205 (read 19 Oct) does not restate the conjecture; it calls the exact guarantee for shuffled ABLQ open and
  uses a non-adaptive query method for its lower bound. One extended web search (19 Oct) found no published refutation.

## Independent check (audit_A/)
I wrote the model from the definition, not from the candidate's scripts: step-2 freedom is (a, c) = (psi2(u) - psi2(w), -psi2(w)),
the g2 means under x and x' when the record is in batch 2.
- check_t2_grid.py (trapezoid on (g1, g2), h = 0.02 and 0.01; check_t2_grid_run1.txt): D(P_S||Q_S) = 0.221269, D(Q_S||P_S) = 0.205107;
  ANTI everywhere = 0.221269 (equals D(P_S||Q_S), as the sign-flip argument says); pointwise max(ANTI, SAME) = 0.223234 (h 0.02: 0.223231);
  the pointwise best over a 9 x 9 grid of psi_2 in [-1, 1]^2 is the same 0.223234, so on this grid SAME and ANTI are the only answers
  that matter.
- One-point inequality: I_SAME - I_ANTI = +5.781e-4 at g1 = -2.5 and +4.531e-6 at g1 = -3.0 (the write-up: +5.78e-4, +4.53e-6).
  SAME wins on g1 <= -2 only.
- The gain 0.223234 - 0.221269 = 1.97e-3 is about 10^3 times the change between the two grid spacings.

## Points for the write-up
1. The claim needs only the one-point inequality plus continuity; the 30-digit mpmath value and the two independent grids agree, but a
   rigorous version should bound I(g1) by interval arithmetic (it is a 1-D integral of the positive part of a sum of four Gaussians
   at fixed g1, so the roots in g2 can be bracketed and the integral written with Phi).
2. The result is for zero-out adjacency, eps = 1/2, s = 1, d = 1, T = 2. State that the conjecture fails as soon as it fails at one eps;
   say nothing beyond the parameters checked until sweep1/renyi2 are audited too (not done here).
3. The construction is adaptive in an essential way: on the 9^4 non-adaptive grid the conjectured pair is optimal (candidate's
   nonadaptive.py, not re-run here).
Not checked by me: renyi2.py, sweep1.txt, threshold_quad.py, exact_closed.py.

## 19:2x addendum: the one-point inequality, proved in ball arithmetic (audit_A/rigorous_point.py, _run1.txt)
At fixed g1 the step-2 integrand is f(x) = u phi(x) + v(phi(x - a) - E phi(x - c)) with u = (phi(g1+2) - E phi(g1+1))/2, v = phi(g1)/2,
and f/phi is a quadratic in e^x for ANTI (a, c) = (2, 1) and monotone in x for SAME (0, -1). So the zero set of f is closed form, and
I(g1) = integral of f+ is a short combination of Phi values at the roots. Evaluated in python-flint arb at 200 bits:
  g1 = -2.5: I_SAME - I_ANTI = 0.0005781226801 +/- 1.1e-14   (proved > 0)
  g1 = -3:   I_SAME - I_ANTI = 4.531470335e-6 +/- 5.0e-16    (proved > 0)
  g1 = -2.01: +9.73e-4 (proved); g1 = -1.99: -9.27e-4 (ANTI wins, proved).
The switch is at g1 = -2 exactly: there u = 0, since phi(0)/phi(1) = e^{1/2} = E. Both I are continuous in g1, so SAME > ANTI on a
neighbourhood of -2.5; the adaptive method (SAME when g1 < -2, ANTI otherwise) has D_{e^{1/2}}(M(x)||M(x')) > integral of I_ANTI =
D_{e^{1/2}}(P_S||Q_S), the last equality exact by the map g1 -> -g1. That breaks Definition 2.3 domination at eps = 1/2, sigma = 1, T = 2,
every b, with no numerics left in the argument except the arb enclosures. What the proof does not give: the size of the gap (0.22323 vs
0.22127 is still the grid value), and D(Q_S||P_S) < 0.22323 (only needed if one reads the conjecture with the max convention).

## Size of the gain from the closed form (audit_A/gap_total.py, _run1.txt; mpmath 30 digits, 1-D quad with analytic breakpoints)
  D_{e^{1/2}}(P_S||Q_S) = 0.22126854532024441193   (integral of I_ANTI over all g1; grid gave 0.221269)
  gain                  = 0.0019660410484528388   (integral of I_SAME - I_ANTI over g1 < -2)
  D(policy)             = 0.22323458636869725074   (grid 0.223234; the candidate's 0.22324)
Breakpoints: ANTI's discriminant vanishes at g1 = -2.18822640646; SAME's integrand is empty on (-1.82400453938, -0.17599546062), the
roots of e^-2 z^2 - z + 1 = 0 with z = e^{-g1}. This is a third independent route (closed-form inner integral, not a 2-D grid) and it
agrees with both grids to the digits they carry. Not interval-rigorous for the size; the sign of the gain is proved above.

## Addendum 20:4x 19 Oct: the adaptive quadrature check finished (check_t2.py, check_t2_run1.txt)
Adaptive quad on the same independent model: D(P_S||Q_S) = 0.221269; ANTI everywhere 0.221268, pointwise max(ANTI, SAME)
0.223234, a gain of 1.966e-3, equal to their closed form 1.96602e-3 and their Monte Carlo 1.9703e-3 +- 1.2e-5. SAME wins on
g1 in [-5.89, -2.01] in this script's coordinates (step-1 means -2 | -1); these are theirs shifted by one (I_ANTI = 0.0635779652 at
g1 = -2.5 here and at -3/2 in cert_t2_arb.txt, I_SAME 0.0641560879 at both), so their certified interval [-1.6, -1.1] sits inside.
At g1 = -2.5 the best of the 81-point step-2 grid is SAME itself. The reverse divergence by dblquad, 0.204978, is 1.3e-4 below the
grid value 0.205107 and their 0.20510; scipy flagged roundoff there, and the grid value stands. Verdict unchanged: CONFIRMED.
