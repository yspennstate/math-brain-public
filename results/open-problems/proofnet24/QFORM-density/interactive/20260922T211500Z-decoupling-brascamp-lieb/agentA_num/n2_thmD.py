try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# N2: audit of Theorem D ingredients.
# (a) brute-force volume-sampling marginals vs the singular-value formula alpha_i = sum_m p_m u_m(i)^2,
#     p_m = s_m^2 e_{k-1}(s^2_{-m}) / e_k(s^2)   (k=3), and sum alpha = sum beta = 3.
# (b) Lieb-sup check: for random Gaussian parameters (d_i, e_j) the ratio
#     prod d^alpha prod e^(1-beta) / det(D + M^T D_I M)  never exceeds 1/Z.
import itertools, numpy as np
rng = np.random.default_rng(1)
def esym(x, k):
    # elementary symmetric polynomial e_k of vector x
    E = np.zeros(k+1); E[0] = 1.0
    for v in x:
        for j in range(k, 0, -1):
            E[j] += E[j-1]*v
    return E[k]
def brute(M, k=3):
    nI, nJ = M.shape; Z = 0.0; a = np.zeros(nI); b = np.zeros(nJ)
    for S in itertools.combinations(range(nI), k):
        for T in itertools.combinations(range(nJ), k):
            w = np.linalg.det(M[np.ix_(S, T)])**2
            Z += w; a[list(S)] += w; b[list(T)] += w
    return Z, a/Z, b/Z
worst_a = 0; worst_ratio = 0
for trial in range(30):
    nI, nJ = rng.integers(4, 8), rng.integers(3, 7)
    rank = rng.integers(3, min(nI, nJ)+1)
    M = rng.standard_normal((nI, rank)) @ rng.standard_normal((rank, nJ)) * rng.uniform(0.2, 2)
    if trial % 3 == 0:
        M[0] *= 5.0   # a heavy row
    Z, a, b = brute(M)
    U, s, Vt = np.linalg.svd(M, full_matrices=False)
    s2 = s**2; e3 = esym(s2, 3)
    p = np.array([s2[m]*esym(np.delete(s2, m), 2)/e3 for m in range(len(s2))])
    a_formula = (U**2) @ p
    worst_a = max(worst_a, np.max(np.abs(a - a_formula)))
    assert abs(Z - e3)/e3 < 1e-8, (Z, e3)
    assert abs(a.sum()-3) < 1e-8 and abs(b.sum()-3) < 1e-8
    # (b) Gaussian ratio test
    for _ in range(2000):
        d = np.exp(rng.normal(0, 2, nI)); e = np.exp(rng.normal(0, 2, nJ))
        det = np.linalg.det(np.diag(e) + M.T @ np.diag(d) @ M)
        logr = np.sum(a*np.log(d)) + np.sum((1-b)*np.log(e)) - np.log(det) + np.log(Z)
        worst_ratio = max(worst_ratio, logr)
print("max |alpha_brute - alpha_formula| =", worst_a)
print("max over random Gaussians of log( Z * prod d^a prod e^(1-b) / det ) =", worst_ratio, "(must be <= 0)")
