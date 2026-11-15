# P0108: first-passage percolation on thin cylinders, Monte Carlo

Problem (Auffinger-Damron-Hanson, 50 years of FPP, Question 20): for site FPP with Exp(1) weights on the
cylinder [0,n] x (Z mod W), W = n^a, for which a does the point-to-line passage time satisfy a Gaussian CLT?
Chatterjee-Dey prove it for a < 1/(d+1) = 1/3 in d = 2; the conjectured threshold is 2/3.

Files: `fpp_cyl_cuda.py` (CUDA Bellman-Ford, periodic width, one row per (n, a) cell),
`fpp_agg.py` (pools rows into the table), `fpp_rows_cuda.jsonl` (raw passage times),
`fpp_agg_cuda_20261114_0047.txt` (table: mean/n, sd, skewness and excess kurtosis with standard errors).

Reading at 14 Nov 00:47 (laptop RTX run, n = 256..2048): skewness is within about one standard error of zero
for a <= 0.667 at n = 256, 512, 1024, and negative (-0.21 to -0.37) at a = 0.75 and 0.85, the sign expected
in the KPZ regime. At n = 2048 the cells are small (126-512 samples) and noisy: +0.20 (1.8 se) at a = 0.33,
-0.18 and -0.24 (about 1.2 se) at a = 0.5 and 0.6. Consistent with a threshold at 2/3; the data cannot separate
0.6 from 0.667. Evidence, not proof.

Reading at 14 Nov 03:43 (`fpp_agg_cuda_20261114_0343.txt`, same run, more samples; `fpp_agg_cuda_20261114_0145.txt` is the
table between). At a = 0.33 the skewness stays within two standard errors of zero at every n (+0.03, -0.02, +0.04,
+0.10). At a >= 0.667 it is negative at every n and does not shrink as n grows: at a = 0.667, -0.16, -0.13, -0.13 and
-0.54 (3.8 se at n = 2048, 300 samples); at a = 0.85, -0.26 to -0.42. The cell that does not fit a clean threshold
is a = 0.5 at n = 2048, -0.25 (3.4 se, 1,092 samples), against -0.07 (1.5 se) at n = 1024. At a = 0.5 the width
W = 45 is well under the transversal scale n^(2/3) = 161, so the Gaussian limit may simply arrive late there; more
samples at n = 2048 and a run at n = 4096 would tell the two readings apart. Evidence, not proof.

Reading at 14 Nov 18:03 (`fpp_agg_all_20261114_1803.txt`), three machines merged: the laptop CUDA rows
(`fpp_rows_cuda.jsonl`), Mac 1 at n = 4096 (`fpp_rows_mac1_n4096.jsonl`) and Mac 2 at a = 0.75, 0.85 for n = 1024, 2048
(`fpp_rows_mac2_wide.jsonl`); 1,490 rows in all, none capped. The a = 0.5 cell at n = 2048 that looked out of place at
03:43 now has 16,107 samples and reads -0.034 (1.8 se); at n = 4096 it is -0.058 (1.9 se, 6,432 samples). So at a = 0.5
the skewness is small at every n and does not grow, which is what a Gaussian limit predicts. At a = 0.667 it is -0.13 to
-0.18 at every n from 256 to 4096 (5 se at n = 2048), and at a = 0.75 and 0.85 it is -0.20 to -0.41, larger in
magnitude at larger n for a = 0.85. The cell between is a = 0.6: -0.017, -0.065, -0.079, -0.112 for n = 256 to 2048 (the
last 4.5 se), growing in magnitude. A threshold at 2/3 predicts this cell turns Gaussian eventually, but W/n^(2/3) =
n^(-1/15) shrinks very slowly (0.60 at n = 2048), so at these sizes a = 0.6 still sits in the crossover. n = 4096 at
a = 0.6 has only 184 samples (the Mac 1 job ran with a small memory budget) and cannot tell. The open question the data
can still move: does the a = 0.6 skewness turn back toward zero by n = 8192? Evidence, not proof.
- 22:26 14 Nov: a = 0.6 at n = 4096 is -0.105 (0.022), flat against n = 2048; see fpp_agg_all_20261114_2216.txt. Collapse test W = c n^(2/3) queued as job 49 on Mac 1.

