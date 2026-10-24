#!/usr/bin/env python3
"""Independent truth-table reconstruction of B05/A025's overlap family."""

from fractions import Fraction
from itertools import product
from math import comb, log, log2


def phi(t: float) -> float:
    if t == 0:
        return 0.0
    return 2 * t * t * (log2(1 / t) + 1 / log(2))


def majority(u):
    return 1 if sum(u) > 0 else -1


def event(v):
    return all(z == 1 for z in v)


def vals(r, m):
    n = 2 * m + 1
    out_f, out_g, out_h = {}, {}, {}
    for x in (-1, 1):
        for u in product((-1, 1), repeat=n):
            k = majority(u)
            for v in product((-1, 1), repeat=r):
                g = x if event(v) else 1
                key = (x,) + u + v
                out_f[key] = x * k
                out_g[key] = g
                out_h[key] = x * k * g
    return out_f, out_g, out_h


def coeff(table, coordinates):
    total = 0
    for z, value in table.items():
        character = 1
        for i in coordinates:
            character *= z[i]
        total += value * character
    return Fraction(total, len(table))


def influence(table, i):
    changed = 0
    for z, value in table.items():
        w = list(z)
        w[i] *= -1
        changed += value != table[tuple(w)]
    return Fraction(changed, len(table))


def singleton_phi(table):
    return sum(phi(abs(float(coeff(table, (i,))))) for i in range(len(next(iter(table)))))


checks = 0
for r in range(1, 4):
    eps = Fraction(1, 2**r)
    for m in range(1, 4):
        n = 2 * m + 1
        c = Fraction(comb(2 * m, m), 4**m)
        f, g, h = vals(r, m)

        # Exact singleton spectra.
        assert all(coeff(f, (i,)) == 0 for i in range(1 + n + r))
        assert abs(coeff(g, (0,))) == eps
        assert all(abs(coeff(g, (1 + n + j,))) == eps for j in range(r))
        assert all(abs(coeff(h, (1 + i,))) == eps * c for i in range(n))
        assert coeff(h, (0,)) == 0
        assert all(coeff(h, (1 + n + j,)) == 0 for j in range(r))

        # Exact physical influence ledger.
        assert influence(f, 0) == 1
        assert influence(g, 0) == eps
        assert influence(h, 0) == 1 - eps
        assert sum(influence(g, i) for i in range(1 + n + r)) == (r + 1) * eps

        # Potential formulas reconstructed from truth tables.
        assert abs(singleton_phi(f)) < 1e-14
        assert abs(singleton_phi(g) - (r + 1) * phi(float(eps))) < 1e-12
        assert abs(singleton_phi(h) - n * phi(float(eps * c))) < 1e-12

        # x-first restrictions: K and K(2*1_E-1).
        child_plus = {z[1:]: value for z, value in h.items() if z[0] == 1}
        child_minus = {z[1:]: value for z, value in h.items() if z[0] == -1}
        expected_x_first = 0.5 * n * (phi(float(c)) + phi(float((1 - 2 * eps) * c)))
        assert abs(0.5 * (singleton_phi(child_plus) + singleton_phi(child_minus)) - expected_x_first) < 1e-12

        # Controls-first restrictions: one K leaf and 2^r-1 copies of xK.
        control_children = []
        for fixed_v in product((-1, 1), repeat=r):
            child = {z[: 1 + n]: value for z, value in h.items() if z[1 + n :] == fixed_v}
            control_children.append(singleton_phi(child))
        assert abs(sum(control_children) / (2**r) - float(eps) * n * phi(float(c))) < 1e-12

        # After both x and v are fixed, every remaining function is +/-K.
        terminal = []
        for fixed_x in (-1, 1):
            for fixed_v in product((-1, 1), repeat=r):
                leaf = {
                    z[1 : 1 + n]: value
                    for z, value in h.items()
                    if z[0] == fixed_x and z[1 + n :] == fixed_v
                }
                terminal.append(singleton_phi(leaf))
        assert all(abs(q - n * phi(float(c))) < 1e-12 for q in terminal)
        checks += 1

# Exact squared forms of the two central-binomial inequalities.
for m in range(1, 501):
    c = Fraction(comb(2 * m, m), 4**m)
    assert 4 * m * c * c >= 1
    assert (m + 1) * c * c <= 1
    checks += 2

print(f"direct truth-table parameter pairs: {9}")
print(f"exact central-binomial inequalities: {1000}")
print(f"total grouped checks: {checks}")
print("PASS: independent Fourier, influence, potential, and both reveal-order ledgers agree.")
