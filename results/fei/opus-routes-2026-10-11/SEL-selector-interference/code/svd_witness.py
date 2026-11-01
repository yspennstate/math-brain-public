import numpy as np
def H(p):
    p = np.asarray(p).ravel(); p = p[p > 1e-300]; return float(-(p*np.log2(p)).sum())
def gap(M):
    M = M/np.linalg.norm(M); U, s, Vt = np.linalg.svd(M, full_matrices=False); V = Vt.T; w = s**2
    return H(M**2) - (H(w) + sum(w[k]*(H(U[:,k]**2)+H(V[:,k]**2)) for k in range(len(s)) if w[k] > 1e-15))
rng = np.random.default_rng(7); best = (-9, None)
for t in range(200000):
    M = rng.integers(-2, 3, size=(2, 2)).astype(float)
    if np.linalg.norm(M) == 0 or abs(np.linalg.det(M)) < 1e-9: continue
    g = gap(M)
    if g > best[0]: best = (g, M.copy())
print(best)
