#!/usr/bin/env python3
"""Independent floating checks for the complete activation correction."""
from fractions import Fraction
from math import log2, log
from random import Random


def xr(x, y):
    return 0.0 if x == 0 else float(x) * log2(float(y / x))


def T(a, b):
    return xr(a, a + b) + xr(b, a + b)


def caps(p):
    a = list(p)
    n = len(a).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(a)):
            if not s & bit:
                a[s] += a[s | bit]
    return a


def fwht(v):
    a = [Fraction(x) for x in v]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def restrict(v, i, bit):
    n = len(v).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << i) - 1)
        hi = z >> i
        out.append(v[lo | (bit << i) | (hi << (i + 1))])
    return tuple(out)


def basic(v):
    h = fwht(v)
    p = [x * x for x in h]
    c = caps(p)
    U = sum(xr(x, y) for x, y in zip(p, c))
    I = sum(s.bit_count() * float(x) for s, x in enumerate(p))
    n = len(v).bit_length() - 1
    B = 0.0
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if not s & bit:
                B += T(p[s], p[s | bit])
    return U, I, B, h, p


def stats(v):
    U, I, B, h, p = basic(v)
    n = len(v).bit_length() - 1
    G = n * U
    for i in range(n):
        G -= 0.5 * basic(restrict(v, i, 0))[0]
        G -= 0.5 * basic(restrict(v, i, 1))[0]
    return U, I, B, G - B, h, p


def activate(v):
    return tuple(v) + tuple(1 for _ in v)


def U4(p):
    return sum(xr(x, y) for x, y in zip(p, caps(p)))


def R(m):
    return U4([(1 + m) ** 2 / 4, (1 - m * m) / 4,
               (1 - m) ** 2 / 4, (1 - m * m) / 4]) - 0.5 * xr(m * m, 1)


def Bz(m):
    return (1 - m * m) / 2 + 0.25 * T((1 + m) ** 2, (1 - m) ** 2)


def C(m, p):
    return (-0.5 * T(m * m, p) + 0.25 * T((1 + m) ** 2, p)
            + 0.25 * T((1 - m) ** 2, p))


def q(p):
    return 0.0 if p == 0 else p * log2(1 / p) + 2 * p / log(2)


def scalar_checks(N=500):
    counts = 0
    max_dr = (-1e100, None)
    max_nc = (-1e100, None)
    max_p = (-1e100, None)
    max_root = (-1e100, None)
    for j in range(N + 1):
        m = -1 + 2 * j / N
        lim = 1 - abs(m)
        J = (1 - m) / 2
        if J:
            rr = ((3 * R(m) - Bz(m)) / J)
            max_root = max(max_root, (rr, m))
            assert rr <= 10.5 + 1e-10
        for k in range(1, N + 1):
            a = lim * k / N
            if a == 0:
                continue
            p = a * a
            dr = R(m) - 0.5 * (R(m - a) + R(m + a))
            nc = -C(m, p)
            pp = dr + nc
            max_dr = max(max_dr, (dr / q(p), (m, a)))
            max_nc = max(max_nc, (nc / q(p), (m, a)))
            max_p = max(max_p, (pp / q(p), (m, a)))
            assert dr <= 0.5 * q(p) + 2e-12
            assert nc <= 0.5 * q(p) + 2e-12
            assert pp <= q(p) + 4e-12
            counts += 1
    return counts, max_dr, max_nc, max_p, max_root


def boolean_checks():
    rng = Random(20261014)
    vectors = []
    for n in range(0, 4):
        size = 1 << n
        for mask in range(1 << size):
            vectors.append(tuple(1 if mask & (1 << j) else -1 for j in range(size)))
    for n in range(4, 8):
        size = 1 << n
        for _ in range(24):
            vectors.append(tuple(1 if rng.getrandbits(1) else -1 for _ in range(size)))
    max_formula = 0.0
    max_bound = -1e100
    checked = 0
    for v in vectors:
        U, I, B, M, h, p = stats(v)
        va = activate(v)
        Ua, Ia, Ba, Ma, ha, pa = stats(va)
        m = float(h[0])
        phi = sum(q(float(p[1 << i])) for i in range(len(v).bit_length() - 1))
        psum = 0.0
        for i in range(len(v).bit_length() - 1):
            a = float(h[1 << i])
            psum += R(m) - 0.5 * (R(m - a) + R(m + a)) - C(m, a * a)
        rhsM = 0.5 * M + psum + R(m) - Bz(m)
        max_formula = max(max_formula, abs(Ma - rhsM))
        assert abs(Ma - rhsM) < 2e-10
        for eta in (0.25, 1.0):
            lhs = Ma + (1 + eta) * Ua
            rhs = 0.5 * (M + (1 + eta) * U) + phi + 10.5 * (1 - m) / 2
            max_bound = max(max_bound, lhs - rhs)
            assert lhs <= rhs + 2e-10
        checked += 1
    return checked, max_formula, max_bound


sc = scalar_checks()
bc = boolean_checks()
print("status=PASS")
print("scalar_cases=", sc[0])
print("max_D_over_q=", sc[1])
print("max_minusC_over_q=", sc[2])
print("max_P_over_q=", sc[3])
print("max_root_ratio_eta1=", sc[4])
print("boolean_cores=", bc[0])
print("max_activation_formula_error=", bc[1])
print("max_theorem_residual=", bc[2])

