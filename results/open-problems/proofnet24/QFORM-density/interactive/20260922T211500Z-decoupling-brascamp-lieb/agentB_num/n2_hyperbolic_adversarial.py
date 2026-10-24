try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Adversarial sets E1,E2 (|E_i|<=1, unions of bins) maximizing the t-integral in the hyperbolic formula.
import numpy as np, sys
rng = np.random.default_rng(7)
BW = 5e-4

def curve(B, delta, T=25.0, N=100001):
    ev, O = np.linalg.eigh(B); mneg, mpos = ev; eneg, epos = O[:, 0], O[:, 1]
    t = np.linspace(-T, T, N); ws = []
    for eps in (1.0, -1.0):
        if delta > 0:
            w = eps*np.sqrt(delta/mpos)*np.cosh(t)*epos[:, None] + np.sqrt(delta/(-mneg))*np.sinh(t)*eneg[:, None]
        else:
            w = np.sqrt(-delta/mpos)*np.sinh(t)*epos[:, None] + eps*np.sqrt(-delta/(-mneg))*np.cosh(t)*eneg[:, None]
        ws.append(w)
    return t, ws

def firstpos(bins_in_order):
    # for each element, the position (in the order) of the first occurrence of its bin
    u, inv = np.unique(bins_in_order, return_inverse=True)
    fp = np.full(len(u), len(bins_in_order), dtype=np.int64)
    np.minimum.at(fp, inv, np.arange(len(bins_in_order)))
    return fp[inv], np.sort(fp)

def best_sets(B, delta):
    t, ws = curve(B, delta); dt = t[1]-t[0]
    W = np.concatenate(ws, axis=1)
    ok = np.all(np.abs(W) < 1e7, axis=0); W = W[:, ok]
    b1 = np.floor(W[0]/BW).astype(np.int64); b2 = np.floor(W[1]/BW).astype(np.int64)
    d1 = np.abs(np.gradient(W[0])); d2 = np.abs(np.gradient(W[1]))
    cap = int(1/BW); best = 0.0
    for lam in np.linspace(0.05, 0.95, 10):
        order = np.argsort(lam*d1 + (1-lam)*d2)
        p1, s1 = firstpos(b1[order]); p2, s2 = firstpos(b2[order])
        # max k with #bins(first k) <= cap on both coordinates
        k1 = s1[cap] if len(s1) > cap else len(order)
        k2 = s2[cap] if len(s2) > cap else len(order)
        k = min(k1, k2)
        val = np.sum((p1 < k) & (p2 < k))*dt
        best = max(best, val)
    ev = np.linalg.eigvalsh(B); D = -ev[0]*ev[1]; Lam = 1/abs(ev[0]) + 1/abs(ev[1])
    return best/(2*np.sqrt(D)), (5.2 + max(0.0, np.log(32/(Lam*abs(delta)))))/np.sqrt(D), best, np.log(1/(Lam*abs(delta)))

def rot(th):
    c, s = np.cos(th), np.sin(th); return np.array([[c, -s], [s, c]])

worst = 0
for trial in range(30):
    th = rng.uniform(0, np.pi); mu1 = np.exp(rng.uniform(-3, 3)); mu2 = -np.exp(rng.uniform(-3, 3))
    delta = np.exp(rng.uniform(-9, 2))*rng.choice([-1, 1])
    B = rot(th) @ np.diag([mu1, mu2]) @ rot(th).T
    dens, bnd, raw, L = best_sets(B, delta); worst = max(worst, dens/bnd)
    print(f"th={th:4.2f} mu=({mu1:7.3f},{mu2:8.3f}) delta={delta:9.2e} dens={dens:8.4f} bnd={bnd:8.3f} "
          f"ratio={dens/bnd:5.3f} raw={raw:6.2f} log(1/(Lam|d|))={L:6.2f}", flush=True)
print("worst ratio dens/bound:", worst)
