try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Hub examples (Prop 5.4, 5.5): exact conditional estimators (no binning), uniform and spread laws.
import numpy as np
rng = np.random.default_rng(5)
n1 = 60                                  # number of leaf coordinates
def leaves(N, kind):
    if kind == 'unif': return rng.uniform(-0.5, 0.5, (n1, N))
    # spread: each coordinate uniform on 4 intervals of length 1/4 at random far positions
    pos = rng.uniform(-20, 20, (n1, 4)); k = rng.integers(0, 4, (n1, N))
    return np.take_along_axis(pos, k, 1) + rng.uniform(0, 0.25, (n1, N))
def f_unif(x): return ((x >= -0.5) & (x < 0.5)).astype(float)
Q, _ = np.linalg.qr(rng.normal(size=(n1, 3)))
w, v, u = Q[:, 0], Q[:, 1], Q[:, 2]
N = 400000
for kind in ('unif', 'spread'):
    Xp = leaves(N, kind); L = w @ Xp; V = v @ Xp; U = u @ Xp
    for lam in (1.0, -1.0, 4.0):
        for beta in (0.0, 0.3):
            # Prop 5.4: Q = 2(L+beta) X_h + lam V^2 ; X_h uniform[-1/2,1/2]
            Vc = V - V.mean()
            svals = np.linspace(-2, 2, 81)
            dens = [np.mean(f_unif((s - lam*Vc**2)/(2*(L - L.mean() + beta)))/(2*np.abs(L - L.mean() + beta))) for s in svals]
            print(f"[5.4] leaves={kind:6s} lam={lam:+.0f} beta={beta:.1f}: max_s p_Q ~ {max(dens):.3f}  (bound {0.5+16/np.sqrt(abs(lam)):.1f})")
    # Prop 5.5: two hubs, arbitrary R(X'') = 3 U^2 - 2 L V + linear
    L1, L2 = L - L.mean(), V - V.mean(); Rr = 3*(U - U.mean())**2 - 2*L1*L2 + 0.7*L1
    # conditional density of c1 X1 + c2 X2 (X1,X2 uniform[-1/2,1/2]) at s - R: trapezoid density
    def trap(z, a, b):
        a, b = np.abs(a), np.abs(b); lo, hi = np.minimum(a, b), np.maximum(a, b)
        z = np.abs(z); top = 1/hi
        return np.where(z <= (hi - lo)/2, top, np.where(z <= (hi + lo)/2, top*((hi + lo)/2 - z)/lo, 0.0))
    c1, c2 = 2*L1, 2*L2
    dens = [np.mean(trap(s - Rr, c1, c2)) for s in np.linspace(-2, 2, 81)]
    print(f"[5.5] leaves={kind:6s}: max_s p_Q ~ {max(dens):.3f}   (bound 8.5 for orthonormal hub rows)")
