"""Weight-side edge E_W for sigma = h_2 (Remark 7.1 of the paper): given W the columns of Y are iid in R^m with
covariance Sigma_W = d/(d+2) G*G - ss^T/(d+2), G = W W^T / d, s = diag(G) (* = entrywise product), and E_W is the
Silverstein-Choi right edge of N-1 samples from that population, times (N-1)/N.
Prints the mean and sd of scale * (E_W - E_0) over reps, per (N, m, d). Usage: python3 edge_weight_side.py reps   (the paper uses reps = 6)"""
import json
import math
import sys

import numpy as np

rng = np.random.default_rng(23)
reps = int(sys.argv[1])
SIZES = [(500, 250, 375), (1000, 500, 750), (2000, 1000, 1500), (4000, 2000, 3000), (8000, 4000, 6000),
         (1000, 2000, 1500), (2000, 4000, 3000)]


def edge(t, n):
    t = t[t > 1e-12]
    g = lambda u: u * u * np.sum(t * t / (1 + t * u) ** 2) / n - 1.0
    lo, hi = -1.0 / t.max() * (1 - 1e-12), -1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    u = 0.5 * (lo + hi)
    return -1.0 / u + np.sum(t / (1 + t * u)) / n


out = []
for N, m, d in SIZES:
    b, c = m / N, (N - 1) / N
    E0 = (math.sqrt(b) + math.sqrt(c)) ** 2
    scale = (c * b) ** (1 / 6) / (math.sqrt(b) + math.sqrt(c)) ** (4 / 3) * N ** (2 / 3)
    vals = []
    for _ in range(reps):
        W = rng.standard_normal((m, d))
        G = W @ W.T / d
        s = np.diag(G).copy()
        tW = np.linalg.eigvalsh(d / (d + 2) * G * G - np.outer(s, s) / (d + 2))
        vals.append(scale * (edge(tW, N - 1) * (N - 1) / N - E0))
    row = dict(N=N, m=m, d=d, reps=reps, EW_minus_E0_tw_mean=float(np.mean(vals)), sd=float(np.std(vals)))
    out.append(row)
    print(json.dumps(row), flush=True)
with open("edge_weight_side_out.json", "w") as fh:
    json.dump(out, fh, indent=1)
