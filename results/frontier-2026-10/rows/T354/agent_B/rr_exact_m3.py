# T354: rr_exact_m2.py with momentum beta1 > 0 (agent B, 20 Oct 2026). Same model (m = n/10 specials b = 9, others -1),
# eps >= 0, no bias correction. m_k = (1-b1) sum_i b1^i g_{k-i} = (x - 1) + 10 (1-b1) sum_i b1^i 1[slot at lag i special], so
# E[m e^(-u v)] needs, besides E e^(-uv), the tilted sums E[1_lag e^(-uv)]. Both come from the elementary-symmetric recursion
# carried with a tangent: f_j <- ((i-j)/i) f_j + (j/i) w f_{j-1}, fd_j <- ((i-j)/i) fd_j + (j/i) w (fd_{j-1} + t_i f_{j-1}),
# so fd = sum_i t_i E[1_i prod] for slot weights t_i. An earlier epoch's tilt is again a function of c alone (slot weights
# b1^(n-1-q) and a common factor b1^(p+1+(e-1)n)), tabulated with Phi on the same log-c grid. The current epoch carries the
# tangent through its nested lag pass with weights b1^lag. Argv: n beta1 beta2 [eps] [h]. n a multiple of 10.
import sys, math, numpy as np
from scipy.optimize import brentq
from scipy.special import erfcx, gammaln
from scipy.interpolate import CubicSpline
from kclosed import K_closed
n = int(sys.argv[1]); b1 = float(sys.argv[2]); b2 = float(sys.argv[3])
eps = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
h = float(sys.argv[5]) if len(sys.argv) > 5 else 0.02
assert n % 10 == 0; m = n // 10; d = 1 - b2
t = np.arange(-45.0, math.log(60.0) + h / 2, h); u = np.exp(t)
k = (np.pi * u) ** -0.5 * (1 - eps * np.sqrt(np.pi * u) * erfcx(eps * np.sqrt(u))); wt = h * u * k
r = b2 ** (-np.arange(n, dtype=float)); mu = r.mean(); var_sub = m * (n - m) / (n - 1) * r.var(); rmax = r.max()
tq = b1 ** (n - 1 - np.arange(n, dtype=float))            # earlier-epoch slot weights (slot q has lag p + e n - q)
def esym_step(f, fd, i, w, ti):
    j = np.arange(1, f.shape[0])[:, None]
    fd[1:] = ((i - j) / i) * fd[1:] + (j / i) * w * (fd[:-1] + ti * f[:-1])
    f[1:] = ((i - j) / i) * f[1:] + (j / i) * w * f[:-1]
def lnC(a, b): return gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)
A_hi = d * ((9 + 1.0) ** 2 - (-1 + 1.0) ** 2) * 1.5
lc_lo = math.log(1e-9 / rmax); lc_hi = math.log(u.max() * A_hi) + 0.5; dl = 0.002
lc = np.arange(lc_lo, lc_hi + dl, dl); c = np.exp(lc)
f = np.zeros((m + 1, lc.size)); f[0] = 1.0; fd = np.zeros_like(f)
for i in range(1, n + 1): esym_step(f, fd, i, np.exp(-c * r[i - 1]), tq[i - 1])
logPhi = CubicSpline(lc, np.log(np.maximum(f[m], 1e-300)))
ratio = CubicSpline(lc, fd[m] / np.maximum(f[m], 1e-300))   # tilt / Phi
ratio0 = (m / n) * tq.sum()                                # its c -> 0 limit
lc_phi = math.log(1e-4 / rmax)
def logPhi_at(cc):
    out = -cc * m * mu + 0.5 * cc * cc * var_sub
    big = cc >= math.exp(lc_phi)
    out[big] = logPhi(np.log(cc[big]))
    return out
def ratio_at(cc):
    out = np.full_like(cc, ratio0)
    big = cc >= c[0]
    out[big] = ratio(np.log(cc[big]))
    return out
P_past = {}
for jj in (m - 1, m):
    W = np.zeros((n, m + 1))
    for p in range(n):
        for kk in range(0, min(p, jj) + 1):
            if jj - kk <= n - 1 - p:
                W[p, kk] = math.exp(lnC(p, kk) + lnC(n - 1 - p, jj - kk) - lnC(n - 1, jj))
    P_past[jj] = W
def D(x):
    gs, go = 9 + x, -1 + x; A = d * (gs * gs - go * go); uA = u * A; tot = 0.0
    fc = np.zeros((m + 1, u.size)); fc[0] = 1.0; fdc = np.zeros_like(fc)
    for p in range(n):
        if p >= 1: esym_step(fc, fdc, p, np.exp(-uA * b2 ** p), b1 ** p)
        cur_s = P_past[m - 1][p] @ fc; cur_o = P_past[m][p] @ fc
        til_s = P_past[m - 1][p] @ fdc; til_o = P_past[m][p] @ fdc
        logP = np.zeros_like(u); tf = np.zeros_like(u); e = 1
        while True:
            cc = uA * b2 ** (p + e * n); wgt = b1 ** (p + 1 + (e - 1) * n)
            if cc.max() * rmax < 1e-4 and wgt < 1e-17: break
            logP += logPhi_at(cc); tf += wgt * ratio_at(cc); e += 1
        base = b2 ** (p + e * n)
        logP += -uA * m * mu * base / (1 - b2 ** n) + 0.5 * uA ** 2 * var_sub * base ** 2 / (1 - b2 ** (2 * n))
        tf += ratio0 * b1 ** (p + 1 + (e - 1) * n) / (1 - b1 ** n)
        common = wt * np.exp(-u * go * go + logP)
        ms = (x - 1) * cur_s + 10 * (1 - b1) * (cur_s + til_s + cur_s * tf)
        mo = (x - 1) * cur_o + 10 * (1 - b1) * (til_o + cur_o * tf)
        tot += 0.1 * (common * np.exp(-uA) * ms).sum() + 0.9 * (common * mo).sum()
    return tot / n
K = K_closed(n, b1, b2); rr = 3 / (3 + eps); x0 = rr * d * K * 72 / 18
xs = brentq(D, 0.3 * x0, 3 * x0, xtol=1e-13 * x0)
print("RRm3 n %d m %d beta1 %s beta2 %s eps %g h %g n(1-b2) %.3f K %.8f x0 %.8g exact x* %.12g x*/x0 %.9f (x*/x0-1)/d %.5f"
      % (n, m, sys.argv[2], sys.argv[3], eps, h, n * d, K, x0, xs, xs / x0, (xs / x0 - 1) / d), flush=True)
