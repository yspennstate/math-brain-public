"""Push the ratio tau_1/tau_0 up by local optimisation over reversible chains on n states (weights W_ij = W_ji >= 0, holding weights on the diagonal)."""
import numpy as np, sys
from scipy.optimize import minimize
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)

def ratio(x, n):
    W = np.zeros((n, n)); iu = np.triu_indices(n)
    W[iu] = np.exp(np.clip(x, -12, 12)); W = W + W.T - np.diag(np.diag(W))
    w = W.sum(1); Q = W / w[:, None]; np.fill_diagonal(Q, 0); np.fill_diagonal(Q, -Q.sum(1))
    pi = w / w.sum(); Pi = np.tile(pi, (n, 1))
    try: Z = np.linalg.inv(Pi - Q) - Pi
    except np.linalg.LinAlgError: return 0.0
    tau0 = np.trace(Z)
    d = np.sqrt(pi); S = (d[:, None] * (-Q)) / d[None, :]; S = (S + S.T) / 2
    ev, U = np.linalg.eigh(S)
    if np.sort(ev)[1] < 1e-9: return 0.0
    def dbar(t):
        Pt = (U * np.exp(-t * ev)) @ U.T; Pt = Pt / d[:, None] * d[None, :]
        m = 0.0
        for i in range(n):
            for j in range(i + 1, n): m = max(m, 0.5 * np.abs(Pt[i] - Pt[j]).sum())
        return m
    lo, hi = 0.0, 1.0
    while dbar(hi) > np.exp(-1): hi *= 2
    for _ in range(50):
        mid = (lo + hi) / 2
        if dbar(mid) > np.exp(-1): lo = mid
        else: hi = mid
    return hi / tau0

best = {}
for n in [3, 4, 5, 6]:
    bn = (0, None)
    for rep in range(int(sys.argv[2]) if len(sys.argv) > 2 else 30):
        x0 = rng.normal(0, 2.5, n * (n + 1) // 2)
        r = minimize(lambda x: -ratio(x, n), x0, method='Nelder-Mead', options={'maxiter': 3000, 'xatol': 1e-6, 'fatol': 1e-9})
        if -r.fun > bn[0]: bn = (-r.fun, r.x)
    best[n] = bn
    W = np.zeros((n, n)); iu = np.triu_indices(n); W[iu] = np.exp(np.clip(bn[1], -12, 12)); W = W + W.T - np.diag(np.diag(W))
    print(f"n={n}: best tau1/tau0 = {bn[0]:.6f}")
    print(np.array2string(W / W.max(), precision=5, suppress_small=True))
