import numpy as np, itertools
from cover_exact import *
rng = np.random.default_rng(5)

def level_times(P, pi):
    """E_pi[time spent with exactly m visited states], m=1..n-1 (time counted in steps t with |V_t|=m, t < C)"""
    n = P.shape[0]; full = (1 << n) - 1
    H = cover_expectations(P)
    # time at levels: use entrance measures via forward recursion on (x,V) expected visits
    # expected number of visits to (x,V) with V != full, over t>=0
    order = sorted(range(1, full), key=lambda m: bin(m).count("1"))
    # visits N(x,V): solve per level: N_V = mu_V G_V(with row-normalized...) easier: forward DP with killed-chain Green.
    N = {}
    for V in order:
        idx = [x for x in range(n) if V >> x & 1]; k = len(idx)
        mu = np.zeros(k)
        for a, y in enumerate(idx):
            if k == 1: mu[a] = pi[y]
            else:
                Vp = V & ~(1 << y)
                if Vp in N:
                    for x in range(n):
                        if Vp >> x & 1: mu[a] += N[Vp][x] * P[x, y]
        Q = np.array([[P[x, y] for y in idx] for x in idx])
        G = np.linalg.inv(np.eye(k) - Q)   # expected visits
        vis = mu @ G
        N[V] = np.zeros(n)
        for a, x in enumerate(idx): N[V][x] = vis[a]
    lt = np.zeros(n + 1)
    for V, v in N.items(): lt[bin(V).count("1")] += v.sum()
    return lt[1:n]

def unpack(theta, n):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    W = np.zeros((n, n))
    for t, (i, j) in zip(theta, pairs):
        W[i, j] = W[j, i] = np.exp(np.clip(t, -10, 10))
    return W / W.sum()

# sanity: level times sum to E_pi C
n = 5; W = unpack(rng.normal(0, 1, 15), n); P = rw_on_graph(W); pi = W.sum(1)
print("sanity: sum of level times %.6f vs E_pi C %.6f" % (level_times(P, pi).sum(), E_pi_cover(P, pi)))

def hess_min_eig(func, W0, n, eps=1e-3):
    # Hessian on the slice: directions = symmetric matrices with zero total sum
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    dirs = []
    for (i, j) in pairs:
        D = np.zeros((n, n)); D[i, j] = D[j, i] = 1
        D -= D.sum() * np.ones((n, n)) / (n * n)   # project to zero-sum (still symmetric)
        dirs.append(D)
    m = len(dirs); Hm = np.zeros((m, m)); f0 = func(W0)
    fc = {}
    def F(a, b, sa, sb):
        return func(W0 + eps * (sa * dirs[a] + sb * dirs[b]))
    for a in range(m):
        for b in range(a, m):
            Hm[a, b] = Hm[b, a] = (F(a, b, 1, 1) - F(a, b, 1, -1) - F(a, b, -1, 1) + F(a, b, -1, -1)) / (4 * eps * eps)
    # Gram matrix of directions (they are not orthonormal); generalized eigen
    Gm = np.array([[np.sum(dirs[a] * dirs[b]) for b in range(m)] for a in range(m)])
    ev = np.linalg.eigvals(np.linalg.pinv(Gm) @ Hm)
    return np.min(np.real(ev)), f0

f_total = lambda W: E_pi_cover(rw_on_graph(W), W.sum(1))
for n in [3, 4, 5]:
    mins = []
    for trial in range(40 if n < 5 else 15):
        W0 = unpack(rng.normal(0, rng.uniform(0.5, 3), n * (n + 1) // 2), n)
        if rng.random() < 0.5: np.fill_diagonal(W0, 0); W0 /= W0.sum()
        # keep away from boundary a bit so finite differences are valid
        W0 = 0.97 * W0 + 0.03 * np.ones((n, n)) / (n * n)
        me, f0 = hess_min_eig(f_total, W0, n)
        mins.append(me)
    print("n=%d: min Hessian eigenvalue on slice over %d random chains: %.4e (all >= -1e-6? %s)" % (n, len(mins), min(mins), all(m > -1e-6 for m in mins)))
# per-level convexity along segments
for n in [4, 5]:
    worst = np.full(n - 1, -np.inf)
    for trial in range(150):
        W1 = unpack(rng.normal(0, 2, n * (n + 1) // 2), n); W2 = unpack(rng.normal(0, 2, n * (n + 1) // 2), n)
        L = [level_times(rw_on_graph(W), W.sum(1)) for W in (W1, W2, (W1 + W2) / 2)]
        worst = np.maximum(worst, L[2] - (L[0] + L[1]) / 2)
    print("n=%d per-level (m=1..n-1) convexity violation max:" % n, np.round(worst, 4))
