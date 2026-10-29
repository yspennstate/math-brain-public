# T354 iid remainder lemma (agent_B/remainder_iid.py, NOTE "Rigorous remainder, iid sampling"), audit 3 (agent C, 20 Oct 2026 03:2x)

Independent of the two audits by agent A. Verdict: CONFIRMED. One scope remark: the bracket is proved for zeros in
[0, 3 x0], which is what the script scans; the NOTE's "every zero" should say so (the exact routes find one zero, at about x0).

## Line by line
- v_k = V + d sum_j beta2^j Z_{k-j} because d sum_j beta2^j = 1; so v = V t_i + d beta2^i Z_{k-i} with t_i a function of the
  other lags only, independent of g_{k-i}, E t_i = 1, Var t_i = d^2 Var Z sum_{j != i} beta2^(2j) / V^2 <= d Var(g^2)/((1+beta2) V^2).
- t_i >= m/V: V t_i = d sum_{j != i} beta2^j g^2 + d beta2^i V >= m (1 - d beta2^i) + d beta2^i V >= m, since V >= m.
- Lag-i term: E[g phi(t + h)] = f' E phi(t) + (d beta2^i C/V) E phi'(t) + E[g R2], using E g = f' and E[g Z] = E g^3 - V E g = C.
  The weights (1-b1) b1^i (b2)^i sum to K, so the middle terms give -(d K C/(2V)) P1 with P1 = -2 sum w_i E phi'(t_i), sum w_i = 1.
- R: h >= -d beta2^i (V - m)/V >= -d, phi'' = (3/4) y^(-5/2) decreasing, so |R2| <= (1/2) phi''(t - d) h^2; with independence and
  sum (1-b1) b1^i beta2^(2i) = (1-b1)/(1-b1 beta2^2) the stated |R| bound follows.
- Jensen: phi convex gives P0 >= 1; phi''' = -(15/8) y^(-7/2) < 0, so phi' is concave and P1 >= 1.
- Divided differences q(t) = int_0^1 (1-s) psi''(1 + s(t-1)) ds: psi'' is decreasing and positive for phi and t^(-5/2), negative
  and increasing for phi', so |q| decreases in t in all three; splitting at t0 with (t-1)^2 <= (1-rho)^2 below t0 gives the
  three bounds in the code (q0, q1, e52). E (t-d)^(-5/2) <= (1 - d/t0)^(-5/2) E t^(-5/2) + (rho - d)^(-5/2) P(t < t0): correct.
- Bernstein: t - 1 is a sum of independent centred terms bounded below by -d(V - m)/V, so the lower tail at 1 - t0 is
  exp(-(1-t0)^2 / (2(s2 + d(V-m)/V (1-t0)/3))), as coded (the V^2 factors in the comment cancel).
- F_lo = x - lead(1 + 2|q1|) - R and F_hi = x(1 + q0) - lead + R bracket sqrt(V) D for x >= 0 and C > 0; bisection plus the
  4000-point scan locate every sign change in [0, 3 x0].

## Exact values against the enclosures (iid_enclosure_check.py, iid_enclosure_check.txt)
Exact x*/x0 by my cumulant route (no Laplace kernel; eps_moment_route.D): 1.000100, 1.000998, 1.004953, 1.00967 (beta2 0.9999,
0.999, 0.995, 0.99 at beta1 0), 1.001037, 1.01322 (beta1 0.9 at 0.999, 0.99), 1.001352, 1.02385 (beta1 0.99). All inside. At
d <= 0.005 they equal A's Laplace values to six digits. At beta2 0.99 my route converges slowly in the Taylor order
(J 14 to 20 moves 1.6e-5; it sits 1.2e-4 below the Laplace value 1.009790), because y reaches 0.11, near the series' radius;
that is far inside enclosures of width 0.8 and does not affect the verdict.
