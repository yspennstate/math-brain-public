---
name: p0310_riesz_1d_gap_convexity_route_still_open_2026_11_14
description: "[PROVISIONAL] P0310 1D Riesz gas uniqueness 1<s<=2: still open (lit check 14 Nov); gap convexity + MTP2 monotonicity + convex canonical free energy proved; route needs strict convexity and a long-range Funaki-Spohn"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T12:25:41+02:00
  status: provisional
  evidence: ""
---

P0310 (Lewin 2022 review Sec VI.A, Thm 47 remark): uniqueness of Gibbs states for the 1D Riesz gas r^{-s}, 1<s<=2. Known: translation invariance s>1 (Frohlich-Pfister 1981), uniqueness s>2 (Papangelou PTRF 74, 1987). Lit check 14 Nov 2026: still open; Boursier 2209.00396 (0<s<1), Pei 2609.28503 (-|x|^a, 0<a<1), Lelotte 2309.08951 (-1<s<0) are other ranges. Note op/P0310/NOTE.md (an agent): proved for all s>0 - energy convex in gaps, mixed derivatives -V''<0 so the canonical law given exterior is MTP2 (Karlin-Rinott), monotone in the boundary; for s>1 Prekopa gives convex canonical free energy per particle in the spacing. Route: label coordinates turn the gas into a convex attractive long-range gradient model with couplings ~k^{-s-2}, second moment finite iff s>1; the A001 cut obstruction (energy sum r^{1-s}) does not appear for forces (sum k^{-s-3/2} converges). Open: (ii) strict convexity of the canonical free energy (single density per mu), (iii) uniqueness of the label-stationary field per mean gap (Funaki-Spohn 1997 is nearest-neighbour, uniformly convex). Suggested numeric: number variance per length of the periodic canonical gas at s=1.5 as N grows. Related: [[p0247_af_last_vertex_uniform_yes_under_dc_via_bht_open_torus_like_2026_11_14]]
