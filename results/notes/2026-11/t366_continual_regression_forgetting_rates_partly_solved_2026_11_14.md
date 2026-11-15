---
name: t366_continual_regression_forgetting_rates_partly_solved_2026_11_14
description: "[PROVISIONAL] T366 forgetting under random task orderings (Evron et al. 2022): partly solved - dimension-free k^-1/4 (2504.04579), 1/sqrt(k) via SGD last iterate (2507.11274), 1/k with increasing regularization (2506.06501); lower bound Omega(1/k); unregularized 1/k open"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T13:53:17+02:00
  status: provisional
  evidence: ""
---

T366 (top-200 DL list, rows_28.py) checked 14 Nov against arXiv abstracts only. Evron, Levinstein, Schliserman, Sherman, Koren, Soudry, Srebro arXiv:2504.04579: fitting a task = one SGD step on a modified objective; dimension-free forgetting O(min(k^-1/4, sqrt(d-r)/k, sqrt(T r)/k)) with replacement, O(T^-1/4) without. Levinstein et al. arXiv:2506.06501: lower bound Omega(1/k); O(log k/k) at fixed l2 strength, O(1/k) with increasing regularization. Attia, Schliserman, Sherman, Koren arXiv:2507.11274: last-iterate SGD on smooth convex interpolation, O(1/sqrt T) at step 1/beta, stated to improve Evron's T^-1/4 in realizable linear regression (transfer to forgetting under exact projection: to verify). Open: does unregularized fitting attain 1/k? Row and STATUS_1114 updated in push 234 (commit 1b027d17). Also T362 (2609.04578, 2611.07406 RR rates) and T368 (2406.08654 large-step two-layer nets) rows updated.
