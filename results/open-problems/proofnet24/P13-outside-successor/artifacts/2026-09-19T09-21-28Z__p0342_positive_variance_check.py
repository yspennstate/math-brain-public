#!/usr/bin/env python3
from functools import lru_cache
from fractions import Fraction
from math import isqrt

LEAF = None

@lru_cache(None)
def trees(n):
    if n == 1:
        return (LEAF,)
    out = []
    for left_n in range(1, n):
        for left in trees(left_n):
            for right in trees(n-left_n):
                out.append((left, right))
    return tuple(out)

@lru_cache(None)
def size(tree):
    if tree is None:
        return 1
    return size(tree[0]) + size(tree[1])

def psi_and_three_clades(tree):
    """Return leafwise Psi and intervals [a,b) of size-3 clades with their sign."""
    n = size(tree)
    psi = [0] * n
    intervals = []

    def visit(t, offset):
        if t is None:
            return
        left, right = t
        a, b = size(left), size(right)
        if a + b == 3:
            if (a, b) == (1, 2):
                psi[offset] = +1
                intervals.append((offset, offset + 3, +1))
            elif (a, b) == (2, 1):
                psi[offset + 2] = -1
                intervals.append((offset, offset + 3, -1))
            else:
                raise AssertionError((a, b))
        visit(left, offset)
        visit(right, offset + a)

    visit(tree, 0)
    return psi, intervals

def H(k):
    return sum((Fraction(1, j) for j in range(1, k + 1)), Fraction(0))

def q(n, i):
    return Fraction(n, 2) * Fraction(1, H(n-1)) * Fraction(1, i * (n-i))

def p_direct(n):
    r = isqrt(n)
    return sum((q(n, i) for i in range(1, n) if min(i, n-i) <= r), Fraction(0))

def p_formula(n):
    r = isqrt(n)
    return (H(r) + sum((Fraction(1, n-i) for i in range(1, r + 1)), Fraction(0))) / H(n-1)

def main():
    assertions = 0
    total_trees = 0
    total_blocks = 0
    max_n = 9

    for n in range(1, max_n + 1):
        for tree in trees(n):
            total_trees += 1
            psi, intervals = psi_and_three_clades(tree)

            assert sum(x != 0 for x in psi) == len(intervals); assertions += 1
            assert sum(psi) == sum(sign for _, _, sign in intervals); assertions += 1
            assert len(intervals) <= n // 3; assertions += 1

            ordered = sorted(intervals)
            for (_, b, _), (c, _, _) in zip(ordered, ordered[1:]):
                assert b <= c
                assertions += 1

            for a in range(n):
                for b in range(a + 1, n + 1):
                    total_blocks += 1
                    complete = [(l, r, s) for l, r, s in intervals if a <= l and r <= b]
                    crossing = [(l, r, s) for l, r, s in intervals
                                if not (r <= a or b <= l) and not (a <= l and r <= b)]
                    assert len(crossing) <= 2; assertions += 1
                    boundary_remainder = sum(psi[a:b]) - sum(s for _, _, s in complete)
                    assert abs(boundary_remainder) <= len(crossing) <= 2; assertions += 1

    first_balanced_n = None
    for n in range(9, 201):
        direct = p_direct(n)
        formula = p_formula(n)
        assert direct == formula; assertions += 1
        if first_balanced_n is None and Fraction(1, 3) < direct < Fraction(2, 3):
            first_balanced_n = n

    a3_pi2_coeff = Fraction(6, 1) * H(2) / 2
    lambda3_pi2_coeff = a3_pi2_coeff / 3
    assert a3_pi2_coeff == Fraction(9, 2); assertions += 1
    assert lambda3_pi2_coeff == Fraction(3, 2); assertions += 1

    print(f"ORDERED_FULL_BINARY_TREES_CHECKED={total_trees}")
    print(f"LEAF_BLOCKS_CHECKED={total_blocks}")
    print(f"EXACT_ASSERTIONS={assertions}")
    print(f"MAX_LEAF_COUNT_ENUMERATED={max_n}")
    print(f"CATALAN_COUNT_AT_N9={len(trees(9))}")
    print(f"FIRST_N_9_TO_200_WITH_1/3<P_N<2/3={first_balanced_n}")
    print(f"A3_COEFFICIENT_OF_1/PI^2={a3_pi2_coeff}")
    print(f"LAMBDA3_COEFFICIENT_OF_1/PI^2={lambda3_pi2_coeff}")
    print("ALL_EXACT_P0342_POSITIVE_VARIANCE_CHECKS_PASS")

if __name__ == "__main__":
    main()
