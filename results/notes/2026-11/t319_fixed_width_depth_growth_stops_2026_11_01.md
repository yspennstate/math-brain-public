---
name: t319_fixed_width_depth_growth_stops_2026_11_01
description: [PROVISIONAL] T319: at fixed layer width the ReLU secant-width estimate is flat in depth (4.1 at k=4, d=4..8); supersedes the sqrt(d) memory
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:58:10+04:00
  status: provisional
  evidence: ""
---



T319 follow-up (1 Nov, an agent), pushed d80c6ac to research-repo (research_pushes/2026-11-01-loop-T319-fixed-width), card claim_73fcda5501a94d999a4e10b29f851237.

With every layer at width 64 and k=4, the lower estimates are 1.89, 3.39, 3.89, 4.13, 4.11 and 4.15 at d = 1, 2, 3, 4, 6, 8. At d=3 the width is 3.33 to 4.21 for n = 16 to 256. The expansive net with d=6 and n=256 gave 4.55. So the earlier sqrt(d) reading needed the width to grow too. O(sqrt k) uniformly in depth is open again and leans toward yes at fixed width.

Lesson: when a confound has been named in the note, run the test that separates it before filing the headline as a memory or card. Here a same-day claim had to be withdrawn.

Supersedes [[t319_secant_width_grows_sqrt_depth_2026_11_01]].
