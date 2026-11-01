try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Stress test of the open core Q = 2 T V + U^2, T = sqrt(l) X_h + eps Z0, two-sheet side s < 0.
# Danger mechanism: Z0 large while V small.  Pairs of coordinates (2j, 2j+1) enter Z0 as a(X+X') and V as
# a(X-X'); their laws are uniform on [-0.45,0.45] u [R_j, R_j+0.1] (density 1), so with probability ~0.01 both
# jump to R_j: Z0 ~ 2 a R_j while V barely moves.  Remaining coordinates uniform, frame re-orthonormalised.
# X_h uniform on [c-1/2, c+1/2]; c is scanned over [-120,120] (the shift eps*2aR/sqrt(l) is where danger sits).
import numpy as np, time
rng = np.random.default_rng(5)
m, N, a = 30, 400000, 0.3
Rs = [10.0, 100.0, 1000.0]
B, _ = np.linalg.qr(rng.standard_normal((m - 6, 3)))
z = np.zeros(m); v = np.zeros(m); u = np.zeros(m)
for j in range(3):
    z[2 * j] = z[2 * j + 1] = a; v[2 * j] = a; v[2 * j + 1] = -a
rest = np.sqrt(1 - 6 * a * a)
z[6:] = rest * B[:, 0]; v[6:] = rest * B[:, 1]; u[6:] = B[:, 2]
print("frame Gram:", np.round(np.stack([z, v, u]) @ np.stack([z, v, u]).T, 3).tolist(), flush=True)
X = rng.uniform(-0.5, 0.5, size=(N, m))
for j in range(3):
    for k in (2 * j, 2 * j + 1):
        far = rng.random(N) < 0.1
        X[:, k] = np.where(far, Rs[j] + rng.uniform(0, 0.1, N), rng.uniform(-0.45, 0.45, N))
Z0, V, U = X @ z, X @ v, X @ u
both = [(X[:, 2 * j] > 5) & (X[:, 2 * j + 1] > 5) for j in range(3)]
print("P(pair j both far):", [round(float(b.mean()), 4) for b in both], flush=True)
svals = -np.concatenate([np.geomspace(2e-3, 0.1, 5), np.linspace(0.2, 2.0, 6)])
cs = np.linspace(-120, 120, 481)
t0 = time.time()
for lval in [0.99, 0.999, 0.9999, 1.0]:
    eps = np.sqrt(1 - lval); sl = np.sqrt(lval)
    best = (0.0, None, None, None)
    for s in svals:
        xs = (s - U ** 2 - 2 * eps * Z0 * V) / (2 * sl * V)
        w = 1.0 / (2 * sl * np.abs(V))
        order = np.argsort(xs); xs_sorted = xs[order]; w_sorted = np.cumsum(w[order])
        # p(c) = mean of w over |xs - c| <= 1/2, via cumulative sums
        lo = np.searchsorted(xs_sorted, cs - 0.5); hi = np.searchsorted(xs_sorted, cs + 0.5)
        tot = np.where(hi > 0, w_sorted[np.maximum(hi - 1, 0)], 0) - np.where(lo > 0, w_sorted[np.maximum(lo - 1, 0)], 0)
        p = tot / N
        k = np.argmax(p)
        if p[k] > best[0]:
            best = (p[k], cs[k], s, None)
    print(f"l={lval:7.5f} eps={eps:6.4f}  sup over c in [-120,120], s<0: {best[0]:.3f} at c={best[1]:+.1f}, s={best[2]:+.4f}  ({time.time()-t0:.0f}s)", flush=True)
