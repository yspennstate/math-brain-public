"""Open Problem 4.45 (Aldous-Fill): push the ratio tau_1^(2)(induced)/tau_1^(2)(original) on n = 6, 7, 8 states,
restricting partitions to one or two merged pairs (the shapes the full search preferred), Nelder-Mead over log-weights."""
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
    try:
        t0, pi = tau12_np(Q); Qh = induced(Q, pi, p); t1, _ = tau12_np(Qh)
    except np.linalg.LinAlgError:
        return 0.0
    if not np.isfinite(t0) or not np.isfinite(t1) or t0 <= 0: return 0.0
    return t1 / t0
def pair_partitions(n, pairs):
    out = []
    for combo in itertools.combinations(itertools.combinations(range(n), 2), pairs):
        used = set()
        ok = True
        for a, b in combo:
            if a in used or b in used: ok = False; break
            used.add(a); used.add(b)
        if not ok: continue
        p = list(range(n)); lab = {}
        for a, b in combo: p[b] = p[a]
        # relabel to restricted growth
        m = {}; q = []
        for v in p:
            if v not in m: m[v] = len(m)
            q.append(m[v])
        out.append(q)
    return out
reps = int(sys.argv[2]) if len(sys.argv) > 2 else 2
for n in [int(a) for a in sys.argv[3:]] or [6, 7]:
    parts = pair_partitions(n, 1) + pair_partitions(n, 2)
    best = (0, None)
    for p in parts:
        for rep in range(reps):
            x0 = rng.normal(0, 2.0, n * (n + 1) // 2)
            r = minimize(lambda x: -ratio(x, n, p), x0, method='Nelder-Mead', options={'maxiter': 1500, 'xatol': 1e-6, 'fatol': 1e-9})
            if -r.fun > best[0]: best = (-r.fun, (p, r.x))
    p, x = best[1]
    W = np.zeros((n, n)); iu = np.triu_indices(n); W[iu] = np.exp(np.clip(x, -9, 9)); W = W + W.T - np.diag(np.diag(W))
    print(f"n={n}: best ratio = {best[0]:.5f}, partition {p}", flush=True)
    print(np.array2string(W / W.max(), precision=5, suppress_small=True), flush=True)
