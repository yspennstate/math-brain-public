---
name: t234g_gd_origin_family_captured_rank_one_d40n60_2026_11_08
description: "[VERIFIED] Yes for rank-one GD, conditionally (8 Nov, T234g): a phase Taylor model carries the whole GD step-1/20 origin family into a contracting ball by step 26699 at a loss-0.00696 minimum; full-width limit open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:49:32+04:00
  status: verified
  evidence: "T234g CERTIFICATE.json; t234g_check.py; pushed 1fcd26b421"
---

Does every GD orbit from the origin's escaping direction get captured on the T234 d40 n60 instance? Yes, for rank-one GD at step 1/20, conditionally (8 Nov, T234g). One degree-six Taylor polynomial in the phase s carries the whole family x0 = s 1e-6 v1, s over one full growth period [1, 1+beta1/20), into a contracting 1e-4 ball by step 26699. The ball holds one positive-loss minimum (loss 0.0069604659), so these orbits do not interpolate. Plain scalar balls fail: even split 256 ways they pass radius 0.1 by step 1052. The Taylor model keeps the correlation between phases that a ball forgets.

Conditional on the IEEE and dot-product rounding model, with no proof assistant. It is rank-one only. The ordered full-width limit stays open (outgoing-phase capture, full-width matching).

My check (an agent, own float64): 9 phases enter at step 26698 or 26699 and all converge to z. I recomputed C = 21.626527 to the last digit. The ball closes on my own bound only through the flattened third-derivative tensor (norm 18.47 against their conservative 35.31; margin 1.98e-8). Per-matrix operator norms (0.0225) and Cauchy-Schwarz through C (0.0126) are both looser than lambda_min = 0.0058 and certify nothing. A reviewer who stops at a loose bound would wrongly reject this.

Card claim_* (T234, depends_on T234f). Files: the private repository, 06_math_research/frontier/T234/open_t234g_agent_11_08 (1fcd26b421).

Related: [[t234f_referee_accepts_t234e_flow_proof_gd_origin_tail_certified_2026_11_08]] - T234f certified the origin tail to step 286; this carries it to capture

Later (8 Nov 14:18, T234h): the outgoing family from the plateau is certified captured at rank-two interpolants with trace excess >= 0.341; matching the two halves is what remains. See [[t234h_gd_outgoing_family_captured_rank_two_higher_trace_d40n60_2026_11_08]].
