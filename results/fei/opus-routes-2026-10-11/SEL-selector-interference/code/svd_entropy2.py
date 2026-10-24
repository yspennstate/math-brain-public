"""Does H(|M|^2) <= H(s) + sum_k s_k [H(u_k^2)+H(v_k^2)] + kappa * sum_k s_k (1 - s_k) hold for every real matrix
(s = squared singular values, ||M||_F = 1, any SVD) with an absolute kappa?  Report max gap / sum s_k(1-s_k)."""
import numpy as np
def H(p):
    p = np.asarray(p).ravel(); p = p[p > 1e-300]; return float(-(p*np.log2(p)).sum())
rng = np.random.default_rng(12)
worst = (0, None)
for t in range(60000):
    m, n = rng.integers(2, 7, size=2)
    kind = rng.integers(4)
    if kind == 0: M = rng.standard_normal((m, n))
    elif kind == 1: M = rng.integers(-2, 3, size=(m, n)).astype(float)
    elif kind == 2:
        U, _ = np.linalg.qr(rng.standard_normal((m, m))); V, _ = np.linalg.qr(rng.standard_normal((n, n)))
        r = min(m, n); s = rng.dirichlet(np.ones(r)*rng.choice([0.1, 0.5, 2.0]))
        M = (U[:, :r]*np.sqrt(s)) @ V[:, :r].T
    else:
        M = np.zeros((m, n)); r = min(m, n); M[np.arange(r), np.arange(r)] = rng.random(r)
        M += 0.05*rng.standard_normal((m, n))
    if np.linalg.norm(M) == 0: continue
    M = M/np.linalg.norm(M)
    U, sv, Vt = np.linalg.svd(M, full_matrices=False); s = sv**2
    gap = H(M**2) - (H(s) + sum(s[k]*(H(U[:, k]**2) + H(Vt[k]**2)) for k in range(len(s)) if s[k] > 1e-14))
    B = float(np.sum(s*(1-s)))
    if B > 1e-9 and gap/B > worst[0]: worst = (gap/B, gap, B, M.round(3))
print('max gap/B =', worst[0], ' gap =', worst[1], ' B =', worst[2]); print(worst[3])
