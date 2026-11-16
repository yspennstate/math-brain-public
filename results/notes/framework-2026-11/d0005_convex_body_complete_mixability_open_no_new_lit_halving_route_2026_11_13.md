---
name: d0005_convex_body_complete_mixability_open_no_new_lit_halving_route_2026_11_13
description: "D0005 (Wang, Current open questions in complete mixability, arXiv 1411.6190, Open Problem 5: is the uniform distribution on a convex body in R^d (d+1)-completely mixable, equivalently n-CM for every n >= d+1?) is open on 13 Nov 2026: arXiv has nothing on multivariate complete mixability of uniform convex bodies since the 2014 list. Our own partial results stand: every simplex and every body with a fixed-point-free affine symmetry of order n is n-CM (orbit construction, 8 Sep A001); the HARD8-01 run (16-17 Sep) reduced the planar case to one missing coupling; the 8-9 Nov recursive equal-area halving work found the L3 stall is a selection problem, not a forced one"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T17:43:50.597Z
---

D0005, rank 49 on the 200 list. Source: Ruodu Wang, "Current open questions in complete mixability", arXiv 1411.6190
(Probability Surveys 2015), Open Problem 5, PDF p.16. C is a convex body in R^d. Is the uniform distribution on C
n-completely mixable (n random vectors with that law whose sum is a.s. constant) for every n >= d+1? The source says
this is equivalent to (d+1)-complete mixability and records only d = 0 and d = 1 as settled.

Status 13 Nov 2026: open.
- My arXiv check on 13 Nov: "complete mixability" or "completely mixable" with convex, uniform or multivariate; all
  titles with "mixability". Nothing on uniform distributions on convex bodies. The nearby papers are one-dimensional or
  about other families:
  - Yin and Zhu, arXiv 1706.05499: joint mixability of elliptical families (a uniform ball or ellipsoid is elliptical,
    but their results are about joint mixes of one-dimensional marginals, with a short multivariate remark).
  - Koike, Lin and Wang, arXiv 2204.11438: joint mixes and negative dependence, one-dimensional marginals.
  - Ansari and Rockel, arXiv 2608.20176 (Aug 2026): the attainable constants of |U'+V'| for uniform U', V' on an
    interval, "generalized mixability" in one dimension.
- Our earlier work:
  - 8 Sep pass D0005-A001 (memory d0005_simplices_are_d_plus_one_completely_mixable_2026_09_08): if C is invariant about
    its centroid under a linear R with R^n = I and no fixed vector, then (X, RX, ..., R^{n-1}X) is a complete mix, since
    sum R^k = 0; affine images keep both uniformity and the mix. So every simplex is (d+1)-CM, and so is every body with
    such a symmetry. A generic body has no symmetry, and gluing simplex pieces fails because the pieces' centroids differ.
  - HARD8-01 in open-problems-repo (16-17 Sep, three reports): reduced the planar case to an aggregation step and an
    exact separator hierarchy, and isolated one missing planar coupling. Retired OPEN/PARTIAL.
  - 8-9 Nov recursive equal-area halving (memory d0005_l3_triple_separating_halving_exists_stall_is_selection_2026_11_08):
    the frozen diameter that stalled level 3 is not forced; an admissible exact halving shrinks the largest piece by
    0.870. The open question there is a selection rule that makes the piece diameters go to zero, which would give a
    planar triple coupling in the limit.
- There is no Codex report for D0005 in referee_reports/2026-11-13.
- Where an attempt could start: d = 2, n = 3, by the halving route. A rule that provably shrinks diameters at a fixed
  rate would finish the planar case; the d-dimensional case would need the same with d+1 pieces.

Related: [[p0023_efficient_coupling_acute_triangle_open_hot_spots_2026_wave_2026_11_13]] (previous item in this loop).
