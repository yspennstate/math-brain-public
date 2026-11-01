import sys, math
import numpy as np
from scipy.optimize import brentq
beta, psi = map(float, sys.argv[1:3]); d = int(sys.argv[3]); seed0 = int(sys.argv[4]) if len(sys.argv) > 4 else 100
N = int(psi * d)
sig = lambda t: 0.5 * (1 + np.tanh(t / 2))
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
gx, gw = np.polynomial.hermite_e.hermegauss(80); gw = gw / gw.sum()
Z1 = gx[:, None]; Z2 = gx[None, :]; W = gw[:, None] * gw[None, :]
F = np.random.default_rng(seed0).standard_normal((N, d)) / math.sqrt(d)
ev, V = np.linalg.eigh(F @ F.T); ev = np.clip(ev, 0, None); S = mu1 ** 2 * ev + mus2; mt = V.T @ (mu1 * F[:, 0])
rho = math.sqrt((mt ** 2 / S).sum())
PY1 = (sig(beta * (rho * Z1[:, :, None] + math.sqrt(1 - rho ** 2) * gx[None, None, :])) * gw[None, None, :]).sum(2)
# cgmt_lam0_closed.py (agent A, 20 Oct 2026): the lam = 0 quantities of cgmt_lam0.py in closed form, no path solve.
# At lam = 0 on the n = inf path: s = 0, A(mu0) = 0, T1 = 1/Vh, T2 = 1/Vh^2, T4 = 1/Vh^3, T3 = N/Vh^2, and J collapses:
#   J11 = A_mu/Vh (A_mu = E[Z1^2 sig'(mu0 Z1)]), J21 = 2 mu0 J11, J12 = Vm/(2 Vh), J22 = 1 + mu0 Vm/Vh, det J = J11, so
#   D(0) = N R2 / (2 Vh).
# First order along the path (moments are even in sg, so s = O(lam^2) does not enter at first order):
#   g = S G = 1/Vh - lam/(Vh^2 S) + ..., w = mt^2/(S rho^2):  mu'(0) = m1 = -mu0 E_w(1/S) / A_mu,
#   s = A1^2 Var_w(g) = c lam^2 + ...,                         c = mu0^2 Var_w(1/S) / Vh^2,
#   E_mu = A, E_s = Vh/2, E_mumu = A_mu  =>  E0''(0) = A_mu m1^2 + Vh c = mu0^2 [E_w(1/S)^2 / A_mu + Var_w(1/S) / Vh].
# D'(0) = d/dlam D(lam, mu0 + m1 lam, c lam^2) (the second-order path terms do not reach a first derivative), central
# difference in lam only. Its leading piece is T3'/T3 = -2 [mean(1/S)/Vh + Vh_mu m1/Vh] (dT3/dVh = -2 N/Vh^3).
def mom(mu, s):
    Q = mu * Z1 + math.sqrt(s) * Z2; p = sig(Q); s1 = p * (1 - p); s2 = s1 * (1 - 2 * p); s3 = s1 * (1 - 6 * p + 6 * p * p)
    Vh = (W * s1).sum(); A = (W * Z1 * (p - PY1)).sum(); R2 = (W * (p * p - 2 * p * PY1 + PY1)).sum()
    Vm = (W * Z1 * s2).sum(); Vs = (W * s3).sum() / 2; EZ2s1 = (W * Z1 ** 2 * s1).sum()
    return Vh, A, R2, Vm, Vs, EZ2s1
def Dfun(lam, mu, s):
    Vh, A, R2, Vm, Vs, EZ2s1 = mom(mu, s); a = A - mu * Vh
    Am = EZ2s1 - Vh - mu * Vm; As = Vm / 2 - mu * Vs
    G = 1 / (lam + Vh * S); T1 = (mt ** 2 * G).sum() / rho ** 2; T2 = (mt ** 2 * S * G ** 2).sum() / rho ** 2
    T3 = (S ** 2 * G ** 2).sum(); T4 = (mt ** 2 * S ** 2 * G ** 3).sum() / rho ** 2
    J = np.array([[1 + Am * T1 - a * T2 * Vm, As * T1 - a * T2 * Vs],
                  [2 * mu - 2 * a * Am * T2 + 2 * a * a * T4 * Vm, 1 - 2 * a * As * T2 + 2 * a * a * T4 * Vs]])
    return R2 * T3 * (J[0, 0] * Vh / 2 - J[0, 1] * A) / np.linalg.det(J), R2, T3, J
mu0 = brentq(lambda m: mom(m, 0.0)[1], 1e-3, 50.0, xtol=1e-15)
Vh, A, R2, Vm, Vs, EZ2s1 = mom(mu0, 0.0); A_mu = EZ2s1
w = mt ** 2 / (S * rho ** 2); Ew = (w / S).sum(); Varw = (w * (1 / S - Ew) ** 2).sum()
m1 = -mu0 * Ew / A_mu; c = mu0 ** 2 * Varw / Vh ** 2
E2 = mu0 ** 2 * (Ew ** 2 / A_mu + Varw / Vh)
h = 1e-6; Dp = (Dfun(h, mu0 + m1 * h, c * h * h)[0] - Dfun(-h, mu0 - m1 * h, c * h * h)[0]) / (2 * h)
D0 = Dfun(0.0, mu0, 0.0)[0]
hm = 1e-6; Vh_mu = (mom(mu0 + hm, 0.0)[0] - mom(mu0 - hm, 0.0)[0]) / (2 * hm)
lead = -2 * ((1 / S).mean() / Vh + Vh_mu * m1 / Vh)
print(f"cgmt_lam0_closed: beta {beta} N {N} d {d} seed0 {seed0}: rho {rho:.4f}")
print(f"  mu0 {mu0:.6f} (A(mu0) = {A:.1e}); Vh {Vh:.6f}; R2 {R2:.6f}; R2/Vh {R2 / Vh:.6f}; A_mu {A_mu:.6f}")
print(f"  E_w(1/S) {Ew:.6f}; Var_w(1/S) {Varw:.6f}; mean(1/S) {(1 / S).mean():.6f}; m1 {m1:.6e}; c = s/lam^2 {c:.6e}")
print(f"  D(0) closed N R2/(2 Vh) = {N * R2 / (2 * Vh):.6e}; from the full formula {D0:.6e}")
print(f"  E0''(0) closed = {E2:.6e}  (A_mu m1^2 {A_mu * m1 ** 2:.4e} + Vh c {Vh * c:.4e})")
print(f"  D'(0) = {Dp:.6e}; D(0) T3'/T3 = {D0 * lead:.6e} ({D0 * lead / Dp:.4f} of it)")
print(f"  k_inf = -D'(0)/(d E0''(0)) = {-Dp / (d * E2):.5f}")