Scaling collapse, 15 Nov 10:5x (`collapse_table_1115.txt`, from `collapse_agg.py` over the Mac 1 collapse rows, the Mac 1
n = 2048 rows in `runs_1115/` and the laptop CUDA n = 4096 rows in `runs_1115/`; the laptop run was still adding rows).
Widths W = c n^(2/3). If n^(2/3) is the transversal scale, the skewness at fixed c should not move with n. For n = 1024,
2048, 4096 it reads: c = 0.5, -0.13, -0.08, -0.11 (se 0.03-0.05); c = 1, -0.19, -0.08, -0.18 (se 0.05-0.07); c = 2,
-0.30, -0.27, -0.43 (se 0.07-0.10). Within each c the values agree to about two standard errors and show no drift with n,
while across c they move steadily, from near zero toward -0.3 to -0.4 as c grows (c = 4 has 20-64 samples and only says
negative). The one value off the pattern is c = 0.5 at n = 512 (-0.006), which is small n. So the skewness behaves as a
function of W/n^(2/3) alone, which is what the 2/3 threshold predicts, and it suggests why a = 0.6 looked stuck at
about -0.1: there c = n^(-1/15) moves from 0.69 to 0.57 between n = 256 and 4096, too little to leave the c = 0.5-1 band.
Job 49 on Mac 1 ended rc 137 (killed under memory pressure on a loaded queue) after every cell had 14-15 batches.
The limit of the test: if the true scale were n^b, the effective c would drift by a factor 4^(2/3-b) between n = 1024 and
4096, which is 10 pct for b = 0.6. Against the spread between c = 0.5 and c = 1 that drift is too small to see, so the
collapse supports a scale near n^(2/3) but cannot fix the exponent closer than about 0.6-0.73. Evidence, not proof.

Final collapse table, 16 Nov 01:1x (`runs_1115/collapse_c12_final.txt`, all rows of the three `runs_1115` collapse files;
the laptop CUDA run for c = 1, 2 finished with 1715 rows). Skewness with standard error, n = 2048 then 4096:
c = 0.5, -0.072 (0.047) and -0.114 (0.028); c = 1, -0.189 (0.022) and -0.181 (0.029); c = 2, -0.277 (0.032) and
-0.356 (0.041). At fixed c the two sizes differ by 0.8, 0.2 and 1.5 standard errors of the difference; from c = 0.5 to
c = 2 the skewness moves by 0.21 at n = 2048 and 0.24 at n = 4096, which is 3.6 and 4.9 standard errors. The larger samples sharpen the earlier reading
without changing it: the skewness is a function of W/n^(2/3) to the precision available, and the exponent bracket
0.6-0.73 above stands.

## Files and credit

The simulation code is `fpp_cyl.py` (reference), `fpp_cyl_c.py` (compiled inner loop) and `fpp_cyl_cuda.py`
(GPU batches); `fpp_agg.py` and `collapse_agg.py` pool the rows into the tables, `fpp_merge.py` merges rows from
several machines. The `fpp_agg_*` and `collapse_table*` files are the tables quoted above, in time order. The
largest raw file, `fpp_rows_cuda.jsonl`, is over the size limit for this repository and is not included; the other
row files are. Nothing here is a proof.

The question and the proved range a < 1/3 in two dimensions are due to Chatterjee and Dey ("Central limit theorem
for first-passage percolation time across thin cylinders"). The 2/3 threshold is the transversal fluctuation
exponent of the Kardar-Parisi-Zhang class, and the skewness test follows the scaling-collapse practice of that
literature; first-passage percolation itself goes back to Hammersley and Welsh, with the basic theory due to Kesten.
