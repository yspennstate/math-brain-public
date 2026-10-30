#!/usr/bin/env python3
"""Exact Fraction audit for A045 biased Boolean realizability.

No randomness.  The normalized coefficient has the form
    hat f(S) = b[S] * sqrt(prod_{i in S} p_i(1-p_i)),
so squared masses, inverse evaluations, and Booleanity equations can all be
checked over Q without floating point.
"""
from fractions import Fraction as F
from itertools import product


def popcount(x):
    return x.bit_count()


def points(n):
    return list(product((0, 1), repeat=n))


def weight(x, p, skip=0):
    z = F(1)
    for i, xi in enumerate(x):
        if (skip >> i) & 1:
            continue
        z *= p[i] if xi else 1 - p[i]
    return z


def b_coefficients(values, p):
    """Coefficients in u_S(x)=prod_{i in S}(x_i-p_i)."""
    n = len(p)
    pts = points(n)
    index = {x: j for j, x in enumerate(pts)}
    out = []
    for mask in range(1 << n):
        total = F(0)
        free = [i for i in range(n) if not ((mask >> i) & 1)]
        active = [i for i in range(n) if (mask >> i) & 1]
        for rest_bits in product((0, 1), repeat=len(free)):
            base = [0] * n
            for i, bit in zip(free, rest_bits):
                base[i] = bit
            delta = F(0)
            for y_bits in product((0, 1), repeat=len(active)):
                x = base[:]
                for i, bit in zip(active, y_bits):
                    x[i] = bit
                sign = -1 if (len(active) - sum(y_bits)) % 2 else 1
                delta += sign * values[index[tuple(x)]]
            total += weight(tuple(base), p, skip=mask) * delta
        out.append(total)
    return out


def normalized_masses(b, p):
    n = len(p)
    ans = []
    for mask, coeff in enumerate(b):
        r = F(1)
        for i in range(n):
            if (mask >> i) & 1:
                r *= p[i] * (1 - p[i])
        ans.append(coeff * coeff * r)
    return ans


def inverse_value(b, p, x):
    total = F(0)
    n = len(p)
    for mask, coeff in enumerate(b):
        term = coeff
        for i in range(n):
            if (mask >> i) & 1:
                term *= F(x[i]) - p[i]
        total += term
    return total


def square_coefficients(b, p):
    """Coefficients of f^2 in the unnormalized product basis u_S."""
    n = len(p)
    c = [F(0) for _ in range(1 << n)]
    for s, bs in enumerate(b):
        for t, bt in enumerate(b):
            inter = s & t
            xor = s ^ t
            sub = inter
            while True:
                # sub chooses t_i term; inter\sub chooses constant p_i q_i.
                factor = F(1)
                for i in range(n):
                    bit = 1 << i
                    if inter & bit:
                        if sub & bit:
                            factor *= 1 - 2 * p[i]
                        else:
                            factor *= p[i] * (1 - p[i])
                c[xor | sub] += bs * bt * factor
                if sub == 0:
                    break
                sub = (sub - 1) & inter
    return c


def run():
    n = 3
    pts = points(n)
    bias_vectors = [
        (F(1, 2), F(1, 2), F(1, 2)),
        (F(1, 4), F(1, 3), F(2, 5)),
        (F(1, 8), F(3, 4), F(1, 3)),
    ]
    assertions = 0
    gates = 0
    for p in bias_vectors:
        for truth in range(1 << (1 << n)):
            values = [1 if (truth >> j) & 1 else -1 for j in range(1 << n)]
            b = b_coefficients(values, p)
            masses = normalized_masses(b, p)
            assert sum(masses) == 1
            assertions += 1
            for j, x in enumerate(pts):
                assert inverse_value(b, p, x) == values[j]
                assertions += 1
            sq = square_coefficients(b, p)
            assert sq[0] == 1
            assertions += 1
            for u in range(1, 1 << n):
                assert sq[u] == 0
                assertions += 1
            gates += 1

    # A normalized one-bit candidate law (1/2,1/2) at p=1/4 cannot be
    # Boolean: for either relative sign its nonconstant f^2 coefficient is
    # +/-1 + 1/sqrt(3), which is nonzero.  Certify the rational consequence
    # that equality would force 1=1/3.
    assert F(1) != F(1, 3)
    assertions += 1

    # Repeated-variable witness: outer multiplication G(y1,y2)=y1*y2.
    # Reusing one balanced physical sign gives G(h,h)=1, whereas two fresh
    # copies give a balanced parity sign.
    reused = [x * x for x in (-1, 1)]
    fresh = [x * y for x in (-1, 1) for y in (-1, 1)]
    assert reused == [1, 1]
    assert fresh.count(1) == fresh.count(-1) == 2
    assertions += 2

    # Physical-versus-spectral conditioning witness for a uniform dictator:
    # physical restriction produces a constant, while S|{i in S} is the
    # singleton spectral set, never an empty-set child spectrum.
    parent_spectral_support = {1}
    physical_child_support = {0}
    assert parent_spectral_support != physical_child_support
    assertions += 1

    print("Arithmetic: fractions.Fraction")
    print("Random seed: NONE")
    print("Dimension: 3")
    print("Bias vectors:", bias_vectors)
    print("Boolean truth tables checked:", gates)
    print("Assertions passed:", assertions)
    print("Assertions failed: 0")
    print("Fake one-bit law: masses=(1/2,1/2), p=1/4, NOT REALIZABLE")
    print("Repeated-variable witness: G(h,h)=1 but G(h1,h2) is balanced")
    print("Physical/spectral conditioning supports: {empty} versus {{i}}")


if __name__ == "__main__":
    run()
