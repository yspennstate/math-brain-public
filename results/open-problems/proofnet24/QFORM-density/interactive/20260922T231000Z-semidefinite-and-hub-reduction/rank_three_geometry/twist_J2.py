try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# J(tau) with a tau-adaptive y-grid: |E exp(i((y + tau Z) V + u U))| is non-negligible for y in -tau*range(Z),
# so the y-window is [-Y0 - 4 tau sd(Z), Y0 + 4 tau sd(Z)].  Raw and floor-corrected values are printed.
import numpy as np, time
def frame(m, rng, kind):
    B, _ = np.linalg.qr(rng.standard_normal((m, 3)))
    if kind == 'rand':
        return B
    a = 0.55; B2, _ = np.linalg.qr(rng.standard_normal((m - 2, 3)))
    z = np.zeros(m); v = np.zeros(m); u = np.zeros(m)
    z[0] = z[1] = a / np.sqrt(2); v[0] = a / np.sqrt(2); v[1] = -a / np.sqrt(2)
    z[2:] = np.sqrt(1 - a * a) * B2[:, 0]; v[2:] = np.sqrt(1 - a * a) * B2[:, 1]; u[2:] = B2[:, 2]
    return np.stack([z, v, u], axis=1)
rng = np.random.default_rng(21)
N = 60000
t0 = time.time()
for m, kind in [(60, 'rand'), (60, 'shared'), (12, 'rand')]:
    F = frame(m, rng, kind)
    X = rng.uniform(-0.5, 0.5, size=(N, m))
    Z, V, U = X @ F[:, 0], X @ F[:, 1], X @ F[:, 2]
    sdZ = Z.std()
    out = []
    for tau in [0, 3, 10, 30]:
        Y0, du = 14.0, 0.5
        Yt = Y0 + 4 * tau * sdZ
        ys = np.arange(-Yt, Yt + 1e-9, du); us = np.arange(-Y0, Y0 + 1e-9, du)
        eu = np.exp(1j * np.outer(us, U))            # (nu, N)
        tot = 0.0
        for y in ys:
            ph = np.exp(1j * (y + tau * Z) * V)       # (N,)
            E = eu @ ph / N
            tot += np.abs(E).sum() * du * du
        floor = 0.886 / np.sqrt(N) * (ys.size * us.size) * du * du
        out.append(f"tau={tau:3d}: raw {tot:6.1f} floor {floor:5.1f} corr {tot-floor:6.1f}")
    print(f"m={m} {kind:6s} sd(Z)={sdZ:.3f} | " + " | ".join(out) + f"  ({time.time()-t0:.0f}s)", flush=True)
