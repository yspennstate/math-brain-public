#!/usr/bin/env python3
"""Exact-Walsh/numerical-log audit of the parity-tower G recurrence."""

from math import e, log, log2
import itertools
import random


def fwht(values):
    a = [float(x) for x in values]
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2 * h):
            for j in range(h):
                x, y = a[start + j], a[start + h + j]
                a[start + j], a[start + h + j] = x + y, x - y
        h *= 2
    return a


def upper_u(values):
    N = len(values)
    coeff = fwht(values)
    p = [x * x / (N * N) for x in coeff]
    cap = p[:]
    n = N.bit_length() - 1
    for bit in range(n):
        for mask in range(N):
            if not (mask >> bit) & 1:
                cap[mask] += cap[mask | (1 << bit)]
    return sum(x * log2(cap[s] / x) for s, x in enumerate(p) if x)


def restrict(values, bit, value):
    return [
        values[x]
        for x in range(len(values))
        if ((x >> bit) & 1) == value
    ]


def influence(values):
    N = len(values)
    n = N.bit_length() - 1
    return sum(
        sum(values[x] != values[x ^ (1 << bit)] for x in range(N)) / N
        for bit in range(n)
    )


def aggregate_g(values):
    U = upper_u(values)
    n = len(values).bit_length() - 1
    return sum(
        U - (upper_u(restrict(values, bit, 0))
             + upper_u(restrict(values, bit, 1))) / 2
        for bit in range(n)
    )


def balance(values):
    return list(values) + [-x for x in values]


def activate(values):
    return [1] * len(values) + list(values)


def tower(base, depth):
    q = balance(base)
    for level in range(depth):
        f = activate(q)
        if level + 1 < depth:
            q = balance(f)
    return f


def xlog(x, y):
    return 0.0 if x == 0 else x * log2(y)


def phi(mu):
    """Exact scalar balancer charge, evaluated continuously."""
    rp = (1 + mu) ** 2 / 4
    rm = (1 - mu) ** 2 / 4
    u0 = 0.0 if mu == 0 else mu * mu * log2(1 / (mu * mu))
    plus = 0.0 if rp == 0 else rp * log2(2 / (1 + mu))
    minus = 0.0 if rm == 0 else rm * log2(2 / (1 - mu))
    endpoint = plus + minus
    return 0.75 + mu * mu / 4 + u0 / 2 - 1.5 * endpoint


phi_half = 7 / 8 - 27 / 32 * log2(4 / 3)
K_star = 15 / 4 - 27 / 16 * log2(4 / 3)
assert abs(phi(0.5) - phi_half) < 1e-15
assert 2 + 1 / (2 * e * log(2)) < K_star

rng = random.Random(20261013)
bases = []
for n in range(4):
    for truth in itertools.product((-1, 1), repeat=1 << n):
        bases.append(list(truth))
for n, count in ((4, 40), (5, 10)):
    for _ in range(count):
        bases.append([rng.choice((-1, 1)) for _ in range(1 << n)])

formula_checks = 0
transfer_checks = 0
max_formula_error = 0.0
max_transfer_slack = -1e100

for base in bases:
    G0 = aggregate_g(base)
    I0 = influence(base)
    mu = sum(base) / len(base)
    for depth in range(1, 5):
        f = tower(base, depth)
        G = aggregate_g(f)
        I = influence(f)
        predicted = (
            G0 / (1 << depth)
            + (1 + phi(mu)) / (1 << (depth - 1))
            + 2 * (1 - 1 / (1 << (depth - 1))) * (1 + phi_half)
        )
        err = abs(G - predicted)
        max_formula_error = max(max_formula_error, err)
        assert err < 4e-11
        formula_checks += 1

        # Each individual base has the valid b=0 coefficient a=G/I
        # (constants have G=I=0).  The theorem predicts a uniform additive
        # K_star under every tower depth.
        a = 0.0 if I0 == 0 else G0 / I0
        slack = (a + K_star) * I - G
        max_transfer_slack = max(max_transfer_slack, slack)
        assert slack > -4e-11
        transfer_checks += 1

print("B01 A003 parity-balanced GU transfer audit")
print(f"base_functions={len(bases)}")
print(f"formula_checks={formula_checks}")
print(f"gu_transfer_checks={transfer_checks}")
print(f"phi_half={phi_half:.15f}")
print(f"K_star={K_star:.15f}")
print(f"max_formula_error={max_formula_error:.3e}")
print("PASS_EXACT_RECURRENCE_AND_DEPTH_UNIFORM_TRANSFER")
