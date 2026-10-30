"""T357: per seed, the lambda where the population over-confidence OC changes sign (lam_cal) and the lambda minimizing the
population excess logistic risk (lam_risk), on a 49-point log grid 1e-4..30 with warm starts, refined by interpolation
(log-linear root for OC, parabola in log lambda for risk). Same model and formulas as calib_path.py.
Also reports at lam_risk the calibration error CE and the first-moment calibration E[(p - E[y|p]) zhat], which the
scale-stationarity of the risk forces to vanish for the risk-optimal SCALE of a fixed direction.
argv: d alpha beta seeds
"""
import sys, math
import numpy as np
sys.argv = sys.argv[:1] + sys.argv[1:4] + [sys.argv[4], "1"]
exec(open("calib_path.py", encoding="utf-8").read().split('print(f"d={d}')[0])

def pop_more(q, c):
    s = q * gh_x
    mu = (c / q ** 2) * s[:, None]; sdv = math.sqrt(max(1 - c ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu + sdv * gh_x[None, :])) * gh_w[None, :]).sum(1)
    return ((sig(s) - ey) * s * gh_w).sum()

grid = np.exp(np.linspace(math.log(30), math.log(1e-4), 49))
out = []
for sd in range(seeds):
    rng = np.random.default_rng(sd)
    X = rng.standard_normal((n, d)); wstar = np.zeros(d); wstar[0] = 1.0
    s = np.where(rng.random(n) < sig(beta * X[:, 0]), 1.0, -1.0)
    w = np.zeros(d); res = []
    for lam in grid:
        w = fit(X, s, lam, w); q = float(np.linalg.norm(w)); c = float(w @ wstar)
        ce, oc, risk = pop(q, c); res.append((lam, q, c, ce, oc, risk - bayes, pop_more(q, c)))
    res = np.array(res)
    oc = res[:, 4]; idx = np.where(np.sign(oc[:-1]) != np.sign(oc[1:]))[0]
    if len(idx):
        i = idx[0]; l0, l1 = math.log(res[i, 0]), math.log(res[i + 1, 0])
        lcal = math.exp(l0 + (l1 - l0) * oc[i] / (oc[i] - oc[i + 1]))
        ex_cal = res[i, 5] + (res[i + 1, 5] - res[i, 5]) * oc[i] / (oc[i] - oc[i + 1])
    else:
        lcal, ex_cal = float("nan"), float("nan")
    j = int(np.argmin(res[:, 5])); j = min(max(j, 1), len(grid) - 2)
    xs = np.log(res[j - 1:j + 2, 0]); ys = res[j - 1:j + 2, 5]
    A = np.polyfit(xs, ys, 2); lrisk = math.exp(-A[1] / (2 * A[0])) if A[0] > 0 else res[j, 0]
    out.append((lcal, lrisk, ex_cal, res[j, 5], res[j, 3], res[j, 6], res[0, 4] if False else res[-1, 4]))
o = np.array(out)
med = np.nanmedian(o, axis=0)
print(f"alpha={alpha} beta={beta} d={d} seeds={seeds}: lam_cal={med[0]:.4g} lam_risk={med[1]:.4g} ratio={med[0]/med[1]:.3f} "
      f"excess at lam_cal={med[2]:.5f} min excess={med[3]:.5f} CE at lam_risk={med[4]:.4f} first-moment at lam_risk={med[5]:+.5f} "
      f"OC at lam=1e-4: {med[6]:+.4f}  (per-seed ratios {', '.join(f'{a/b:.3f}' for a, b in o[:, :2])})", flush=True)
