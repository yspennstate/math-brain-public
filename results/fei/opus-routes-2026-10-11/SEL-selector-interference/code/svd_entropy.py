"""Is H(|M|^2) <= H(sigma^2) + sum_k sigma_k^2 [H(u_k^2) + H(v_k^2)] for every real matrix M with ||M||_F = 1
and every SVD M = sum_k sigma_k u_k v_k^T ?  (Would imply T1-sharp.)  Random and adversarial tests."""
import numpy as np
from scipy.linalg import hadamard
def H(p):
    p = np.asarray(p).ravel(); p = p[p > 1e-300]; return float(-(p*np.log2(p)).sum())
def gap(M, U=None, s=None, V=None):
    M = M/np.linalg.norm(M)
    if U is None:
        U, s, Vt = np.linalg.svd(M, full_matrices=False); V = Vt.T
    lhs = H(M**2)
    w = s**2
    rhs = H(w) + sum(w[k]*(H(U[:,k]**2) + H(V[:,k]**2)) for k in range(len(s)) if w[k] > 1e-15)
    return lhs - rhs
rng = np.random.default_rng(3)
worst = -9
for t in range(20000):
    m, n = rng.integers(2, 9, size=2)
    kind = rng.integers(4)
    if kind == 0: M = rng.standard_normal((m, n))
    elif kind == 1: M = rng.standard_normal((m, n)) * (rng.random((m, n)) < 0.4)
    elif kind == 2:
        r = rng.integers(1, min(m, n)+1)
        M = rng.standard_normal((m, r)) @ rng.standard_normal((r, n))
    else:
        M = np.sign(rng.standard_normal((m, n))) * (rng.random((m, n)) < 0.7)
    if np.linalg.norm(M) == 0: continue
    worst = max(worst, gap(M))
print('random matrices: max(lhs - rhs) =', worst)
# degenerate singular values: Hadamard with rotated bases inside the degenerate space
worst2 = -9
for N in (2, 4, 8):
    Hm = hadamard(N) / np.sqrt(N)
    for t in range(3000):
        Q, _ = np.linalg.qr(rng.standard_normal((N, N)))
        U = Q; V = Hm.T @ Q        # M = Hm/sqrt(N) = sum_k (1/sqrt N) u_k v_k^T with u_k=Q e_k, v_k=Hm^T u_k
        s = np.ones(N)/np.sqrt(N)
        worst2 = max(worst2, gap(Hm/np.sqrt(N), U, s, V))
print('Hadamard, rotated degenerate SVD bases: max(lhs - rhs) =', worst2)
