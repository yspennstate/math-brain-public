"""Numerical side of arXiv 2610.34036 (Ando, Umehara): a closed strictly convex smooth surface with one umbilic.

F(x, y) = a(x) - a(y) + sin x sin y, a(t) = sin^4 t + 3 sin^2 t.
1. c = inf |F_zz|, M0 = sup |F|, M1 = sup |F_W| on a period; a delta with E_delta < c/2  (Lemma 1.1, (2.3)).
2. Lemma 2.1: |(f_delta)_WW| / b_delta >= c/2 on a window, f_delta = exp(-delta (1+|W|^2)^(1/4)) F, with the
   derivative taken symbolically from f_delta itself (not from the paper's formula (2.7)).
3. Lemma 1.4: for the surface with support function rho, built in R^3 from the 1-homogeneous extension
   H(x) = |x| rho(x/|x|), the difference of the principal radii of curvature equals
   D^2 |rho_WW + (2 conj(W)/D) rho_W|, D = 1 + |W|^2, and their sum equals 2 rho + D^2 rho_{W conj(W)}.
   The radii are the nonzero eigenvalues of the Hessian of H, taken by finite differences at 40 digits.
4. The identity rho_WW + (2 conj(W)/D) rho_W = eps f_WW / D for rho = 1 + eps f / D, at random points.
"""
import math
import random
import sys

import sympy as sp
import mpmath as mp


def part1():
    n = 1440
    xs = [2 * math.pi * i / n for i in range(n)]
    s = [math.sin(t) for t in xs]
    co = [math.cos(t) for t in xs]
    a = [v ** 4 + 3 * v ** 2 for v in s]
    a1 = [(4 * v ** 3 + 6 * v) * w for v, w in zip(s, co)]
    s4 = [v ** 4 for v in s]
    cmin, m0, m1 = 1e9, 0.0, 0.0
    arg = None
    for i in range(n):
        for j in range(n):
            re = 12 - 16 * (s4[i] + s4[j])
            im = 2 * co[i] * co[j]
            q = math.hypot(re, im) / 4
            if q < cmin:
                cmin, arg = q, (xs[i], xs[j])
            f = abs(a[i] - a[j] + s[i] * s[j])
            if f > m0:
                m0 = f
            fx = a1[i] + co[i] * s[j]
            fy = -a1[j] + s[i] * co[j]
            g = math.hypot(fx, fy) / 2
            if g > m1:
                m1 = g
    return cmin, arg, m0, m1


