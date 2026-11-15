---
name: t302_weight_mod_q_weak_learnable_iff_full_parity_component_2026_11_01
description: [PROVISIONAL] T302: under 2208.03113's hypercube characterization, h(weight mod q) is GD weak-learnable iff (1/q) sum (-1)^r h(r) != 0; odd q never; the paper's SGD-hard mod-8 target has parity correlation 0.447
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T17:55:28+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Exact Fourier formula f_hat_k = (1/q) sum_t H(t) c_t^(d-k) s_t^k (c,s = (1 +- omega^t)/2), brute-force checked d=10. Only the t=q/2 term survives in the window, at k=d. Paper mod-4 example a=0 (hard, their conclusion); sum x mod 8 has a=+-1. Full parity under Gaussian init is named open by the authors. Pushed 063dd1f (research_pushes/2026-11-01-loop-T302-modq), frontier move 7ff1ab96. Related: [[t289_online_sign_rules_reach_alpha_0p35_kappa2_d_1p7_2026_11_01]]
Store card claim_bf189a232eea4147b217e4c115d7d990 (3 links), export 9e09e3e.

AUDIT 1 Nov 18:4x: an agent read 2208.03113 on 31 Oct (frontier log). The mod-q corollary is not in that move and stays new. Note re-pushed a3c1da3 with credit.
