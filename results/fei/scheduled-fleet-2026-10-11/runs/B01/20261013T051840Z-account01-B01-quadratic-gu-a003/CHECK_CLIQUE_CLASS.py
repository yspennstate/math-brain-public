#!/usr/bin/env python3
"""Exact direct checks for the restriction-closed clique-quadratic class."""

from fractions import Fraction
from CHECK_FACTOR3_GU import gu_vector, influence, upper_entropy_vector


def clique_truth(n, epsilon):
    out = []
    for x in range(1 << n):
        weight = x.bit_count()
        q = (weight * (weight - 1) // 2 + epsilon * weight) & 1
        out.append(-1 if q else 1)
    return tuple(out)


def main():
    rows = []
    for n in range(1, 11):
        for epsilon in (0, 1):
            truth = clique_truth(n, epsilon)
            u = upper_entropy_vector(truth)
            g = gu_vector(truth)
            inf = influence(truth)
            if n == 1:
                assert g == {}
                assert inf == epsilon
                rows.append((n, epsilon, u.get(2, Fraction()), Fraction(), inf))
                continue
            assert inf == Fraction(n, 2)
            if n % 2 == 0:
                expected_u = Fraction(n, 2)
                expected_g = Fraction(3 * n, 2) - Fraction(n, 1 << (n - 1))
                assert u == {2: expected_u}
                assert g == {2: expected_g}
            else:
                delta = epsilon ^ (((n - 1) // 2) & 1)
                expected_u = Fraction(n, 2) - 1 + Fraction(delta, 1 << (n - 1))
                expected_g = n * (-Fraction(1, 2) + Fraction(delta, 1 << (n - 1)))
                assert u == ({2: expected_u} if expected_u else {})
                assert g == ({2: expected_g} if expected_g else {})
            rows.append((n, epsilon, u.get(2, Fraction()), g.get(2, Fraction()), inf))

    print("class=f_n,epsilon=(-1)^[sum_{i<j}x_ix_j+epsilon*sum_i x_i]")
    print("even_formula=U=I=n/2; G=(3/2)n-n*2^(-(n-1)); G/I=3-2^(2-n)")
    print("odd_formula=U=n/2-1+delta*2^(-(n-1)); G=n*(-1/2+delta*2^(-(n-1)))<=0")
    print("direct_exact_scope=n=1..10, epsilon=0,1")
    print("rows=" + repr(rows))
    print("arithmetic=exact_Fraction_and_prime_log_vectors")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