def main():
    c, arg, M0, M1 = part1()
    print("1: c = inf |F_zz| = %.6f at (x, y) = (%.4f, %.4f); M0 = %.4f; M1 = %.4f  (grid 1440 x 1440 on a period)" % (c, arg[0], arg[1], M0, M1))
    delta = 0.03
    E = delta * M1 / 2 + (delta ** 2 + 3 * delta) * M0 / 16
    print("1: delta = %.3f gives E_delta = %.5f, c/2 = %.5f, condition (2.3) holds: %s" % (delta, E, c / 2, E < c / 2))

    X, Y = sp.symbols("X Y", real=True)
    a = lambda t: sp.sin(t) ** 4 + 3 * sp.sin(t) ** 2
    F = a(X) - a(Y) + sp.sin(X) * sp.sin(Y)
    D = 1 + X ** 2 + Y ** 2
    b = sp.exp(-sp.Rational(3, 100) * D ** sp.Rational(1, 4))
    f = b * F
    dW = lambda g: (sp.diff(g, X) - sp.I * sp.diff(g, Y)) / 2
    dWb = lambda g: (sp.diff(g, X) + sp.I * sp.diff(g, Y)) / 2
    fWW = dW(dW(f))
    ratio = sp.lambdify((X, Y), fWW / b, "math")
    # lambdify with "math" cannot return complex: split
    re_r = sp.lambdify((X, Y), sp.re(sp.expand(fWW / b, complex=True)), "math")
    im_r = sp.lambdify((X, Y), sp.im(sp.expand(fWW / b, complex=True)), "math")
    lo = 1e9
    where = None
    step = 0.07
    R = 45.0
    k = int(R / step)
    npts = 0
    for i in range(-k, k + 1):
        x = i * step
        for j in range(-k, k + 1):
            y = j * step
            v = math.hypot(re_r(x, y), im_r(x, y))
            npts += 1
            if v < lo:
                lo, where = v, (x, y)
    print("2: min of |(f_delta)_WW| / b_delta on |X|, |Y| <= %.0f (step %.2f, %d points) = %.6f at (%.2f, %.2f); c/2 = %.6f; Lemma 2.1 holds there: %s" % (R, step, npts, lo, where[0], where[1], c / 2, lo >= c / 2))

    # ---- part 3: the umbilic criterion against the surface in R^3 ----
    mp.mp.dps = 40
    eps = sp.Rational(1, 50)
    tests = {
        "rho_eps (the paper's, eps = 1/50)": 1 + eps * f / D,
        "test function": 1 + sp.Rational(1, 10) * sp.exp(-(X - sp.Rational(1, 3)) ** 2 - Y ** 2 / 2) * (1 + X * Y) + sp.Rational(1, 20) * sp.cos(X + 2 * Y) / D,
    }
    rng = random.Random(11)
    for name, rho in tests.items():
        crit = dW(dW(rho)) + 2 * (X - sp.I * Y) / D * dW(rho)
        lap = dW(dWb(rho))
        rho_n = sp.lambdify((X, Y), rho, "mpmath")
        crit_n = sp.lambdify((X, Y), crit, "mpmath")
        lap_n = sp.lambdify((X, Y), lap, "mpmath")

        def H(x1, x2, x3):
            r = mp.sqrt(x1 * x1 + x2 * x2 + x3 * x3)
            den = r - x3
            return r * rho_n(x1 / den, x2 / den)

        worst_d, worst_s = mp.mpf(0), mp.mpf(0)
        for _ in range(6):
            Xv, Yv = mp.mpf(rng.uniform(-2.5, 2.5)), mp.mpf(rng.uniform(-2.5, 2.5))
            Dv = 1 + Xv * Xv + Yv * Yv
            n = [2 * Xv / Dv, 2 * Yv / Dv, (Dv - 2) / Dv]
            h = mp.mpf(10) ** (-10)
            Hm = mp.zeros(3, 3)
            for i in range(3):
                for j in range(3):
                    def sh(si, sj):
                        p = list(n)
                        p[i] += si * h
                        p[j] += sj * h
                        return H(*p)
                    Hm[i, j] = (sh(1, 1) - sh(1, -1) - sh(-1, 1) + sh(-1, -1)) / (4 * h * h)
            tr = Hm[0, 0] + Hm[1, 1] + Hm[2, 2]
            e2 = (Hm[0, 0] * Hm[1, 1] - Hm[0, 1] * Hm[1, 0] + Hm[0, 0] * Hm[2, 2] - Hm[0, 2] * Hm[2, 0] + Hm[1, 1] * Hm[2, 2] - Hm[1, 2] * Hm[2, 1])
            diff_r3 = mp.sqrt(abs(tr * tr - 4 * e2))
            cv = crit_n(Xv, Yv)
            diff_formula = Dv * Dv * abs(cv)
            sum_formula = 2 * rho_n(Xv, Yv) + Dv * Dv * mp.re(lap_n(Xv, Yv))
            worst_d = max(worst_d, abs(diff_r3 - diff_formula))
            worst_s = max(worst_s, abs(tr - sum_formula))
            last = (float(Xv), float(Yv), float(diff_r3), float(diff_formula), float(tr), float(sum_formula))
        print("3: %s: 6 random points; largest |R1-R2 (from R^3) - D^2|criterion|| = %s; largest |R1+R2 - (2 rho + D^2 rho_WWbar)| = %s; last point W = (%.3f, %.3f): %.12f vs %.12f, %.12f vs %.12f" % ((name, mp.nstr(worst_d, 3), mp.nstr(worst_s, 3)) + last))

    # ---- part 4: the identity behind 'no finite umbilics' ----
    rho = 1 + eps * f / D
    lhs = dW(dW(rho)) + 2 * (X - sp.I * Y) / D * dW(rho)
    rhs = eps * fWW / D
    lhs_n = sp.lambdify((X, Y), lhs, "mpmath")
    rhs_n = sp.lambdify((X, Y), rhs, "mpmath")
    worst = mp.mpf(0)
    for _ in range(40):
        Xv, Yv = mp.mpf(rng.uniform(-30, 30)), mp.mpf(rng.uniform(-30, 30))
        worst = max(worst, abs(lhs_n(Xv, Yv) - rhs_n(Xv, Yv)) / abs(rhs_n(Xv, Yv)))
    print("4: rho_WW + (2 conj(W)/D) rho_W against eps f_WW / D at 40 random points: largest relative difference %s" % mp.nstr(worst, 3))


if __name__ == "__main__":
    main()
