#!/usr/bin/env python3
"""Exact exhaustive verification of the linear-parity padding identities.

Scope: every Boolean core on n <= 3 variables and every ordered list of
linear labels c_i in F_2^m for m <= 2.  All Walsh coefficients and influences
are computed with fractions.  Entropy equality is certified by equality of
the positive spectral-mass multisets, so no floating logarithms are used.
"""

from fractions import Fraction
from itertools import product, combinations
import json


def parity(x: int) -> int:
    return x.bit_count() & 1


def walsh(values, dim):
    den = 1 << dim
    return [Fraction(sum(v * (-1 if parity(mask & x) else 1)
                         for x, v in enumerate(values)), den)
            for mask in range(1 << dim)]


def masses(values, dim):
    return [a * a for a in walsh(values, dim)]


def positive_signature(ms):
    return sorted(q for q in ms if q)


def influence(ms, dim, coordinate_mask=None):
    if coordinate_mask is None:
        coordinate_mask = (1 << dim) - 1
    return sum(q * ((s & coordinate_mask).bit_count())
               for s, q in enumerate(ms))


def evaluate_lift(core, n, labels, m):
    out = []
    for state in range(1 << (n + m)):
        x = state & ((1 << n) - 1)
        z = state >> n
        transformed = 0
        for i, label in enumerate(labels):
            bit = ((x >> i) & 1) ^ parity(label & z)
            transformed |= bit << i
        out.append(core[transformed])
    return out


def restrict_padding(values, n, m, chosen, assignment):
    chosen = tuple(chosen)
    remaining = tuple(j for j in range(m) if j not in chosen)
    out = []
    for state in range(1 << (n + len(remaining))):
        x = state & ((1 << n) - 1)
        rz = state >> n
        z = 0
        for k, j in enumerate(chosen):
            z |= ((assignment >> k) & 1) << j
        for k, j in enumerate(remaining):
            z |= ((rz >> k) & 1) << j
        out.append(values[x | (z << n)])
    return out


def main():
    assertions = 0
    instances = 0
    restriction_instances = 0
    nontrivial_padding_instances = 0
    for n in range(1, 4):
        for m in range(1, 3):
            for truth_bits in range(1 << (1 << n)):
                core = [1 if ((truth_bits >> x) & 1) == 0 else -1
                        for x in range(1 << n)]
                core_hat = walsh(core, n)
                core_ms = [a * a for a in core_hat]
                for labels in product(range(1 << m), repeat=n):
                    instances += 1
                    lifted = evaluate_lift(core, n, labels, m)
                    lift_hat = walsh(lifted, n + m)
                    expected = [Fraction(0) for _ in lift_hat]
                    label_of_s = []
                    for s, a in enumerate(core_hat):
                        t = 0
                        for i, label in enumerate(labels):
                            if (s >> i) & 1:
                                t ^= label
                        label_of_s.append(t)
                        expected[s | (t << n)] = a
                    assert lift_hat == expected
                    assertions += 1

                    lift_ms = [a * a for a in lift_hat]
                    assert positive_signature(lift_ms) == positive_signature(core_ms)
                    assertions += 1

                    added = sum(core_ms[s] * label_of_s[s].bit_count()
                                for s in range(1 << n))
                    assert influence(lift_ms, n + m) == influence(core_ms, n) + added
                    assertions += 1

                    pad_mask = ((1 << m) - 1) << n
                    assert influence(lift_ms, n + m, pad_mask) == added
                    assertions += 1
                    if added:
                        nontrivial_padding_instances += 1

                    for size in range(1, m + 1):
                        for chosen in combinations(range(m), size):
                            for assignment in range(1 << size):
                                child = restrict_padding(lifted, n, m, chosen, assignment)
                                child_ms = masses(child, n + m - size)
                                assert positive_signature(child_ms) == positive_signature(core_ms)
                                assertions += 1
                                restriction_instances += 1

    result = {
        "status": "PASS",
        "arithmetic": "exact rational Walsh; entropy via positive-mass multiset equality",
        "dimensions": {"core_n": [1, 2, 3], "padding_m": [1, 2]},
        "instances": instances,
        "nontrivial_padding_instances": nontrivial_padding_instances,
        "physical_restriction_instances": restriction_instances,
        "assertions": assertions,
        "seed": None,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
