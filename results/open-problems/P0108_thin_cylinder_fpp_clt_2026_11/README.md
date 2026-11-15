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
3. **Scaling collapse** (`fpp_cyl_c.py`, `collapse_agg.py`, table `collapse_table.txt`). If the transversal scale is
   n^(2/3), then with W = c n^(2/3) the skewness should depend on c alone. At n = 512 and 1024 it does for c = 1
   (-0.206 and -0.187) and c = 2 (-0.287 and -0.296), within one standard error, and it grows in magnitude with c:
   about 0 at c = 0.25 and -0.5 at c = 4. At c = 0.5 the two values differ by about 2.4 se (-0.006 and -0.133). The
   cells at n = 2048 and 4096 have too few samples to test the collapse. The c = 0.25 and c = 4 run ended early.

The data are consistent with a threshold at 2/3 and with n^(2/3) as the transversal scale. They cannot separate 2/3
from nearby exponents, because finite-size corrections are large at n <= 4096: the growth of the standard deviation
per doubling of n sits 0.05 to 0.08 below the KPZ heuristic n^(1/2 - a/4).

## Files

- `fpp_cyl.py`, `fpp_cyl_cuda.py`, `fpp_cyl_c.py`: samplers (W = n^a, the CUDA port, and W = c n^(2/3)).
  Environment: `FPP_NS`, `FPP_AS` or `FPP_CS`, `FPP_ELEMS`; a file `STOP` in the working directory ends a run.
- `fpp_merge.py`, `fpp_agg.py`, `collapse_agg.py`, `followon_a06.py`: merging and summary scripts.
- `fpp_rows_*.jsonl`: raw rows. Each row holds n, a or c, W, the batch of passage times T and the seed.

## Credits

The question and its framing are due to Auffinger, Damron and Hanson. The proved range and the conditional sharp
answer are due to Chatterjee and Dey, whose block decomposition also gives the block-count heuristic in item 2. The
negated Tracy-Widom prediction above the threshold rests on the KPZ scaling theory for growth models (Kardar, Parisi
and Zhang, Phys. Rev. Lett. 56, 1986) and on the exactly solvable last-passage models: Johansson (Comm. Math. Phys.
209, 2000) for the GUE law in the point-to-point case, and Baik and Rains (2001) for the GOE law in the point-to-line
case, the one closest to the flat ends used here.
