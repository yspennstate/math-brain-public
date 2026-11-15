---
name: t419_converged_lora_is_rrr_exactly_gap_opens_below_bbp_threshold_2026_11_01
description: T419: converged LoRA GD = reduced-rank regression exactly; RRR risk / dof 1.04-1.30 above the BBP threshold (d_in d_out)^(1/4) sigma/sqrt(n), up to 1.62 below; oracle early stop wins only below it
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T18:49:29+04:00
  status: provisional
  evidence: "frontier T419 moves fab6b3de, files 906cb4db (lora_rrr.py, run_sv321.txt, run_sv32p3.txt)"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T419 Target 2 (LoRA vs reduced-rank regression at finite n), 1 Nov 2026, an agent, move m419b.
The LoRA loss in M = BA is unweighted rank-r approximation in M S^(1/2) (S = X^T X/n), so GD from B = 0 converges to RRR exactly:
measured |LoRA - RRR|/|RRR| ~ 1e-15 (d_in 40, d_out 30, r 3, 40 reps). The finite-n question is then RRR's own risk. Over
r(d_in + d_out - r) sigma^2/n it is 1.30/1.12/1.04 at n 200/400/1600 when every sigma_i(Delta) clears the rectangular BBP threshold
(d_in d_out)^(1/4) sigma/sqrt(n), and 1.62/1.45/1.12 when sigma_r = 0.3 sits below, at and above that threshold (0.42/0.29/0.15). Early
stopping with an oracle stop cuts risk up to 46 pct below threshold and only 1-8 pct above it. The sample condition is sigma_r above
the threshold, not a kappa^2 factor. PREREG32 PASS 3/3; the threshold reading is post hoc.
Practical: when a "does the method beat the estimator" question has an exact-optimum reduction, check it first; here it turned a
constant-factor theorem into equality and moved the work to the estimator's own risk.


Related: [[t419_lora_gd_rate_is_sqrt_q2_plus_4sigma2_minus_q_over_2_2026_10_31]] - Target 1's population rates; the incremental fitting there is why early stopping drops the weak direction last.

CORRECTION (1 Nov, m419c): the "46 pct" is against rank-r RRR. Rank-2 RRR, or RRR with its rank picked on an n/2 validation set,
gets the same below threshold. Against rank-selected RRR, LoRA with a validation stop wins 8-9 pct near threshold (sigma_r ~ 2 theta_c)
by shrinking the weak direction; elsewhere the two tie (ratios 0.915-0.993, never worse). The validation stop is within 0.6-3.4 pct of
the oracle stop. PREREG33 PASS 3/3; its clause (c) passed only as a tie (0.985).

ADDENDUM (1 Nov, m419d): the gain of validation-stopped LoRA over validation-ranked RRR is a window in sigma_r/theta_c of about 1.3 to 4,
peaking at 9.7 pct near 2 theta_c (n 400), where RRR's validated rank flips from r - 1 to r. Outside the window it is under 1 pct.
Early stopping is soft shrinkage against RRR's hard rank threshold. PREREG34 PASS 4/4.
