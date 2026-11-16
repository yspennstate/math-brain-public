---
name: g0013_r10_ten_blocks_22222_clean_at_cap_10_11_on_grid_2026_11_09
description: "G0013 ten-value blocks (r10): 711,168 orbits; partition 22222 positive on the whole grid at mass cap 10/11 (min +0.419), 1,022 orbits fail at the full square; interval proof only on a 200-orbit sample; full proof ~105 CPU hours"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T22:01:43+02:00
  status: provisional
  evidence: "G0013/REPORT.md; r10_audit.py"
---

G0013 round r10, worker report G0013/REPORT.md (finished 9 Nov; readback audit r10_audit.py passes, reference hashes match).

Counts: 2,829,324 indecomposable non-reversal ten-value blocks, 711,168 orbits under inverse and reverse-complement (orbit sizes 1/2/4 occur 196 / 7,380 / 703,592; an independent indecomposable recurrence agrees).

Grid scan (r7-r9 cell-integral formulas, R=10, 244 mass/position bands, all 89 compositions into 1s and 2s):
- mass cap 10/11 (the one the argument needs): partition 22222 alone is positive on every orbit; smallest margin +0.419 at block 8976543210.
- cap 0.9: also clean, smallest margin +0.744.
- full square (cap 1): 1,022 orbits / 3,582 blocks fail all 89 partitions; worst -3.418 at 8976543210, band (0,1). These are real obstructions to the family (interval dual closes all 89 negative bounds). Adding the 185 compositions that contain a 3-strip rescues all but 53 orbits (remaining_bad_three_strip.jsonl).

Interval proof: only a sample. 200 orbits (the 40 smallest grid margins plus 16 per margin decile) all closed with 22222, 25,202 boxes, smallest lower bound of F 0.000149. Not a proof for all blocks.

Cost of the full interval proof of cap 10/11: the stratified estimate is about 378,000 CPU seconds (about 105 CPU hours; 1.09M wall seconds at the sample's parallelism). Peak RSS per worker about 190 MB, so it is CPU-bound and fits the RAM gate easily. This is the next G0013 job if it is run.

How far to trust: the grid result is a float screen checked against SciPy solves (max diff 2e-12); positivity at cap 10/11 for every block is unproved until the full interval run closes. Follows the r9 memory [[g0013_r9_partition_12222_fails_on_full_square_n_ge_10_only_2026_11_07]] and [[g0013_every_permutation_n_le_10_proved_exact_certificate_2026_11_08]]: 12222 failed only on the full square, and here too the failures sit at cap 1.

