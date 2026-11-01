#!/usr/bin/env python3
"""New B13 diagnostic for the all-cut quadratic relaxation.

This does not test FEI.  It checks the explicit non-Boolean subset laws P_m
used in the accompanying report against the previously proved B13
complementary-cut inequality and prints H(P_m)/E|S|.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
from math import comb, log2

getcontext().prec = 80
GAMMA = (Decimal(13) - Decimal(3) * Decimal(17).sqrt()) / Decimal(8)


def cut_masses(m, u):
    # P(empty)=47/64, total singleton mass=1/4, total pair mass=1/64.
    den_pairs = comb(m, 2)
    a = Fraction(u, 4 * m) + Fraction(comb(u, 2), 64 * den_pairs)
    b = Fraction(m-u, 4 * m) + Fraction(comb(m-u, 2), 64 * den_pairs)
    q = Fraction(u * (m-u), 64 * den_pairs)
    return a, b, q


def entropy_and_mean(m):
    p0 = Fraction(47, 64)
    ps = Fraction(1, 4*m)
    pe = Fraction(1, 64*comb(m, 2))
    H = -float(p0) * log2(float(p0))
    H += m * float(ps) * log2(1.0 / float(ps))
    H += comb(m, 2) * float(pe) * log2(1.0 / float(pe))
    return H, Fraction(9, 32)


def main():
    print("gamma =", GAMMA)
    print("uniform analytic cut-ratio lower bound 128/289 =", float(Fraction(128,289)))
    for m in (5, 8, 16, 64, 256, 1024, 4096):
        best = None
        best_u = None
        violations = 0
        for u in range(1, m):
            a, b, q = cut_masses(m, u)
            ratio = q / (a*b)
            if best is None or ratio < best:
                best, best_u = ratio, u
            if Decimal(q.numerator) * Decimal(a.denominator*b.denominator) < GAMMA * Decimal(q.denominator) * Decimal(a.numerator*b.numerator):
                violations += 1
        H, mean = entropy_and_mean(m)
        print(
            f"m={m:4d}  min_q_over_ab={float(best):.12f}  at_u={best_u:4d}  "
            f"violations={violations}  H={H:.12f}  Esize={float(mean):.8f}  H/Esize={H/float(mean):.12f}"
        )


if __name__ == "__main__":
    main()
