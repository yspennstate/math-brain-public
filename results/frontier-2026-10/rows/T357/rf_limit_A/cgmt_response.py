import sys, math
import numpy as np
from scipy.optimize import root
beta, alpha, psi = map(float, sys.argv[1:4]); d = int(sys.argv[4]); seed0 = int(sys.argv[5]) if len(sys.argv) > 5 else 100
n = alpha * d; N = int(psi * d)
sig = lambda t: 0.5 * (1 + np.tanh(t / 2)); sp = lambda t: np.logaddexp(0, t)
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
gx, gw = np.polynomial.hermite_e.hermegauss(80); gw = gw / gw.sum()
Z1 = gx[:, None]; Z2 = gx[None, :]; W = gw[:, None] * gw[None, :]
bayes = ((sig(beta * gx) * sp(-beta * gx) + (1 - sig(beta * gx)) * sp(beta * gx)) * gw).sum()
def excess(q, cz):
    s_ = q * gx; mu_ = (cz / q ** 2) * s_[:, None]; sd = math.sqrt(max(1 - cz ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu_ + sd * gx[None, :])) * gw[None, :]).sum(1)
    return ((ey * sp(-s_) + (1 - ey) * sp(s_)) * gw).sum() - bayes
F = np.random.default_rng(seed0).standard_normal((N, d)) / math.sqrt(d)
ev, V = np.linalg.eigh(F @ F.T); ev = np.clip(ev, 0, None); S = mu1 ** 2 * ev + mus2; mt = V.T @ (mu1 * F[:, 0])
rho = math.sqrt((mt ** 2 / S).sum())
PY1 = (sig(beta * (rho * Z1[:, :, None] + math.sqrt(1 - rho ** 2) * gx[None, None, :])) * gw[None, None, :]).sum(2)
def moments(mu, sg):
    Q = mu * Z1 + sg * Z2; s_ = sig(Q); d2 = (W * s_ * (1 - s_)).sum()
    A = (W * Z1 * (s_ - PY1)).sum(); R2 = (W * (s_ * s_ - 2 * s_ * PY1 + PY1)).sum()
    return d2, A - mu * d2, R2
def Ts(lam, Vh):
    G = 1 / (lam + Vh * S)
    return (mt ** 2 * G).sum() / rho ** 2, (mt ** 2 * S * G ** 2).sum() / rho ** 2, (S ** 2 * G ** 2).sum()
# cgmt_response.py (agent A, 20 Oct 2026): the FEEDBACK share of alpha lam_risk as an exact first-order response.
# x = (mu, s = sg^2); e1 = mu + A1 T1, e2 = mu^2 + s - A1^2 T2 - eps R2 T3, eps = 1/n. At eps = 0 the n = inf root x0; then
# dx/deps = J^{-1} (0, R2 T3) with J = de/dx, and dE/deps = grad E . dx/deps. Frozen keeps only dx = (0, R2 T3), i.e. dE_s R2 T3.
# Feedback = grad E . J^{-1}(0, R2 T3) - dE_s R2 T3. Prediction: the zero of E0' + (1/n)(dE/deps)' on the grid = the full sweep.
def resid(x, lam, eps):
    mu, s = x; sg = math.sqrt(s); Vh, A1, R2 = moments(mu, sg); T1, T2, T3 = Ts(lam, Vh)
    return np.array([mu + A1 * T1, mu ** 2 + s - A1 ** 2 * T2 - eps * R2 * T3])
def Ex(x): return excess(math.hypot(x[0], math.sqrt(x[1])), rho * x[0])
def solve0(lam, x):
    sol = root(lambda y: resid([y[0], math.exp(y[1])], lam, 0) / np.array([abs(y[0]) + 1e-12, y[0] ** 2 + math.exp(y[1])]),
               [x[0], math.log(x[1])], method="hybr", tol=1e-14)
    return np.array([sol.x[0], math.exp(sol.x[1])])
HREL = float(sys.argv[6]) if len(sys.argv) > 6 else 1e-6
print(f"cgmt_response: HREL {HREL} beta {beta} alpha {alpha} N {N} d {d} seed0 {seed0}: rho {rho:.4f}", flush=True)
kap = (gw * gx * PY1[:, 0]).sum(); l0 = 10.0
x = np.array([kap * (mt ** 2 / (l0 + 0.25 * S)).sum() / rho ** 2, 1e-6 + 0.25 / n * (S ** 2 / (l0 + 0.25 * S) ** 2).sum()])
for lam in np.exp(np.linspace(math.log(10), math.log(0.3 / alpha), 120)): x = solve0(lam, x)
lams = np.exp(np.linspace(math.log(0.3 / alpha), math.log(0.003 / alpha), 81)); rows = []
for lam in lams:
    x = solve0(lam, x); mu, s = x; Vh, A1, R2 = moments(mu, math.sqrt(s)); T3 = Ts(lam, Vh)[2]
    h = np.array([HREL * abs(mu), HREL * s]); J = np.zeros((2, 2)); gE = np.zeros(2)
    for i in range(2):
        e = np.zeros(2); e[i] = h[i]
        J[:, i] = (resid(x + e, lam, 0) - resid(x - e, lam, 0)) / (2 * h[i]); gE[i] = (Ex(x + e) - Ex(x - e)) / (2 * h[i])
    f = np.array([0.0, R2 * T3]); dx = np.linalg.solve(J, f)
    rows.append((lam, Ex(x), gE @ dx, gE[1] * R2 * T3, Vh * R2 * T3 / 2))
r = np.array(rows); lam_ = r[:, 0]
print(f"  Stein check dE/ds = Vh/2 at three lam: " + " ".join(f"{a:.6e}/{b:.6e}" for a, b in zip(r[::40, 3], r[::40, 4])), flush=True)
def zero(tot):
    fz = np.gradient(r[:, 1], lam_) + np.gradient(tot, lam_) / n; k = np.where(np.sign(fz[:-1]) != np.sign(fz[1:]))[0]
    if not len(k): return float("nan")
    k = k[0]; return lam_[k] - fz[k] * (lam_[k + 1] - lam_[k]) / (fz[k + 1] - fz[k])
lf, lr = zero(r[:, 3]), zero(r[:, 2])
print(f"  first order, frozen only: alpha*lam = {alpha * lf:.5f}   with the feedback: alpha*lam = {alpha * lr:.5f}", flush=True)
print(f"  feedback / frozen in dE/deps at three lam: " + " ".join(f"{l:.3g}:{(a - b) / b:+.4f}" for l, a, b in zip(lam_[::40], r[::40, 2], r[::40, 3])), flush=True)
k = int(np.argmin(abs(lam_ - lr))); mu, s = r[k, 0], 0
print(f"  dx/deps at alpha*lam {alpha * lam_[k]:.4f}: J^-1 (0, R2 T3) vs frozen (0, R2 T3) - ratio of the s components and the mu shift are the feedback channels", flush=True)
