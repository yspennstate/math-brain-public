try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
"""Which twists survive the adversarial bump laws?  n = 4, k = 1, v = (1,1,1,1)/2.
 (a) kappa vv^T                     compression kappa            (fatal: ~ 2 pi N)
 (b) kappa (vv^T - diag(v o v))      zero diagonal, compression 3 kappa/4
 (c) kappa R, R random dense symmetric with v^T R v = 0, ||R|| = 1 (zero compression)
 (d) kappa (v w^T + w v^T), w = (1,-1,1,-1)/2  (cross term only, zero compression)
Bump laws as in N2 with separation parameter C (positions scale D = C N/kappa)."""
import numpy as np, sys, math, time
sys.path.insert(0, '.')
from gmix import components, J_k1_windowed

def laws_for(n, N, D, v):
    s0 = 1.0 / (N * math.sqrt(2 * math.pi))
    return [(np.full(N, 1.0 / N), np.array([p * N ** i * D / v[i] for p in range(N)], float), np.full(N, s0)) for i in range(n)]

rng = np.random.default_rng(3)
v = np.full(4, 0.5); w = np.array([1, -1, 1, -1]) / 2.0
R = rng.standard_normal((4, 4)); R = (R + R.T) / 2
R -= (v @ R @ v) * np.outer(v, v)            # kill the compression v^T R v
R /= np.linalg.norm(R, 2)
print("check v^T R v =", float(v @ R @ v), flush=True)
t0 = time.time()
for kappa in [1.0, 0.1]:
    for C in [8.0, 1.0]:
        for N in [2, 3]:
            D = C * N / kappa
            laws = laws_for(4, N, D, v); W, MU, S = components(laws)
            du = min(0.02, 0.1 / D, 0.2 / (kappa * D + 1e-9))
            out = []
            for name, E in [('a', kappa * np.outer(v, v)), ('b', kappa * (np.outer(v, v) - np.diag(v * v))),
                            ('c', kappa * R), ('d', kappa * (np.outer(v, w) + np.outer(w, v)))]:
                out.append(f"{name}:{J_k1_windowed(v, E, W, MU, S, du):7.3f}")
            print(f"kappa={kappa:4.1f} C={C:3.0f} N={N}: " + "  ".join(out) + f"   [{time.time()-t0:.0f}s]", flush=True)
