# x0 = -D: locate the step where E X_K = 0 (closed form via phi) and minimise the exact error around it.
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from rr_exact_core import err, phi

for (n, n1, K) in [(40, 1, 1000), (40, 1, 10000), (100, 10, 1000), (100, 10, 10000),
                   (100, 50, 1000), (100, 50, 10000), (1000, 100, 1000), (1000, 100, 10000)]:
    mu = n1 / n; T = n * K; Lam = math.log(mu * T); unit = Lam ** 2 / (8 * mu * T ** 2)

    def EX(g):
        A = (1 - g) ** n1; AK = A ** K
        return -AK + (1 - AK) * g / 2 * phi(1 - g, n1)

    gs = np.geomspace(1e-3 * Lam / (mu * T), 1, 4000); v = [EX(g) for g in gs]
    roots = [brentq(EX, gs[i], gs[i + 1], xtol=1e-16) for i in range(len(gs) - 1) if v[i] * v[i + 1] < 0]
    best = (np.inf, None)
    for g0 in roots:
        f = lambda lg: err(n, n1, K, math.exp(lg), x0=-1.0)[0]
        r = minimize_scalar(f, bounds=(math.log(g0) - 0.05, math.log(g0) + 0.05), method="bounded",
                            options={"xatol": 1e-13})
        best = min(best, (r.fun, math.exp(r.x)))
    at_root = err(n, n1, K, roots[0], x0=-1.0)[0] / unit if roots else float("nan")
    print("(%d,%d,%d) roots %s  min/unit %.4e at g*mu*T/Lam %.4f  (error at root %.4e)"
          % (n, n1, K, ["%.6g" % (g * mu * T / Lam) for g in roots], best[0] / unit,
             best[1] * mu * T / Lam if best[1] else float("nan"), at_root), flush=True)
