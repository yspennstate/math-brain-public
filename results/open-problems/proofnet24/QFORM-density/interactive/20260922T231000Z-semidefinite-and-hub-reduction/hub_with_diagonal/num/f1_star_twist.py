try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Family A: star + rank one + eps W with hub diagonal a.  Q = a Xh^2 + 2 Xh (L + beta) + lam V^2 + eps X'^T W X' + b.X'
import numpy as np, time, sys
sys.path.insert(0, '.')
from hublib import *
rng = np.random.default_rng(11)
n = 60
w = rng.choice([-1.0, 1.0], n); w /= np.linalg.norm(w)
v = rng.normal(size=n); v -= (v @ w)*w; v /= np.linalg.norm(v)
G = rng.normal(size=(n, n)); Wm = (G + G.T)/2; Wm /= np.linalg.norm(Wm, 2)
N = 200000
t0 = time.time()
def make_sampler(lam, eps, law, bvec):
    def samp(r):
        X = np.empty((N, n))
        for i in range(n):
            X[:, i] = law.sample(r, N)
        L = X @ w; V = X @ v
        R = lam*V*V + eps*np.einsum('ij,ij->i', X @ Wm, X) + X @ bvec
        return L, R
    return samp
laws = {'unif': uniform_law(), 'spread': spread_law(rng, 5, 8.0)}
print("n", n, "N per chunk", N, flush=True)
for lawname in ['unif', 'spread']:
    law = laws[lawname]
    fh = law
    for lam in [1.0, -1.0]:
        for eps in [0.0, 0.2]:
            for beta in [0.0, 0.4]:
                bvec = np.zeros(n)
                samp = make_sampler(lam, eps, law, bvec)
                # locate the peak region with a coarse scan at a = 0, then reuse the window for all a
                row = []
                for a in [0.0, 0.02, 0.1, 0.3, -0.1, -0.3]:
                    # coarse scan over s: centre from a pilot sample
                    Lp, Rp = samp(rng)
                    med = np.median(Rp); spr = np.percentile(Rp, 90) - np.percentile(Rp, 10) + 1.0
                    sg = np.linspace(med - spr, med + spr, 41)
                    d = density_on_grid(a, beta, samp, fh, sg, 1, rng)
                    j = int(np.argmax(d))
                    s1, dm, _ = refine_max(a, beta, samp, fh, sg[j], (sg[1]-sg[0]), 3, rng, npts=11)
                    row.append((a, round(float(dm), 3)))
                print(lawname, "lam", lam, "eps", eps, "beta", beta, "max_s p_Q by a:", row, "t=%.0fs" % (time.time()-t0), flush=True)
