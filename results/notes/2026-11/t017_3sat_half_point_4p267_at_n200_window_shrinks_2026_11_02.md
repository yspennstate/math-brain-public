---
name: t017_3sat_half_point_4p267_at_n200_window_shrinks_2026_11_02
description: T017 random 3-SAT, exact DPLL n 50-200: half-satisfiable point 4.354 -> 4.267 +- 0.01 at n 200, window 0.70 -> 0.41; curve crossings too noisy (PREREG86 b miss)
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:15:16+04:00
  status: provisional
  evidence: "rows/T017/moves.jsonl 2bc1159b"
---

T017 (sharp random k-SAT threshold; 3-SAT conjectured at 4.2667, rigorous upper bound 4.268), first frontier move, 2 Nov 2026, an agent. Move m017a, rows/T017/moves.jsonl 2bc1159b; t017_dpll.c, t017_analyze.py and the runs are in 06_math_research/frontier/rows/T017.

- Method: an exact DPLL solver, with every satisfying assignment checked; n 50-200.
- The half-satisfiable point falls with n: 4.354 to 4.267 at n 200, +- 0.01.
- The 10-90% window narrows from 0.70 to 0.41 (nu_eff about 1.8).
- PREREG86: (b) MISSED. Crossings of successive curves scatter 4.06-4.34, because nearly parallel curves give noisy crossings. The half-point is the better statistic here.
- Cost: the DPLL node count grows about 10x per 50 variables at the threshold (22k nodes at n 200, 0.12 s per instance). n 300 is out of reach for this solver.
  - The next step needs a CDCL solver (for example kissat, if installed) or survey propagation for larger n.
  - Timing n 300 first, before a full scan, saved an hour.
- Related: [[t012_interchange_3d_long_cycles_poisson_dirichlet_2026_11_02]].

