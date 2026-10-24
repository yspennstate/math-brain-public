try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# N6: try to break Theorem F near its edge: few coordinates (n = 6..8), max leverage close to 1/2,
# arbitrary diagonal (including the choice making A zero-diagonal), uniform / resonant / shifted laws.
import numpy as np
rng = np.random.default_rng(21)
def frame(n, target=0.5, tries=4000):
    if n == 6:   # all leverages exactly 1/2: pair-sum frame rotated by a random O(3)
        O, _ = np.linalg.qr(rng.standard_normal((3, 3)))
        R = np.vstack([np.eye(3), np.eye(3)])/np.sqrt(2) @ O
        return R, (R**2).sum(1).max()
    best = None
    for _ in range(tries):
        R, _ = np.linalg.qr(rng.standard_normal((n, 3))); lev = (R**2).sum(1).max()
        if lev <= target and (best is None or lev > best[1]): best = (R, lev)
    return best
def maxdens(q, h=0.01):
    lo, hi = np.quantile(q, [1e-5, 1-1e-5]); c, _ = np.histogram(q, bins=np.arange(lo, hi+h, h))
    return c.max()/(len(q)*h)
def law(kind, N):
    if kind == 'unif': return rng.uniform(-0.5, 0.5, N)
    if kind == 'shift': return rng.uniform(0, 1, N)
    if kind == 'res':   # density 1 on {x in [0,R]: cos(8 x^2) >= 0}
        xs = np.linspace(0, 4, 400_001); g = np.cos(8*xs*xs) >= 0; cum = np.cumsum(g)*(xs[1]-xs[0])
        R = xs[np.searchsorted(cum, 1.0)]; pts = xs[(xs <= R) & g]
        return rng.choice(pts, N) + rng.uniform(0, xs[1]-xs[0], N)
worst_phi, worst_d = 0, 0
for n in [6, 8, 10]:
    R, lev = frame(n)
    lam = np.array([1.0, 1.0, -1.0]); B3 = R @ np.diag(lam) @ R.T
    for dname, D in [("zero-diag A", -np.diag(np.diag(B3))), ("D=0", np.zeros((n, n))), ("D random", np.diag(rng.uniform(-2, 2, n)))]:
        A = B3 + D
        for kind in ['unif', 'shift', 'res']:
            X = np.stack([law(kind, 1_500_000) for _ in range(n)], 1)
            q = np.einsum('bi,ij,bj->b', X, A, X)
            d = maxdens(q); worst_d = max(worst_d, d/12)
            ratios = [abs(np.mean(np.exp(1j*t*q)))*t**1.5/(4*np.pi)**1.5 for t in [3, 6, 12, 24]]
            worst_phi = max(worst_phi, max(ratios))
            print(f"n={n} lev={lev:.3f} {dname:11s} {kind:5s}: max density {d:.3f} (bound 12);  |phi| t^1.5/(4pi)^1.5 at t=3,6,12,24: "
                  + " ".join(f"{r:.3f}" for r in ratios))
print("worst density/bound =", round(worst_d, 3), "  worst |phi|/bound =", round(worst_phi, 3), " (MC noise at t=24 ~ 0.05 in these units)")
