try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, itertools
rng = np.random.default_rng(11)
def esym(y, k):
    e = np.zeros(k+1); e[0] = 1.0
    for v in y:
        for j in range(k, 0, -1):
            e[j] += e[j-1]*v
    return e[k]
def Wbrute3(E, L):
    n = E.shape[0]; W = 0.0
    trip = np.array(list(itertools.combinations(range(n), 3)))
    for S in itertools.combinations(L, 3):
        ok = ~np.isin(trip, S).any(1)
        T = trip[ok]
        sub = E[np.array(S)][:, T]            # 3 x m x 3
        sub = np.transpose(sub, (1, 0, 2))    # m x 3 x 3
        W += (np.linalg.det(sub)**2).sum()
    return W
n = 22
for name in ["spread rank3", "spread rank4", "spread rank3 + hub column(J side)"]:
    U, _ = np.linalg.qr(rng.standard_normal((n, 4)))
    if name == "spread rank3":
        E = U[:, :3] @ np.diag([2.0, -1.5, 1.2]) @ U[:, :3].T
    elif name == "spread rank4":
        E = U @ np.diag([2.0, -1.5, 1.2, 1.0]) @ U.T
    else:
        E = U[:, :2] @ np.diag([1.4, -1.2]) @ U[:, :2].T
        w = rng.standard_normal(n); w[0] = 0; w /= np.linalg.norm(w); e0 = np.eye(n)[0]
        E = E + np.outer(e0, w) + np.outer(w, e0)
    E = (E + E.T)/2; np.fill_diagonal(E, 0.0)
    rows = np.sqrt((E**2).sum(1))
    L = [i for i in range(n) if rows[i] < 0.9]
    W = Wbrute3(E, L)
    nu2 = np.linalg.svd(E[L, :], compute_uv=False)**2
    e3, e2 = esym(nu2, 3), esym(nu2, 2)
    rho2 = max(rows[i]**2 for i in L)
    print(f"{name:34s} |L|={len(L)} rho_L={np.sqrt(rho2):.3f} W/e3={W/e3:.3f} (e3-4rho^2 e2)/e3={(e3-4*rho2*e2)/e3:+.3f} ok={W >= e3-4*rho2*e2}", flush=True)
