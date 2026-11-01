#!/usr/bin/env python3
"""Exact finite audit for the B07 A034 row-marginal-floor closure."""

from fractions import Fraction
from math import log2


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def entropy(ps):
    return sum(-float(p)*log2(float(p)) for p in ps if p)


def spectrum_law(values):
    n = len(values).bit_length()-1
    N = 1 << n
    return [Fraction(x*x, N*N) for x in fwht(values)]


def influence_from_law(p):
    return sum(Fraction(s.bit_count())*x for s, x in enumerate(p))


def audit_four_variables():
    assertions = fair_count = 0
    min_active = Fraction(1)
    max_fair_ratio = 0.0
    for bits in range(1 << 16):
        vals = [1 if (bits >> x) & 1 else -1 for x in range(16)]
        p = spectrum_law(vals)
        w = [p[T] + p[T | 8] for T in range(8)]
        IA = sum(Fraction(T.bit_count())*w[T] for T in range(8))
        IY = sum(p[T | 8] for T in range(8))
        I = IA + IY
        H = entropy(p)
        Hw = entropy(w)

        # Previously proved K3 marginal ledger, checked here on the full domain.
        assert Hw <= 4*float(IA) + 8*float(IY) + 2e-12
        assertions += 1

        fair = True
        R = 0.0
        for T in range(8):
            if not w[T]:
                continue
            theta = p[T | 8] / w[T]
            if theta not in (0, 1):
                min_active = min(min_active, theta)
            if theta not in (0, Fraction(1, 2), 1):
                fair = False
            R += float(w[T]) * entropy([1-theta, theta])
        assert abs(H - Hw - R) < 2e-12
        assertions += 1

        if fair:
            fair_count += 1
            assert R <= 2*float(IY) + 2e-12
            assert H <= 4*float(IA) + 10*float(IY) + 2e-12
            assert H <= 10*float(I) + 2e-12
            assertions += 3
            if I:
                max_fair_ratio = max(max_fair_ratio, H/float(I))
    assert min_active == Fraction(1, 50)
    assertions += 1
    return assertions, fair_count, min_active, max_fair_ratio


def bent2(x):
    # (-1)^(x1*x2), a two-bit bent Boolean function.
    return -1 if (x & 1) and (x & 2) else 1


def audit_bent_substitution():
    assertions = 0
    max_ratio = 0.0
    # Three address bits and three disjoint two-bit bent blocks.
    for gate_bits in range(256):
        vals = []
        for x in range(1 << 9):
            a = x & 7
            y = x >> 3
            transformed = 0
            for i in range(3):
                ai = (a >> i) & 1
                bi = bent2((y >> (2*i)) & 3)
                # bit 0 represents sign +1; toggling by b=-1 flips it.
                ti = ai ^ (1 if bi == -1 else 0)
                transformed |= ti << i
            vals.append(1 if (gate_bits >> transformed) & 1 else -1)
        p = spectrum_law(vals)
        H = entropy(p)
        I = influence_from_law(p)
        assert H <= 4*float(I) + 3e-11
        assertions += 1
        if I:
            max_ratio = max(max_ratio, H/float(I))

        # Every address row has only fair/frozen data marginals.
        for T in range(8):
            row = [p[T | (U << 3)] for U in range(64)]
            w = sum(row)
            if not w:
                continue
            for j in range(6):
                theta = sum(row[U] for U in range(64) if (U >> j) & 1)/w
                assert theta in (0, Fraction(1, 2), 1)
                assertions += 1
    return assertions, max_ratio


def audit_scalar_bound():
    assertions = 0
    for beta in (0.02, 0.05, 0.1, 0.25, 0.5):
        c = entropy([beta, 1-beta])/beta
        for k in range(1, 10001):
            x = beta + (1-beta)*k/10000
            assert entropy([x, 1-x]) <= c*x + 2e-14
            assertions += 1
    return assertions


def main():
    a1, fair_count, min_active, max_fair = audit_four_variables()
    a2, max_bent = audit_bent_substitution()
    a3 = audit_scalar_bound()
    print("B07 A034 row-marginal-floor verification")
    print(f"assertions={a1+a2+a3}")
    print("four_variable_boolean_functions=65536")
    print(f"fair_frozen_functions={fair_count}")
    print(f"minimum_nontrivial_one_data_marginal={min_active}")
    print(f"maximum_fair_frozen_ratio={max_fair:.12f}")
    print("bent_substitution_base_gates=256")
    print(f"maximum_bent_substitution_ratio={max_bent:.12f}")
    print("scalar_grid_points=50000")
    print("status=PASS")


if __name__ == "__main__":
    main()
