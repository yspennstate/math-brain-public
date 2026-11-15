"""Stars K_{1,k} plus m isolated vertices, weights 1/k: second structured search for the maximum of s(G, x).

x runs over the span of

    u1  top eigenvector (k on the centre, -1 on the leaves),
    z0  the star's vertices against the isolated ones,
    e_{leaf 1} - e_{leaf 2}                (k >= 2),
    e_{leaf 1} - e_{isolated 1},
    e_{isolated 1} - e_{isolated 2}        (m >= 2),

orthonormalised; Nelder-Mead from 150 starts in at most five dimensions, then a polish in the full space.
Values below the slack are lower bounds of the maximum; equality with the slack is exact.

usage: star_struct_check2.py NMIN NMAX SEED T104_FOLDER
"""
import sys
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, sys.argv[4])
from star_states_n import setup, lap, s_of  # noqa: E402


def main():
    nmin, nmax, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    for n in range(nmin, nmax + 1):
        pairs, B, SW = setup(n)
        Pi = np.eye(n) - 1.0 / n
        print("n = %d" % n, flush=True)
        for k in range(2, n - 1):
            m = n - 1 - k
            w = np.array([1.0 / k if (i == 0 and j <= k) else 0.0 for (i, j) in pairs])
            L = lap(n, pairs, w)
            M = np.tensordot(w, SW, axes=1)
            need = (n - 1) * (k + 1.0) / k - 2.0
            slack = (n - 2) * np.linalg.eigvalsh(M)[-1] - need
            vecs = []
            v = np.zeros(n); v[0] = k; v[1:k + 1] = -1; vecs.append(v)
            v = np.zeros(n); v[:k + 1] = m; v[k + 1:] = -(k + 1); vecs.append(v)
            v = np.zeros(n); v[1] = 1; v[2] = -1; vecs.append(v)
            v = np.zeros(n); v[1] = 1; v[k + 1] = -1; vecs.append(v)
            if m >= 2:
                v = np.zeros(n); v[k + 1] = 1; v[k + 2] = -1; vecs.append(v)
            E, _ = np.linalg.qr(np.array(vecs).T)
            assert np.allclose(E.sum(axis=0), 0, atol=1e-12)

            def f(c):
                nc = np.linalg.norm(c)
                if nc < 1e-12:
                    return 1e3
                return -s_of(n, B, L, M, E @ (c / nc), need)

            best, bestx = -1e9, None
            for st in range(150):
                r = minimize(f, rng.normal(0, 1, E.shape[1]), method="Nelder-Mead",
                             options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 4000})
                if -r.fun > best:
                    best, bestx = -r.fun, E @ (r.x / np.linalg.norm(r.x))

            def fall(z):
                x = Pi @ z
                nx = np.linalg.norm(x)
                if nx < 1e-12:
                    return 1e3
                return -s_of(n, B, L, M, x / nx, need)

            r = minimize(fall, bestx, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 8000})
            pol = max(best, -r.fun)
            print("  K_{1,%d} + %d isolated: slack %+.6f  structured max %+.6f  after polish in all x %+.6f  x = %s"
                  % (k, m, slack, best, pol, np.array2string(bestx, precision=3, suppress_small=True)), flush=True)


if __name__ == "__main__":
    main()
