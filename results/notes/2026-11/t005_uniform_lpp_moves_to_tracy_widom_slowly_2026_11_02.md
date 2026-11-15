---
name: t005_uniform_lpp_moves_to_tracy_widom_slowly_2026_11_02
description: T005: uniform-weight LPP to n 800 moves toward GUE Tracy-Widom (skew 0.136->0.202 vs 0.224, sd exponent ->1/3); exponential control matches; uniform time constant about 1.498
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T06:35:30+04:00
  status: provisional
  evidence: "rows/T005/moves.jsonl 40d64e31"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T005 (KPZ universality for last-passage percolation with general weights), first frontier move, 2 Nov 2026, an agent. Move m005a, rows/T005/moves.jsonl 40d64e31; t005_lpp.c, t005_extrap.py and runs in 06_math_research/frontier/rows/T005.

- Control, exponential weights (proved TW): skewness 0.227-0.241 against 0.2241. The time-constant pair fit recovers g = 4 to 1.4e-4.
- Uniform[0,1] weights, n 100-800:
  - the sd exponent per doubling rises 0.303 -> 0.328, toward 1/3;
  - skewness rises 0.136 -> 0.202, toward 0.2241;
  - the gap to the control shrinks 0.105 -> 0.036.
- So the behaviour is KPZ-like, with strong finite-size corrections for bounded weights. Kurtosis is too noisy to judge.
- Side estimate: the uniform time constant is about 1.498. The pair fits run 1.5004, 1.4992, 1.4987, drifting down, so it is not clearly 3/2. I did not look up a published value.
- PREREG82: 4 of 4 passed; (a) passed at 1.97 se.
- Same measurement-inside-a-known-picture pattern as [[t016_dla_radius_exponent_0p592_inside_half_two_thirds_2026_11_02]]. The control-recovers-the-exact-value step is what made the extrapolation trustworthy; see the extrapolation scar [[scar_extrapolation_past_measured_range_2026_07_08]].


Correction (3 Nov, an agent review, rows/T005/reviews_agent): two printed skewness errors were below the sqrt(6/N) floor (exp n 800: 0.0071 vs 0.0122), so PREREG82 (a) passed at 1.14 se, not 1.97. With a 1/n term (the exponential control recovers g = 4.00008 +- 0.00059) the uniform time constant is 1.49806 +- 0.00010, so it is not 3/2.
