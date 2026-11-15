# I0001: exact annealed MSD of the randomly oriented Manhattan walk (numerical evidence)

Problem: Bou-Rabee and Peres, arXiv:2609.07621, Section 7, Problem 1 (is the annealed mean-square displacement of order t^{4/3}?).

The scripts evolve the full quenched distribution of the walk in one iid environment at a time, with no walker noise; the
average of the exact quenched MSD over environments is the annealed MSD.

- manhattan_exact_torch.py: full (2T+2)^2 grid, CUDA.
- manhattan_exact_torch_w.py (CUDA) and manhattan_exact_w.py (MLX): a cropped (2W+2)^2 window. The environment is drawn on the
  full grid and cropped, so a window run sees the same environment as the full-grid run with the same seed. The mass in a
  64-wide edge band is recorded (edge_max); rows with edge_max above 1e-9 are not used.
- pooled_slopes.py: local log-log slopes of the pooled MSD on dyadic windows, bootstrap over environments.

Results to 13 Nov 2026 (150 environments to T=2000, 54 to T=4000): local slopes 1.317, 1.317, 1.302, 1.315 (+-0.016-0.019) on
[125,250] .. [1000,2000] and 1.343 (+-0.029) on [2000,4000]. Consistent with 4/3; t log t would read about 1.15. The windows
share environments and are not independent. Numerical evidence only, not a proof. Data (npz) follows when the T=4000 and
T=8000 window runs finish.
