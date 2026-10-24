"""Adversarial search: maximise gap/B for the Schmidt-entropy inequality with defect
   H(|M|^2) <= H(s) + sum_k s_k [H(u_k^2) + H(v_k^2)] + kappa * sum_k s_k (1 - s_k).
Nelder-Mead from many starts in shapes 2x2, 2x3, 3x3, 4x4; also near-rank-one scans."""
import numpy as np
from scipy.optimize import minimize
def H(p):
    p = np.asarray(p).ravel(); p = p[p > 1e-300]; return float(-(p*np.log2(p)).sum())
def ratio(flat, m, n):
    M = flat.reshape(m, n); nm = np.linalg.norm(M)
    if nm == 0: return 0.0
    M = M/nm
    U, sv, Vt = np.linalg.svd(M, full_matrices=False); s = sv**2
    B = float(np.sum(s*(1-s)))
    if B < 1e-10: return 0.0
    gap = H(M**2) - (H(s) + sum(s[k]*(H(U[:, k]**2) + H(Vt[k]**2)) for k in range(len(s)) if s[k] > 1e-15))
    return gap/B
rng = np.random.default_rng(21)
for (m, n) in [(2, 2), (2, 3), (3, 3), (2, 4), (4, 4)]:
    best = (-1, None)
    for start in range(60):
        x0 = rng.standard_normal(m*n)
        if start % 3 == 0:   # near rank one
            x0 = np.outer(rng.standard_normal(m), rng.standard_normal(n)).ravel() + 0.05*rng.standard_normal(m*n)
        res = minimize(lambda z: -ratio(z, m, n), x0, method='Nelder-Mead', options={'maxiter': 4000, 'xatol': 1e-10, 'fatol': 1e-12})
        if -res.fun > best[0]: best = (-res.fun, res.x)
    M = best[1].reshape(m, n); M = M/np.linalg.norm(M)
    U, sv, Vt = np.linalg.svd(M)
    print('%dx%d  max gap/B = %.5f   squared singular values %s' % (m, n, best[0], np.round(sv**2, 6)), flush=True)
    print(np.round(M, 4))
