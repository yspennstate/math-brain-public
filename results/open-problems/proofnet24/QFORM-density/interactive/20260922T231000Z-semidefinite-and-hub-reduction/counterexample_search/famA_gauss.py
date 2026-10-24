"""Spread-leaf (Gaussian) limit of families (a)/(b): hub X_h (uniform law) + Gaussian projections Y ~ N(0, I/12),
Q = a X_h^2 + 2 X_h (Y_1 + beta) + Y^T D Y + beta'.Y .  Maximise F = |mu_3(A_core)| max_s p(s) by Nelder-Mead over
(D, beta, beta') from several starts, E2 with common random numbers; verify with fresh samples."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys, time
from scipy.optimize import minimize
from lib import *
k = int(sys.argv[1]); a_h = float(sys.argv[2]); seed = int(sys.argv[3]); nst = int(sys.argv[4]) if len(sys.argv) > 4 else 4
rng = np.random.default_rng(seed)
sig = np.sqrt(1/12)
laws = [U()] + [GaussLaw(sig)]*k
nD = k*(k+1)//2; iu = np.triu_indices(k)
def unpack(x):
    D = np.zeros((k, k)); D[iu] = x[:nD]; D = D + D.T - np.diag(np.diag(D))
    beta = x[nD]; bp = x[nD+1:nD+1+k]
    A = np.zeros((k+1, k+1)); A[0, 0] = a_h; A[0, 1] = A[1, 0] = 1.0; A[1:, 1:] = D
    b = np.zeros(k+1); b[0] = 2*beta; b[1:] = bp
    return A, b
def Fval(x, N, sd, ngrid=61, ret=False):
    A, b = unpack(x); m3 = mu3(A)
    if m3 < 0.05: return 0.0
    # locate the bulk of Q with a small pilot sample
    Xp = sample_X(laws, 4000, np.random.default_rng(sd+17))
    Qv = np.einsum('ij,ij->i', Xp, Xp @ A) + Xp @ b
    lo, hi = np.quantile(Qv, [0.02, 0.98])
    sv = np.linspace(lo, hi, ngrid)
    mm, se = fibre_density(A, laws, sv, N=N, b=b, rng=np.random.default_rng(sd))
    j = int(np.argmax(mm))
    # refine around the max
    sv2 = np.linspace(sv[max(j-1, 0)], sv[min(j+1, ngrid-1)], 21)
    m2, s2 = fibre_density(A, laws, sv2, N=N, b=b, rng=np.random.default_rng(sd+1))
    jj = int(np.argmax(m2))
    if ret: return m3*m2[jj], m3, sv2[jj], m3*s2[jj]
    return m3*m2[jj]
t0 = time.time()
starts = []
x0 = np.zeros(nD+1+k); D0 = np.zeros((k, k)); D0[1, 1] = 1.0; x0[:nD] = D0[iu]; starts.append(('star+rank1', x0))
for r in range(nst-1):
    x = np.zeros(nD+1+k); D = rng.normal(size=(k, k)); D = (D+D.T)/2; D[0, 0] *= 0.2
    x[:nD] = D[iu]; x[nD] = 0.1*rng.normal(); x[nD+1:] = 0.2*rng.normal(size=k); starts.append((f'rand{r}', x))
best = None
for name, x in starts:
    f0 = Fval(x, 20000, 5)
    res = minimize(lambda z: -Fval(z, 20000, 5), x, method='Nelder-Mead',
                   options=dict(maxiter=250, xatol=1e-3, fatol=1e-3, adaptive=True))
    fv, m3, sbest, se = Fval(res.x, 300000, 99, ngrid=81, ret=True)
    A, b = unpack(res.x)
    print(f"k={k} a={a_h} start {name}: F0={f0:.3f} -> opt {-res.fun:.3f}; fresh F={fv:.4f}+-{se:.4f} "
          f"(mu3={m3:.3f}, s={sbest:.3f}) eig={np.round(np.linalg.eigvalsh(A),3)} t={time.time()-t0:.0f}", flush=True)
    print("   D=", np.round(A[1:, 1:], 3).tolist(), " beta=", round(b[0]/2, 3), " beta'=", np.round(b[1:], 3).tolist(), flush=True)
    if best is None or fv > best[0]: best = (fv, name, res.x)
print("BEST", best[0], best[1], flush=True)
