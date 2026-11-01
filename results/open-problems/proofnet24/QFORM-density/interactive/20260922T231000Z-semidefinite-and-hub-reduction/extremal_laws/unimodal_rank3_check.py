# Plausibility check for Corollary 4.4 (unimodal laws, rank three): Monte Carlo density of Q = X^T A X + b^T X for
# random rank-three A (eigenvalues of modulus in [1, 3], both signatures), laws with a sharp peak (density e^{-2|x|},
# value 1 at the mode) against laws uniform on unit intervals; largest histogram density over s at bin width 0.02,
# then re-estimated on a fresh sample at the chosen s (so the choice of the top bin does not inflate it).
import numpy as np, json
rng = np.random.default_rng(7)
def run(n, law, A, b, N=2_000_000, h=0.02):
    def sample(k):
        if law == 'laplace2':
            X = rng.laplace(0.0, 0.5, size=(k, n))
        else:
            X = rng.random((k, n)) - 0.5
        return np.einsum('ij,jk,ik->i', X, A, X) + X @ b
    q = sample(N)
    lo, hi = np.percentile(q, 0.1), np.percentile(q, 99.9)
    hist, edges = np.histogram(q, bins=int((hi - lo)/h) + 1, range=(lo, lo + (int((hi - lo)/h) + 1)*h))
    k = int(np.argmax(hist)); s = 0.5*(edges[k] + edges[k + 1])
    q2 = sample(N)
    return float(np.mean(np.abs(q2 - s) <= h/2)/h), float(s)
out = []
for trial in range(8):
    n = int(rng.integers(3, 9))
    Qm, _ = np.linalg.qr(rng.standard_normal((n, 3)))
    lam = rng.uniform(1, 3, size=3)*rng.choice([-1, 1], size=3)
    A = (Qm*lam) @ Qm.T
    b = rng.normal(0, 1, size=n)*rng.choice([0, 1])
    vl, sl = run(n, 'laplace2', A, b)
    vu, su = run(n, 'unif', A, b)
    rec = dict(n=n, eig=[round(x, 2) for x in lam], linear=bool(np.any(b)), laplace2=round(vl, 3), interval=round(vu, 3))
    print(json.dumps(rec), flush=True)
