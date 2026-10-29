# Second audit of agent B's RR momentum and eps > 0 lemmas (T354; remainder_rr_mom.py, remainder_rr_eps.py, push 9bf2f37b).
# agent A, 20 Oct 2026. Exact x* under random reshuffling on the test model g_i = x + b_i, b = (9, -1 x 9), n = 10, with
# momentum and eps, no Taylor step. Only the slot of the special sample in each epoch matters. With the current step at position p,
# the special at q_e in epoch e (e = 0 current, uniform and independent across epochs), lag_0 = p - q_0 (past only if q_0 <= p),
# lag_e = p + e n - q_e:
#   v = g_o^2 + A sum_e b2^lag_e [past],  A = (1 - b2)(g_s^2 - g_o^2);   m = g_o + (g_s - g_o)(1 - b1) sum_e b1^lag_e [past].
# 1/(sqrt v + eps) = int k(u) e^(-uv) du, k(u) = (pi u)^(-1/2) [1 - eps sqrt(pi u) erfcx(eps sqrt u)]. Given u the epochs factorize:
#   E[m e^(-uv)] = e^(-u g_o^2) prod_e F_e(u) [g_o + (g_s - g_o)(1 - b1) sum_e G_e(u)/F_e(u)],
#   F_e = E_q e^(-u A b2^lag_e(q) [past]),  G_e = E_q b1^lag_e(q) [past] e^(-u A b2^lag_e(q)).
# Epochs are exact while the momentum weight is above 1e-17 or u A b2^lag (r_max - r_min) > 1e-3 at the largest u; the rest of
# log prod F by cumulants of r_q = b2^(-q) to order 4, summed in closed form. Trapezoid in t = log u on [-45, log 60].
# D(x) = sum_p int k E[m e^(-uv)] du; x* its root. Argv: beta1 beta2 eps [h].
import sys, math, numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx
b1, b2, eps = (float(a) for a in sys.argv[1:4]); h = float(sys.argv[4]) if len(sys.argv) > 4 else 0.02
n = 10; d = 1 - b2
t = np.arange(-45.0, math.log(60.0) + h / 2, h); u = np.exp(t)
k = (np.pi * u) ** -0.5 * (1 - eps * np.sqrt(np.pi * u) * erfcx(eps * np.sqrt(u))); wt = h * u * k
q = np.arange(n); r = b2 ** (-q.astype(float)); spread = r.max() - r.min()
mom = [np.mean(r ** j) for j in range(1, 5)]
kap = [mom[0], mom[1] - mom[0] ** 2, mom[2] - 3 * mom[1] * mom[0] + 2 * mom[0] ** 3,
       mom[3] - 4 * mom[2] * mom[0] - 3 * mom[1] ** 2 + 12 * mom[1] * mom[0] ** 2 - 6 * mom[0] ** 4]
def D(x):
    gs, go = 9 + x, -1 + x; A = d * (gs * gs - go * go); tot = 0.0
    for p in range(n):
        past = q <= p; lag0 = np.where(past, p - q, 0)
        E0 = np.exp(-np.outer(u * A, np.where(past, b2 ** lag0, 0.0)))
        logF = np.log(E0.mean(1)); GF = (E0 @ np.where(past, b1 ** lag0, 0.0) / n) / E0.mean(1)
        e = 1
        while True:
            base = b2 ** (p + e * n); mw = b1 ** (p + e * n - (n - 1)) if b1 > 0 else 0.0
            if mw < 1e-17 and u.max() * A * base * spread <= 1e-3: break
            lag = p + e * n - q
            E = np.exp(-np.outer(u * A, b2 ** lag.astype(float)))
            Fm = E.mean(1); logF += np.log(Fm)
            if mw >= 1e-17: GF += (E @ (b1 ** lag.astype(float)) / n) / Fm
            e += 1
        for j in range(1, 5):     # sum over e' >= e of (-a_e' )^j kappa_j / j!, a_e' = u A b2^(p + e' n)
            geo = (A * b2 ** (p + e * n)) ** j / (1 - b2 ** (j * n))
            logF += (-1) ** j * kap[j - 1] * (u ** j) * geo / math.factorial(j)
        integ = np.exp(-u * go * go + logF) * (go + (gs - go) * (1 - b1) * GF)
        tot += wt @ integ
    return tot / n
import os
if os.environ.get("EVALX"):
    for xv in os.environ["EVALX"].split(","): print("D(%s) = %.6e" % (xv, D(float(xv))))
    sys.exit()
sys.path.insert(0, "../agent_B"); from kfactor import K_rr
K = K_rr(n, b1, b2); x0 = d * K * 72 / 18 * 3 / (3 + eps)
xs = brentq(D, 0.05 * x0, 5 * x0, xtol=1e-12 * x0)
print("RR beta1 %s beta2 %s eps %s h %s: K %.6f x0 %.6g exact x* %.10g = x0 * %.6f   (D(0.5x0) %.3e, D(2x0) %.3e)"
      % (sys.argv[1], sys.argv[2], sys.argv[3], h, K, x0, xs, xs / x0, D(0.5 * x0), D(2 * x0)), flush=True)
