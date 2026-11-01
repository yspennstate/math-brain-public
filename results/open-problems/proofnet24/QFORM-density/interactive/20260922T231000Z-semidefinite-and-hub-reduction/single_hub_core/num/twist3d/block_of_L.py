# Proposition 5.6 on the smallest configuration it alone covers: w = (e1 + e2)/sqrt 2 on two uniform coordinates,
# v = (e3 + e4)/sqrt 2 on two comb coordinates (N teeth of width 1/N at the integers), q^ = (e1 - e2 + e3 - e4)/2, so the
# partner has a part on the block of L orthogonal to w and a part on the comb coordinates. Estimates the worst hub that
# sees P (Phi), the eps = 0 bathtub and the shuffled-P control from one weighted histogram in (x*_0, P), as in
# adapted_hub.py, with lambda = 1 and the bound 1/2 + sqrt 2 (2 + log(1 + 2 pi^4)) = 10.8 of the proposition.
import sys, math
import numpy as np

def run(N, s=0.0, beta=None, n=16_000_000, chunk=1_000_000, b0=0.02, bp=0.05, xmax=8.0, seed=7):
    rng = np.random.default_rng(seed)
    r2 = math.sqrt(2.0)
    if beta is None:
        beta = -(1.0 / r2)            # -E L: L = (X1 + X2)/sqrt 2 has mean 1/sqrt 2
    vmean = (N - 1 + 1.0 / N) / r2    # E V, so that the square is centred
    plo, phi = -(N + 2) / 2.0, (N + 2) / 2.0
    nx = int(round(2 * xmax / b0)); npb = int(math.ceil((phi - plo) / bp))
    rg = ((-xmax, xmax), (plo, plo + npb * bp))
    H = np.zeros((nx, npb)); H0 = np.zeros((nx, npb))
    for _ in range(n // chunk):
        X1 = rng.random(chunk); X2 = rng.random(chunk)
        X3 = rng.integers(0, N, chunk) + rng.random(chunk) / N
        X4 = rng.integers(0, N, chunk) + rng.random(chunk) / N
        L = (X1 + X2) / r2; V = (X3 + X4) / r2 - vmean; P = (X1 - X2 + X3 - X4) / 2.0
        T = L + beta
        xs = (s - V * V) / (2 * T); wt = 1.0 / (2 * np.abs(T))
        H += np.histogram2d(xs, P, bins=(nx, npb), range=rg, weights=wt)[0]
        H0 += np.histogram2d(xs, rng.permutation(P), bins=(nx, npb), range=rg, weights=wt)[0]
    top = int(round(1.0 / b0)); nn = (n // chunk) * chunk
    B0 = np.sort(H.sum(axis=1))[::-1][:top].sum() / nn
    Phi = np.sort(H, axis=0)[::-1][:top].sum() / nn
    Sh = np.sort(H0, axis=0)[::-1][:top].sum() / nn
    return B0, Phi, Sh, Phi - (Sh - B0)

if __name__ == "__main__":
    print("bound of Proposition 5.6 (lambda = 1): %.2f" % (0.5 + math.sqrt(2) * (2 + math.log(1 + 2 * math.pi ** 4))))
    for N in [int(x) for x in sys.argv[1].split(",")]:
        for s in (0.0, 1.0):
            B0, Phi, Sh, net = run(N, s=s)
            print("N=%3d s=%.1f  bathtub %.4f  Phi %.4f  shuffled %.4f  net %.4f  ratio %.3f" % (N, s, B0, Phi, Sh, net, net / B0), flush=True)
