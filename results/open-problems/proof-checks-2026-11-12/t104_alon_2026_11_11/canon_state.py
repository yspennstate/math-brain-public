"""A canonical matching state for the pair tau = [2, 1^(n-2)], sigma = [2, 2, 1^(n-4)].

psi in V_tau is a unit x in R^n with sum 0, and 1 - <psi, (i j) psi> = 2 - (x_i - x_j)^2.
V_sigma = sign (x) {symmetric T, zero diagonal, zero row sums}; pair energy there is |T|^2 + <T, P_ij T P_ij>.
Candidate: rho(x) = normalised average over unit y orthogonal to 1 and x of the projection P of
(x y^t + y x^t)/sqrt(2) onto that space.  With c = (n-2)/(n-1) the dual form asks, for every pair ij,
    2 - (x_i - x_j)^2  >=  c * tr(rho(x) (I - sigma(ij))).
This script evaluates slack_ij(x) = (2 - d^2) * N - c * A_ij (N = sum of |PT|^2, A_ij = sum of pair energies over
an orthonormal basis of y) by direct matrices, compares with the closed form, and searches for a negative slack.
usage: canon_state.py n samples seed
"""
import sys
import numpy as np
from scipy.optimize import minimize


def direct(x):
    n = len(x)
    one = np.ones(n) / np.sqrt(n)
    Pi = np.eye(n) - np.outer(one, one)
    B = np.linalg.svd(np.vstack([one, x]))[2][2:]          # orthonormal basis of {1, x}^perp
    N = 0.0
    A = np.zeros((n, n))
    for y in B:
        T = (np.outer(x, y) + np.outer(y, x)) / np.sqrt(2.0)
        PT = T - (n / (n - 2.0)) * Pi @ np.diag(np.diag(T)) @ Pi
        assert abs(np.diag(PT)).max() < 1e-10 and abs(PT.sum(axis=0)).max() < 1e-10
        nn = (PT * PT).sum()
        N += nn
        for i in range(n):
            for j in range(i + 1, n):
                p = np.arange(n)
                p[i], p[j] = j, i
                A[i, j] += nn + (PT * PT[np.ix_(p, p)]).sum()
    return N, A


def closed(x):
    n = len(x)
    m4 = (x ** 4).sum()
    N = (n - 2.0) - (2.0 / (n - 2.0)) * (n - 1.0 - n * m4)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d2 = (x[i] - x[j]) ** 2
            s = x[i] ** 2 + x[j] ** 2
            q = x[i] ** 2 - x[j] ** 2
            A[i, j] = (2 - d2) * (n - 3 + 2 * d2) - (n / (n - 2.0)) * (4 * (1 - 1.0 / n - m4) - 2 * (s - d2 / n - q * q))
    return N, A


def min_slack(x, fn=closed):
    n = len(x)
    c = (n - 2.0) / (n - 1.0)
    N, A = fn(x)
    best = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            best = min(best, (2 - (x[i] - x[j]) ** 2) * N - c * A[i, j])
    return best


def unit(z):
    z = z - z.mean()
    return z / np.linalg.norm(z)


def main():
    n, samples, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    dev = 0.0
    for _ in range(40):
        x = unit(rng.normal(0, 1, n))
        N1, A1 = direct(x)
        N2, A2 = closed(x)
        dev = max(dev, abs(N1 - N2), abs(A1 - A2).max())
    star = unit(np.array([n - 1.0] + [-1.0] * (n - 1)))
    edge = unit(np.array([1.0, -1.0] + [0.0] * (n - 2)))
    print("n=%d closed form against direct matrices: largest deviation %.1e" % (n, dev))
    print("  slack at the star vector %.3e, at the edge vector %.3e" % (min_slack(star), min_slack(edge)))
    worst = float("inf")
    arg = None
    for k in range(samples):
        kind = k % 5
        if kind == 0:
            x = rng.normal(0, 1, n)
        elif kind == 1:
            x = star + 0.2 * rng.normal(0, 1, n)
        elif kind == 2:
            x = edge + 0.2 * rng.normal(0, 1, n)
        elif kind == 3:
            x = rng.normal(0, 1, n) * (rng.uniform(0, 1, n) < 0.5)
        else:
            x = rng.choice([-1.0, 0.0, 1.0, 2.0], n) + 0.05 * rng.normal(0, 1, n)
        if np.linalg.norm(x - x.mean()) < 1e-9:
            continue
        x = unit(x)
        v = min_slack(x)
        if v < worst:
            worst, arg = v, x
    print("  random search: smallest slack %.6e over %d vectors" % (worst, samples))
    for r in range(12):
        x0 = arg + 0.3 * rng.normal(0, 1, n) if r else arg
        res = minimize(lambda z: min_slack(unit(z)), x0, method="Nelder-Mead",
                       options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 6000})
        if res.fun < worst:
            worst, arg = res.fun, unit(res.x)
    print("  after local search: smallest slack %.6e at x = %s" % (worst, " ".join("%.5f" % v for v in np.sort(arg))))


if __name__ == "__main__":
    main()
