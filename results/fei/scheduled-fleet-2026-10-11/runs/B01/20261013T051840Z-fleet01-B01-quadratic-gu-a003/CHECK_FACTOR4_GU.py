#!/usr/bin/env python3
"""Exact exhaustive GU' certificate through four Boolean variables."""

from fractions import Fraction
from CHECK_FACTOR3_GU import (
    add_vec, gu_vector, influence, scale_vec, sign_log_vector,
    upper_entropy_vector,
)


def main():
    a4 = {2: Fraction(11, 4)}  # 11/4 exactly
    strict = equal = constants = 0
    equality_masks = []
    n = 4
    size = 1 << n
    for mask in range(1 << (size - 1)):
        truth = tuple(-1 if (mask >> x) & 1 else 1 for x in range(size))
        inf = influence(truth)
        if inf == 0:
            constants += 1
            continue
        deficit = add_vec(scale_vec(a4, inf), gu_vector(truth), Fraction(-1))
        sign, _, _, _ = sign_log_vector(deficit)
        assert sign >= 0, (n, mask, deficit)
        if sign == 0:
            equal += 1
            equality_masks.append(mask)
        else:
            strict += 1

    witness_mask = 6014
    witness = tuple(-1 if (witness_mask >> x) & 1 else 1 for x in range(size))
    assert upper_entropy_vector(witness) == {2: Fraction(2)}
    assert gu_vector(witness) == {2: Fraction(11, 2)}
    assert influence(witness) == Fraction(2)
    assert add_vec(scale_vec(a4, Fraction(2)), gu_vector(witness), Fraction(-1)) == {}

    print("class=finitely_many_disjoint_factors_each_of_arity_at_most_4")
    print("n4_output_complement_representatives=32768")
    print(f"n4_nonconstant_strict={strict}")
    print(f"n4_nonconstant_equal={equal}")
    print(f"n4_constants={constants}")
    print("sharp_a4=11/4")
    print("mask6014_U=2")
    print("mask6014_G=11/2")
    print("mask6014_I=2")
    print("equality_masks=" + repr(equality_masks))
    print("all_signs=EXACT_INTEGER_PRODUCT_COMPARISONS")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
