"""CN1019 refined bound. For hierarchical (ultrametric, binary) chains, merging two blocks of weights a, b lowers F by
2ab(a+b) = (2/3)((a+b)^3 - a^3 - b^3), so F telescopes to 1/3 + (2/3) sum pi^3, whatever the tree.
(1) check that formula on explicit multi-scale chains with nonuniform pi;
(2) minimise D = F - 1/3 - (2/3) sum pi^3 over all reversible chains on n states. D < 0 would refute the refined bound.

    python dtest.py N1 N2 STARTS
"""
import sys

import numpy as np
from scipy.optimize import minimize

from meet import F, unpack


def tree_chain(pi, merges, eps):
    """merges: list of (setA, setB) from finest to coarsest; level k gets conductance eps**k between A and B."""
    n = len(pi)
    C = np.zeros((n, n))
    for k, (A, B) in enumerate(merges):
        for a in A:
            for b in B:
                C[a, b] = C[b, a] = eps ** k
    return C


def D(v, n):
    pi, C = unpack(v, n)
    return F(pi, C) - 1 / 3 - 2 / 3 * (pi ** 3).sum()


if __name__ == "__main__":
    rng = np.random.default_rng(5)
    print("formula check on multi-scale chains")
    cases = [
        (np.array([0.5, 0.3, 0.2]), [({0}, {1}), ({0, 1}, {2})]),
        (np.array([0.1, 0.2, 0.3, 0.4]), [({0}, {1}), ({0, 1}, {2}), ({0, 1, 2}, {3})]),
        (np.array([0.4, 0.1, 0.25, 0.25]), [({0}, {1}), ({2}, {3}), ({0, 1}, {2, 3})]),
        (np.array([0.3, 0.05, 0.15, 0.2, 0.3]), [({3}, {4}), ({0}, {1}), ({0, 1}, {2}), ({0, 1, 2}, {3, 4})]),
    ]
    for pi, merges in cases:
        for eps in (1e-2, 1e-3, 1e-4):
            f = F(pi, tree_chain(pi, merges, eps))
            print("  pi=%s eps=%g F=%.6f formula=%.6f" % (pi, eps, f, 1 / 3 + 2 / 3 * (pi ** 3).sum()), flush=True)
    n1, n2, S = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    for n in range(n1, n2 + 1):
        m = n + n * (n - 1) // 2
        best = (np.inf, None)
        for s in range(S):
            v0 = rng.normal(0, rng.choice([0.5, 2, 5]), m)
            r = minimize(D, v0, args=(n,), method="Powell", options={"xtol": 1e-8, "ftol": 1e-12, "maxfev": 20000})
            if r.fun < best[0]:
                best = (r.fun, r.x)
        pi, C = unpack(best[1], n)
        print("n=%d min D=%.3e pi=%s" % (n, best[0], np.round(pi, 4)), flush=True)
        np.save("dbest_n%d.npy" % n, best[1])
