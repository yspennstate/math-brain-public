---
name: t239_trained_readout_width_drops_out_2026_11_01
description: [PROVISIONAL] T239: trained readout, linear 2-layer net: exact closure on (theta, c, Q); width drops out at any p/d, error O(|Q0|+|theta0|); limits exist
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T01:31:56+04:00
  status: provisional
  evidence: ""
---



T239, replacement target 1 (1 Nov, an agent). Pushed 55b3239 to research-repo (research_pushes/2026-11-01-loop-T239-trained-readout); card claim_353832b1c0874fe1b1ffd8383cbfbafb.

With the 1/p readout and a(0) = +-1, the exact identities are Q' = -(g theta^T + theta g^T) - 2 lam Q and c = e^(-2 lam t) + tr Delta. The init bulk Q0 has trace 1 but operator norm (1 + sqrt(d/p))^2/d. It feeds c at O(1) while its action on vectors vanishes, so beta drops out. Checked at d = 200 for p = d/4 to 16d: every width is within 8e-3 of the p-free flow. Training the readout moves the test error by 0.027.

Method worth reusing: when a preconditioner has a bulk with O(1) trace but a vanishing operator norm, the bulk enters only through scalar traces. Look for the trace identity before trying a measure-valued DMFT.

Related: [[t252_hessian_bulk_is_plugin_mp_law_2026_11_01]], [[t307_one_step_dsm_finds_hidden_line_2026_11_01]].
