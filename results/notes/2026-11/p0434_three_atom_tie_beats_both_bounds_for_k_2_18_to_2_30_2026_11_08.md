---
name: p0434_three_atom_tie_beats_both_bounds_for_k_2_18_to_2_30_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: three-atom tie law beats max(S2, 2u/(1+u)) for K about 2.185 to 2.30; a free multistart found the lower edge below the tie-constrained search's 2.2005"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:07:24-05:00
  status: provisional
  evidence: "runs/own_p0434 tie_check.out tie_check2.out"
---

P0434 (M-SERPT against Gittins), 8 Nov 2026 08:0x. The three-atom law {1, 1+d, K} with d -> 0 on the M-SERPT tie r(1) = r(0) beats max(S2, 2u/(1+u)), the best two-atom value and the heavy-traffic bound, for K from about 2.185 to about 2.30. Peak excess +2.2e-3 near K 2.25 (sup 1.05797 to 1.05807 by two searches). At K 2.17 the best law found is the two-atom one, off the tie; at 2.305 and above nothing beyond 2u/(1+u) was found (local search). So the [1,K] supremum is not max(S2, 2u/(1+u)) on that window. See [[a_finite_load_search_skipped_the_k_range_where_the_bound_fails_2026_11_08]] and [[p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08]].

How it was checked: an agent's w3tielim puts the K-mass on the tie and optimises (w, eps); it gave the window from 2.2005. My tie_check left (twin, K-mass, eps) free with m - 1 = 1e-9 and a multistart Nelder-Mead. Wherever the sup beat S2 the free optimiser landed on the tie to 1e-15 on its own, which confirms the reduction. But at K <= 2.205 the free multistart found a higher point (twin 0.0055, K-mass 0.124, eps 0.19 at K 2.2: excess +3.9e-4 where w3tielim had -3.9e-5), so the lower edge moved down to about 2.185. At 2.25, w3tielim was 1e-4 above mine. The two searches differ by up to 2e-4, so both edges are lower bounds on the window, good to about 0.01.

Lesson: a constrained search that is right about where the optimum lives (the tie) can still sit on the wrong branch inside it. Run a free multistart next to the reduced one before quoting where a counterexample window begins. Both runs use the same soap.ratio, so neither is a check of the SOAP model. The model check is 637c11d8's event simulation at 9/4 (1.05740 +- 0.00055 against 1.05805).

Evidence: ~/codex_fleet/runs/own_p0434/ tie_check.py/.out, tie_check2.py/.out, w3tielim_agent.py/.out, NOTE.md 08:0x; research-repo codex-fleet ad0265c7.

