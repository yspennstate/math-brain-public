---
name: t249_ntk_crossover_double_scaling_2026_11_11
description: "T249 NTK lambda_min between critical line and ordered phase? Candidate double-scaling law: eps=1-chi_1, L=t/eps, (eps/q*)Theta -> g(t)I + ..., g(t)=e^-t(2t-3+4e^-t-e^-2t)/(1-e^-t)^2; two derivations, tanh/sin/erf numerics; depth-uniform proof written, audited once (agent), second audit owed"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T00:57:11+02:00
  status: provisional
  evidence: "06_math_research/t249_crossover_agent_2026_11_11/T249_CROSSOVER.md; check2_tanh.out; koenigs_check.out"
---

T249 (NTK smallest eigenvalue, ordered phase) - a double-scaling law that joins the critical line to the ordered phase. Candidate. Audited once (an agent, 11 Nov 2026: g(t) re-derived, their own tanh code within 0.3 pct at eps = 0.0025; PROOF_UNIFORM.md read line by line, every step holds as written; their note is 06_math_research/lean_checks_agent/t249_referee/README.md, brain main f92fbef7). A second independent audit is owed before it is claimed.

Setting: infinite-width fully connected net, inputs on the fixed-point sphere (q = q*), sb2 > 0 fixed, eps = 1 - chi_1 -> 0, depth L = t/eps with t fixed.
Claim: (eps/q*) Theta_L -> g(t) I + (1 - e^-t - g(t)) 11^T, with
  g(t) = e^-t (2t - 3 + 4e^-t - e^-2t) / (1 - e^-t)^2,
so lambda_min ~ (q*/eps) g(t) and cond = n(1-e^-t)^3 / (e^-t(2t-3+4e^-t-e^-2t)) - (n-1).
Ends: t -> 0 gives lambda_min ~ (2/3) q* L and cond -> (n+2)/2 (the critical-line value); t -> inf gives lambda_min ~ 2 q* L chi_1^L (the ordered-phase law of the posted T249 note, github.com/yspennstate/ntk-smallest-eigenvalue-ordered-phase, commit 8277f3d).
Derivation 1: delta = 1 - c obeys d delta/dl = -eps delta - (beta/2) delta^2, so beta delta/eps = 2e^-s/(1-e^-s) (the curvature beta cancels); D = Theta_diag - Theta_off = (q*/eps) g with g' = -(1+r) g + 2e^-s.
Derivation 2: the posted law kappa k L chi_1^L with Koenigs value k(delta_0) = eps delta_0/(eps + beta delta_0/2) -> 2 eps/beta and kappa ~ beta q*/eps gives kappa k -> 2 q*.
Measured (tanh, sb2 = 0.05, n = 8, six eps from 0.04 to 0.00125): at t = 1 (g = 0.30951) the bracket [lam_min, lam_(n-1)] eps/q* closes from [0.1159, 0.6056] to [0.3006, 0.3265]; cond/n minus prediction falls 1.96, 0.83, 0.354, 0.151, 0.063, 0.025 (about halving with eps). kappa k/(2q*) at delta_0 = 0.5: 0.885, 0.958, 0.989 for eps 0.02, 0.01, 0.005.
Limits of the claim: the limit is NOT uniform in the inputs - relative error is of order eps/(beta min delta_0), so pairs with 1 - c_0 ~ eps/beta sit outside it. tanh, sin and erf have been run (uniform_*.out). A depth-uniform proof with error term is written (PROOF_UNIFORM.md: D_L = 2 q* chi^L S_L/(1-chi^L)^2 (1+O(log N/N)), N = min(L,1/eps), S_L = sum_{j<=L}(1-chi^j)^2), one author, read once by an agent.
Literature read (none states the crossover): Xiao-Pennington-Schoenholz 1912.13053 (three phases treated separately), 1905.13654, Martens et al. DKS 2110.01765 Sec. 24.5-24.6 (three cases, mu = 1/3 at criticality, cond(K) under DKS left to future work), 2206.02768, 2202.00553. Also checked 11 Nov: Terjek 2501.13225 ((a,b)-ReLU exactly at the EOC, no off-critical parameter) and Roberts-Yaida-Hanin 2106.10165 (keyword search only: analysis at criticality; its double scaling is depth over width).
What would change it: a second activation (erf, sin) failing the same table; a line in 2106.10165 or 2501.13225 giving g(t); an audit finding a gap in the ODE-vs-discrete-map step.
Files: brain-repo/06_math_research/t249_crossover_agent_2026_11_11/ (T249_CROSSOVER.md, crossover_check.py/.out, crossover_check2.py, check2_tanh.out, koenigs_check.py/.out, lit/).
Method lesson: when two regimes of a posted result have separate constants, set the control parameter to c/L and look for the interpolating function before proving either end again; the second route (posted constant -> limit) is the cheap independent check.

Later, 11 Nov morning. The Theorem of PROOF_UNIFORM.md has two readers (an agent and a Codex referee, see [[codex_referee_runs_on_mac_mini_1_and_found_a_false_corollary_2026_11_11]]); the Codex referee found the Corollary false as first written (L = 1, n = 2, c_1 = 0) and Remark 2 overstated; both were restated, and the restated versions were read correct by an agent (04:32Z), who also proved the order condition T_L >= F_L for every L >= 4 and chi in (0, 1) (06_math_research/lean_checks_agent/t249_corollary/README.md). The fit sentence now says 'consistent with the logarithm', not 'visible'.

T249 (NTK smallest eigenvalue, ordered phase) - a double-scaling law that joins the critical line to the ordered phase. Candidate, not proved, not audited by a second party.
