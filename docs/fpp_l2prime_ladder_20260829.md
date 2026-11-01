# Block-resampling kurtosis ladder, 2026-08-29

Tool: `tools/fpp_l2prime_kurtosis.py` (commit 0dc317a). Law U[1,2] on the square lattice,
exact Dijkstra, one axis block of side b centred on the segment, block resampled, positive
part of the increment conditioned on the geodesic touching the block; 2,000 touched samples
per point, seed 2026, 2,000 bootstrap replicates. The read was fixed before the run:
saturation holds if the two largest points lie in [5.5, 7.0] with intervals overlapping that
band; growth if both exceed 7.5 with intervals clear of 7.0; anything else unresolved.

| b  | n   | occupation | kurtosis | 95% interval | reroute (increment > 0) |
|----|-----|-----------:|---------:|--------------|------------------------:|
| 12 | 48  | 12.4 | 6.04 | 5.38 to 6.85 | 0.51 |
| 16 | 64  | 16.5 | 5.71 | 5.19 to 6.26 | 0.50 |
| 24 | 96  | 24.8 | 5.91 | 5.37 to 6.59 | 0.50 |
| 32 | 128 | 33.1 | 5.67 | 5.19 to 6.19 | 0.48 |
| 48 | 192 | 49.8 | 6.60 | 5.86 to 7.27 | 0.49 |

Read: saturation holds at these sizes. The ladder extends the occupation range of the
2026-08-15 measurement (3.95 to 14.05) by a factor of 3.5 and stays inside the band; the
largest point is the highest and its upper interval reaches 7.27, so a longer ladder is the
next check. The reroute column counts only worsening reroutes and is not comparable to the
earlier run's figure without checking that run's definition. Nothing here bounds anything
asymptotic. Raw points: `docs/fpp_l2prime_ladder_20260829.jsonl`.
