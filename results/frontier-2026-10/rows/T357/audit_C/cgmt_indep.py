"""T357 audit (agent C, 20 Oct 2026): independent numerics for the logistic-ridge proportional-limit fixed point and the
calibrating vs risk-optimal lambda. Same three equations as cgmt_ridge.py (re-derived in the audit), but every Gaussian average by
the trapezoid rule on a fine uniform grid (spectrally accurate for these analytic integrands; step H, default 0.05 on [-10, 10]),
the outer half-line integrals of the population quantities by adaptive quad, and the prox solved by bracketed Newton to 1e-14.
Reports lam_risk (population logistic risk min), lam_FM (first-moment calibration E[(p - E[y|p]) zhat] = 0) and lam_OC (signed
over-confidence E[(p - E[y|p]) sign(zhat)] = 0, the 19 Oct finite-d definition).  argv: alpha beta lam_guess"""
import sys, math, os
import numpy as np
from scipy.optimize import root, minimize_scalar, brentq
from scipy.integrate import quad

H = float(os.environ.get("H", "0.05"))
z = np.arange(-10, 10 + H / 2, H); wz = np.exp(-z * z / 2); wz /= wz.sum()
Z1 = z[:, None]; Z2 = z[None, :]; W = wz[:, None] * wz[None, :]
alpha, beta, lg = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
sig = lambda t: 0.5 * (1 + np.tanh(0.5 * t))
PY1 = sig(beta * Z1)

def prox(Q, y, c):                       # solve P + c (sig(P) - y) = Q; monotone, Newton from Q - c (sig(Q) - y)
    P = Q - c * (sig(Q) - y)
    for _ in range(100):
        s = sig(P); f = P + c * (s - y) - Q; step = f / (1 + c * s * (1 - s)); P = P - step
        if np.abs(step).max() < 1e-14: break
    return P

def eqs(v, lam):
    mu, sg, c = v[0], math.exp(v[1]), math.exp(v[2])
    Q = mu * Z1 + sg * Z2; a = b = e = 0.0
    for y, wy in ((1.0, PY1), (0.0, 1 - PY1)):
        P = prox(Q, y, c); s = sig(P); d1 = s - y; ww = W * wy
        a += (ww * Z1 * d1).sum(); b += (ww / (1 + c * s * (1 - s))).sum(); e += (ww * d1 * d1).sum()
    return [lam * mu + a, 1 / alpha - 1 + b - lam * c, sg * sg - alpha * c * c * e]

def ey(s, q, cc):                         # E[y | zhat = s] for zhat = w.x with |w| = q, w.w* = cc
    m = cc / q ** 2 * s; sd = math.sqrt(max(1 - cc * cc / q ** 2, 0.0))
    return float((sig(beta * (m + sd * z)) * wz).sum())

def popq(q, cc):                          # risk, FM, OC as integrals over zhat = q u, u ~ N(0,1); m(s) is odd, use u > 0 twice
    phi = lambda u: math.exp(-u * u / 2) / math.sqrt(2 * math.pi)
    sp = lambda t: math.log1p(math.exp(-abs(t))) + max(t, 0)
    def r_int(u):
        s = q * u; e1 = ey(s, q, cc); e2 = 1 - e1  # E[y|-s] = 1 - E[y|s]
        return phi(u) * (e1 * sp(-s) + (1 - e1) * sp(s) + e2 * sp(s) + (1 - e2) * sp(-s))
    m = lambda u: float(sig(q * u)) - ey(q * u, q, cc)
    risk = quad(r_int, 0, 12, epsabs=1e-13, epsrel=1e-13, limit=400)[0]
    fm = 2 * quad(lambda u: phi(u) * m(u) * q * u, 0, 12, epsabs=1e-14, epsrel=1e-12, limit=400)[0]
    oc = 2 * quad(lambda u: phi(u) * m(u), 0, 12, epsabs=1e-14, epsrel=1e-12, limit=400)[0]
    return risk, fm, oc

# continuation from large lam down to 0.3 lam_guess
v = np.array([0.01, math.log(0.01), math.log(0.1 / alpha)]); path = []
for lam in np.exp(np.linspace(math.log(30.0), math.log(0.3 * lg), 70)):
    sol = root(eqs, v, args=(lam,), method="hybr", tol=1e-13)
    if not sol.success: print("no convergence", lam); break
    v = sol.x; path.append((lam, v.copy()))
def at(lam):
    k = int(np.argmin([abs(math.log(l / lam)) for l, _ in path]))
    s = root(eqs, path[k][1], args=(lam,), method="hybr", tol=1e-14)
    res = max(abs(t) for t in eqs(s.x, lam))
    mu, sg = s.x[0], math.exp(s.x[1]); q = math.hypot(mu, sg)
    return (q, mu / q) + popq(q, mu) + (res,)
a, b = math.log(0.5 * lg), math.log(2.0 * lg)
lr = math.exp(minimize_scalar(lambda t: at(math.exp(t))[2], bounds=(a, b), method="bounded", options={"xatol": 1e-9}).x)
lf = math.exp(brentq(lambda t: at(math.exp(t))[3], a, b, xtol=1e-12))
lo = math.exp(brentq(lambda t: at(math.exp(t))[4], a, b, xtol=1e-12))
q, rh, rk, fm, oc, res = at(lr)
print("alpha %g beta %g H %g: lam_risk %.7g  lam_FM %.7g (ratio %.6f)  lam_OC %.7g (ratio %.6f)  at lam_risk q %.6f rho %.7f FM %+.3e OC %+.3e  residual %.1e"
      % (alpha, beta, H, lr, lf, lf / lr, lo, lo / lr, q, rh, fm, oc, res), flush=True)
