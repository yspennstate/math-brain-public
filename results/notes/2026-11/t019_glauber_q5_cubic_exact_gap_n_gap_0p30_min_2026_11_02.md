---
name: t019_glauber_q5_cubic_exact_gap_n_gap_0p30_min_2026_11_02
description: T019 Glauber colourings, exact heat-bath gap at Delta 3 q 5 (outside proved range): 21 cubic graphs n<=10 all ergodic, n*gap 0.30-0.50; cycles q 4 n*gap 0.350; q = Delta+1 freezes K4, Q3, C9; PREREG99 4/4
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T08:37:22+04:00
  status: provisional
  evidence: "rows/T019/moves.jsonl d024053d"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T019 (Glauber colourings mix in O(n log n) at q >= Delta + 2), first frontier move, 2 Nov 2026, an agent. m019a is in rows/T019/moves.jsonl (d024053d); the code is t019_gap.py in 06_math_research/frontier/rows/T019.

- Method: an exact heat-bath gap computed by enumerating all colourings and running Lanczos. Delta 3 and q 5 lies outside every proved range.
- Cubic graphs at q 5 (21 of them, n <= 10): all ergodic, with n*gap from 0.2996 (Mobius ladder n 10) to 0.5 (K4).
- Cycles at q 4: n*gap = 0.350 at every even n, and odd n fall toward it.
- At q = Delta + 1, K4, Q3 and C5/C6/C9 freeze.
- PREREG99 4/4. This is small-n evidence, not asymptotics.
- Method note: vectorised enumeration of the q^n assignments plus a searchsorted transition map stays cheap up to about 2e7 assignments.
- Status: 8 of the 244 frontier rows had no move at 08:4x; T002, T004, T011, T013, T022 and T023 remain. T059's folder has no hunt.json.
- Related: [[t014_d7_percolation_tail_exponent_0p496_mean_field_2026_11_02]].

