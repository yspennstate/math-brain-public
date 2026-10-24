"""H+/Delta for two-weight thresholds 1[a*N0 + b*N1 >= theta] with group sizes up to 24 and
bias optimization over (q0,q1) (mpmath, adaptive precision). Evidence for the sharp-constant conjecture."""
import mpmath as mp, math, sys, time, itertools
from scipy.optimize import minimize
import numpy as np
from levels import spectrum_2groups
TLIM = float(sys.argv[1]) if len(sys.argv) > 1 else 300
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 4)
def ratio(a, b, m0, m1, th, x):
    q0 = 1 / (1 + math.exp(-x[0])); q1 = 1 / (1 + math.exp(-x[1]))
    mn = min(q0, 1 - q0, q1, 1 - q1)
    mp.mp.dps = 30 + int(2 * (m0 + m1) * max(1.0, -math.log10(mn)))
    r = spectrum_2groups(lambda u, v: int(a * u + b * v >= th), m0, mp.mpf(q0), m1, mp.mpf(q1))
    if not (r['Delta'] > 1e-30): return 0.0
    return r['ratio_HD']
t0 = time.time(); best = (0, None); cnt = 0
print('majority uniform:', [ (m, round(spectrum_2groups(lambda u, v: int(u >= (m + 1) // 2), m, mp.mpf(0.5), 0, mp.mpf(0.5))['ratio_HD'], 4)) for m in (3, 9, 21, 41)], flush=True)
while time.time() - t0 < TLIM:
    a, b = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4)][rng.integers(5)]
    m0 = int(rng.integers(1, 13)); m1 = int(rng.integers(1, 13))
    sums = sorted(set(a * u + b * v for u in range(m0 + 1) for v in range(m1 + 1)))
    th = sums[int(rng.integers(1, len(sums)))]
    x0 = rng.normal(0, 2.5, 2)
    try:
        res = minimize(lambda x: -ratio(a, b, m0, m1, th, np.clip(x, -9, 9)), x0, method='Nelder-Mead', options=dict(maxiter=60, xatol=0.05, fatol=1e-3))
    except Exception as e:
        continue
    cnt += 1
    v = -res.fun
    if v > best[0]:
        best = (v, (a, b, m0, m1, th, (1 / (1 + np.exp(-np.clip(res.x, -9, 9)))).round(5).tolist()))
        print(round(time.time() - t0), 'new best', round(v, 4), best[1], flush=True)
print('optimizations', cnt, 'best', best)
