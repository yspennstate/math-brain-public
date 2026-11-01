#!/usr/bin/env python3
"""Numerical pilot: repeat fair activation of mask 56242."""

import math

QMASK = 56242


def fwht(a):
    a = list(map(float, a))
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def upper_caps(p):
    c = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if not s & bit:
                c[s] += c[s | bit]
    return c


def ubi(f):
    p = [x * x for x in fwht(f)]
    caps = upper_caps(p)
    U = sum(p[s] * math.log2(caps[s] / p[s]) for s in range(len(p)) if p[s])
    I = sum(s.bit_count() * p[s] for s in range(len(p)))
    B = 0.0
    n = len(f).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if s & bit:
                continue
            a, b = p[s], p[s | bit]
            mass = a + b
            if a:
                B += a * math.log2(mass / a)
            if b:
                B += b * math.log2(mass / b)
    return U, B, I


def restrict(f, i, bit):
    return [f[x] for x in range(len(f)) if ((x >> i) & 1) == bit]


def stats(f):
    U, B, I = ubi(f)
    n = len(f).bit_length() - 1
    G = n * U - sum((ubi(restrict(f, i, 0))[0] + ubi(restrict(f, i, 1))[0]) / 2
                    for i in range(n))
    M = G - B
    return U, I, B, G, M, (M + 1.25 * U) / I, M + 1.25 * U - 2 * I


def activate(q):
    # New low bit: q on bit 0, +1 on bit 1.
    out = []
    for value in q:
        out.extend((value, 1))
    return out


q = [1 if (QMASK >> j) & 1 else -1 for j in range(16)]
print("depth,n,U,I,B,G,M,ratio,residual_c2")
for depth in range(11):
    row = stats(q)
    print(depth, len(q).bit_length() - 1, *(f"{x:.15f}" for x in row), sep=",")
    q = activate(q)
