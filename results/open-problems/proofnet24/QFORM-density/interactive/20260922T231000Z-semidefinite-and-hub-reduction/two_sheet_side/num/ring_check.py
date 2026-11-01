# Rings on the upper sheet z3 = h(r) = sqrt(1 + r^2) of z1^2 + z2^2 - z3^2 = -1.
# Band k: R_k <= r <= R_k + a, |z3 - h(r)| <= w_k, w_k = c R_k^-3, R_k = 4^k.
# Check: (1) density contribution of each band at level -1; (2) max over many lines of total length inside the bands.
import numpy as np, sys
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
K = int(sys.argv[1]) if len(sys.argv) > 1 else 4
a, c = 0.25, 0.05
R = np.array([4.0**k for k in range(1, K+1)]); w = c / R**3
h = lambda r: np.sqrt(1.0 + r*r)
# (1) contribution of band k to p_Q(-1): D * 2 pi * int_{R_k}^{R_k+a} r dr / (2 h(r)) = D*pi*(h(R_k+a)-h(R_k))
D = 2*np.sqrt(2)
contrib = D*np.pi*(h(R+a) - h(R))
print("per-band contribution to p_Q(-1):", np.round(contrib, 4), " total:", round(contrib.sum(), 3))
print("band masses:", ["%.2e" % m for m in D*2*w*np.pi*((R+a)**2 - R**2)], " total %.3e" % (D*2*w*np.pi*((R+a)**2-R**2)).sum())

def length_inside(p0, e, tmax, n=400001):
    # total length of the line p0 + t e, |t| <= tmax, inside the union of bands (fine grid, refined twice)
    t = np.linspace(-tmax, tmax, n); dt = t[1]-t[0]
    P = p0[None,:] + t[:,None]*e[None,:]
    r = np.hypot(P[:,0], P[:,1]); g = P[:,2] - h(r)
    inside = np.zeros(n, bool)
    for Rk, wk in zip(R, w):
        inside |= (r >= Rk) & (r <= Rk + a) & (np.abs(g) <= wk)
    return inside.sum()*dt, inside

rng = np.random.default_rng(1)
best = 0.0; worst = None
# (2a) lines tangent to the sheet at a point of a band, in random tangent directions, with tiny normal tilts
for k in range(K):
    for trial in range(400):
        r0 = R[k] + a*rng.random(); phi = 2*np.pi*rng.random()
        y0 = r0*np.array([np.cos(phi), np.sin(phi)]); p0 = np.array([y0[0], y0[1], h(r0)])
        n_ = np.array([-y0[0]/h(r0), -y0[1]/h(r0), 1.0]); n_ /= np.linalg.norm(n_)   # normal of the graph
        v = rng.normal(size=3); v -= v.dot(n_)*n_; v /= np.linalg.norm(v)       # tangent direction
        tilt = rng.normal()*1e-3; e = v + tilt*n_; e /= np.linalg.norm(e)
        L, _ = length_inside(p0, e, tmax=2*R[-1]+10, n=800001)
        if L > best: best, worst = L, (k, r0, tilt)
print("max length over %d tangent lines: %.4f  (band, r0, tilt) = %s" % (400*K, best, worst))
# (2b) radial-plane lines tangent to the hyperbola at r* between and inside bands (the near-asymptotic family)
bestr = 0.0
for rstar in np.exp(np.linspace(np.log(1.0), np.log(R[-1]*2), 600)):
    y0 = np.array([rstar, 0.0]); p0 = np.array([rstar, 0.0, h(rstar)])
    e = np.array([1.0, 0.0, rstar/h(rstar)]); e /= np.linalg.norm(e)
    L, _ = length_inside(p0, e, tmax=2*R[-1]+10, n=800001)
    bestr = max(bestr, L)
print("max length over radial tangent lines: %.4f" % bestr)
