#!/usr/bin/env python3
"""Exact finite falsification check for B18 parent signed pivotization.

Uses integer cube representation and Fraction arithmetic.  Exhausts all
coordinate subcube defects through n=5, all affine locations, all ordered
translation pairs, and all physical-pivot flags.
"""
from fractions import Fraction

def pc(x): return x.bit_count()

pair_cases = zero_pair_cases = flag_cases = sharp_cases = 0
max_ratio = Fraction(0)

for n in range(1, 6):
    for F in range(1, 1 << n):
        c = pc(F)
        assignments = []
        a = F
        while True:
            assignments.append(a)
            if a == 0:
                break
            a = (a - 1) & F

        for a in assignments:
            def g(x):
                return -1 if (x & F) == a else 1

            # Check the signed-curvature formula and vanishing opposite orientation.
            for i in range(n):
                ib = 1 << i
                for w in range(1 << n):
                    if w & ib:
                        continue
                    flag_cases += 1
                    sq = opp = 0
                    for y in range(1 << n):
                        if y & ib:
                            continue
                        d0 = (g(y) - g(y | ib)) // 2
                        yw = y ^ w
                        d1 = (g(yw) - g(yw | ib)) // 2
                        sq += (d0 - d1) ** 2
                        opp += int(d0 != 0 and d1 == -d0)
                    kap = Fraction(sq, 1 << (n - 1))
                    expected = Fraction(0)
                    if c >= 2 and (F & ib) and (w & (F ^ ib)):
                        expected = Fraction(1, 1 << (c - 2))
                    assert kap == expected
                    assert opp == 0

            J = Fraction(0) if c == 1 else Fraction(c, 1 << (c - 1))

            # Check account02 rank-two plaquette law and deterministic pivotization.
            for u in range(1 << n):
                uf = u & F
                for v in range(1 << n):
                    pair_cases += 1
                    vf = v & F
                    bad = 0
                    for x in range(1 << n):
                        bad += int(g(x) * g(x ^ u) * g(x ^ v) * g(x ^ u ^ v) == -1)
                    P = Fraction(bad, 1 << n)
                    independent = uf != 0 and vf != 0 and uf != vf
                    expected_P = Fraction(1, 1 << (c - 2)) if independent else Fraction(0)
                    assert P == expected_P

                    if P == 0:
                        zero_pair_cases += 1
                        continue

                    active = (u | v) & F
                    ib = active & -active          # deterministic least pivot
                    if (u & ib) and not (v & ib):
                        w = v
                    elif (v & ib) and not (u & ib):
                        w = u
                    else:
                        w = u ^ v
                    assert not (w & ib)

                    sq = opp = 0
                    for y in range(1 << n):
                        if y & ib:
                            continue
                        d0 = (g(y) - g(y | ib)) // 2
                        yw = y ^ w
                        d1 = (g(yw) - g(yw | ib)) // 2
                        sq += (d0 - d1) ** 2
                        opp += int(d0 != 0 and d1 == -d0)
                    kap = Fraction(sq, 1 << (n - 1))
                    assert kap == P
                    assert opp == 0
                    ratio = P / J
                    max_ratio = max(max_ratio, ratio)
                    sharp_cases += int(ratio == 1)

print("PASS")
print(f"pair_cases={pair_cases}")
print(f"zero_pair_cases={zero_pair_cases}")
print(f"flag_cases={flag_cases}")
print(f"max_P_over_J={max_ratio}")
print(f"sharp_codim2_cases={sharp_cases}")
