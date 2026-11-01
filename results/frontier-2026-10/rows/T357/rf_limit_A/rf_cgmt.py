"""T357, random features at finite alpha: the leave-one-out fixed point of cgmt_ridge.py carried to an anisotropic Gaussian
design (Gaussian equivalence u = mu1 F x + mus xi, Sig = mu1^2 F F' + mus^2 I), same model and scaling as rf_cross.py:
F rows N(0, I/d), w = argmin mean softplus(-y a.u) + (lam/2)|a|^2, P(y = 1 | x) = sig(beta x_1), no intercept.
Teacher in u-space: m = mu1 F e1, rho^2 = m' Sig^-1 m, s = t.u with t = Sig^-1 m/rho, z* = x_1 = rho s + sqrt(1 - rho^2) Z'.
Unknowns mu = cov(zhat, s), sg (cavity spread), c (prox step); Q = mu Z1 + sg Z2, P = prox_{c rho_y}(Q), G = (lam + Vh Sig)^-1:
  Vh = E[rho''(P)/(1 + c rho''(P))],  A1 = E[Z1 rho'(P)] - mu Vh   (Stein; A1 is the y-through-s part),
  (i)   c = (1/n) tr Sig G
  (ii)  mu = -A1 t'Sig G Sig t
  (iii) mu^2 + sg^2 = A1^2 t'Sig G Sig G Sig t + (E rho'^2/n) tr (Sig G Sig G)
Derived 20 Oct 17:2x by the same leave-one-out step as cgmt_ridge.py (Stein on the Gaussian vector u for the mean of
(1/n) sum rho'(P_i) u_i, its fluctuation N(0, E rho'^2 Sig/n)); with Sig = I it reduces to cgmt_ridge.py's (i)-(iii) exactly.
Then q = sqrt(mu^2 + sg^2), cov(zhat, z*) = rho mu, and rf_cross.py's pop() gives CE, OC, excess risk.
argv: beta alpha(n/d) psi(N/d) d seeds [seed0]   (seed0 100 = rf_cross.py's F for seed 0)"""
import sys, math
import numpy as np
from scipy.optimize import root
beta, alpha, psi = map(float, sys.argv[1:4]); d, seeds = int(sys.argv[4]), int(sys.argv[5])
seed0 = int(sys.argv[6]) if len(sys.argv) > 6 else 100
n = alpha * d; N = int(psi * d)
sig = lambda t: 0.5 * (1 + np.tanh(t / 2)); sp = lambda t: np.logaddexp(0, t)
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
gx, gw = np.polynomial.hermite_e.hermegauss(80); gw = gw / gw.sum()
Z1 = gx[:, None]; Z2 = gx[None, :]; W = gw[:, None] * gw[None, :]
bayes = ((sig(beta * gx) * sp(-beta * gx) + (1 - sig(beta * gx)) * sp(beta * gx)) * gw).sum()
def prox(Q, y, c):
    P = Q.copy()
    for _ in range(60):
        s_ = sig(P); f = P + c * (s_ - y) - Q; P = P - f / (1 + c * s_ * (1 - s_))
    return P
def pop(q, cz):
    s_ = q * gx; mu_ = (cz / q ** 2) * s_[:, None]; sd = math.sqrt(max(1 - cz ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu_ + sd * gx[None, :])) * gw[None, :]).sum(1); p = sig(s_)
    return ((np.abs(ey - p) * gw).sum(), ((p - ey) * np.sign(p - .5) * gw).sum(),
            ((ey * sp(-s_) + (1 - ey) * sp(s_)) * gw).sum() - bayes, ((p - ey) * s_ * gw).sum())
