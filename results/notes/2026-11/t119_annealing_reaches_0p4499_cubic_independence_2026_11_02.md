---
name: t119_annealing_reaches_0p4499_cubic_independence_2026_11_02
description: T119: annealed independent sets on random cubic graphs reach 0.44985 (n 1e5, 1e5 sweeps), between Csoka's 0.44533 and Harangi's 0.45078521; not finite-size
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T05:34:55+04:00
  status: provisional
  evidence: "rows/T119/moves.jsonl 03036cfd"
---

T119 (independence ratio alpha_3 of random cubic graphs), first frontier move, 2 Nov 2026, an agent. Move m119a, rows/T119/moves.jsonl 03036cfd; files t119_sa_mis.c, t119_run1.sh and the run outputs (research folder 06_math_research/frontier/rows/T119).

- Proved interval: 0.44533 (Csoka, local algorithms) < alpha_3 < 0.45078521 (Harangi 2204.01353). The w675 claims on the row reproduce the upper bound.
- Hard-core annealing (fugacity 1 to 1e4, swap moves, greedy fill) at n = 1e5 reaches 0.44766, 0.44932 and 0.44985 at 1e3, 1e4 and 1e5 sweeps.
- At n = 1e6 and 1e4 sweeps it reaches 0.449331, so these are not finite-size effects.
- A geometric fit to the three gains gives about 0.4501. That is an extrapolation past the measured range, not a bound.
- So search passes the local-algorithm bound by 0.0045 and stops about 0.0009 under the upper bound.
- PREREG77: (a) MISS (I expected 0.444-0.4475); (b) and (c) PASS.
- Same method as the T122 MaxCut annealing, [[t122_first_moment_maxcut_ceiling_0p9385_d3_harangi_bounds_below_2026_11_02]] (sa_cut.c).


ADDENDUM (2 Nov 05:52, move m119b, moves 0d9159c3): 1e6 sweeps at n = 3e4.
- A control at 1e5 sweeps reproduces n = 1e5 (mean 0.44985).
- Best set seen: 0.45027 and 0.45000. End sets after the fill: 0.44993 and 0.44980.
- At this n the best-over-sweeps figure runs 3 to 9 vertices above the end set, so 0.4499 (end sets) is the conservative number.
- Gains per decade: 0.00166, 0.00053, 0.00028, which points to a stop near 0.4502, about 0.0006 under the upper bound. That is a guess from four points.
- PREREG78: all three predictions passed.
