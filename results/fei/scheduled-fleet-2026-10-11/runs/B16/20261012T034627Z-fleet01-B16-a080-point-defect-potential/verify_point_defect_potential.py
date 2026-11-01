#!/usr/bin/env python3
"""Exact Walsh audit for the A080 point-defect tensor classification.

All spectra, upper-set masses, and influences are Fractions.  Decimal logs
are used only to compare the closed entropy/potential formulas after the
exact probability identities have been established.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

getcontext().prec = 90
LN2 = Decimal(2).ln()


def dlog2(x: Fraction) -> Decimal:
    return (Decimal(x.numerator) / Decimal(x.denominator)).ln() / LN2


def walsh(values):
    n = len(values).bit_length() - 1
    ans = []
    for s in range(1 << n):
        total = 0
        for x, v in enumerate(values):
            total += v * (-1 if ((s & x).bit_count() & 1) else 1)
        ans.append(Fraction(total, 1 << n))
    return ans


def entropy(p):
    return sum((-Decimal(x.numerator) / Decimal(x.denominator) * dlog2(x))
               for x in p if x)


def influence(p):
    return sum(Fraction(s.bit_count()) * x for s, x in enumerate(p))


def upper_potential(p):
    n = len(p).bit_length() - 1
    total = Decimal(0)
    for s, ps in enumerate(p):
        if not ps:
            continue
        pi = sum(p[t] for t in range(1 << n) if (t & s) == s)
        total += (Decimal(ps.numerator) / Decimal(ps.denominator)) * dlog2(pi / ps)
    return total


def point_defect(d):
    vals = [1] * (1 << d)
    vals[0] = -1
    return vals


def tensor_spectrum(p, q):
    return [a * b for b in q for a in p]


def close(a, b, tol=Decimal("1e-75")):
    return abs(a - b) <= tol


def main():
    exact_assertions = 0
    decimal_assertions = 0

    spectra = {}
    for d in range(1, 11):
        coeff = walsh(point_defect(d))
        p = [x * x for x in coeff]
        spectra[d] = p
        delta = Fraction(1, 1 << d)
        p0 = (1 - 2 * delta) ** 2
        atom = 4 * delta * delta

        assert p[0] == p0
        exact_assertions += 1
        assert all(x == atom for x in p[1:])
        exact_assertions += len(p) - 1
        assert sum(p) == 1
        exact_assertions += 1

        I = influence(p)
        assert I == 2 * d * delta
        exact_assertions += 1

        # Exact upper-set law: pi(empty)=1 and pi(S)=atom*2^(d-|S|).
        for s in range(1 << d):
            pi = sum(p[t] for t in range(1 << d) if (t & s) == s)
            expected = Fraction(1) if s == 0 else atom * (1 << (d - s.bit_count()))
            assert pi == expected
            exact_assertions += 1

        H = entropy(p)
        U = upper_potential(p)
        empty_term = Decimal(0) if p0 == 0 else -(Decimal(p0.numerator) / Decimal(p0.denominator)) * dlog2(p0)
        U_formula = empty_term + Decimal((I * (1 - 2 * delta)).numerator) / Decimal((I * (1 - 2 * delta)).denominator)
        assert close(U, U_formula)
        decimal_assertions += 1
        assert H < Decimal(4 * I.numerator) / Decimal(I.denominator)
        decimal_assertions += 1
        bound = (Decimal(1) - Decimal(2 * delta.numerator) / Decimal(delta.denominator)) * (
            Decimal(1) + Decimal(2) / (Decimal(d) * LN2)
        )
        assert U / (Decimal(I.numerator) / Decimal(I.denominator)) <= bound + Decimal("1e-75")
        decimal_assertions += 1

    # Independent direct checks of H, I, and U tensor additivity.
    tensor_cases = 0
    for d1, d2 in product(range(1, 5), repeat=2):
        p, q = spectra[d1], spectra[d2]
        pq = tensor_spectrum(p, q)
        assert influence(pq) == influence(p) + influence(q)
        exact_assertions += 1
        assert close(entropy(pq), entropy(p) + entropy(q))
        decimal_assertions += 1
        assert close(upper_potential(pq), upper_potential(p) + upper_potential(q))
        decimal_assertions += 1
        tensor_cases += 1

    print("PASS: point-defect potential and tensor laws")
    print(f"point-defect dimensions: 1..10")
    print(f"tensor pairs: {tensor_cases} (all ordered d1,d2 in 1..4)")
    print(f"exact rational assertions: {exact_assertions}")
    print(f"90-digit decimal assertions: {decimal_assertions}")
    print("seed: None")
    print("scope: finite audit; all-dimensional theorem is proved analytically")


if __name__ == "__main__":
    main()
