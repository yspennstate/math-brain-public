#!/usr/bin/env python3
"""Exact finite falsification check for B13 product-spectrum rigidity.

Enumerates Boolean functions modulo global sign through n=4, computes the
integer Walsh transform, tests mutual independence of spectral membership
with exact Fraction arithmetic, and checks that every marginal of every
product-spectrum example lies in {0, 1/2, 1}.

This is only a finite self-check. The all-dimensional theorem is proved in
REPORT.md and does not depend on this enumeration.
"""
from collections import Counter
from fractions import Fraction
import json


def walsh_int(values):
    a = list(values)
    h = 1
    while h < len(a):
        for base in range(0, len(a), 2 * h):
            for j in range(base, base + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def analyse(values, n):
    W = walsh_int(values)
    den = 4 ** n
    probs = [Fraction(w * w, den) for w in W]
    marg = [
        sum((probs[m] for m in range(1 << n) if (m >> i) & 1), Fraction(0))
        for i in range(n)
    ]
    for mask, p in enumerate(probs):
        q = Fraction(1)
        for i, pi in enumerate(marg):
            q *= pi if ((mask >> i) & 1) else (1 - pi)
        if p != q:
            return False, marg
    return True, marg


def main():
    rows = []
    allowed = {Fraction(0), Fraction(1, 2), Fraction(1)}
    for n in range(1, 5):
        N = 1 << n
        product_count = 0
        patterns = Counter()
        half_counts = Counter()
        violations = 0
        # Fix f at the all-zero-index truth-table point to -1; this quotients
        # by global sign, which leaves squared Fourier coefficients unchanged.
        for bits in range(1 << (N - 1)):
            values = [-1] + [
                1 if (bits >> (j - 1)) & 1 else -1 for j in range(1, N)
            ]
            product, marg = analyse(values, n)
            if not product:
                continue
            product_count += 1
            patterns[tuple(marg)] += 1
            half_counts[sum(p == Fraction(1, 2) for p in marg)] += 1
            if any(p not in allowed for p in marg):
                violations += 1
        rows.append({
            "n": n,
            "product_spectrum_functions_mod_global_sign": product_count,
            "distinct_marginal_patterns": len(patterns),
            "count_by_number_of_half_marginals": {
                str(k): half_counts[k] for k in sorted(half_counts)
            },
            "violations_of_0_half_1_marginal_claim": violations,
        })
    result = {
        "status": "PASS_SELF_CHECK_ONLY",
        "arithmetic": "exact Python integers and fractions",
        "scope": "all Boolean truth tables modulo global sign for n<=4",
        "rows": rows,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    assert all(r["violations_of_0_half_1_marginal_claim"] == 0 for r in rows)


if __name__ == "__main__":
    main()
