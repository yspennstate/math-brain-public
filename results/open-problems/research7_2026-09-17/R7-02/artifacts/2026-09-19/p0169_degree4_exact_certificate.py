#!/usr/bin/env python3
"""Exact finite certificate for P0169, degree four.

This script certifies two finite claims used by the written proof.

(A) For every m <= 16, the exact layer-relaxation forced by a Boolean
    degree-<=4 function has signed singleton Fourier sum at most 2.
    No floating point is used.  The layer relaxation is a *superset* of
    realizable Boolean functions, so its optimum is a rigorous upper bound.

(B) An explicit seven-variable Boolean degree-4 function has all seven
    singleton Fourier coefficients equal to 1/4, hence signed/l1 linear mass
    7/4.  This is greater than the four-bit-majority value 3/2, so it refutes
    the sharper majority-extremizer proposal at d=4 while not refuting the
    weaker sqrt(d)=2 inequality.

Arithmetic: integers and fractions.Fraction only.
"""

from fractions import Fraction
from itertools import product
from math import comb


def ceil_div(a, b):
    assert b > 0
    return -((-a) // b)


def layer_max(m):
    """Exact optimum over necessary layer conditions for degree <=4."""
    cs = [comb(m, k) for k in range(m + 1)]

    # For m <= 3 every layer profile is represented by a polynomial of degree
    # <=4; enumerate the number b_k of +1 values in each Hamming layer.
    if m <= 3:
        best = None
        witness = None
        feasible = 0
        for bs in product(*(range(c + 1) for c in cs)):
            # h=2r-1 and E[(m-2K)]=0, so
            # L = 2 E[r(K)(m-2K)].
            num = sum(bs[k] * (m - 2 * k) for k in range(m + 1))
            val = Fraction(2 * num, 2 ** m)
            feasible += 1
            if best is None or val > best:
                best = val
                witness = tuple(bs)
        return best, witness, feasible

    # For m >=4 write the quartic layer polynomial in the normalized Newton
    # basis
    #   r(k)=sum_{j=0}^4 u_j C(k,j)/C(m,j).
    # Then the number b_k=C(m,k)r(k) of +1 values in layer k is
    #   b_k=sum_{j=0}^4 u_j C(m-j,k-j).
    # The triangular equations at k=0,1,2,3 make u_0,...,u_3 integers.
    # For each such prefix, all later layer constraints give an exact integer
    # interval for u_4.  Since
    #   L=-u_1-u_2-(3/4)u_3-(1/2)u_4,
    # the optimum in that interval uses its smallest feasible u_4.
    best = None
    witness = None
    feasible_u = 0

    for b0 in range(cs[0] + 1):
        u0 = b0
        for b1 in range(cs[1] + 1):
            u1 = b1 - u0 * comb(m, 1)
            for b2 in range(cs[2] + 1):
                u2 = b2 - u0 * comb(m, 2) - u1 * comb(m - 1, 1)
                for b3 in range(cs[3] + 1):
                    u3 = (b3 - u0 * comb(m, 3)
                          - u1 * comb(m - 1, 2)
                          - u2 * comb(m - 2, 1))

                    lo = -10**30
                    hi = 10**30
                    for k in range(4, m + 1):
                        base = (u0 * comb(m, k)
                                + u1 * comb(m - 1, k - 1)
                                + u2 * comb(m - 2, k - 2)
                                + u3 * comb(m - 3, k - 3))
                        slope = comb(m - 4, k - 4)
                        lo = max(lo, ceil_div(-base, slope))
                        hi = min(hi, (cs[k] - base) // slope)
                        if lo > hi:
                            break
                    if lo > hi:
                        continue

                    feasible_u += hi - lo + 1
                    u4 = lo
                    val = (-Fraction(u1, 1) - Fraction(u2, 1)
                           - Fraction(3 * u3, 4) - Fraction(u4, 2))
                    if best is None or val > best:
                        best = val
                        witness = (u0, u1, u2, u3, u4)

    return best, witness, feasible_u


BAD_TRIPLES = {
    (1, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5),
    (1, 2, 6), (2, 3, 6), (1, 4, 6), (3, 5, 6),
    (1, 2, 7), (2, 3, 7), (3, 4, 7), (4, 5, 7),
    (4, 6, 7), (5, 6, 7),
}

GOOD_QUADS = {
    (2, 3, 4, 5), (2, 3, 4, 6), (1, 4, 5, 6),
    (1, 2, 4, 7), (1, 3, 5, 7), (1, 3, 6, 7),
    (2, 5, 6, 7),
}


def witness_value(bits):
    """Explicit seven-bit witness; bits=1 means x_i=-1."""
    A = tuple(i + 1 for i, bit in enumerate(bits) if bit)
    k = len(A)
    if k == 0:
        return -1
    if k in (1, 2):
        return 1
    if k == 3:
        return -1 if A in BAD_TRIPLES else 1
    if k == 4:
        return 1 if A in GOOD_QUADS else -1
    return -1


def walsh_numerators(n, values):
    nums = []
    for mask in range(1 << n):
        total = 0
        for point, value in enumerate(values):
            parity = (mask & point).bit_count() & 1
            total += value * (-1 if parity else 1)
        nums.append(total)
    return nums


def majority4_value(point):
    xs = [(-1 if ((point >> i) & 1) else 1) for i in range(4)]
    # Tie choice is immaterial for the signed singleton sum.
    return 1 if sum(xs) >= 0 else -1


def qstr(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def main():
    expected = {
        1: Fraction(1), 2: Fraction(1), 3: Fraction(3, 2),
        4: Fraction(3, 2), 5: Fraction(3, 2), 6: Fraction(3, 2),
        7: Fraction(7, 4), 8: Fraction(7, 4), 9: Fraction(7, 4),
        10: Fraction(2), 11: Fraction(2), 12: Fraction(2),
        13: Fraction(2), 14: Fraction(2), 15: Fraction(2),
        16: Fraction(2),
    }

    print("P0169 degree-4 exact certificate")
    print("arithmetic=integer/Fraction; floating_point=False")
    print("PART A: exact quartic layer-relaxation maxima")
    print("m feasible_profiles max_signed_linear_sum witness_Newton_u")
    for m in range(1, 17):
        best, witness, feasible = layer_max(m)
        assert best == expected[m], (m, best, expected[m])
        assert best <= 2
        print(m, feasible, qstr(best), witness)

    print("PART B: explicit 7-variable sharper-clause counterexample")
    n = 7
    values = []
    for point in range(1 << n):
        bits = tuple((point >> i) & 1 for i in range(n))
        values.append(witness_value(bits))
    assert all(v in (-1, 1) for v in values)

    nums = walsh_numerators(n, values)
    nonzero_by_level = {}
    for mask, num in enumerate(nums):
        if num:
            nonzero_by_level.setdefault(mask.bit_count(), []).append(num)

    assert max(nonzero_by_level) == 4
    singleton_nums = [nums[1 << i] for i in range(n)]
    assert singleton_nums == [32] * 7
    witness_mass = Fraction(sum(singleton_nums), 1 << n)
    assert witness_mass == Fraction(7, 4)

    expected_level_summary = {
        0: (1, {-16}),
        1: (7, {32}),
        2: (4, {-16, 16}),
        3: (22, {-16, 16}),
        4: (9, {-16, 16}),
    }
    for level, (count, vals) in expected_level_summary.items():
        got = nonzero_by_level[level]
        assert len(got) == count
        assert set(got) == vals

    maj_values = [majority4_value(point) for point in range(16)]
    maj_nums = walsh_numerators(4, maj_values)
    maj_singletons = [maj_nums[1 << i] for i in range(4)]
    assert maj_singletons == [6] * 4
    maj_mass = Fraction(sum(maj_singletons), 16)
    assert maj_mass == Fraction(3, 2)
    assert witness_mass > maj_mass
    assert witness_mass < 2

    print("witness_constant", qstr(Fraction(nums[0], 128)))
    print("witness_singleton_numerators", singleton_nums)
    print("witness_linear_mass", qstr(witness_mass))
    print("witness_nonzero_level_summary",
          {k: (len(v), sorted(set(v))) for k, v in sorted(nonzero_by_level.items())})
    print("majority4_singleton_numerators", maj_singletons)
    print("majority4_linear_mass", qstr(maj_mass))
    print("ASSERTIONS_PASS")


if __name__ == "__main__":
    main()
