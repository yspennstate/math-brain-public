#!/usr/bin/env python3
"""Finite corroboration for the partial-star point-defect theorem.

The proof is analytic.  This checker independently enumerates truth tables,
Walsh spectra, U, influences and physical restrictions for the stated finite
range, and compares them with the closed forms used in the proof.
"""

from __future__ import annotations

import math


def fwht(a):
    a = list(map(float, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    scale = 1.0 / len(a)
    return [x * scale for x in a]


def upper_u(vals):
    m = (len(vals)).bit_length() - 1
    p = [x * x for x in fwht(vals)]
    ans = 0.0
    for s, ps in enumerate(p):
        if ps == 0.0:
            continue
        cap = sum(p[t] for t in range(1 << m) if (t & s) == s)
        ans += ps * math.log2(cap / ps)
    return ans


def influence(vals, i):
    return sum(vals[x] != vals[x ^ (1 << i)] for x in range(len(vals))) / len(vals)


def restrict(vals, i, bit):
    m = (len(vals)).bit_length() - 1
    out = []
    for y in range(1 << (m - 1)):
        lo = y & ((1 << i) - 1)
        hi = y >> i
        x = lo | (bit << i) | (hi << (i + 1))
        out.append(vals[x])
    return out


def delta(vals, i):
    return upper_u(vals) - 0.5 * (upper_u(restrict(vals, i, 0)) + upper_u(restrict(vals, i, 1)))


def partial_star(n, t):
    # bit 0 is z; bits 1,...,n are data; R={1,...,t}.
    out = []
    for mask in range(1 << (n + 1)):
        z = mask & 1
        xs = [(mask >> (1 + j)) & 1 for j in range(n)]
        exponent = z * sum(xs[:t]) + int(not any(xs))
        out.append(1 if exponent % 2 == 0 else -1)
    return out


def shifted_defect(n, t):
    out = []
    for mask in range(1 << n):
        exponent = sum((mask >> j) & 1 for j in range(t)) + int(mask == 0)
        out.append(1 if exponent % 2 == 0 else -1)
    return out


checks = 0
max_partial_ratio = (-1e100, None)
max_boundary_ratio = (-1e100, None)

for n in range(1, 10):
    delta_n = 2.0 ** (-n)
    e = 4.0 * delta_n * delta_n
    a = (0.5 - 2.0 * delta_n) ** 2
    for t in range(1, n + 1):
        vals = partial_star(n, t)
        p = [x * x for x in fwht(vals)]
        expected = sorted(x for x in [0.25, 0.25, a, a] + [e] * (2**n - 2) if x > 1e-24)
        actual = sorted(x for x in p if x > 1e-24)
        assert len(actual) == len(expected)
        assert max(abs(x - y) for x, y in zip(actual, expected)) < 1e-12
        checks += 1

        infs = [influence(vals, i) for i in range(n + 1)]
        assert abs(infs[0] - 0.5) < 1e-12
        for j in range(n):
            target = 0.5 if j < t else 2.0 * delta_n
            assert abs(infs[j + 1] - target) < 1e-12
        losses = [delta(vals, i) for i in range(n + 1)]
        assert sum(losses) <= 14.0 * sum(infs) + 1e-10
        for i, (loss, inf) in enumerate(zip(losses, infs)):
            if inf:
                ratio = loss / inf
                if ratio > max_partial_ratio[0]:
                    max_partial_ratio = (ratio, (n, t, i))
            assert loss <= 14.0 * inf + 1e-10
        checks += n + 2

for n in range(1, 11):
    for t in range(0, n + 1):
        vals = shifted_defect(n, t)
        infs = [influence(vals, i) for i in range(n)]
        losses = [delta(vals, i) for i in range(n)]
        for i, (loss, inf) in enumerate(zip(losses, infs)):
            if inf:
                ratio = loss / inf
                if ratio > max_boundary_ratio[0]:
                    max_boundary_ratio = (ratio, (n, t, i))
            assert loss <= 14.0 * inf + 1e-10
        assert sum(losses) <= 14.0 * sum(infs) + 1e-10
        checks += n + 1

print(f"PASS assertions/groups={checks}")
print(f"partial-star max coordinate loss/influence={max_partial_ratio[0]:.12f} at n,t,i={max_partial_ratio[1]}")
print(f"shifted-defect max coordinate loss/influence={max_boundary_ratio[0]:.12f} at n,t,i={max_boundary_ratio[1]}")
print("finite scope: partial stars n<=9; all parity-shifted defects n<=10")
print("analytic theorem scope: all n,t; finite check is corroboration only")
