# The worst hub law for given light laws. For Q = 2 X_h (L + beta) + V^2 + 2 eps L P, given X' the form is affine in the
# hub with slope 2T, T = L + beta, so p_Q(s) = int f_h(x) W(x) dx with W the density of the measure
# nu(A) = E[1_A(x*)/(2|T|)], x* = (s - V^2 - 2 eps L P)/(2T). Over hub laws f_h <= 1, int f_h = 1, the supremum is the
# integral of W over its top set of measure one (bathtub). W is estimated by a weighted histogram of x* over exact comb
# light laws; the top-set integral is taken at two bin widths to see the bias from sampling noise.
import sys, math, time
import numpy as np
from jperp import S, rot

def run(N, eps, s, which="irr2", n=40_000_000, chunk=2_000_000, xmax=6.0, bins=(0.01, 0.02), seed=3, beta=0.0):
    R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3))) if which == "irr" else \
        rot([3, -1, 2], math.atan(math.sqrt(5))) @ rot([1, 1, 1], math.atan(math.sqrt(7)))
    E = S @ R / math.sqrt(8.0)
    rng = np.random.default_rng(seed)
    b0 = min(bins); nb = int(round(2 * xmax / b0)); acc = np.zeros(nb)
    for _ in range(n // chunk):
        X = rng.integers(0, N, size=(chunk, 8)) + rng.random((chunk, 8)) / N
        Y3 = X @ E; L, V, P = Y3[:, 0], Y3[:, 1], Y3[:, 2]
        T = L + beta
        xs = (s - V * V - 2 * eps * L * P) / (2 * T)
        acc += np.histogram(xs, bins=nb, range=(-xmax, xmax), weights=1.0 / (2 * np.abs(T)))[0]
    out = []
    for b in bins:
        k = int(round(b / b0)); a = acc[: (nb // k) * k].reshape(-1, k).sum(axis=1)
        W = a / (n * b)                       # density of nu on bins of width b
        top = np.sort(W)[::-1][: int(round(1.0 / b))]
        out.append((b, float(top.sum() * b), float(W.max())))
    return out

if __name__ == "__main__":
    for N in (4, 6):
        for s in (0.0, 0.3):
            for eps in (0.0, 0.003):
                t0 = time.time(); out = run(N, eps, s)
                print("irr2 N=%d s=%.1f eps=%.3f  " % (N, s, eps) + "  ".join("bin %.2f: worst-hub density %.4f (max W %.3f)" % o for o in out) + "  (%.0fs)" % (time.time() - t0), flush=True)
