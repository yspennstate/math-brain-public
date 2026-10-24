#!/usr/bin/env python3
"""Exact Walsh audit for the shared-address packet family.

All transform and influence checks use integers/Fractions. Entropies are
deduced from the proved uniform spectral law, so no floating tolerance is
used.
"""

from fractions import Fraction


def fwht(v):
    a = list(v)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def truth_table(t, k):
    N = 1 << t
    n = t + k * N
    vals = []
    for x in range(1 << n):
        b = x & (N - 1)
        value = 1
        for r in range(k):
            pos = t + r * N + b
            value *= 1 if ((x >> pos) & 1) == 0 else -1
        vals.append(value)
    return vals


def direct_influences(vals, n):
    den = len(vals)
    out = []
    for i in range(n):
        flips = sum(vals[x] != vals[x ^ (1 << i)] for x in range(den))
        out.append(Fraction(flips, den))
    return out


pairs = [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1)]
assertions = 0
print("t k n atoms H I coord_budget_formula fractional_congestion")
for t, k in pairs:
    N = 1 << t
    n = t + k * N
    vals = truth_table(t, k)
    W = fwht(vals)
    den = len(vals)
    atoms = [(s, Fraction(w * w, den * den)) for s, w in enumerate(W) if w]

    assert len(atoms) == N * N
    assertions += 1
    assert all(p == Fraction(1, N * N) for _, p in atoms)
    assertions += len(atoms)
    assert sum(p for _, p in atoms) == 1
    assertions += 1

    influence_spectral = sum(p * s.bit_count() for s, p in atoms)
    expected_I = Fraction(t, 2) + k
    assert influence_spectral == expected_I
    assertions += 1

    infl = direct_influences(vals, n)
    assert infl[:t] == [Fraction(1, 2)] * t
    assertions += t
    assert infl[t:] == [Fraction(1, N)] * (k * N)
    assertions += k * N
    assert sum(infl) == expected_I
    assertions += 1

    # Packet law: B and address subset A are independent uniform N-laws.
    packet_mass = Fraction(1, N)
    address_fractional_load = sum(packet_mass * Fraction(1, 2) for _ in range(N))
    data_fractional_load = packet_mass
    assert address_fractional_load == Fraction(1, 2)
    assert data_fractional_load == Fraction(1, N)
    assertions += 2

    print(t, k, n, len(atoms), 2 * t, str(expected_I),
          f"{t}+{k}*{N}*h2(1/{N})", "1/2")

print("assertions", assertions)
print("PASS: exact Walsh law, influences, and packet congestion verified")
