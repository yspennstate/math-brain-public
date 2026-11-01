"""T357: exact proportional-limit (n/d = alpha) fixed point for logistic ridge, same model and scaling as calib_path.py:
x ~ N(0, I_d), |w*| = 1, P(y = 1 | x) = sig(beta x.w*), w = argmin mean softplus loss + (lam/2)|w|^2.
Leave-one-out form: Q = mu Z1 + sig_ Z2 (Z1 = z*), P = prox_{c rho_y}(Q), rho_y(t) = softplus(t) - y t,
  (i)   lam mu  = -E[Z1 rho'_y(P)]
  (ii)  1/alpha = 1 - E[1/(1 + c rho''(P))] + lam c
  (iii) sig_^2  = alpha c^2 E[rho'_y(P)^2]
(derived 19 Oct by leave-one-out; checked on ridge regression, where it gives |w|^2 = s^2/(alpha-1) at lam 0 and the
population ridge at alpha -> inf). Then q = |w| = sqrt(mu^2 + sig_^2), c_ = w.w* = mu, rho = mu/q, and the population
risk / first-moment FM exactly as calib_path.pop / calib_cross.pop_more.
argv: alpha beta [lam_min lam_max npts]"""
import sys, math
import numpy as np
from scipy.optimize import root

alpha = float(sys.argv[1]); beta = float(sys.argv[2])
lmin = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-4
lmax = float(sys.argv[4]) if len(sys.argv) > 4 else 30.0
npts = int(sys.argv[5]) if len(sys.argv) > 5 else 241

gx, gw = np.polynomial.hermite_e.hermegauss(int(__import__("os").environ.get("GHN", "80"))); gw = gw / gw.sum()
Z1 = gx[:, None]; Z2 = gx[None, :]; W = gw[:, None] * gw[None, :]
sig = lambda t: 0.5 * (1 + np.tanh(0.5 * t))
softplus = lambda t: np.logaddexp(0, t)
PY1 = sig(beta * Z1)                      # P(y = 1 | Z1)


def prox(Q, y, c):
    P = Q.copy()
    for _ in range(60):
        s = sig(P); f = P + c * (s - y) - Q; P = P - f / (1 + c * s * (1 - s))
    return P


def eqs(v, lam):
    mu, ls, lc = v; sg = math.exp(ls); c = math.exp(lc)
    Q = mu * Z1 + sg * Z2
    r = np.zeros(3)
    for y, wy in ((1.0, PY1), (0.0, 1 - PY1)):
        P = prox(Q, y, c); s = sig(P); d1 = s - y; d2 = s * (1 - s)
        ww = W * wy
        r[0] += (ww * Z1 * d1).sum(); r[1] += (ww / (1 + c * d2)).sum(); r[2] += (ww * d1 ** 2).sum()
    return [lam * mu + r[0], 1 / alpha - 1 + r[1] - lam * c, sg ** 2 - alpha * c ** 2 * r[2]]


def pop(q, cc):
    s = q * gx
    mu = (cc / q ** 2) * s[:, None]; sd = math.sqrt(max(1 - cc ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu + sd * gx[None, :])) * gw[None, :]).sum(1)
    risk = ((ey * softplus(-s) + (1 - ey) * softplus(s)) * gw).sum()
    fm = ((sig(s) - ey) * s * gw).sum()
    return risk, fm


lams = np.exp(np.linspace(math.log(lmax), math.log(lmin), npts))
v = np.array([0.01, math.log(0.01), math.log(0.1 / alpha)]); rows = []
for lam in lams:
    sol = root(eqs, v, args=(lam,), method="hybr", tol=1e-12)
    if not sol.success or max(abs(x) for x in eqs(sol.x, lam)) > 1e-8:
        print(f"  no convergence at lam={lam:.3g}: {sol.message}"); break
    v = sol.x; mu, sg, c = v[0], math.exp(v[1]), math.exp(v[2]); q = math.hypot(mu, sg)
    risk, fm = pop(q, mu); rows.append((lam, mu, sg, c, q, mu / q, risk, fm))
R = np.array(rows)
j = int(np.argmin(R[:, 6]))
# d rho / d q along the path at the risk optimum, and the path lemma's kappa q^2 drho/dq with kappa = E sig'(zhat)... reported as FM
lo, hi = max(j - 3, 0), min(j + 4, len(R))
A = np.polyfit(R[lo:hi, 4], R[lo:hi, 5], 2); drdq = 2 * A[0] * R[j, 4] + A[1]
jr = int(np.argmax(R[:, 5]))
k0 = np.where(np.diff(np.sign(R[:, 7])) != 0)[0]
lcal = R[k0[0], 0] if len(k0) else float("nan")
print(f"alpha={alpha} beta={beta}: lam_risk={R[j,0]:.4g} (q={R[j,4]:.4f} rho={R[j,5]:.4f} FM={R[j,7]:+.5f} drho/dq={drdq:+.4f}) "
      f"lam_rhomax={R[jr,0]:.4g} (rho={R[jr,5]:.4f})  lam(FM=0)={lcal:.4g}  points={len(R)}", flush=True)
if "--table" in sys.argv:
    for r in R[:: max(1, len(R) // 30)]:
        print("  lam %.4g mu %.4f sig %.4f c %.4f q %.4f rho %.4f risk %.5f FM %+.5f" % tuple(r))

# --refine: locate lam_risk (risk min), lam_rhomax (rho max) and lam_cal (FM = 0) to high precision near the grid optimum,
# each fixed point solved fresh from the nearest grid solution (warm start).
if "--refine" in sys.argv:
    from scipy.optimize import minimize_scalar, brentq
    def at(lam):
        k = int(np.argmin(abs(np.log(R[:, 0]) - math.log(lam))))
        v0 = np.array([R[k, 1], math.log(R[k, 2]), math.log(R[k, 3])])
        s = root(eqs, v0, args=(lam,), method="hybr", tol=1e-13)
        mu, sg, c = s.x[0], math.exp(s.x[1]), math.exp(s.x[2]); q = math.hypot(mu, sg)
        rk, fm = pop(q, mu); return q, mu / q, rk, fm
    a, b = math.log(R[min(j + 6, len(R) - 1), 0]), math.log(R[max(j - 6, 0), 0])
    lr = math.exp(minimize_scalar(lambda t: at(math.exp(t))[2], bounds=(a, b), method="bounded", options={"xatol": 1e-10}).x)
    lm = math.exp(minimize_scalar(lambda t: -at(math.exp(t))[1], bounds=(a, b), method="bounded", options={"xatol": 1e-10}).x)
    try: lc = math.exp(brentq(lambda t: at(math.exp(t))[3], a, b, xtol=1e-12))
    except ValueError: lc = float("nan")
    q, rh, rk, fm = at(lr); h = 1e-4
    q1, r1, _, _ = at(lr * math.exp(h)); q0, r0, _, _ = at(lr * math.exp(-h))
    print(f"  REFINED alpha={alpha} beta={beta}: lam_risk={lr:.6g} lam_rhomax={lm:.6g} lam_cal={lc:.6g}  "
          f"lam_cal/lam_risk={lc/lr:.5f} lam_rhomax/lam_risk={lm/lr:.5f}  FM(lam_risk)={fm:+.3e} drho/dq={(r1-r0)/(q1-q0):+.4e} q={q:.5f} rho={rh:.6f}", flush=True)
