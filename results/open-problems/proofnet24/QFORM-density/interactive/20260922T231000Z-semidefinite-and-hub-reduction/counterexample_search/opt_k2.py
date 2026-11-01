"""Maximise F = mu_3 * max_s p(s) over the Gaussian hub model with a rank-2 remainder on span(w, v)
(= spread limit of family (a) with W in span{ww^T, vv^T, wv^T+vw^T} and of Prop 5.4), zero hub diagonal,
uniform hub law; parameters mu, kap, lam, beta, b1, b2 and leaf-variance inflations s1, s2 >= 1/sqrt 12."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys, time
from scipy.optimize import minimize
from gq2 import p_hub2g, SIG
seed = int(sys.argv[1]); nst = int(sys.argv[2])
rng = np.random.default_rng(seed)
SG = np.linspace(-1.2, 1.2, 121)
def mu3(mu, kap, lam):
    A = np.array([[0, 1, 0], [1, mu, kap], [0, kap, lam]], float)
    return np.sort(np.abs(np.linalg.eigvalsh(A)))[0]
def F(x, nq=120, fine=False):
    mu, kap, lam, beta, b1, b2, l1, l2 = x
    s1 = SIG*np.exp(abs(l1)); s2 = SIG*np.exp(abs(l2))
    m3 = mu3(mu, kap, lam)
    if m3 < 1e-3 or max(abs(mu), abs(kap), abs(lam)) > 20: return 0.0, 0.0
    v = p_hub2g(SG, mu, kap, lam, beta, b1, b2, 0.0, s1, s2, nq)[0]
    j = int(np.argmax(v))
    sl = np.linspace(SG[max(j-1, 0)], SG[min(j+1, len(SG)-1)], 17)
    v2 = p_hub2g(sl, mu, kap, lam, beta, b1, b2, 0.0, s1, s2, 400 if fine else nq)[0]
    jj = int(np.argmax(v2))
    return m3*v2[jj], sl[jj]
t0 = time.time()
starts = [np.array([0, 0, 1.0, 0, 0, 0, 0, 0])]
for r in range(nst-1):
    starts.append(np.concatenate([rng.normal(0, 0.7, 3), rng.normal(0, 0.15, 1), rng.normal(0, 0.3, 2), rng.normal(0, 0.1, 2)]))
best = (0, None)
for i, x0 in enumerate(starts):
    f0, _ = F(x0)
    res = minimize(lambda z: -F(z)[0], x0, method='Nelder-Mead', options=dict(maxiter=600, xatol=1e-4, fatol=1e-5, adaptive=True))
    fv, sb = F(res.x, fine=True)
    mu, kap, lam, beta, b1, b2, l1, l2 = res.x
    print(f"start {i}: F0={f0:.4f} -> F={fv:.4f} at s={sb:.4f} | mu={mu:.3f} kap={kap:.3f} lam={lam:.3f} beta={beta:.3f} "
          f"b1={b1:.3f} b2={b2:.3f} s1/SIG={np.exp(abs(l1)):.3f} s2/SIG={np.exp(abs(l2)):.3f} mu3={mu3(mu,kap,lam):.3f} "
          f"eig={np.round(np.linalg.eigvalsh(np.array([[0,1,0],[1,mu,kap],[0,kap,lam]])),3)} nfev={res.nfev} t={time.time()-t0:.0f}", flush=True)
    if fv > best[0]: best = (fv, res.x)
print("BEST", best[0], np.round(best[1], 4).tolist(), flush=True)
