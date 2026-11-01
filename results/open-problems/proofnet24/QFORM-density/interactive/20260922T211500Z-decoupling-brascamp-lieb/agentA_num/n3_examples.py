try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# N3: empirical |phi(t)| and max density for the new Fourier classes vs the proved bounds.
import numpy as np, sys
rng = np.random.default_rng(7)
def sampler(kind, size):
    if kind == 'unif':
        return rng.uniform(-0.5, 0.5, size)
    if kind == 'latt':   # density 1 on 10 intervals of length 0.1, spacing 3 (lattice-like)
        k = rng.integers(-5, 5, size); return 3.0*k + rng.uniform(-0.05, 0.05, size)
    raise ValueError
def run(name, qfun, n, kinds, ts, bound_phi, bound_dens, N=3_000_000, batch=200_000, h=0.01):
    vals = []
    for s in range(0, N, batch):
        X = np.empty((batch, n))
        for j in range(n):
            X[:, j] = sampler(kinds[j], batch)
        vals.append(qfun(X))
    q = np.concatenate(vals)
    phis = [abs(np.mean(np.exp(1j*t*q))) for t in ts]
    lo, hi = np.quantile(q, [1e-4, 1-1e-4])
    cnt, edges = np.histogram(q, bins=np.arange(lo, hi+h, h))
    dens = cnt.max()/(len(q)*h)
    print(f"{name}: n={n}  max hist density={dens:.3f}  (proved bound {bound_dens:.2f})")
    for t, p in zip(ts, phis):
        b = bound_phi(t) if bound_phi else float('nan')
        print(f"   t={t:7.1f}  |phi|={p:.4f}   bound={b:.4f}   MC noise~{1/np.sqrt(len(q)):.4f}")
    sys.stdout.flush()
ts = [2, 5, 10, 20, 50]
# A: diagonal + spread rank 3 (Fresnel-BL): bound |phi|<=(4pi)^{3/2}|t|^{-3/2}|l1l2l3|^{-1/2}, density<=12|l1l2l3|^{-1/3}
n = 40
R, _ = np.linalg.qr(rng.standard_normal((n, 3)))
lev = (R**2).sum(1).max()
lam = np.array([1.0, 1.0, -1.0]); d = rng.uniform(-3, 3, n)
A = R @ np.diag(lam) @ R.T + np.diag(d)
print("A: max leverage of frame =", round(lev, 3))
for kind in ['unif', 'latt']:
    run(f"A diag+rank3 [{kind}]", lambda X: np.einsum('bi,ij,bj->b', X, A, X), n, [kind]*n, ts,
        lambda t: (4*np.pi)**1.5*t**-1.5, 12.0)
# B: Q = 2 X_1 G + Y^2, G=<g,X_L>, Y=<r2,X_L>, g ⟂ r2 unit spread (mixed Fresnel |H|=1, r=1)
n = 60
F, _ = np.linalg.qr(rng.standard_normal((n-1, 2))); g, r2 = F[:, 0], F[:, 1]
for k1 in ['unif', 'latt']:
    run(f"B 2X1G+Y^2 [X1 {k1}]", lambda X: 2*X[:, 0]*(X[:, 1:] @ g) + (X[:, 1:] @ r2)**2, n,
        [k1] + ['unif']*(n-1), ts, lambda t: (4*np.pi)**1.5/2*t**-1.5, 3/np.pi*((4*np.pi)**1.5/2)**(2/3))
# C: three hyperbolic pairs: |phi|<=(pi/|t|)^{3/2}, density <= 3
for kind in ['unif', 'latt']:
    run(f"C 2(X1X2+X3X4+X5X6) [{kind}]", lambda X: 2*(X[:, 0]*X[:, 1]+X[:, 2]*X[:, 3]+X[:, 4]*X[:, 5]), 6,
        [kind]*6, ts, lambda t: (np.pi/t)**1.5, 3.0)
# D: n=3 zero diagonal (geometric peel, bound not optimised)
for kind in ['unif', 'latt']:
    run(f"D 2(X1X2+X2X3+X1X3) [{kind}]", lambda X: 2*(X[:, 0]*X[:, 1]+X[:, 1]*X[:, 2]+X[:, 0]*X[:, 2]), 3,
        [kind]*3, ts, None, float('nan'))