def run(F):
    ev, V = np.linalg.eigh(F @ F.T); ev = np.clip(ev, 0, None); S = mu1 ** 2 * ev + mus2; mt = V.T @ (mu1 * F[:, 0])
    rho = math.sqrt((mt ** 2 / S).sum())
    PY1 = (sig(beta * (rho * Z1[:, :, None] + math.sqrt(1 - rho ** 2) * gx[None, None, :])) * gw[None, None, :]).sum(2)
    def eqs(v, lam):
        mu, sg, c = v[0], math.exp(v[1]), math.exp(v[2]); Q = mu * Z1 + sg * Z2
        Vh = A = R2 = 0.0
        for y, wy in ((1.0, PY1), (0.0, 1 - PY1)):
            P = prox(Q, y, c); s_ = sig(P); d1 = s_ - y; d2 = s_ * (1 - s_); ww = W * wy
            Vh += (ww * d2 / (1 + c * d2)).sum(); A += (ww * Z1 * d1).sum(); R2 += (ww * d1 ** 2).sum()
        A1 = A - mu * Vh; G = 1 / (lam + Vh * S)
        return [c - (S * G).sum() / n, mu + A1 * (mt ** 2 * G).sum() / rho ** 2,
                mu ** 2 + sg ** 2 - A1 ** 2 * (mt ** 2 * S * G ** 2).sum() / rho ** 2 - R2 / n * (S ** 2 * G ** 2).sum()]
    lo = min(1e-3, 0.02 / alpha)                            # the crossings fall like 1/alpha (0.083 at alpha 3, 0.0012 at 100)
    lams = np.exp(np.linspace(math.log(10), math.log(lo), int(round(30 * math.log10(10 / lo))) + 1)); out = []
    kap = (gw * gx * PY1[:, 0]).sum(); l0 = lams[0]         # large-lam start: P ~ Q ~ 0, rho' ~ 1/2 - y, Vh ~ 1/4
    c0 = (S / (l0 + 0.25 * S)).sum() / n; mu0 = kap * (mt ** 2 / (l0 + 0.25 * S)).sum() / rho ** 2
    sg0 = math.sqrt(0.25 / n * (S ** 2 / (l0 + 0.25 * S) ** 2).sum()); v = np.array([mu0, math.log(sg0), math.log(c0)])
    def eqs_scaled(v, lam):                                 # same roots; each residual relative to its own size (20 Oct 18:1x:
        e = eqs(v, lam); mu, sg, c = v[0], math.exp(v[1]), math.exp(v[2])   # at alpha >= 100 sg^2 << mu^2 and hybr stalled)
        return [e[0] / c, e[1] / max(abs(mu), 1e-12), e[2] / (mu ** 2 + sg ** 2)]
    for lam in lams:
        sol = root(eqs, v, args=(lam,), method="hybr", tol=1e-12)
        if not sol.success or max(abs(x) for x in eqs(sol.x, lam)) > 1e-8:
            sol = root(eqs_scaled, v, args=(lam,), method="hybr", tol=1e-12)
        if not sol.success or max(abs(x) for x in eqs(sol.x, lam)) > 1e-8:
            print(f"  no convergence at lam {lam:.3g}: {sol.message}", flush=True); break
        v = sol.x; mu, sg = v[0], math.exp(v[1]); q = math.hypot(mu, sg)
        out.append((lam, q, rho * mu) + pop(q, rho * mu))
    return rho, np.array(out)
def cross(r, col):
    o = r[:, col]; i = np.where(np.sign(o[:-1]) != np.sign(o[1:]))[0]
    if not len(i): return float("nan")
    i = i[0]; l0, l1 = math.log(r[i, 0]), math.log(r[i + 1, 0]); return math.exp(l0 + (l1 - l0) * o[i] / (o[i] - o[i + 1]))
def argm(r, col):
    j = min(max(int(np.argmin(r[:, col])), 1), len(r) - 2); xs = np.log(r[j - 1:j + 2, 0]); P = np.polyfit(xs, r[j - 1:j + 2, col], 2)
    return math.exp(-P[1] / (2 * P[0])) if P[0] > 0 else r[j, 0]
print(f"beta {beta} alpha {alpha} N/d {psi} d {d} (n {n:.0f}, N {N}); mu1 {mu1:.5f} mus2 {mus2:.5f}", flush=True)
for k in range(seeds):
    rng = np.random.default_rng(seed0 + k); F = rng.standard_normal((N, d)) / math.sqrt(d)
    rho, r = run(F)
    for row in r[::10]:
        print(f"   lam {row[0]:9.4g}  q {row[1]:6.3f}  c {row[2]:6.3f}  CE {row[3]:.4f}  OC {row[4]:+.4f}  excess {row[5]:.5f}  FM {row[6]:+.4f}")
    lc, lr, lf = cross(r, 4), argm(r, 5), cross(r, 6)
    print(f" F seed {seed0 + k}: rho {rho:.4f}  lam_cal(OC) {lc:.5g}  lam_FM {lf:.5g}  lam_risk {lr:.5g}  cal/risk {lc / lr:.3f}", flush=True)
