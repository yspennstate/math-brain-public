"""Stars K_{1,k} plus isolated vertices, weights 1/k: is the maximum of s(G, x) over all unit sum-zero x the slack?

star_states_n.py searched all x by Nelder-Mead from 40 starts in n dimensions; a value below the slack there is
only a lower bound.  Here x is restricted to the span of four orthonormal vectors,

    u1  top eigenvector (k on the centre, -1 on the leaves),
    v_j first j leaves against the other k - j,
    z0  the star's vertices against the isolated ones,
    w_i first i isolated vertices against the other m - i   (only when m >= 2),

the low-dimensional search is repeated from many starts for every (j, i), and the best point is polished in
the full space.  Values are again lower bounds of the maximum; equality with the slack is exact.

usage: star_struct_check.py NMIN NMAX SEED T104_FOLDER
"""
import sys
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, sys.argv[4])
from star_states_n import setup, lap, s_of  # noqa: E402


def unit(v):
    return v / np.linalg.norm(v)


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
            lam = (k + 1.0) / k
            need = (n - 1) * lam - 2.0
            slack = (n - 2) * np.linalg.eigvalsh(M)[-1] - need
            u1 = np.zeros(n); u1[0] = k; u1[1:k + 1] = -1; u1 = unit(u1)
            z0 = np.zeros(n); z0[:k + 1] = m; z0[k + 1:] = -(k + 1); z0 = unit(z0)
            best, bestx, bestlab = -1e9, None, ""
            for j in range(1, k // 2 + 1):
                v = np.zeros(n); v[1:j + 1] = 1.0 / j; v[j + 1:k + 1] = -1.0 / (k - j); v = unit(v)
                for i in ([0] if m == 1 else range(1, m // 2 + 1)):
                    basis = [u1, v, z0]
                    if i > 0:
                        ww = np.zeros(n); ww[k + 1:k + 1 + i] = 1.0 / i; ww[k + 1 + i:] = -1.0 / (m - i); basis.append(unit(ww))
                    E = np.array(basis).T
                    assert np.allclose(E.T @ E, np.eye(E.shape[1]), atol=1e-12)

                    def f(c):
                        nc = np.linalg.norm(c)
                        if nc < 1e-12:
                            return 1e3
                        return -s_of(n, B, L, M, E @ (c / nc), need)

                    for st in range(60):
                        r = minimize(f, rng.normal(0, 1, E.shape[1]), method="Nelder-Mead",
                                     options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 3000})
                        if -r.fun > best:
                            best, bestx, bestlab = -r.fun, E @ (r.x / np.linalg.norm(r.x)), "j=%d i=%d" % (j, i)

            def fall(z):
                x = Pi @ z
                nx = np.linalg.norm(x)
                if nx < 1e-12:
                    return 1e3
                return -s_of(n, B, L, M, x / nx, need)

            r = minimize(fall, bestx, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 8000})
            pol = max(best, -r.fun)
            print("  K_{1,%d} + %d isolated: slack %+.6f  structured max %+.6f (%s)  after polish in all x %+.6f  x = %s"
                  % (k, m, slack, best, bestlab, pol, np.array2string(bestx, precision=3, suppress_small=True)), flush=True)


if __name__ == "__main__":
    main()
