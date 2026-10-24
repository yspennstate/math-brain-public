#!/usr/bin/env python3
"""Exact row-sum obstruction for multiplier-invariant cyclic GS seeds at order 2092.

Target: a cyclic Goethals-Seidel seed consists of four +/-1 sequences of odd
length v=523 satisfying sum_i PAF_i(t)=4v delta_0.  At t=0 this forces the
four row sums r_i to satisfy sum_i r_i^2=4v.

If the -1 support of a sequence is invariant under a multiplicative subgroup
H <= (Z/523Z)^* of order h, then (523 is prime) the H-orbits are {0} and
nonzero orbits all of size h.  Thus |X| mod h is 0 or 1 and
r=523-2|X| is congruent to 523 or 521 modulo 2h.

This program enumerates every possible ordered odd row-sum quadruple exactly,
then applies that necessary orbit congruence for h=9,18,29.  It proves that
h=18 and h=29 admit no row-sum quadruple at all, while h=9 has examples,
which is a useful positive control.  This is only a restricted-family
nonexistence certificate; it says nothing about unrestricted H(2092).
"""
from itertools import product
from math import isqrt

V = 523
ORDER = 4 * V
SUBGROUP_ORDERS = (9, 18, 29)


def admissible_for_h(r, h):
    # For a +/-1 sequence of odd length V, k=(V-r)/2 is its number of -1's.
    k = (V - r) // 2
    return 0 <= k <= V and (k % h) in (0, 1)


def main():
    bound = isqrt(ORDER)
    row_sums = [r for r in range(-bound, bound + 1) if r & 1]
    total_four_square = 0
    counts = {h: 0 for h in SUBGROUP_ORDERS}
    examples = {}

    for rs in product(row_sums, repeat=4):
        if sum(r*r for r in rs) != ORDER:
            continue
        total_four_square += 1
        for h in SUBGROUP_ORDERS:
            if all(admissible_for_h(r, h) for r in rs):
                counts[h] += 1
                examples.setdefault(h, (rs, tuple((V-r)//2 for r in rs)))

    print(f"v={V} order={ORDER} row_sum_bound={bound}")
    print(f"ordered_four_square_row_sum_quadruples={total_four_square}")
    for h in SUBGROUP_ORDERS:
        print(f"subgroup_order={h} feasible_ordered_row_sum_quadruples={counts[h]}")
        if h in examples:
            rs, ks = examples[h]
            print(f"subgroup_order={h} example_row_sums={rs} example_support_sizes={ks}")

    assert total_four_square == 8384
    assert counts[9] == 256
    assert counts[18] == 0
    assert counts[29] == 0
    print("VERDICT: no order-18- or order-29-multiplier-invariant cyclic GS seed can satisfy the mandatory four-square row-sum condition for v=523")
    print("SCOPE: restricted multiplier-invariant cyclic GS families only; NOT nonexistence of H(2092)")


if __name__ == "__main__":
    main()
