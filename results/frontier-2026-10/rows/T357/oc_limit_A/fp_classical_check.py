"""T357: the proportional fixed point reduces to the classical constants at leading order in 1/alpha.
With eps = 1/alpha, lam = ell*eps, the scaled unknowns mu = beta + eps*m, sig_^2 = eps*s, c = eps*g solve a system that is smooth in eps
(only even powers of sig_ survive the Z2 average) and at eps = 0 is triangular:
  g = 1/i_perp,  s = g^2 i_perp = 1/i_perp = C,  m = -(s/2) E[Z sig''(beta Z)]/i_par - ell*beta/i_par = b - A*ell,
with i_perp = E sig'(beta Z), i_par = E Z^2 sig'(beta Z), b = Cox-Snell bias, A = beta/i_par. This script solves the exact fixed point
(same equations as cgmt_ridge.py, own copy) at alpha 100..6400 and prints alpha*(mu-beta), alpha*sig_^2, alpha*c against m, C, g.
The gaps should fall like 1/alpha. argv: none."""
import math
import numpy as np
from scipy.optimize import root

gx, gw = np.polynomial.hermite_e.hermegauss(100); gw = gw / gw.sum()
Z1 = gx[:, None]; Z2 = gx[None, :]; W = gw[:, None] * gw[None, :]
sig = lambda t: 0.5 * (1 + np.tanh(0.5 * t))


def prox(Q, y, c):
    P = Q.copy()
    for _ in range(60):
        s = sig(P); f = P + c * (s - y) - Q; P = P - f / (1 + c * s * (1 - s))
    return P


def solve(alpha, beta, lam, v0):
    PY1 = sig(beta * Z1)
    def eqs(v):
        mu, ls, lc = v; sg = math.exp(ls); c = math.exp(lc)
        Q = mu * Z1 + sg * Z2; r = np.zeros(3)
        for y, wy in ((1.0, PY1), (0.0, 1 - PY1)):
            P = prox(Q, y, c); s = sig(P); d1 = s - y; d2 = s * (1 - s); ww = W * wy
            r[0] += (ww * Z1 * d1).sum(); r[1] += (ww / (1 + c * d2)).sum(); r[2] += (ww * d1 ** 2).sum()
        return [lam * mu + r[0], 1 / alpha - 1 + r[1] - lam * c, sg ** 2 - alpha * c ** 2 * r[2]]
    sol = root(eqs, v0, method="hybr", tol=1e-13)
    res = max(abs(x) for x in eqs(sol.x))
    return sol.x, res


for beta in (1.0, 2.0, 5.0):
    sp = sig(beta * gx) * (1 - sig(beta * gx)); s2 = sp * (1 - 2 * sig(beta * gx))      # sig', sig''
    ip = (gw * sp).sum(); ipar = (gw * gx ** 2 * sp).sum(); ezs2 = (gw * gx * s2).sum()
    C = 1 / ip; b = -C * ezs2 / (2 * ipar); A = beta / ipar
    for ell in (0.0, 1.0):
        m0 = b - A * ell
        print(f"beta {beta} ell {ell}: predicted alpha(mu-beta) {m0:+.6f}  alpha sig^2 {C:.6f}  alpha c {C:.6f}")
        v = None
        for alpha in (100, 400, 1600, 6400):
            eps = 1 / alpha
            v0 = v if v is not None else [beta + eps * m0, math.log(math.sqrt(eps * C)), math.log(eps * C)]
            if v is not None:                               # rescale the previous solution to the new alpha
                v0 = [beta + (v[0] - beta) / 4, v[1] - 0.5 * math.log(4), v[2] - math.log(4)]
            v, res = solve(alpha, beta, ell * eps, v0)
            mu, sg, c = v[0], math.exp(v[1]), math.exp(v[2])
            a1, a2, a3 = alpha * (mu - beta), alpha * sg ** 2, alpha * c
            print(f"  alpha {alpha:5d}: alpha(mu-beta) {a1:+.6f} (gap {a1-m0:+.2e})  alpha sig^2 {a2:.6f} (gap {a2-C:+.2e})"
                  f"  alpha c {a3:.6f} (gap {a3-C:+.2e})  resid {res:.1e}", flush=True)
