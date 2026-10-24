"""Fast search for a 9-variable Boolean function with max |Walsh coefficient| <= 30, which refutes
Conjecture 13 of the Randomstrasse 2024 list at k = 9 (it predicts 32).

Rotation-symmetric functions are constant on the 60 cyclic orbits of {0,1}^9, so flipping orbit j
changes every Walsh coefficient by a fixed vector:  W_a  ->  W_a - 2 * x_j * S_j(a),  where
S_j(a) = sum over u in orbit j of (-1)^{a.u} and x_j = +-1 is the orbit's current sign.  Precomputing the
60 x 512 matrix S makes each move one vector addition instead of a transform.

Cost is sum |W_a|^p, which pushes down the largest coefficients; p is raised as the run proceeds.
"""
import numpy as np, sys, time

K = 9; N = 1 << K

def build():
    rep = -np.ones(N, dtype=int); reps = []
    for u in range(N):
        if rep[u] >= 0: continue
        idx = len(reps); reps.append(u); v = u
        for _ in range(K):
            rep[v] = idx
            v = ((v << 1) & (N - 1)) | (v >> (K - 1))
    nor = len(reps)
    a = np.arange(N)
    S = np.zeros((nor, N), dtype=np.int32)
    for u in range(N):
        par = 1 - 2 * (np.bitwise_count(a & u).astype(np.int64) & 1)   # cast: bitwise_count is unsigned
        S[rep[u]] += par
    return rep, reps, nor, S

REP, REPS, NORB, S = build()

def run(seed, iters, p0=4.0, p1=10.0, T0=60.0):
    rng = np.random.default_rng(seed)
    xs = 1 - 2 * rng.integers(0, 2, NORB)            # +-1 per orbit
    W = (xs[:, None] * S).sum(axis=0).astype(np.int64)
    def cost(w, p): return float((np.abs(w) ** p).sum())
    p = p0
    c = cost(W, p); best = int(np.abs(W).max()); bx = xs.copy()
    for it in range(iters):
        if it % 20000 == 0:
            p = p0 + (p1 - p0) * it / iters
            c = cost(W, p)
        temp = max(0.02, T0 * (1 - it / iters))
        j = rng.integers(0, NORB)
        dW = W - 2 * xs[j] * S[j]
        c2 = cost(dW, p)
        if c2 <= c or rng.random() < np.exp(-min(50.0, (c2 - c) / max(1e-9, c * temp * 1e-3))):
            W = dW; xs[j] = -xs[j]; c = c2
            m = int(np.abs(W).max())
            if m < best:
                best = m; bx = xs.copy()
                if best <= 30: return best, bx
    return best, bx

if __name__ == '__main__':
    seeds = int(sys.argv[1]); iters = int(sys.argv[2])
    t0 = time.time(); overall, ob = 10**9, None
    for s in range(seeds):
        b, xs = run(s, iters)
        if b < overall:
            overall, ob = b, xs.copy()
            print(f"  seed {s:3d}: max|W| = {b}  nonlinearity = {N//2 - b//2}   [{time.time()-t0:.0f}s]", flush=True)
        if overall <= 30: break
    print(f"\nbest over {seeds} restarts: max|W| = {overall}, nonlinearity = {N//2 - overall//2}", flush=True)
    print(f"the conjecture requires 32 / 240; a 30 / 241 refutes it", flush=True)
    if overall <= 30:
        np.save('rsbf9_witness.npy', ob)
        ones = [REPS[i] for i in range(NORB) if ob[i] < 0]
        print("WITNESS FOUND. orbit representatives where f = 1:", ones, flush=True)
