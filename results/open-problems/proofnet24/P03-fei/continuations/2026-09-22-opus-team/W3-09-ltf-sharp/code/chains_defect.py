"""Defect D(t) = 4 I(t) - H(t) of AND/OR chains, and its scaling limit near t = 0.

For t = 2^-m s, s in [1/2, 1):  2^m D(2^-m s) = D(s) + 2 sum_{l=0}^{m-1} 2^l eps(2^-l s),  eps(p) = 4p - A(p),
so D_inf(s) = lim_m 2^m D(2^-m s) = D(s) + 2 sum_{l>=0} 2^l eps(2^-l s).
Chains satisfy H <= 4 I iff D >= 0 on [0,1]; the chains' H/I tends to 4 at t -> 0 with gap D_inf(s)/(2 m s + I(s)).
"""
import numpy as np
from chains_takagi import A, HI_t

def eps(p):
    return 4 * p - A(p)

def D_of_t(t, depth=64):
    H, I = HI_t(t, depth)
    return 4 * I - H, H, I

def D_inf(s, L=80):
    s = np.asarray(s, dtype=np.float64)
    D, H, I = D_of_t(s)
    acc = D.copy()
    for l in range(L):
        acc += 2 * (2.0 ** l) * eps(s * 2.0 ** (-l))
    return acc, D, H, I

if __name__ == "__main__":
    p = np.linspace(0, 1, 2001)
    e = eps(p)
    neg = p[(e < 0)]
    print("eps(p) = 4p - A(p): negative on p in (%.4f, %.4f); eps(1/2) = %.3e; min eps = %.6f at p = %.4f; max = %.4f"
          % (neg.min(), neg.max(), eps(np.array([0.5]))[0], e.min(), p[np.argmin(e)], e.max()))
    s = np.linspace(0.5, 1.0, 200001)[:-1]
    Dinf, D, H, I = D_inf(s)
    k = np.argmin(Dinf / s)
    print("min over s in [1/2,1) of D_inf(s)/s = %.10f at s = %.8f ; D_inf there = %.10f" % ((Dinf / s)[k], s[k], Dinf[k]))
    k2 = np.argmin(Dinf)
    print("min D_inf(s) = %.10f at s = %.8f" % (Dinf[k2], s[k2]))
    # D on the whole interval
    t = np.linspace(1e-9, 1 - 1e-9, 2000001)
    Dt, Ht, It = D_of_t(t)
    print("min D(t)/t over (0,1): %.8f at t = %.6g ;  min D(t) = %.3e" % ((Dt / t).min(), t[np.argmin(Dt / t)], Dt.min()))
    print("max H/I over grid: %.8f at t = %.6g" % ((Ht / It).max(), t[np.argmax(Ht / It)]))
    # near-2/3 values of s
    for sv in [0.5, 2 / 3, 0.66, 0.7, 0.75, 0.8, 0.9, 0.99]:
        a, d, h, i = D_inf(np.array([sv]))
        print("s=%.5f D(s)=%.6f D_inf(s)=%.6f D_inf/s=%.6f I(s)=%.6f" % (sv, d[0], a[0], a[0] / sv, i[0]))
    # predicted gap for t = 2^-m s at large m
    for m in [10, 20, 40, 80, 160]:
        for sv in [2 / 3]:
            tt = np.array([sv * 2.0 ** (-m)])
            Dt1, Ht1, It1 = D_of_t(tt, depth=m + 70)
            print("m=%d s=2/3: H/I = %.10f, 4 - H/I = %.4e, predicted D_inf/(2 m s + I(s)) = %.4e"
                  % (m, Ht1[0] / It1[0], 4 - Ht1[0] / It1[0], D_inf(np.array([sv]))[0][0] / (2 * m * sv + HI_t(np.array([sv]))[1][0])))
