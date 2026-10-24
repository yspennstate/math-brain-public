# Sanity check for Proposition 3 of curved_marginal (unimodal laws, no leverage condition): Monte Carlo density of
# U + c (V - b)^2 for laws e^{-2|x|} (value 1 at the mode) and for unit intervals, on random orthonormal pairs (u, v)
# in R^m, m = 2..12, NOT restricted to leverages <= 1/2; largest histogram density over s (bin 0.02) re-estimated on a
# fresh sample, maximised over c in {0.01, 0.1, 1, 10} and three vertex positions b.
import numpy as np, json
rng = np.random.default_rng(11)
def dens(u, v, law, c, b, N=1_000_000, h=0.02):
    def sample(k):
        X = rng.laplace(0.0, 0.5, size=(k, len(u))) if law == 'lap' else rng.random((k, len(u))) - 0.5
        return X @ u + c*(X @ v - b)**2
    q = sample(N)
    lo, hi = np.percentile(q, 0.05), np.percentile(q, 99.95)
    nb = int((hi - lo)/h) + 1
    hist, edges = np.histogram(q, bins=nb, range=(lo, lo + nb*h))
    k = int(np.argmax(hist)); s = 0.5*(edges[k] + edges[k + 1])
    return float(np.mean(np.abs(sample(N) - s) <= h/2)/h)
for trial in range(10):
    m = int(rng.integers(2, 13))
    Qm, _ = np.linalg.qr(rng.standard_normal((m, 2))); u, v = Qm[:, 0], Qm[:, 1]
    lev = float(np.max(u**2 + v**2))
    best = {}
    for law in ('lap', 'unif'):
        best[law] = max(dens(u, v, law, c, b) for c in (0.01, 0.1, 1.0, 10.0) for b in (-1.0, 0.0, 1.0))
    print(json.dumps(dict(m=m, max_leverage=round(lev, 3), laplace2=round(best['lap'], 3), interval=round(best['unif'], 3))), flush=True)
