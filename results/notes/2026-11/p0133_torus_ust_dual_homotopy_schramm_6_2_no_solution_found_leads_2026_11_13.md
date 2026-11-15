---
name: p0133_torus_ust_dual_homotopy_schramm_6_2_no_solution_found_leads_2026_11_13
description: "P0133 (Schramm 2006 Problem 6.2, limiting law of the homotopy classes of the three noncontractible paths in the dual complement of a UST on a fine square torus) - no solution found 13 Nov 2026; leads are Kenyon 1001.4028 (vector-bundle Laplacian, CRSFs), Kassel-Kenyon 1211.6974 (CRSF multicurve limits on surfaces), Kenyon-Sun-Wilson 1310.2603 (dimers on tori, winding of double-dimer loops); none answers it as stated"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T14:36:15.057Z
---

P0133, rank 26: on a toroidal square grid with mesh -> 0, the edges not in a uniform spanning tree form a dual graph with
N faces and N+1 edges: a theta graph of three edge-simple noncontractible paths plus trees. Find the limiting joint law of
their homotopy classes. Source: Schramm, "Conformally invariant scaling limits" (ICM 2006 v2), Problem 6.2.

Structure: pi_1(torus) = Z^2, so homotopy = homology here. The complement of the tree must cut the torus into a disc, so
the three classes are a, b, a+b (up to signs) with (a, b) a basis of Z^2. The answer is therefore a law on bases mod the
theta-graph symmetries, i.e. on GL_2(Z) modulo a finite group, depending on the torus modulus tau.

Literature, checked 13 Nov 2026 (arXiv and web): no paper found that computes this law.
- Kenyon, "Long-range properties of spanning trees" (J. Math. Phys. 2000): crossing and winding on rectangles, annuli and
  cylinders, not the torus.
- Kenyon, "Spanning forests and the vector bundle Laplacian" (arXiv 1001.4028, AoP 2011): CRSF measures from line-bundle
  Laplacians. A U(1) connection with holonomy (z, w) weights each CRSF by its cycles' homology. This is the natural
  generating function: the UST's dual theta graph is the cycle structure seen by the dual Laplacian twisted by (z, w).
  The 200-list caveat already flags these "line-bundle determinant methods" as needing an exact-scope comparison.
- Kassel and Kenyon, arXiv 1211.6974: limits of CRSF multicurves on surfaces, conformally invariant, independent of the
  approximating graphs.
- Kenyon, Sun and Wilson, arXiv 1310.2603: finite-size corrections for dimers on tori and the law of the number of
  winding loops in double dimers (theta-function sums). Via Temperley on the torus, the UST's dual winding is a dimer
  height-change class, so the expected answer is a lattice theta-type sum in tau.

Prior work: 6 Sep first pass (Euler count only) and two 8-9 Sep Lean runs (no verdict). Next step if picked up: compute
det of the (z, w)-twisted dual Laplacian on the n x n torus, extract the coefficient pattern by (a, b), check against
exact enumeration on small tori, then take the limit. That is a computation we could actually run.
Related: [[p0141_pa_typical_distance_and_diameter_both_log_nu_n_solved_in_print_2026_11_13]] (same day's sweep).
