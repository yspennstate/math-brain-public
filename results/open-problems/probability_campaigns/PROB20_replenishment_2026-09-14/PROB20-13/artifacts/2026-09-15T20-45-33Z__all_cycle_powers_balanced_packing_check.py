#!/usr/bin/env python3
"""Exact checker for PROB20-13 balanced-packing theorem and cycle-power formula.

The theorem checked here is purely integral:
for every k>=1 and r>=k, there are S_k=k(k+1)/2 bins of sum r,
using r copies of each part size 1,...,k in total.

No floating-point arithmetic is used in the theorem checks.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from fractions import Fraction


def S(k: int) -> int:
    return k * (k + 1) // 2


@lru_cache(maxsize=None)
def balanced_bins(k: int, r: int) -> tuple[tuple[int, ...], ...]:
    assert k >= 1 and r >= k

    if k == 1:
        return (tuple([1] * r),)

    # Induction in r by concatenating a design of length r-k
    # with the exact base design of length k.
    if r >= 2 * k:
        left = balanced_bins(k, r - k)
        right = balanced_bins(k, k)
        assert len(left) == len(right) == S(k)
        return tuple(a + b for a, b in zip(left, right))

    # Base interval k <= r < 2k.
    t = r - k
    bins: list[tuple[int, ...]] = []

    if t == 0:
        # Complementary pairing s <-> k-s on 1,...,k-1,
        # plus singleton bins for size k.
        used: set[int] = set()
        for s in range(1, k):
            if s in used:
                continue
            u = k - s
            if u == s:
                assert k % 2 == 0
                for _ in range(k // 2):
                    bins.append((s, s))
                used.add(s)
            else:
                for _ in range(k):
                    bins.append((s, u))
                used.add(s)
                used.add(u)
        for _ in range(k):
            bins.append((k,))
        return tuple(bins)

    # Complementary pairing on the large interval t,...,k
    # under s <-> r-s.
    used: set[int] = set()
    for s in range(t, k + 1):
        if s in used:
            continue
        u = r - s
        assert t <= u <= k
        if u == s:
            assert r % 2 == 0
            for _ in range(r // 2):
                bins.append((s, s))
            used.add(s)
        else:
            for _ in range(r):
                bins.append((s, u))
            used.add(s)
            used.add(u)

    # Residual small sizes 1,...,t-1 are solved by the outer induction in k.
    if t >= 2:
        bins.extend(balanced_bins(t - 1, r))

    return tuple(bins)


def verify_design(k: int, r: int) -> None:
    bins = balanced_bins(k, r)
    assert len(bins) == S(k), (k, r, len(bins), S(k))

    counts: Counter[int] = Counter()
    for b in bins:
        assert sum(b) == r, (k, r, b)
        assert all(1 <= x <= k for x in b), (k, r, b)
        counts.update(b)

    for s in range(1, k + 1):
        assert counts[s] == r, (k, r, s, counts[s])


def cycle_mean_distance(n: int) -> Fraction:
    if n % 2 == 0:
        return Fraction(n, 4)
    return Fraction(n * n - 1, 4 * n)


def exact_F_cycle_power(n: int, k: int) -> Fraction:
    assert n >= 2 * k + 1
    return Fraction(4, k + 1) * cycle_mean_distance(n)


def diameter_cycle_power(n: int, k: int) -> int:
    R = n // 2
    return (R + k - 1) // k


def verify_cycle_target(n: int, k: int) -> None:
    assert n >= 2 * k + 1
    F = exact_F_cycle_power(n, k)

    if n == 2 * k + 1:
        # Complete graph K_n: tau_rel=(n-1)/n, D=1.
        rhs = 2 * Fraction(n - 1, n)
        assert F == rhs, (n, k, F, rhs)
    else:
        # Every connected noncomplete simple graph has tau_rel>=1,
        # so checking F<=2D is sufficient.
        D = diameter_cycle_power(n, k)
        assert F <= 2 * D, (n, k, F, D)


def main() -> None:
    # Broad exact-integer regression of the constructive theorem.
    for k in range(1, 31):
        for r in range(k, 201):
            verify_design(k, r)

    # Exact rational regression of the closed formula and the diameter comparison.
    for k in range(1, 31):
        for n in range(2 * k + 1, 8 * k + 40):
            verify_cycle_target(n, k)

    print("PASS: balanced packing for 1<=k<=30, k<=r<=200")
    print("PASS: exact cycle-power formula target checks on the tested grid")


if __name__ == "__main__":
    main()
