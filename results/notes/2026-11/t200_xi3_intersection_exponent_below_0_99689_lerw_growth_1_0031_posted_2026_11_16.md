---
name: t200_xi3_intersection_exponent_below_0_99689_lerw_growth_1_0031_posted_2026_11_16
description: "T200 posted: Brownian intersection exponent xi_3(1,1) < 0.99689 in 3D, so loop-erased random walk growth exponent and Brownian cut-point dimension >= 1.0031 (Zenodo 24247997); improves Liu's 0.9999 via Bessel exit law and Riesz kernel weights"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:14:11+02:00
  status: verified
  evidence: "fillq_ctl/t200_note/paper/main.tex"
---

T200, posted (paper "A sharper explicit bound for the Brownian intersection exponent in three dimensions", Zenodo 10.5281/zenodo.24247997; source fillq_ctl/t200_note/paper/main.tex).

Result: xi_3(1,1) <= 1 - 9000/(2361557 log(17/5)) < 0.99689, improving Liu's xi_3(1,1) < 0.9999. Consequences: the growth exponent of three-dimensional loop-erased random walk is at least 1.0031 (was 1.0001), and the cut points of a 3D Brownian path have Hausdorff dimension at least 1.0031 almost surely.

Method: Liu's comparison of the first and second moments of the non-intersection probability through the capacities of successive pieces of one path, with four changes: the exact exit-time law of the 3D Bessel process replaces the tail bound for a piece's duration; the occupation measure of a piece is weighted by the equilibrium measure of the 1D Riesz kernel of order one half; an exponential moment of the total capacity is bounded instead of counting large-capacity pieces; the two radius ratios vary. Independent numeric check: fillq_ctl/t200_note/indep_check.py.

Plain words: how often two Brownian paths in space miss each other, and so how fast a loop-erased random walk grows.

Why this memory exists: on 16 Nov a recall probe built from the four posted abstracts found T200 0 of 3, because the brain had no memory of the posted result at all (fillq_ctl/recall_probe_1115_RESULTS.md).

