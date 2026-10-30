#!/usr/bin/env python3
"""Independent exact review of B06-A027-MODULATION-BLOCK-HIERARCHY-v1.

All asserted Fourier coefficients, probability laws, influences, physical
children, and sequential restriction ledgers use fractions.Fraction.
Floating point is used only for a displayed point-defect ratio diagnostic.
"""

from fractions import Fraction as Q
from itertools import product
from math import log2


def fwht(values):
    out = list(values)
    step = 1
    while step < len(out):
        for start in range(0, len(out), 2 * step):
            for j in range(start, start + step):
                a, b = out[j], out[j + step]
                out[j], out[j + step] = a + b, a - b
        step *= 2
    return out


def fourier(values):
    n = len(values)
    return [Q(a, n) for a in fwht(values)]


def spectral_law(values):
    return [a * a for a in fourier(values)]


def influence(law):
    return sum(p * mask.bit_count() for mask, p in enumerate(law))


def direct_coordinate_influence(values, bit):
    return Q(sum(values[x] != values[x ^ (1 << bit)]
                 for x in range(len(values))), len(values))


def boolean_tables(n):
    for code in range(1 << (1 << n)):
        yield [1 if (code >> x) & 1 else -1 for x in range(1 << n)]


def sign(bit):
    return 1 if bit == 0 else -1


def multiply(items):
    value = 1
    for item in items:
        value *= item
    return value


def auxiliary_product(hs, subset, m):
    return [
        multiply(hs[i][z] for i in range(len(hs)) if (subset >> i) & 1)
        for z in range(1 << m)
    ]


def modulation(g, n, hs, m):
    values = []
    for state in range(1 << (n + m)):
        x = state & ((1 << n) - 1)
        z = state >> n
        input_index = 0
        for i in range(n):
            if sign((x >> i) & 1) * hs[i][z] == -1:
                input_index |= 1 << i
        values.append(g[input_index])
    return values


def restrict(values, nvars, fixed):
    free = [i for i in range(nvars) if i not in fixed]
    out = []
    for state in range(1 << len(free)):
        full = 0
        for i, bit in fixed.items():
            full |= bit << i
        for j, i in enumerate(free):
            full |= ((state >> j) & 1) << i
        out.append(values[full])
    return out


assertions = 0
one_step_cases = 0


def review_one_step(g, n, hs, m):
    global assertions, one_step_cases
    F = modulation(g, n, hs, m)
    cg, cF = fourier(g), fourier(F)
    mu, lawF = spectral_law(g), spectral_law(F)
    aux_coefficients = []
    aux_laws = []

    for S in range(1 << n):
        hS = auxiliary_product(hs, S, m)
        aux_coefficients.append(fourier(hS))
        aux_laws.append(spectral_law(hS))

    # Independent reconstruction of the coefficient and squared-law products.
    for S in range(1 << n):
        for T in range(1 << m):
            index = S | (T << n)
            assert cF[index] == cg[S] * aux_coefficients[S][T]
            assert lawF[index] == mu[S] * aux_laws[S][T]
            assertions += 2

    # Parseval and the X/Z influence split.
    assert sum(mu) == 1 and sum(lawF) == 1
    ix = sum(p * (mask & ((1 << n) - 1)).bit_count()
             for mask, p in enumerate(lawF))
    iz = sum(p * (mask >> n).bit_count()
             for mask, p in enumerate(lawF))
    assert ix == influence(mu)
    assert iz == sum(mu[S] * influence(aux_laws[S])
                     for S in range(1 << n))
    assertions += 4

    # Every physical Z-child has exactly the base squared spectrum.
    for z in range(1 << m):
        child = [F[x | (z << n)] for x in range(1 << n)]
        assert spectral_law(child) == mu
        assertions += 1

    # The sequential physical query ledger charges every Z edge once.
    queried = Q(0)
    for j in range(m):
        for prefix in range(1 << j):
            node = restrict(
                F, n + m,
                {n + r: (prefix >> r) & 1 for r in range(j)}
            )
            queried += Q(1, 1 << j) * direct_coordinate_influence(node, n)
    assert queried == iz
    assertions += 1
    one_step_cases += 1
    return F


# Exhaustive nonlinear one-step review on two complementary finite domains.
for g in boolean_tables(2):
    pool = list(boolean_tables(2))
    for hs in product(pool, repeat=2):
        review_one_step(g, 2, hs, 2)

for g in boolean_tables(3):
    pool = list(boolean_tables(1))
    for hs in product(pool, repeat=3):
        review_one_step(g, 3, hs, 1)


# Two-level hierarchy: independently check that querying newest then oldest
# ends in a sign-flipped base and that the two queried ledgers partition all
# auxiliary influence.
hierarchy_cases = 0
for g0 in boolean_tables(1):
    for h1 in boolean_tables(1):
        f1 = modulation(g0, 1, [h1], 1)
        for hs2 in product(list(boolean_tables(1)), repeat=2):
            f2 = modulation(f1, 2, hs2, 1)
            target = spectral_law(g0)
            for z2 in range(2):
                child1 = [f2[u | (z2 << 2)] for u in range(4)]
                for z1 in range(2):
                    child0 = [child1[x | (z1 << 1)] for x in range(2)]
                    assert spectral_law(child0) == target
                    assertions += 1
            assert influence(spectral_law(f2)) >= influence(spectral_law(f1))
            assert influence(spectral_law(f1)) >= influence(target)
            assertions += 2
            hierarchy_cases += 1


# Exact point-defect Fourier law and influence formulas.
point_defect_cases = 0
max_ratio = (0.0, None)
for m in range(1, 17):
    N = 1 << m
    q = [-1] + [1] * (N - 1)
    law = spectral_law(q)
    assert law[0] == Q((N - 2) ** 2, N ** 2)
    assert all(law[S] == Q(4, N ** 2) for S in range(1, N))
    assert influence(law) == Q(2 * m, N)
    assertions += N + 1
    delta = Q(4 * (N - 1), N ** 2)
    if m == 1:
        H = 0.0
    else:
        d = float(delta)
        H = -d * log2(d) - (1 - d) * log2(1 - d)
        H += d * log2(N - 1)
    ratio = H / float(Q(2 * m, N))
    assert ratio <= 4.5 + 1e-12
    assertions += 1
    if ratio > max_ratio[0]:
        max_ratio = (ratio, m)
    point_defect_cases += 1


print("status PASS")
print("randomness NONE")
print("one_step_cases", one_step_cases)
print("hierarchy_cases", hierarchy_cases)
print("point_defect_cases", point_defect_cases)
print("assertions", assertions)
print("largest_checked_point_defect_ratio", max_ratio)
print("exact_scope Fourier laws, physical children, influences, sequential ledgers")
print("float_scope displayed finite point-defect ratio diagnostic only")
print("full_FEI OPEN")
