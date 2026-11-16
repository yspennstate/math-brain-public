"""CN1019 refined bound at a FIXED interior pi: minimise D = F - 1/3 - (2/3) sum pi^3 over the conductances only.
(The free-pi search in dtest.py slides to point masses, where D = 0 trivially.)

    python dfixed.py N1 N2 PIS STARTS
"""
import sys

import numpy as np
from scipy.optimize import minimize

from meet import F


def cond(v, n):
    C = np.zeros((n, n))
    iu = np.triu_indices(n, 1)
    C[iu] = np.exp(np.clip(v, -14, 14))
    return C + C.T


if __name__ == "__main__":
    n1, n2, P, S = (int(a) for a in sys.argv[1:5])
    rng = np.random.default_rng(23)
    for n in range(n1, n2 + 1):
        worst = (np.inf, None)
        for k in range(P):
            pi = rng.dirichlet(np.full(n, rng.choice([0.5, 1.0, 3.0])))
            pi = np.maximum(pi, 0.02)
            pi /= pi.sum()
            target = 1 / 3 + 2 / 3 * (pi ** 3).sum()
            best = np.inf
            for s in range(S):
                v0 = rng.normal(0, rng.choice([0.5, 2, 5]), n * (n - 1) // 2)
                r = minimize(lambda v: F(pi, cond(v, n)) - target, v0, method="Powell",
                             options={"xtol": 1e-8, "ftol": 1e-12, "maxfev": 20000})
                best = min(best, r.fun)
            print("n=%d pi=%s min D=%.3e" % (n, np.round(pi, 3), best), flush=True)
            if best < worst[0]:
                worst = (best, pi)
        print("n=%d WORST min D=%.3e at pi=%s" % (n, worst[0], np.round(worst[1], 3)), flush=True)
