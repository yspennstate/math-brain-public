# Theorem 2 check: for a graph whose Laplacian Fiedler value is simple, adding the edge e={u,v}
# with weight w changes lambda_2 by g with
#      w c^2 Delta / (Delta + 2w + w c^2)  <=  g  <=  min(w c^2, Delta),
# c = phi(u)-phi(v) (unit Fiedler vector), Delta = lambda_3 - lambda_2.
# Also the hypercube corollary of Theorem 1: Q_d has lambda_2 = 2 of multiplicity d, so adding
# any d-1 edges cannot raise lambda_2 nor the SRW gap; d edges can.
import numpy as np, itertools
rng = np.random.default_rng(1)
def random_regular(n, d):
    # pairing model with rejection of loops/multi-edges
    while True:
        pts = rng.permutation(n*d); A = np.zeros((n, n)); ok = True
        for k in range(0, n*d, 2):
            a, b = pts[k]//d, pts[k+1]//d
            if a == b or A[a, b]: ok = False; break
            A[a, b] = A[b, a] = 1
        if ok: return A
def lap(A): return np.diag(A.sum(1)) - A
worst_lo = worst_hi = 0; count = 0
for trial in range(6):
    n, d = [(30, 3), (40, 4), (60, 3), (50, 5), (24, 3), (80, 3)][trial]
    A = random_regular(n, d); L = lap(A); lam, V = np.linalg.eigh(L)
    Delta = lam[2] - lam[1]
    if Delta < 1e-6: continue
    phi = V[:, 1]
    for w in [0.05, 0.3, 1.0, 3.0]:
        for u in range(n):
            for v in range(u+1, n):
                if A[u, v]: continue
                e = np.zeros(n); e[u] = 1; e[v] = -1
                g = np.linalg.eigvalsh(L + w*np.outer(e, e))[1] - lam[1]
                c2 = (phi[u]-phi[v])**2
                hi = min(w*c2, Delta); lo = w*c2*Delta/(Delta + 2*w + w*c2)
                worst_hi = max(worst_hi, g - hi); worst_lo = max(worst_lo, lo - g); count += 1
    print(f"random {d}-regular n={n}: Delta={Delta:.4f}; checked so far {count} (edge,weight) pairs; max violation upper {worst_hi:.2e} lower {worst_lo:.2e}")
# path graphs (Delta ~ 3 pi^2/n^2, the interlacing cap binds)
for n in [10, 30, 100]:
    A = np.zeros((n, n))
    for x in range(n-1): A[x, x+1] = A[x+1, x] = 1
    L = lap(A); lam, V = np.linalg.eigh(L); Delta = lam[2]-lam[1]; phi = V[:, 1]
    for u in range(n):
        for v in range(u+2, n):
            e = np.zeros(n); e[u] = 1; e[v] = -1
            g = np.linalg.eigvalsh(L + np.outer(e, e))[1] - lam[1]
            c2 = (phi[u]-phi[v])**2
            worst_hi = max(worst_hi, g - min(c2, Delta)); worst_lo = max(worst_lo, c2*Delta/(Delta+2+c2) - g); count += 1
    print(f"path n={n}: Delta={Delta:.5f}, first-order term at the ends c^2={ (phi[0]-phi[-1])**2:.4f} (>> Delta): cap binds")
print("TOTAL checked", count, "max violation of upper bound", worst_hi, "of lower bound", worst_lo)
# hypercube corollary
d = 4; n = 2**d
A = np.zeros((n, n))
for x in range(n):
    for b in range(d): A[x, x ^ (1 << b)] = 1
L = lap(A); lam = np.linalg.eigvalsh(L); print("Q_4 Laplacian spectrum start:", np.round(lam[:6], 6))
def srw_gap(A):
    dd = A.sum(1); S = A/np.sqrt(np.outer(dd, dd)); mu = np.sort(np.linalg.eigvalsh(S))[::-1]; return 1-mu[1]
base = srw_gap(A); nonedges = [(u, v) for u in range(n) for v in range(u+1, n) if not A[u, v]]
for r in [d-1, d]:
    maxgap = 0; maxl2 = 0
    for _ in range(3000):
        idx = rng.choice(len(nonedges), r, replace=False); B = A.copy()
        for i in idx: u, v = nonedges[i]; B[u, v] = B[v, u] = 1
        maxgap = max(maxgap, srw_gap(B)); maxl2 = max(maxl2, np.linalg.eigvalsh(lap(B))[1])
    print(f"Q_4 plus {r} random edges (3000 samples): max SRW gap {maxgap:.6f} vs base {base:.6f}; max lambda_2(L) {maxl2:.6f} vs 2")
