# First-passage percolation across thin cylinders: numerics for the CLT width

## The question

Auffinger, Damron and Hanson, *50 years of first-passage percolation* (AMS University Lecture Series 68, 2017;
arXiv:1511.03262), Question 20: find the largest alpha such that the passage time across the cylinder
[0, n] x [-n^alpha, n^alpha]^(d-1), centred and scaled, has a standard normal limit.

## What is known

Chatterjee and Dey, *Central limit theorem for first-passage percolation time across thin cylinders*, Probab. Theory
Relat. Fields 156 (2013) 613-663 (arXiv:0911.5702), prove the CLT for widths h_n = o(n^(1/(d+1))). Under only a
(2 + delta) moment, Auffinger, Damron and Hanson state the exponent as 1/(d + 1 + 2(d - 1)/delta). Chatterjee and Dey
also show that, if the fluctuation and transversal exponents exist and the limit shape is strictly convex in the
direction e_1, the CLT holds in d = 2, 3 up to the width n^xi of an unrestricted geodesic. In d = 2 the KPZ prediction
is xi = 2/3, so the expected answer there is alpha = 2/3. Alexander (arXiv:2011.07223) proves uniform concentration and
wandering bounds inside cylinders but no CLT width. The question is open; an unconditional sharp threshold would
determine xi, which is open in every d >= 2.

Above the threshold the passage time should behave like a last-passage time in a wide strip, whose fluctuations in
the KPZ class follow Tracy-Widom laws. For the minimum, the limit is a negated Tracy-Widom law, so the skewness is
negative (the GOE value is 0.29 in absolute value). Below the threshold the cylinder splits into many nearly
independent blocks and the skewness should vanish. That sign change is what these runs measure.

## What was computed

All runs are on Z_W x {0, ..., n - 1} with periodic width W, iid Exp(1) site weights, and line-to-line passage time
from column 0 to column n - 1, solved by Bellman-Ford iterated to its fixed point. The same solver runs on an NVIDIA GPU
(`fpp_cyl_cuda.py`, PyTorch) and on an Apple GPU (`fpp_cyl.py`, MLX); `fpp_cyl_cuda.py --check` compares a small case
with an exact CPU Dijkstra. These are Monte Carlo estimates, not proofs.

1. **Width W = n^a**, a from 0.33 to 1.0, n from 256 to 4096 (`fpp_agg_all_20261114_2216.txt`, 2,256 rows from three
   machines, merged by `fpp_merge.py` and summarized by `fpp_agg.py`). For a = 0.5 the skewness is about zero at every
   n (n = 2048: -0.034, 1.8 se, 16,107 samples). For a = 2/3 it sits at -0.13 to -0.18 for every n, and for a >= 0.75 at
   -0.20 to -0.41. At a = 0.6 the skewness stops growing in magnitude: -0.105 (se 0.022) at n = 4096 against -0.112
   (0.025) at n = 2048.
2. **Why more samples at a = 0.6 cannot decide 0.6 against 2/3.** A cylinder of width W holds about n / W^(3/2)
   independent blocks, so below the threshold the skewness should decay like n^(-(1 - 3a/2)/2). At a = 0.6 that is a
   factor of 0.966 per doubling of n, which no feasible n can resolve.
3. **Scaling collapse** (`fpp_cyl_c.py`, `collapse_agg.py`, table `collapse_table.txt`, rows `fpp_rows_mac1_collapse*.jsonl`,
   `fpp_rows_mac2_collapse_n2048.jsonl` and `fpp_rows_cuda_collapse_n4096.jsonl`). If the transversal scale is n^(2/3), then with W = c n^(2/3) the skewness
   should depend on c alone. For n = 1024, 2048 and 4096 it reads -0.13, -0.12, -0.10 at c = 0.5 (se 0.03 to 0.05),
   -0.19, -0.12, -0.18 at c = 1 (se 0.04 to 0.07) and -0.30, -0.27, -0.43 at c = 2 (se 0.05 to 0.10). Within each c the
   values agree to about two standard errors and do not drift with n; across c they move from about -0.1 at c = 0.5 to -0.3 to
   -0.4 (c = 4 has 20 to 64 samples and is only negative). The value off the pattern is c = 0.5 at n = 512 (-0.006).
   This also accounts for item 1: at a = 0.6, c = n^(-1/15) falls only from 0.69 to 0.57 between n = 256 and 4096, so
   those cells stay in the c = 0.5 to 1 band. The test has a limit: if the true scale were n^b, the effective c would
   drift by 4^(2/3 - b) between n = 1024 and 4096, 10 percent for b = 0.6, which is too small to see here. The collapse
   supports a scale near n^(2/3) but fixes the exponent only to about 0.6 to 0.73.

