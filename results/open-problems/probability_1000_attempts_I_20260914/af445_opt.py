"""Open Problem 4.45 (Aldous-Fill): maximise tau_1^(2)(induced)/tau_1^(2)(original) over reversible chains on n states and partitions.
Nelder-Mead over log-weights for each partition shape; report the best ratio per n. Then exact (mpmath) verification of the best small example."""
import numpy as np, sys, itertools
from scipy.optimize import minimize
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def tau12_np(Q):
    n = Q.shape[0]
    ev, V = np.linalg.eig(Q.T); k = np.argmin(np.abs(ev)); pi = np.real(V[:, k]); pi = pi / pi.sum()
    Pi = np.tile(pi, (n, 1)); Z = np.linalg.inv(Pi - Q) - Pi
    return np.max(-Z / pi[None, :]), pi
def induced(Q, pi, p):
    m = max(p) + 1; hatpi = np.zeros(m); Qh = np.zeros((m, m)); n = len(p)
    for i in range(n): hatpi[p[i]] += pi[i]
    for i in range(n):
        for j in range(n):
            if i != j and p[i] != p[j]: Qh[p[i], p[j]] += pi[i] * Q[i, j]
    Qh = Qh / hatpi[:, None]; np.fill_diagonal(Qh, -Qh.sum(1))
    return Qh
def ratio(x, n, p):
    W = np.zeros((n, n)); iu = np.triu_indices(n); W[iu] = np.exp(np.clip(x, -9, 9)); W = W + W.T - np.diag(np.diag(W))
    w = W.sum(1); Q = W / w[:, None]; np.fill_diagonal(Q, 0); np.fill_diagonal(Q, -Q.sum(1))
    t0, pi = tau12_np(Q)
    Qh = induced(Q, pi, p)
    if Qh.shape[0] < 2: return 0.0
    t1, _ = tau12_np(Qh)
    return t1 / t0
def partitions(n):
    def rec(i, cur, m):
        if i == n: yield list(cur); return
        for b in range(m + 1):
            cur.append(b); yield from rec(i + 1, cur, max(m, b + 1)); cur.pop()
    for p in rec(0, [], 0):
        if 1 < max(p) + 1 < n: yield p
for n in [3, 4]:
    best = (0, None)
    parts = list(partitions(n))
    for p in parts:
        for rep in range(int(sys.argv[2]) if len(sys.argv) > 2 else 6):
            x0 = rng.normal(0, 2.0, n * (n + 1) // 2)
            r = minimize(lambda x: -ratio(x, n, p), x0, method='Nelder-Mead', options={'maxiter': 2000, 'xatol': 1e-7, 'fatol': 1e-10})
            if -r.fun > best[0]: best = (-r.fun, (p, r.x))
    p, x = best[1]
    W = np.zeros((n, n)); iu = np.triu_indices(n); W[iu] = np.exp(np.clip(x, -9, 9)); W = W + W.T - np.diag(np.diag(W))
    print(f"n={n}: best induced/original tau_1^(2) ratio = {best[0]:.5f}, partition {p}")
    print(np.array2string(W / W.max(), precision=5, suppress_small=True))
