"""n = 5, D = 3 remainder: minimise the bracket F(v) = 7 + 16g + (70-200g) m4 + 120 g m3^2 over unit zero-sum v in R^5 with
nonnegative weights w_ij = (2+g)/20 + g v_i v_j, for g in (35/76, 2/3] (g <= 2/3 because lambda - g >= 0).
Also the same without the weight constraint, to see whether the constraint is needed.
usage: python t104_n5d3_window.py starts seed"""
import sys
import numpy as np
from scipy.optimize import minimize
ST, SEED = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(SEED)
iu = np.triu_indices(5, 1)


def F(v, g):
    return 7 + 16 * g + (70 - 200 * g) * (v ** 4).sum() + 120 * g * (v ** 3).sum() ** 2


for g in np.linspace(35 / 76, 2 / 3, 9):
    best = {True: (np.inf, None), False: (np.inf, None)}
    for wc in (True, False):
        cons = [{"type": "eq", "fun": lambda v: v.sum()}, {"type": "eq", "fun": lambda v: (v ** 2).sum() - 1}]
        if wc:
            cons.append({"type": "ineq", "fun": lambda v, g=g: (2 + g) / 20 + g * np.outer(v, v)[iu]})
        for s in range(ST):
            v0 = rng.standard_normal(5); v0 -= v0.mean(); v0 /= np.linalg.norm(v0)
            r = minimize(F, v0, args=(g,), constraints=cons, method="SLSQP", options=dict(maxiter=500, ftol=1e-13))
            v = r.x
            if abs(v.sum()) > 1e-7 or abs((v ** 2).sum() - 1) > 1e-7:
                continue
            if wc and ((2 + g) / 20 + g * np.outer(v, v)[iu]).min() < -1e-9:
                continue
            if r.fun < best[wc][0]:
                best[wc] = (r.fun, np.sort(v))
    print("g %.4f  min F with weights>=0: %.5f at %s   without: %.5f at %s" % (
        g, best[True][0], (None if best[True][1] is None else np.round(best[True][1], 4)), best[False][0], (None if best[False][1] is None else np.round(best[False][1], 4))))
