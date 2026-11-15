"""Odd circulants, small n: for a fixed top frequency k, F(a) = sum g P - sum g Q is a quadratic form in the weights
(after homogenising with sum a = 1). Minimise it over the polytope {a >= 0, sum a = 1, theta_k >= theta_j for all j}
by enumerating every active set of inequality constraints and solving the KKT system on that face (lstsq; a solution
is kept only if it is feasible and the stationarity residual is small). The minimum of F over the polytope is the
smallest value found. F = 0 at the uniform weights (K_n, all theta equal), so the claim on circulants is min F >= 0.
usage: python t104_circ_qp.py n_max [n_min]
"""
import sys, itertools
import numpy as np

NMAX = int(sys.argv[1])


def build(n, k):
    m = (n - 1) // 2
    S = np.arange(1, m + 1)
    C = np.cos(2 * np.pi * np.outer(np.arange(n), S) / n)

    def F(a):
        s = a.sum(); a = a / s
        th = (2.0 / n) * ((1 - C) @ a); lam = th[k]
        gQ = 16 * np.sum((a / n) * (1 - C[k]) * (lam - 2.0 / n - a / n))
        gP = 0.0
        for j in range(1, m + 1):
            if j != k:
                Pj = (4 * th[j] + 8 * lam / (n - 2) - 16 * (1 - np.sum(a * C[k] * C[j])) / (n * (n - 2))
                      + 4 * (1 - lam) * (n - 4) / (n - 2) ** 2)
                gP += (lam - th[j]) * Pj
        return (gP - gQ) * s * s
    E = np.eye(m)
    M = np.zeros((m, m))
    for i in range(m):
        M[i, i] = F(E[i])
    for i in range(m):
        for j in range(i + 1, m):
            M[i, j] = M[j, i] = (F(E[i] + E[j]) - M[i, i] - M[j, j]) / 2
    # inequality rows G a >= 0: a_i >= 0, theta_k - theta_j >= 0
    rows = [E[i] for i in range(m)]
    for j in range(1, m + 1):
        if j != k:
            rows.append((2.0 / n) * ((1 - C[k]) - (1 - C[j])))
    G = np.array(rows)
    # check the quadratic reproduces F
    rng = np.random.default_rng(0); z = rng.random(m)
    assert abs(z @ M @ z - F(z)) < 1e-10 * max(1, abs(F(z)))
    return M, G, F


def qp_min(M, G):
    global far
    m = M.shape[0]; best = (np.inf, None); r = G.shape[0]
    for size in range(0, m):
        for A in itertools.combinations(range(r), size):
            GA = G[list(A)]
            K = np.zeros((m + size + 1, m + size + 1))
            K[:m, :m] = 2 * M; K[:m, m:m + size] = -GA.T; K[:m, -1] = -1
            K[m:m + size, :m] = GA; K[-1, :m] = 1
            rhs = np.zeros(m + size + 1); rhs[-1] = 1
            sol, *_ = np.linalg.lstsq(K, rhs, rcond=None)
            if np.abs(K @ sol - rhs).max() > 1e-9:
                continue
            a = sol[:m]
            if (G @ a).min() < -1e-11:
                continue
            v = a @ M @ a
            if v < best[0]:
                best = (v, a)
            if np.abs(a - 1.0 / m).sum() > 0.05 and v < far[0]:
                far[0] = v
    return best


NMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 5
for n in range(NMIN, NMAX + 1, 2):
    m = (n - 1) // 2
    for k in range(1, m + 1):
        M, G, F = build(n, k)
        far = [np.inf]
        v, a = qp_min(M, G)
        u = np.ones(m) / m
        print("n %2d k %d  min F over the polytope %+.3e  at a = %s  (F at uniform %+.1e)  smallest KKT value off uniform (L1 > 0.05) %+.3e"
              % (n, k, v, np.array2string(a, precision=3, suppress_small=True) if a is not None else None, F(u), far[0]),
              flush=True)
