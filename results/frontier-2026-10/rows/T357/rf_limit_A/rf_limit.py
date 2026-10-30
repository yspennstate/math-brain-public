"""T357, random features, infinite-data limit (n -> inf at fixed N/d), Gaussian equivalence.
u = tanh(F x) ~ mu1 F x + mus xi (mu0 = 0, tanh odd). The best linear predictor of z* = beta w*.x from u leaves an independent Gaussian
residual: z* = b s + tau Z, s = standardized projection, b = beta rho_max, tau^2 = beta^2 (1 - rho_max^2),
    rho_max^2 = mu1^2 avg_i lam_i / (mu1^2 lam_i + mus^2) over the eigenvalues of F^T F (d x d; zeros when N < d).
So y | u has the link g(s) = E sigma(b s + tau Z): the RF logistic model is MISSPECIFIED for every finite N/d. Any fit zhat = k s on
the radial family; FM = 0 is its risk optimum (path lemma, d rho/dq = 0). This script finds, at n = inf:
  k_FM (risk optimum), OC there, k_OC (OC = 0), and the excess risk paid for OC = 0.
argv: beta [d]"""
import sys, math
import numpy as np
beta = float(sys.argv[1]); d = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
sig = lambda t: 0.5 * (1 + np.tanh(t / 2)); sp = lambda t: np.logaddexp(0, t)
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
gx, gw = np.polynomial.hermite_e.hermegauss(200); gw = gw / gw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
lx, lw = np.polynomial.legendre.leggauss(300); lx = 5 * (lx + 1); lw = 5 * lw * np.exp(-lx ** 2 / 2) / math.sqrt(2 * math.pi)
S = np.concatenate([-lx[::-1], lx]); W = np.concatenate([lw[::-1], lw])  # s on [-10, 10], kinks at 0 handled by the split
rng = np.random.default_rng(0)
print(f"beta {beta}  mu1 {mu1:.5f}  mus^2 {mus2:.5f}  (d {d} for the spectrum)")
print(" N/d   rho_max   tau   k_FM    OC(k_FM)   k_OC   k_OC/k_FM  risk(k_OC)-risk(k_FM)  risk(k_FM)-bayes")
for psi in [0.25, 0.5, 1, 2, 3, 4, 8, 16, 64]:
    N = int(psi * d); F = rng.standard_normal((N, d)) / math.sqrt(d)
    lam = np.linalg.eigvalsh(F.T @ F); lam = np.clip(lam, 0, None)
    r2 = mu1 ** 2 * np.mean(lam / (mu1 ** 2 * lam + mus2)); b = beta * math.sqrt(r2); tau = beta * math.sqrt(1 - r2)
    g = (sig(b * S[:, None] + tau * gx[None, :]) * gw[None, :]).sum(1)
    risk = lambda k: ((g * sp(-k * S) + (1 - g) * sp(k * S)) * W).sum()
    fm = lambda k: ((sig(k * S) - g) * S * W).sum(); oc = lambda k: ((sig(k * S) - g) * np.sign(S) * W).sum()
    def root(f, lo=1e-3, hi=50.0):
        for _ in range(200):
            m = 0.5 * (lo + hi); lo, hi = (m, hi) if f(m) < 0 else (lo, m)
        return 0.5 * (lo + hi)
    kf, ko = root(fm), root(oc)
    bayes = ((-g * np.log(np.clip(g, 1e-300, 1)) - (1 - g) * np.log(np.clip(1 - g, 1e-300, 1))) * W).sum()
    print(f"{psi:5}  {math.sqrt(r2):.4f}  {tau:.4f}  {kf:.4f}  {oc(kf):+.5f}  {ko:.4f}  {ko / kf:.4f}   {risk(ko) - risk(kf):+.2e}            {risk(kf) - bayes:.2e}",
          flush=True)
