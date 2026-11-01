# (C3) in angle form: with q = sin^2(g), p = sin^2(psi), D(p||q) <= sin^2(psi - g) (2 + ln(1/sin^2(2g))). Both sides vanish at
# psi = g; comparing derivatives reduces it to, with a = tan g, x = tan(psi)/tan(g), kappa(a) = 1 + ln((1 + a^2)/(2a)):
#   (i)  x ln x      <= kappa (x - 1)(1 + a^2 x)/(1 + a^2)   for x >= 1,
#   (ii) -x ln x     <= kappa (1 - x)(1 + a^2 x)/(1 + a^2)   for 0 < x < 1.
# Check (i), (ii) on a grid, and (C3) itself directly in (p, q).
import numpy as np
a = np.exp(np.linspace(np.log(1e-4), np.log(1e4), 801))[:, None]
kap = 1 + np.log((1 + a * a) / (2 * a))
x1 = np.exp(np.linspace(0, np.log(1e9), 4001))[None, :]
g1 = kap * (x1 - 1) * (1 + a * a * x1) / (1 + a * a) - x1 * np.log(x1)
x2 = np.exp(np.linspace(np.log(1e-12), 0, 4001))[None, :]
g2 = kap * (1 - x2) * (1 + a * a * x2) / (1 + a * a) + x2 * np.log(x2)
print('(i)  min of RHS - LHS over the grid: %.3e' % g1.min())
print('(ii) min of RHS - LHS over the grid: %.3e' % g2.min())
i = np.unravel_index(np.argmin(g1), g1.shape); print('     (i) worst at a=%.4g x=%.4g' % (a[i[0], 0], x1[0, i[1]]))
i = np.unravel_index(np.argmin(g2), g2.shape); print('     (ii) worst at a=%.4g x=%.4g' % (a[i[0], 0], x2[0, i[1]]))
# direct check of (C3) in (p, q)
p = np.linspace(0, 1, 4001)[None, :]
q = np.concatenate([np.logspace(-8, np.log10(0.5), 400), 1 - np.logspace(-8, np.log10(0.5), 400)])[:, None]
def xlogy(x, y): return np.where(x > 0, x * np.log(np.where(x > 0, x, 1) / y), 0.0)
D = xlogy(p, q) + xlogy(1 - p, 1 - q)
BC = np.sqrt(p * q) + np.sqrt((1 - p) * (1 - q))
K = 2 + np.log(1 / (4 * q * (1 - q)))
print('(C3) max of D - (1 - BC^2) K: %.3e' % (D - (1 - BC ** 2) * K).max())
