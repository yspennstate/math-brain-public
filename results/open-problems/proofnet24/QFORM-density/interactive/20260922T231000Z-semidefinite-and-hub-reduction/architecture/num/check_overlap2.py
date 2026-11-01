try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, itertools
rng = np.random.default_rng(7)
def esym(y, k):
    e = np.zeros(k+1); e[0] = 1.0
    for v in y:
        for j in range(k, 0, -1):
            e[j] += e[j-1]*v
    return e[k]
def Wbrute(E, L, k):
    n = E.shape[0]; W = 0.0
    for S in itertools.combinations(L, k):
        rest = [j for j in range(n) if j not in S]
        for T in itertools.combinations(rest, k):
            W += np.linalg.det(E[np.ix_(S, T)])**2
    return W
n = 12
for name in ["spread rank3", "spread rank3 + noise", "Wigner", "hub+rank1 (hub row heavy)", "hub+rank2"]:
    for rep in range(3):
        if name.startswith("spread rank3"):
            U, _ = np.linalg.qr(rng.standard_normal((n, 3)))
            E = U @ np.diag([2.0, -1.5, 1.2]) @ U.T
            if "noise" in name: E += 0.15*rng.standard_normal((n,n))
        elif name == "Wigner":
            E = rng.standard_normal((n, n))/np.sqrt(n)
        elif name.startswith("hub+rank1"):
            w = rng.standard_normal(n); w[0] = 0; w /= np.linalg.norm(w)
            v = rng.standard_normal(n); v[0] = 0; v -= (v@w)*w; v /= np.linalg.norm(v)
            e0 = np.eye(n)[0]
            E = np.outer(e0, w) + np.outer(w, e0) + 1.3*np.outer(v, v) + 0.05*rng.standard_normal((n,n))
        else:
            w = rng.standard_normal(n); w[0] = 0; w /= np.linalg.norm(w)
            V, _ = np.linalg.qr(rng.standard_normal((n, 2))); e0 = np.eye(n)[0]
            E = np.outer(e0, w) + np.outer(w, e0) + V @ np.diag([1.3, -1.1]) @ V.T
        E = (E+E.T)/2; np.fill_diagonal(E, 0.0)
        rows = np.sqrt((E**2).sum(1))
        for k in (2, 3):
            for Lname, L in [("all", list(range(n))), ("light", [i for i in range(n) if rows[i] <= np.median(rows)*1.5])]:
                if len(L) < k: continue
                W = Wbrute(E, L, k)
                nu2 = np.linalg.svd(E[L, :], compute_uv=False)**2
                ek, ek1 = esym(nu2, k), esym(nu2, k-1)
                rho2 = max(rows[i]**2 for i in L)
                rhs = ek - 2*(k-1)*rho2*ek1
                print(f"{name:28s} k={k} L={Lname:5s} |L|={len(L):2d} W/e_k={W/ek:.3f} rhs/e_k={rhs/ek:+.3f} ok={W >= rhs - 1e-9}", flush=True)
