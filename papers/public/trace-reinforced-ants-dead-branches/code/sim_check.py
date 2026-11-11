# Check of the crossing probabilities against the simulated process: for every edge the sum over ants of
# (indicator the ant crossed e) - p_e(W) is a martingale; z = sum / sqrt(sum p(1-p)) should be O(1).
# p_e(W) comes from the per-edge linear solve (ants_core.pvals). Also prints W/n for several seeds on the paw.
# Usage: python3 sim_check.py NANTS
import sys, random, math, numpy as np
import ants_core as A
def ant(adj, W, N, F, rnd):
    x = N; crossed = set()
    while x != F:
        nb = adj[x]; tot = 0.0
        for (_, k) in nb: tot += W[k]
        r = rnd.random() * tot
        for (z, k) in nb:
            r -= W[k]
            if r <= 0: break
        crossed.add(k); x = z
    return crossed
def mk(n, E):
    adj = [[] for _ in range(n)]
    for k, (u, v) in enumerate(E): adj[u].append((v, k)); adj[v].append((u, k))
    return adj
def zcheck(name, n, E, N, F, nants, seed):
    rnd = random.Random(seed); adj = mk(n, E); W = [1.0] * len(E); M = np.zeros(len(E)); V = np.zeros(len(E))
    for t in range(1, nants + 1):
        p = A.pvals(n, E, np.array(W), N, F)[0]
        c = ant(adj, W, N, F, rnd)
        d = np.zeros(len(E)); d[list(c)] = 1.0
        M += d - p; V += p * (1 - p)
        for k in c: W[k] += 1.0
    print(name, "ants", nants, "z per edge", [round(float(m / math.sqrt(v)), 2) if v > 0 else 0.0 for m, v in zip(M, V)], "W/n", [round(w / nants, 4) for w in W], flush=True)
nants = int(sys.argv[1])
zcheck("paw", 4, [(0, 1), (1, 2), (1, 3), (2, 3)], 0, 3, nants, 1)
zcheck("c4detour", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (4, 1), (4, 2)], 0, 2, nants, 2)
zcheck("shadow5", 5, [(0, 1), (0, 2), (1, 3), (2, 3), (4, 1), (4, 2), (4, 3)], 0, 3, nants, 3)
zcheck("K33+xF", 6, [(i, j) for i in (1, 2, 3) for j in (0, 4, 5)] + [(5, 4)], 0, 4, nants, 4)
# paw, several seeds: X/n and the formula's own running prediction  X_pred(n) = X(n0) + sum X/(X+A)
E = [(0, 1), (1, 2), (1, 3), (2, 3)]; adj = mk(4, E)
for seed in range(21, 27):
    rnd = random.Random(seed); W = [1.0] * 4; S = 0.0; out = []
    for t in range(1, 1000001):
        S += W[1] / (W[1] + W[2])
        c = ant(adj, W, 0, 3, rnd)
        for k in c: W[k] += 1.0
        if t in (1000, 10000, 100000, 1000000): out.append((t, round(W[1] / t, 5), round(W[3] / t, 5), round((W[1] - 1 - S) / math.sqrt(S), 2)))
    print("paw seed", seed, "(n, W_xy/n, W_yF/n, z of W_xy against sum X/(X+A))", out, flush=True)
