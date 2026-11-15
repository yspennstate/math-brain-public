"""T_L / F_L = (1-chi^L)^3 / (2 eps chi^L S_L): for which depths is it >= 1 (the parallel eigenvalue is the top one)?
Exact rational arithmetic for small L, floats on a grid for large L."""
from fractions import Fraction as Fr
import numpy as np

def ratio_exact(L, chi):
    eps = 1 - chi
    S = sum((1 - chi**j)**2 for j in range(1, L + 1))
    return (1 - chi**L)**3 / (2 * eps * chi**L * S)

print("limit eps->0: 3L^2/((L+1)(2L+1)) =", [round(3*L*L/((L+1)*(2*L+1)), 4) for L in range(1, 8)])
grid = [Fr(k, 1000) for k in range(1, 1000)]          # chi = 0.001 .. 0.999
for L in range(1, 13):
    vals = [ratio_exact(L, c) for c in grid]
    m = min(vals); cm = grid[vals.index(m)]
    print("L=%2d  min over chi grid of T/F = %.6f at chi=%s  %s" % (L, float(m), float(cm), "T>=F" if m >= 1 else "T<F somewhere"))
# large L, floats; x_j = (1-chi^j)/eps
worst = (9e9, None)
for eps in np.concatenate([np.logspace(-6, -1, 61), np.linspace(0.1, 0.99, 90)]):
    chi = 1 - eps
    Lmax = int(min(max(60 / eps, 50), 4e6))
    j = np.arange(1, Lmax + 1, dtype=np.float64)
    x = -np.expm1(j * np.log1p(-eps)) / eps
    cs = np.cumsum(x * x)
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        r = x**3 / (2 * np.exp(j * np.log1p(-eps)) * cs)
    r = r[3:]                                             # L >= 4
    r = r[np.isfinite(r)]
    k = int(np.argmin(r))
    if r[k] < worst[0]:
        worst = (float(r[k]), (float(eps), k + 4))
print("L>=4, 151 eps values in [1e-6, 0.99], L up to 60/eps: min T/F = %.6f at (eps, L) = %s" % worst)
