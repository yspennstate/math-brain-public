#!/usr/bin/env python3
"""Test the exact half-activation recurrence for the SMR(2,1/4) residual.

All Walsh coefficients are accumulated exactly as Fractions; only logarithms
are evaluated in floating point.  The reported recurrence error compares the
closed-form node remainder with direct evaluation on A(q).
"""

from fractions import Fraction
from math import log2
import random

SEED = 2026101405
rng = random.Random(SEED)


def fwht(values):
    a = [Fraction(v) for v in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/len(a) for x in a]


def upper_caps(p):
    c = list(p)
    n = len(c).bit_length()-1
    for i in range(n):
        b = 1 << i
        for s in range(1 << n):
            if not s & b:
                c[s] += c[s | b]
    return c


def xlogratio(x, y):
    return 0.0 if x == 0 else float(x) * log2(float(y/x))


def T(a, b):
    return xlogratio(a, a+b) + xlogratio(b, a+b)


def stats(f):
    n = len(f).bit_length()-1
    phat = fwht(f)
    p = [x*x for x in phat]
    cap = upper_caps(p)
    U = sum(xlogratio(x, y) for x, y in zip(p, cap))
    I = sum(float(x) * s.bit_count() for s, x in enumerate(p))
    B = 0.0
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                B += T(p[s], p[s | bit])
    return U, I, B, p, phat


def restrict(f, i, bit):
    n = len(f).bit_length()-1
    out = []
    for z in range(1 << (n-1)):
        lo = z & ((1 << i)-1)
        hi = z >> i
        out.append(f[lo | (bit << i) | (hi << (i+1))])
    return tuple(out)


def full_stats(f):
    U, I, B, p, phat = stats(f)
    n = len(f).bit_length()-1
    G = sum(U - (stats(restrict(f, i, 0))[0] + stats(restrict(f, i, 1))[0])/2
            for i in range(n))
    M = G-B
    L = M + 1.25*U - 2*I
    return dict(U=U, I=I, B=B, G=G, M=M, L=L, p=p, phat=phat)


def activate(q):
    # New selector is bit 0: +1 branch (bit 1) is constant +1.
    return tuple(1 if x & 1 else q[x >> 1] for x in range(2*len(q)))


def R_from_direct(q):
    return stats(activate(q))[0] - stats(q)[0]/2


def node_formula(q):
    sq = full_stats(q)
    n = len(q).bit_length()-1
    m = sq["phat"][0]
    r = R_from_direct(q)
    dr = 0.0
    for i in range(n):
        dr += r - (R_from_direct(restrict(q, i, 0)) +
                   R_from_direct(restrict(q, i, 1)))/2

    var = 1-float(m*m)
    a = (1+m)*(1+m)
    b = (1-m)*(1-m)
    bz = var/2 + 0.25*T(a, b)
    correction = 0.0
    for i in range(n):
        pi = sq["p"][1 << i]
        correction += (-0.5*T(m*m, pi) + 0.25*T(a, pi) + 0.25*T(b, pi))
    J = (1-float(m))/2
    remainder = dr + 2.25*r - bz - 2*J - correction
    sa = full_stats(activate(q))
    direct = sa["L"] - sq["L"]/2
    return direct, remainder, sq, sa, dict(m=float(m), R=r, DR=dr, Bz=bz,
                                           J=J, correction=correction)


max_rem = (-1e100, None)
min_rem = (1e100, None)
max_activated_L = (-1e100, None)
max_err = 0.0
count = 0
for n in range(4):
    for mask in range(1 << (1 << n)):
        q = tuple(1 if mask >> j & 1 else -1 for j in range(1 << n))
        direct, formula, sq, sa, pieces = node_formula(q)
        err = abs(direct-formula)
        max_err = max(max_err, err)
        rec = (n, mask, direct, sq["L"], sa["L"], pieces)
        max_rem = max(max_rem, (direct, rec), key=lambda x:x[0])
        min_rem = min(min_rem, (direct, rec), key=lambda x:x[0])
        max_activated_L = max(max_activated_L, (sa["L"], rec), key=lambda x:x[0])
        count += 1

random_count = 0
for n in range(4, 5):
    for _ in range(1000):
        q = tuple(-1 if j == 0 else rng.choice((-1,1)) for j in range(1 << n))
        direct, formula, sq, sa, pieces = node_formula(q)
        err = abs(direct-formula)
        max_err = max(max_err, err)
        qmask = sum((1 << j) for j, v in enumerate(q) if v == 1)
        rec = (n, qmask, direct, sq["L"], sa["L"], pieces)
        max_rem = max(max_rem, (direct, rec), key=lambda x:x[0])
        min_rem = min(min_rem, (direct, rec), key=lambda x:x[0])
        max_activated_L = max(max_activated_L, (sa["L"], rec), key=lambda x:x[0])
        random_count += 1

print(f"seed={SEED}")
print(f"exhaustive_cases={count}")
print(f"random_cases={random_count}")
print(f"max_recurrence_error={max_err:.3e}")
print(f"max_node_remainder={max_rem}")
print(f"min_node_remainder={min_rem}")
print(f"max_activated_L={max_activated_L}")
print("PASS")
