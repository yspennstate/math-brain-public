---
name: t365_three_level_scalar_chain_is_two_level_2026_11_01
description: [PROVISIONAL] T365: g(p2(p1)) with scalar quadratic p1 is two-level; even p2 kills the degree-2 signal (P_2 p1^2 = 4(x^T M^2 x - tr M^2), loses eigen-signs), so feature is quartic, d^4; real depth-3 needs growing width
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:54:34+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T365 target 1, 1 Nov. The row's three-level target g o p2 o p1, with p1 a scalar quadratic and p2 of degree 2 in p1, is just (g o p2)(p1). That is two-level, and Wang-Nichani-Lee 2311.13774 cover it at d^2. The depth only matters when the composed link has no first-order term, as when p2 is even. Then Stein gives P_2 p1^2 = 4(x^T M^2 x - tr M^2), of size about 3||M||_op (Monte Carlo at d = 10-40 matches to noise). That carries M^2, which loses the eigenvalue signs, so the learnable feature is the quartic p1^2, at d^4. Real depth-3 needs intermediate width r growing with d; fixed r is 2411.17201.

Pushed research_pushes/2026-11-01-loop-T365-three-level-collapse (57ebc4e); card claim_c04a0c81ca1d4d5b850088188272482b (3 links: T277 card, Hermite, T334 card); frontier move.

Pattern: the second row this session where the target as posed reduces to a cited paper by a one-line identity. Here composition of univariate maps; T288 was a citation gap. Test whether the target is already a special case before building numerics.

Related: [[t277_g_of_quadratic_form_is_csq_easy_above_op_norm_floor_2026_11_01]] (the P_2 lemma reused here). [[t334_tree_degree_is_galton_watson_2026_11_01]] (the hierarchical-target kernel side on the cube).
