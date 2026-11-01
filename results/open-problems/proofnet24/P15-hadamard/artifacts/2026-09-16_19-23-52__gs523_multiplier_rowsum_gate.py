#!/usr/bin/env python3
"""Exact row-sum feasibility gate for multiplier-invariant 4-circulant GS at 523.

If four ±1 circulant first rows on Z_523 are invariant under a multiplicative
subgroup K <= F_523^* of order d, then the nonzero entries split into 522/d
orbits of size d. Their row sums lie in an explicit finite set. The aggregate
PAF condition needed by a Goethals-Seidel four-circulant construction implies
that the four squared row sums add to 4*523. This script enumerates exactly
which subgroup orders survive that necessary condition.

Restricted-route filter only; it is not a nonexistence test for H(2092).
"""
from itertools import combinations_with_replacement

P = 523
N = P - 1
TARGET = 4 * P


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def possible_rowsums(d):
    m = N // d
    vals = set()
    for eps0 in (-1, 1):
        for k in range(m + 1):
            z = m - 2 * k  # sum of m orbit signs
            vals.add(eps0 + d * z)
    return sorted(vals)


survivors = []
for d in divisors(N):
    vals = possible_rowsums(d)
    bounded = sorted({abs(r) for r in vals if r * r <= TARGET})
    profiles = [q for q in combinations_with_replacement(bounded, 4)
                if sum(x*x for x in q) == TARGET]
    if profiles:
        survivors.append(d)
    print(f"d={d} orbit_count={N//d} bounded_abs_rows={bounded} profile_count={len(profiles)}")
    if d in (3, 6, 9):
        print("  profiles=" + ";".join(",".join(map(str, q)) for q in profiles))

assert survivors == [1, 2, 3, 6, 9]
print("surviving_subgroup_orders=" + ",".join(map(str, survivors)))
print("surviving_nontrivial_orders=2,3,6,9")
print("largest_surviving_nontrivial_order=9")
print("EXACT_GS523_ROWSUM_GATE_PASS")
print("SCOPE: necessary row-sum gate for multiplier-invariant 4-circulant GS families only; unrestricted H(2092) remains open.")
