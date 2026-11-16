---
name: t340_linear_bn_width_floor_exact_n_n1_over_2n1_per_mode_2026_11_01
description: T340 linear centered-BN width floor exact? N E|mode|^2 -> dim_mode n(n+1)/(2(n-1)) (n 32: 528/7903); chain to N 16384 hits 1.0003; dossier 5pct gap = mean shift
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T12:48:16+04:00
  status: verified
  evidence: "06_math_research/frontier/rows/T340 m340a, bn_linear_exact_n32.txt"
  modified: 2026-11-01T08:57:02.474Z
---

T340 (centered batch norm, width-N floor of the batch Gram), 1 Nov 2026, an agent. For a LINEAR network the floor constant
is exact and needs no Monte Carlo. At the fixed point P* = (n/(n-1)) P the BN rows are sqrt(n) u, u uniform on the sphere of 1-perp
(m = n-1). Its fourth moments are isotropic on trace-free symmetric matrices, E[(u'Du)^2] = 2|D|^2/(m(m+2)), and both modes contract
at m/(m+2), so N E|proj_mode(C - P*)|_F^2 -> dim_mode * n(n+1)/(2(n-1)), with dim_std = n-1 and dim_(n-2,2) = n(n-3)/2. That gives
36.00 / 102.86 at n 8 and 528.0 / 7903.0 at n 32.

Check: bn_linear_exact.py simulates the exact reduction. For a linear net G_(l+1) = C_l, so the next N rows are iid N(0, C_l) and no
N x N weight matrix is needed (4 widths up to 16384 in 120 s). At n 32 the (n-2,2) ratio to 7903 is 1.064 / 1.015 / 1.009 / 1.0003
(+-0.0009) at N 256 / 1024 / 4096 / 16384.

Two things this settled from the 18 Oct dossier:
- The "linear residual not shrinking" was the old closed form's Monte Carlo error.
- At N 256 the 5 pct gap between E|C - P*|^2 (8406) and the dossier's floor (8022) is the squared stationary-mean shift
  (N |mean C - P*|^2 = 427). The dossier's floors are variances about the sample mean. From N 1024 on, the remaining mean term (about
  30) is the sample mean's own noise, Var (1+lambda)/((1-lambda) L).
  CORRECTED 1 Nov (move m340b, same author): the second bullet is wrong. By S_n symmetry with tr C = n and C 1 = 0 the stationary
  mean of C is exactly P*, so there is no mean shift. At n 32, N 256 the chain has a slow component (block-mean cosine 0.49 against
  0.005 at N 1024; lag-512 autocorrelation 0.067 where AR(1) gives 0), and the sample mean absorbs a run-length-dependent part of it:
  the sample-mean term is 833 at 1,400 layers and 354 at 32,000, the variance 7566 and 8101 (bn_linear_exact_n32_L1400_seeds.txt,
  _L32k_split.txt). The dossier's short row (7497) is inside the 1,400-layer seed spread (z -1.2). The exact constant and the
  convergence at large N (where the chain is AR(1)) stand.
  ADDED 1 Nov (move m340c): the slow component is RANK COLLAPSE. Range(C_(l+1)) lies in range(C_l), so a direction whose eigenvalue
  reaches machine zero never returns. At n 32 the rank on 1-perp falls 31 -> 20 by layer 3000 at N 128, loses one at layer 6065 at
  N 256 (seed 7 collapsed early: bottom eigenvalue at 1e-15 in 99 pct of layers), and stays 31 for 10,000 layers at N >= 384
  (bn_linear_rank_n32.txt). One lost direction is an offset of about N (n/(n-1))^2 = 273, the persistent block mean. So every n 32,
  N 256 floor (dossier and m340a) mixes full-rank and collapsed states; the linearized floor theory needs full rank. Before trusting
  a Gram-chain statistic at moderate width, check the numerical rank along the chain.

How to apply: compare a stationary floor with a formula as the second moment about the fixed point the symmetry forces, not as the
variance about a sample mean; when the two differ, look for a slow component before calling it a mean shift, and check first
whether symmetry allows a shift at all.

Open: ReLU and tanh in the same exact form (their row-sampling term is not isotropic), and the O(1/N) correction.
Files: 06_math_research/frontier/rows/T340 (bn_linear_exact.py, bn_linear_exact_n8.txt, _n32.txt, _n32_split.txt, _n32_N256_long.txt),
move m340a.

