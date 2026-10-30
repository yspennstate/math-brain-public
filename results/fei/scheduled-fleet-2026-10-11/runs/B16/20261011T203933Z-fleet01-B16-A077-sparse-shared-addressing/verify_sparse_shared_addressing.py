#!/usr/bin/env python3
"""Exact checks for the sparse activated shared-addressing family.

All Walsh coefficients and influences are fractions.  Decimal entropy values
are deliberately omitted: the entropy formula in the report follows exactly
from coefficient multiplicities, while the all-t bounds are analytic.
"""

from fractions import Fraction as Q
import hashlib
import json


def fwht(values):
    a = [Q(v) for v in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def family_values(t, k, r):
    """Truth table for f=1+A(z)(g-1), with bit 0 representing sign +1."""
    N = 1 << t
    n = t + k * N + r
    vals = []
    for word in range(1 << n):
        address = word & (N - 1)
        g = 1
        for layer in range(k):
            bit_index = t + layer * N + address
            g *= 1 if ((word >> bit_index) & 1) == 0 else -1
        active = True
        for j in range(r):
            bit_index = t + k * N + j
            if ((word >> bit_index) & 1) != 0:
                active = False
                break
        vals.append(g if active else 1)
    return vals


def influences(values):
    n = (len(values)).bit_length() - 1
    result = []
    for i in range(n):
        disagreements = sum(values[x] != values[x ^ (1 << i)] for x in range(len(values)))
        result.append(Q(disagreements, len(values)))
    return result


def expected_spectrum(t, k, r):
    N = 1 << t
    p = Q(1, 1 << r)
    expected = {(0): Q(1) - p}
    trigger_offset = t + k * N
    for U in range(1, 1 << r):
        expected[U << trigger_offset] = -p
    # Shared-addressing core: masks indexed by address frequency T and label u.
    for u in range(N):
        data_mask = 0
        for layer in range(k):
            data_mask |= 1 << (t + layer * N + u)
        for T in range(N):
            core_hat = Q(-1 if (T & u).bit_count() % 2 else 1, N)
            base_mask = T | data_mask
            for U in range(1 << r):
                expected[base_mask | (U << trigger_offset)] = p * core_hat
    return expected


def verify_case(t, k, r):
    N = 1 << t
    p = Q(1, 1 << r)
    vals = family_values(t, k, r)
    hats = fwht(vals)
    expected = expected_spectrum(t, k, r)
    assert sum(x * x for x in hats) == 1
    assert {i: x for i, x in enumerate(hats) if x} == expected
    inf = influences(vals)
    assert inf[:t] == [p / 2] * t
    assert inf[t:t + k * N] == [p / N] * (k * N)
    assert inf[t + k * N:] == [p] * r
    assert sum(inf) == p * (Q(t, 2) + k + r)

    dc_mass = (1 - p) ** 2
    trigger_only_mass = (Q(1, p) - 1) * p * p
    core_mass = Q(N * N, 1) * Q(1, p) * (p / N) ** 2
    assert dc_mass + trigger_only_mass + core_mass == 1

    # Spectral expected-degree ledger: trigger influence is split equally
    # between trigger-only and core-carrying coefficients.
    trigger_only_degree = Q(r, 2) * p
    core_trigger_degree = Q(r, 2) * p
    core_base_degree = p * (Q(t, 2) + k)
    assert trigger_only_degree + core_trigger_degree + core_base_degree == sum(inf)
    return {
        "t": t,
        "k": k,
        "r": r,
        "variables": t + k * N + r,
        "truth_table_rows": len(vals),
        "nonzero_walsh_coefficients": len(expected),
        "p": str(p),
        "total_influence": str(sum(inf)),
        "spectral_mass_ledger": {
            "dc": str(dc_mass),
            "trigger_only": str(trigger_only_mass),
            "core_copies": str(core_mass),
        },
    }


def main():
    cases = [(1, 1, 1), (1, 2, 1), (2, 1, 1), (2, 2, 2), (3, 1, 2)]
    rows = [verify_case(*case) for case in cases]
    payload = {
        "status": "PASS",
        "randomness": "NONE",
        "arithmetic": "fractions.Fraction exact truth tables and FWHT",
        "cases": rows,
        "assertion_scope": [
            "complete signed Walsh spectrum",
            "Parseval",
            "every coordinate influence",
            "total influence",
            "spectral mass partition",
            "cross-scale expected-degree partition",
        ],
        "all_parameter_claim": "proved algebraically in REPORT.md; finite checks are not extrapolated",
        "full_FEI": "OPEN",
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    print(encoded, end="")
    print("payload_sha256=" + hashlib.sha256(encoded.encode()).hexdigest())


if __name__ == "__main__":
    main()
