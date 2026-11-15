---
name: p0434_ratio_jumps_at_an_mserpt_rank_tie_so_item_42_is_not_the_max_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 07:5x: M-SERPT/Gittins ratio is discontinuous where the rank on [1,1+d) meets the band-0 rank; item 42 sits on the strict side; edge sup (d->0) gives 1.05807 at K=9/4 and beats S2 by 4.2e-4 at K=2.2 (exact solver only)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:58:04-05:00
  status: provisional
  evidence: ""
---

On {1, 1+d, K} the M-SERPT rank on [1,1+d) is max(rank on [0,1), SERPT(1)). If SERPT(1) is above by any margin, new arrivals preempt age-1 jobs; if below, the bands tie and FCFS keeps the old job. The ratio jumps about 0.028 across that edge at K=9/4. Item 42 (637c11d8) is on the strict side (ranks 1.086251 vs 1.086282), not a local max: shrinking d raises it to 1.0580678. Hill climb at the edge (d=1e-12, P(m)=w* by bisection) vs the two-atom climb: K=2.2 1.0517616 vs 1.0513448; K=9/4 1.0580723 vs 1.0547380 (exact S2 1.0547504, so climber error ~1e-5). So max(S2, 2u/(1+u)) fails at K=2.2 too. K=2.1 unresolved (5e-5, grid level); K=2.5 and 3 below 2u/(1+u) on a coarse grid. Not simulated. Lesson: a smooth sweep over P(m) steps over the jump; sample at rank ties on purpose. Files: brain-repo 06_math_research/frontier/P0434/audit_agent_2026_11_08/AUDIT_EDGE.md, commit 31af6a10. Links [[p0434_item42_soap_ratio_confirmed_by_own_solver_and_sim_2026_11_08]] [[p0434_s2_is_a_first_order_local_max_against_a_third_atom_2026_11_08]] [[a_finite_load_search_skipped_the_k_range_where_the_bound_fails_2026_11_08]]

8 Nov 08:2x update: 637c11d8 route item 47 (commit 31070528) found the same family and a closed-form crossing K* = 2.175833; my independent climb matches its gaps (+4.07e-4 at 2.2, +1.48e-4 at 2.19, +1.45e-5 at 2.18, 0 at 2.175) to about 1e-6 (main 09744108). See [[p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08]].
