# Audit of agent B's remainder_rr.py (T354): exact x* under random reshuffling, beta1 = 0, eps = 0, no Taylor step.
# Model g_i = x + b_i, b = (9, -1 x 9): only the position of the special sample in each epoch matters. With the current sample at
# position p of its epoch, the special at q_0 there and at q_m in the m-th earlier epoch (all uniform on 0..n-1, independent):
#   v = g_o^2 + d (g_s^2 - g_o^2) [ beta^(p - q_0) 1{q_0 <= p} + sum_{m >= 1} beta^(p + m n - q_m) ],   g = g_s if q_0 = p else g_o.
# v^(-1/2) = (2/sqrt pi) int_0^inf e^(-w^2 v) dw; the earlier epochs factorize; epochs with a beta^L < 1e-3 are summed in closed
# form through the cumulants of beta^(-q) to order 4. D(x) = E[g v^(-1/2)], x* its root. Argv: beta2 [nodes].
import sys, math, numpy as np
from scipy.optimize import brentq
b2 = float(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 300; d = 1 - b2; n = 10
wn, ww = np.polynomial.legendre.leggauss(N); W = 7.0; w = (wn + 1) * W / 2; ww = ww * W / 2; s = w * w
q = np.arange(n); r = b2 ** (-q.astype(float))
mom = [np.mean(r ** k) for k in range(1, 5)]
kap = [mom[0], mom[1] - mom[0] ** 2, mom[2] - 3 * mom[1] * mom[0] + 2 * mom[0] ** 3,
       mom[3] - 4 * mom[2] * mom[0] - 3 * mom[1] ** 2 + 12 * mom[1] * mom[0] ** 2 - 6 * mom[0] ** 4]
def D(x):
    gs, go = 9 + x, -1 + x; A = d * (gs * gs - go * go); tot = 0.0
    for p in range(n):
        # earlier epochs: log E exp(-s A beta^(p+mn) r_q), exact while s A beta^(p+mn) r_max > 1e-3
        logE = np.zeros_like(s); m = 1
        while True:
            c = A * b2 ** (p + m * n)
            if (s.max() * c * r.max()) <= 1e-3: break
            logE += np.log(np.mean(np.exp(-np.outer(s * c, r)), axis=1)); m += 1
        for k in range(1, 5):   # sum_{m' >= m} (s c_m')^k kappa_k (-1)^k / k!
            geo = (A * b2 ** (p + m * n)) ** k / (1 - b2 ** (k * n))
            logE += (-1) ** k * kap[k - 1] * (s ** k) * geo / math.factorial(k)
        for q0 in range(n):
            c0 = b2 ** (p - q0) if q0 <= p else 0.0
            g = gs if q0 == p else go
            integ = np.exp(-s * (go * go + A * c0) + logE)
            tot += g * (2 / math.sqrt(math.pi)) * (ww @ integ)
    return tot / (n * n)
x0 = None
from kfactor import K_rr
K = K_rr(n, 0.0, b2); x0 = d * K * 72 / 18
xs = brentq(D, 0.3 * x0, 3 * x0, xtol=1e-13 * x0)
print("RR beta2 %s nodes %d: K %.6f x0 %.6g exact x*/x0 = %.6f   (D(0.5x0) %.3e, D(2x0) %.3e)" % (sys.argv[1], N, K, x0, xs / x0, D(0.5 * x0), D(2 * x0)), flush=True)
