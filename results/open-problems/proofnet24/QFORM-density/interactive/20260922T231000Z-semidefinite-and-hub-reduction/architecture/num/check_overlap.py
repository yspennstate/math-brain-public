try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, itertools
rng = np.random.default_rng(1)

def esym(y, k):
    e = np.zeros(k+1); e[0] = 1.0
    for v in y:
        for j in range(k, 0, -1):
            e[j] += e[j-1]*v
    return e[k]

def brute(E, L, k):
    n = E.shape[0]
    W = 0.0; O = 0.0; Phi = 0.0
    for S in itertools.combinations(L, k):
        for T in itertools.combinations(range(n), k):
            d = np.linalg.det(E[np.ix_(S, T)])**2
            inter = set(S) & set(T)
            if inter: O += d; Phi += d*len(inter)
            else: W += d
    return W, O, Phi

def phi_formula(E, L, k):
    B0 = E[L, :]
    A, nu, Bt = np.linalg.svd(B0, full_matrices=False)
    Bm = Bt.T   # columns b_r in R^n
    m = len(nu)
    tot = 0.0
    for idx, i in enumerate(L):
        x = A[idx, :]**2          # A_ir^2 (row idx of left sing vecs)
        y = Bm[i, :]**2           # B_ir^2
        ab = A[idx, :]*Bm[i, :]
        t1 = 0.0
        for R in itertools.combinations(range(m), k):
            nuR2 = np.prod(nu[list(R)]**2)
            s = sum(x[r]*y[rp] for r in R for rp in R if r != rp)
            t1 += nuR2*s
        t2 = 0.0
        for Q in itertools.combinations(range(m), k-1):
            nuQ2 = np.prod(nu[list(Q)]**2) if k > 1 else 1.0
            t2 += nuQ2*(sum(nu[r]*ab[r] for r in Q))**2
        tot += t1 + t2
    return tot

def marg_check(B, k):
    p, q = B.shape
    ek = 0.0; ai = np.zeros(p)
    for S in itertools.combinations(range(p), k):
        for T in itertools.combinations(range(q), k):
            d = np.linalg.det(B[np.ix_(S, T)])**2
            ek += d
            for i in S: ai[i] += d
    ai /= ek
    s2 = np.linalg.svd(B, compute_uv=False)**2
    bound = (B**2).sum(1)*esym(s2, k-1)/esym(s2, k)
    return ai.max(), (ai/bound).max(), ai.sum()

worst_ineq = 1e9; worst_formula = 0.0; worst_marg = 0.0
for trial in range(40):
    n = 8
    kind = trial % 4
    if kind == 0:
        E = rng.standard_normal((n, n)); E = (E+E.T)/2
    elif kind == 1:   # hub + rank one + noise
        w = rng.standard_normal(n); w[0] = 0; v = rng.standard_normal(n)
        E = np.outer(np.eye(n)[0], w) + np.outer(w, np.eye(n)[0]) + 0.7*np.outer(v, v) + 0.1*rng.standard_normal((n,n))
        E = (E+E.T)/2
    elif kind == 2:   # two hubs + noise
        w1 = rng.standard_normal(n); w2 = rng.standard_normal(n); w1[:2] = 0; w2[:2] = 0
        e0, e1 = np.eye(n)[0], np.eye(n)[1]
        E = np.outer(e0,w1)+np.outer(w1,e0)+np.outer(e1,w2)+np.outer(w2,e1)+0.2*rng.standard_normal((n,n)); E=(E+E.T)/2
    else:             # low rank minus its diagonal
        U = rng.standard_normal((n, 3)); E = U @ np.diag([1.5, -1, 2]) @ U.T
    np.fill_diagonal(E, 0.0)
    for k in (2, 3):
        L = sorted(rng.choice(n, size=rng.integers(k+1, n+1), replace=False).tolist())
        W, O, Phi = brute(E, L, k)
        nu2 = np.linalg.svd(E[L, :], compute_uv=False)**2
        ek, ek1 = esym(nu2, k), esym(nu2, k-1)
        rho2 = max((E[i, :]**2).sum() for i in L)
        # identities: W + O = e_k(nu^2); Phi(brute, with multiplicity) = formula
        assert abs(W + O - ek) < 1e-8*max(1, ek), (W+O, ek)
        f = phi_formula(E, L, k)
        worst_formula = max(worst_formula, abs(f - Phi)/max(1e-12, Phi))
        slack = (W - (ek - 2*(k-1)*rho2*ek1))/max(ek, 1e-12)
        worst_ineq = min(worst_ineq, slack)
    B = rng.standard_normal((6, 5)) * rng.uniform(0.1, 3, size=(6, 1))
    for k in (1, 2, 3):
        amax, ratio, asum = marg_check(B, k)
        worst_marg = max(worst_marg, ratio)
print("max rel error: Phi formula vs brute (with multiplicity):", worst_formula, flush=True)
print("min normalized slack of W >= e_k - 2(k-1)rho^2 e_{k-1} (must be >= 0):", worst_ineq, flush=True)
print("max ratio marginal / (|b_i|^2 e_{k-1}/e_k) (must be <= 1):", worst_marg, flush=True)
