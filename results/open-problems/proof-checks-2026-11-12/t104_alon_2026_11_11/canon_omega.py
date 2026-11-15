"""Explicit covariances for Reduction R (HOOKS_AND_TWO_ROWS.md section 5).

C = Q diag(omega(x_k)) Q / trace, Q the projection onto {1, x}^perp, omega a fixed weight function that is large
where |x_k| is small.  For each omega in a small family, the smallest value of (*) over pairs and over many unit
x (random, structured, then a local search).  A family member with smallest value >= 0 would be an explicit
matching state for Conjecture F.
usage: canon_omega.py n samples seed
"""
import sys
import numpy as np
from scipy.optimize import minimize


def star_min(x, om):
    n = len(x)
    Q = np.eye(n) - 1.0 / n - np.outer(x, x)
    C = Q @ np.diag(om) @ Q
    tr = np.trace(C)
    if tr < 1e-14:
        return 0.0
    C = C / tr
    dg = np.diag(C)
    kappa = float((x * x * dg).sum())
    d2 = (x[:, None] - x[None, :]) ** 2
    cij = dg[:, None] + dg[None, :] - 2 * C
    gij = (x * x * dg)[:, None] + (x * x * dg)[None, :] - 2 * np.outer(x, x) * C
    S = (2 - d2) + (2 * n * kappa / (n - 2.0)) * ((n - 1) * d2 - 2) - 2 * n * gij - (n - 2) * (2 * d2 - 1) * cij
    iu = np.triu_indices(n, 1)
    return float(S[iu].min())


def unit(z):
    z = z - z.mean()
    return z / np.linalg.norm(z)


FAMILIES = {
    "uniform": lambda x, b: np.ones_like(x),
    "exp(-b n x^2)": lambda x, b: np.exp(-b * len(x) * x * x),
    "1/(1+b n x^2)^2": lambda x, b: 1.0 / (1.0 + b * len(x) * x * x) ** 2,
    "exp(-b n (x-med)^2)": lambda x, b: np.exp(-b * len(x) * (x - np.median(x)) ** 2),
}


def main():
    n, samples, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    star = unit(np.array([n - 1.0] + [-1.0] * (n - 1)))
    edge = unit(np.array([1.0, -1.0] + [0.0] * (n - 2)))
    xs = []
    for k in range(samples):
        kind = k % 5
        if kind == 0:
            x = rng.normal(0, 1, n)
        elif kind == 1:
            t = rng.uniform(0, 1)
            x = t * star + (1 - t) * edge + 0.03 * rng.normal(0, 1, n)
        elif kind == 2:
            x = star * rng.choice([-1, 1]) + 0.3 * rng.normal(0, 1, n)
        elif kind == 3:
            x = rng.normal(0, 1, n) * (rng.uniform(0, 1, n) < 0.6)
        else:
            x = rng.choice([-1.0, 0.0, 1.0, 3.0], n) + 0.05 * rng.normal(0, 1, n)
        if np.linalg.norm(x - x.mean()) > 1e-6:
            xs.append(unit(x))
    for name, fam in FAMILIES.items():
        best = (-float("inf"), None)
        for b in ([0.0] if name == "uniform" else [0.25, 0.5, 1, 2, 4, 8, 16, 64]):
            vals = np.array([star_min(x, fam(x, b)) for x in xs])
            k = int(vals.argmin())
            worst, arg = float(vals[k]), xs[k]
            res = minimize(lambda z: star_min(unit(z), fam(unit(z), b)), arg, method="Nelder-Mead",
                           options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 3000})
            if res.fun < worst:
                worst, arg = float(res.fun), unit(res.x)
            if worst > best[0]:
                best = (worst, (b, arg))
        b, arg = best[1]
        print("n=%d %-22s best b=%-5g smallest (*) %.5f at x = %s"
              % (n, name, b, best[0], " ".join("%.3f" % v for v in np.sort(arg))))


if __name__ == "__main__":
    main()
