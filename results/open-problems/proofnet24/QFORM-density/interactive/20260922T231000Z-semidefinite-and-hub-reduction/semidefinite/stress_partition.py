try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Stress test of Lemma S (s_k(A_IJ) >= theta/4) and of the volume-sampling marginals for
# PSD matrices with small diagonal and multi-scale spectra, random partitions.
import numpy as np
rng = np.random.default_rng(7)

def esym_all(vals, k):
    e = np.zeros(k + 1); e[0] = 1.0
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e

def marg(M, k):
    G = M @ M.T
    sig, U = np.linalg.eigh(G)
    sig = np.clip(sig, 0, None)
    # p_m = sigma_m e_{k-1}(sigma_{-m}) / e_k(sigma): compute e_{k-1}(sigma_{-m}) by deflation
    ek = esym_all(sig, k)
    p = np.zeros_like(sig)
    for m in range(len(sig)):
        # e_j(sigma_{-m}) = e_j - sigma_m e_{j-1}(sigma_{-m}), recursion
        em = np.zeros(k + 1); em[0] = 1.0
        for j in range(1, k + 1):
            em[j] = ek[j] - sig[m] * em[j - 1]
        p[m] = sig[m] * em[k - 1] / ek[k]
    alpha = (U ** 2) @ p
    return alpha, ek[k], np.sort(sig)[::-1]

def make(n, kind):
    Q, _ = np.linalg.qr(rng.standard_normal((n, min(n, 400))))
    if kind == "huge+two":          # Lambda u u^T + v v^T + w w^T + eps P_W
        lam = np.zeros(Q.shape[1]); lam[0] = 0.3 * n; lam[1] = 1.0; lam[2] = 1.0
        lam[3:3 + n // 4] = 0.004
    elif kind == "multiscale":      # eigenvalues 2^j
        L = int(np.log2(0.2 * n)); lam = np.zeros(Q.shape[1])
        lam[:L + 1] = 2.0 ** np.arange(L + 1)
    elif kind == "flat_many":       # projection of rank ~ c n
        lam = np.zeros(Q.shape[1]); lam[: n // 50] = 1.0
    elif kind == "three_plus_bulk":  # exactly three at 1, big bulk just below theta
        lam = np.zeros(Q.shape[1]); lam[:3] = 1.0; lam[3:3 + n // 3] = 0.01
    elif kind == "sparseish":       # eigenvectors = normalized indicators of disjoint blocks, plus huge spread one
        lam = None
    if kind == "sparseish":
        blocks = np.array_split(rng.permutation(n), 3)
        V = np.zeros((n, 4))
        for a, b in enumerate(blocks):
            V[b, a] = 1 / np.sqrt(len(b))
        v = rng.standard_normal(n); v -= V[:, :3] @ (V[:, :3].T @ v); V[:, 3] = v / np.linalg.norm(v)
        lam = np.array([1.0, 1.0, 1.0, 0.25 * n])
        A = (V * lam) @ V.T
        return A
    A = (Q * lam) @ Q.T
    return A

for kind in ["huge+two", "multiscale", "flat_many", "three_plus_bulk", "sparseish"]:
    for n in (200, 600):
        A = make(n, kind)
        A = (A + A.T) / 2
        c = np.max(np.diag(A))
        ev = np.sort(np.linalg.eigvalsh(A))[::-1]
        n_ge1 = int(np.sum(ev >= 1 - 1e-9)); n_ge_theta = int(np.sum(ev >= 0.2887))
        res = []
        for rep in range(20):
            xi = rng.integers(0, 2, size=n).astype(bool)
            I = np.where(xi)[0]; J = np.where(~xi)[0]
            M = A[np.ix_(I, J)]
            alpha, Z, s2 = marg(M, 3)
            res.append((np.sqrt(s2[2]), np.max(alpha), Z))
        res = np.array(res)
        print(f"{kind:16s} n={n:4d} maxdiag c={c:.4f} #eig>=1:{n_ge1:3d} #eig>=.29:{n_ge_theta:3d} lam_max={ev[0]:.1f} | "
              f"s3 min={res[:,0].min():.3f} med={np.median(res[:,0]):.3f} | max alpha3 max={res[:,1].max():.4f} "
              f"(55.4c={55.4*c:.3f}) | Z3 min={res[:,2].min():.3g}", flush=True)
