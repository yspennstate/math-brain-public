---
name: catalogue_row_already_solved_in_store_recall_first_2026_11_16
description: "[VERIFIED] Open-problem catalogue (1,128 rows): 'checked_open' meant open on the WEB only; CN0541 (Aldous-Brightwell p(m)~3e/(m!)^2) was already PS29 in our store. Recall first; 117 rows carry fleet_leads."
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T04:43:53+02:00
  status: provisional
  evidence: ""
---

16 Nov 2026. I computed CN0541 (Aldous-Brightwell Subproblem 4, chance two random 2-dim orders coincide) from scratch: p(n)=f_n/(n!)^3, f_n=sum over permutations of the number of transitive orientations of the incomparability graph; exact match to brute force n<=6; closed form F=Phi(B), x=3B-2Phi(B)+3Phi(B)^2/(1+Phi(B)) checked to n=30; n=300 -> 3e with 5/k correction. Only then did math_recall show the store already holds it as PS29 (Codex swarm, audit-holds, card claim_9f62b6be21caa43dcbac519470f083def7eec5a605be8bdcaf2fc9e81213eded), same constant. So my work is an independent confirmation, nothing new. Fix: catalogue/source_crosscheck.py matches each row's source URL/arXiv id against the swarm briefs and store cards; 117 rows now carry fleet_leads (a lead, not a status). How to apply: before computing on any catalogue row, run math_recall with the row's object words AND read its fleet_leads; TF-IDF title matching (store_crosscheck.py) missed PS29, so match on the cited source. Related: [[open_problem_catalogue_1128_probability_networks_computation_2026_11_16]]
