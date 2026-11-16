---
name: p0133_ust_torus_superbase_law_rotation_invariant_2026_11_14
description: "[PROVISIONAL] P0133 (Schramm 6.2 UST torus dual theta): is the superbase law conformally invariant? Simulated 14 Nov: yes to 1-2 se - tori at an angle to Z^2 give the PSL2(Z)-mapped law of the axis-aligned torus"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-15T00:05:00.000Z
---

P0133, Schramm 2006 Problem 6.2: the homology data of the uniform spanning tree's dual on a torus. Simulated (Wilson's algorithm, ust_torus_shear.py), 14 Nov 2026, an agent. Builds on [[p0133_torus_ust_dual_homotopy_schramm_6_2_no_solution_found_leads_2026_11_13]].

- Measured: the law of the random superbase of fundamental-cycle classes depends on the modulus tau only through its PSL2(Z) class. Modulus 0.6+0.8i = (tau-1)/tau for tau = 0.5+i, realised as 50x40 s30 and 100x80 s60; 0.8+0.4i = 2i/(1+2i) as 100x40 s80 and 150x60 s120. With classes mapped back (compare.py, matrices 0 -1 1 1 and 1 0 1 1), against 40x40 s20 and 32x64 at 24,000 samples a side: largest gaps 1.1, 2.8, 1.0, 1.7 se. The 2.8 is the fine 100x80 mesh against the coarse 40x40, in the direction the axis-aligned 80x80 run already moved (mesh effect about 1 percent).
- Also measured earlier the same day: figure-eight core frequency halves with each mesh halving; P(S) roughly C exp(-0.9 Q), Q = sum |v|^2 / Im tau, not exact.
- Open: an exact formula for P_tau(S). Leads: Kenyon arXiv 1001.4028 (line-bundle Laplacian, homology of CRSFs on the torus), Kassel-Kenyon arXiv 1211.6974.
- Files: 12_cognitive_architecture/math/trio_1011/op/P0133/ (NOTE.md finding 4, STATUS.md, compare.py). Samples: data/p0133_samples_2026_11_14.tar.gz and data/m_*.tsv.gz (10^6 each).

- Million-sample check, same day (ust_metal.swift on mini 2's GPU): 160x160 s80 vs 200x160 s120 agree to 0.34 se on the main superbases (max 1.9 se); 64x128 vs 300x120 s240 agree (mirror-pair sum 1.25 se). Scaling-limit values to ~3 digits: square torus top superbases 0.475 each, next four 0.0125 each; tau=0.5+i top 0.714 (meshes 40, 80, 160 move by under 0.001). NOTE finding 5.

- Later the same evening: 256x256 square torus 0.4750/0.4749 (limit holds); hexagonal torus (30x26 s15, 60x52 s30, 120x104 s60) top 0.7276, next three 0.090 each. Effective c in P ~ exp(-c Q): 0.904-0.911 on square, hexagonal and 0.5+i, but 0.85 at tau = 2i, and a pure exp(-c Q) fit gives chi2/dof 112 (shape_fit.py --deg 1). Commits 421dec52, 086f514e, dd828405.
- TRAP: "P_tau(S) = w(shape(S)) / Z(tau)" is vacuous. A superbase's triangle fixes its lattice up to similarity, so a shape never recurs at a non-equivalent modulus and any law fits it; a good chi2 there only re-tests conformal invariance. The content is the form of w: with e1 = sum cot (= Q/2) and e3 = prod cot (sum of pairwise cot products is 1) fixing the shape, shape_fit.py --deg k fits log w as a polynomial in (e1, e3). Degree 2 gave chi2/dof 2.97 on only 11 shapes; the 50-modulus grid (n1 = 100, n2 90..300, s 0..50, mini 2) decides it. Full grid, 49 moduli, 333 cells, 284 shapes (NOTE finding 6, data/grid/, 15 Nov): chi2/dof by degree 94.03, 11.67, 2.54, 4: 1.25. The cubic that fitted 38 moduli at 1.5-1.7 fails once the elongated n2 = 250, 300 tori come in, so the needed degree grows with the range: the polynomial is a local fit, not the law. Held-out six finest meshes: quartic 1.02 (28 dof, worst 1.92 se), cubic 2.48. Closed forms: best 4-term 2.58, 3-term 3.94. No formula. Do not read the cubic's e1 coefficient -2.00 as w ~ exp(-Q): it is the expansion at e1 = 0, outside the domain e1 >= sqrt 3.

What would change this: an exact formula disagreeing with the finding-5 values, or a placement gap at 256-scale meshes.
