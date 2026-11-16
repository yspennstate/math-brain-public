---
name: a_finite_load_search_skipped_the_k_range_where_the_bound_fails_2026_11_08
description: "[VERIFIED] P0434 8 Nov: 3975 laws at K = 1.5, 3, 10, 100 found nothing above 2u/(1+u); the bound fails only for K in (2, 2.2432), a range the grid never sampled"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:22:37-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT vs Gittins, sizes in [1, K]). Route item 16 checked R <= 2u/(1+u) at every load on 3975 laws and reported none above. Its K values were 1.5, 3, 10 and 100. An exact closed-form O(t) slope on the extremal family, -u^2 (u^3+u^2-u-3)/(u+1)^2, turned positive below K = 2.85 and pointed at the gap. There the two-atom law {1, K}, mass (K-2)/(K-1) at K, load about 0.8, beats the bound for every K in (2, 2.243174), by up to 1.46e-2 at K = 2.1 (exact rational arithmetic agrees). The lesson: a parameter grid is a sample of the parameter too. Before calling a bound unbroken, look where a closed form or a sign change says the boundary is (here K = 2, where the bound crosses 1) and sample densely next to it. Files: route_agent.md item 21, twoatom_agent.*, crossK_agent.*. Same family as [[a_bounded_read_makes_whole_fields_look_truncated_2026_08_22]] and [[negative_search_does_not_establish_absence_2026_09_09]]; context [[p0434_heavy_traffic_reduces_to_a_staircase_hull_inequality_2026_11_08]].
