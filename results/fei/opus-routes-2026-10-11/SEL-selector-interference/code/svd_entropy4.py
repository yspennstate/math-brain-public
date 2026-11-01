"""Degenerate singular values: the defect inequality must hold for EVERY SVD.  Build M = sum_k sigma_k u_k v_k^T with
sigma_1 = sigma_2, then rotate the pair (u_1,u_2),(v_1,v_2) by the same angle (still an SVD) and maximise gap/B."""
import numpy as np
def H(p):
    p = np.asarray(p).ravel(); p = p[p > 1e-300]; return float(-(p*np.log2(p)).sum())
rng = np.random.default_rng(5)
worst = -9
for t in range(3000):
    m, n = rng.integers(2, 6, size=2); r = min(m, n)
    U, _ = np.linalg.qr(rng.standard_normal((m, m))); V, _ = np.linalg.qr(rng.standard_normal((n, n)))
    if t % 2 == 0:   # sparse-ish bases (more extreme entropies)
        U = np.linalg.qr(np.eye(m) + 0.2*rng.standard_normal((m, m)))[0]; V = np.linalg.qr(np.eye(n) + 0.2*rng.standard_normal((n, n)))[0]
    s = rng.dirichlet(np.ones(r)); s[1] = s[0]; s = s/s.sum()
    M = (U[:, :r]*np.sqrt(s)) @ V[:, :r].T
    lhs = H(M**2); B = float(np.sum(s*(1-s)))
    for th in np.linspace(0, np.pi, 181):
        c, sn = np.cos(th), np.sin(th)
        U2 = U[:, :r].copy(); V2 = V[:, :r].copy()
        U2[:, 0], U2[:, 1] = c*U[:, 0] + sn*U[:, 1], -sn*U[:, 0] + c*U[:, 1]
        V2[:, 0], V2[:, 1] = c*V[:, 0] + sn*V[:, 1], -sn*V[:, 0] + c*V[:, 1]
        assert np.allclose((U2*np.sqrt(s)) @ V2.T, M)
        rhs = H(s) + sum(s[k]*(H(U2[:, k]**2) + H(V2[:, k]**2)) for k in range(r))
        worst = max(worst, (lhs - rhs)/B)
print('max gap/B over degenerate rotated SVDs:', worst)
