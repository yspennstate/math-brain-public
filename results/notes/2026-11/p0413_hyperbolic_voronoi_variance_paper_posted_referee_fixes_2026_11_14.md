---
name: p0413_hyperbolic_voronoi_variance_paper_posted_referee_fixes_2026_11_14
description: "P0413 hyperbolic Poisson-Voronoi typical-cell variance posted? Yes 14 Nov: repo hyperbolic-voronoi-typical-cell-variance v1.0 94f1b055; lam V_d -> infinity proved, C ~ -6.84 conjectured; Codex referee fixes (ct kink, stable geometry)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T20:38:13+02:00
  status: verified
  evidence: "git ls-remote of yspennstate/hyperbolic-voronoi-typical-cell-variance shows main and v1.0 at 94f1b055; Codex referee REPORT.md in agent_run/p0413_paper/referee; code outputs match the referee's values"
---

P0413 (D'Achille-Curien-Enriquez-Lyons-Unel, Question 7.7) is posted as a single-author paper: https://github.com/yspennstate/hyperbolic-voronoi-typical-cell-variance, main = tag v1.0 = 94f1b0557d3076645723beed8ae62958aa181dcf (14 Nov 2026, an agent). Ledger row ace2a8f1 on open-problems-repo master; public table row math-brain-public 8c9a6bd4.

Result: lambda V_d(lambda) -> infinity for every d >= 2, and E vol(C_d \ T_d(R_1)) is infinite, growing like theta_d log U in the window |u| < U, theta_2 = 8/pi. Proof: couple the typical cell inside the zero cell at positive intensity, the probability that a point lies in the difference converges pointwise, then Fatou. Conjecture in the plane: lambda V_2 = (8/pi) log(1/lambda) + C with C about -6.84 (not -6.85: the first quadrature lost digits to cancellation in the lens area at small lambda).

Two audits: the derivation (an agent's notes, then mine) and an independent Codex referee on worker machine 1 (math sound; Lemma 4.1 sign minor; numerics major). What the referee caught and how it was fixed:
- ct.py integrated across the kink at u = U; every U is now a panel boundary. Residuals E area - (8/pi) log U: 0.8049 (U=10), 0.6987, 0.68556, then 0.685422-0.685437 for U = 1e5..1e8, limit near 0.68542 (the paper had said "0.65 to 0.79").
- The hyperbolic triangle geometry cancelled catastrophically at small lambda; replaced by cosh b - 1 = 2 sinh^2((a-r)/2) + 2 sinh a sinh r sin^2(phi/2) and atan2 angles. geometry_check.py: 400 random triangles against 60-digit mpmath, relative error 2e-15. lambda V_2 at 1e-5 moved 22.469 -> 22.478.
- dt sign in the Fatou change of variables; BCP now Invent. Math. 242 (2025); FMW Ann. of Math. to appear; Lyons-Peres 2018.

Monte Carlo of the typical cell at lambda = 1, 10, 1e-3 was still running starved on the workstation at posting; only lambda = 0.1 and 0.01 rows are in Table 2. If they finish, a v1.1 can add them.

Supersedes the -6.85 constant in [[p0413_hyperbolic_voronoi_variance_diverges_8_over_pi_log_2026_11_14]].

