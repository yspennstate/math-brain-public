---
name: t311_svgd_kl_decay_set_by_tails_not_mode_profile_2026_11_01
description: [PROVISIONAL] T311 SVGD Gaussian RBF d=1: KL decay from N(0,s2) set by tails, linear slope -(2/s2-1), nonlinear about -1 whatever s2; dossier alpha law does not fit Hermite-geometric laws
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T12:37:24+04:00
  status: provisional
  evidence: "t311/eigen_prereg.txt, lag3.txt; move m311a 912db7d0"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T311 (mean-field SVGD, pi = N(0,1), Gaussian RBF kernel bandwidth h), Target 1, 1 Nov 2026, an agent. Row folder
06_math_research/frontier/rows/T311, move m311a.

- Exact identity: with mu = pi(1+f) the Stein velocity is v = -T(f') (linear in f, no remainder), so the flow is
  df/dt = -D*((1+f) T D f), quadratic.
- Hermite-of-f Galerkin is the wrong tool for natural laws: a Hermite-geometric profile sum rho^(k/2) h_k grows like exp(gamma x^2)
  (Mehler); truncated at 60 modes it is ~1e33 at the outer nodes and the quadratic term swamps the linear one (svgd_galerkin.py).
- What works: Lagrangian map X(z,t) on Gauss-Hermite nodes, evolve log X' (not X' from an expansion: h_n(z) ~ 1e21 at outer nodes
  amplifies rounding), KL exact from the map (svgd_lagrange.py / svgd_lagrange2.py). G 80 = 120 = 240 to 6 digits.
- Linear decay from N(0,s2) (chi2 profile geometric in HERMITE modes, rho = |s2-1|): slope -(2/s2-1) - 1/(2 log t) for 1<s2<2, ~ -1
  for s2<1; three pre-registered bands met (1e5->1e6: s2 1.7 -0.211, 1.2 -0.699, 0.8 -1.093). h-free. The dossier's alpha =
  log(1/rho)/log(1/B) assumed a profile geometric in the EIGENBASIS, which a Hermite-geometric law is not.
- Heuristic behind it (smooth laws only): T g ~ h sqrt(2 pi) pi g, so far out the flow is a degenerate diffusion with diffusivity
  ~ h pi (linear) or ~ h mu (nonlinear); frozen until pi t ~ 1 (mu_0 t ~ 1). Level test: one constant per h holds chi2_lin within
  1.04-1.17x over 4 decades for s2 1.382/1.7 at h 1, drifts 2.7x for s2<1. It does NOT describe the eigenmodes: their centre
  x_k ~ 0.86 sqrt(k) at h 1 with lambda_k far below pi(x_k) (mode_location.py) - they mix frequency and position.
- Nonlinear (svgd_lagrange3.py, lag3.txt, G 80, KL in the positive form): h 1 slopes 1e4->1e5 -0.986 -0.964 -0.948 -0.938 -0.925
  -0.912 -0.896 for s2 0.618 .. 1.7, i.e. KL ~ 1/t up to logs whatever s2, against linear -1.09 .. -0.20; 4 pre-registered bands met
  (s2 0.8, 1.2, 1.382, 1.7). h 0.5 alike (-0.99, -0.94). h 2 decays in steps (half-decade slopes -0.49..-1.54), unresolved at G 80.
  Move m311a, moves.jsonl 912db7d0. A first pass faked a late steepening: [[lagrangian_kl_offset_from_early_steps_faked_late_steepening_2026_11_01]].
- Numerics scars: h 2 linear sums are not resolved in double (19 eigenvalues above 1e-13); late RK4 step may grow to 0.5/lambda_1 (same 6 digits as 0.2/lambda_1); the
  EARLY step must be small (0.05).

