import numpy as np
from cover_exact import *
rng = np.random.default_rng(11)

def unpack(theta, n):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    W = np.zeros((n, n))
    for t, (i, j) in zip(theta, pairs):
        W[i, j] = W[j, i] = np.exp(np.clip(t, -12, 12))
    return W / W.sum()

def surv(P, pi, tmax):
    """P_pi(C > t) for t=0..tmax via pair-chain forward recursion"""
    n = P.shape[0]; full = (1 << n) - 1
    dist = {}
    for x in range(n): dist[(x, 1 << x)] = pi[x]
    out = []
    for t in range(tmax + 1):
        out.append(sum(p for (x, V), p in dist.items() if V != full))
        new = {}
        for (x, V), p in dist.items():
            if V == full: continue
            for y in range(n):
                if P[x, y] > 0:
                    key = (y, V | (1 << y)); new[key] = new.get(key, 0) + p * P[x, y]
        dist = new
    return np.array(out)

for n in [3, 4, 5]:
    m = n * (n + 1) // 2
    worst_t = np.full(12, -np.inf); worst_x = -np.inf; worst_lvl = -np.inf
    for trial in range(300):
        W1 = unpack(rng.normal(0, rng.uniform(1, 4), m), n); W2 = unpack(rng.normal(0, rng.uniform(1, 4), m), n)
        Wm = (W1 + W2) / 2
        Ps = [rw_on_graph(W) for W in (W1, W2, Wm)]
        pis = [W.sum(1) for W in (W1, W2, Wm)]   # slice: pi = row sums
        S = [surv(P, pi, 11) for P, pi in zip(Ps, pis)]
        worst_t = np.maximum(worst_t, S[2] - (S[0] + S[1]) / 2)
        Ex = [E_x_cover(P) for P in Ps]
        worst_x = max(worst_x, np.max(Ex[2] - (Ex[0] + Ex[1]) / 2))
    print("n=%d  per-t convexity violation (max over trials), t=0..11:" % n, np.round(worst_t, 4))
    print("      fixed-start E_x C convexity violation max: %.4f" % worst_x)
