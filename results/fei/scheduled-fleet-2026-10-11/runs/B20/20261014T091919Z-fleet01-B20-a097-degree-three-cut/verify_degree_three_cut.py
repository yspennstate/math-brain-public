#!/usr/bin/env python3
"""Exact arithmetic checks for B20-A097-DEGREE-THREE-CUT-v1."""

from fractions import Fraction


def main() -> None:
    a = Fraction(4)
    b = Fraction(3, 4)
    low_degree_g_coefficient = Fraction(2)

    i_coefficient = low_degree_g_coefficient - a
    u_coefficient = -b
    assert i_coefficient == -2
    assert u_coefficient == Fraction(-3, 4)
    assert b < 1

    # Exact GU-to-U and GU-to-H constants.
    u_over_i = a / (1 - b)
    h_over_i = 2 + 2 * u_over_i
    assert u_over_i == 16
    assert h_over_i == 34

    # For all I>0 and U>=0, the low-degree residual is strictly negative.
    for i_num in range(1, 33):
        for u_num in range(33):
            residual_bound = i_coefficient * i_num + u_coefficient * u_num
            assert residual_bound < 0

    print("claim=B20-A097-DEGREE-THREE-CUT-v1")
    print("exact_low_degree_residual_bound=-2*I-(3/4)*U<0 for I>0,U>=0")
    print("remaining_domain=tensor-prime,positive-residual,Fourier-degree>=3")
    print("gu_pair=(4,3/4)")
    print("derived_U_over_I=16")
    print("derived_H_over_I=34")
    print("status=PASS")


if __name__ == "__main__":
    main()

