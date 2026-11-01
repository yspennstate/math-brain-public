#!/usr/bin/env python3
"""Finite-support consistency check for PROB20-14 exact Laplace/Cramer duality.

This is NOT proof evidence for the infinite-variance theorem. It checks the
algebra/numerics of the exact identities on a critical finite-support law.
"""
import math

P = {0: 0.5, 1: 0.25, 3: 0.25}  # critical: E xi = 1, span h=1
HSPAN = 1


def f(s):
    return sum(p * s**k for k, p in P.items())


def lam(theta):
    return theta + math.log(f(math.exp(-theta)))


def total_progeny_pgf(z):
    # Monotone iteration from 0 gives the minimal solution T=z f(T).
    x = 0.0
    for _ in range(100000):
        y = z * f(x)
        if abs(y - x) < 1e-15:
            return y
        x = y
    raise RuntimeError("fixed-point iteration did not converge")


def invert_lam(t):
    lo, hi = 0.0, 1.0
    while HSPAN * lam(hi) < t:
        hi *= 2.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if HSPAN * lam(mid) < t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def K(t):
    theta = invert_lam(t)
    return theta - lam(theta)


def golden_max(func, lo, hi, steps=220):
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    x1 = hi - gr * (hi - lo)
    x2 = lo + gr * (hi - lo)
    f1, f2 = func(x1), func(x2)
    for _ in range(steps):
        if f1 < f2:
            lo = x1
            x1, f1 = x2, f2
            x2 = lo + gr * (hi - lo)
            f2 = func(x2)
        else:
            hi = x2
            x2, f2 = x1, f1
            x1 = hi - gr * (hi - lo)
            f1 = func(x1)
    x = (lo + hi) / 2.0
    return func(x), x


def H(y):
    return golden_max(lambda th: th * y - lam(th), 0.0, 30.0)


def I_direct(M, b):
    # Direct definition sup_t {b K(t)-M t}.
    return golden_max(lambda t: b * K(t) - M * t, 0.0, 10.0, steps=150)


def main():
    mean = sum(k * p for k, p in P.items())
    assert abs(mean - 1.0) < 1e-15

    transform_rows = []
    for theta in (0.05, 0.2, 0.7, 1.5):
        la = lam(theta)
        z = math.exp(-la)
        Tz = total_progeny_pgf(z)
        target = math.exp(-theta)
        assert abs(Tz - target) < 2e-13
        phi_u = math.exp(la) * Tz  # h=1, U=X-1, t=Lambda(theta)
        kval = -math.log(phi_u)
        assert abs(kval - (theta - la)) < 2e-13
        transform_rows.append((theta, la, Tz, kval))

    cramer_rows = []
    for M, b in ((20, 2), (20, 8), (100, 15)):
        direct, tstar = I_direct(M, b)
        hval, thstar = H(b / (M + b))
        formula = (M + b) * hval
        assert abs(direct - formula) < 2e-10
        cramer_rows.append((M, b, direct, formula, tstar, thstar))

    print("critical_mean", mean)
    print("transform_checks")
    for row in transform_rows:
        print("  theta=%.6g Lambda=%.12g T=%.12g K=%.12g" % row)
    print("cramer_checks")
    for row in cramer_rows:
        print("  M=%d b=%d direct=%.12g formula=%.12g t*=%.12g theta*=%.12g" % row)
    print("ALL_ASSERTIONS_PASSED")


if __name__ == "__main__":
    main()
