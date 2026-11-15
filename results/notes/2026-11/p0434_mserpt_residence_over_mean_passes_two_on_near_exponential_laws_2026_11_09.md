---
name: p0434_mserpt_residence_over_mean_passes_two_on_near_exponential_laws_2026_11_09
description: "[VERIFIED] P0434 9 Nov 04:5x: closed form for M-SERPT residence matches soap; R_MS<=2E[X] is FALSE at rho 0.65 (DFR near-exponential laws give -Li2(-rho/(1-rho))/rho = 2.088; 2000-atom law 2.078); (R) with Q_G survives (z -0.014); few-atom sups were artefacts"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T04:52:22-05:00
  status: verified
  evidence: "codex_fleet/runs/own_p0434/resid_formula.out resid_dfr.out resid_fast.out resid_dfr_z.out"
---

P0434 (M-SERPT vs Gittins, Scully et al. Conj. 8.1), 9 Nov 04:5x EST, an agent, ~/codex_fleet/runs/own_p0434.

Closed form for M-SERPT residence on a discrete law (s_0 = 0): R_MS = sum_k p_k s_k / (1 - lambda m(theta_k)), m(t) =
E[min(X,t)], theta_k = s_{j-1} for the first j <= k maximising E[X | X >= s_j] - s_{j-1}. It equals soap's split_T value
to 6 digits on 9 random laws (resid_formula.out) and exactly on 120-atom DFR laws (resid_dfr.out).

The target "R_MS <= 2 E[X] for rho <= 0.65" is FALSE. On decreasing-failure-rate laws M-SERPT serves like FB and the
exponential limit gives R_MS/E[X] = -Li2(-rho/(1-rho))/rho (pi^2/6 at 0.5, 2.0879 at 0.65, 2.962 at 0.8). A 2000-atom
hyperexponential 0.5 Exp(1)+0.5 Exp(1.05) gives 2.078 at rho 0.65. The weaker (R) R_MS <= (2-c)Q_G + 2E[X] holds there
(z = -0.0135 at 150 atoms) because Q_G is large on those laws too.

Scar: the earlier sups (1.617 at rho 0.65, "R_MS < 2E[X] on every law up to 0.65") came from 3-4 atom searches; the
closed-form search shows the sup rising with atom count at every load (rho 0.65: 1.43 at 2 atoms, 1.74 at 7). The 1.617
was also a rank-tie limit (rounded p gives 1.0026). Residence sups need many atoms or a continuous DFR family.

How to apply: do not try to prove a residence lemma free of Q_G past rho ~0.63; charge the FB-like residence excess to
Gittins waiting instead. Corrects the 03:2x-04:1x addenda of [[p0434_mixing_both_gittins_lower_bounds_beats_thm_5_1_at_every_load_2026_11_09]].

