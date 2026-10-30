#!/usr/bin/env python3
"""Verify the complete-graph quadratic obstruction to GU good-coordinate descent."""

from fractions import Fraction
import math


def q_values(n):
    return [1 if ((x.bit_count() * (x.bit_count() - 1) // 2) & 1) == 0 else -1
            for x in range(1 << n)]


def fwht(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def U(values):
    N = len(values)
    n = N.bit_length() - 1
    w = fwht(values)
    sq = [z * z for z in w]
    upper = sq[:]
    for i in range(n):
        for s in range(N):
            if not (s >> i) & 1:
                upper[s] += upper[s | (1 << i)]
    den = N * N
    return sum((x / den) * math.log2(y / x) for x, y in zip(sq, upper) if x)


def restrict(values, n, i, bit):
    out = []
    for y in range(1 << (n - 1)):
        lo = y & ((1 << i) - 1)
        hi = y >> i
        x = lo | (bit << i) | (hi << (i + 1))
        out.append(values[x])
    return out


def G(values):
    n = len(values).bit_length() - 1
    if n == 0:
        return 0.0
    u = U(values)
    return sum(u - (U(restrict(values, n, i, 0))
                    + U(restrict(values, n, i, 1))) / 2
               for i in range(n))


def formulas(n):
    assert n >= 2 and n % 2 == 0
    U0 = Fraction(n, 2)
    I0 = Fraction(n, 2)
    G0 = Fraction(3 * n, 2) - Fraction(n, 2 ** (n - 1))
    dU = Fraction(3, 2) - Fraction(1, 2 ** (n - 1))
    dG = Fraction(4 * n - 1, 2) - Fraction(2 * n - 1, 2 ** (n - 1))
    ratio = 2 * dG
    return U0, I0, G0, dU, dG, ratio


def main():
    direct_cases = 0
    for n in range(2, 13, 2):
        v = q_values(n)
        u = U(v)
        g = G(v)
        U0, I0, G0, dU0, dG0, ratio = formulas(n)
        assert abs(u - float(U0)) < 1e-10
        assert abs(g - float(G0)) < 1e-9
        for i in range(n):
            children = [restrict(v, n, i, bit) for bit in (0, 1)]
            du = u - sum(U(c) for c in children) / 2
            dg = g - sum(G(c) for c in children) / 2
            assert abs(du - float(dU0)) < 1e-9
            assert abs(dg - float(dG0)) < 1e-8
            # Mixed derivative across any cross-part pair is nonzero at zero,
            # so no nontrivial disjoint tensor factorization is possible.
            j = (i + 1) % n
            rect = v[0] * v[1 << i] * v[1 << j] * v[(1 << i) | (1 << j)]
            assert rect == -1
        direct_cases += 1
        print("direct", n, "U", u, "G", g, "curvature_ratio", float(ratio))

    print("exact_formula_table")
    for n in range(2, 102, 2):
        U0, I0, G0, dU0, dG0, ratio = formulas(n)
        # The family obeys GU with (a,b)=(3,0), even though every fixed
        # good-coordinate pair fails for sufficiently large n.
        assert G0 <= 3 * I0
        if n >= 6:
            assert ratio > 14
        if n in (2, 4, 6, 8, 16, 32, 64, 100):
            print(n, str(U0), str(I0), str(G0), str(dU0), str(dG0), str(ratio))

    print("QUADRATIC_CURVATURE_OBSTRUCTION_PASS")
    print("direct_dimensions", direct_cases)
    print("exact_even_dimensions", 50)
    print("status=GC14_REFUTED_GU_NOT_REFUTED")


if __name__ == "__main__":
    main()
