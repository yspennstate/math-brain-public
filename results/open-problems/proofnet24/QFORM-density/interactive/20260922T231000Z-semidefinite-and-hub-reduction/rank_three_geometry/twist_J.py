try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# J(tau) = int int |E exp(i(yV + uU + tau Z0 V))| dy du for light orthonormal (Z0,V,U), Monte Carlo on a grid.
# Noise floor of |E_N| where the truth is 0 is ~ 0.886/sqrt(N); we report J raw and J with the floor removed.
import numpy as np, time
def frame(m, rng, kind):
    if kind == 'rand':
        B, _ = np.linalg.qr(rng.standard_normal((m, 3)))
        return B
    if kind == 'shared':   # Z0 and V share two coordinates hyperbolically, still light (entries^2 <= 1/2 overall)
        B, _ = np.linalg.qr(rng.standard_normal((m - 2, 3)))
        a = 0.55
        z = np.zeros(m); v = np.zeros(m); u = np.zeros(m)
        z[0] = z[1] = a / np.sqrt(2); v[0] = a / np.sqrt(2); v[1] = -a / np.sqrt(2)
        z[2:] = np.sqrt(1 - a * a) * B[:, 0]; v[2:] = np.sqrt(1 - a * a) * B[:, 1]; u[2:] = B[:, 2]
        return np.stack([z, v, u], axis=1)
def sample(law, N, m, rng):
    if law == 'unif':
        return rng.uniform(-0.5, 0.5, size=(N, m))
    # comb law: 3 teeth of width 1/3 at spacing 2 (density 1): far from Gaussian, sd ~ 1.6
    k = rng.integers(0, 3, size=(N, m)); return (k - 1) * 2.0 + rng.uniform(-1 / 6, 1 / 6, size=(N, m))
def J(tau, F, X, Y, nG):
    Zs, Vs, Us = X @ F[:, 0], X @ F[:, 1], X @ F[:, 2]
    ys = np.linspace(-Y, Y, nG); dy = ys[1] - ys[0]
    tot = 0.0
    for y in ys:
        ph = np.exp(1j * ((y + tau * Zs) * Vs))                # N
        E = (ph[None, :] * np.exp(1j * np.outer(ys, Us))).mean(axis=1)   # over u grid
        tot += np.abs(E).sum() * dy * dy
    floor = 0.886 / np.sqrt(len(Zs)) * (2 * Y) ** 2
    return tot, tot - floor
rng = np.random.default_rng(3)
t0 = time.time()
for m, kind, law, Y in [(60, 'rand', 'unif', 16.0), (8, 'rand', 'unif', 16.0), (60, 'shared', 'unif', 16.0), (60, 'rand', 'comb', 6.0), (10, 'rand', 'comb', 6.0)]:
    F = frame(m, rng, kind)
    lev = (F ** 2).sum(axis=1).max()
    X = sample(law, 40000, m, rng)
    row = []
    for tau in [0, 1, 3, 10, 30, 100]:
        raw, cor = J(tau, F, X, Y, 49)
        row.append(f"{tau}:{cor:6.1f}")
    print(f"m={m:3d} {kind:6s} {law:4s} max leverage {lev:.3f}  J(tau) floor-corrected  " + "  ".join(row) + f"   ({time.time()-t0:.0f}s)", flush=True)
