# Numeric checks of the C_4 statements in "Conserved charges in linearly reinforced graph urns".
import numpy as np
from scipy.integrate import quad
from scipy.stats import logistic

f = lambda s: (s / np.tanh(s / 2) - 2) / (4 * np.sinh(s / 2) ** 2) if abs(s) > 1e-6 else 1 / 6
# compare with the convolution of two standard logistic densities
conv = lambda s: quad(lambda x: logistic.pdf(x) * logistic.pdf(s - x), -60, 60, limit=200)[0]
for s in [0.0, 0.5, 1.0, 3.0, 8.0]:
    print("s=%.1f  f=%.10f  logistic*logistic=%.10f" % (s, f(s), conv(s)))
m0 = 2 * quad(f, 0, 80, limit=200)[0]
m2 = 2 * quad(lambda s: s * s * f(s), 0, 80, limit=200)[0]
print("mass %.12f  E M^2 %.10f  (L pi^2/6 at L=4: %.10f)" % (m0, m2, 4 * np.pi ** 2 / 6))
# p = (1 + tanh(M/4)) / 2 = 1/(1 + exp(-M/2))
sig = lambda s: 1 / (1 + np.exp(-s / 2))
Ep = 2 * quad(lambda s: sig(s) * f(s), 0, 80, limit=200)[0] / 2 + 2 * quad(lambda s: sig(-s) * f(s), 0, 80, limit=200)[0] / 2
Ep2 = quad(lambda s: sig(s) ** 2 * f(s), -80, 80, limit=400, points=[0])[0]
print("E p %.10f  Var p %.10f  (paper pi^2/32 - 1/4 = %.10f)" % (Ep, Ep2 - Ep ** 2, np.pi ** 2 / 32 - 0.25))
# density of p near 1 against 4 (1-p) log(1/(1-p))
for q in [1e-3, 1e-5, 1e-7]:
    p = 1 - q
    dens = 2 * f(2 * np.log(p / q)) / (p * q)
    print("1-p=%.0e  density %.6e  4(1-p)log(1/(1-p)) %.6e  ratio %.4f" % (q, dens, 4 * q * np.log(1 / q), dens / (4 * q * np.log(1 / q))))
