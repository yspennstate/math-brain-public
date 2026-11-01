try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Negative controls: the checks must FAIL for deliberately wrong statements.
#  (a) identity without the -|Ng|^2 term;
#  (b) Lemma 3.1 without the factor 2 (alpha_i <= ridge_i);
#  (c) Lemma 3.1 with kappa = sigma_k (too large, the lemma needs kappa <= sigma_k/k), factor 2 kept;
#  (d) p_m <= sigma_m/sigma_k (dropping the factor k);
#  (e) Lemma 2.2 with a too-strong conclusion s_k >= theta/1.2 under S_K <= 1/8;
#  (f) Lemma 3.2 monotonicity with Lambda replaced by Lambda/4 (false direction should appear).
import itertools, numpy as np
rng = np.random.default_rng(4242)

def esym(vals, k):
    e = np.zeros(k + 1); e[0] = 1.0
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e[k]

def formula_marginals(M, k):
    G = M @ M.T
    sig, U = np.linalg.eigh(G); sig = np.clip(sig, 0, None)
    ek = esym(sig, k)
    p = np.array([sig[m] * esym(np.delete(sig, m), k - 1) / ek for m in range(len(sig))])
    return (U ** 2) @ p, sig, p

cnt = dict(a=0, b=0, c=0, d=0, e=0, f=0); tot = dict(a=0, b=0, c=0, d=0, e=0, f=0)
for trial in range(80):
    n = int(rng.integers(8, 14)); r = int(rng.integers(3, n + 1))
    Uf, _ = np.linalg.qr(rng.standard_normal((n, n))); U = Uf[:, :r]
    lam = np.exp(rng.uniform(-3, 4, size=r)); Lam = np.diag(lam)
    B = U * np.sqrt(lam); A = B @ B.T
    xi = rng.integers(0, 2, size=n)
    I = np.where(xi == 1)[0]; J = np.where(xi == 0)[0]
    if len(I) < 3 or len(J) < 3:
        continue
    M = A[np.ix_(I, J)]; HI = B[I].T @ B[I]; HJ = B[J].T @ B[J]; N = HI - Lam / 2
    g = rng.standard_normal(r)
    lhs = (B[I] @ g) @ M @ (B[J] @ g); wrong = np.sum((Lam @ g) ** 2) / 4
    tot["a"] += 1; cnt["a"] += abs(lhs - wrong) > 1e-6 * (1 + abs(wrong))
    for k in (1, 2, 3):
        alpha, sig, p = formula_marginals(M, k)
        sk = np.sort(sig)[::-1][k - 1]
        if sk < 1e-10:
            continue
        def ridge(kap):
            Minv = np.linalg.inv(M.T @ M + kap * np.eye(M.shape[1]))
            return np.array([M[a] @ Minv @ M[a] for a in range(M.shape[0])])
        tot["b"] += 1; cnt["b"] += np.any(alpha > ridge(sk / k) + 1e-12)
        tot["c"] += 1; cnt["c"] += np.any(alpha > 2 * ridge(sk) + 1e-12)
        tot["d"] += 1; cnt["d"] += np.any(p > sig / sk + 1e-12)
        kap = sk / k
        mono_wrong = np.array([B[i] @ np.linalg.solve(HI + kap * np.diag(4 / lam), B[i]) for i in I])
        tot["f"] += 1; cnt["f"] += np.any(ridge(kap) > mono_wrong + 1e-12)
        # (e): choose K = top-k of lam; if S_K <= 1/8 test the too-strong conclusion
        order = np.argsort(-lam); K = order[:k]; theta = lam[K].min()
        SK = sum(np.sum(N[:, m] ** 2) / lam[m] ** 2 for m in K)
        if SK <= 1 / 8:
            tot["e"] += 1; cnt["e"] += np.sqrt(sk) < theta / 1.2
for key, lab in zip("abcdef", ["identity w/o |Ng|^2", "alpha <= ridge (no factor 2)", "kappa = sigma_k",
                              "p_m <= sigma_m/sigma_k", "s_k >= theta/1.2", "Lambda/4 in monotonicity"]):
    print(f"({key}) {lab:30s}: violated in {cnt[key]}/{tot[key]} cases (should be > 0)", flush=True)
