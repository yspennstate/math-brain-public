"""Leading-order FM = 0 root, three ways, at |w_perp|^2 = s = 1/(alpha i_perp):
(a) direct: solve E[(sig(kz + g) - sig(beta z)) (kz + g)] = 0 for k by Gauss-Hermite in (z, g), g ~ N(0, s);
(b) hand expansion: kappa - beta = -(1/alpha)(T3/(2 i_par i_perp) + 1/(beta i_par));
(c) DOSSIER 05:5x: kappa - beta = (1/(alpha i_perp))(T3/(2 i_par) - 1/beta)."""
import numpy as np
from scipy.optimize import brentq
from scipy.special import expit
x, w = np.polynomial.hermite_e.hermegauss(120); w = w/w.sum()
sp = lambda t: expit(t)*(1-expit(t)); spp = lambda t: sp(t)*(1-2*expit(t))
for beta in (1.0, 2.0, 5.0):
    ipar = (w*sp(beta*x)*x**2).sum(); iperp = (w*sp(beta*x)).sum(); T3 = (w*x*spp(beta*x)).sum()
    for alpha in (1e3, 1e4, 1e5):
        s = 1/(alpha*iperp)
        Z, G = np.meshgrid(x, x*np.sqrt(s), indexing='ij'); W = np.outer(w, w)
        f = lambda k: (W*(expit(k*Z+G)-expit(beta*Z))*(k*Z+G)).sum()
        k = brentq(f, beta-50/alpha, beta+50/alpha, xtol=1e-15)
        hand = -(T3/(2*ipar*iperp) + 1/(beta*ipar))
        dos = (T3/(2*ipar) - 1/beta)/iperp
        print(f"beta {beta} alpha {alpha:.0e}: alpha(k-beta) direct {alpha*(k-beta):+.5f}  hand {hand:+.5f}  dossier {dos:+.5f}")
