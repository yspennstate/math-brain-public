---
name: t285_committee_amp_specializes_at_3p27_k_squared_2026_11_01
description: [PROVISIONAL] T285: sign committee AMP non-specialized fixed point loses stability at alpha = K^2/0.3058 = 3.27 K^2 (formal large K, MC-checked to K = 129)
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T21:57:49+04:00
  status: provisional
  evidence: ""
---



T285 target 1, 1 Nov. 1806.05451 (Aubin et al.) proved the non-specialized committee AMP fixed point stable for alpha = o(K^2) and left the Theta(K^2) term (I_C^(1)) "for future work". By S_K symmetry the specialization eigenvalue is alpha E[c^2]. Here c is the scalar with Cov(z_perp | Y, s) - I = c P_perp. One per-unit third cumulant, between the energy z^2 - 1 and the vote, sets c at order 1/K. The closed form is alpha_lin = K^2/J, with J = E_s[beta^2 s^2 phi(beta s)^2/(Phi(beta s) Phi(-beta s))] = 0.3058 and beta = sqrt(2/(pi-2)). That gives 3.27 K^2, against the IT threshold of 7.65 K.

Monte Carlo at q_a = 1 with five seeds gives (K-1)^2 E[c^2] = 0.285, 0.301, 0.306, 0.302, 0.310 at K = 5, 17, 33, 65, 129. The level of rigor is the paper's own: formal limits, no uniform-in-K control.

Lesson: the first one-seed run had K = 17 at 0.38. That came from estimating A with R*1{Y} instead of R*(1{Y} - p), which has a much larger variance. Seeds exposed it before anything was written.

Pushed: research-repo research_pushes/2026-11-01-loop-T285-stability-threshold (8fceb9f); card claim_76631185f13647b4b9b7ee8a260e62a3 (3 links); frontier move on T285.

Related: [[t284_ogp_chain_and_estimator_stability_meet_at_log_n_2026_11_01]] and [[t283_reed_solomon_counterexample_never_polytime_2e_ln_log_q_floor_2026_11_01]] are the same night's computational-gap rows. [[t299_binary_perceptron_alpha_it_1p2447_and_overlap_barrier_2026_10_31]] is the same statistical-physics family.
