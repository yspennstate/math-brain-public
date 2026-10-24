try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from itertools import combinations
rng = np.random.default_rng(7)

def e2(lams):
    s = lams.sum(); return 0.5*(s*s - (lams**2).sum())

def marg2_formula(A):
    G = A @ A.T
    tr = np.trace(G); G2 = G @ G
    return (np.diag(G)*tr - np.diag(G2))/e2(np.linalg.eigvalsh(G))

def marg2_brute(A):
    p, q = A.shape
    Z = 0.0; row = np.zeros(p)
    for S in combinations(range(p), 2):
        for T in combinations(range(q), 2):
            d = np.linalg.det(A[np.ix_(S, T)])**2
            Z += d; row[list(S)] += d
    return row/Z

# (1) marginal formula vs brute force
for trial in range(3):
    A = rng.normal(size=(6, 7)); A[0] *= 5
    print("marginal formula max err:", np.abs(marg2_formula(A) - marg2_brute(A)).max(), flush=True)

# (2) identity N^(h)_ij = -det M_{hi,hj} and eigen-test
n = 9
M = rng.normal(size=(n, n)); M = (M + M.T)/2
h = 3
m = M[:, h]
N = np.outer(m, m) - M[h, h]*M
err = 0.0
for i in range(n):
    for j in range(n):
        if i == h or j == h: continue
        d = M[h, h]*M[i, j] - M[h, i]*M[h, j]
        err = max(err, abs(N[i, j] + d))
print("identity N = -minors, max err:", err, " h-row of N:", np.abs(N[h]).max(), flush=True)
mu, V = np.linalg.eigh(M)
lhs = np.linalg.norm(N, 2)
rhs = max(abs(mu[k])*(abs(mu[k])*V[h, k]**2 - abs(M[h, h])) for k in range(n))
print("eigen-test ||N|| >= max_k |mu|(|mu| v^2 - |m_hh|):", lhs, ">=", rhs, flush=True)

# (3) STEP B: huge spread square + second eigen-direction + sub-threshold hub, zero diagonal
def build(n, K, mu2, hub_size, noise, rng):
    v1 = rng.choice([-1.0, 1.0], size=n)/np.sqrt(n)
    v2 = rng.normal(size=n); v2 -= (v2 @ v1)*v1; v2 /= np.linalg.norm(v2)
    M = K*np.outer(v1, v1) + mu2*np.outer(v2, v2)
    if hub_size > 0:
        hh = 0
        w = rng.normal(size=n); w[hh] = 0; w /= np.linalg.norm(w)
        H = np.zeros((n, n)); H[hh, :] = w; H[:, hh] = w
        M += hub_size*H
    W = rng.normal(size=(n, n)); W = (W + W.T)/np.sqrt(2*n)
    M += noise*W
    np.fill_diagonal(M, 0.0)
    return M

def analyse(M, rng, parts=8):
    n = M.shape[0]
    mu, V = np.linalg.eigh(M)
    order = np.argsort(-np.abs(mu)); mu = mu[order]; V = V[:, order]
    # no-pivot stats
    d = np.abs(np.diag(M)).max()
    off = M - np.diag(np.diag(M))
    maxent = np.abs(off).max()
    # hub theorem stats
    best = 0.0
    cand = np.argsort(-(np.abs(mu[0])*V[:, 0]**2 + np.abs(mu[1])*V[:, 1]**2))[:5]
    for hh in cand:
        m = M[:, hh]; Nh = np.outer(m, m) - M[hh, hh]*M
        Nh[hh, :] = 0; Nh[:, hh] = 0
        No = Nh - np.diag(np.diag(Nh))
        best = max(best, np.linalg.norm(No, 2))
    ev = [max(abs(mu[k])*(abs(mu[k])*V[:, k]**2 - d)) for k in (0, 1)]
    out = []
    for _ in range(parts):
        side = rng.random(n) < 0.5
        I = np.where(side)[0]; J = np.where(~side)[0]
        A = M[np.ix_(I, J)]
        s = np.linalg.svd(A, compute_uv=False)
        a1 = marg2_formula(A); a2 = marg2_formula(A.T)
        # bound: u1^2 + share(A_res) + |row A_res|^2/S
        U, sv, Vt = np.linalg.svd(A, full_matrices=False)
        Ares = A - sv[0]*np.outer(U[:, 0], Vt[0])
        T = (Ares**2).sum(); S = sv[0]**2
        rows = (Ares**2).sum(1)
        bnd = U[:, 0]**2 + rows/T + rows/S
        out.append((s[0], s[1], a1.max(), a2.max(), (a1 - bnd).max(), np.abs(Ares).max()/np.sqrt(T)))
    out = np.array(out)
    return dict(mu=mu[:4], diag=d, maxent=maxent, hubN=best, eigtest=ev,
                s1=out[:, 0].min(), s2min=out[:, 1].min(), s2med=np.median(out[:, 1]),
                maxmarg_best_orient=np.minimum(out[:, 2], out[:, 3]).max(),
                bound_violation=out[:, 4].max(), entry_over_frob=out[:, 5].max())

for (n, K, mu2, hub, noise) in [(500, 30, -1.2, 0.0, 0.0), (500, 30, 1.2, 0.0, 0.3), (500, 100, -1.2, 0.0, 0.3),
                                  (500, 30, -1.2, 0.9, 0.2), (500, 100, 1.2, 0.9, 0.0), (500, 150, -1.3, 0.8, 0.5)]:
    r = analyse(build(n, K, mu2, hub, noise, rng), rng)
    print(f"n={n} K={K} mu2={mu2} hub={hub} noise={noise}:", flush=True)
    print("   ", {k: (np.round(v, 4) if not isinstance(v, list) else [round(x, 4) for x in v]) for k, v in r.items()}, flush=True)
