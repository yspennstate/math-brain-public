---
name: p0434_region_rationals_miss_the_faces_2026_11_08
description: "P0434 8 Nov 13:0x: five rationals cover all above-1 three-atom laws; each falls in K; put on m=1 or m=K none equals the two-atom ratio (up to 2.4e3 off), so bound by chaining region boundaries, not faces"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:11:22-05:00
  status: provisional
  evidence: "w3face1_agent.out; commit f79bd0c7"
---

P0434 (M-SERPT vs Gittins on [1, K], 2 < K <= 9/4), route item 69, 8 Nov 13:0x, an agent.

Every above-1 law seen on three atoms {1, m, K} equals one of five exact rationals: R5 (the closed tie region),
RA, RB, RC (item 68) and RD (new; tiny w, p < 0.035). On each one's validity set (|R - soap.ratio| <= 1e-9),
dR/dK < 0 at every sampled law, dR/dp > 0 and dR/deps < 0 nearly everywhere; R5 and RC fall in m, RB and RD rise in m,
RA is mixed.

The lesson: a region's rational put on a face (m = 1 or m = K) is NOT the two-atom ratio there. Differences up to 2.4e3
(RA at m = 1); only RB at m = 1 agreed, on 11 pct of points. So "follow the rise to a face and compare with S2" does
not work: the rise ends on the region's own boundary, where a run decision flips and another rational takes over.
Bound each rational by chaining region boundaries (as the F2 decision ended R5's path in item 65), not by faces.

Files: codex_fleet/runs/own_p0434/w3sgn, w3fifth, w3face1 (_agent), route item 69; brain repo commit f79bd0c7.
Links: [[p0434_region_ratio_rises_in_w_below_the_tie_exactly_2026_11_08]] [[p0434_tie_region_ends_before_u_max_exactly_2026_11_08]]

