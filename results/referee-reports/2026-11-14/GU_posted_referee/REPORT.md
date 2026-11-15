# Referee report: Conserved charges in linearly reinforced graph urns

Paper: yspennstate/graph-urn-conserved-charges at 69ce6d0 (main.tex, 419 lines). Referee: an agent, 14 Nov 2026.
Earlier review: referee_reports/2026-11-12/P0081 (Codex, before posting), which found the exact terminal law now in the paper.

## Verdict

SOUND. No change to the paper is needed. Every proof was checked step by step and every closed-form number was
recomputed independently.

## Proofs checked

- Theorem 1 (charge martingale). Jump sigma_e/n at the passage n -> n+1, conditional mean (B sigma)_v/S_v = 0,
  [M]_t = sum sigma_e^2 H2(N_e - 1) <= zeta(2) sum sigma_e^2. Correct.
- Lemma 2 (growth). D_e = H(N_e - 1) - a_e is a martingale with bracket H2 <= zeta(2); S_v <= d + sum of the clocks of
  v and its at most d neighbours, so a_e >= lambda' log t - C. Correct.
- Theorem 3 (terminal law). An increase of n_e multiplies P_theta by 1 + i theta sigma_e / n_e, so the generator is
  i theta P_theta sum_v (B sigma)_v / S_v = 0. |Gamma(x+iy)| <= Gamma(x) bounds P_theta, and
  Gamma(n+z)/(Gamma(n) n^z) -> 1 with the link identity (sum sigma_e = 0) gives the limit; dominated convergence closes
  it. Var <M>_inf = zeta(4) sum sigma^4 follows from R = [M] - <M>, [R] = sum sigma^4 H4, [M]_inf deterministic. Correct.
- Remark 4 (fibre). P is bounded (x_e <= b_v), the entropy functional has its minimiser inside P, and
  pi(log x) = pi(log W) because pi kills the range of B^T. Correct.
- Lemma 5 (equilibria on C_L). Rebuilt the block analysis: along a positive path S alternates s, s' = s/(s-1),
  x_{2i} = i d, x_{2i+1} = s - i d; odd blocks force d = 0 and k = 1, even blocks give d = 2s/k and
  s = (2k+2)/(k+2). The zero edge next to an even block has d_e L >= (k+2)/(2k+2) - 1/2 = 1/(2k+2) >= 1/(2L). Correct.
- Theorem 5 (convergence). K is forward invariant (d sum x = L - sum x; dS_v/dtau >= 1 - S_v). The Doob bound uses
  rate L, which dominates the true rate 2 of one count; Borel-Cantelli along integer tau works. Ben99 Prop 6.4 applies
  since L takes finitely many values on the equilibria. The type-(2) exclusion: on A_m the internal time grows at rate
  (1 + delta)/t, so X_e >= c t^delta, contradiction. The endpoints are excluded by Phi -> +-inf. Correct.
- Corollary 6. Gamma(1+i theta) Gamma(1-i theta) = pi theta / sinh(pi theta); E(<M>/L - pi^2/6)^2 =
  zeta(4) L / L^2 = pi^4/(90 L). Correct.
- Proposition 7 (line). The compensator of H2(N_0 - 1) and the shift E[1/(N_0 S_1)] = E[1/(N_{-1} S_0)] give
  E int dt/(N_{-1} N_0) = E H2(N_0(T) - 1) -> zeta(2). Correct.
- Section 4 heuristics. The linearised rate is (1 + cos k)/2 (checked from d_e L at x = 1); the drift identity
  dY_e = -(J_{e+1} - J_e) dt + dM_e checks. The PDE is labelled formal, as it should be.

## Numbers recomputed (agent_run/gu_check.py, gu_check.out)

- The stated C_4 density f(s) = (s coth(s/2) - 2)/(4 sinh^2(s/2)) equals the convolution of two standard logistic
  densities at s = 0, 0.5, 1, 3, 8 to 10 digits; its mass is 1 and E M^2 = 6.5797362674 = 4 pi^2/6.
- Var p = 0.0584251375 = pi^2/32 - 1/4 to 10 digits.
- The density of p over 4(1-p) log(1/(1-p)) is 0.858, 0.913, 0.938 at 1-p = 1e-3, 1e-5, 1e-7, matching the exact
  correction 1 - 1/log(1/(1-p)); the asymptotic statement on line 252 is right.
- Kurtosis 12/(5L) = (excess kurtosis 1.2 of the logistic)/(L/2); C_50 variance 50 pi^2/6 = 82.25. Both as printed.

## Simulation rerun with new seeds (code/exact_law_check.py)

- C_4, 4000 rings, 20000 runs, seed 11: Var M 6.510 (exact 6.580, s.e. 0.065), excess kurtosis 0.53 (exact 0.60),
  KS 0.0041 (5% level 0.0096), Var p 0.05833 (exact 0.05843). The paper's seed gave 6.63; the two runs average 6.57.
- C_50, 1e5 rings, 4000 runs, seed 12: Var M 79.5 (exact 82.25, s.e. 1.8), KS 0.0106 (5% level 0.0215). The paper's
  seed gave 81.9; the two average 80.7, 1.2 pooled standard errors below the exact value.
- Stopping at K rings removes E sum_e (zeta(2) - H2(N_e - 1)), about sum_e 1/N_e, from the variance: roughly 0.01 on
  C_4 and 0.03 on C_50, too small to matter. The deviations are sampling noise.
- Outputs: agent_run/gu_rerun_c4.txt, gu_rerun_c50.txt (copied here).

## Remarks (no change requested)

- The line experiment of Section 5 runs on a cycle of length 1001, which is odd, so it has no global charge and one
  frustrated site. At T = 1e5 the diffusive scale in tau = log t is a few sites, so the wrap and the defect cannot reach
  the sampled edges in any measurable way; the text describes the setup accurately.
- The funding paragraph follows the author's standing rule of 20 Sep (memory
  funding_statement_names_google_cloud_edu_credit_2026_09_20).
