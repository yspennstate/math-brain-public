try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from itertools import combinations, permutations
rng = np.random.default_rng(7)

def esym(x, k):
    e = np.zeros(k+1); e[0] = 1.0
    for t in x:
        e[1:] = e[1:] + t*e[:-1]
    return e[k]

# (a) skeleton identity: E_w sum_{l in L\K, m notin K u {l}} (A-P)_lm^2 = 9 V3L / V2L, w_ST ~ det(A_ST)^2, S in L
n = 8
A = rng.standard_normal((n, n)); A = (A + A.T)/2
Lset = [0, 1, 2, 3, 4, 5]          # light rows; 6, 7 play the role of hubs (allowed only in T)
def pairs(k):
    out = []
    for S in combinations(Lset, k):
        rest = [j for j in range(n) if j not in S]
        for T in combinations(rest, k):
            out.append((S, T))
    return out
V2 = 0.0; V3 = 0.0; acc = 0.0
for S, T in pairs(2):
    d = np.linalg.det(A[np.ix_(S, T)])**2
    V2 += d
    K = set(S) | set(T)
    P = A[:, list(T)] @ np.linalg.inv(A[np.ix_(S, T)]) @ A[list(S), :]
    err = 0.0
    for l in Lset:
        if l in K: continue
        for m in range(n):
            if m in K or m == l: continue
            err += (A[l, m] - P[l, m])**2
    acc += d*err
for S, T in pairs(3):
    V3 += np.linalg.det(A[np.ix_(S, T)])**2
print("skeleton identity: E_w err =", acc/V2, "  9 V3L/V2L =", 9*V3/V2, flush=True)

# (b) e_3 <= e_2 T_3 and e_3 >= T_3 T_2 T_1 / 6 >= T_3^3/6
worst_up = 0; worst_lo = np.inf
for t in range(2000):
    s = np.sort(np.abs(rng.standard_normal(rng.integers(3, 12)))*rng.uniform(0.01, 10, size=1))[::-1]
    if rng.random() < 0.5:
        s[rng.integers(0, len(s)):] *= 1e-3
    x = s**2
    T = lambda k: np.sum(x[k-1:])
    e3, e2 = esym(x, 3), esym(x, 2)
    worst_up = max(worst_up, e3/(e2*T(3)))
    worst_lo = min(worst_lo, e3/(T(3)*T(2)*T(1)/6))
print("max e3/(e2 T3) =", worst_up, "(<= 1)   min e3/(T3 T2 T1/6) =", worst_lo, "(>= 1)", flush=True)

# (c) canonical family: hub + rank one + eps W. H = {hub}. Random partitions of L with the hub in J.
def canonical(n, eps, lam=1.0):
    w = rng.standard_normal(n-1); w /= np.linalg.norm(w)
    v = rng.standard_normal(n-1); v -= (v @ w)*w; v /= np.linalg.norm(v)
    W = rng.standard_normal((n-1, n-1)); W = (W + W.T)/2; np.fill_diagonal(W, 0); W /= np.linalg.norm(W, 2)
    A = np.zeros((n, n))
    A[0, 1:] = w; A[1:, 0] = w
    A[1:, 1:] = lam*np.outer(v, v) + eps*W
    np.fill_diagonal(A, 0.0)        # no pivot: zero diagonal
    return A
for n in [60, 200]:
    for eps in [0.0, 0.3/np.sqrt(n), 1/np.sqrt(n), 3/np.sqrt(n)]:
        A = canonical(n, eps)
        rows = np.linalg.norm(A, axis=1)
        ev = np.linalg.eigvalsh(A)
        T3s = []; ratio = []; amax = []
        for t in range(60):
            xi = rng.integers(0, 2, size=n); xi[0] = 0     # hub always in J
            I = np.where(xi == 1)[0]; J = np.where(xi == 0)[0]
            B = A[np.ix_(I, J)]
            s = np.linalg.svd(B, compute_uv=False); x = s**2
            T3s.append(np.sum(x[2:])); ratio.append(esym(x, 3)/esym(x, 2))
            # marginals
            Uu, ss, _ = np.linalg.svd(B, full_matrices=False); xx = ss**2; e3 = esym(xx, 3)
            p = np.array([xx[m]*esym(np.delete(xx, m), 2)/e3 for m in range(len(xx))])
            amax.append(np.max((Uu**2) @ p))
        print(f"n={n:4d} eps*sqrt(n)={eps*np.sqrt(n):.2f} |ev|>=1: {np.sum(np.abs(ev)>=1)}  hub row={rows[0]:.2f} "
              f"max light row={rows[1:].max():.3f}  T3 median={np.median(T3s):.4f}  e3/e2 median={np.median(ratio):.4f} "
              f" max marginal median={np.median(amax):.3f}", flush=True)
