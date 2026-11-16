"""Local behaviour of the top-eigenvector state next to the uniform star K_{1,n-1}.

s_beta = (n-2) (N_t + N_x)/(D_t + D_x) - need, where t are the pairs (top, l) and x the pairs (k, l) with k below the
top, weighted by exp(beta (lam_k - lam)/lam). Where the top eigenvalue is simple, s_beta -> s_inf (top pairs only) as
beta -> infinity, so H = sup_beta s_beta >= s_inf there. Next to the star the top eigenvalue is simple with a gap of
order one, so H >= 0 next to the star follows from s_inf >= 0 next to the star. This script measures s_inf on
star + eps v, for random directions v: leaf weights of either sign (sum zero, so W stays 1) and leaf-leaf weights >= 0.

usage: python t104_star_local.py n ndirs seed
"""
import sys
import numpy as np

n = int(sys.argv[1]); NDIR = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]))
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
star_e = [p for p in pairs if p[0] == 0]
ll_e = [p for p in pairs if p[0] != 0]
ONES = np.ones((n, n)) / n
R2 = np.sqrt(2.0)


def lap(w):
    L = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        L[i, i] += v; L[j, j] += v; L[i, j] -= v; L[j, i] -= v
    return L


def basis32():
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            r = np.zeros((n, n)); r[i, j] = 1; r[j, i] = -1; rows.append(r.ravel())
        r = np.zeros((n, n)); r[i, i] = 1; rows.append(r.ravel())
        r = np.zeros((n, n)); r[i, :] = 1; rows.append(r.ravel())
    u, s, vt = np.linalg.svd(np.array(rows))
    B = vt[int((s > 1e-10).sum()):].T
    assert B.shape[1] == n * (n - 3) // 2
    return B


B = basis32(); d = B.shape[1]
SW = []
for (i, j) in pairs:
    P = np.eye(n); P[[i, j]] = P[[j, i]]
    SW.append(np.eye(d) - B.T @ np.kron(P, P) @ B)
SW = np.array(SW)


def parts(w):
    """Return s_inf and, for the check, s_beta at beta = 1e6 computed the minbeta way."""
    w = w / w.sum()
    ev, U = np.linalg.eigh(lap(w) - ONES)
    lam = ev[-1]
    M = np.tensordot(w, SW, axes=1)
    need = (n - 1) * lam - 2.0
    k = n - 1
    num = den = 0.0
    for l in range(1, k):
        g = ev[k] - ev[l]
        a = B.T @ ((np.outer(U[:, k], U[:, l]) + np.outer(U[:, l], U[:, k])) / R2).ravel()
        num += g * float(a @ M @ a); den += g * float(a @ a)
    return (n - 2) * num / den - need, ev[-1] - ev[-2]


star = np.zeros(len(pairs))
for p in star_e:
    star[pairs.index(p)] = 1.0 / (n - 1)
s0, gap0 = parts(star)
print("n %d: s_inf at the star %+.3e, top gap %.4f" % (n, s0, gap0), flush=True)

EPS = 10.0 ** np.arange(-2, -6.5, -0.5)
rows = []
for t in range(NDIR):
    kind = t % 3            # 0: leaf weights only; 1: leaf-leaf only; 2: both
    v = np.zeros(len(pairs))
    if kind in (0, 2):
        a = rng.normal(size=n - 1); a -= a.mean(); a /= np.linalg.norm(a)
        for p, x in zip(star_e, a):
            v[pairs.index(p)] = x
    if kind in (1, 2):
        b = rng.exponential(size=len(ll_e)) * (rng.random(len(ll_e)) < 0.6)
        if b.sum() == 0:
            b[0] = 1.0
        b /= b.sum()
        sc = 1.0 if kind == 1 else 10.0 ** rng.uniform(-3, 0)
        for p, x in zip(ll_e, b):
            v[pairs.index(p)] = sc * x
    vals = []
    for e in EPS:
        w = star + e * v
        if w.min() < 0:
            vals.append(np.nan); continue
        vals.append(parts(w)[0])
    vals = np.array(vals)
    rows.append((kind, vals))

names = {0: "leaf only", 1: "leaf-leaf only", 2: "both"}
for kind in (0, 1, 2):
    V = np.array([r[1] for r in rows if r[0] == kind])
    print("\n%s (%d directions): min over directions of s_inf, s_inf/eps, s_inf/eps^2 at each eps" % (names[kind], len(V)))
    for j, e in enumerate(EPS):
        c = V[:, j]; c = c[np.isfinite(c)]
        if len(c) == 0:
            continue
        print("  eps %.1e  min s %+.3e  s/eps [%+.4e, %+.4e]  s/eps^2 [%+.4e, %+.4e]  negatives %d" %
              (e, c.min(), (c / e).min(), (c / e).max(), (c / e ** 2).min(), (c / e ** 2).max(), int((c < -1e-13).sum())), flush=True)
