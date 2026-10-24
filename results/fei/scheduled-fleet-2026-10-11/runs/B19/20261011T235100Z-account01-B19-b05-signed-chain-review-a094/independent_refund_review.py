#!/usr/bin/env python3
"""Independent A094 reconstruction of the q_n terminal-refund telescope.

The formal telescope is checked exactly without entropy evaluation.  Separate
finite signs and constants use exact Fraction arithmetic with rigorous
atanh-series logarithm enclosures.  No author code is imported.
"""

from fractions import Fraction as F
from functools import lru_cache


TERMS = 90


@lru_cache(maxsize=None)
def ln_iv(x):
    assert x > 0
    exponent = 0
    y = x
    while y < 1:
        y *= 2
        exponent -= 1
    while y >= 2:
        y /= 2
        exponent += 1

    def core(u):
        z = (u - 1) / (u + 1)
        z2 = z * z
        power = z
        total = F(0)
        for k in range(TERMS):
            total += 2 * power / (2 * k + 1)
            power *= z2
        tail = 2 * power / ((2 * TERMS + 1) * (1 - z2))
        return total, total + tail

    lo, hi = core(y)
    l2, u2 = core(F(2))
    if exponent >= 0:
        return lo + exponent * l2, hi + exponent * u2
    return lo + exponent * u2, hi + exponent * l2


LN2 = ln_iv(F(2))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[1], x[1] - y[0]


def mul(c, x):
    if c >= 0:
        return c * x[0], c * x[1]
    return c * x[1], c * x[0]


def quotient(x, y):
    corners = (x[0] / y[0], x[0] / y[1], x[1] / y[0], x[1] / y[1])
    return min(corners), max(corners)


@lru_cache(maxsize=None)
def entropy_atom(x):
    if x == 0:
        return F(0), F(0)
    lo, hi = ln_iv(x)
    return quotient((-x * hi, -x * lo), LN2)


@lru_cache(maxsize=None)
def physical_cell(a, v):
    mass = a * a + v * v
    label = sub(add(entropy_atom(a * a), entropy_atom(v * v)),
                entropy_atom(mass))
    if mass == 0:
        return label
    p = F(1, 2) + abs(a * v) / mass
    binary_entropy = add(entropy_atom(p), entropy_atom(1 - p))
    phase = mul(mass, sub((F(1), F(1)), binary_entropy))
    return add(label, phase)


@lru_cache(maxsize=None)
def packet(n):
    d = F(1, 1 << n)
    return add(physical_cell(-1 + d, d),
               mul((1 << n) - 1, physical_cell(d, d)))


def formal_add(out, index, coefficient):
    out[index] = out.get(index, F(0)) + coefficient
    if out[index] == 0:
        del out[index]


def formal_telescope(n, t):
    """Coefficients of D_n + reached debt - 2^(t-n)D_t."""
    out = {}
    formal_add(out, n, F(1))
    for m in range(t + 1, n + 1):
        reach = F(1 << m, 1 << n)
        formal_add(out, m, -reach)
        formal_add(out, m - 1, reach / 2)
    formal_add(out, t, -F(1 << t, 1 << n))
    return out


def fwht(a):
    a = list(a)
    step = 1
    while step < len(a):
        for base in range(0, len(a), 2 * step):
            for j in range(step):
                x, y = a[base + j], a[base + j + step]
                a[base + j], a[base + j + step] = x + y, x - y
        step *= 2
    return a


def truth(n):
    return [1] + [-1] * ((1 << n) - 1)


def restrict(a, coordinate, bit):
    return [value for index, value in enumerate(a)
            if ((index >> coordinate) & 1) == bit]


def as_float(x):
    return float(x[0]), float(x[1])


def main():
    checks = 0

    # Formal identity for every stop depth in a broad triangular range.
    for n in range(3, 101):
        for t in range(2, n):
            assert formal_telescope(n, t) == {}
            checks += 1

    # Genuine Boolean spectrum and the unique exceptional chain.
    for n in range(2, 10):
        raw = fwht(truth(n))
        assert raw[0] == -((1 << n) - 2)
        assert raw[1:] == [2] * ((1 << n) - 1)
        checks += len(raw)
        if n >= 3:
            for coordinate in range(n):
                assert restrict(truth(n), coordinate, 0) == truth(n - 1)
                assert restrict(truth(n), coordinate, 1) == [-1] * (1 << (n - 1))
                checks += 2

    c2 = mul(4, packet(2))
    assert F(48676, 10000) < c2[0] < c2[1] < F(48677, 10000)
    checks += 1

    # Independent finite reconstruction of the full D signs and constants.
    for n in range(3, 31):
        gamma = sub(packet(n), mul(F(1, 2), packet(n - 1)))
        cn = mul(1 << n, packet(n))
        assert gamma[1] < 0
        assert cn[0] > 4
        checks += 2

    c30 = mul(1 << 30, packet(30))
    debt_coefficient = sub(c2, c30)
    debt_fraction = quotient(debt_coefficient, c2)
    assert debt_coefficient[1] < F(8677, 10000)
    assert debt_fraction[1] < F(1783, 10000)
    checks += 2

    print(f"C2={as_float(c2)}")
    print(f"C30={as_float(c30)}")
    print(f"C2-C30={as_float(debt_coefficient)}")
    print(f"(C2-C30)/C2={as_float(debt_fraction)}")
    print(f"formal_and_rigorous_checks={checks}")
    print("random_seed=None")
    print("status=PASS")


if __name__ == "__main__":
    main()
