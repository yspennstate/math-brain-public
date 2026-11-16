---
name: t016_dla_block_jumps_lower_beta_0p589_to_0p604_relaunch_innocent_2026_11_03
description: [PROVISIONAL] T016: row DLA's 8x8 block jumps lower beta 0.589 -> 0.604 when off (3.4 se, 3 seeds); uniform relaunch innocent; c4 anisotropy already 0.4 at 256k; switch approximations off one at a time
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T06:40:51+04:00
  status: provisional
  evidence: "the private repository, rows/T016/reviews_agent/ADDENDUM_T016_1.md"
---

When a numerical exponent disagrees between two simulation codes, switch each approximation off one at a time in the faster code, rather than arguing from what each approximation should do.

T016 (3 Nov review of m016a, planar on-lattice DLA): the row's t016_dla.c gave Rg beta 0.5886 +- 0.0032 over n 32k-256k (8 seeds), and my exact-step dla2.c gave 0.5992 +- 0.0029 (18 seeds). The obvious suspect was the uniform relaunch at the box edge, which is only 2.9 Rmax away at n 256k and catches 15-16 percent of walkers. With exact Poisson-kernel return it gave 0.5882 +- 0.0041, no change. Switching off the radius-7 jumps inside empty 8x8 blocks, which look harmless as an exact Brownian exit law, gave 0.6042 +- 0.0032 (3 seeds, 3.4 se from the row) and restored the rising per-doubling exponent of the exact code. Mechanism not found.

Second point: c4 = <cos 4 theta> over the outer half of the cluster rises to 0.40-0.47 at n 256k, so square-lattice anisotropy is already strong at 10^5 particles, though the row assumed it lies far beyond.

How to apply: build a mode switch into a copy of the code under review (mode 0 = unchanged and reproducing the row), run equal seeds per mode, and report the shift per approximation with seed-spread errors.

Evidence: the private repository, rows/T016/reviews_agent/ADDENDUM_T016_1.md, diag_1.txt, row_diag.c.
Related: [[rerun_the_outlier_point_long_t015_miss_was_n2000_t002_gap_chance_2026_11_03]] - same review round; [[bound_rigor_marks_and_best_seen_bias_t119_2026_11_03]] - same round, the T119 lessons.


Final (addendum 2, pushed 3 Nov 07:01, move on T016): all seeds in. Block jumps off 0.6042 +- 0.0043 (8 seeds), row code 0.5886 +- 0.0032 (8), exact dla2 0.5968 +- 0.0024 (24); jumps lower beta by 0.0156 +- 0.0054 (2.9 se). With all seeds mode 2 is flat near 0.60 per doubling (0.600, 0.608, 0.604, 0.600 from 16k) and only dla2 rises (to 0.603). c4 at 256k is 0.40-0.47 on every code, so anisotropy does not separate them: the addendum-1 link between c4 and the higher exact-code beta is withdrawn. Lesson: the 3-seed reading (same rise as dla2) did not survive 8 seeds; quote per-doubling shapes only at full seed count.

Addendum 3 (pushed 3 Nov 07:39, move on T016, 24 seeds each): the block jump's own law is innocent too. Drawing it from the exact SRW exit law of the radius-7 disk (mode 3) gives 0.5861 +- 0.0024, the row code 0.5911 +- 0.0025 (= row's 0.5909). Moving the rounded far jump out from Rmax+4 to Rmax+20 (mode 4) gives 0.5990 +- 0.0026: 3.6 se up, 0.6 se from exact dla2 0.5968, rising per doubling like dla2. No-jump mode 2 also keeps far jumps from Rmax+4 and is high (0.6052, 12 seeds), so the bias needs both: block jumps landing up to 7 sites past Rmax+4, then the far jump from there. Why is open. Method that found it: switch one approximation at a time with a written decision rule; 1.5 s per seed made 24-seed groups cheap.
Final mode 2 (24 seeds, pushed 3 Nov 07:59): 0.5986 +- 0.0028; the 8-seed 0.6042 was partly fluctuation. Exact-near-tips codes (mode 2, mode 4, dla2) 0.597-0.599; jump-scheme codes (modes 0, 1, 3) 0.586-0.591.
