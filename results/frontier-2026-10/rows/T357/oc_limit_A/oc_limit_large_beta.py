# T357 (agent A, 20 Oct 2026 11:1x): the beta -> inf limit of oc_limit.py's ratio.
# Hand derivation (u = x/beta, phi0 = phi(0)): C ~ beta/phi0, b ~ 3 beta^2/(2 pi^2 phi0) (int x s2 = -1, int x^2 s1 = pi^2/3),
# r_FM ~ -3 beta^3/(2 pi^2), r_OC ~ -beta^3/(8 ln 2) (int_0^inf s2 = -1/4, int_0^inf x s1 = ln 2), so
# A alpha lam_FM ~ 3 beta^2/(pi^2 phi0), A alpha lam_OC ~ beta^2/phi0 (3/(2 pi^2) + 1/(8 ln 2)), ratio -> 1/2 + pi^2/(24 ln 2).
# Numerics: oc_limit.py's formula with the integrals split at 0 and on the scale 1/beta.
import numpy as np
from scipy.integrate import quad
s1 = lambda x: 0.25 / np.cosh(x / 2) ** 2
s2 = lambda x: s1(x) * np.tanh(-x / 2)
phi = lambda u: np.exp(-u * u / 2) / np.sqrt(2 * np.pi)
def E(f, beta):
    pts = [0.0] + [k / beta for k in (1, 3, 10, 30)]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        tot += quad(lambda u: phi(u) * (f(u) + f(-u)), lo, hi, epsabs=1e-17, epsrel=1e-13, limit=500)[0]
    tot += quad(lambda u: phi(u) * (f(u) + f(-u)), pts[-1], 40, epsabs=1e-17, epsrel=1e-13, limit=500)[0]
    return tot
lim = 0.5 + np.pi ** 2 / (24 * np.log(2))
print("closed-form limit 1/2 + pi^2/(24 ln 2) = %.6f" % lim)
for beta in (5, 10, 20, 50, 100, 200, 400):
    ip, ia = E(lambda z: s1(beta * z), beta), E(lambda z: s1(beta * z) * z * z, beta)
    b = -E(lambda z: z * s2(beta * z), beta) / (2 * ia * ip); C = 1 / ip
    rF = beta ** 2 / 2 * E(lambda u: u * s2(beta * u), beta) / E(lambda u: u * u * s1(beta * u), beta)
    rO = beta ** 2 / 2 * E(lambda u: np.sign(u) * s2(beta * u), beta) / E(lambda u: abs(u) * s1(beta * u), beta)
    lF, lO = b - C * (rF - beta) / beta ** 2, b - C * (rO - beta) / beta ** 2
    print("beta %4g: ratio %.6f  limit - ratio %.2e  beta*(limit - ratio) %.4f" % (beta, lO / lF, lim - lO / lF, beta * (lim - lO / lF)))
