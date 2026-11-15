---
name: p0434_large_excess_over_large_waiting_grows_with_n_past_one_half_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 10:2x: large-class excess over Gittins large waiting climbs 0.19/0.50/0.58/0.61 at n 2-5 large atoms; a 1/2 lemma fitted on 2-3 atoms fails at n 4"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T10:30:43-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/xl_climb2.out"
---

P0434, 8 Nov 10:2x (an agent). For tie laws with n large atoms, the large classes' excess XL = (T_MS - T_G)(large) over their Gittins waiting QL = Q_G(large) is not bounded by 1/2. Hill climbs over a, rho, size ratios and work shares reach 0.187 (n 2), 0.498 (n 3), 0.584 (n 4) and 0.607 (n 5). On 420 two- and three-atom cases (charge_wait) the maximum was 0.364, which made a 1/2 lemma look safe until n 4. The residence-only form had already failed: eps was up to 17 with three atoms (eps_three).

Lesson: a constant fitted on few-atom laws keeps growing with n here, the same pattern as [[p0434_record_lemma_constant_grows_with_the_number_of_large_classes_2026_11_08]]. Climb over n before writing a lemma. Open question: is sup XL/QL < 1 for every n? Files: ~/codex_fleet/runs/own_p0434/xl_climb.py, xl_climb2.py, .out; NOTE.md 10:2x. Related: [[p0434_large_class_excess_steps_at_r_star_1_plus_1_over_sqrt_w1_2026_11_08]].

Update 10:3x (xl_climb3.out): 0.618 (n 6), 0.710 (n 8), 0.857 (n 10), at rho 0.14-0.34 with geometrically spread sizes. Still rising; likely passes 1.

Update 11:4x (xl_climb4.out): the same climb gives 0.80 at n 12 (rho 0.19) and 0.75 at n 16 (rho 0.63), so the rise to 0.86 at n 10 did not continue under a fixed budget (a weaker search at higher n, not a bound). Maximisers sit at low/moderate load with beta < 0. With c2 about 0.024 ([[p0434_small_class_charge_needs_only_0_024_of_large_waiting_2026_11_08]]) c2 + c stays under 1 on all seen.
