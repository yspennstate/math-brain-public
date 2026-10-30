import sys, math
import numpy as np
from scipy.optimize import root
beta, psi = map(float, sys.argv[1:3]); d = int(sys.argv[3]); seed0 = int(sys.argv[4]) if len(sys.argv) > 4 else 100
N = int(psi * d)
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
def resid(x, lam):
    mu, s = x; sg = math.sqrt(s); Vh, A1, R2 = moments(mu, sg); T1, T2, T3 = Ts(lam, Vh)
    return np.array([mu + A1 * T1, mu ** 2 + s - A1 ** 2 * T2])
def Ex(x): return excess(math.hypot(x[0], math.sqrt(x[1])), rho * x[0])
# s -> 0 as lam -> 0 on the n = inf path (s ~ lam^2: at lam = 0, T1 = 1/Vh and T2 = 1/Vh^2, so s = A1^2 (T2 - T1^2) = 0).
# mu^2 + s - A1^2 T2 then cancels to ~1e-9 of mu^2, so solve0 uses the equivalent e2' = s - A1^2 Var_w(g) (equal to e2 where
# e1 = 0), w = mt^2/(S rho^2) (sum 1), g = S G, T1 = E_w g, T2 = E_w g^2; no cancellation.
wv = mt ** 2 / (S * rho ** 2)
def resid2(x, lam):
    mu, s = x; Vh, A1, R2 = moments(mu, math.sqrt(s)); g = S / (lam + Vh * S); gb = (wv * g).sum()
    return np.array([(mu + A1 * gb) / (abs(mu) + 1e-12), 1 - A1 ** 2 * (wv * (g - gb) ** 2).sum() / s])
def solve0(lam, x):
    sol = root(lambda y: resid2([y[0], math.exp(y[1])], lam), [x[0], math.log(x[1])], method="hybr", tol=1e-14)
    return np.array([sol.x[0], math.exp(sol.x[1])])
# cgmt_lam0.py (agent A, 20 Oct 2026): the alpha -> inf limit of alpha lam_risk from the closed form of cgmt_explicit.py.
# Nothing on the n = inf path depends on alpha: alpha enters only through eps = 1/n = 1/(alpha d). So lam_risk(alpha) solves
#   E0'(lam) + D'(lam) / (alpha d) = 0,   D = dE/deps = R2 T3 (J11 Vh/2 - J12 A) / det J   (cgmt_explicit.py),
# and with E0'(0) = 0 (the n = inf ridge path starts at the population optimum) the limit is
#   k_inf = lim alpha lam_risk = -D'(0) / (d E0''(0)).
# E0' is explicit too: dx0/dlam = -J^{-1} de/dlam with de/dlam = (-A1 U1, 2 A1^2 U2), U1 = sum mt^2 G^2/rho^2,
# U2 = sum mt^2 S G^3/rho^2, and E0' = grad E . dx0/dlam, grad E = (A, Vh/2).
def explicit(lam, x):
    mu, s = x; sg = math.sqrt(s); Q = mu * Z1 + sg * Z2; p = sig(Q); s1 = p * (1 - p); s2 = s1 * (1 - 2 * p); s3 = s1 * (1 - 6 * p + 6 * p * p)
    Vh = (W * s1).sum(); A = (W * Z1 * (p - PY1)).sum(); R2 = (W * (p * p - 2 * p * PY1 + PY1)).sum()
    Vm = (W * Z1 * s2).sum(); Vs = (W * s3).sum() / 2; a = A - mu * Vh
    Am = (W * Z1 ** 2 * s1).sum() - Vh - mu * Vm; As = Vm / 2 - mu * Vs
    G = 1 / (lam + Vh * S); T1 = (mt ** 2 * G).sum() / rho ** 2; T2 = (mt ** 2 * S * G ** 2).sum() / rho ** 2
    T3 = (S ** 2 * G ** 2).sum(); T4 = (mt ** 2 * S ** 2 * G ** 3).sum() / rho ** 2
    U1 = (mt ** 2 * G ** 2).sum() / rho ** 2; U2 = (mt ** 2 * S * G ** 3).sum() / rho ** 2
    J = np.array([[1 + Am * T1 - a * T2 * Vm, As * T1 - a * T2 * Vs],
                  [2 * mu - 2 * a * Am * T2 + 2 * a * a * T4 * Vm, 1 - 2 * a * As * T2 + 2 * a * a * T4 * Vs]])
    D = R2 * T3 * (J[0, 0] * Vh / 2 - J[0, 1] * A) / np.linalg.det(J)
    E1 = np.array([A, Vh / 2]) @ np.linalg.solve(J, -np.array([-a * U1, 2 * a * a * U2]))
    return D, E1
print(f"cgmt_lam0: beta {beta} N {N} d {d} seed0 {seed0}: rho {rho:.4f}", flush=True)
kap = (gw * gx * PY1[:, 0]).sum(); l0 = 10.0
x = np.array([kap * (mt ** 2 / (l0 + 0.25 * S)).sum() / rho ** 2, 1e-6 + 0.25 / (1000 * d) * (S ** 2 / (l0 + 0.25 * S) ** 2).sum()])
for lam in np.exp(np.linspace(math.log(10), math.log(2e-2), 120)): x = solve0(lam, x)
lams = np.exp(np.linspace(math.log(2e-2), math.log(1e-8), 240)); rows = []
for lam in lams:
    x = solve0(lam, x); D, E1 = explicit(lam, x); rows.append((lam, Ex(x), D, E1, x[1]))
r = np.array(rows[::-1]); lam_, E0, D, E1, s_ = r.T
# checks: s ~ lam^2, the explicit E0' against differences of the computed excess, and E0'(0) = 0 by extrapolation
k = np.searchsorted(lam_, 1e-4)
print(f"  s/lam^2 at lam {lam_[0]:.1e}, {lam_[k]:.1e}: {s_[0] / lam_[0] ** 2:.6e}, {s_[k] / lam_[k] ** 2:.6e}", flush=True)
print(f"  explicit E0' vs differenced excess at lam {lam_[k]:.3e}: {E1[k]:.6e} vs {np.gradient(E0, lam_)[k]:.6e}", flush=True)
# slopes at 0: quadratic fits on lam <= 1e-6, where the path is polynomial to many digits
m = lam_ <= 1e-6
cE = np.polyfit(lam_[m], E1[m], 2); cD = np.polyfit(lam_[m], D[m], 2); E2 = cE[1]; D1 = cD[1]
print(f"  E0'(0) extrapolated = {cE[2]:.3e} (E0'(1e-6) = {E1[m][-1]:.3e}); E0''(0) = {E2:.6e}; D(0) = {cD[2]:.6e}; "
      f"D'(0) = {D1:.6e}", flush=True)
print(f"  k_inf = lim alpha lam_risk = -D'(0) / (d E0''(0)) = {-D1 / (d * E2):.5f}", flush=True)
Dp = np.gradient(D, lam_)
for alpha in (10, 100, 1000, 10000, 100000):
    f = E1 + Dp / (alpha * d); j = np.where((np.sign(f[:-1]) != np.sign(f[1:])) & (lam_[:-1] > 0))[0]
    if not len(j): print(f"  alpha {alpha}: no root on the grid"); continue
    j = j[0]; lr = lam_[j] - f[j] * (lam_[j + 1] - lam_[j]) / (f[j + 1] - f[j])
    print(f"  alpha {alpha}: alpha lam_risk = {alpha * lr:.5f} (first order in 1/n, full lam dependence)", flush=True)
