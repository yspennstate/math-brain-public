---
name: t006_fpp_chi_0p31_xi_0p67_kpz_relation_holds_2026_11_02
description: T006 planar FPP to n 512: chi 0.310 +- 0.006, xi 0.675 +- 0.012, KPZ relation off by 0.039 (1.6 se); one seed's low last doubling was noise
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T06:46:51+04:00
  status: provisional
  evidence: "rows/T006/moves.jsonl 8e96e72c"
---

T006 (planar first-passage percolation: the KPZ relation chi = 2 xi - 1 and the values 1/3, 2/3), first frontier move, 2 Nov 2026, an agent. Move m006a, rows/T006/moves.jsonl 8e96e72c; t006_fpp.c, t006_fit.py and runs in 06_math_research/frontier/rows/T006.

- Setup: exponential(1) edges, Dijkstra in a box, n 32-512. No geodesic touched the box side.
- Fit over n 64-512: chi = 0.310 +- 0.006 (sd of T), xi = 0.675 +- 0.012 (geodesic max deviation). chi - (2 xi - 1) = -0.039, 1.6 se.
- Lesson: with one seed, the 256->512 doubling gave chi 0.249, three se low. A second seed raised it to 0.280, and xi dips over that same doubling, so the relation tracks there too. Do not report one seed's last doubling as a trend; add a seed first, as with [[t015_saw_gain_per_step_at_least_9_7_parity_dip_2026_11_02]]'s adjacent-doubling zigzag.
- fit.py now pools repeated n by sample-weighted mean square. The unpooled fit was rechecked and is identical.
- T/n still falls at n 512 (0.4163).
- PREREG83: 4 of 4 passed.


Addition (3 Nov, an agent review, rows/T006/reviews_agent, ACCEPT): with mu fixed at Alm-Deijfen 0.4041702 the mean drift T/n - mu decays as n^-0.634 (chi_eff 0.366) against 0.310 from sd T, so the two channels straddle 1/3; forcing n^-2/3 overshoots mu by 6-10 se at n <= 512. The xi error comes from 3 slopes (2 dof), so the 1.6 se KPZ gap is within noise.
