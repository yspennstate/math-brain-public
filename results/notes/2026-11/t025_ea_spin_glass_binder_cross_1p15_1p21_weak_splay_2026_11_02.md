---
name: t025_ea_spin_glass_binder_cross_1p15_1p21_weak_splay_2026_11_02
description: T025 3D +-J spin glass, PT, L 4/6/8: Binder g crossings at T 1.153 and 1.214 (lit. T_c 1.12-1.14); below T_c g splays only 2.1 se, so xi/L is the needed probe; PREREG95 4/4 but weak
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T08:15:59+04:00
  status: provisional
  evidence: "rows/T025/moves.jsonl acf0a2da"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T025 (positive-temperature nonzero overlap, 3D short-range spin glass), first frontier move, 2 Nov 2026, an agent. m025a is in rows/T025/moves.jsonl (acf0a2da); the code is t025_sg.c in 06_math_research/frontier/rows/T025.

- Setup: +-J EA model, L 4/6/8 with 2000/1500/1002 disorder samples, parallel tempering over 12 temperatures from 0.9 to 1.6, 2 replicas.
- The Binder g crossings are 1.153 (L4/L6) and 1.214 (L6/L8), near the literature T_c of 1.12-1.14.
- Below T_c the curves barely splay. At T 0.9, g goes 0.816 -> 0.821 -> 0.828, only 2.1 se from L 4 to 8. Above T_c g falls fast: 0.526 -> 0.389 at T 1.6.
- Equilibration: the half and quarter windows agree within 0.0007.
- PREREG95 4/4, but (a) and (b) are weak. LESSON: in 3D spin glasses g is a marginal probe; use xi/L. Run 2 adds xi/L (t025_sgxi.c), pre-registered as PREREG96.
- Harness: the backslash guard bit again. A heredoc Python builder that matched a C printf with a double-escaped newline failed its assert. Builders that carry backslashes go through the Write tool.
- Related: [[t028_ising_interface_rough_k0p30_to_0p40_smooth_0p45_2026_11_02]].


Addendum (2 Nov, m025b, moves.jsonl f11279df): xi/L on fresh disorder (2000/1500/1002 samples) crosses at T 1.133 (L4/6) and 1.174 (L6/8). At T 0.9 it grows with L, 0.771 -> 0.792 -> 0.828, a 4.5 se rise from L4 to L8. On the same samples g is 0.8206, 0.8203, 0.8262, not monotone. PREREG96 4/4. This confirms the lesson: xi/L, not g, is the probe for 3D spin glasses.
