"""Independent check of rf_limit.py with REAL tanh features (no Gaussian equivalence in the fit): logistic MLE in a on
u = tanh(F x), n = alpha d, Newton, tiny ridge 1e-8; OC = E[(sigma(zhat) - sigma(z*)) sign(zhat)] and FM = E[(sigma(zhat) - sigma(z*)) zhat]
by Monte Carlo on 4e5 fresh points (tower property, no bins). If the n = inf limit is OC_inf > 0, then OC(alpha) = OC_inf + c/alpha,
so the fit over alpha recovers OC_inf; the GE prediction for this F is printed beside it.
argv: beta d psi seeds"""
import sys, math
import numpy as np
beta, d, psi, seeds = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
N = int(psi * d); sig = lambda t: 0.5 * (1 + np.tanh(t / 2))
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum(); gx, gw = np.polynomial.hermite_e.hermegauss(200); gw = gw / gw.sum()
lx, lw = np.polynomial.legendre.leggauss(300); lx = 5 * (lx + 1); lw = 5 * lw * np.exp(-lx ** 2 / 2) / math.sqrt(2 * math.pi)
S = np.concatenate([-lx[::-1], lx]); W = np.concatenate([lw[::-1], lw])
def ge_pred(F):
    nrm = np.linalg.norm(F, axis=1); mu1 = np.array([(hw * (1 - np.tanh(r * hx) ** 2)).sum() for r in nrm])
    v = np.array([(hw * np.tanh(r * hx) ** 2).sum() for r in nrm])
    Sig = (mu1[:, None] * mu1[None, :]) * (F @ F.T); np.fill_diagonal(Sig, v)
    cz = beta * mu1 * F[:, 0]; r2 = cz @ np.linalg.solve(Sig, cz) / beta ** 2
    b, tau = beta * math.sqrt(r2), beta * math.sqrt(max(1 - r2, 0)); g = (sig(b * S[:, None] + tau * gx[None, :]) * gw[None, :]).sum(1)
    fm = lambda k: ((sig(k * S) - g) * S * W).sum(); lo, hi = 1e-3, 50.0
    for _ in range(200):
        m = 0.5 * (lo + hi); lo, hi = (m, hi) if fm(m) < 0 else (lo, m)
    return math.sqrt(r2), ((sig(lo * S) - g) * np.sign(S) * W).sum()
for sd in range(seeds):
    rng = np.random.default_rng(1000 + sd); F = rng.standard_normal((N, d)) / math.sqrt(d)
    rho, oc_ge = ge_pred(F); Xt = rng.standard_normal((400000, d)); Ut = np.tanh(Xt @ F.T); pt = sig(beta * Xt[:, 0])
    out = []
    for alpha in [25, 50, 100, 200]:
        n = int(alpha * d); X = rng.standard_normal((n, d)); y = (rng.random(n) < sig(beta * X[:, 0])).astype(float); U = np.tanh(X @ F.T)
        a = np.zeros(N)
        for _ in range(60):
            p = sig(U @ a); gr = U.T @ (p - y) / n + 1e-8 * a; H = (U * (p * (1 - p))[:, None]).T @ U / n + 1e-8 * np.eye(N)
            st = np.linalg.solve(H, gr); a -= st
            if np.abs(st).max() < 1e-10: break
        zh = Ut @ a; diff = sig(zh) - pt; oc = (diff * np.sign(zh)).mean(); se = (diff * np.sign(zh)).std() / math.sqrt(len(zh))
        out.append((alpha, oc, se)); print(f"  seed {sd} alpha {alpha}: OC {oc:+.5f} +- {se:.5f}  FM {(diff * zh).mean():+.5f}", flush=True)
    A = np.array([[1, 1 / al] for al, _, _ in out]); y_ = np.array([o for _, o, _ in out]); coef = np.linalg.lstsq(A, y_, rcond=None)[0]
    print(f"seed {sd}: rho_max(GE) {rho:.4f}  OC_inf fit {coef[0]:+.5f} (slope c {coef[1]:+.4f})  GE prediction {oc_ge:+.5f}", flush=True)
