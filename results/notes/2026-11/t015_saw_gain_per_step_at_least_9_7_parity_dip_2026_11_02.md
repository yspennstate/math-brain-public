---
name: t015_saw_gain_per_step_at_least_9_7_parity_dip_2026_11_02
description: T015 SAW: exact enumeration (d2 n20, d3 n14, d4 n11; counts = OEIS) gives E|w_n|^2/n >= 1 increasing and per-step gain >= (2d+1)/(2d-1), with an odd-n dip in the gain
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T06:02:42+04:00
  status: provisional
  evidence: "rows/T015/moves.jsonl d3e4f431"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T015 (prove E|omega_n|^2 >= c n for strict self-avoiding walk in d = 2, 3, 4), first frontier move, 2 Nov 2026, an agent. Move m015a, rows/T015/moves.jsonl d3e4f431; t015_saw_enum.c and run outputs in 06_math_research/frontier/rows/T015.

- The best proved bound is Madras 2014, E|omega_N|^2 >= N^{4/(3d)}/36. Even monotonicity of E|omega_n|^2 in n is unproved.
- Exact enumeration ran to n = 20 (d 2), 14 (d 3) and 11 (d 4). All 45 walk counts equal the OEIS b-files A001411, A001412 and A010575.
- a_n = E|omega_n|^2/n is at least 1 and strictly increasing at every computed n.
- The stronger D_n = E|omega_n|^2 - E|omega_{n-1}|^2 >= 1 also holds. Its minimum is D_2 = (2d+1)/(2d-1), that is 5/3, 7/5 and 9/7.
- D_n dips at every odd n >= 7 in every d, so a convexity proof has to split even and odd n.
- This is small-n evidence only.
- PREREG79: 3 of 3 passed.
- Same exact-count-then-check-the-statement pattern as [[t119_annealing_reaches_0p4499_cubic_independence_2026_11_02]] used for search; a first move on a row with no moves.jsonl needs the file created, see push_row.sh.


ADDENDUM (2 Nov 06:10, moves T015 m015b 4f451305 and T003 m003a d3c494a4): pivot algorithm to n = 4000 in d 2 and 3.
- Checked against the exact values first. The in-run batch-means error is about 1.6x too small, so the error bars are spreads over 4 seeds.
- R2/n keeps rising (d 2: 12.2 to 48.7; d 3: 3.13 to 5.16), and gain/n is 4 to 62. So the target holds with room at these n.
- nu from wide bases is 0.7488 (d 2), against the conjectured 3/4. d 3 gives 0.586-0.593.
- Per-doubling nu in d 2 zigzags, because one high R2 at n 2000 pushes the doubling below it up and the one above it down. So the last-doubling prediction (PREREG80 a, d 2) MISSED at 0.735; b and c passed. Use a wide base, not adjacent doublings.
- The T003 row first move records sqrt(R2)/n falling 2^{-1/4} per doubling. It was also the first live use of append.py creating a missing moves.jsonl, which worked.
