# Independent check of T392 1-D CFG numbers (agent C, 20 Oct). Different method from cfg1d*.py:
# DDIM by adaptive ODE (solve_ivp, rtol 1e-10) per start point + Gauss-Hermite expectation; leakage by bisection on the
# monotone start->end map; tilted law by direct quadrature.
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
from scipy.stats import norm

def flow(y0, w, A):  # dy/da = w + (1-w) tanh(a y), a from 0 to A
    s = solve_ivp(lambda a, y: [w + (1 - w) * np.tanh(a * y[0])], (0, A), [y0], rtol=1e-10, atol=1e-12)
    return s.y[0, -1]

def ddim_leak(w, m):
    f = lambda y0: flow(y0, w, m / 2)
    y0s = brentq(f, -(2 * w - 1) * m / 2 - 1, -m / 2 + 1e-9, xtol=1e-12)
    return norm.cdf(y0s), y0s

def zinf_moments(w, A=12.0, n=200):  # z(A) = y(A) - A, A large: the m-free limit law
    x, wt = np.polynomial.hermite_e.hermegauss(n)
    wt = wt / wt.sum()
    z = np.array([flow(v, w, A) - A for v in x])
    mu = (wt * z).sum()
    return mu, (wt * (z - mu) ** 2).sum()

def tilted(w, m):
    lq = lambda y: -(y * y + m * m / 4) / 2 + (1 - w) * np.logaddexp(m * y / 2, -m * y / 2) + w * m * y / 2 - (1 - w) * np.log(2)
    f = lambda y: np.exp(lq(y))
    Z = quad(f, -40, 40, points=[0, m / 2], limit=400)[0]
    leak = quad(f, -40, 0, limit=400)[0] / Z
    pos = quad(f, 0, 40, limit=400)[0]
    mean = quad(lambda y: y * f(y), 0, 40, limit=400)[0] / pos
    var = quad(lambda y: (y - mean) ** 2 * f(y), 0, 40, limit=400)[0] / pos
    return mean, var, leak

for w in (1.5, 2, 4, 8):
    mu, var = zinf_moments(w)
    print("z_inf w %-4g mean %.4f var %.4f   (dossier: 1.5 0.383/0.649, 2 0.649/0.518, 4 1.363/0.340, 8 2.264/0.250)" % (w, mu, var))
for w, m in ((1.5, 2), (2, 2), (2, 4), (8, 2)):
    p, y0s = ddim_leak(w, m)
    lo, hi = norm.cdf(-(2 * w - 1) * m / 2), norm.cdf(-w * m / 2)
    print("DDIM leak w %g m %g: %.4e (start threshold %.4f), bracket [%.3e, %.3e]" % (w, m, p, y0s, lo, hi))
for w, m in ((2, 2), (2, 4), (8, 2), (8, 4)):
    print("tilted w %g m %g: mean|y>0 %.3f var %.3f leak %.2e" % ((w, m) + tilted(w, m)))
# large-m tilted leak against the asymptotic (2/m) e^{-m^2/8} C(w) / (2^{w-1} sqrt(2 pi)), C(w) = int_0^inf cosh^{1-w}(u) e^{-wu} du
for w in (2, 4):
    C = quad(lambda u: np.cosh(u) ** (1 - w) * np.exp(-w * u), 0, np.inf)[0]
    for m in (8, 16):
        asym = (2 / m) * np.exp(-m * m / 8) * C / (2 ** (w - 1) * np.sqrt(2 * np.pi))
        print("tilted leak w %g m %g: quad %.4e  asymptotic %.4e  ratio %.4f" % (w, m, tilted(w, m)[2], asym, tilted(w, m)[2] / asym))
