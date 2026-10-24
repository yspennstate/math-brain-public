"""Accurate defect of AND/OR chains.

eps(p) = 4p - A(p) is O(p^2 log(1/p)) as p -> 0, and the naive formula loses it to cancellation.  Here
    eps(p) = 4p^2 + 2p^2 log2(p) + [2(1-p)^2 log1p(-p) - (1-2p)^2 log1p(-2p)]/ln 2      (0 <= p <= 1),
and for p < 1e-3 the bracket is replaced by its Taylor series.
D(t) = 4I(t) - H(t) = sum_k 2^-k eps(2 d(T^k t)),   D_inf(s) = D(s) + 2 sum_{l>=0} 2^l eps(2^-l s).
"""
import sys
import numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p

LN2 = np.log(2.0)


def bracket_series(p, terms=40):
    # 2(1-p)^2 log1p(-p) - (1-2p)^2 log1p(-2p) = sum_k c_k p^k ; computed from the series of log1p
    # log1p(-x) = -sum_{j>=1} x^j / j
    p = np.asarray(p, dtype=np.float64)
    out = np.zeros_like(p)
    # (1-p)^2 = 1 - 2p + p^2 ; (1-2p)^2 = 1 - 4p + 4p^2
    for j in range(1, terms):
        a = -1.0 / j          # coefficient of p^j in log1p(-p)
        b = -(2.0 ** j) / j   # coefficient of p^j in log1p(-2p)
        # 2(1 - 2p + p^2) * a p^j - (1 - 4p + 4p^2) * b p^j
        out += (2 * a - b) * p ** j + (-4 * a + 4 * b) * p ** (j + 1) + (2 * a - 4 * b) * p ** (j + 2)
    return out


def eps(p):
    p = np.asarray(p, dtype=np.float64)
    out = np.empty_like(p)
    small = p < 1e-3
    ps = p[small]
    with np.errstate(divide="ignore", invalid="ignore"):
        lp = np.where(ps > 0, np.log2(np.where(ps > 0, ps, 1.0)), 0.0)
    out[small] = 4 * ps ** 2 + 2 * ps ** 2 * lp + bracket_series(ps) / LN2
    pb = p[~small]
    q = np.abs(1 - 2 * pb)
    with np.errstate(divide="ignore", invalid="ignore"):
        lq = np.where(pb < 0.5, np.log1p(-2 * np.minimum(pb, 0.5)), np.log(np.where(q > 0, q, 1.0)))
        l1 = np.where(pb < 1, np.log1p(-np.minimum(pb, 1 - 1e-17)), 0.0)
    br = 2 * (1 - pb) ** 2 * l1 - q ** 2 * np.where(q > 0, lq, 0.0)
    out[~small] = 4 * pb ** 2 + 2 * pb ** 2 * np.log2(pb) + br / LN2
    return out


def eps_mp(p):
    p = mpf(p)
    if p == 0:
        return mpf(0)
    br = 2 * (1 - p) ** 2 * mlog1p(-p) if p < 1 else mpf(0)
    q = abs(1 - 2 * p)
    if q != 0:
        br -= q ** 2 * (mlog1p(-2 * p) if p < mpf(1) / 2 else mlog(q))
    return 4 * p ** 2 + 2 * p ** 2 * mlog(p, 2) + br / mlog(2)


def D_of_t(t, depth=60):
    t = np.array(t, dtype=np.float64, copy=True)
    D = np.zeros_like(t)
    I = np.zeros_like(t)
    w = 1.0
    for k in range(depth):
        d = np.minimum(t, 1 - t)
        D += w * eps(2 * d)
        I += w * 2 * d
        t = (2 * t) % 1.0
        w *= 0.5
    return D, I


def D_inf(s, L=200):
    s = np.asarray(s, dtype=np.float64)
    D, I = D_of_t(s)
    acc = D.copy()
    for l in range(L):
        acc += 2 * (2.0 ** l) * eps(s * 2.0 ** (-l))
    return acc, D, I


if __name__ == "__main__":
    mp.dps = 40
    # accuracy check of eps against mpmath
    ps = np.concatenate([10.0 ** -np.arange(1, 18), np.linspace(0.001, 1, 50)])
    err = max(abs(float(eps_mp(p)) - eps(np.array([p]))[0]) / max(abs(float(eps_mp(p))), 1e-300) for p in ps if p > 0)
    print("max relative error of eps vs mpmath on test points:", err)
    p = np.linspace(1e-6, 1 - 1e-6, 200001)
    e = eps(p)
    print("sign of eps: negative on (0,1/2) grid:", bool(np.all(e[p < 0.5 - 1e-6] < 0)), " positive on (1/2,1):", bool(np.all(e[p > 0.5 + 1e-6] > 0)))
    s = np.linspace(0.5, 1.0, 500001)[:-1]
    Dinf, D, I = D_inf(s)
    k = np.argmin(Dinf)
    print("min over s in [1/2,1) of D_inf(s) = %.10f at s = %.8f  (D(s) = %.6f, I(s) = %.6f)" % (Dinf[k], s[k], D[k], I[k]))
    k2 = np.argmin(Dinf / s)
    print("min D_inf(s)/s = %.10f at s = %.8f" % ((Dinf / s)[k2], s[k2]))
    for sv in [0.5, 2 / 3, 0.664, 0.668, 0.7, 0.75, 0.8, 0.9]:
        a, d, i = D_inf(np.array([sv]))
        print("s=%.6f D(s)=%.8f D_inf(s)=%.8f I(s)=%.6f" % (sv, d[0], a[0], i[0]))
    # direct check along t = 2^-m (2/3)
    for m in [10, 20, 40, 80, 160, 400]:
        tt = np.array([(2 / 3) * 2.0 ** (-m)])
        Dt, It = D_of_t(tt, depth=m + 60)
        print("m=%d t=(2/3)2^-m: 2^m D = %.10f ; 4 - H/I = %.6e" % (m, Dt[0] * 2.0 ** m, Dt[0] / It[0]))
    # min of D over the unit interval on a grid, normalised by t(1-t)
    t = np.linspace(1e-7, 1 - 1e-7, 2000001)
    Dt, It = D_of_t(t)
    print("min D(t) on grid: %.4e ; min D/t: %.6f at t=%.6g ; min D/(t(1-t)): %.6f ; max H/I: %.8f at t=%.6g"
          % (Dt.min(), (Dt / t).min(), t[np.argmin(Dt / t)], (Dt / (t * (1 - t))).min(), (4 - Dt / It).max(), t[np.argmax(4 - Dt / It)]))
