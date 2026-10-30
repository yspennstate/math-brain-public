# T357 (agent A, 20 Oct 2026 06:0x): alpha -> inf limit of lam_OC/lam_risk for logistic ridge, P(y=1|z) = sig(beta z).
# Leading order in 1/alpha: what_hat = kappa w* + w_perp, |w_perp|^2 = C/alpha, C = 1/i_perp, i_perp = E sig'(beta z),
# kappa - beta = b/alpha - A lam, b = -E[z sig''(beta z)]/(2 i_par i_perp) (Cox-Snell, trace term), i_par = E[sig'(beta z) z^2].
# With q = |w_hat|, rho = kappa/q: delta = q - beta rho = (kappa - beta) + |w_perp|^2/beta, eps = 1 - rho^2 = |w_perp|^2/beta^2.
# Calibration residual m(u) = sig(q u) - E[y | zhat = q u] = delta u sig'(beta u) - (beta^2 eps/2) sig''(beta u) + ...
# FM = 0 <=> delta/eps = r_FM = (beta^2/2) E[u sig''(beta u)]/E[u^2 sig'(beta u)];  OC = 0 <=> r_OC with u -> sign(u), u^2 -> |u|.
# Root in lam: A alpha lam_r = b - C (r - beta)/beta^2. lam_risk = lam_FM at this order (numerics: ratio -> 1 like 1/alpha).
import numpy as np
from scipy.integrate import quad
s1 = lambda x: 0.25 / np.cosh(x / 2) ** 2                       # sig'
s2 = lambda x: s1(x) * np.tanh(-x / 2)                           # sig'' = sig'(1 - 2 sig)
phi = lambda u: np.exp(-u * u / 2) / np.sqrt(2 * np.pi)
E = lambda f: quad(lambda u: phi(u) * f(u), -40, 40, epsabs=1e-15, epsrel=1e-13, limit=500)[0]
meas = {1: 1.006889, 2: 1.028618, 3: 1.047687, 5: 1.069658}
for beta in (0.5, 1, 2, 3, 5, 10, 20):
    ip, ia = E(lambda z: s1(beta * z)), E(lambda z: s1(beta * z) * z * z)
    b = -E(lambda z: z * s2(beta * z)) / (2 * ia * ip); C = 1 / ip
    rF = beta ** 2 / 2 * E(lambda u: u * s2(beta * u)) / E(lambda u: u * u * s1(beta * u))
    rO = beta ** 2 / 2 * E(lambda u: np.sign(u) * s2(beta * u)) / E(lambda u: abs(u) * s1(beta * u))
    lF, lO = b - C * (rF - beta) / beta ** 2, b - C * (rO - beta) / beta ** 2
    print("beta %4g: b %.5f C %.5f r_FM %+.5f r_OC %+.5f  A*alpha*lam_FM %.5f lam_OC %.5f  ratio %.6f  measured %s"
          % (beta, b, C, rF, rO, lF, lO, lO / lF, meas.get(beta, "-")))
