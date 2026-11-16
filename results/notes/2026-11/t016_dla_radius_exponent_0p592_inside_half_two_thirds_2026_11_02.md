---
name: t016_dla_radius_exponent_0p592_inside_half_two_thirds_2026_11_02
description: T016: on-lattice planar DLA, 8 clusters to 512k particles, radius exponent 0.5916 +- 0.0025 (D_f 1.69), far inside the proved 1/2..2/3 window
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T06:23:23+04:00
  status: provisional
  evidence: "rows/T016/moves.jsonl a93f038c"
---

T016 (planar DLA radius growth), first frontier move, 2 Nov 2026, an agent. Move m016a, rows/T016/moves.jsonl a93f038c; t016_dla.c, t016_fit.py and the raw runs in 06_math_research/frontier/rows/T016.

- Proved: n^{1/2} <~ R_n <~ n^{2/3} (Kesten). Nothing better is known for DLA.
- On-lattice DLA on Z^2, 8 clusters to 512,000 particles. Near the cluster the walk is exact; far jumps are Brownian circle jumps rounded to the lattice, an approximation.
- Rg ~ n^0.5916 +- 0.0025 (D_f 1.690) over n 32k-512k. Rmax gives 0.5906 +- 0.0084, and Rmax/Rg = 1.90 throughout.
- The error is the spread of 8 independent clusters' slopes. Doublings within one cluster are correlated and were not counted as separate confirmations.
- The exponent per doubling is flat from 4k to 512k. A 0.610 last doubling on 2 clusters was noise (0.594 on 8).
- PREREG81: 3 of 3 passed.
- The run took about 10 min on 2 cores. Same move pattern as [[t015_saw_gain_per_step_at_least_9_7_parity_dip_2026_11_02]] (a measurement placed inside a proved window, not a bound).

