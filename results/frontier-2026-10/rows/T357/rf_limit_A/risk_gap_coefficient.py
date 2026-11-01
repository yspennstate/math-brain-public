"""T357 (agent A, 20 Oct 2026): closed form for k_risk = lim alpha lam_risk, the companion of fm_gap_coefficient.py.
Exact at every n: dw_hat/dlam = -Hh^{-1} w_hat (Hh = empirical Hessian + lam), and grad Rhat(w_hat) = -lam w_hat, so the
population risk R(w_hat_lam) is stationary where
    lam_risk = [grad R - grad Rhat](w_hat) . v / (w_hat' Hh^{-1} w_hat),   v = Hh^{-1} w_hat,
the same shape as lam_FM = [grad R - grad Rhat](w_hat) . w_hat / |w_hat|^2 with w_hat replaced by v. The numerator is the
train-test gap of the statistic rho'(zhat) zeta, zeta = x.v. Leave one out: x_i.Hh^{-1} = x_i.H_{-i}^{-1}/(1 + c rho''_i) and
w_hat = w_{-i} - (1/n) H_{-i}^{-1} x_i rho'(P_i), so a training zeta_i = (zeta_cav - c2 rho'(P_i))/(1 + c rho''(P_i)) with
c = (1/n) tr Sig H^{-1}, c2 = (1/n) tr Sig H^{-2}. (The move of the other points' Hessian weights by w_hat - w_{-i} enters with
E sig''(zhat) = 0 and drops.) To first order in 1/alpha
    gap = 2 c E[rho'' rho' zeta] + c2 E rho'^2,
H = E sig'(zhat) x x' = Vh Sig + gam Sig a a' Sig (Stein, gam = E sig'''(zhat)), all at the n = inf fit a_0 = kappa Sig^{-1} m / Vh.
So k_risk = psi [2 E(rho'' rho' zeta) / Vh + mean(1/s) E rho'^2 / Vh^2] / (a_0' H^{-1} a_0), s the spectrum of Sig.
Compared with the alpha sweep's alpha lam_risk (rf_cgmt_*_v2.txt). argv: beta psi [d] [seed]"""
import sys, math
src = open(__file__.replace("risk_gap_coefficient.py", "rf_ridge_inf.py"), encoding="utf-8").read()
src = src[:src.index("q0, c0, R0 = fit(1e-12)")]
src = src.replace("q = 0.5 * (lo + hi); a = h(q)[1]; c = (a * mt).sum(); return q, c, A(q) - kap * c",
                  "q = 0.5 * (lo + hi); a = h(q)[1]; c = (a * mt).sum(); return q, c, A(q) - kap * c, a")
g = {"__name__": "rf_ridge_inf_body"}; exec(compile(src, "rf_ridge_inf.py", "exec"), g)
np, sig, hx, hw, ux, uw, beta, psi = g["np"], g["sig"], g["hx"], g["hw"], g["ux"], g["uw"], g["beta"], g["psi"]
s, mt = g["s"], g["mt"]
print(__doc__)
for lam0 in (1e-8, 1e-6):
    q, c, R, a = g["fit"](lam0)
    mu = (c / q) * ux; sd = math.sqrt(max(1 - c ** 2 / q ** 2, 0))
    X1 = mu[:, None] + sd * hx[None, :]
    ey = (sig(beta * X1) * hw[None, :]).sum(1)                 # P(y = 1 | u)
    eyx = (sig(beta * X1) * X1 * hw[None, :]).sum(1)           # E[y x1 | u]
    z = q * ux; p = sig(z); d1 = p * (1 - p)
    Vh = (d1 * uw).sum(); gam = (d1 * (ux ** 2 - 1) * uw).sum() / q ** 2
    Erp2 = ((p * p - 2 * p * ey + ey) * uw).sum()               # E (sig - y)^2
    Ez = (d1 * (p - ey) * z * uw).sum()                          # E sig'(sig - y) zhat
    Ex = (d1 * (p * mu - eyx) * uw).sum()                        # E sig'(sig - y) x1
    Sa = s * a; qq = (a * Sa).sum()                              # Sig a, |a|_Sig^2 (= q^2)
    # H^{-1} a by Sherman-Morrison on Vh Sig + gam (Sig a)(Sig a)'
    Hinv_a = a / (Vh * s) - (gam * (Sa * (a / (Vh * s))).sum() / (1 + gam * (Sa * (Sa / (Vh * s))).sum())) * (Sa / (Vh * s))
    czz, czx = (Hinv_a * Sa).sum(), (Hinv_a * mt).sum()          # cov(zeta, zhat), cov(zeta, x1)
    b1, b2 = np.linalg.solve(np.array([[q * q, c], [c, 1.0]]), np.array([czz, czx]))
    Erz = b1 * Ez + b2 * Ex                                      # E rho'' rho' zeta
    den = (a * Hinv_a).sum(); ms = (1 / s).mean()
    k = psi * (2 * Erz / Vh + ms * Erp2 / Vh ** 2) / den
    k0 = psi * (ms * Erp2 / Vh ** 2) / den
    print(f"beta {beta} psi {psi} lam0 {lam0:g}: q0 {q:.5f} Vh {Vh:.5f} gam {gam:+.5f} E rho'^2 {Erp2:.5f} "
          f"E rho''rho'zeta {Erz:+.5f} mean(1/s) {ms:.4f} a'H^-1 a {den:.4f} (spike-free {(a * a / (Vh * s)).sum():.4f})  "
          f"k_risk predicted {k:.5f}  (variance term alone {k0:.5f})")
