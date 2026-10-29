# T354 audit (agent A, 20 Oct 2026): exact iid limit point x* for Adam with eps > 0, independent of next_order_eps.py.
# 1/(sqrt(v)+eps) = int_0^inf k(u) e^(-uv) du, k(u) = (pi u)^(-1/2) [1 - eps sqrt(pi u) erfcx(eps sqrt u)] (derived by hand in the audit).
# Integrated in t = log u by the trapezoid rule (not Gauss-Legendre in sqrt u); the lag product is summed lag by lag until the
# exponent a = u d beta2^j gmax falls below 1e-5, then the rest by cumulants to order 4 in closed form.
# m = (1-b1) sum_i b1^i g_i; E[g_i e^(-uv)] = E[g e^(-u c_i g^2)] / E[e^(-u c_i g^2)] * prod_j E[e^(-u c_j g^2)], c_j = d b2^j.
# Argv: eps beta2 beta1 [h]; env BVEC.
import sys, os, math, numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx
eps = float(sys.argv[1]); b2 = float(sys.argv[2]); b1 = float(sys.argv[3]); h = float(sys.argv[4]) if len(sys.argv) > 4 else 0.02
B = np.array([float(t) for t in os.environ.get("BVEC", "9" + ",-1" * 9).split(",")]); P = np.full(len(B), 1 / len(B))
d = 1 - b2; B2 = P @ B**2; B3 = P @ B**3; K = (1 - b1) / (1 - b1 * b2); s0 = math.sqrt(B2); r = s0 / (s0 + eps)
x0 = r * d * K * B3 / (2 * B2)
t = np.arange(-45.0, 6.0 + h / 2, h); u = np.exp(t)
k = (np.pi * u) ** -0.5 * (1 - eps * np.sqrt(np.pi * u) * erfcx(eps * np.sqrt(u)))
wt = h * u * k                                            # du = u dt
I = 0 if b1 == 0 else int(math.ceil(math.log(1e-14) / math.log(b1)))
def D(x):
    g = x + B; g2 = g * g; gmax = g2.max()
    mom = [P @ g2**q for q in range(1, 5)]
    k1 = mom[0]; k2 = mom[1] - mom[0]**2; k3 = mom[2] - 3*mom[1]*mom[0] + 2*mom[0]**3
    k4 = mom[3] - 4*mom[2]*mom[0] - 3*mom[1]**2 + 12*mom[1]*mom[0]**2 - 6*mom[0]**4
    logM = np.zeros_like(u)
    for n, un in enumerate(u):
        a0 = un * d
        J = 0 if a0 * gmax < 1e-5 else int(math.ceil(math.log(1e-5 / (a0 * gmax)) / math.log(b2)))
        if J:
            aj = a0 * b2 ** np.arange(J)
            logM[n] = np.log(np.exp(-np.outer(aj, g2)) @ P).sum()
        aJ = a0 * b2 ** J
        logM[n] += -k1*aJ/(1-b2) + k2*aJ**2/2/(1-b2**2) - k3*aJ**3/6/(1-b2**3) + k4*aJ**4/24/(1-b2**4)
    base = np.exp(logM)
    tot = 0.0
    for i in range(I + 1):
        E = np.exp(-np.outer(u * d * b2**i, g2))
        tot += (1 - b1) * b1**i * (wt * base * (E @ (P * g)) / (E @ P)).sum()
    return tot
xs = brentq(D, 0.3 * x0, 3 * x0, xtol=1e-15 * x0)
print("eps %s beta2 %s beta1 %s h %s: exact x*/x0 = %.9f  (x*/x0-1)/d %.5f" % (sys.argv[1], sys.argv[2], sys.argv[3], h, xs / x0, (xs / x0 - 1) / d))
