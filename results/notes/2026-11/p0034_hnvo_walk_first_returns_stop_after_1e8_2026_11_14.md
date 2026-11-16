---
name: p0034_hnvo_walk_first_returns_stop_after_1e8_2026_11_14
description: "[PROVISIONAL] P0034 (Lyons-Peres Q2.27 horizontal-new/vertical-old walk) recurrent? 1400 walks to 1e9: range t/(0.065 ln^2 t); P(no return) 0.355->0.256, 3.5-7%/decade first returns, undecided; returns come only via column-0 entries near height 0; a '0 of 103' stop did not replicate; proved: origin recurrent only if the column-0 run around it grows without bound (15 Nov)"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-14T23:28:40.200Z
---

P0034, the planar walk that steps horizontally at a first visit and vertically at a repeat visit (Lyons-Peres Q2.27). 14 Nov 2026, an agent.

- 1400 walks to 10^9 (hnvo_hash.c, about 10^8 steps/s, 50 walks to 10^9 in ~10 min per core on a worker machine). t/E R_t/(ln t)^2 = 0.063-0.068 from 10^4 to 10^9: range ~ t/(0.065 ln^2 t).
- P(no return to 0 by t): 0.355, 0.330, 0.313, 0.291, 0.280, 0.265, 0.256 at 10^3..10^9. First returns per decade among the not-yet-returned: 0.071, 0.050, 0.071, 0.037, 0.054, 0.035. Fits (ln t)^-1/3 and t^-0.026 equally; recurrence undecided by numerics.
- SCAR, same day: the first batch (394 walks) had 0 of 101 first returns in [10^8, 10^9], which looked like a hard stop with p ~ 1e-3; I wrote it into NOTE.md and pushed it before replicating. The other 1000 walks gave 13 of 269. Replicate a surprising zero before writing a mechanism around it.
- Mechanism to aim a proof at: in old territory the walk moves only vertically, so column changes happen at column tips; a return needs an entry into column 0 from a fresh site in column +-1 and a vertical excursion to height 0 inside column 0's visited interval. hnvo_col0.c logs column-0 entries, near-height-0 entries and extent (same path as hnvo_hash.c on the same seed, checked on worker machine 1). Measured on 400 walks: every first return came in a decade with a column-0 entry at |y| <= 10 (30 of 104 such decades; 0 of 630 decades without one); near-entry chance 0.07-0.09 per decade from 10^6 on, while all column-0 entries grow like t^0.45 at the tips (8.6 expected near 0 if spread evenly at 10^8, 0.59 seen). Recurrence = are near entries summable, i.e. are the holes in columns +-1 near height 0 filled at a summable rate.
- Files: 12_cognitive_architecture/math/trio_1011/op/P0034/ (NOTE.md, STATUS.md, decades.py, analyze.py, hnvo_hash.c, hnvo_col0.c, col0_stats.py, data/n1e9_*.tsv, data/c1e9_*.tsv).

- 15 Nov: the seed 23/24 files had been copied mid-run (49 and 45 walks); complete files pushed, NOTE table recomputed on 1400 walks (changes in the third decimal; the batch was 400 walks, 0 of 103). PROVED (NOTE item 4): with [a_t,b_t] the run of visited column-0 sites containing 0, the walk steps onto an old run site from outside only by a horizontal step from a hole (unvisited (+-1,y), a<=y<=b) at its first visit; inside, it is a simple walk on [a,b] until it steps onto a fresh end neighbour, so every excursion lengthens the run and each hole opens at most one. Bounded run => finitely many visits to 0. hnvo_holes.c, 200 walks to 1e9 (worker machine 1): no return in any of 3446 intervals with the run unchanged; runs growing per decade 37, 34, 24, 17, 13, 7 of 200 (about x0.7 a decade, summable if it continues); median run width 10 at 1e9, about 5-6 holes sitting unused. Commits a12473f6, 2b36e9f6; the data lives only on GitHub now (op/P0034/data).

What would change this: a proof that the per-decade first-return rate is bounded below (recurrent origin) or summable, or a proof that the column-0 run around the origin stays bounded (transient origin).
