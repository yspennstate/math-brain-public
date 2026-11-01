try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
rng = np.random.default_rng(3)
# Q = 4 X_h Lw + 2 Lw^2 + 2 V^2 + sum d_i X_i^2 : hub row along a Fresnel direction, diagonal twist.
n = 60
w = rng.standard_normal(n); w /= np.linalg.norm(w)
v = rng.standard_normal(n); v -= (v@w)*w; v /= np.linalg.norm(v)
M = np.zeros((n+1, n+1)); h = 0
M[h, 1:] = 2*w; M[1:, h] = 2*w
M[1:, 1:] = 2*np.outer(w, w) + 2*np.outer(v, v)
ev = np.linalg.eigvalsh(M); print("core eigenvalues (|.|>0.5):", np.round(ev[np.abs(ev) > 0.5], 3), flush=True)
# off-diagonal block ranks for random partitions
ranks = []
for _ in range(20):
    I = rng.random(n+1) < 0.5
    B = M[np.ix_(I, ~I)]; s = np.linalg.svd(B, compute_uv=False)
    ranks.append(int((s > 1e-9).sum()))
print("ranks of M_IJ over 20 random partitions:", sorted(set(ranks)), flush=True)
def sample(law, N):
    if law == "uniform":
        return rng.random((N, n+1)) - 0.5
    # spread law: uniform on [0,1/4] u [3,3+1/4] u [-7,-7+1/4] u [11, 11+1/4], centred per column
    k = rng.integers(0, 4, size=(N, n+1)); base = np.array([0.0, 3.0, -7.0, 11.0])[k]
    return base + 0.25*rng.random((N, n+1))
for law in ("uniform", "spread"):
    for dscale in (0.0, 0.02, 0.1):
        d = dscale*rng.choice([-1, 1], size=n)
        A = M.copy(); A[1:, 1:] += np.diag(d)
        peak = 0.0
        for rep in range(4):
            X = sample(law, 500000)
            Q = np.einsum('ij,jk,ik->i', X, A, X)
            hist, edges = np.histogram(Q, bins=np.arange(np.percentile(Q, 0.5), np.percentile(Q, 99.5), 0.02))
            peak = max(peak, hist.max()/(len(Q)*0.02))
        print(f"law={law:8s} d={dscale:4.2f}  max histogram density ~ {peak:.3f}", flush=True)
