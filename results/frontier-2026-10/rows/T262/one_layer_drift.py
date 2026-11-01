"""T262 Target 2, the drift (agent A, 20 Oct): n E log det M after one critical He ReLU layer, three inputs at tangent
positions p1 = 0, p2, p3 (units of 1/n). Net: chunked Monte Carlo, the log det only. Model (S = W/|x|^2, W ~ Wishart_2(K-1),
K ~ Bin(n, 1/2), then the side contraction D -> D (1 - D/(3 pi n))): computed without sampling. E log det S given K is
psi((K-1)/2) + psi((K-2)/2) - 2 psi(K/2) exactly (about -6/n); the contraction is applied at the input distances.
usage: python one_layer_drift.py n1,n2 reps phi2x,phi3x,phi3y"""
import sys, numpy as np
from scipy.special import digamma
from scipy.stats import binom
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
ns = [int(v) for v in sys.argv[1].split(",")]; reps = int(sys.argv[2])
p2x, p3x, p3y = (float(v) for v in sys.argv[3].split(",")); rng = np.random.default_rng(26222)

def logdet_gram(U, n):
    def ang(a, b): c = np.linalg.norm(U[..., a, :] - U[..., b, :], axis=-1); return 2 * np.arcsin(np.minimum(c / 2, 1)) * n
    d12, d13, d23 = ang(0, 1), ang(0, 2), ang(1, 2)
    off = (d12 ** 2 + d13 ** 2 - d23 ** 2) / 2
    return np.log(d12 ** 2 * d13 ** 2 - off ** 2)

for n in ns:
    def pt(qx, qy):
        r = np.hypot(qx, qy) / n
        return np.array([np.cos(r), np.sin(r) * qx / np.hypot(qx, qy), np.sin(r) * qy / np.hypot(qx, qy)])
    X = np.stack([np.array([1.0, 0, 0]), pt(p2x, 0.0), pt(p3x, p3y)])
    L0 = logdet_gram(X, n)
    B = max(1, int(2e7 // (3 * n))); done = 0; s1 = 0.0; s2 = 0.0
    while done < reps:
        b = min(B, reps - done)
        H = np.maximum(np.einsum('ij,rjn->rin', X, rng.standard_normal((b, 3, n))), 0)
        U = H / np.linalg.norm(H, axis=2, keepdims=True)
        z = logdet_gram(U, n) - L0; s1 += z.sum(); s2 += (z * z).sum(); done += b
    m = s1 / reps; v = s2 / reps - m * m
    # model
    K = np.arange(3, n + 1); pk = binom.pmf(K, n, 0.5); pk /= pk.sum()
    wish = (pk * (digamma((K - 1) / 2) + digamma((K - 2) / 2) - 2 * digamma(K / 2))).sum()
    d0 = np.array([np.hypot(p2x, 0), np.hypot(p3x, p3y), np.hypot(p3x - p2x, p3y)])
    D = d0 * (1 - d0 / (3 * np.pi * n)); off0 = (d0[0]**2 + d0[1]**2 - d0[2]**2) / 2; off = (D[0]**2 + D[1]**2 - D[2]**2) / 2
    contr = np.log(D[0]**2 * D[1]**2 - off**2) - np.log(d0[0]**2 * d0[1]**2 - off0**2)
    print(f"n {n} reps {reps} p2 ({p2x},0) p3 ({p3x},{p3y}): net n E logdet {n*m:+.4f} +/- {n*np.sqrt(v/reps):.4f} | "
          f"model {n*(wish+contr):+.4f} (Wishart {n*wish:+.4f}, contraction {n*contr:+.4f}) | n Var {n*v:.3f}", flush=True)
