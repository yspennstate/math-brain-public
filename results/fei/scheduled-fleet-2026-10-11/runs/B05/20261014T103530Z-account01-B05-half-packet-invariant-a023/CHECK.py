#!/usr/bin/env python3
"""Checks the half-packet scalar bound and augmented activation invariant."""
from fractions import Fraction
from math import log, log2
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
    cp = caps(p)
    U = sum(xr(x, y) for x, y in zip(p, cp))
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
    phi = sum(q(float(p[1 << i])) for i in range(n))
    return dict(U=U, I=I, B=B, M=G-B, G=G, h=h, p=p, phi=phi, n=n)


def activate(v):
    return tuple(v) + tuple(1 for _ in v)


def product(v, w):
    return tuple(x * y for y in w for x in v)


def q(p):
    return 0.0 if p == 0 else p * log2(1 / p) + 2 * p / log(2)


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


def scalar_checks(N=700):
    count = 0
    mx = (-1e100, None)
    for j in range(N + 1):
        m = -1 + 2 * j / N
        lim = 1 - abs(m)
        for k in range(1, N + 1):
            a = lim * k / N
            if a == 0:
                continue
            p = a * a
            P = R(m) - 0.5 * (R(m - a) + R(m + a)) - C(m, p)
            ratio = P / q(p)
            mx = max(mx, (ratio, (m, a)))
            assert P <= 0.5 * q(p) + 5e-12
            count += 1
    return count, mx


def invariant(s, eta=1.0):
    cstar = 14.5 + 4 / log(2)
    return s['M'] + (1 + eta) * s['U'] - cstar * s['I'] + 2 * s['phi']


def boolean_checks():
    rng = Random(20261014)
    vecs = []
    for n in range(4):
        size = 1 << n
        for mask in range(1 << size):
            vecs.append(tuple(1 if mask & (1 << j) else -1 for j in range(size)))
    for n in range(4, 8):
        size = 1 << n
        for _ in range(20):
            vecs.append(tuple(1 if rng.getrandbits(1) else -1 for _ in range(size)))
    max_half = -1e100
    max_aug = -1e100
    for v in vecs:
        s = stats(v)
        sa = stats(activate(v))
        m = float(s['h'][0])
        eta = 1.0
        cstar = 14.5 + 4 / log(2)
        L = s['M'] + (1 + eta) * s['U'] - cstar * s['I']
        La = sa['M'] + (1 + eta) * sa['U'] - cstar * sa['I']
        half_rhs = 0.5 * L + 0.5 * s['phi'] + (10.5 - cstar) * (1 - m) / 2
        max_half = max(max_half, La - half_rhs)
        assert La <= half_rhs + 3e-10
        max_aug = max(max_aug, invariant(sa) - 0.5 * invariant(s))
        assert invariant(sa) <= 0.5 * invariant(s) + 3e-10
    return len(vecs), max_half, max_aug


def generated_checks():
    rng = Random(530)
    pool = [(-1,), (1,), (-1, 1), (1, -1)]
    checked = 0
    max_inv = -1e100
    for _ in range(120):
        choices = [v for v in pool if (len(v).bit_length() - 1) < 7]
        v = rng.choice(choices)
        if rng.random() < 0.65:
            w = activate(v)
        else:
            candidates = [u for u in pool if len(u) * len(v) <= 128]
            w = product(v, rng.choice(candidates))
        pool.append(w)
        sw = stats(w)
        max_inv = max(max_inv, invariant(sw))
        assert invariant(sw) <= 3e-9
        n = len(w).bit_length() - 1
        for i in range(n):
            for bit in (0, 1):
                sr = stats(restrict(w, i, bit))
                max_inv = max(max_inv, invariant(sr))
                assert invariant(sr) <= 3e-9
                checked += 1
    return len(pool), checked, max_inv


sc = scalar_checks()
bc = boolean_checks()
gc = generated_checks()
print('status=PASS')
print('scalar_cases=', sc[0])
print('max_P_over_q=', sc[1])
print('boolean_cores=', bc[0])
print('max_half_packet_residual=', bc[1])
print('max_augmented_contraction_residual=', bc[2])
print('generated_functions=', gc[0])
print('generated_restrictions=', gc[1])
print('max_generated_invariant=', gc[2])
print('c_star=', 14.5 + 4 / log(2))
print('GU_a_eta1=', 16.5 + 4 / log(2))
print('FEI_C_eta1=', 35 + 8 / log(2))

