---
name: ag05_jacobian_dim3_counterexample_recomputed_exactly_2026_11_12
description: "Jacobian conjecture false in dimension 3 (Alpoge 2026)? Yes: map recomputed, det -1/9, two points one image; dimension two stays open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:22:16+02:00
  status: verified
  evidence: "det JF = -1/9 three ways in exact arithmetic; F(1,0,-1) = F(0,-9,71); control values of q1 fail"
---

Row AG05 (Jacobian conjecture), 12 Nov 2026.

The three-dimensional counterexample (Alpöge, July 2026; van den Essen's form in arXiv 2609.17795) recomputed exactly. With u = 1 - (2/3)xy: F1 = u^3 z + y^2(-(2/3)u^2 - (2/9)u), F2 = x u^2 z + y(u^2 - (2/3)u - 2/9), F3 = x + x^2 y + x^3 z, degrees 7, 6, 4.

det JF = -1/9, three ways (sympy; own Fraction-dictionary polynomial arithmetic; evaluated Jacobian at 200 random rational points). F(1,0,-1) = F(0,-9,71) = (-1,-1,0); 16 coincidences on a grid of 3375 small rational points, some off the plane w = 0. F3 = x(1 + xy + x^2 z) is reducible. So the conjecture is false in every dimension n >= 3. This is a finite exact check, not a reading of someone's proof.

Open: dimension two (Magnus's prime-degree theorem blocks the same construction in the plane). Not recomputed: de Bondt's derived counterexamples (arXiv 2610.24889: HJC(15), JC(12,3), cubic-linear in dimension 90, Zhao's vanishing conjecture).

Method worth keeping: when a claimed refutation is an explicit object, recompute the object before reading any commentary; leave a coefficient the text prints unclearly as an unknown and let the defining identity fix it (here q1 = -2/3 was forced); add a control (other q1 give a non-constant determinant) so the check is seen to be able to fail.

Files: 06_math_research/ag05_jacobian_agent_2026_11_12/ (AG05_CHECK.md, ag05_check.py, ag05_check.out). Row proposal: restate to dimension two. Related: [[lo01_vaught_infinitary_counterexample_first_order_open_2026_11_12]], [[it01_mds_even_characteristic_preprint_last_section_checked_2026_11_12]].

