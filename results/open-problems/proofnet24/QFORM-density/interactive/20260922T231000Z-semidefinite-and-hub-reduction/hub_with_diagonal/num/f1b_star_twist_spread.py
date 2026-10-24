try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Family A with spread laws (every coordinate: 5 intervals of length 1/5 in [-8, 8], hub law independent draw).
import numpy as np, time, sys
sys.path.insert(0, '.')
from hublib import *
rng = np.random.default_rng(12)
n = 60
w = rng.choice([-1.0, 1.0], n); w /= np.linalg.norm(w)
v = rng.normal(size=n); v -= (v @ w)*w; v /= np.linalg.norm(v)
G = rng.normal(size=(n, n)); Wm = (G + G.T)/2; Wm /= np.linalg.norm(Wm, 2)
N = 150000
laws = [spread_law(rng, 5, 8.0) for _ in range(n)]
fh = spread_law(rng, 5, 8.0)
t0 = time.time()
def make_sampler(lam, eps):
    def samp(r):
        X = np.empty((N, n))
        for i in range(n):
            X[:, i] = laws[i].sample(r, N)
        L = X @ w; V = X @ v
        R = lam*V*V + eps*np.einsum('ij,ij->i', X @ Wm, X)
        return L, R
    return samp
for lam, eps in [(1.0, 0.0), (-1.0, 0.0), (1.0, 0.1)]:
    samp = make_sampler(lam, eps)
    Lp, Rp = samp(rng)
    # the hub offset beta: put the spread L's centre near the hub critical line; try beta = -median(L) and a shift
    for beta in [-np.median(Lp), -np.median(Lp) + 0.5]:
        row = []
        for a in [0.0, 0.05, 0.3, -0.3]:
            # R + 2 x t has scale set by X_h ~ 8 and |L|; scan a wide window of s
            Q = a*fh.sample(rng, N)**2 + 2*fh.sample(rng, N)*0 + 0  # placeholder not used
            xs = fh.sample(rng, N)
            Qs = a*xs**2 + 2*xs*(Lp + beta) + Rp
            lo, hi = np.percentile(Qs, [5, 95])
            sg = np.linspace(lo, hi, 31)
            d = density_on_grid(a, beta, samp, fh, sg, 1, rng)
            j = int(np.argmax(d))
            s1, dm, _ = refine_max(a, beta, samp, fh, sg[j], (sg[1]-sg[0]), 2, rng, npts=9)
            row.append((a, round(float(dm), 3)))
        print("spread lam", lam, "eps", eps, "beta %.2f" % beta, "max_s p_Q by a:", row, "t=%.0fs" % (time.time()-t0), flush=True)
