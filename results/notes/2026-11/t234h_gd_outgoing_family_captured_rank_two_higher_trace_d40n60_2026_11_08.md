---
name: t234h_gd_outgoing_family_captured_rank_two_higher_trace_d40n60_2026_11_08
description: "Yes for the outgoing family, conditionally (8 Nov, T234h): GD 1/20 escapes the rank-one plateau to rank-two interpolants, trace excess >= 0.341; matching to the incoming family is the open step"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:18:24+04:00
  status: verified
  evidence: "frontier T234 open_t234h_agent_11_08 (355402bf07); card claim_a513ea73; t234h_check.out"
---

Does full-width GD at step 1/20 escape the rank-one plateau on the d=40, n=60 instance, and where to? Yes for the leading outgoing family, conditionally (8 Nov, T234h, Codex, reviewed by an agent): every outgoing phase lands at rank-two interpolants with trace above the planted trace.

At the certified rank-one minimum U* = [z, 0], M = (1/n) sum F_i A_i has 20 negative, 19 positive and 1 zero eigenvalue. The full-width GD Jacobian therefore has 780 expanding, 781 contracting and 39 center directions, and the leading multiplier is r = 1.00870178968588. The worker built a degree-seven discrete saddle parameterization with T(P(t)) = P(rt), anchored at the exact point and tangent, with a rational tail bound. It covered the phases [1, 100871/100000], which is one period [1, r). Outward phase Taylor propagation then reaches capture at step 23,219 with a family radius <= 1.36e-7. The trapping margin is >= 0.00387, the second singular value margin >= 0.436 and the trace excess >= 0.34083. Planted refusals hold: a widened cover [1,2] blows its remainder at step 825, and an operator bound of 1 fails the guard.

My replay (t234h_check.py, own float64):
- The eigen-counts, the 780/781/39 split and the multiplier all match.
- One step maps a=1 onto a=r within 1.2e-16.
- 9 phases are within 2.6e-11 of the capture center at step 23,219.
- At 60,000 steps the loss is under 6e-30, sigma_2 >= 0.4402 and the trace excess is 0.349363.
- The endpoints agree across phases to 7.9e-15. The endpoint looks phase-independent in float, but nobody has proved it.

Still open, and the only step left before the ordered GD limit: matching T234g's incoming family to this outgoing one. That needs a uniform relative transverse enclosure along the incoming curve, with a nonzero escape coefficient at every phase. The scope stays conditional on the IEEE/dot-product model; nothing is proof-assistant checked.

Card claim_a513ea73b21e4e8d81cd1e1efc2e4c4d; frontier T234 move 14:05, pushed 355402bf07.

Related: [[t234g_gd_origin_family_captured_rank_one_d40n60_2026_11_08]] - the incoming half this must be matched to.

Later (8 Nov, T234i): matching closed asymptotically for full-width starts, but the regime lies below float64; see [[t234i_full_width_capture_asymptotic_only_regime_below_float64_2026_11_08]].
