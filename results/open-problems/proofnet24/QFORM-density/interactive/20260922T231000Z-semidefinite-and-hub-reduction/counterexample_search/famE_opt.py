"""Family (e) optimiser on the semi-Gaussian model of famE_semi.py.
Parameters: rho in R^3 (leverage |rho|^2 <= .95 of the heavy coordinate), lam = (l1, l2, l3) with signs fixed by the
mode, linear terms b (3) and c0.  Objective F = min|lam| * max_s p(s) over s on the requested side:
  mode 'pd'  : lam > 0, all s;  mode 'two' : (+,+,-), s below the critical value of the Y-form (two-sheet side),
  mode 'all' : (+,+,-), all s (both sides; one-sheet side <= pi sqrt 2 by Theorem C when c0 = 0)."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys, time
from scipy.optimize import minimize
from famE_semi import density, SIG

mode = sys.argv[1]; seed = int(sys.argv[2]); nst = int(sys.argv[3])
rng = np.random.default_rng(seed)


def unpack(x):
    r = x[0:3]; nr = np.linalg.norm(r)
    lev = 0.95*np.tanh(nr)**2 if nr > 0 else 0.0
    rho = r/nr*np.sqrt(lev) if nr > 0 else np.zeros(3)
    l = 1 + np.abs(x[3:6])                     # magnitudes >= 1, min normalised below
    sg = np.array([1, 1, 1]) if mode == 'pd' else np.array([1, 1, -1])
    lam = sg*l/np.min(l)
    b = x[6:9]; c0 = x[9]
    return rho, lam, b, c0


def svals_for(rho, lam, b, c0):
    # critical value of the Y-form ignoring X0 coupling: Q = (Y - y0)^T L (Y - y0) + qc, y0 = -L^{-1} b/2
    y0 = -b/(2*lam); qc = -np.sum(b*b/(4*lam))
    if mode == 'pd':
        return np.linspace(qc + 0.005, qc + 1.0, 40), qc
    if mode == 'two':
        return np.linspace(qc - 0.8, qc - 0.002, 40), qc
    return np.linspace(qc - 0.8, qc + 0.8, 61), qc


def F(x, nx=16, fine=False):
    rho, lam, b, c0 = unpack(x)
    sv, qc = svals_for(rho, lam, b, c0)
    p = density(sv, rho, lam, b, c0, nx=nx)
    j = int(np.argmax(p))
    if fine:
        sl = np.linspace(sv[max(j-1, 0)], sv[min(j+1, len(sv)-1)], 11)
        if mode == 'two': sl = sl[sl < qc]
        p2 = density(sl, rho, lam, b, c0, nx=32)
        jj = int(np.argmax(p2)); return p2[jj], sl[jj]
    return p[j], sv[j]


t0 = time.time()
best = (0, None)
for i in range(nst):
    x0 = np.concatenate([rng.normal(0, 1.0, 3), np.abs(rng.normal(0, 0.3, 3)), rng.normal(0, 0.1, 3), rng.normal(0, 0.1, 1)])
    if i == 0: x0[0:3] = 1e-3; x0[3:] = 0            # Gaussian start
    f0 = F(x0)[0]
    res = minimize(lambda z: -F(z)[0], x0, method='Nelder-Mead', options=dict(maxiter=260, xatol=1e-3, fatol=1e-4, adaptive=True))
    fv, sb = F(res.x, fine=True)
    rho, lam, b, c0 = unpack(res.x)
    print(f"{mode} start {i}: F0={f0:.4f} -> F={fv:.4f} at s={sb:.4f} | rho={np.round(rho,3)} lev={rho@rho:.3f} lam={np.round(lam,3)} "
          f"b={np.round(b,3)} c0={c0:.3f} nfev={res.nfev} t={time.time()-t0:.0f}", flush=True)
    if fv > best[0]: best = (fv, res.x)
print("BEST", mode, best[0], flush=True)
