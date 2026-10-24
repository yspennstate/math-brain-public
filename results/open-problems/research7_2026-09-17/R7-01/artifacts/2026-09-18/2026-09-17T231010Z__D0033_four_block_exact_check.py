#!/usr/bin/env python3
"""Exact rational adversarial check for the four-block D0033 prefix interface.

This is a finite self-check only, not a proof or independent audit.
It exhausts a 5-point rational probability grid for every parameter of a
2-state, 4-time, time-inhomogeneous Markov chain and verifies the three
conditional factorization identities used in the four-block pattern
U1 < V1 < U2 < V2.
"""
from fractions import Fraction
from itertools import product

VALS = [Fraction(0), Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(1)]


def tp(row, x, y):
    p1 = row[x]
    return p1 if y == 1 else 1 - p1


def check(params):
    pi1, p01_0, p01_1, p12_0, p12_1, p23_0, p23_1 = params
    k01 = (p01_0, p01_1)
    k12 = (p12_0, p12_1)
    k23 = (p23_0, p23_1)
    joint = {}
    for x0, x1, x2, x3 in product((0, 1), repeat=4):
        p0 = pi1 if x0 else 1 - pi1
        joint[(x0, x1, x2, x3)] = (
            p0 * tp(k01, x0, x1) * tp(k12, x1, x2) * tp(k23, x2, x3)
        )

    def sm(pred):
        return sum((p for xs, p in joint.items() if pred(xs)), Fraction(0))

    # E_12 = 0: X0 and X3 are independent conditional on X1.
    for x1 in (0, 1):
        den = sm(lambda xs, x1=x1: xs[1] == x1)
        if den:
            for x0, x3 in product((0, 1), repeat=2):
                lhs = sm(lambda xs, x0=x0, x1=x1, x3=x3:
                         xs[0] == x0 and xs[1] == x1 and xs[3] == x3) * den
                rhs = sm(lambda xs, x0=x0, x1=x1:
                         xs[0] == x0 and xs[1] == x1) * sm(
                         lambda xs, x1=x1, x3=x3: xs[1] == x1 and xs[3] == x3)
                if lhs != rhs:
                    return False, ("E12", x0, x1, x3, lhs, rhs)

    # E_21 adjacent-reverse interface: conditioning on X0 does not change K12.
    for x0, x1, x2 in product((0, 1), repeat=3):
        den = sm(lambda xs, x0=x0, x1=x1: xs[0] == x0 and xs[1] == x1)
        if den:
            num = sm(lambda xs, x0=x0, x1=x1, x2=x2:
                     xs[0] == x0 and xs[1] == x1 and xs[2] == x2)
            want = den * tp(k12, x1, x2)
            if num != want:
                return False, ("E21", x0, x1, x2, num, want)

    # E_22 adjacent-forward interface: prefix X0,X1 does not change K23.
    for x0, x1, x2, x3 in product((0, 1), repeat=4):
        den = sm(lambda xs, x0=x0, x1=x1, x2=x2:
                 xs[0] == x0 and xs[1] == x1 and xs[2] == x2)
        if den:
            num = joint[(x0, x1, x2, x3)]
            want = den * tp(k23, x2, x3)
            if num != want:
                return False, ("E22", x0, x1, x2, x3, num, want)
    return True, None


def main():
    count = 0
    for params in product(VALS, repeat=7):
        count += 1
        ok, why = check(params)
        if not ok:
            print("FAIL", params, why)
            raise SystemExit(1)
    print(f"PASS tuples={count} grid_size={len(VALS)} states=2 exact=Fraction")


if __name__ == "__main__":
    main()
