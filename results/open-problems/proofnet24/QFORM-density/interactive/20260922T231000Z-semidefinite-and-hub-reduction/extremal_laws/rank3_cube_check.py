"""Rank-3 forms on a unit cube in R^n with a heavy-leverage coordinate and a linear term outside the range:
max_s density estimated by fine windows (large samples).  The theorem says bounded by a universal constant."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, time
rng = np.random.default_rng(7)
def frame(n, heavy):
    # three orthonormal columns; first column has weight 'heavy' on coordinate 0
    G = rng.normal(size=(n, 4)); G[0, 0] = 0
    G[:, 0] /= np.linalg.norm(G[:, 0]); G[:, 0] = np.sqrt(1-heavy**2)*G[:, 0]; G[0, 0] = heavy
    Qm, _ = np.linalg.qr(G); 
    if Qm[0,0]*heavy < 0: Qm[:,0] *= -1
    return Qm[:, :3], Qm[:, 3]
T0 = time.time()
for n in [10, 40]:
    for heavy in [0.3, 0.95]:
        R, u = frame(n, heavy)
        for lam in [(1,1,1), (1,1,-1), (1,-1,-1)]:
            for gamma in [0.0, 0.3, 3.0]:
                A = R @ np.diag(lam) @ R.T
                b = gamma*u + R @ rng.normal(scale=0.5, size=3)
                vals = []
                N = 400_000
                X = rng.random((N, n)) - 0.5 + rng.normal(scale=0.3, size=n)   # cube in a random position
                Qv = np.einsum('ij,jk,ik->i', X, A, X) + X @ b
                lo, hi = np.quantile(Qv, [0.001, 0.999]); w = (hi - lo)/600
                h, e = np.histogram(Qv, bins=np.arange(lo, hi + w, w))
                k = np.argmax(h); cen = (e[k] + e[k+1])/2
                pk = max(h[k]/N/w, np.mean(np.abs(Qv - cen) < w/4)/(w/2))
                print(f"n={n} lev0={heavy**2:.2f} lam={lam} gamma={gamma}: max density ~ {pk:.3f}", flush=True)
print("time", time.time()-T0)
