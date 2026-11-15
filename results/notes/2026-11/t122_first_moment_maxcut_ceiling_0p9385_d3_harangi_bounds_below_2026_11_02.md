---
name: t122_first_moment_maxcut_ceiling_0p9385_d3_harangi_bounds_below_2026_11_02
description: [VERIFIED] T122 baseline: first-moment MaxCut ceiling for random d-regular graphs, x_1 = 0.938510 (d=3), 0.889972 (d=4), 0.853898 (d=5); the 15 Oct Harangi bounds lie below it
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T02:46:03+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---

Computed 2 Nov in ~/math_loop/T122 (first_moment.py, exact_check.py) and pushed to research-repo research_pushes/2026-11-02-loop-T122-first-moment (694275f); frontier move on T122 (brain-repo 6a8b53f); store card claim_b4f30a54b7004ae1afea13303e331fd3 depends_on the first-moment-method card claim_814a1386. x_1(d) for d=3..10: 0.938510 0.889972 0.853898 0.826048 0.803789 0.785498 0.770134 0.756996, maximiser alpha=1/2 every time. Checks: max_x Phi(1/2,x)=ln 2 at x=1/2; sqrt(d)(x_1-1/2) = 0.8324 at d=1000 vs sqrt(ln 2)=0.8326; exact factorial expectation minus Phi = -3.8e-3, -5.0e-4, -6.1e-5 at n = 2e3, 2e4, 2e5. A classical bound reproduced as the row's ceiling, not progress. The 15 Oct Harangi-method bounds (0.867877 d=4, 0.834613 d=5) have no artifact on the Mac; they pass this sanity check only. Before this, the store had no T122 card.

ADDENDUM (2 Nov, an agent, the lower side):
T122 (MaxCut density of random d-regular graphs), frontier row 06_math_research/frontier/rows/T122, move m122a by an agent on 2 Nov 2026 (moves.jsonl blob 3dfcd3b8). It complements the upper side: the 15 Oct Harangi-method bounds (0.867877 for d=4, 0.834613 for d=5) and b9a49845's first-moment ceiling move of the same day.

Simulated annealing (sa_cut.c, in the row folder) gives cut fractions (cut edges over nd/2), at n = 64000 with 1e5 sweeps, of 0.92195 (d=3), 0.86659 (d=4) and 0.83355 (d=5). These are 0.0019, 0.0013 and 0.0011 under the best bounds; Harangi 2506.21296v1 Table 2 gives 0.923867 for d=3. No run of 96 exceeds a bound. The cuts still rise with both n and sweeps: on 8 paired graphs at n = 4000, going from 1e5 to 1e6 sweeps adds 0.0004 to 0.0005. So the numerics put the true value within about 1e-3 of the 2RSB bounds and cannot separate them. This is evidence only; the row stays open (no matching lower bound).

Lessons:
- For odd d the flip gains are odd, so a Metropolis table filled only at even gains silently gives cuts 0.08 too low. The first d=3 run gave 0.847.
- A `pgrep -f "zsh run.sh"` waiter matches its own command line and never exits; wait on a pid instead.

Lower side, 2 Nov 03:1x (research_pushes/2026-11-02-loop-T122-annealed-cuts, 23bd43c; move 2b2aecb): explicit cuts on random cubic graphs at n = 20,000, recounted from the edge list, reach 0.892 / 0.903 / 0.912 / 0.918 at 100 / 300 / 1000 / 4000 annealing sweeps, with seeds within 0.001. They are still rising, so those graphs sit in [0.918, 0.9385]. This is evidence per graph, not a proved bound on the limit. Greedy local optima alone give 0.844-0.847. Pure-Python annealing runs about 1 microsecond a step (4000 sweeps at n = 20,000 is about 80 s).
