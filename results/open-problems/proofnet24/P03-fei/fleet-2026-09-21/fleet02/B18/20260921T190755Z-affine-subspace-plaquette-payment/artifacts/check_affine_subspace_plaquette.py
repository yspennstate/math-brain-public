#!/usr/bin/env python3
"""Exact sanity checker for B18 affine-subspace plaquette theorem.

The analytic theorem reduces every affine subspace defect to the quotient F_2^c.
For every c<=7 and every ordered pair (u,v) in F_2^c, this checker enumerates x
and verifies:
  P_g(u,v) = 2^(2-c) iff u,v are linearly independent, else 0,
where g(x)=-1 only at the quotient origin.
It also verifies P_g<=c*2^(1-c) for c>=2, the minimal folded-influence
budget of an affine codimension-c defect relative to any spanning physical basis.
"""

from fractions import Fraction

def g(x: int) -> int:
    return -1 if x == 0 else 1

def independent(u: int, v: int) -> bool:
    # Over F_2, two vectors are independent iff both are nonzero and distinct.
    return u != 0 and v != 0 and u != v

def exact_bad_fraction(c: int, u: int, v: int) -> Fraction:
    N = 1 << c
    bad = 0
    for x in range(N):
        if g(x) * g(x ^ u) * g(x ^ v) * g(x ^ u ^ v) == -1:
            bad += 1
    return Fraction(bad, N)

def main() -> None:
    direction_pairs = 0
    rank2_pairs = 0
    max_ratio = Fraction(0, 1)
    max_ratio_c = None
    for c in range(0, 8):
        N = 1 << c
        for u in range(N):
            for v in range(N):
                direction_pairs += 1
                got = exact_bad_fraction(c, u, v)
                if independent(u, v):
                    rank2_pairs += 1
                    expected = Fraction(4, N)
                else:
                    expected = Fraction(0, 1)
                assert got == expected, (c, u, v, got, expected)

                if c <= 1:
                    assert got == 0
                else:
                    minimal_J = Fraction(2 * c, N)  # c*2^(1-c)
                    assert got <= minimal_J
                    ratio = got / minimal_J
                    if ratio > max_ratio:
                        max_ratio = ratio
                        max_ratio_c = c

    print("PASS")
    print(f"quotient_c_range=0..7")
    print(f"ordered_direction_pairs={direction_pairs}")
    print(f"rank2_direction_pairs={rank2_pairs}")
    print(f"max_P_over_minimal_J={max_ratio} at_c={max_ratio_c}")
    print("analytic_expected_max=1 at_c=2")

if __name__ == "__main__":
    main()
