"""Accurate defect of AND/OR chains (numba).

eps(p) = 4p - A(p).  For 0 <= p <= 1/2 the exact series
    eps(p) = p^2 (4 - 3/ln2 + 2 log2 p) + (2/ln2) sum_{n>=3} (2^n - 2) p^n / (n (n-1) (n-2))
is used when p < 0.05; otherwise the closed form with log1p.  (For p > 1/2 no cancellation occurs.)
D(t) = 4 I(t) - H(t) = sum_k 2^-k eps(2 d(T^k t)),   d(t) = min(t, 1-t),  T t = 2t mod 1.
D_inf(s) = lim_m 2^m D(2^-m s) = D(s) + 2 sum_{l>=0} 2^l eps(2^-l s)   (s in [1/2, 1)).
"""
import sys, math
import numpy as np
import numba as nb
import ltfcore  # sets priority and affinity
from mpmath import mp, mpf, log as mlog, log1p as mlog1p

LN2 = math.log(2.0)


@nb.njit(cache=True)
def eps(p):
    if p <= 0.0:
        return 0.0
    if p < 0.05:
        s = 0.0
        pn = p * p
        for n in range(3, 60):
            pn *= p
            term = (2.0 ** n - 2.0) * pn / (n * (n - 1.0) * (n - 2.0))
            s += term
            if term < 1e-20 * p * p:
                break
        return p * p * (4.0 - 3.0 / LN2 + 2.0 * math.log2(p)) + 2.0 * s / LN2
    q = abs(1.0 - 2.0 * p)
    br = 0.0
    if p < 1.0:
        br += 2.0 * (1.0 - p) ** 2 * math.log1p(-p)
    if q > 0.0:
        if p < 0.5:
            br -= q * q * math.log1p(-2.0 * p)
        else:
            br -= q * q * math.log(q)
    return 4.0 * p * p + 2.0 * p * p * math.log2(p) + br / LN2


@nb.njit(cache=True)
def D_I(t, depth):
    D = 0.0
    I = 0.0
    w = 1.0
    for k in range(depth):
        d = min(t, 1.0 - t)
        D += w * eps(2.0 * d)
        I += w * 2.0 * d
        t = (2.0 * t) % 1.0
        w *= 0.5
    return D, I


@nb.njit(cache=True)
def D_inf(s):
    D, I = D_I(s, 60)
    acc = D
    for l in range(90):
        acc += 2.0 * (2.0 ** l) * eps(s * 2.0 ** (-l))
    return acc, D, I


@nb.njit(cache=True)
def scan_Dinf(ss):
    out = np.empty(ss.shape[0])
    for i in range(ss.shape[0]):
        out[i] = D_inf(ss[i])[0]
    return out


@nb.njit(cache=True)
def scan_t(ts, depth):
    D = np.empty(ts.shape[0])
    I = np.empty(ts.shape[0])
    for i in range(ts.shape[0]):
        D[i], I[i] = D_I(ts[i], depth)
    return D, I


def eps_mp(p):
    p = mpf(p)
    if p == 0:
        return mpf(0)
    br = 2 * (1 - p) ** 2 * mlog1p(-p) if p < 1 else mpf(0)
    q = abs(1 - 2 * p)
    if q != 0:
        br -= q ** 2 * (mlog1p(-2 * p) if p < mpf(1) / 2 else mlog(q))
    return 4 * p ** 2 + 2 * p ** 2 * mlog(p, 2) + br / mlog(2)


if __name__ == "__main__":
    mp.dps = 50
    worst = 0.0
    for p in list(10.0 ** -np.arange(1, 25)) + list(np.linspace(0.001, 1, 997)):
        e1 = float(eps_mp(p)); e2 = eps(p)
        worst = max(worst, abs(e1 - e2) / max(abs(e1), 1e-300))
    print("max relative error of eps against mpmath (50 digits), 1021 points:", worst)
    p = np.linspace(1e-9, 1 - 1e-9, 1000001)
    e = np.array([eps(x) for x in p])
    print("eps < 0 at every grid point of (0,1/2):", bool(np.all(e[p < 0.5 - 1e-9] < 0)),
          "; eps > 0 at every grid point of (1/2,1):", bool(np.all(e[p > 0.5 + 1e-9] > 0)),
          "; min eps = %.6f at p = %.5f" % (e.min(), p[np.argmin(e)]))
    s = np.linspace(0.5, 1.0, 400001)[:-1]
    Dinf = scan_Dinf(s)
    k = int(np.argmin(Dinf))
    print("min over grid s in [1/2,1) of D_inf(s) = %.10f at s = %.9f" % (Dinf[k], s[k]))
    k2 = int(np.argmin(Dinf / s))
    print("min over grid of D_inf(s)/s = %.10f at s = %.9f" % ((Dinf / s)[k2], s[k2]))
    for sv in [0.5, 2 / 3, 0.664, 0.668, 0.7, 0.75, 0.8, 0.9, 0.99]:
        a, d, i = D_inf(sv)
        print("s=%.6f D(s)=%.8f D_inf(s)=%.8f I(s)=%.6f" % (sv, d, a, i))
    for m in [10, 20, 40, 80, 160, 400, 1000]:
        tt = (2 / 3) * 2.0 ** (-m)
        Dt, It = D_I(tt, m + 60)
        print("m=%d t=(2/3)2^-m: 2^m D = %.10f ; 4 - H/I = %.6e" % (m, Dt * 2.0 ** m, Dt / It))
    t = np.linspace(1e-8, 1 - 1e-8, 1000001)
    Dt, It = scan_t(t, 60)
    print("grid t in (0,1), 1e6 points: min D = %.4e ; min D/t = %.6f at t = %.6g ; max H/I = %.8f at t = %.6g"
          % (Dt.min(), (Dt / t).min(), t[np.argmin(Dt / t)], (4 - Dt / It).max(), t[np.argmax(4 - Dt / It)]))
