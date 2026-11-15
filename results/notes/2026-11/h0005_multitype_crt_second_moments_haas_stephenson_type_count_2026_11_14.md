---
name: h0005_multitype_crt_second_moments_haas_stephenson_type_count_2026_11_14
description: "[PROVISIONAL] Does a critical multitype GW tree reach the Brownian CRT under second moments only? Yes when conditioned on one type's count (Haas-Stephenson 1912.07296 Thm 4.1); total-size conditioning still open (H0005)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T17:59:16+02:00
  status: provisional
  evidence: ""
---

H0005 = open problem 3 of arXiv 2608.15987 (Kumar, threshold cascades): replace exponential moments in Thm 6.4 (CRT limit of the critical multitype failed cluster, via Miermont 2008) by g''(1) < inf. 14 Nov 2026, an agent, provisional, not audited.
Found: Haas-Stephenson, Scaling limits of multi-type Markov branching trees, arXiv 1912.07296, Thm 4.1: finitely many types, critical, irreducible, non-singular, finite second moments; conditioned on n vertices of type 1 with uniform measure on type-1 vertices, GHP limit (2 sqrt(a_1)/sigma) x Brownian CRT. Read in the paper text (lines ~1326-1390 of the pdftotext).
Open: conditioning on the TOTAL size under second moments (Addario-Berry-Beltran-Stufler-Thevenin 2507.23241 do weighted counts under exponential moments). Route: reduced type-1 tree with i.i.d. (xi, W) block pairs, bivariate cyclic lemma + local CLT, Brownian bridge independent of the second endpoint, Kortchemski 2012 leaves-conditioning method; missing step is transferring the full-tree metric.
Files: 12_cognitive_architecture/math/trio_1011/op/H0005/NOTE.md, STATUS.md. Related: [[p0418_hyperbolic_ensemble_gives_ipvt_nonpoisson_needs_long_range_2026_11_14]] (same day, same loop).
