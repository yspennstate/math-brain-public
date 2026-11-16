---
name: p0245_n5_per_node_lemma_fails_on_a_path_bound_holds_in_search_2026_11_10
description: "[PROVISIONAL] P0245 holding walk: does the per-node lemma L_s >= c_s/2 carry it? n=4 yes (proved); n=5 no, fails on a weighted path, yet a 60-restart search finds nothing below (n-1)H_{n-1}"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T10:20:41+02:00
  status: provisional
  evidence: ""
---

P0245 (Aldous-Fill OP 6.30, holding walk: is E_pi C >= (n-1) H_{n-1} for every reversible chain with holds?), checked by an agent on 10 Nov 2026.

- n = 4: the per-node holding lemma L_s >= c_s/2 is proved for every weighted graph (exact rational certificates in sympy, n4_fast.py), and the K4 certificate matches a Monte Carlo of the walk (24 values, max gap 0.04).
- n = 5: the per-node lemma is FALSE. On the weighted path 0-1-2-3-4 (weights 1, a, b, c) the end node has L_0/c_0 -> 4a/b + 4/b + 4/a - 1/3 as c -> infinity, negative for a > 12 and b >> a; float check at weights 1, 100, 1e5, 1e8 gives L_0/c_0 = -0.285. So the node-by-node route to P0245 cannot work at n = 5.
- The inequality itself survives: on that path family E_pi C - B is 2e6 to 2e8 and a hold removes at most 17 pct; a 60-restart Nelder-Mead search over all ten K5 conductances plus five holds (exact E_pi C on position x visited-set states) finds minimum (E_pi C - B)/B = 0 at uniform K5 and nothing below. Evidence, not proof.

Files and write-up: the private repository, 12_cognitive_architecture/codex_local_1108/briefs/OPEN3/independent_check_agent/HOLDING_REDUCTION.md (commits 79a6db76, 860e8026, d9be49e9, 44e23b28, 8d39eee0).
What would change it: a five-node chain with holds below 25/3, or a proof that sums the L_s with weights (pi_s) instead of node by node.

Related: [[p0245_four_state_stationary_cover_time_bound_certified_2026_11_10]] [[p0245_n3_proved_holding_only_raises_cover_time_2026_11_10]]
