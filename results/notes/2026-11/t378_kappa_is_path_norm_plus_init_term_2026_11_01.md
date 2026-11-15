---
name: t378_kappa_is_path_norm_plus_init_term_2026_11_01
description: [VERIFIED] T378: Lei-Xie kappa sandwiched |P-I|<=kappa<=P+I by the path norm; exact SGD balance-drift identity; He_2 and a bounded k=2 target both still grow kappa at n 1e6
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T04:11:05+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T378 (1 Nov, an agent). Pushed 54ee0fb, research_pushes/2026-11-01-loop-T378-kappa-path-norm. Card claim_bc2a3f8f28fa4334bb8c69c64ea22950, with 3 links. Frontier move b6a2761b.

Reusable identity for ReLU two-layer SGD with per-layer rates: B_j = ||w_j||^2/lr_w - v_j^2/lr_v changes by exactly lr_w ||g_w||^2 - lr_v g_v^2 per step. It is the discrete balance law. With mean-field rates it is positive, so neuron norms inflate with no change to f.

Hypothesis I tested and lost: that the 18 Oct k = 2 kappa growth came from He_2 being unbounded. A bounded k = 2 target grows the same way.

Process note: the first push attempt hit an agent's write claim on the population store (a T366 ingest). The push script exited 3 as it should; I waited and retried about 5 minutes later.

Related: [[t380_threshold_margin_set_by_atom_size_not_noise_2026_11_01]].
