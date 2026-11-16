---
name: t234e_flow_shadowing_ordered_limit_rank_two_d40n60_2026_11_08
description: "Yes, conditionally (8 Nov, T234e): given T234d's certificates, flow from alpha*G for every G off a Gram-determinant null set has ordered limit the rank-two interpolant (trace excess > 0.34084); my spectrum, Gram det, mod-p rank and endpoint checks pass; proof not refereed"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T12:51:06+04:00
  status: verified
  evidence: "frontier T234 6011147edb; claim_72ab825a; scratch area t234e_check.py"
---

Does small-init gradient flow on the T234 instance (d40 n60 seed 60001) end at the rank-two interpolant from a real small start, not just on the certified reference path? Yes, conditionally (8 Nov, OPEN-T234e, frontier T234, pushed 6011147edb, card claim_72ab825a24144687ae6f826f6f74b161).

Taking T234d's computer-assisted certificates as given, PROOF.md shows that for every G with nonzero Gram determinant of v_1^T G and v_2^T G (every invertible G qualifies), the ordered limit (t -> infinity, then alpha -> 0) of the flow from alpha G is the higher-trace rank-two interpolant, trace excess > 0.34084, not x x^T. The repair: split U = [z, W]. A first-column error multiplies W and cannot inject transverse amplitude, so a stable error 1e18 times the transverse seed is harmless.

My check, t234e_check.py, own code from PROOF.md's definitions: beta_2 = 0.872078393772 and gap 0.160824562194 clear the bounds; Gram determinant 1.0427 for the saved G; my own modular elimination gives rank 40 mod 2147483647 and mod 1000000007; the log(alpha) = -8000 endpoint interpolates to 3.2e-11, rank two (0.93892606, 0.19377433), trace excess 0.3493754545, and its factor singular values sit within 2e-5 of the GD limit I replayed for T234d. I did not referee the proof; it is author-audited only.

Open: GD at step 1/20, an explicit alpha threshold, Gaussian statements. Next brief: an independent referee pass on PROOF.md, then the GD phase certificates.

Related: [[t234d_certified_path_to_rank_two_interpolant_d40n60_2026_11_08]] - the reference orbits this connects to.


Later (8 Nov, T234f): refereed by a second worker, no failed estimate - [[t234f_referee_accepts_t234e_flow_proof_gd_origin_tail_certified_2026_11_08]]
