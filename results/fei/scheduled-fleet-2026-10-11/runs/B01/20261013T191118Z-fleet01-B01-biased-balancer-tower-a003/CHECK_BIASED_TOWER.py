#!/usr/bin/env python3
"""Independent finite audit for the biased-balancer activation tower.

The proof of the uniform constant is analytic.  This checker reconstructs
U, I and G directly from truth tables and separately checks every exact
recurrence used by the proof.
"""

from fractions import Fraction
from math import log2
import random

SEED = 0xB01A003B
rng = random.Random(SEED)
B = (-1, -1, -1, 1)  # mean -1/2, U=I=1, G=2


def fwht(values):
    a = [Fraction(x) for x in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def upper_caps(p):
    c = list(p)
    n = len(c).bit_length() - 1
    for j in range(n):
        bit = 1 << j
        for s in range(1 << n):
            if not s & bit:
                c[s] += c[s | bit]
    return c


def U(f):
    p = [x * x for x in fwht(f)]
    c = upper_caps(p)
    return sum(float(x) * log2(float(y / x)) for x, y in zip(p, c) if x)


def restrict(f, j, bit):
    n = len(f).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << j) - 1)
        hi = z >> j
        out.append(f[lo | (bit << j) | (hi << (j + 1))])
    return out


def influence(f):
    n = len(f).bit_length() - 1
    return sum(
        Fraction(sum(f[x] != f[x ^ (1 << j)] for x in range(1 << n)), 1 << n)
        for j in range(n)
    )


def G(f):
    n = len(f).bit_length() - 1
    root = U(f)
    return sum(root - (U(restrict(f, j, 0)) + U(restrict(f, j, 1))) / 2 for j in range(n))


def mean(f):
    return Fraction(sum(f), len(f))


def W1(f):
    h = fwht(f)
    n = len(f).bit_length() - 1
    return sum(h[1 << j] ** 2 for j in range(n))


def product(f, g):
    # f uses the low block, g the high block.
    return [f[x] * g[y] for y in range(len(g)) for x in range(len(f))]


def balance(f):
    return product((-1, 1), f)


def activate(q):
    # Low fresh selector: selector 0 returns q, selector 1 returns +1.
    return [q[x >> 1] if not (x & 1) else 1 for x in range(2 * len(q))]


def scalar_F(t):
    t = float(t)
    u = 0.0 if t == 0 else t * t * log2(1 / (t * t))
    x = (1 + t) / 2
    y = (1 - t) / 2
    e1 = 0.0 if x == 0 else x * x * log2(1 / (x * x))
    e2 = 0.0 if y == 0 else y * y * log2(1 / y)
    return e1 + e2 - u / 2 + (1 - t * t) / 4


def tower(base, depth):
    assert depth >= 1
    f = activate(balance(base))
    layers = [f]
    for _ in range(2, depth + 1):
        f = activate(product(B, f))
        layers.append(f)
    return layers


assert mean(B) == Fraction(-1, 2)
assert influence(B) == 1
assert abs(U(B) - 1) < 1e-14
assert abs(G(B) - 2) < 1e-14

cases = []
for n in range(0, 4):
    for mask in range(1 << (1 << n)):
        cases.append(tuple(1 if (mask >> x) & 1 else -1 for x in range(1 << n)))

# Add rare defects and deterministic generic functions through seven variables.
for n in range(4, 8):
    rare = [-1] * (1 << n)
    rare[-1] = 1
    cases.append(tuple(rare))
    for _ in range(4):
        cases.append(tuple(rng.choice((-1, 1)) for _ in range(1 << n)))

direct_cases = 0
recurrence_checks = 0
transfer_checks = 0
endpoint_transfer_checks = 0
max_additive = (-1e100, None)
max_step_excess = (-1e100, None)
max_w1 = 0.0
max_error = 0.0

for base in cases:
    # Depth three is direct only when the resulting table remains modest.
    n = len(base).bit_length() - 1
    max_depth = 3 if n <= 4 else 2
    layers = tower(base, max_depth)
    prev = None
    for depth, f in enumerate(layers, 1):
        direct_cases += 1
        uf, gf = U(f), G(f)
        inf = float(influence(f))
        wf = float(W1(f))
        max_w1 = max(max_w1, wf)
        assert wf <= 0.5 + 2e-12
        additive = gf - (2 ** (-depth)) * G(base)
        if additive > max_additive[0]:
            max_additive = (additive, (n, depth, mean(base), uf, inf, gf))
        assert additive <= 24 + 2e-10

        ib, ub, gb = float(influence(base)), U(base), G(base)
        for bcoef in (0.0, 0.25, 0.75):
            acoef = 0.0 if ib == 0 else max(0.0, (gb - bcoef * ub) / ib)
            assert gb <= acoef * ib + bcoef * ub + 2e-12
            assert gf <= (acoef + 24) * inf + bcoef * uf + 2e-10
            transfer_checks += 1

        c_endpoint = 72 / 35
        if ub <= c_endpoint * ib + 2e-12:
            assert uf <= c_endpoint * inf + 2e-10
            endpoint_transfer_checks += 1

        if depth == 1:
            assert mean(f) == Fraction(1, 2)
            assert abs(uf - (1 + U(base) / 2)) < 3e-12
            assert influence(f) == 1 + influence(base) / 2
        else:
            m = mean(prev)
            assert Fraction(3, 8) <= m <= Fraction(1, 2)
            expected_mean = Fraction(1, 2) - m / 4
            expected_i = influence(prev) / 2 + 1 + m / 4
            expected_u = U(prev) / 2 + 0.5 + scalar_F(-m / 2)
            expected_w = W1(prev) / 16 + m * m / 8 + Fraction(1, 4) * (1 + m / 2) ** 2
            max_error = max(max_error, abs(float(mean(f) - expected_mean)))
            max_error = max(max_error, abs(float(influence(f) - expected_i)))
            max_error = max(max_error, abs(uf - expected_u))
            max_error = max(max_error, abs(wf - float(expected_w)))
            assert mean(f) == expected_mean
            assert influence(f) == expected_i
            assert abs(uf - expected_u) < 4e-11
            assert abs(wf - float(expected_w)) < 4e-12
            step_excess = gf - G(prev) / 2
            if step_excess > max_step_excess[0]:
                max_step_excess = (step_excess, (n, depth, mean(base)))
            assert step_excess <= 12 + 2e-10
            recurrence_checks += 4
        prev = f

print(f"seed={SEED}")
print(f"base_cases={len(cases)}")
print(f"direct_tower_cases={direct_cases}")
print(f"exact_recurrence_checks={recurrence_checks}")
print(f"GU_transfer_checks={transfer_checks}")
print(f"endpoint_transfer_checks={endpoint_transfer_checks}")
print(f"max_W1={max_w1:.15f}")
print(f"max_step_G_minus_half_previous={max_step_excess[0]:.15f} witness={max_step_excess[1]}")
print(f"max_G_minus_seed={max_additive[0]:.15f} witness={max_additive[1]}")
print(f"max_recurrence_error={max_error:.3e}")
print("theorem_constant=24")
print("full_fei=OPEN")
print("PASS")
