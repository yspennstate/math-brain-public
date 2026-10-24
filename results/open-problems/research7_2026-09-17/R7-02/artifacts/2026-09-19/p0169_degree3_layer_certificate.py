#!/usr/bin/env python3
"""Exact finite core for P0169 at Fourier degree 3.

For each m<=16, enumerate every layer-average sequence that could arise from
symmetrizing a Boolean degree-<=3 function on m coordinates, using only the
necessary conditions:
  * layer sum a_k is an integer in [-C(m,k),C(m,k)] of parity C(m,k);
  * normalized layer averages g_k=a_k/C(m,k) have fourth finite difference 0.

This is deliberately a superset of realizable Boolean functions.  Therefore
its maximum signed first-level Fourier sum is a rigorous upper bound.
All arithmetic is exact (fractions.Fraction).
"""

from fractions import Fraction
from itertools import product
from math import comb


def admissible_sums(c):
    return range(-c, c + 1, 2)


def certify_dimension(m):
    cs = [comb(m, k) for k in range(m + 1)]
    best = None
    witness = None
    feasible = 0

    # With at most four layers, every layer sequence is represented by some
    # polynomial of degree <=3, so there is no recurrence constraint to add.
    if m <= 3:
        for vals in product(*(admissible_sums(c) for c in cs)):
            gs = [Fraction(vals[k], cs[k]) for k in range(m + 1)]
            obj = sum(Fraction(cs[k]) * gs[k] * (m - 2 * k)
                      for k in range(m + 1)) / (2 ** m)
            feasible += 1
            if best is None or obj > best:
                best, witness = obj, tuple(vals)
        return best, witness, feasible

    # A cubic sequence is uniquely fixed by g_0,g_1,g_2,g_3.  Enumerate all
    # admissible Boolean layer sums there, propagate by Delta^4 g = 0, and
    # demand the exact Boolean averaging lattice at every later layer.
    for a0 in admissible_sums(cs[0]):
        g0 = Fraction(a0, cs[0])
        for a1 in admissible_sums(cs[1]):
            g1 = Fraction(a1, cs[1])
            for a2 in admissible_sums(cs[2]):
                g2 = Fraction(a2, cs[2])
                for a3 in admissible_sums(cs[3]):
                    gs = [g0, g1, g2, Fraction(a3, cs[3])]
                    vals = [a0, a1, a2, a3]
                    ok = True
                    for k in range(m - 3):
                        nxt = 4 * gs[k + 3] - 6 * gs[k + 2] + 4 * gs[k + 1] - gs[k]
                        c = cs[k + 4]
                        a = nxt * c
                        if a.denominator != 1:
                            ok = False
                            break
                        ai = a.numerator
                        if ai < -c or ai > c or ((ai - c) & 1):
                            ok = False
                            break
                        gs.append(nxt)
                        vals.append(ai)
                    if not ok:
                        continue
                    feasible += 1
                    obj = sum(Fraction(cs[k]) * gs[k] * (m - 2 * k)
                              for k in range(m + 1)) / (2 ** m)
                    if best is None or obj > best:
                        best, witness = obj, tuple(vals)

    return best, witness, feasible


def qstr(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def main():
    expected = {
        1: Fraction(1), 2: Fraction(1),
        3: Fraction(3, 2), 4: Fraction(3, 2), 5: Fraction(3, 2),
        6: Fraction(3, 2), 7: Fraction(3, 2), 8: Fraction(3, 2),
        9: Fraction(3, 2),
        10: Fraction(2), 11: Fraction(2), 12: Fraction(2),
        13: Fraction(2), 14: Fraction(2), 15: Fraction(2),
        16: Fraction(2),
    }
    print("P0169 exact degree-3 layer certificate")
    print("arithmetic=Fraction; floating_point=False")
    print("columns: m feasible_sequences max_signed_linear_sum witness_layer_sums")
    for m in range(1, 17):
        best, witness, feasible = certify_dimension(m)
        assert best == expected[m], (m, best, expected[m])
        print(m, feasible, qstr(best), witness)
    print("ASSERTIONS_PASS")
    print("m<=9: max <= 3/2")
    print("10<=m<=16: max <= 2")


if __name__ == "__main__":
    main()
