"""Second audit of agent_B/NOTE.md "Every n" (agent A, 20 Oct 2026). Monte Carlo, not the elementary-symmetric route.

Model as in the NOTE: n samples per epoch, m = n/10 with b = 9, the rest b = -1, g = x + b, beta1 = 0, eps = 0, frozen x,
v_k = d sum_j beta2^j g_{k-j}^2 (d = 1 - beta2), drift D(x) = E[g_k / sqrt(v_k)] with k uniform over epoch positions.

Control variate. With V = mean g^2 (a constant), g/sqrt(v) = g/sqrt(V) - g (v - V)/(2 V^1.5) + Y, and the mean of the first two terms is
exact: E[g v] = d [ mean g^3 + (beta2/d) gbar hbar + sum_{j=1}^{n-1} beta2^j (n-j)/n (Ein - gbar hbar) ], h = g^2, where a lag j inside
the current epoch (probability (n-j)/n) pairs two distinct slots of one permutation, Ein = (n^2 gbar hbar - n mean(g h))/(n(n-1)), and a lag
in an earlier epoch is independent of g_k. Only Y = O(eta^2) is simulated. The root of D is found from three x near x0 with common
random numbers. Chains are independent; the error bar is the spread of per-chain means.

usage: python rrm_mc_cv.py N BETA2 CHAINS MEASURE_EPOCHS [SEED]
"""
import math
import sys

import numpy as np

n = int(sys.argv[1]); b2 = float(sys.argv[2]); C = int(sys.argv[3]); ME = int(sys.argv[4])
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
assert n % 10 == 0
m = n // 10; d = 1.0 - b2
b = np.array([9.0] * m + [-1.0] * (n - m))
B2 = np.mean(b ** 2); B3 = np.mean(b ** 3)

# K at beta1 = 0 from my own lag sum (same-epoch pair: -1/(n-1) of C; earlier epochs: 0)
j = np.arange(1, n)
# E[g eta] V = d [C + sum_{j=1}^{n-1} b2^j (n-j)/n (-C/(n-1))]  =>  K = 1 - sum_j b2^j (n-j) / (n (n-1))
K = 1.0 - np.sum(b2 ** j * (n - j)) / (n * (n - 1))
x0 = d * K * B3 / (2 * B2)


def Dlin(x):
    g = x + b; h = g * g
    gb = g.mean(); hb = h.mean(); V = hb
    Ein = (n * n * gb * hb - n * np.mean(g * h)) / (n * (n - 1))
    Egv = d * (np.mean(g ** 3) + (b2 / d) * gb * hb + np.sum(b2 ** j * (n - j) / n) * (Ein - gb * hb))
    return gb / math.sqrt(V) - (Egv - gb * V) / (2 * V ** 1.5), V


xs = x0 * np.array([0.97, 1.0, 1.03]) + x0 * d * 0.3
nx = xs.size
Vs = np.array([Dlin(x)[1] for x in xs])
rng = np.random.default_rng(seed)
burn_ep = int(math.ceil(35.0 / d / n)) + 1
v = np.tile(Vs[:, None], (1, C))           # (nx, C)
acc = np.zeros((nx, C))
for ep in range(burn_ep + ME):
    S = np.argsort(rng.random((C, n)), axis=1) < m   # uniform m-subset per chain
    bb = np.where(S, 9.0, -1.0)                       # (C, n)
    for p in range(n):
        g = xs[:, None] + bb[None, :, p]              # (nx, C)
        v = b2 * v + d * g * g
        if ep >= burn_ep:
            sV = np.sqrt(Vs)[:, None]
            acc += g / np.sqrt(v) - g / sV + g * (v - Vs[:, None]) / (2 * sV ** 3)
Ymean = acc / (ME * n)                                # per chain
R = Ymean.mean(axis=1); Rse = Ymean.std(axis=1, ddof=1) / math.sqrt(C)
D = np.array([Dlin(x)[0] for x in xs]) + R
# root: quadratic through the three points (common random numbers keep R's errors correlated across xs)
coef = np.polyfit(xs, D, 2); rts = np.roots(coef); xr = float(np.real(rts[np.argmin(abs(rts - xs[1]))]))
# error: shift D by +-Rse at the middle point (the errors are strongly correlated across xs)
slope = 2 * coef[0] * xr + coef[1]; xerr = Rse[1] / abs(slope)
c = (xr / x0 - 1) / d; cerr = xerr / x0 / d
print("MCcv n %d m %d beta2 %s n(1-b2) %.3f K %.8f x0 %.8g | C %d epochs %d burn %d | R %s +- %s | x* %.10g +- %.2g | (x*/x0-1)/d %.4f +- %.4f"
      % (n, m, sys.argv[2], n * d, K, x0, C, ME, burn_ep, np.array2string(R, precision=3), np.array2string(Rse, precision=2),
         xr, xerr, c, cerr), flush=True)
