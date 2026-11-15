---
name: p0434_srpt_plus_waiting_lower_bound_max_still_loses_2_07_on_dfr_2026_11_09
description: "[VERIFIED] P0434 9 Nov 06:0x: T_MS/max(Q_G+E[X], T_SRPT) = 2.071 on a DFR law (true ratio 1); universal Gittins lower bounds lose >2x - prove policy against policy"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T06:02:40-05:00
  status: verified
  evidence: "~/codex_fleet/runs/own_p0434/maxbound_best_check.out"
---

P0434 (M-SERPT vs Gittins), 9 Nov 06:0x, an agent. Even the mixed lower bound T_G >= max(Q_G + E[X], T_SRPT) is
too weak for ratio 2: on a DFR law (M-SERPT = Gittins = FB, true ratio 1) T_MS / max(...) = 2.071. The law has three
exponential phases, means 1 / 2.9e-4 / 3634, load shares 0.166 / 0.795 / 0.039, rho 0.9903. Checked two ways (quad with
SRPT residence by Fubini; 400k trapezoid with cumulative residence), both 2.07107. The peak sits where the two bounds cross.
SRPT is a valid bound (it is optimal over all policies) but is 5.67x below FB on exponential at rho 0.99.
Together with kappa 2.263 for Q_G + E[X] alone ([[p0434_joint_target_t_ms_le_2_q_g_plus_mean_fails_kappa_2_26_on_dfr_2026_11_09]]):
a proof must compare M-SERPT with Gittins policy against policy (rank levels), not through a universal lower bound on T_G.
See [[p0434_levels_on_a_gittins_block_wait_under_twice_by_record_telescoping_2026_11_09]],
[[p0434_each_mserpt_level_waits_no_longer_than_its_gittins_block_2026_11_08]].
Files: ~/codex_fleet/runs/own_p0434/maxbound_dfr_search.py/.out, maxbound_best_check.py/.out, srpt_bound_check.py/.out, NOTE.md 05:5x and 06:0x.

