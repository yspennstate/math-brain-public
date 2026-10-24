"""Gaussian hub model with a rank-3 remainder (spread limit of family (a) with W having a component on a third
direction u): Q = 2 X_h (Y1 + beta) + Y^T D Y + b.Y,  D 3x3 free.  Maximise F = mu_3(A_core) max_s p(s)."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys, time
from scipy.optimize import minimize
from gq2 import p_hub3, SIG
seed = int(sys.argv[1]); nst = int(sys.argv[2]); m_gh = int(sys.argv[3]) if len(sys.argv) > 3 else 16
rng = np.random.default_rng(seed)
SG = np.linspace(-1.2, 1.2, 97)
def Acore(x):
    mu, kap, lam, beta, b1, b2, k13, k23, nu, b3 = x
    return np.array([[0, 1, 0, 0], [1, mu, kap, k13], [0, kap, lam, k23], [0, k13, k23, nu]], float)
def F(x, nq=100, m=m_gh, fine=False):
    mu, kap, lam, beta, b1, b2, k13, k23, nu, b3 = x
    if np.max(np.abs(x[[0, 1, 2, 6, 7, 8]])) > 20: return 0.0, 0.0
    m3 = np.sort(np.abs(np.linalg.eigvalsh(Acore(x))))[::-1][2]
    if m3 < 1e-3: return 0.0, 0.0
    v = p_hub3(SG, mu, kap, lam, beta, b1, b2, k13, k23, nu, b3, m=m, nq=nq)
    j = int(np.argmax(v))
    sl = np.linspace(SG[max(j-1, 0)], SG[min(j+1, len(SG)-1)], 13)
    v2 = p_hub3(sl, mu, kap, lam, beta, b1, b2, k13, k23, nu, b3, m=(40 if fine else m), nq=(300 if fine else nq))
    jj = int(np.argmax(v2))
    return m3*v2[jj], sl[jj]
t0 = time.time()
base = np.array([0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0])
starts = []
for r in range(nst):
    if r % 2 == 0:
        x = base.copy(); x[[6, 7, 8]] = rng.normal(0, 0.3, 3); x[[3, 4, 5, 9]] = rng.normal(0, 0.05, 4)
    else:
        x = np.concatenate([rng.normal(0, 0.8, 3), rng.normal(0, 0.1, 1), rng.normal(0, 0.2, 2), rng.normal(0, 0.8, 3), rng.normal(0, 0.2, 1)])
    starts.append(x)
best = (0, None)
for i, x0 in enumerate(starts):
    f0, _ = F(x0)
    res = minimize(lambda z: -F(z)[0], x0, method='Nelder-Mead', options=dict(maxiter=700, xatol=1e-4, fatol=1e-5, adaptive=True))
    fv, sb = F(res.x, fine=True)
    A = Acore(res.x)
    print(f"start {i}: F0={f0:.4f} -> F={fv:.4f} at s={sb:.4f} | x={np.round(res.x,3).tolist()} eig={np.round(np.linalg.eigvalsh(A),3)} nfev={res.nfev} t={time.time()-t0:.0f}", flush=True)
    if fv > best[0]: best = (fv, res.x)
print("BEST", best[0], np.round(best[1], 4).tolist(), flush=True)
