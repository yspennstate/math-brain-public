"""Search the Patterson-Wiedemann symmetry class on GF(2^15) for a Boolean function with
max |W| <= 254, which refutes Conjecture 13 of the Randomstrasse 2024 list at k = 15
(it predicts that the smallest achievable max |W| is exactly 256).

Flipping one of the 74 classes changes the whole Walsh spectrum by a precomputed vector, so a move is
a single vector addition.  Cost is the Clark-Jacob form sum ||W_a| - X|^R, which pushes the spectrum
toward flatness rather than merely shaving the single largest coefficient.
"""
import numpy as np, sys, time
from pw15 import REP, REPS, NORB, N, spectrum

def build_T():
    T = np.zeros((NORB, N), dtype=np.int32)
    a = np.arange(N)
    for u in range(N):
        par = 1 - 2 * (np.bitwise_count(a & u).astype(np.int64) & 1)
        T[REP[u]] += par
    return T

print("precomputing the per-class spectrum vectors ...", flush=True)
t0 = time.time(); T = build_T(); print(f"  done in {time.time()-t0:.0f}s", flush=True)

X, R = 181.0, 3.0        # 2^(15/2) = 181.02

def cost(w):
    return float((np.abs(np.abs(w) - X) ** R).sum())

def run(seed, iters, T0=0.02):
    rng = np.random.default_rng(seed)
    s = (1 - 2 * rng.integers(0, 2, NORB)).astype(np.int64)
    W = (s[:, None] * T).sum(axis=0)
    c = cost(W); best = int(np.abs(W).max()); bs = s.copy()
    for it in range(iters):
        temp = max(1e-4, T0 * (1 - it / iters))
        j = rng.integers(0, NORB)
        W2 = W - 2 * s[j] * T[j]
        c2 = cost(W2)
        if c2 <= c or rng.random() < np.exp(-(c2 - c) / (c * temp)):
            W = W2; s[j] = -s[j]; c = c2
            m = int(np.abs(W).max())
            if m < best:
                best, bs = m, s.copy()
    return best, bs

if __name__ == '__main__':
    seeds = int(sys.argv[1]); iters = int(sys.argv[2])
    overall, ob = 10**9, None
    for sd in range(seeds):
        b, s = run(sd, iters)
        if b < overall:
            overall, ob = b, s.copy()
            print(f"  seed {sd:3d}: max|W| = {b}   nonlinearity = {N//2 - b//2}   "
                  f"(bound to beat: 256 / 16256)", flush=True)
        if overall <= 254:
            np.save('pw15_witness.npy', ob)
            print("WITNESS: classes with f = 1:", [int(REPS[i]) for i in range(NORB) if ob[i] < 0], flush=True)
            break
    print(f"\nbest over {seeds} restarts: max|W| = {overall}, nonlinearity = {N//2 - overall//2}", flush=True)
