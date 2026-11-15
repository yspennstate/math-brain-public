---
name: an09_fuglede_dim2_finite_sets_in_z60xz12_check_out_2026_11_12
description: "Fuglede dimension two (Zhang 2607.15632): do the two 60-point sets in Z60 x Z12 hold up? Yes, both finite claims checked twice; the R^2 transfer step not checked; dimension one open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T00:47:21+02:00
  status: verified
  evidence: "an09_check.out and an09_check2.out: two separate programs, exact and floating, largest family 10 of 12, positive controls 12; push 71436d7b2490"
---

Row AN09 (Fuglede's conjecture in dimensions one and two), 12 Nov 2026.

arXiv 2607.15632 (Tao Zhang, 17 Jul 2026) gives two explicit 60-point sets in G = Z60 x Z12: A- tiles G (complement T- of 12 points) and has no spectrum; A+ has a 60-point spectrum and does not tile G. Both finite claims were checked here by two separately written programs (exact arithmetic in Z[x]/(Phi_60) plus a clique search; floating sums plus a layered backtracking in Z12 x Z12 x Z5). Both give: largest orthogonal family in a fibre 10 (12 needed), largest packing complement of A+ 10 (12 needed); positive controls find 12.

The argument for "no spectrum" that needs only a small search: a 60-point spectrum has 12 points in one coset of the index-5 subgroup S of the dual; their differences are zeros of the transform inside S (105 of 143); the largest clique there is 10.

Not checked: the passage to R^2 (Proposition 2.1 of the preprint; Kolountzakis-Matolcsi 2006 Theorems 4.1, 4.2 and a rectangular version of Matolcsi's Proposition 2.5). No follow-up on arXiv as of 12 Nov.

Scar from the check: my first positive control for the layered search returned 0 because the layering was on the wrong coordinate for the control sets (E is a graph over the second coordinate). A control that fails is first a question about the control's own precondition; the main searches had theirs verified (no zero of the form (0, v, 0)).

Files: 06_math_research/an09_fuglede_agent_2026_11_12/ (AN09_CHECK.md, an09_check.py, an09_check2.py, outputs). Row proposal: restate to dimension one. Related: [[t283_polytime_low_degree_conjecture_refuted_small_noise_only_2026_11_12]].

