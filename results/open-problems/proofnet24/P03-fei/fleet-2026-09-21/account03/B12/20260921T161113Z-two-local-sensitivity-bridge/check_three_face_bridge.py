#!/usr/bin/env python3
"""Exact 3-face checker for the B12 FEI spectral/sensitivity bridge.

This is a finite local lemma checker, not an exhaustive FEI search.  It enumerates
the 256 Boolean functions on one 3-cube and verifies:

1. spectral and physical-sensitivity pair-inclusion probabilities agree for
   each of the three coordinate pairs;
2. with d = P({1,2,3} subset S_spec) - P({1,2,3} subset Sens(X)),
      |d| <= I_face / 6;
3. the sharp ratio is 1/6 and the signed defect distribution is recorded.

All comparisons use exact fractions / integers.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def stats(bits: int):
    vals = [1 if ((bits >> x) & 1) else -1 for x in range(8)]

    # Unnormalised Walsh coefficients c_A; hat f(A) = c_A / 8.
    c = []
    for mask in range(8):
        total = 0
        for x in range(8):
            parity = (x & mask).bit_count() & 1
            total += vals[x] * (-1 if parity else 1)
        c.append(total)
    p = [Fraction(z * z, 64) for z in c]

    # Physical sensitivity masks and number of undirected bichromatic edges.
    sens_masks = []
    boundary_edges = 0
    for x in range(8):
        mask = 0
        for i in range(3):
            y = x ^ (1 << i)
            if vals[x] != vals[y]:
                mask |= 1 << i
                if x < y:
                    boundary_edges += 1
        sens_masks.append(mask)

    for i, j in combinations(range(3), 2):
        q_spec = sum(
            p[m] for m in range(8)
            if ((m >> i) & 1) and ((m >> j) & 1)
        )
        q_sens = Fraction(
            sum(
                1 for m in sens_masks
                if ((m >> i) & 1) and ((m >> j) & 1)
            ),
            8,
        )
        assert q_spec == q_sens, (bits, i, j, q_spec, q_sens)

    q3_spec = p[7]
    q3_sens = Fraction(sum(1 for m in sens_masks if m == 7), 8)
    defect = q3_spec - q3_sens
    influence = Fraction(boundary_edges, 4)
    assert abs(defect) <= influence / 6, (bits, defect, influence)
    return defect, influence


def main():
    defects = Counter()
    sharp = Fraction(0)
    sharp_count = 0
    pair_checks = 0

    for bits in range(256):
        defect, influence = stats(bits)
        defects[defect] += 1
        pair_checks += 3
        if influence:
            ratio = abs(defect) / influence
            if ratio > sharp:
                sharp = ratio
                sharp_count = 1
            elif ratio == sharp:
                sharp_count += 1

    print("truth_tables=256")
    print(f"pair_inclusion_checks={pair_checks} all_passed=true")
    print("cubic_defect_bound_checks=256 all_passed=true")
    print(f"sharp_abs_defect_over_influence={sharp}")
    print(f"sharp_truth_tables={sharp_count}")
    print("signed_defect_counts=")
    for defect in sorted(defects):
        print(f"  {defect}: {defects[defect]}")

    # Named exact controls.
    majority_bits = 0
    onepoint_bits = 0
    parity_bits = 0
    # bit x is 1 iff the function value is +1.
    for x in range(8):
        ones = x.bit_count()
        # majority in the {0,1} convention: +1 on Hamming weight <= 1.
        if ones <= 1:
            majority_bits |= 1 << x
        # one-point defect: -1 only at x=0.
        if x != 0:
            onepoint_bits |= 1 << x
        # parity character: +1 on even Hamming weight.
        if ones % 2 == 0:
            parity_bits |= 1 << x

    for name, bits in [
        ("majority3", majority_bits),
        ("one_point3", onepoint_bits),
        ("parity3", parity_bits),
    ]:
        defect, influence = stats(bits)
        tv = 4 * abs(defect)
        print(
            f"control {name}: defect={defect} tv={tv} "
            f"influence={influence} two_thirds_I={Fraction(2,3)*influence}"
        )


if __name__ == "__main__":
    main()
