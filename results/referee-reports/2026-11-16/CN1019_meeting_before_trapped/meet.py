"""CN1019 = Conjecture 1.5 of Addario-Berry, Oliveira, Peres, Sousi, Random walks colliding before getting trapped,
EJP 21 (2016) (Conjecture 1.6 in the journal numbering): for every finite irreducible reversible chain, X, Y at rate 1
and Z frozen, all started independently from pi, P(M <= min(H_X, H_Y)) >= 1/3. A uniform c > 0 would already be new.

A reversible chain on n states = stationary law pi and symmetric conductances c_xy >= 0, rates q(x,y) = c_xy / pi_x.
For a frozen z, h(x,y) = P(X, Y meet before either hits z | X0=x, Y0=y) is harmonic for the pair generator
L(x) + L(y) off the boundary, with h = 1 on {x = y} (ties count as meeting, as M <= min H) and h = 0 on
{x = z or y = z, x != y}. The target is F = sum_{x,y,z} pi_x pi_y pi_z h_z(x,y). Minimise F over (pi, c).

    python meet.py N1 N2 STARTS
"""
import sys

import numpy as np
from scipy.optimize import minimize


def F(pi, C):
    n = len(pi)
    Q = C / pi[:, None]
    np.fill_diagonal(Q, 0)
    out = Q.sum(1)
    tot = 0.0
    idx = {(x, y): i for i, (x, y) in enumerate((x, y) for x in range(n) for y in range(n))}
    N = n * n
    for z in range(n):
        A = np.zeros((N, N))
        b = np.zeros(N)
        for x in range(n):
            for y in range(n):
                i = idx[x, y]
                if x == y:
                    A[i, i] = 1
                    b[i] = 1
                elif x == z or y == z:
                    A[i, i] = 1
                else:
                    A[i, i] = -(out[x] + out[y])
                    for w in range(n):
                        if w != x:
                            A[i, idx[w, y]] += Q[x, w]
                        if w != y:
                            A[i, idx[x, w]] += Q[y, w]
        try:
            h = np.linalg.solve(A, b).reshape(n, n)
            if h.min() < -1e-9 or h.max() > 1 + 1e-9 or not np.isfinite(h).all():
                return 1.0
        except np.linalg.LinAlgError:
            return 1.0
        tot += pi[z] * pi @ h @ pi
    return tot


def unpack(v, n):
    a = np.clip(v[:n], -5, 5)
    pi = np.exp(a - a.max())
    pi /= pi.sum()
    C = np.zeros((n, n))
    iu = np.triu_indices(n, 1)
    C[iu] = np.exp(np.clip(v[n:], -14, 14))
    C = C + C.T
    return pi, C


if __name__ == "__main__":
    n1, n2, S = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(11)
    # sanity: two states, any chain; complete graph uniform
    for n in range(n1, n2 + 1):
        m = n + n * (n - 1) // 2
        u = F(np.ones(n) / n, np.ones((n, n)) - np.eye(n))
        best = (np.inf, None)
        for s in range(S):
            v0 = rng.normal(0, rng.choice([0.5, 2, 5]), m)
            r = minimize(lambda v: F(*unpack(v, n)), v0, method="Powell", options={"xtol": 1e-8, "ftol": 1e-12, "maxfev": 20000})
            if r.fun < best[0]:
                best = (r.fun, r.x)
        pi, C = unpack(best[1], n)
        print("n=%d complete-uniform F=%.6f | min F=%.6f  pi=%s" % (n, u, best[0], np.round(pi, 4)), flush=True)
        np.save("best_n%d.npy" % n, best[1])
