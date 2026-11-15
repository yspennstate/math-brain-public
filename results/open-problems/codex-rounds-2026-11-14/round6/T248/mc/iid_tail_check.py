"""Is the heavy upper tail of the GPU iid control real? Compare the GPU lambda_max sample with a float64 numpy run
of the same model (iid entries he2(Z) = (Z^2-1)/sqrt2, m x N, rows centred, K = Yc Yc^T / N).
Also record the largest entry, since a single large chi-square entry moves lambda_max at these sizes.
Usage: python iid_tail_check.py N m reps"""
import math
import sys

import numpy as np

N, m, reps = (int(a) for a in sys.argv[1:4])
b = m / N
scale = b ** (1 / 6) / (1 + math.sqrt(b)) ** (4 / 3) * N ** (2 / 3)
edge = (1 + math.sqrt(b)) ** 2

gpu = np.load(f"out_1115/iid_he2_N{N}_m{m}_d{3 * N // 4}.npy")
sg = scale * (gpu - edge)
print(f"GPU  n={len(gpu)} lam max {gpu.max():.3f}  quantiles 50/90/95/99 of s:",
      np.round(np.quantile(sg, [0.5, 0.9, 0.95, 0.99]), 2), " frac lam>2*edge", np.mean(gpu > 2 * edge))

rng = np.random.default_rng(5)
s, amax = [], []
for _ in range(reps):
    Z = rng.standard_normal((m, N))
    Y = (Z * Z - 1.0) / math.sqrt(2.0)
    Yc = Y - Y.mean(axis=1, keepdims=True)
    lam = np.linalg.eigvalsh(Yc @ Yc.T / N)[-1]
    s.append(scale * (lam - edge))
    amax.append(np.abs(Y).max())
s = np.array(s)
print(f"CPU  n={reps} quantiles 50/90/95/99 of s:", np.round(np.quantile(s, [0.5, 0.9, 0.95, 0.99]), 2),
      f" mean {s.mean():.2f}  max entry mean {np.mean(amax):.1f}")
