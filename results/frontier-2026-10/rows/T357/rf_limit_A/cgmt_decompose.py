"""T357 (agent A, 20 Oct 2026): which 1/alpha ingredient of the rf_cgmt.py fixed point sets lam_risk.
The fixed point has two finite-n effects: the noise term (E rho'^2/n) tr(Sig G Sig G) in equation (iii), and the prox step c in
P = prox_{c rho}(Q) (which enters Vh = E[rho''/(1 + c rho'')] and A1 = E[Z1 rho'(P)] - mu Vh). Switching each off in turn
(NOISE=0 drops the term; PROXC=0 sets P = Q and Vh = E rho''(Q)) and locating the risk minimum shows which one carries alpha
lam_risk (0.0768 at beta 2, 0.0296 at beta 5 with both on; the fixed-N closed form gave 0.0518 / 0.0135).
Same model, F and quadrature as rf_cgmt.py. argv: beta alpha psi d [seed0]"""
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
def prox(Q, y, c):
    P = Q.copy()
    for _ in range(60):
        s_ = sig(P); f = P + c * (s_ - y) - Q; P = P - f / (1 + c * s_ * (1 - s_))
    return P
def excess(q, cz):
    s_ = q * gx; mu_ = (cz / q ** 2) * s_[:, None]; sd = math.sqrt(max(1 - cz ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu_ + sd * gx[None, :])) * gw[None, :]).sum(1)
    return ((ey * sp(-s_) + (1 - ey) * sp(s_)) * gw).sum() - bayes
F = np.random.default_rng(seed0).standard_normal((N, d)) / math.sqrt(d)
ev, V = np.linalg.eigh(F @ F.T); ev = np.clip(ev, 0, None); S = mu1 ** 2 * ev + mus2; mt = V.T @ (mu1 * F[:, 0])
rho = math.sqrt((mt ** 2 / S).sum())
PY1 = (sig(beta * (rho * Z1[:, :, None] + math.sqrt(1 - rho ** 2) * gx[None, None, :])) * gw[None, None, :]).sum(2)
kap = (gw * gx * PY1[:, 0]).sum()
def eqs(v, lam, NOISE, PROXC):
    mu, sg, c = v[0], math.exp(v[1]), math.exp(v[2]); Q = mu * Z1 + sg * Z2
    Vh = A = R2 = 0.0
    for y, wy in ((1.0, PY1), (0.0, 1 - PY1)):
        P = prox(Q, y, c) if PROXC else Q; s_ = sig(P); d1 = s_ - y; d2 = s_ * (1 - s_); ww = W * wy
        Vh += (ww * (d2 / (1 + c * d2) if PROXC else d2)).sum(); A += (ww * Z1 * d1).sum(); R2 += (ww * d1 ** 2).sum()
    A1 = A - mu * Vh; G = 1 / (lam + Vh * S)
    return [(c - (S * G).sum() / n) / c, (mu + A1 * (mt ** 2 * G).sum() / rho ** 2) / max(abs(mu), 1e-12),
            (mu ** 2 + sg ** 2 - A1 ** 2 * (mt ** 2 * S * G ** 2).sum() / rho ** 2 - NOISE * R2 / n * (S ** 2 * G ** 2).sum())
            / (mu ** 2 + sg ** 2)]
def lam_risk(NOISE, PROXC):
    lo = 0.01 / alpha
    lams = np.exp(np.linspace(math.log(10), math.log(lo), int(round(40 * math.log10(10 / lo))) + 1))
    l0 = lams[0]; c0 = (S / (l0 + 0.25 * S)).sum() / n; mu0 = kap * (mt ** 2 / (l0 + 0.25 * S)).sum() / rho ** 2
    sg0 = math.sqrt(0.25 / n * (S ** 2 / (l0 + 0.25 * S) ** 2).sum() + 1e-6); v = np.array([mu0, math.log(sg0), math.log(c0)])
    out = []
    for lam in lams:
        sol = root(eqs, v, args=(lam, NOISE, PROXC), method="hybr", tol=1e-13)
        if not sol.success or max(abs(x) for x in eqs(sol.x, lam, NOISE, PROXC)) > 1e-9:
            print(f"   no convergence at lam {lam:.3g} (NOISE {NOISE} PROXC {PROXC}): {sol.message}", flush=True); break
        v = sol.x; mu, sg = v[0], math.exp(v[1]); q = math.hypot(mu, sg); out.append((lam, excess(q, rho * mu)))
    r = np.array(out); j = min(max(int(np.argmin(r[:, 1])), 1), len(r) - 2)
    xs = np.log(r[j - 1:j + 2, 0]); P = np.polyfit(xs, r[j - 1:j + 2, 1], 2)
    lr = math.exp(-P[1] / (2 * P[0])) if P[0] > 0 else r[j, 0]
    return lr, r[:, 1].min(), (j == 1 or j == len(r) - 2)
print(__doc__); print(f"beta {beta} alpha {alpha} N {N} d {d} seed0 {seed0}: rho {rho:.4f}", flush=True)
for NOISE, PROXC in ((1, 1), (1, 0), (0, 1)):
    lr, ex, edge = lam_risk(NOISE, PROXC)
    print(f"  NOISE {NOISE} PROXC {PROXC}: lam_risk {lr:.5g}  alpha*lam_risk {alpha * lr:.5f}  min excess {ex:.4e}"
          + ("  (minimum at the grid edge)" if edge else ""), flush=True)
