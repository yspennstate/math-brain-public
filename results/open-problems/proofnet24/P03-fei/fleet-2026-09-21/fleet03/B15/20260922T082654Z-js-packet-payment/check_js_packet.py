#!/usr/bin/env python3
"""Finite stress test for the analytic inequality JS(U,V) <= (2/ln2) Inf_i.

Enumerates all Boolean truth tables through n=4 and all coordinates. This is
only a diagnostic; the theorem in REPORT.md is analytic.
"""
import math


def fwht(a):
    a = [float(x) for x in a]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]


def restriction(vals, n, i, b):
    rem = [j for j in range(n) if j != i]
    out = []
    for y in range(1 << (n-1)):
        x = b << i
        for t, j in enumerate(rem):
            x |= ((y >> t) & 1) << j
        out.append(vals[x])
    return out


def js(U, V):
    ans = 0.0
    for u, v in zip(U, V):
        m = (u+v)/2.0
        if u:
            ans += 0.5*u*math.log2(u/m)
        if v:
            ans += 0.5*v*math.log2(v/m)
    return ans


def influence(vals, n, i):
    pairs = 0
    for x in range(1 << n):
        if ((x >> i) & 1) == 0 and vals[x] != vals[x ^ (1 << i)]:
            pairs += 1
    return pairs / float(1 << (n-1))


bound = 2.0/math.log(2.0)
print(f"analytic_bound={bound:.16f}")
for n in range(1, 5):
    best = 0.0
    arg = None
    for mask in range(1 << (1 << n)):
        vals = [1.0 if ((mask >> x) & 1) else -1.0 for x in range(1 << n)]
        for i in range(n):
            inf = influence(vals, n, i)
            if inf == 0.0:
                continue
            u = fwht(restriction(vals, n, i, 0))
            v = fwht(restriction(vals, n, i, 1))
            U = [z*z for z in u]
            V = [z*z for z in v]
            ratio = js(U, V)/inf
            if ratio > best:
                best = ratio
                arg = (mask, i)
    print(f"n={n} max_JS_over_Inf={best:.16f} arg={arg}")
    assert best <= bound + 1e-12
print("PASS")
