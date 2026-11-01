"""Refutation witnesses BT-1 / BT-2: T_s = 1[s*y0 + y1+...+ys >= s] = y0 OR AND_s.

Route's choice: light bias p = x/50, x = mu_A(y0=0) = 1/s, so q0 = p_h solves (1-p_h) a = x alpha, a = p^s:
   p_h = a(1-x) / (x + a(1-x)).
biased.tex (Thm biasfull:weightedcounter) choice: q = m^{-2}, eta = 1/m (same x = eta).

Part 1 (s <= 12): MY generic exact transform on the full 2^{s+1} table; rho_i, I_i, V exact; TC(mu_A) from the
explicit conditional law (marginal entropies minus joint entropy); logs in mpmath.iv (rigorous intervals).
Part 2: closed forms (derived independently in REFEREE.md) cross-checked against Part 1, then large s.
"""
import time
from fractions import Fraction as Fr
from math import comb
import mpmath
from mpmath import iv
from bfcore import *

iv.dps = 50
mpmath.mp.dps = 50


def ivlog(x):
    return iv.log(ivq(x)) if isinstance(x, Fr) else iv.log(x)


def ln_plus_iv(x):
    """ln^+ of a positive Fraction, as an interval."""
    if x <= 1:
        return iv.mpf(0)
    return iv.log(ivq(x))


def family(s, light, x):
    a = light ** s
    ph = a * (1 - x) / (x + a * (1 - x))
    return ph, a


def generic(s, light, x):
    n = s + 1
    ph, a = family(s, light, x)
    qs = [ph] + [light] * s
    T = [1 if (s * (y & 1) + popcount(y >> 1)) >= s else 0 for y in range(1 << n)]
    P = spectrum([2 * t - 1 for t in T], qs)
    V, I, D, J = metrics_exact(P)
    w = mu_weights(qs)
    alpha = sum(w[y] for y in range(1 << n) if T[y])
    Ii = [sum(P[S] for S in range(1 << n) if (S >> i) & 1) for i in range(n)]
    rho = [Ii[i] / sig2(qs[i]) for i in range(n)]
    # credit and excess (rigorous)
    credit = iv.mpf(0)
    for i in range(n):
        credit += ivq(Ii[i]) * ln_plus_iv(4 * rho[i] / V)
    vlv = ivq(V) * iv.log(ivq(1 / V))
    excess = (vlv - credit) / ivq(I)
    # TC of mu_A from the explicit law
    muA = {y: w[y] / alpha for y in range(1 << n) if T[y]}
    HY = iv.mpf(0)
    for pr in muA.values():
        HY += ivq(pr) * iv.log(ivq(1 / pr))
    Hm = iv.mpf(0)
    for i in range(n):
        p1 = sum(pr for y, pr in muA.items() if (y >> i) & 1)
        for pp in (p1, 1 - p1):
            if pp > 0:
                Hm += ivq(pp) * iv.log(ivq(1 / pp))
    TC = Hm - HY
    aTC = ivq(alpha) * TC / ivq(I)
    E = iv.mpf(0)
    for S in range(1, 1 << n):
        if P[S]:
            E += ivq(P[S]) * iv.log(ivq(sigS2(S, qs) / P[S]))
    ratio = E / iv.log(2) / ivq(D)
    # check x
    xA = sum(pr for y, pr in muA.items() if not (y & 1))
    return dict(excess=excess, aTC=aTC, ratio=ratio, alpha=alpha, xA=xA, V=V, I=I, D=D, E=E, TC=TC)