4. **Collapse at n = 8192 and 16384** (`fpp_cyl_k.py`, rows `fpp_rows_mac2_n8192k.jsonl` and
   `fpp_rows_mac2_n8192k_b2.jsonl` at n = 8192; `fpp_rows_mac1_n16384k.jsonl`, `fpp_rows_mac1_n16384k_b2.jsonl`,
   `_b3`, `_b5`, `fpp_rows_mac2_n16384k_b4.jsonl` and `_b6` at n = 16384; table
   `collapse_table_n8192_16384_20261117.txt`). `fpp_cyl_k.py` does the relaxation step as one Metal kernel; its
   `--selftest` gives passage times bit-identical to `fpp_cyl_c.py`, and it holds far fewer arrays in memory at once,
   which is what made these sizes fit. At n = 8192 the skewness is -0.135 (se 0.085, 840 samples) at c = 0.5, -0.235
   (0.074, 1092) at c = 1 and -0.292 (0.114, 465) at c = 2, each within about one standard error of the n = 4096 value
   for the same c. At n = 16384 it is -0.235 (0.075, 1064), -0.168 (0.093, 692) and -0.127 (0.132, 346). The passage
   times of one row share a random key, so the table also gives a bootstrap that resamples whole rows; its standard
   errors (0.085, 0.094 and 0.124 at n = 16384) are close to sqrt(6/N). Every cell is negative, and at each c the
   n = 8192 and n = 16384 values differ by about one combined standard error or less. At n = 16384 the cells are not
   ordered by c as they are at n = 8192, so the ordering is not a stable feature at these sizes. The six n = 16384
   batches have independent seeds and agree in mean and spread at each c: the mean passage time is 7524.7 to 7526.9
   at c = 0.5, 7511.1 to 7514.2 at c = 1 and 7502.6 to 7505.1 at c = 2.

The data are consistent with a threshold at 2/3 and with n^(2/3) as the transversal scale. They cannot separate 2/3
from nearby exponents, because finite-size corrections are large at n <= 4096: the growth of the standard deviation
per doubling of n sits 0.05 to 0.08 below the KPZ heuristic n^(1/2 - a/4).

## Files

- `fpp_cyl.py`, `fpp_cyl_cuda.py`, `fpp_cyl_c.py`, `fpp_cyl_k.py`: samplers (W = n^a, the CUDA port, W = c n^(2/3), and the
  same with a Metal relaxation kernel).
  Environment: `FPP_NS`, `FPP_AS` or `FPP_CS`, `FPP_ELEMS`; a file `STOP` in the working directory ends a run.
- `fpp_merge.py`, `fpp_agg.py`, `collapse_agg.py`, `followon_a06.py`: merging and summary scripts.
- `fpp_rows_*.jsonl`: raw rows. Each row holds n, a or c, W, the batch of passage times T and the seed.
  `fpp_rows_mac1_n16384k_interim_20261116.jsonl` is the first 77 rows of `fpp_rows_mac1_n16384k.jsonl`; leave it
  out of any merge.
  `fpp_rows_mac1_n16384k_b3.jsonl` is a run of 25 rows that ended early; its rows are complete and are pooled.

## Credits

The question and its framing are due to Auffinger, Damron and Hanson. The proved range and the conditional sharp
answer are due to Chatterjee and Dey, whose block decomposition also gives the block-count heuristic in item 2. The
negated Tracy-Widom prediction above the threshold rests on the KPZ scaling theory for growth models (Kardar, Parisi
and Zhang, Phys. Rev. Lett. 56, 1986) and on the exactly solvable last-passage models: Johansson (Comm. Math. Phys.
209, 2000) for the GUE law in the point-to-point case, and Baik and Rains (2001) for the GOE law in the point-to-line
case, the one closest to the flat ends used here.
