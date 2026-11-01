# Adversarial random search for the hub that sees P. Each light coordinate is uniform on T teeth of width 1/T placed at
# random positions in [0, R] (a unit-measure set, the extreme points of the laws with density at most 1); s and beta are
# random too. For each draw the eps = 0 bathtub B0, the adapted Phi and the shuffled-P control are estimated from the
# same samples, and the net Phi = Phi - (shuffled - B0) is kept. The best draws are re-estimated with 10x the samples.
import sys, math, time
import numpy as np
from adapted_hub import frame

def draw(rng, T, R):
    pos = []
    for _ in range(8):
        while True:
            p = np.sort(rng.uniform(0, R - 1.0 / T, T))
            if T == 1 or np.all(np.diff(p) > 1.0 / T):
                break
        pos.append(p)
    return pos, rng.uniform(-2, 2), rng.uniform(-3, 3)

def estimate(pos, s, beta, T, n, seed, E, b0=0.02, bp=0.05, xmax=6.0, chunk=1_000_000):
    rng = np.random.default_rng(seed)
    q = E[:, 2]; lo = sum(min(0, q[i]) * (pos[i][-1] + 1.0 / T) for i in range(8)) - 0.2
    hi = sum(max(0, q[i]) * (pos[i][-1] + 1.0 / T) for i in range(8)) + 0.2
    nx = int(round(2 * xmax / b0)); npb = int(math.ceil((hi - lo) / bp))
    rg = ((-xmax, xmax), (lo, lo + npb * bp))
    H = np.zeros((nx, npb)); H0 = np.zeros((nx, npb))
    for _ in range(max(1, n // chunk)):
        X = np.empty((chunk, 8))
        for i in range(8):
            X[:, i] = pos[i][rng.integers(0, T, chunk)] + rng.random(chunk) / T
        Y = X @ E; Tt = Y[:, 0] + beta; V = Y[:, 1]; P = Y[:, 2]
        xs = (s - V * V) / (2 * Tt); wt = 1.0 / (2 * np.abs(Tt))
        H += np.histogram2d(xs, P, bins=(nx, npb), range=rg, weights=wt)[0]
        H0 += np.histogram2d(xs, rng.permutation(P), bins=(nx, npb), range=rg, weights=wt)[0]
    top = int(round(1.0 / b0)); nn = max(1, n // chunk) * chunk
    B0 = np.sort(H.sum(axis=1))[::-1][:top].sum() / nn
    Phi = np.sort(H, axis=0)[::-1][:top].sum() / nn
    Sh = np.sort(H0, axis=0)[::-1][:top].sum() / nn
    return B0, Phi, Sh, Phi - (Sh - B0)

if __name__ == "__main__":
    E = frame("irr2"); rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 11)
    draws = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    res = []
    t0 = time.time()
    for k in range(draws):
        T = int(rng.integers(1, 5)); R = float(rng.choice([1.0, 2.0, 4.0, 8.0])) * max(T, 1)
        R = max(R, 1.0 + 1e-9)
        pos, s, beta = draw(rng, T, R)
        B0, Phi, Sh, net = estimate(pos, s, beta, T, 4_000_000, 1000 + k, E)
        res.append((net, B0, Phi, Sh, T, R, s, beta, pos, k))
        print("draw %2d T=%d R=%4.1f s=%+.2f beta=%+.2f  bathtub %.4f  Phi %.4f  shuffled %.4f  net %.4f  ratio %.3f"
              % (k, T, R, s, beta, B0, Phi, Sh, net, net / B0 if B0 > 0 else float('nan')), flush=True)
    res.sort(key=lambda r: -r[0])
    print("best 3 re-estimated with 4e7 samples (%.0fs so far)" % (time.time() - t0), flush=True)
    for net, B0, Phi, Sh, T, R, s, beta, pos, k in res[:3]:
        B0b, Phib, Shb, netb = estimate(pos, s, beta, T, 40_000_000, 5000 + k, E)
        print("draw %2d T=%d R=%4.1f s=%+.2f beta=%+.2f  bathtub %.4f  Phi %.4f  shuffled %.4f  net %.4f  ratio %.3f  teeth %s"
              % (k, T, R, s, beta, B0b, Phib, Shb, netb, netb / B0b, [list(np.round(p, 2)) for p in pos[:2]]), flush=True)
