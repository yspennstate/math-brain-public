"""Cross-checks for cylnd.py: f_1 and f_2 against the independent cyl2d.py formulas; node doubling; Monte Carlo for
one middle-k case."""
import numpy as np
import cylnd
from cyl2d import interval, ball

for rho in [0.1, 0.5, 0.9]:
    for a in [0.2, 0.5, 0.8, 0.95]:
        print(f'rho={rho} a={a} f1-interval={cylnd.f(1, a, rho) - interval(a, rho):+.1e} f2-ball={cylnd.f(2, a, rho) - ball(a, rho):+.1e}')
small = [(0.05, 0.7, 5, 6), (0.1, 0.7, 5, 6), (0.95, 0.6, 5, 6), (0.05, 0.3, 5, 6)]
f600 = {k: cylnd.f(k, a, rho) for rho, a, k1, k2 in small for k in (1, k1, k2)
        for _ in [0]} if False else None
for rho, a, km, kn in small:
    v600 = {k: cylnd.f(k, a, rho) for k in (1, km, kn)}
    cylnd.GL = np.polynomial.legendre.leggauss(1500)
    v1500 = {k: cylnd.f(k, a, rho) for k in (1, km, kn)}
    cylnd.GL = np.polynomial.legendre.leggauss(600)
    print(f'rho={rho} a={a} node-doubling change: ' + ' '.join(f'k={k}:{v1500[k] - v600[k]:+.1e}' for k in v600),
          f'margin k={km} over k in (1,{kn}): {v1500[km] - max(v1500[1], v1500[kn]):+.2e}')
# Monte Carlo: rho = 0.7, a = 0.7, k = 3 vs k = 1 and k = 6, 4e7 samples in batches, common random numbers
from scipy.stats import chi2
rng = np.random.default_rng(1)
rho, a = 0.7, 0.7
acc = {1: 0, 3: 0, 6: 0}; n = 0
for _ in range(40):
    X = rng.standard_normal((1_000_000, 6)); Z = rng.standard_normal((1_000_000, 6))
    Y = rho * X + np.sqrt(1 - rho * rho) * Z
    cx = np.cumsum(X * X, 1); cy = np.cumsum(Y * Y, 1)
    for k in acc:
        r2 = chi2.ppf(a, k)
        acc[k] += int(((cx[:, k - 1] <= r2) & (cy[:, k - 1] <= r2)).sum())
    n += 1_000_000
mc = {k: v / n for k, v in acc.items()}
print('MC rho=0.7 a=0.7:', {k: round(v, 6) for k, v in mc.items()}, 'quadrature:', {k: round(cylnd.f(k, a, rho), 6) for k in acc},
      f'MC margin k=3 over best of (1,6): {mc[3] - max(mc[1], mc[6]):+.2e} (MC s.e. of a difference ~ {np.sqrt(2 * 0.5 * 0.5 / n):.0e})')
