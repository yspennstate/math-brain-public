---
name: p0434_small_class_charge_needs_only_0_024_of_large_waiting_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 11:3x: small-class excess is charged as 0.036 R_G + c2 Q_G(large) with c2 about 0.024 on climbs; the proof closes if large excess stays under 0.97 of large waiting"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:35:36-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/c2_climb.out"
---

P0434 (E[T_MS] <= 2 E[T_G], M-SERPT against Gittins), tie laws on the n-family: the small classes' excess D_small = T_MS - 2 Q_G - R_G (classes 0, 1) is charged as D_small <= 0.036 R_G + c2 Q_G(large), and short adversarial climbs (c2_climb.out, n 24, about 60 evaluations from each of two seeds) needed c2 only 0.023-0.024, at rho 0.915-0.923. The law where small D alone reaches 0.073 R_G (smallD_climb.out, rho 0.989) needs c2 0.003, because its large-class Gittins waiting is 11.8 R_G.

Why it matters: with D_large = XL - Q_G(large) and XL <= c Q_G(large), beta <= 0.036 + (c2 + c - 1) Q_G(large)/R_G, so the bound T_MS <= 2 Q_G + 1.036 R_G follows while c2 + c <= 1. The weak link is c: [[p0434_large_excess_over_large_waiting_grows_with_n_past_one_half_2026_11_08]] has it at 0.86 by n 10 and still rising. The 0.036 is the equal-family limit, [[p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_035_2026_11_08]]. Short climbs give lower estimates of the needed constants, not bounds.

Files: ~/codex_fleet/runs/own_p0434/c2_climb.py/.out, smallD_climb.py/.out, beta_limit.out, NOTE.md 11:2x-11:3x.

Update 12:0x (a_climb.out): a direct climb on the additive slack of D_small <= 0.036 R_G + 0.03 QL reached -0.0008 R_G from both seeds (small D 0.040, QL 0.16 R_G, rho 0.916, a at cap 0.4999), still rising. 0.03 is near tight; since c (XL/QL) stays <= 0.86, the plan uses 0.1 QL with lemma B at 0.9. 2000 random laws (joint_test2.out) showed no violation of either lemma.