def closed(s, light, x, ctx=mpmath.mp, spectrum_sums=True):
    """Closed forms (all in ctx: mp or iv)."""
    ph, a = family(s, light, x)
    q = light
    alpha = ph + (1 - ph) * a
    V = 4 * alpha * (1 - alpha)
    I0 = 4 * ph * (1 - ph) * (1 - a)
    rho0 = 1 - a
    rhoj = (1 - ph) * q ** (s - 1)
    Ij = 4 * q * (1 - q) * rhoj
    I = I0 + s * Ij
    if ctx is iv:
        cv = lambda z: ivq(z)
        lg = iv.log
    else:
        cv = mpq
        lg = mpmath.log
    def lnp(z):
        return lg(cv(z)) if z > 1 else (iv.mpf(0) if ctx is iv else mpmath.mpf(0))
    credit = cv(I0) * lnp(4 * rho0 / V) + s * cv(Ij) * lnp(4 * rhoj / V)
    vlv = cv(V) * lg(cv(1 / V))
    excess = (vlv - credit) / cv(I)
    # TC(mu_A) = s h(x' ) - (1-xx) s h(q), x' = xx + (1-xx) q, xx = mu_A(y0=0) = (1-ph) a / alpha
    xx = (1 - ph) * a / alpha
    def h(z):
        if z == 0 or z == 1:
            return iv.mpf(0) if ctx is iv else mpmath.mpf(0)
        return cv(z) * lg(cv(1 / z)) + cv(1 - z) * lg(cv(1 / (1 - z)))
    TC = s * h(xx + (1 - xx) * q) - cv(1 - xx) * s * h(q)
    aTC = cv(alpha) * TC / cv(I)
    if not spectrum_sums:
        return dict(excess=excess, aTC=aTC, ratio=None, alpha=alpha, I=I, V=V, D=None, E=None, TC=TC)
    # corrected entropy and deficit from the explicit spectrum (see REFEREE.md section 2)
    E = (iv.mpf(0) if ctx is iv else mpmath.mpf(0))
    D = Fr(0)
    pq = q * (1 - q)
    for k in range(1, s + 1):
        base = comb(s, k) * pq ** k * q ** (2 * s - 2 * k)
        P_light = 4 * (1 - ph) ** 2 * base           # total mass of the C(s,k) light sets of size k
        P_heavy = 4 * ph * (1 - ph) * base           # total mass of the C(s,k) sets {0} u B, |B| = k
        L_light = (k - 1) * lg(cv(Fr(4))) + 2 * lg(cv(1 / (1 - ph))) + 2 * (s - k) * lg(cv(1 / q))
        L_heavy = k * lg(cv(Fr(4))) + 2 * (s - k) * lg(cv(1 / q))
        E += cv(P_light) * L_light + cv(P_heavy) * L_heavy
        D += (k - 1) * P_light + k * P_heavy
    P0 = 4 * ph * (1 - ph) * (1 - a) ** 2
    E += cv(P0) * lg(cv(1 / (1 - a) ** 2))
    ratio = E / lg(cv(Fr(2))) / cv(D)
    return dict(excess=excess, aTC=aTC, ratio=ratio, alpha=alpha, I=I, V=V, D=D, E=E, TC=TC)


def lo(z):
    return mpmath.mpf(z.a)


def hi(z):
    return mpmath.mpf(z.b)


def mid(z):
    return (lo(z) + hi(z)) / 2


def fmt(z):
    if z is None:
        return "(not computed)"
    if isinstance(z, iv.mpf):
        return "[%s, %s]" % (mpmath.nstr(lo(z), 10), mpmath.nstr(hi(z), 10))
    return mpmath.nstr(z, 10)


if __name__ == "__main__":
    t0 = time.time()
    print("=== Part 1: generic exact transform, route's family x = 1/s, p = x/50 ===")
    for s in [4, 6, 8, 10, 12]:
        x = Fr(1, s)
        light = x / 50
        g = generic(s, light, x)
        c = closed(s, light, x, iv)
        bound = (mpmath.mpf(s - 1) / (2 * s)) * mpmath.log(s) - mpmath.log(2)
        print("s=%2d  x_check=%s  excess/I=%s  alphaTC/I=%s  H+/Delta=%s  claimed lower display ((s-1)/2s)ln s - ln2 = %s"
              % (s, g["xA"] == x, fmt(g["excess"]), fmt(g["aTC"]), fmt(g["ratio"]), mpmath.nstr(bound, 6)))
        agree = all(abs(mid(g[k]) - mid(c[k])) < mpmath.mpf(10) ** -30
                    for k in ["excess", "aTC", "ratio"]) and g["I"] == c["I"] and g["V"] == c["V"] and g["D"] == c["D"]
        below = hi(g["excess"]) < bound
        print("      certified: excess/I < displayed lower bound?", below)
        print("      closed forms agree with the generic transform:", agree, "  (t=%.0fs)" % (time.time() - t0))
    print("=== Part 2: closed forms, large s (interval arithmetic) ===")
    for s in [16, 32, 64, 128, 256, 1024, 4096, 65536]:
        x = Fr(1, s)
        c = closed(s, x / 50, x, iv, spectrum_sums=(s <= 256))
        print("s=%5d excess/I=%s  alphaTC/I=%s  H+/Delta=%s   (ln s)/2 - ln 2 = %s, (ln s + 1)/8 = %s"
              % (s, fmt(c["excess"]), fmt(c["aTC"]), fmt(c["ratio"]),
                 mpmath.nstr(mpmath.log(s) / 2 - mpmath.log(2), 6), mpmath.nstr((mpmath.log(s) + 1) / 8, 6)))
    print("=== biased.tex parametrization: q = m^-2, eta = 1/m ===")
    for m in [4, 8, 16, 64, 256, 1024, 4096]:
        x = Fr(1, m)
        c = closed(m, Fr(1, m * m), x, iv, spectrum_sums=(m <= 256))
        print("m=%5d excess/I=%s  alphaTC/I=%s  H+/Delta=%s" % (m, fmt(c["excess"]), fmt(c["aTC"]), fmt(c["ratio"])))
    print("time", round(time.time() - t0, 1))
