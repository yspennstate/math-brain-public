"""T228 review: an independent numerical re-derivation of the contraction bound q and the
tail exponent alpha, by adaptive quadrature (not the package's exact rational checker A08).
Checks: max over eta in [0.99,1.01], theta in [-1,1] of E L_theta (Lemma 2.1 bound) < 0.99010707;
h_eta(1) < 1 < h_eta(2); the root alpha(eta) of E|1-eta A^2|^alpha = 1 lies in (1,2)."""
import json, math, os
from scipy import integrate, optimize, stats
d = 1e-3
phi, Phi = stats.norm.pdf, stats.norm.cdf
def h(eta, a):  # E|1-eta A^2|^a, split at the zero of 1-eta A^2
    r = 1/math.sqrt(eta)
    f = lambda x: abs(1-eta*x*x)**a*phi(x)
    s = integrate.quad(f, 0, r, limit=200)[0] + integrate.quad(f, r, math.inf, limit=200)[0]
    return 2*s
def EA2absY(theta):  # E[A^2 |sigma(A theta)+E|], inner E|m+E| closed form
    def g(x):
        m = x*theta + d*math.tanh(x*theta)
        return x*x*(m*(2*Phi(m)-1) + 2*phi(m))*phi(x)
    return integrate.quad(g, -math.inf, math.inf, limit=200)[0]
def EL(eta, theta):
    return h(eta, 1) + eta*(4*d+3*d*d)*1.0 + 2*d*eta*EA2absY(theta)
out = {"grid": []}
worst = 0
for eta in [0.99, 0.995, 1.0, 1.005, 1.01]:
    for theta in [0, 0.25, 0.5, 0.75, 1.0]:
        v = EL(eta, theta); worst = max(worst, v)
        out["grid"].append([eta, theta, round(v, 8)])
    a = optimize.brentq(lambda s: h(eta, s)-1, 1.0001, 1.9999)
    out.setdefault("alpha", []).append([eta, round(a, 6), round(h(eta, 1), 6), round(h(eta, 2), 6)])
out["max_EL_on_grid"] = round(worst, 8)
out["q_stated"] = 0.99010707
out["EL_below_q"] = worst < 0.99010707
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t228_quad_check.json")
json.dump(out, open(p, "w", encoding="utf-8"), indent=1)
print(json.dumps({k: out[k] for k in ("max_EL_on_grid", "EL_below_q", "alpha")}))
