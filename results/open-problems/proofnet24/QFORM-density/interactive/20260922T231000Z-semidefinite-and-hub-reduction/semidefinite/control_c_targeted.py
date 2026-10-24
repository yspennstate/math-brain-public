try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from itertools import combinations
# M = U diag(s) V^T with s = (1,1,1,eps), left vector of eps localized on row 0.
def esym(vals, k):
    e = np.zeros(k + 1); e[0] = 1.0
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e[k]
rng = np.random.default_rng(1)
p, q, k = 7, 6, 3
for eps in (0.3, 0.1, 0.03):
    Ul = np.zeros((p, 4)); Ul[0, 3] = 1.0
    X = rng.standard_normal((p - 1, 3)); Qx, _ = np.linalg.qr(X); Ul[1:, :3] = Qx
    V, _ = np.linalg.qr(rng.standard_normal((q, 4)))
    s = np.array([1, 1, 1, eps])
    M = Ul @ np.diag(s) @ V.T
    # brute-force k-volume marginal of row 0
    Z = 0; a0 = 0
    for S in combinations(range(p), k):
        for T in combinations(range(q), k):
            d = np.linalg.det(M[np.ix_(S, T)]) ** 2
            Z += d; a0 += d * (0 in S)
    a0 /= Z
    sig = np.sort(np.linalg.eigvalsh(M @ M.T))[::-1]; sk = sig[k - 1]
    def ridge(kap):
        return M[0] @ np.linalg.solve(M.T @ M + kap * np.eye(q), M[0])
    print(f"eps={eps}: alpha_0={a0:.5f}  2*ridge(kappa=sigma_k)={2*ridge(sk):.5f}  2*ridge(kappa=sigma_k/k)={2*ridge(sk/k):.5f}", flush=True)
