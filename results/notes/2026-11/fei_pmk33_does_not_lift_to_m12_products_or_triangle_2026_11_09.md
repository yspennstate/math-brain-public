---
name: fei_pmk33_does_not_lift_to_m12_products_or_triangle_2026_11_09
description: "FEI record PM(K33) at m=12? Built on top of it, it does not lift: 762 products h OP g (best 5.7384) and 729 K33+triangle hosts (best 5.4262) are all below the 6.4000 bar and none is exact; 0.009 gaps between symmetric hosts are uS tie-break noise"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T09:26:08+02:00
  status: provisional
  evidence: ""
---

The 6.5218 FEI record PM(K33) (the 3x3 rook grid line host on 9 points) does not carry over to m = 12 when hosts are built on top of it. Both runs used fano_19as's uS completion and score formula with scipy matching (score_it_lib.py), and each was checked against fano_19as's own scorer on three hosts.

- 19cr: f = h(x_0..x_8) OP g(x_9..x_11), with h = PM(K33), g any of the 254 non-constant 3-bit functions and OP xor/and/or, 762 hosts in all. The best is 5.7384 (or, g = indicator of 000, d 386, not exact). The best and and xor hosts score 5.61 and 5.14. 70 of the xor hosts are exact.
- 19cs: K33's six lines plus a triangle {9,10,a}, {10,11,b}, {9,11,c} on three new points, all 729 choices of a, b, c. The best is 5.4262 (a = b = c, d 688), all 729 lie in 5.31-5.43, and none is exact.
- The m = 12 bar is 6.4000392, from the 19cj two-regular classes, which do not contain K33. Every extension scored 0.66 or more below it.
- Choices that K33's symmetry makes equivalent differ by up to 0.009. That is uS breaking ties at the split level by cell index, so a difference of that size between non-exact hosts is noise, not structure.

Why it matters: the record is exact because level 4 has 9 + 9 = d cells ([[fei_pmk33_exact_because_level4_is_9_plus_9_equals_d_2026_11_09]]). Every extension tried has d in the hundreds and loses that exactness. A 12-point candidate has to be designed so that its own completion stays exact, not grown from the 9-point record. Files: fei_loop_agent/{prod_19cr.py,tri_19cs.py,orbit_19ah_note.md} (sections 19cr and 19cs). On GitHub: the private brain repository: 06_math_research/frontier/fei_loop_agent (commit 5add0ea3dfd3 for 19cr; 19cs in push66). Related: [[fei_pmk33_record_independently_recomputed_with_its_18_variable_lift_2026_11_09]], [[fei_r72_exhaustive_radius_3_around_pmk33_no_gain_2026_11_08]].

Status: provisional. These are real computations, but they search one family each, and the uS completion is not exact on these hosts, so a score is a lower-bound estimate of what the host can reach.

