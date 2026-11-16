---
name: p0434_joint_target_t_ms_le_2_q_g_plus_mean_fails_kappa_2_26_on_dfr_2026_11_09
description: "[VERIFIED] P0434 9 Nov 05:4x: T_MS <= 2(Q_G+E[X]) is FALSE - kappa 2.263 on a DFR law (dust + rare heavy Exp tail, rho 0.95), two independent integrations; proofs need a Gittins residence bound beyond E[X]"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:40:45-05:00
  status: verified
  evidence: "~/codex_fleet/runs/own_p0434/kappa_three_phase_check.out"
---

P0434 (M-SERPT vs Gittins, Scully et al. Conj. 8.1), 9 Nov 05:4x, an agent, workstation yitz8.

The joint target T_MS <= 2 (Q_G + E[X]) is FALSE. On a DFR law (M-SERPT = Gittins = FB, so T_MS/T_G = 1) the ratio
kappa = T_MS/(Q_G + E[X]) reaches 2.263: dust carrying load share 0.6715, plus a big part 0.999 Exp(mean 0.729) +
0.001 Exp(mean 272), load 0.9516. Per unit E[X]: Q_G 1.438, R 4.079, T 5.517.

Measured two ways: (1) dust closed form, kappa_dust3b.py, Nelder-Mead over 24 starts, 30k and 300k log trapezoid and
quad all 2.26299; (2) kappa_three_phase_check.py, dust replaced by a real exponential phase of rate D, FB integrals on
the whole three-phase law: D 100 2.235, 1e3 2.260, 1e4 2.2627, 1e5 2.2630 (quad within 3e-4).

Consequence: no proof of ratio <= 2 can use only T_G >= Q_G + E[X] (Prop 4.9's R_G >= E[X]); here R_G = 4.08 E[X].
A proof needs a residence lower bound for Gittins that grows with the load on heavy tails.

Corrections: an earlier "kappa <= 1.61" was a few-atom-grid artefact; dust + Exp(1) alone peaks at 1.9878 (rho 0.9).
kappa_dust3.py's 5.22 was a quad failure on a degenerate law (trapezoid 1.44). Lesson: sups of these ratios sit on
many-atom heavy-tailed DFR shapes, and every optimiser best must be rechecked with a second integrator.

Files: ~/codex_fleet/runs/own_p0434/NOTE.md (05:4x section), kappa_dust3b.py/.out, kappa_three_phase_check.py/.out.
Related: [[p0434_residence_lemma_r_fails_on_hyperexponential_dfr_laws_2026_11_09]],
[[p0434_mserpt_residence_over_mean_passes_two_on_near_exponential_laws_2026_11_09]],
[[p0434_mixing_both_gittins_lower_bounds_beats_thm_5_1_at_every_load_2026_11_09]].

