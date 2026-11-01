try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Theorem U check: leaves S (30 coords, carry V) and T (30 coords, carry L and the twist).
#   'T-only' : Q = a Xh^2 + 2 Xh (L + beta) + lam V^2 + eps X_T^T W X_T      (Theorem U applies; bound 9.5 at a = 0)
#   'all'    : same but the twist acts on all 60 leaves (touches supp v; not covered)
import numpy as np, time, sys
sys.path.insert(0, '.')
from hublib import *
rng = np.random.default_rng(51)
nS, nT = 30, 30; n = nS + nT
v = np.zeros(n); v[:nS] = rng.choice([-1.0, 1.0], nS); v /= np.linalg.norm(v)
w = np.zeros(n); w[nS:] = rng.choice([-1.0, 1.0], nT); w /= np.linalg.norm(w)
G = rng.normal(size=(n, n)); Wall = (G + G.T)/2; Wall /= np.linalg.norm(Wall, 2)
GT = rng.normal(size=(nT, nT)); WT = np.zeros((n, n)); WT[nS:, nS:] = (GT + GT.T)/2; WT /= np.linalg.norm(WT, 2)
N = 200000
fh = uniform_law()
t0 = time.time()
def sampler(lam, eps, Wm):
    def samp(r):
        X = r.random((N, n)) - 0.5
        L = X @ w; V = X @ v
        R = lam*V*V + eps*np.einsum('ij,ij->i', X @ Wm, X)
        return L, R
    return samp
def maxdens(a, beta, samp):
    Lp, Rp = samp(rng); xs = fh.sample(rng, N)
    Qs = a*xs**2 + 2*xs*(Lp + beta) + Rp
    lo, hi = np.percentile(Qs, [5, 95]); sg = np.linspace(lo, hi, 41)
    d = density_on_grid(a, beta, samp, fh, sg, 1, rng); j = int(np.argmax(d))
    s1, dm, _ = refine_max(a, beta, samp, fh, sg[j], (sg[1]-sg[0]), 2, rng, npts=11)
    return dm
for name, Wm in [('T-only', WT), ('all', Wall)]:
    for lam in [1.0, -1.0]:
        for eps in [0.3, 1.0]:
            row = []
            for a in [0.0, 0.05, -0.05]:
                row.append((a, round(float(maxdens(a, 0.0, sampler(lam, eps, Wm))), 3)))
            print("%-6s lam %4.1f eps %.1f  max p_Q by a:" % (name, lam, eps), row, "t=%.0fs" % (time.time()-t0), flush=True)
