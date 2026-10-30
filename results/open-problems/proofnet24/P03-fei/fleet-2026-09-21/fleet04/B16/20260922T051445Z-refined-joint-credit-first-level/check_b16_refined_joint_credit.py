#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import log2, sqrt

C = Fraction(4076157, 625000)
D0 = Fraction(7, 40)
YLOW = Fraction(3, 25)


def ln_interval_ge1(q, terms=220):
    q = Fraction(q)
    assert q >= 1
    z = (q - 1) / (q + 1)
    s = Fraction(0)
    p = z
    for k in range(terms):
        s += p / Fraction(2 * k + 1)
        p *= z * z
    lo = 2 * s
    hi = lo + 2 * p / (Fraction(2 * terms + 1) * (1 - z * z))
    return lo, hi


LN2_LO, LN2_HI = ln_interval_ge1(Fraction(2), 240)


def h2_interval(x):
    x = Fraction(x)
    if x in (0, 1):
        return Fraction(0), Fraction(0)
    a0, a1 = ln_interval_ge1(1 / x)
    b0, b1 = ln_interval_ge1(1 / (1 - x))
    nlo = x * a0 + (1 - x) * b0
    nhi = x * a1 + (1 - x) * b1
    return nlo / LN2_HI, nhi / LN2_LO


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0 if x in (0.0, 1.0) else float("nan")
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def g(u):
    return h2((1.0 - u) / 2.0)


def psi(u):
    u = min(1.0, max(0.0, u))
    return 1.0 + g(sqrt(max(0.0, 1.0 - u * u))) - g(u)


def fwht(vals):
    a = [float(v) for v in vals]
    n = len(a)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return [x / n for x in a]


def joint_credit(f0, f1):
    n = len(f0)
    aa, bb = fwht(f0), fwht(f1)
    delta = sum(x != y for x, y in zip(f0, f1)) / n
    hb_given_s = 0.0
    hj_given_s = 0.0
    for a, b in zip(aa, bb):
        den = a * a + b * b
        if den < 1e-30:
            continue
        mass = den / 2.0
        xb = b * b / den
        theta = (a - b) ** 2 / (2.0 * den)
        hb_given_s += mass * h2(xb)
        hj_given_s += mass * h2(theta)
    return hb_given_s + h2(delta) - hj_given_s, delta, aa[0], bb[0]


def refined_bound(delta, a):
    A = a * a
    if A >= 1.0 - 1e-14:
        return 1.0
    u = abs(1.0 - 2.0 * delta + A) / (1.0 - A)
    return h2(delta) - 1.0 + 2.0 * A + (1.0 - A) * psi(u)


# Exact logarithm-enclosure proof at delta=7/40.
hd_lo, hd_hi = h2_interval(D0)
hy_lo, hy_hi = h2_interval(YLOW)
L_lower = C * D0 - 1 - hd_hi + hy_lo
assert L_lower > 0

# y(7/40)=(20-sqrt(231))/40 > 3/25.
assert Fraction(231) < Fraction(76, 5) ** 2

# Derivative proof.  artanh z <= z + z^3/(3(1-z^2)).
x = Fraction(13, 20)
v2 = 1 - x * x
expr = 2 * x + x ** 3 / (3 * v2) + v2 / (3 * x)
assert expr == Fraction(79039, 45045)
assert LN2_LO > Fraction(2, 3)
derivative_margin_lower = C - 3 * expr
assert derivative_margin_lower > 0

# Direct finite Walsh-pair self-check through three residual variables.
count = 0
min_slack = float("inf")
for nvars in range(4):
    N = 2 ** nvars
    funcs = list(product((-1, 1), repeat=N))
    means = [sum(f) / N for f in funcs]
    for i, f0 in enumerate(funcs):
        for j, f1 in enumerate(funcs):
            if abs(means[i] + means[j]) > 1e-12:
                continue
            credit, delta, a, b = joint_credit(f0, f1)
            A = a * a
            assert delta + 1e-12 >= A
            if A < 1.0 - 1e-12:
                lower = refined_bound(delta, abs(a))
                slack = credit - lower
                assert slack >= -1e-10
                min_slack = min(min_slack, slack)
            count += 1

assert count == 12948

# Numerical context only: zero of L_C in (0,1/2).
def L(delta):
    y = (1.0 - 2.0 * sqrt(delta * (1.0 - delta))) / 2.0
    return float(C) * delta - 1.0 - h2(delta) + h2(y)

lo, hi = 0.17, 0.18
for _ in range(100):
    mid = (lo + hi) / 2.0
    if L(mid) > 0:
        hi = mid
    else:
        lo = mid
root = (lo + hi) / 2.0

print("refined_pair_checks", count)
print("min_refined_slack", min_slack)
print("L_7_40_rigorous_lower", float(L_lower))
print("derivative_rigorous_margin_lower", float(derivative_margin_lower))
print("exact_zero_numeric_context", root)
print("status PASS")
