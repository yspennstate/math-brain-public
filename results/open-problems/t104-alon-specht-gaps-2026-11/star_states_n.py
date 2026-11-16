"""Conjecture F and the states D_x at the stars K_{1,k} plus isolated vertices, n = 5..8 (W = 1).

For a weighted graph G on n vertices, lam = lambda_max(L_G):

    slack(G) = (n-2) lambda_max(G, [n-2,2]) - (n-1) lam + 2W  >=  s(G, x) = (n-2) tr(D_x L(G, [n-2,2])) - (n-1) lam + 2W

for every unit sum-zero x, D_x as in state_mix_n5.py.  minmax_n5.out found that at n = 5 the smallest values of
F(G) = max over the top two-plane of s(G, x) away from zero sit at K_{1,2} and K_{1,3} with isolated vertices
(0.02 and 0.0145).  This script evaluates, at K_{1,k} with n-1-k isolated vertices and equal weights 1/k:

    slack,  s at the top eigenvector,  the maximum of s over x = cos t u1 + sin t v with v a unit vector of the
    second eigenspace (all of it),  the maximum of s over all unit sum-zero x.

usage: star_states_n.py NMIN NMAX SEED
"""
import sys
import numpy as np
from scipy.optimize import minimize


def setup(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            r = np.zeros((n, n)); r[i, j] = 1; r[j, i] = -1; rows.append(r.ravel())
        r = np.zeros((n, n)); r[i, i] = 1; rows.append(r.ravel())
        r = np.zeros((n, n)); r[i, :] = 1; rows.append(r.ravel())
    u, s, vt = np.linalg.svd(np.array(rows))
    B = vt[int((s > 1e-10).sum()):].T
    assert B.shape[1] == n * (n - 3) // 2
    d = B.shape[1]
    SW = []
    for (i, j) in pairs:
        P = np.eye(n); P[[i, j]] = P[[j, i]]
        SW.append(np.eye(d) - B.T @ np.kron(P, P) @ B)
    return pairs, B, np.array(SW)


def lap(n, pairs, w):
    L = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        L[i, i] += v; L[j, j] += v; L[i, j] -= v; L[j, i] -= v
    return L


def s_of(n, B, L, M, x, need):
    Pi = np.eye(n) - 1.0 / n
    Q = Pi - np.outer(x, x)
    A = Q @ (float(x @ L @ x) * Pi - L) @ Q
    g, Y = np.linalg.eigh((A + A.T) / 2)
    num = den = 0.0
    for k in range(n):
        if g[k] > 1e-13:
            y = Y[:, k]
            a = B.T @ ((np.outer(x, y) + np.outer(y, x)) / np.sqrt(2.0)).ravel()
            num += g[k] * float(a @ M @ a); den += g[k] * float(a @ a)
    if den < 1e-15:
        return -need
    return (n - 2) * num / den - need


def main():
    nmin, nmax, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    for n in range(nmin, nmax + 1):
        pairs, B, SW = setup(n)
        Pi = np.eye(n) - 1.0 / n
        print("n = %d" % n, flush=True)
        for k in range(1, n):
            w = np.array([1.0 / k if (i == 0 and j <= k) else 0.0 for (i, j) in pairs])
            L = lap(n, pairs, w)
            M = np.tensordot(w, SW, axes=1)
            # the constant vector is moved to eigenvalue -1, so columns 1..n-1 of U span the sum-zero space
            ev, U = np.linalg.eigh(L - np.ones((n, n)) / n)
            assert abs(ev[0] + 1.0) < 1e-9
            lam = ev[-1]
            need = (n - 1) * lam - 2.0
            slack = (n - 2) * np.linalg.eigvalsh(M)[-1] - need
            u1 = U[:, -1]
            top = s_of(n, B, L, M, u1, need)
            # second eigenspace: every sum-zero eigenvector with eigenvalue within 1e-9 of the second largest
            E2 = U[:, [c for c in range(1, n - 1) if abs(ev[c] - ev[-2]) < 1e-9]]
            m2 = E2.shape[1]

            def fplane(p):
                t, c = p[0], p[1:]
                v = E2 @ c
                nv = np.linalg.norm(v)
                if nv < 1e-12:
                    return 1e3
                x = np.cos(t) * u1 + np.sin(t) * v / nv
                return -s_of(n, B, L, M, x, need)

            bestp = top
            for st in range(12 * m2):
                p0 = np.concatenate([[rng.uniform(0, np.pi)], rng.normal(0, 1, m2)])
                r = minimize(fplane, p0, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 4000})
                bestp = max(bestp, -r.fun)

            def fall(z):
                x = Pi @ z
                nx = np.linalg.norm(x)
                if nx < 1e-12:
                    return 1e3
                return -s_of(n, B, L, M, x / nx, need)

            besta, xa = bestp, None
            for st in range(40):
                z0 = rng.normal(0, 1, n) if st >= 4 else U[:, -1 - (st % 2)] + 0.2 * rng.normal(0, 1, n)
                r = minimize(fall, z0, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 6000})
                r = minimize(fall, r.x, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 6000})
                if -r.fun > besta:
                    besta = -r.fun; xa = Pi @ r.x; xa = xa / np.linalg.norm(xa)
            ov = "" if xa is None else "  best x overlaps: top %.3f, second space %.3f" % (abs(xa @ u1), np.linalg.norm(E2.T @ xa))
            print("  K_{1,%d} + %d isolated: lam %.4f  slack %+.6f  s(top) %+.6f  max over top+second space (dim %d) %+.6f  max over all x %+.6f%s"
                  % (k, n - 1 - k, lam, slack, top, m2, bestp, besta, ov), flush=True)


if __name__ == "__main__":
    main()
