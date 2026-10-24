try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# M-D2 probe: density of Y = X^T (2 w w^T + 2 v v^T + D) X + b^T X for spread orthonormal w, v and a small diagonal D.
# If sup density stays bounded over laws, n, D and b, the degenerate hub is bounded for every hub law.
import os, sys, time, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "real_variable_hub"))
from fibre_density import Law, density
rng = np.random.default_rng(7)
n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
G = rng.normal(size=(n, 2)); Qm, _ = np.linalg.qr(G); w, v = Qm[:, 0], Qm[:, 1]
lev = w**2 + v**2
print(f"n={n} max leverage {lev.max():.3f}", flush=True)
Ds = {
  "D=0": np.zeros(n),
  "zero-diag": -2 * lev,
  "half-diag": -lev,
  "rand+-0.1": 0.1 * rng.choice([-1, 1], n),
  "-0.1 I": -0.1 * np.ones(n),
  "+0.1 I": 0.1 * np.ones(n),
}
bs = {"b=0": np.zeros(n), "b=4w(hub x=1)": 4 * w, "b rand|1|": rng.normal(size=n) / np.sqrt(n)}
lawsets = {"unif": lambda: [Law('unif', rng) for _ in range(n)],
           "multi M=2": lambda: [Law('multi', rng, M=2, spread=2.3) for _ in range(n)],
           "bumpy N=3": lambda: [Law('bumpy', rng, N=3, spread=1.7) for _ in range(n)]}
t0 = time.time()
for lname, mk in lawsets.items():
    laws = mk()
    Xs = np.stack([laws[i].sample(4000) for i in range(n)], axis=1)
    for dname, d in Ds.items():
        A = 2 * np.outer(w, w) + 2 * np.outer(v, v) + np.diag(d)
        for bname, b in bs.items():
            Yv = np.sum(Xs * (Xs @ A), axis=1) + Xs @ b
            # locate the peak with a histogram, then evaluate the exact estimator on a grid around it
            h, e = np.histogram(Yv, bins=200)
            c = 0.5 * (e[1:] + e[:-1]); w0 = e[1] - e[0]
            k = np.argmax(np.convolve(h, np.ones(3) / 3, mode='same'))
            svals = c[k] + w0 * np.linspace(-4, 4, 9)
            mean, sd = density(A, b, laws, svals, 12000)
            j = np.argmax(mean)
            print(f"{lname:10s} {dname:10s} {bname:14s} peak p={mean[j]:.3f} +- {sd[j]:.3f} at s={svals[j]:.3f}  ({time.time()-t0:.0f}s)", flush=True)
