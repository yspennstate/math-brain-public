---
name: p0434_large_class_excess_steps_at_r_star_1_plus_1_over_sqrt_w1_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 10:0x: large-class eps is a step at the M-SERPT rank crossing r* = 1 + 1/sqrt(w1) (1+sqrt2 at equal work); 1e-4 below, up to 0.22 just above"
metadata:
  node_type: memory
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T10:02:21-05:00
  status: provisional
  evidence: codex_fleet/runs/own_p0434/eps_step.out
  modified: 2026-11-08T15:06:20.261Z
---

On a tie law with two large atoms K1 < K2 = r K1 holding work shares w1 and 1 - w1, the large-class excess eps = (D_large + Q_G large)/R_G large, the large classes' T_MS - T_G over their R_G, is not a smooth function of how close the sizes are. It is a step at the M-SERPT rank crossing r* = 1 + 1/sqrt(w1): below it M-SERPT holds the K2 job at the running max and eps is 1e-4 to 4e-4; above it the K2 piece takes its own rank K2 - K1 and eps jumps to 0.03-0.16 at rho 0.9 and 0.11-0.22 at rho 0.98, largest at w1 0.5-0.7, then decays roughly like 1/r (3e-4 by r 1000).

Measured (eps_step.out, a 0.45, K1 1e3): crossings 3.23445, 2.41301, 2.19413, 2.05307, 2.01434 at w1 0.2/0.5/0.7/0.9/0.97 against the formula 3.23607 (1+sqrt5), 2.41421 (1+sqrt2), 2.19523, 2.05409, 2.01535; the 1e-3 offset is the previous small atom over K1. Derivation: q1/q2 = r t with t = w1/(1-w1); the crossing (r-1)(rt+1) = r(t+1) is t r^2 - 2 t r - 1 = 0.

Why it matters: the charge for P0434's T_MS <= 2 Q_G + (1+beta) R_G needs eps bounded, and an earlier read that eps is small "for far-apart sizes" was a regime artefact; the bad region is a band just past r*. Same mechanism as [[p0434_mserpt_jump_is_the_twin_rank_crossing_its_held_max_2026_11_08]] for the small classes. Files: ~/codex_fleet/runs/own_p0434/eps_close/eps_fine/eps_jump*/eps_step .py/.out, NOTE.md 09:5x and 10:0x. Related: [[p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_035_2026_11_08]].

Update 10:0x (eps_peak.out, eps_peak2.out): just past r* eps rises with rho and levels off; the heavy-traffic maximiser moves to w1 -> 1 (r* -> 2). Largest seen 0.2493 (rho 0.99999, w1 0.95-0.98); nothing above 1/4, so the working conjecture is eps < 1/4 on two large atoms.

Update 10:1x (eps_three.out, eps_three_check.out): the 1/4 does not extend. Three large atoms (1000, 1242.2, 9694.1; work 0.9827/0.0095/0.0078) give eps 17 at rho 0.999 and 22 at 0.9999, while beta stays very negative (-24, -150) and T_MS/T_G is 1.357 at most. The excess is 0.36 of the large classes' Q_G, so a proof must charge it to waiting, not residence.
