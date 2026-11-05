"""T357 review, check 3 (agent H): Thm C sign by 1-D adaptive quadrature.

check2's 2-D Gauss-Hermite OC was wrong (the indicator S>=0 is not smooth; |OC| came out above CE,
which is impossible). Here, with U = k Z + tau G ~ N(0, sd^2) and g(u) = P(Y=1 | U=u):
  OC(c) = 2 int_0^inf (sigma(c u) - g(u)) phi_sd(u) du,   CE(c) = 2 int_0^inf |sigma(c u) - g(u)| phi_sd(u) du,
  R'(c) = 2 int_0^inf u (sigma(c u) - g(u)) phi_sd(u) du  (zero at c_*).
Point: beta = 1, alpha = 2, gamma = 1 (k, tau2 from check2). Output t357_check3.json.
"""
import json, math, os
from scipy import integrate, optimize

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t357_check3.json")
prev = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "t357_check2.json")))
P = prev["thmC_beta1_alpha2_gamma1"]
beta, k, tau2 = 1.0, P["k"], P["tau2"]
sd2 = k * k + tau2; sd = math.sqrt(sd2)
sig = lambda x: 1 / (1 + math.exp(-x)) if x > -700 else 0.0
phi = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
s = math.sqrt(tau2 / sd2)


def g(u):
    m = k * u / sd2
    return integrate.quad(lambda x: sig(beta * (m + s * x)) * phi(x), -12, 12, epsabs=1e-14, limit=200)[0]


def I(f):
    return 2 * integrate.quad(lambda u: f(u) * phi(u / sd) / sd, 0, 12 * sd, epsabs=1e-14, limit=400)[0]


Rp = lambda c: I(lambda u: u * (sig(c * u) - g(u)))
cs = optimize.brentq(Rp, 0.1, 10, xtol=1e-12)
out = {"beta": beta, "k": k, "tau2": tau2, "c_star": cs, "c_star_check2": P["c_star"],
       "upper_bracket_m": beta * k / sd2, "lower_bracket_4gprime0": 4 * (g(1e-4) - g(-1e-4)) / 2e-4}
for lab, c in (("0.5c*", 0.5 * cs), ("c*", cs), ("2c*", 2 * cs)):
    out[lab] = {"c": c, "OC": I(lambda u: sig(c * u) - g(u)), "CE": I(lambda u: abs(sig(c * u) - g(u)))}
# crossing point u* of e(u) = sigma(c* u) - g(u)
try:
    out["u_star_over_sd"] = optimize.brentq(lambda u: sig(cs * u) - g(u), 0.01 * sd, 12 * sd) / sd
except ValueError as e:
    out["u_star_over_sd"] = str(e)
json.dump(out, open(OUT, "w"), indent=1)
print(json.dumps(out, indent=1))
