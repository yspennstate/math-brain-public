"""T357 (agent A, 20 Oct 2026): check of the identity FM_inf(lam) = -lam |a_lam|^2 on the n = inf ridge path of
rf_ridge_inf.py (same F, same Gaussian-equivalence model). Proof: the population ridge objective A(q) - kappa a.m + lam|a|^2/2,
q = |a|_Sig, is stationary where A'(q) Sig a / q - kappa m + lam a = 0; dotting with a gives q A'(q) - kappa c = -lam |a|^2,
and FM = E[(sig(zhat) - y) zhat] = q A'(q) - kappa c (E sig(q u) q u = q A'(q); E y zhat = kappa c by Stein). The same
computation on the empirical objective gives train FM = -lam |w_hat|^2 exactly at every n.
argv: beta psi [d] [seed]"""
import sys, math, runpy
src = open(__file__.replace("fm_identity_check.py", "rf_ridge_inf.py"), encoding="utf-8").read()
src = src[:src.index("q0, c0, R0 = fit(1e-12)")]                  # model, F and fit() only
src = src.replace("q = 0.5 * (lo + hi); a = h(q)[1]; c = (a * mt).sum(); return q, c, A(q) - kap * c",
                  "q = 0.5 * (lo + hi); a = h(q)[1]; c = (a * mt).sum(); return q, c, A(q) - kap * c, a")
g = {"__name__": "rf_ridge_inf_body"}; exec(compile(src, "rf_ridge_inf.py", "exec"), g)
print(__doc__)
for lam in (1e-5, 1e-4, 1.677e-4, 1e-3, 1e-2, 1e-1):
    q, c, R, a = g["fit"](lam); oc, fm = g["oc_fm"](q, c)
    print(f"  lam {lam:9.4g}  FM {fm:+.6e}  -lam|a|^2 {-lam * (a * a).sum():+.6e}  rel diff {(fm + lam * (a * a).sum()) / abs(fm):+.1e}  OC {oc:+.5f}")
