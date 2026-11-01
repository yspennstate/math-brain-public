"""T357, random features, n = inf ridge path under Gaussian equivalence. For any zhat jointly Gaussian with z* = beta w*.x,
R(q, c) = A(q) - kappa_beta c (path lemma, 19 Oct 06:4x; c = cov(zhat, w*.x), A(q) = E softplus(q g)). Population ridge:
  min_a A(sqrt(a' Sig a)) - kappa_beta a.m + lam |a|^2/2,  Sig = mu1^2 F F' + mus^2 I,  m = mu1 F w*  (c = a.m),
  so a = kappa (A'(q)/q Sig + lam I)^{-1} m with q solved self-consistently. Reports lam_OC (OC = 0), OC at lam = 0+, the risk cost
  R(lam_OC) - R(0+), and the radial (temperature) cost from rf_limit.py for comparison.
argv: beta psi [d] [seed]   (seed 100 = rf_cgmt.py and rf_cross.py F for seed 0)"""
import sys, math
import numpy as np
beta, psi = float(sys.argv[1]), float(sys.argv[2]); d = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
sig = lambda t: 0.5 * (1 + np.tanh(t / 2)); sp = lambda t: np.logaddexp(0, t)
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
kap = (hw * sig(beta * hx) * hx).sum()
A = lambda q: (hw * sp(q * hx)).sum(); A1 = lambda q: (hw * sig(q * hx) * hx).sum()
lx, lw = np.polynomial.legendre.leggauss(200); lx = 5 * (lx + 1); lw = 5 * lw * np.exp(-lx ** 2 / 2) / math.sqrt(2 * math.pi)
ux = np.concatenate([-lx[::-1], lx]); uw = np.concatenate([lw[::-1], lw])
def oc_fm(q, c):  # zhat = q u, u ~ N(0,1); w*.x | u ~ N(c u / q, 1 - c^2/q^2)
    mu = (c / q) * ux; sd = math.sqrt(max(1 - c ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu[:, None] + sd * hx[None, :])) * hw[None, :]).sum(1); p = sig(q * ux)
    return ((p - ey) * np.sign(ux) * uw).sum(), ((p - ey) * q * ux * uw).sum()
rng = np.random.default_rng(int(sys.argv[4]) if len(sys.argv) > 4 else 0); N = int(psi * d); F = rng.standard_normal((N, d)) / math.sqrt(d)
ev, V = np.linalg.eigh(F @ F.T); ev = np.clip(ev, 0, None); s = mu1 ** 2 * ev + mus2; mt = V.T @ (mu1 * F[:, 0])
def fit(lam):
    def h(q):
        a = kap * mt / (A1(q) / q * s + lam); return q - math.sqrt((s * a * a).sum()), a
    lo, hi = 1e-4, 60.0
    for _ in range(100):
        m = 0.5 * (lo + hi); lo, hi = (m, hi) if h(m)[0] < 0 else (lo, m)
    q = 0.5 * (lo + hi); a = h(q)[1]; c = (a * mt).sum(); return q, c, A(q) - kap * c
q0, c0, R0 = fit(1e-12); oc0, fm0 = oc_fm(q0, c0)
print(f"beta {beta} N/d {psi} d {d}: lam->0: q {q0:.4f} rho {c0 / q0:.4f} OC {oc0:+.5f} FM {fm0:+.2e} risk {R0:.6f}")
lams = np.logspace(-6, 0, 61); prev = None
for lam in lams:
    q, c, R = fit(lam); oc, fm = oc_fm(q, c)
    if prev is not None and prev[1] > 0 >= oc:
        l0, o0, R_0 = prev; t = o0 / (o0 - oc); lo_, hi_ = l0, lam
        for _ in range(60):
            m = math.sqrt(lo_ * hi_); om = oc_fm(*fit(m)[:2])[0]; lo_, hi_ = (m, hi_) if om > 0 else (lo_, m)
        qo, co, Ro = fit(lo_)
        print(f"  lam_OC {lo_:.5g}: q {qo:.4f} rho {co / qo:.4f}  risk cost {Ro - R0:+.3e}  (FM there {oc_fm(qo, co)[1]:+.5f})")
        break
    prev = (lam, oc, R)
