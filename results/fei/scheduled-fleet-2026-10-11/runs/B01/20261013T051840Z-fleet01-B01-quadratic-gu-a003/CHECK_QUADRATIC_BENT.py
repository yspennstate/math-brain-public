#!/usr/bin/env python3
"""Exact checks for the quadratic-bent GU formula."""

from fractions import Fraction
from CHECK_FACTOR3_GU import gu_vector, influence, upper_entropy_vector


def matrix_from_mask(n, mask):
    rows = [0] * n
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> k) & 1:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
            k += 1
    return rows


def inverse_rows(rows, n):
    work = [rows[i] | (1 << (n + i)) for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if (work[r] >> col) & 1), None)
        if pivot is None:
            return None
        work[col], work[pivot] = work[pivot], work[col]
        for r in range(n):
            if r != col and ((work[r] >> col) & 1):
                work[r] ^= work[col]
    return [row >> n for row in work]


def quadratic_truth(rows, linear, n):
    out = []
    for x in range(1 << n):
        q = (linear & x).bit_count() & 1
        for i in range(n):
            for j in range(i + 1, n):
                if ((rows[i] >> j) & 1) and ((x >> i) & 1) and ((x >> j) & 1):
                    q ^= 1
        out.append(-1 if q else 1)
    return tuple(out)


def expected_g(inverse, n):
    return Fraction(3 * n, 2) - sum(Fraction(1, 1 << row.bit_count()) for row in inverse)


def main():
    tested = {2: 0, 4: 0, 6: 0}
    for n in (2, 4):
        edge_count = n * (n - 1) // 2
        for mask in range(1 << edge_count):
            rows = matrix_from_mask(n, mask)
            inverse = inverse_rows(rows, n)
            if inverse is None:
                continue
            for linear in range(1 << n):
                truth = quadratic_truth(rows, linear, n)
                assert upper_entropy_vector(truth) == {2: Fraction(n, 2)}
                assert influence(truth) == Fraction(n, 2)
                assert gu_vector(truth) == {2: expected_g(inverse, n)}
                tested[n] += 1

    # Bounded deterministic six-bit pilot: first 48 invertible matrices and
    # four linear shifts apiece.  The theorem itself is analytic.
    n = 6
    edge_count = n * (n - 1) // 2
    matrices = 0
    for mask in range(1 << edge_count):
        rows = matrix_from_mask(n, mask)
        inverse = inverse_rows(rows, n)
        if inverse is None:
            continue
        for linear in (0, 1, 21, 63):
            truth = quadratic_truth(rows, linear, n)
            assert upper_entropy_vector(truth) == {2: Fraction(n, 2)}
            assert influence(truth) == Fraction(n, 2)
            assert gu_vector(truth) == {2: expected_g(inverse, n)}
            tested[n] += 1
        matrices += 1
        if matrices == 48:
            break

    print("formula=G=(3/2)n-sum_i 2^(-r_i), I=n/2, G/I=3-(2/n)sum_i2^(-r_i)")
    print("r_i=row_weight_of_inverse_polar_matrix")
    print("tested=" + repr(tested))
    print("n2_n4_scope=all_invertible_alternating_matrices_and_all_linear_shifts")
    print("n6_scope=first_48_invertible_alternating_matrices_times_4_linear_shifts")
    print("arithmetic=exact_Fraction_and_prime_log_vectors")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
