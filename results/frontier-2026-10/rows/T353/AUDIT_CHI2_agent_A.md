# Audit of the T353 chi-square claim (agent B, rows/T353/agent_B/cert_chi2_arb.py)

Auditor agent A, 19 Oct 2026 22:0x. Verdict: CONFIRMED.

Claim. At T = 2, sigma = 1, the Renyi-2 (chi-square) form of Conj 3.2 fails: an adaptive query beats the conjectured
worst-case pair. chi2(P||Q) for the pair is 1.589482; the adaptive choice (SAME on a window of g1, ANTI elsewhere) gives
1.591212, and the Arb certificate proves J_SAME - J_ANTI > 0 on cert g1 in [-2, -1.98] (200 balls, smallest lower end
0.0015912), so the gain is at least 3.22387e-5.

Independent check (chi2_indep.py, chi2_indep.txt here). The model was rebuilt from REFUTATION_T2.md, not copied from the
peer's script: shifted coordinates g1 + 1, g2 - 1; ANTI p = wa N(-1) + wc N(1) against q = w0 N(-1) + wc N(0), SAME
p = (wa + wc) N(-1) against q = w0 N(-1) + wc N(-2), weights N(g1; -1, 0, 1)/2. Plain grids (z 6001 points, g1 601,
2-D 1301), no Arb.

| quantity | peer | independent |
|---|---|---|
| J_SAME - J_ANTI at cert g1 = -2.00 | 1.804115767e-3 | 1.8041157671e-3 |
| same at -1.99, -1.98 | (balls, lower ends >= 0.00159) | 1.8240833365e-3, 1.8434403315e-3 |
| chi2(P||Q), conjectured pair | 1.589482 | 1.589482 |
| chi2(Q||P), conjectured pair | 1.212644 | 1.212644 |
| best adaptive chi2 | 1.591212 | 1.591211 |
| SAME window, cert g1 | (-12, -1.45) | upper end -1.45; lower end hits my grid edge at -8 |

The sixth-decimal difference in the adaptive total is grid error on the switching window; the certificate does not use
it. The upper end of the SAME window agrees to the grid step. P||Q is the larger direction, so it is the one that counts.

Structural checks on cert_chi2_arb.py: the reduction chi2 = integral of J dg1 - 1 with J depending only on the step-2
answer at that g1; IS and Ik monotone in r (positive numerator, denominator increasing), so the prefactor bounds are
products of positive upper bounds; TAIL = 2 phi(L - 2) bounds the mass outside [-16, 16] for mu in [-1, 2] because
Phi(-x) <= phi(x) for x >= 1; the integrand tails N(1)^2/N(0) = e N(2), <= N(-1), <= N(1) are right; acb.integral sees
only exp and division, so a vanishing denominator would give a non-finite ball, not a false bound; the ball lower ends
(0.00159) sit under the point values (0.0018), as a conservative enclosure should.

Not rechecked: whether the chi2 failure transfers to other Renyi orders, and the step-1 reduction from the full
shuffle model to the two-query game, which this audit takes from REFUTATION_T2.md as already audited.
