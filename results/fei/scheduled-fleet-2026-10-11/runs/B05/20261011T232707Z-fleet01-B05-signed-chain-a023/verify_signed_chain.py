#!/usr/bin/env python3
"""Rigorous certificate for the B05/A023 signed q_n refund telescope.

All logarithmic enclosures use exact Fraction arithmetic and an atanh
series with an explicit rational tail.  No floating-point value is used in
an assertion.  The analytic report proves the all-n identities; this file
certifies a broad finite range and the exact Boolean restriction chain.
"""

from fractions import Fraction as F
from functools import lru_cache


TERMS = 100


@lru_cache(maxsize=None)
def ln_interval(x):
    """Rigorous enclosure for ln(x), for positive rational x."""
    assert x > 0
    power2 = 0
    y = x
    while y < 1:
        y *= 2
        power2 -= 1
    while y >= 2:
        y /= 2
        power2 += 1

    def base(zarg):
        z = (zarg - 1) / (zarg + 1)
        total = F(0)
        power = z
        for j in range(TERMS):
            total += 2 * power / (2 * j + 1)
            power *= z * z
        tail = 2 * power / ((2 * TERMS + 1) * (1 - z * z))
        return total, total + tail

    lo, hi = base(y)
    ln2lo, ln2hi = base(F(2))
    if power2 >= 0:
        return lo + power2 * ln2lo, hi + power2 * ln2hi
    return lo + power2 * ln2hi, hi + power2 * ln2lo


LN2 = ln_interval(F(2))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[1], x[1] - y[0]


def scale(c, x):
    return (c * x[0], c * x[1]) if c >= 0 else (c * x[1], c * x[0])


def div(x, y):
    values = (x[0] / y[0], x[0] / y[1], x[1] / y[0], x[1] / y[1])
    return min(values), max(values)


@lru_cache(maxsize=None)
def phi(t):
    """Enclosure for t log_2(1/t)."""
    if t == 0:
        return F(0), F(0)
    lo, hi = ln_interval(t)
    return div((-t * hi, -t * lo), LN2)


@lru_cache(maxsize=None)
def l_packet(a, v):
    q = a * a + v * v
    return sub(add(phi(a * a), phi(v * v)), phi(q))


@lru_cache(maxsize=None)
def q_packet(a, v):
    q = a * a + v * v
    if q == 0:
        return F(0), F(0)
    # sqrt(t(1-t))=|av|/q, so both binary-entropy arguments are rational.
    p = F(1, 2) + abs(a * v) / q
    h = add(phi(p), phi(1 - p))
    return scale(q, sub((F(1), F(1)), h))


@lru_cache(maxsize=None)
def d_packet(a, v):
    return add(l_packet(a, v), q_packet(a, v))


@lru_cache(maxsize=None)
def d_n(n):
    """Complete physical L+Q selector packet for q_n."""
    delta = F(1, 1 << n)
    return add(d_packet(-1 + delta, delta),
               scale((1 << n) - 1, d_packet(delta, delta)))


@lru_cache(maxsize=None)
def c_n(n):
    return scale(1 << n, d_n(n))


@lru_cache(maxsize=None)
def gamma_n(n):
    return sub(d_n(n), scale(F(1, 2), d_n(n - 1)))


def interval_sum(values):
    ans = (F(0), F(0))
    for value in values:
        ans = add(ans, value)
    return ans


def weighted_debt(n, t):
    """sum_{m=t+1}^n 2^(m-n)(-Gamma_m)."""
    return interval_sum(
        scale(F(1 << m, 1 << n), scale(-1, gamma_n(m)))
        for m in range(t + 1, n + 1)
    )


def fwht(values):
    values = list(values)
    width = len(values).bit_length() - 1
    for j in range(width):
        step = 1 << j
        for base in range(0, len(values), 2 * step):
            for k in range(step):
                x, y = values[base + k], values[base + k + step]
                values[base + k] = x + y
                values[base + k + step] = x - y
    return values


def q_truth(n):
    return [1] + [-1] * ((1 << n) - 1)


def restriction(values, coordinate, bit):
    return [v for index, v in enumerate(values)
            if ((index >> coordinate) & 1) == bit]


def decimal(iv):
    return float(iv[0]), float(iv[1])


def main():
    assertions = 0

    # Exact Boolean realizability, spectrum, and exceptional-chain recurrence.
    for n in range(2, 11):
        truth = q_truth(n)
        raw = fwht(truth)
        expected = [-((1 << n) - 2)] + [2] * ((1 << n) - 1)
        assert raw == expected
        assertions += len(raw)
        if n >= 3:
            for coordinate in range(n):
                child0 = restriction(truth, coordinate, 0)
                child1 = restriction(truth, coordinate, 1)
                assert child0 == q_truth(n - 1)
                assert child1 == [-1] * (1 << (n - 1))
                assertions += 2

    c2 = c_n(2)
    assert F(48676, 10000) < c2[0] < c2[1] < F(48677, 10000)
    assertions += 1

    # The analytic proof covers all n>=3; certify negativity, monotonic C_n,
    # and the signed terminal refund for a broad finite range.
    for n in range(3, 41):
        gamma = gamma_n(n)
        delta_c = sub(c_n(n), c_n(n - 1))
        assert gamma[1] < 0
        assert delta_c[1] < 0
        assert c_n(n)[0] > 4
        assertions += 3

        debt = weighted_debt(n, 2)
        terminal = scale(F(1, 1 << (n - 2)), d_n(2))
        remainder = add(d_n(n), debt)
        # Dependency-aware interval arithmetic is not used, so require the
        # two rigorous enclosures to overlap.  The exact equality is proved
        # symbolically by 2^m Gamma_m=C_m-C_{m-1}.
        assert remainder[0] <= terminal[1] and terminal[0] <= remainder[1]
        assertions += 1

    # At n=40 the total debt coefficient C_2-C_n is already close to its
    # all-depth limit C_2-4, and the terminal/debt split is bounded away from
    # both zero and one.
    n = 40
    debt_coeff = sub(c_n(2), c_n(n))
    assert F(8676, 10000) < debt_coeff[0] < debt_coeff[1] < F(8678, 10000)
    assertions += 1
    ratio = div(debt_coeff, c_n(2))
    assert F(1782, 10000) < ratio[0] < ratio[1] < F(1783, 10000)
    assertions += 1

    for n in (2, 3, 4, 5, 8, 12, 20, 40):
        gamma = None if n == 2 else decimal(gamma_n(n))
        debt_coeff = decimal(sub(c_n(2), c_n(n)))
        print(f"n={n} C_n={decimal(c_n(n))} gamma={gamma} "
              f"debt_coefficient_C2-Cn={debt_coeff}")

    print(f"exact_and_interval_assertions={assertions}")
    print("random_seed=None")
    print("status=PASS")


if __name__ == "__main__":
    main()
