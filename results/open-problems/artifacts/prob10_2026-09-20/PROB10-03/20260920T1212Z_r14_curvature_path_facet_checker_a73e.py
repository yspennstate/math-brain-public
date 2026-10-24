"""PROB10-03 / R14 self-checker.

Exact/symbolic checks:
  * matched-Gaussian Fisher rewrite;
  * two-point curvature-variability identity;
  * thermodynamic KL derivative;
  * explicit negation of a monotone-variance shortcut.

Numerical-only scouts:
  * inner hinge curvature-variability cage at three x values;
  * outer tilted-U positive-path identity at V=0;
  * one-facet Gaussian-polytope first-moment exponent.

Nothing numerical in this file is promoted to a source endpoint.
"""

import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import log_ndtr, ndtr, logsumexp, roots_hermitenorm
from numpy.polynomial.legendre import leggauss

# ---------------------------------------------------------------------------
# Exact symbolic checks
# ---------------------------------------------------------------------------

a, delta = sp.symbols("a delta", real=True)
v = 1 - delta
R = a - delta
assert sp.simplify(1 + v * R - delta**2 - v * (1 + a)) == 0
print("EXACT_FISHER_REWRITE_PASS")

A, p = sp.symbols("A p", positive=True)
avg_tau = A * p
E_inv = (1-p) + p/(1+A)
eta_from_BL = sp.simplify((1+avg_tau)*E_inv - 1)
eta_two_point = A**2 * p * (1-p)/(1+A)
assert sp.simplify(eta_from_BL - eta_two_point) == 0
print("EXACT_BERNOULLI_CURVATURE_VARIABILITY_PASS")

t = sp.symbols("t", positive=True)
F = sp.Function("F")
D = t*sp.diff(F(t), t) - F(t)
assert sp.simplify(sp.diff(D, t) - t*sp.diff(F(t), t, 2)) == 0
print("EXACT_THERMODYNAMIC_DERIVATIVE_PASS")

pp = sp.Rational(3,4)
kappa3 = sp.simplify(pp*(1-pp)*(1-2*pp))
dvar_negative_tilt = -kappa3
assert dvar_negative_tilt == sp.Rational(3,32)
print("EXACT_VARIANCE_MONOTONICITY_NEGATION_PASS", dvar_negative_tilt)

# ---------------------------------------------------------------------------
# Numerical-only scouts at the archived third-full candidate parameters.
# ---------------------------------------------------------------------------

p3 = 0.59916661553777206
p2 = 0.96911591246056061
c3 = 2.867401746232769
c2 = 13.103474332343133
gamma_sq = 0.076564602131018136
B = c2/(4*gamma_sq)
m = c3/c2
d = math.sqrt(p2-p3)
s = math.sqrt(1-p2)
A0 = 1 + 2*B*s*s


def logf_closed(x):
    """Exact closed one-step log kernel, evaluated stably."""
    x = np.asarray(x)
    l1 = log_ndtr(-x/s)
    l2 = -0.5*math.log(A0) - B*x*x/A0 + log_ndtr(x/(s*math.sqrt(A0)))
    return np.logaddexp(l1, l2)


def inner_direct(x):
    norm = 1/math.sqrt(2*math.pi)
    kink = -x/s

    def base(h):
        hp = max(x+s*h, 0.0)
        return math.exp(-0.5*h*h-B*hp*hp)*norm

    qopts = dict(epsabs=1e-13, epsrel=1e-12, limit=300)
    Z = quad(base, -12, 12, **qopts)[0]
    mu = quad(lambda h: h*base(h), -12, 12, **qopts)[0]/Z
    e2 = quad(lambda h: h*h*base(h), -12, 12, **qopts)[0]/Z
    ehp2 = quad(lambda h: max(x+s*h,0.0)**2*base(h), -12, 12, **qopts)[0]/Z
    if -12 < kink < 12:
        pos = quad(lambda h: base(h), kink, 12, **qopts)[0]/Z
    elif kink <= -12:
        pos = 1.0
    else:
        pos = 0.0
    vv = e2-mu*mu
    KL = -B*ehp2-math.log(Z)
    return mu, vv, pos, KL


for x in (-1.0, 0.0, 1.0):
    mu, vv, pos, KL = inner_direct(x)
    curv = 2*B*s*s
    eta = curv*curv*pos*(1-pos)/(1+curv)
    DG = 0.5*(mu*mu+vv-1-math.log(vv))
    upper = DG + 0.5*math.log1p(eta)
    assert DG <= KL + 2e-8
    assert KL <= upper + 2e-8
    print("NUMERICAL_ONLY_HINGE_CAGE", x, "DG", DG, "KL", KL, "UPPER", upper,
          "PI", pos, "ETA", eta)

# Positive thermodynamic-path identity for the outer U tilt at V=0.
unodes, uw = roots_hermitenorm(120)
uw = uw/math.sqrt(2*math.pi)
xvals = d*unodes - 1.0
uvals = logf_closed(xvals)


def outer_logZ_stats(tt):
    lv = np.log(uw) + tt*uvals
    L = logsumexp(lv)
    prob = np.exp(lv-L)
    mean = float(np.sum(prob*uvals))
    var = float(np.sum(prob*(uvals-mean)**2))
    return float(L), mean, var


L, mean, _ = outer_logZ_stats(m)
D_direct = m*mean-L
lnodes, lweights = leggauss(48)
ts = 0.5*m*(lnodes+1)
tweights = 0.5*m*lweights
D_path = sum(float(wt)*float(tt)*outer_logZ_stats(float(tt))[2]
             for wt,tt in zip(tweights,ts))
assert abs(D_direct-D_path) < 1e-11
print("NUMERICAL_ONLY_OUTER_PATH_V0", "DIRECT", D_direct, "PATH", D_path,
      "ABS_DIFF", abs(D_direct-D_path))

# Exact one-facet first-moment formula, numerical exponent diagnostic.
def facet_rate(alpha, r=1.0):
    return (alpha*math.log(alpha)-(alpha-1)*math.log(alpha-1)
            -0.5*r*r+(alpha-1)*math.log(ndtr(r)))

facet_root = brentq(lambda aa: facet_rate(aa,1.0), 15.0, 30.0)
current_alpha = 12.31963446
current_rate = facet_rate(current_alpha,1.0)
assert facet_root > current_alpha
assert current_rate > 0
print("NUMERICAL_ONLY_FACET_FIRST_MOMENT_ROOT", facet_root)
print("NUMERICAL_ONLY_FACET_RATE_AT_CURRENT_UPPER", current_rate)

print("ALL_EXACT_SELF_CHECKS_PASS")
print("NUMERICAL_SCOUT_COMPLETE")
