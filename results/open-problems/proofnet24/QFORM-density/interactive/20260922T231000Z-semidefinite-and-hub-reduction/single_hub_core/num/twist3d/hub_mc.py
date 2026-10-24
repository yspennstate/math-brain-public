# Monte Carlo density of the single hub Q = 2 X_h (L + beta) + lam V^2 + 2 eps L P on the spread 3D Walsh frame
# (8 coordinates, leverages 3/8, irrational rotation), exact comb light laws X_i = K_i + W_i/N, hub law uniform on
# [-1/2, 1/2] or a comb. Histogram of Q, bin 0.02; reports the largest bin density and its location.
import sys, math, time
import numpy as np
from jperp import S, rot

def run(N, eps, lam=1.0, beta=0.0, hub="unif", n=40_000_000, chunk=2_000_000, seed=0, lo=-6.0, hi=6.0, b=0.02):
    R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
    E = S @ R / math.sqrt(8.0)
    rng = np.random.default_rng(seed)
    nb = int(round((hi - lo) / b)); cnt = np.zeros(nb)
    for _ in range(n // chunk):
        X = rng.integers(0, N, size=(chunk, 8)) + rng.random((chunk, 8)) / N
        Y = X @ E; L, V, P = Y[:, 0], Y[:, 1], Y[:, 2]
        if hub == "unif":
            xh = rng.random(chunk) - 0.5
        else:
            xh = rng.integers(0, hub, size=chunk) - hub // 2 + rng.random(chunk) / hub
        Q = 2 * xh * (L + beta) + lam * V * V + 2 * eps * L * P
        cnt += np.histogram(Q, bins=nb, range=(lo, hi))[0]
    dens = cnt / (n * b)
    i = int(np.argmax(dens))
    return dens[i], lo + (i + 0.5) * b, 1.0 / math.sqrt(cnt[i])

if __name__ == "__main__":
    for N in (2, 4, 8):
        for eps in (0.0, 0.01, 0.001):
            t0 = time.time()
            d, s, rel = run(N, eps)
            print("N=%d eps=%.3f  max density %.4f at s=%.2f (rel. noise %.3f, %.0fs)" % (N, eps, d, s, rel, time.time() - t0), flush=True)
