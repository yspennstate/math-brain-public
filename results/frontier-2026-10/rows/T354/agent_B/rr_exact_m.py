# T354 exact limit point under random reshuffling for a FIXED noise distribution at any n (agent B, 20 Oct 2026).
# Model: g_i = x + b_i, m = n/10 "special" samples b_s = 9 and n - m ordinary b_o = -1 (E b = 0, B2 = 9, B3 = 72 for every n),
# beta1 = 0, eps >= 0, bias correction off (stationary). With the current step at slot p of its epoch,
#   v = g_o^2 + A sum_{special slots in the past, lag 0 included} beta2^lag,   A = (1 - beta2)(g_s^2 - g_o^2),
# and 1/(sqrt v + eps) = int k(u) e^(-u v) du as in audit_A/rr_exact_mom_eps.py. The special slots of each epoch are a
# uniform random m-subset, independent across epochs, so E e^(-u v) factorizes over epochs and each factor is the normalized
# elementary symmetric mean of w_q = exp(-u A beta2^lag_q) over the subset, computed by the stable recursion
#   f_j(i) = ((i - j)/i) f_j(i-1) + (j/i) w_i f_{j-1}(i-1)          (f_j(i) = e_j(w_1..w_i) / C(i, j)).
# In the current epoch the n - 1 slots other than p hold m - 1 specials (current special) or m (current ordinary). Far epochs,
# once u A beta2^lag_min < 1e-4 at the largest u, are summed in closed form by the first two cumulants of the subset sum.
# Argv: n beta2 [eps] [h]. Prints x*, x0 = r d K B3/(2 B2) with K the closed form (kclosed.py), and (x*/x0 - 1)/d.
import sys, math, numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx
from kclosed import K_closed
n = int(sys.argv[1]); b2 = float(sys.argv[2]); eps = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
h = float(sys.argv[4]) if len(sys.argv) > 4 else 0.02
assert n % 10 == 0; m = n // 10; d = 1 - b2
t = np.arange(-45.0, math.log(60.0) + h / 2, h); u = np.exp(t)
k = (np.pi * u) ** -0.5 * (1 - eps * np.sqrt(np.pi * u) * erfcx(eps * np.sqrt(u))); wt = h * u * k
r = b2 ** (-np.arange(n, dtype=float)); mu = r.mean(); s2 = r.var()
var_sub = m * (n - m) / (n - 1) * s2                     # variance of a without-replacement m-subset sum of r
def esym(W, top):
    # W: (slots, len(u)); returns f_0..f_top after all slots (normalized elementary symmetric means)
    f = np.zeros((top + 1, W.shape[1])); f[0] = 1.0
    for i in range(1, W.shape[0] + 1):
        w = W[i - 1]
        for j in range(min(i, top), 0, -1):
            f[j] = ((i - j) / i) * f[j] + (j / i) * w * f[j - 1]
    return f
def D(x):
    gs, go = 9 + x, -1 + x; A = d * (gs * gs - go * go); tot = 0.0
    for p in range(n):
        q = np.array([s for s in range(n) if s != p])
        lag = np.where(q < p, p - q, -1)
        W = np.where(lag[:, None] >= 0, np.exp(-np.outer(b2 ** np.maximum(lag, 0).astype(float), u * A)), 1.0)
        f = esym(W, m); cur_s = f[m - 1]; cur_o = f[m]
        logP = np.zeros_like(u); e = 1
        while True:
            lmin = p + e * n - (n - 1)
            if u.max() * A * b2 ** lmin < 1e-4: break
            lagq = (p + e * n - np.arange(n)).astype(float)
            fe = esym(np.exp(-np.outer(b2 ** lagq, u * A)), m)[m]
            logP += np.log(fe); e += 1
        base = b2 ** (p + e * n)                         # remaining epochs e' >= e: sum_q in subset b2^(p + e'n) r_q
        logP += -u * A * m * mu * base / (1 - b2 ** n) + 0.5 * (u * A) ** 2 * var_sub * base ** 2 / (1 - b2 ** (2 * n))
        common = wt * np.exp(-u * go * go + logP)
        tot += 0.1 * gs * (common * np.exp(-u * A) * cur_s).sum() + 0.9 * go * (common * cur_o).sum()
    return tot / n
K = K_closed(n, 0.0, b2); rr = 3 / (3 + eps); x0 = rr * d * K * 72 / 18
xs = brentq(D, 0.3 * x0, 3 * x0, xtol=1e-13 * x0)
print("RRm n %d m %d beta2 %s eps %g h %g n(1-b2) %.3f K %.8f x0 %.8g exact x* %.12g x*/x0 %.9f (x*/x0-1)/d %.5f"
      % (n, m, sys.argv[2], eps, h, n * d, K, x0, xs, xs / x0, (xs / x0 - 1) / d), flush=True)
