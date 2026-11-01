"""T357 (agent A, 20 Oct 2026): closed form for k_FM = lim alpha lam_FM, from the identity train FM = -lam |w_hat|^2.
At the fixed point of rf_cgmt.py a training prediction is P = prox_{c rho_y}(Q) = Q - c rho'(P), while a fresh prediction has
the law of Q. With g(z, y) = (sig(z) - y) z, the population FM is E g(Q) and the train FM is E g(P), so
    gap = E g(Q) - E g(P) = c E[g'(Q) rho'(Q)] + O(c^2),   g'(z) rho'(z) = (sig'(z) z + sig(z) - y)(sig(z) - y),
and c = (1/n) tr Sig G -> N/(n Vh) = psi/(alpha Vh) as lam -> 0 (Sig full rank), Vh = E sig'(zhat). At lam_FM, FM_pop = 0, so
    lam_FM |w_hat|^2 = gap   =>   k_FM = alpha lam_FM -> psi E[(sig' zhat + sig - y)(sig - y)] / (Vh |a_0|^2),
every expectation at the n = inf population fit (lam -> 0+, zhat = q0 u, y | u from the teacher). Compared with the alpha
sweep's alpha lam_FM (0.095 at beta 2, 0.034 at beta 5, d 1000, N/d 1, F seed 100). argv: beta psi [d] [seed]"""
import sys, math
src = open(__file__.replace("fm_gap_coefficient.py", "rf_ridge_inf.py"), encoding="utf-8").read()
src = src[:src.index("q0, c0, R0 = fit(1e-12)")]
src = src.replace("q = 0.5 * (lo + hi); a = h(q)[1]; c = (a * mt).sum(); return q, c, A(q) - kap * c",
                  "q = 0.5 * (lo + hi); a = h(q)[1]; c = (a * mt).sum(); return q, c, A(q) - kap * c, a")
g = {"__name__": "rf_ridge_inf_body"}; exec(compile(src, "rf_ridge_inf.py", "exec"), g)
np, sig, hx, hw, ux, uw, beta, psi = g["np"], g["sig"], g["hx"], g["hw"], g["ux"], g["uw"], g["beta"], g["psi"]
print(__doc__)
for lam0 in (1e-8, 1e-6):
    q, c, R, a = g["fit"](lam0)
    mu = (c / q) * ux; sd = math.sqrt(max(1 - c ** 2 / q ** 2, 0))
    ey = (sig(beta * (mu[:, None] + sd * hx[None, :])) * hw[None, :]).sum(1)      # P(y = 1 | zhat = q u)
    z = q * ux; p = sig(z); d1 = p * (1 - p)
    Vh = (d1 * uw).sum()
    # E[(d1 z + p - y)(p - y)] with y ~ Bernoulli(ey): E[(B - y)(p - y)] = B p - (B + p) ey + ey, B = d1 z + p
    B = d1 * z + p; T = ((B * p - (B + p) * ey + ey) * uw).sum()
    a2 = (a * a).sum()
    print(f"beta {beta} psi {psi} lam0 {lam0:g}: q0 {q:.5f}  Vh {Vh:.5f}  E[g'rho'] {T:.6f}  |a0|^2 {a2:.5f}  "
          f"k_FM predicted {psi * T / (Vh * a2):.5f}")
