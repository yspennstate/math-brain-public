---
name: p0108_thin_cylinder_fpp_clt_width_open_chatterjee_dey_1_over_d_plus_1_2026_11_13
description: "[PROVISIONAL] P0108 thin-cylinder FPP CLT (ADH Q20): sharp width exponent open; proved below 1/(d+1) (Chatterjee-Dey PTRF 2013), conditionally up to the transversal exponent in d=2,3"
metadata:
  type: project
status: provisional
---
P0108 (200 list rank 14; Auffinger-Damron-Hanson "50 years of FPP", Question 20, arXiv 1511.03262 p.72): find the largest
alpha such that passage times across [0,n] x [-n^alpha, n^alpha]^(d-1), centred and scaled, have a standard normal limit.

Status 13 Nov 2026: OPEN. Best proved: Chatterjee-Dey, "Central limit theorem for first-passage percolation time across thin
cylinders", PTRF 156 (2013) 613-663, arXiv 0911.5702: CLT for h_n = o(n^(1/(d+1))). Under a (2+delta) moment only, ADH state
the exponent as 1/(d+1+2(d-1)/delta). Chatterjee-Dey also show, ASSUMING the fluctuation and transversal exponents exist and
the limit shape is strictly convex in e_1, that in d = 2, 3 the CLT holds up to the unrestricted geodesic's width n^xi
(conjecturally xi = 2/3 in d = 2), so the expected answer is alpha = xi. Two extended searches (13 Nov) found no
unconditional improvement; Alexander arXiv 2011.07223 gives uniform concentration and wandering bounds in cylinders but no CLT
width. A 2026 hop-count CLT on spread-out line graphs (arXiv 2607.28865) uses the Chatterjee-Dey method without changing alpha.

Why it is hard: an unconditional sharp threshold would pin down the transversal exponent xi, which is open in every d >= 2.
A realistic target is an unconditional improvement of 1/(d+1) (the block argument loses in how it counts independent slabs),
not the sharp value.

How to apply: skip as a solve target unless a concrete idea beats the slab count; cite Chatterjee-Dey with the moment caveat.
Related: [[p0107_critical_fpp_z3_log_n_open_needs_theta_pc_zero_2026_11_13]], [[p0098_strict_fpp_comparison_large_atom_d_ge_3_open_marchand_d2_2026_11_13]].

Numerics, 14 Nov 00:10 (an agent, workstation CUDA, iid Exp(1) site weights, periodic width W = n^a, line-to-line passage
time across n columns, Bellman-Ford to the fixed point; Monte Carlo evidence, not a proof). n = 256, 512, 1024; a = 0.33 ..
0.85; 67-512 samples a cell (table: ~/gpu_work/p0108_fpp/fpp_agg_cuda_20261114_0010.txt). Standardized skewness
is within about one se of 0 for every a <= 0.667 at every n (largest |skew| 0.143, se 0.158); at a = 0.75 and 0.85 it turns
negative, -0.21 to -0.37 (2-3 se at n = 256, 512; n = 1024 too thin to resolve), the sign and size of a minus-Tracy-Widom
limit (GOE skew 0.29). Consistent with the conjectured threshold 2/3, but the data cannot separate 0.6 from 0.667. The sd
growth per doubling of n sits 0.05-0.08 below the KPZ heuristic n^(1/2 - a/4), so finite-size effects are still large at
n <= 1024. The run continues to n = 2048 and a = 1.0 (4 h budget from 20:44); re-aggregate with fpp_agg.py.


Update 14 Nov 00:47 (n = 2048 cells, 126-512 samples): skew +0.20 (1.8 se) at a = 0.33, -0.18 (1.2 se) at a = 0.5, -0.24 (1.1 se) at a = 0.6 - noisy, none decisive, and no cell yet for a >= 0.667 at n = 2048. The reading above stands. Rows, table, code and README on GitHub: the private repository, 06_math_research/p0108_fpp_agent/ (table fpp_agg_cuda_20261114_0047.txt). Next useful step: more samples at n = 2048 for a = 0.6, 0.667, 0.75 (the only cells that can move the threshold reading).


Update 14 Nov 03:43 (b3c629f8, table fpp_agg_cuda_20261114_0343.txt in 06_math_research/p0108_fpp_agent): a = 0.33 skew within 2 se of zero at every n; a >= 0.667 negative at every n and not shrinking (a = 0.667: -0.16, -0.13, -0.13, -0.54 at n = 256..2048, the last 3.8 se on 300 samples). Open cell: a = 0.5 at n = 2048 is -0.25 (3.4 se, 1,092 samples) against -0.07 at n = 1024; W = 45 << n^(2/3) = 161, so a late Gaussian limit is the likely reading. To decide: more n = 2048 samples at a = 0.5 and an n = 4096 run. The worker machine 2 MLX copy of this job was withdrawn (workstation CUDA covers it). Evidence, not proof.


Update 14 Nov 18:03 (three machines merged, 1,490 rows; table fpp_agg_all_20261114_1803.txt in 06_math_research/p0108_fpp_agent): the a = 0.5 n = 2048 outlier is gone (16,107 samples, skew -0.034, 1.8 se; n = 4096 -0.058, 1.9 se), so a = 0.5 looks Gaussian. a = 0.667 sits at -0.13 to -0.18 for every n (256..4096); a >= 0.75 at -0.20 to -0.41. The only cell still moving is a = 0.6: -0.02, -0.07, -0.08, -0.11 for n = 256..2048 (4.5 se), growing; W/n^(2/3) = n^(-1/15) shrinks slowly, so this is the expected crossover, not yet evidence against 2/3. Next useful run: a = 0.6 at n = 4096 and 8192 with >= 2,000 samples (n = 4096 has 184). Evidence, not proof.


Update 14 Nov 22:26 (an agent; 2,256 rows from three machines, table fpp_agg_all_20261114_2216.txt in 06_math_research/p0108_fpp_agent): the a = 0.6 cell has stopped growing. At n = 4096 it is -0.105 (se 0.022, 12,437 samples) against -0.112 (0.025) at n = 2048. The block heuristic predicts exactly this: a cylinder of width W = n^a holds about n / W^(3/2) = n^(1 - 3a/2) independent blocks, so the skew should fall like n^(-(1 - 3a/2)/2), a factor 0.966 per doubling at a = 0.6. That is invisible at any feasible n (a twofold drop needs n near 2^20). More samples at fixed a = 0.6 cannot separate 0.6 from 2/3, so that line is closed. The sharper test is a scaling collapse: with W = c n^(2/3), the skew should depend on c alone if n^(2/3) is the transversal scale. That run is job 49 on Mac 1 (c = 0.5, 1, 2; n = 512 to 4096; rows fpp_rows_mac1_collapse.jsonl; script fpp_cyl_c.py).
