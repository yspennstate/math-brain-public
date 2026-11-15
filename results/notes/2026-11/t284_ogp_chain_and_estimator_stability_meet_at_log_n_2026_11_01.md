---
name: t284_ogp_chain_and_estimator_stability_meet_at_log_n_2026_11_01
description: [PROVISIONAL] T284: in Li-Schramm shortest path the OGP chain reaches T = o(log n/loglog n) and the log-degree estimator is stable only for T >~ m = log n/loglog n; degree gap = stability tail
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T21:41:56+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T284 target 2, 1 Nov, from the TeX of 2411.01836 (Li-Schramm). On G(n, B log n/n) the shortest-path OGP holds per correlated pair only with probability 1 - O(log log n/log n). The no-stable-algorithm chain of T steps therefore needs T = o(log n/log log n). The polynomial that solves the problem counts m-edge paths, with m = Theta(log n/log log n). Its path survives (1 - 1/T)-correlation with probability exp(-m/T), so it is stable only for T >~ m. The two scales meet, and that is the property the estimator lacks.

For degree D the mean change is at most 2D(1 - rho), but the chain needs a tail: Markov over T steps gives 2D/gamma, which is useless. The paper's tail bound, as I read its constants, reaches D ~ log log n/log log log n, conditional on its o_n(1) term. A stability tail o(1/T) up to degree c log n/log log n would close the gap. The paper's lower bound covers only fixed D.

Pushed: research-repo research_pushes/2026-11-01-loop-T284-stability-scale (8f694c0); card claim_986fc482de8a4abba70b86dec954aef2 (2 links); frontier move on T284.

Related: [[t279_stable_minima_generalize_isotropic_wendel_floor_2026_11_01]] was the same night, and in both a stability notion only works on the scale the data allow. This row is a reading result, no numerics.
