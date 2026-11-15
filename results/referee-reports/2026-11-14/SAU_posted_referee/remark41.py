# Remark 4.1 check: Xi_0 = union C_n, C_n = {n + j/(10n)}, G_2 joins points at distance < 2.
# Effective resistance from the point of C_1 to the outer shell C_N (shorted) should stay bounded (<= 1 by the flow).
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
for N in (10, 20, 40, 80, 120):
    pts = np.array([n + j/(10*n) for n in range(1, N+1) for j in range(n)])
    lab = np.array([n for n in range(1, N+1) for j in range(n)])
    M = len(pts)
    order = np.argsort(pts); pts = pts[order]; lab = lab[order]
    rows, cols = [], []
    for i in range(M):
        k = i + 1
        while k < M and pts[k] - pts[i] < 2:
            rows.append(i); cols.append(k); k += 1
    A = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(M, M)); A = (A + A.T).tocsr()
    deg = np.asarray(A.sum(1)).ravel(); L = (sp.diags(deg) - A).tocsr()
    src = int(np.where(lab == 1)[0][0]); sink = np.where(lab == N)[0]
    keep = np.setdiff1d(np.arange(M), sink)         # sink shorted to ground (potential 0)
    Lk = L[keep][:, keep]
    b = np.zeros(len(keep)); b[np.searchsorted(keep, src)] = 1.0
    v = sla.spsolve(Lk.tocsc(), b)
    R = v[np.searchsorted(keep, src)]
    Nr = (pts < N).sum()
    print(f"N={N:4d} points={M:6d} edges={len(rows):8d} R_eff(C_1 -> C_N)={R:.5f}  N(r)/r^2 at r=N: {Nr/N**2:.4f}")
