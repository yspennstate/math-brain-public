#!/usr/bin/env python3
"""Exhaustive checks for the one-shared-coordinate block-potential lemma."""

from itertools import product
from math import log
from random import Random

LN2 = log(2.0)


def q(y):
    if y == 0:
        return 0.0
    return (-y * log(y) + 2.0 * y) / LN2


def all_tables(dim):
    points = list(product((-1, 1), repeat=dim))
    for values in product((-1, 1), repeat=len(points)):
        yield dict(zip(points, values))


def random_table(dim, rng):
    return {z: rng.choice((-1, 1)) for z in product((-1, 1), repeat=dim)}


def coeff(table, subset):
    total = 0
    for z, value in table.items():
        chi = 1
        for i in subset:
            chi *= z[i]
        total += value * chi
    return total / len(table)


def phi(table):
    dim = len(next(iter(table)))
    return sum(q(coeff(table, (i,)) ** 2) for i in range(dim))


def block_potential(table):
    # Shared coordinate is index 0.
    dim = len(next(iter(table)))
    mean = coeff(table, ())
    dx = coeff(table, (0,))
    ans = q(mean * mean + dx * dx)
    for i in range(1, dim):
        a = coeff(table, (i,))
        ax = coeff(table, (0, i))
        ans += q(a * a + ax * ax)
    return ans


def multiply_shared(f, g):
    # f=(x,u), g=(x,v), output=(x,u,v).
    du = len(next(iter(f))) - 1
    dv = len(next(iter(g))) - 1
    h = {}
    for x in (-1, 1):
        for u in product((-1, 1), repeat=du):
            for v in product((-1, 1), repeat=dv):
                h[(x,) + u + v] = f[(x,) + u] * g[(x,) + v]
    return h


def restriction_average_phi(table):
    plus = {z[1:]: value for z, value in table.items() if z[0] == 1}
    minus = {z[1:]: value for z, value in table.items() if z[0] == -1}
    return 0.5 * (phi(plus) + phi(minus))


max_product_slack = -1e100
max_restriction_slack = -1e100
exhaustive_pairs = 0
restriction_checks = 0

# Every f on (x,u1,u2) and every g on (x,v1): 256*16=4096 pairs.
small_f = list(all_tables(3))
small_g = list(all_tables(2))
for f in small_f:
    lf = block_potential(f)
    ravg = restriction_average_phi(f)
    assert ravg <= lf + 1e-12
    max_restriction_slack = max(max_restriction_slack, ravg - lf)
    restriction_checks += 1
    for g in small_g:
        h = multiply_shared(f, g)
        slack = phi(h) - lf - block_potential(g)
        assert slack <= 1e-12
        max_product_slack = max(max_product_slack, slack)
        exhaustive_pairs += 1

# Larger random pairs on (x,u1,u2) and (x,v1,v2).
rng = Random(20261014)
random_pairs = 10000
for _ in range(random_pairs):
    f = random_table(3, rng)
    g = random_table(3, rng)
    h = multiply_shared(f, g)
    slack = phi(h) - block_potential(f) - block_potential(g)
    assert slack <= 1e-12
    max_product_slack = max(max_product_slack, slack)
    for table in (f, g):
        rslack = restriction_average_phi(table) - block_potential(table)
        assert rslack <= 1e-12
        max_restriction_slack = max(max_restriction_slack, rslack)
        restriction_checks += 1

# Scalar concavity/Jensen check over a fine deterministic grid.
scalar_checks = 0
for ia in range(-200, 201):
    a = ia / 400.0
    for ib in range(-200, 201):
        b = ib / 400.0
        if abs(a + b) <= 1 and abs(a - b) <= 1:
            lhs = 0.5 * (q((a + b) ** 2) + q((a - b) ** 2))
            rhs = q(a * a + b * b)
            assert lhs <= rhs + 2e-12
            scalar_checks += 1

print(f"exhaustive shared-product pairs: {exhaustive_pairs}")
print(f"random larger shared-product pairs: {random_pairs}")
print(f"physical-restriction checks: {restriction_checks}")
print(f"scalar Jensen checks: {scalar_checks}")
print(f"maximum product slack: {max_product_slack:.3e}")
print(f"maximum restriction slack: {max_restriction_slack:.3e}")
print("PASS: one-shared-coordinate block-potential inequalities hold.")
