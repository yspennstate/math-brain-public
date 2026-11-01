try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Checks: (1) identity <B_I g, A_IJ B_J g> = |Lam g|^2/4 - |N g|^2 ;
# (2) brute-force k-volume marginals vs sum_m p_m u_m(i)^2 ;
# (3) p_m <= k sigma_m / sigma_(k) ;
# (4) alpha_i <= 2 m_i^T (M^T M + kappa)^{-1} m_i for kappa = sigma_(k)/k ;
# (5) m_i^T (M^T M + kappa)^{-1} m_i == b_i^T H_J (H_I H_J + kappa)^{-1} b_i  and <= b_i^T (H_I + kappa Lam^{-1})^{-1} b_i
import itertools, numpy as np
rng = np.random.default_rng(12345)

def esym(vals, k):
    e = np.zeros(k + 1); e[0] = 1.0
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e[k]

def brute_marginals(M, k):
    p, q = M.shape
    w = {}
    Z = 0.0
    for S in itertools.combinations(range(p), k):
        for T in itertools.combinations(range(q), k):
            d = np.linalg.det(M[np.ix_(S, T)]) ** 2
            Z += d
            w[(S, T)] = d
    alpha = np.zeros(p)
    for (S, T), d in w.items():
        for i in S:
            alpha[i] += d / Z
    return alpha, Z

def formula_marginals(M, k):
    G = M @ M.T
    sig, U = np.linalg.eigh(G)
    sig = np.clip(sig, 0, None)
    ek = esym(sig, k)
    p = np.array([sig[m] * esym(np.delete(sig, m), k - 1) / ek for m in range(len(sig))])
    alpha = (U ** 2) @ p
    return alpha, ek, sig, p

worst = {"id": 0, "marg": 0, "pm": -np.inf, "ridge": -np.inf, "push": 0, "mono": -np.inf}; count = 0
for trial in range(60):
    n = rng.integers(7, 11)
    r = rng.integers(3, n + 1)
    # PSD with multi-scale spectrum
    Uf, _ = np.linalg.qr(rng.standard_normal((n, n)))
    U = Uf[:, :r]
    lam = np.exp(rng.uniform(-3, 5, size=r))
    Lam = np.diag(lam)
    B = U * np.sqrt(lam)
    A = B @ B.T
    xi = rng.integers(0, 2, size=n)
    if xi.sum() < 4 or (n - xi.sum()) < 4:
        continue
    I = np.where(xi == 1)[0]; J = np.where(xi == 0)[0]
    M = A[np.ix_(I, J)]
    HI = B[I].T @ B[I]; HJ = B[J].T @ B[J]
    N = HI - Lam / 2
    # (1)
    for _ in range(5):
        g = rng.standard_normal(r)
        lhs = (B[I] @ g) @ M @ (B[J] @ g)
        rhs = np.sum((Lam @ g) ** 2) / 4 - np.sum((N @ g) ** 2)
        worst["id"] = max(worst["id"], abs(lhs - rhs) / (1 + abs(rhs)))
    for k in (1, 2, 3):
        if min(len(I), len(J)) < k:
            continue
        ab, Zb = brute_marginals(M, k)
        af, Zf, sig, p = formula_marginals(M, k)
        worst["marg"] = max(worst["marg"], np.max(np.abs(ab - af)))
        sk = np.sort(sig)[::-1][k - 1]
        if sk <= 1e-12:
            continue
        worst["pm"] = max(worst["pm"], np.max(p - k * sig / sk))
        kappa = sk / k; count += 1
        Minv = np.linalg.inv(M.T @ M + kappa * np.eye(M.shape[1]))
        ridge = np.array([M[a] @ Minv @ M[a] for a in range(M.shape[0])])
        worst["ridge"] = max(worst["ridge"], np.max(ab - 2 * ridge))
        # (5)
        push = np.array([B[i] @ HJ @ np.linalg.solve(HI @ HJ + kappa * np.eye(r), B[i]) for i in I])
        worst["push"] = max(worst["push"], np.max(np.abs(push - ridge)))
        mono = np.array([B[i] @ np.linalg.solve(HI + kappa * np.diag(1 / lam), B[i]) for i in I])
        worst["mono"] = max(worst["mono"], np.max(ridge - mono))
print("max |identity error| (relative):", worst["id"], flush=True)
print("max |brute - formula| marginal :", worst["marg"], flush=True)
print("max p_m - k sigma_m/sigma_(k)  :", worst["pm"], "(should be <= 0)", flush=True)
print("max alpha - 2 ridge            :", worst["ridge"], "(should be <= 0)", flush=True)
print("max |push-through - ridge|     :", worst["push"], flush=True)
print("max ridge - (H_I+kappa/Lam) lev :", worst["mono"], "(should be <= 0)", flush=True)
print("cases checked:", count, flush=True)
