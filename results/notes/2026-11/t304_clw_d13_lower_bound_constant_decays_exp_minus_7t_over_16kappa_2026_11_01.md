---
name: t304_clw_d13_lower_bound_constant_decays_exp_minus_7t_over_16kappa_2026_11_01
description: [PROVISIONAL] T304 sampling query complexity: Cao-Lu-Wang 2003.09906 prove Theta(sqrt(d) N^-3/2) strong error for underdamped Langevin on bounded-kappa strongly convex U (randomized midpoint optimal), but the proved C_low(T) <= exp(-7T/(16 kappa)) x T-free factors, so the d^(1/3) is a d^(1/3) only at T = O(kappa)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T04:44:46+04:00
  status: provisional
  evidence: ""
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

Row T304, moves 25b67f76, 998b7f03, 314b8ee4 (1 Nov). Read from the paper's LaTeX source (arxiv e-print), not the PDF: the PDF text extraction garbles eq. 3.5. Family F(d, l, L) = {l I <= Hess U <= L I}, so kappa = L/l is bounded. The oracle gives grad U plus W_t and its weighted integral. Theorem 1.1: C_low sqrt(d) N^(-3/2) <= inf worst-case L2 strong error at time T <= C_up sqrt(d) N^(-3/2), for N >= N_0 independent of d. Eq. 3.5 has Cbar = exp((3Cx/(2Cv) - T)(1 - sqrt(1 - u_R/L))) x ...; Lemma 2.2 forces T >= 12 Cx/Cv, so the exponent is <= -7T/(16 kappa). This bounds the constant the proof delivers, not the true complexity. Two gaps to a sampling lower bound: (a) the error is strong error against the same-W path; (b) at T = a kappa log(sqrt d/eps) the proved bound is at best (sqrt d/eps)^((2/3)(1 - 7a/16)). Repair idea: a perturbation estimate localised near the terminal time. Method note: on this Mac there is no pdftotext; fetch https://arxiv.org/e-print/<id> (gzip tar of the LaTeX) for exact formulas. Related: [[t360_robust_overfitting_in_isotropic_linear_model_2026_11_01]] (same PDF-extraction route).

Update 2026-11-01 04:47: move 2f55dcb9 (sketch). The exp(-T) is an artefact of the event, not the method. Require the +-Cx crossing (and |V| <= Cv) only in a final window [T - tau, T]. By superposition the separation is Phi(T, T - tau) Delta(T - tau), whose X part stays <= 0 by the trapping lemma with g = 0, plus the window source term, which is <= -Cbar(tau) mu(I). So C_low is uniform in T >= tau, and N = Omega(d^(1/3) eps^(-2/3)) holds for path simulation at any horizon. Simulated windowed event probability, 1D quadratic, Cv 8: 0.54, 0.60, 0.60, 0.60 at T 10, 20, 40, 80. Gap (a), strong error rather than W2 to the target, remains.
