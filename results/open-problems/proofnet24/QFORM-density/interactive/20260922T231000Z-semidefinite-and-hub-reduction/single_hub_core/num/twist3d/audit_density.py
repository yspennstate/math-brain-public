# Independent checks of hub_mc.py and of the transform integral of phiq.py.
# (1) window estimator, exact in the hub: for X_h uniform on [-1/2, 1/2], P(|Q - s| <= d | X') is the length of the set
#     {x in [-1/2,1/2] : |2x(L+beta) + Y - s| <= d}, an interval; averaged over X' and divided by 2d.
# (2) fine combs (teeth of width 1/N at spacing 2/N in [0,2], light and hub, both centred as in phiq.py): Monte Carlo
#     density of Q = 2 X_h L + V^2 on a grid of s, to compare with (1/pi) int |phi_Q| ~ 0.95.
import math, numpy as np
from jperp import S, rot
R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
E = S @ R / math.sqrt(8.0)
rng = np.random.default_rng(7)

def window(N, s, d, n=4_000_000, eps=0.0, beta=0.0):
    tot = 0.0
    for _ in range(n // 1_000_000):
        X = rng.integers(0, N, size=(1_000_000, 8)) + rng.random((1_000_000, 8)) / N
        Y3 = X @ E; L, V, P = Y3[:, 0], Y3[:, 1], Y3[:, 2]
        a = 2 * (L + beta); b = V * V + 2 * eps * L * P - s
        # |a x + b| <= d  <=>  x in [(-d - b)/a, (d - b)/a] (a > 0), intersected with [-1/2, 1/2]
        lo = np.minimum((-d - b) / a, (d - b) / a); hi = np.maximum((-d - b) / a, (d - b) / a)
        tot += np.clip(np.minimum(hi, 0.5) - np.maximum(lo, -0.5), 0, None).sum()
    return tot / n / (2 * d)

print("window estimator, N=2, eps=0, s=0.01, d=0.01: %.4f   (hub_mc.py: 1.5284)" % window(2, 0.01, 0.01))
print("window estimator, N=4, eps=0, s=0.01, d=0.01: %.4f   (hub_mc.py: 0.5139)" % window(4, 0.01, 0.01))
print("window estimator, N=8, eps=0.01, s=0.15, d=0.01: %.4f   (hub_mc.py: 0.1822)" % window(8, 0.15, 0.01, eps=0.01))

def fine(N, n=20_000_000, lo=-3.0, hi=3.0, b=0.02):
    nb = int(round((hi - lo) / b)); cnt = np.zeros(nb)
    for _ in range(n // 1_000_000):
        X = (2 * rng.integers(0, N, size=(1_000_000, 8)) + rng.random((1_000_000, 8))) / N
        X = X - X.mean(axis=0) * 0 - (1.0 - 0.5 / N)     # centre each coordinate (mean of the fine comb is 1 - 1/(2N))
        Y3 = X @ E; L, V = Y3[:, 0], Y3[:, 1]
        xh = (2 * rng.integers(0, N, size=1_000_000) + rng.random(1_000_000)) / N - 1.0
        Q = 2 * xh * L + V * V
        cnt += np.histogram(Q, bins=nb, range=(lo, hi))[0]
    dens = cnt / (n * b); i = int(np.argmax(dens))
    return dens[i], lo + (i + 0.5) * b

for N in (4, 8):
    d, s = fine(N)
    print("fine combs N=%d: largest MC density %.4f at s=%.2f   ((1/pi) int |phi_Q| on the grid ~ 0.96)" % (N, d, s))
