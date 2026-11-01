try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# (i) spread hub law (X_h far from 0, so a X_h^2 is large), uniform leaves, beta = -a*x0 puts the critical slab
#     |a x + t| < 1 on the hub mass near x0.  (iii) dense twist with curvature mu along w: R = lam V^2 + mu L^2 + eps X'WX'.
import numpy as np, time, sys
sys.path.insert(0, '.')
from hublib import *
rng = np.random.default_rng(31)
n = 60
w = rng.choice([-1.0, 1.0], n); w /= np.linalg.norm(w)
v = rng.normal(size=n); v -= (v @ w)*w; v /= np.linalg.norm(v)
G = rng.normal(size=(n, n)); Wm = (G + G.T)/2; Wm /= np.linalg.norm(Wm, 2)
N = 200000
law = uniform_law()
t0 = time.time()
def sampler(lam, mu, eps):
    def samp(r):
        X = r.random((N, n)) - 0.5
        L = X @ w; V = X @ v
        R = lam*V*V + mu*L*L + eps*np.einsum('ij,ij->i', X @ Wm, X)
        return L, R
    return samp
def maxdens(a, beta, samp, fh, chunks=2):
    Lp, Rp = samp(rng)
    xs = fh.sample(rng, N)
    Qs = a*xs**2 + 2*xs*(Lp + beta) + Rp
    # scan the central 90% of Q plus a fine window around the median
    lo, hi = np.percentile(Qs, [5, 95])
    sg = np.linspace(lo, hi, 41)
    d = density_on_grid(a, beta, samp, fh, sg, 1, rng)
    j = int(np.argmax(d))
    s1, dm, _ = refine_max(a, beta, samp, fh, sg[j], (sg[1]-sg[0]), chunks, rng, npts=11)
    return s1, dm
print("(i) spread hub law, x0 = centre of the hub interval nearest 12; uniform leaves", flush=True)
fh_sp = Law([-15.1, -6.3, 4.4, 11.9, 17.2], 0.2)
samp = sampler(1.0, 0.0, 0.0)
for a in [0.0, 0.02, 0.1, -0.1]:
    for x0 in [12.0, 17.3]:
        beta = -a*x0
        s1, dm = maxdens(a, beta, samp, fh_sp)
        print("  a %5.2f  x0 %5.1f beta %6.2f : max p_Q %.3f at s %.2f   t=%.0fs" % (a, x0, beta, dm, s1, time.time()-t0), flush=True)
print("(iii) dense twist with curvature mu along w, uniform hub", flush=True)
fh = uniform_law()
for mu in [0.5, 2.0]:
    for eps in [0.0, 0.2]:
        samp = sampler(1.0, mu, eps)
        row = []
        for a in [0.0, 0.1, 0.3, -0.3]:
            s1, dm = maxdens(a, 0.0, samp, fh)
            row.append((a, round(1 - a*mu, 2), round(float(dm), 3)))
        print("  mu %.1f eps %.1f  (a, D_H, max p_Q):" % (mu, eps), row, "t=%.0fs" % (time.time()-t0), flush=True)
