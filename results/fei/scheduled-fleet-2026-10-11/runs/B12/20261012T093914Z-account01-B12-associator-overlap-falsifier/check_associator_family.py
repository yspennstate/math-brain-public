#!/usr/bin/env python3
"""Deterministic checks for the character--point-defect family."""

from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 80


def walsh(values):
    a = [Fraction(x) for x in values]
    n = len(a)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return tuple(x / n for x in a)


def phi(x):
    x = Decimal(x.numerator) / Decimal(x.denominator)
    if not x:
        return Decimal(0)
    return x * x * (Decimal(1) / (x * x)).ln()


def entropy_hat(coeffs):
    return sum((phi(x) for x in coeffs), Decimal(0))


def family(n):
    N = 1 << n
    # Coordinate 0 is fastest.  Choose y=1, where chi_0(y)=-1.
    chi = tuple(1 if (j & 1) == 0 else -1 for j in range(N))
    y = 1
    gm = chi
    gp = tuple(1 if j == y else chi[j] for j in range(N))
    h = tuple(-x for x in chi)
    a = tuple(Fraction(x + z, 2) for x, z in zip(gp, gm))
    b = tuple(Fraction(x - z, 2) for x, z in zip(gp, gm))
    F = tuple(a[j] + h[j] * b[j] for j in range(N))
    assert F == gp
    A, C = a, tuple(h[j] * b[j] for j in range(N))
    assert C == tuple(Fraction(int(j == y)) for j in range(N))

    Ah, Ch, Fh, hh, bh = map(walsh, (A, C, F, h, b))
    omega = entropy_hat(Fh) - entropy_hat(Ah) - entropy_hat(Ch)

    alpha_log = sum(
        (phi(x) for i, x in enumerate(hh) if i and x), Decimal(0)
    )
    nonzero_selector = [(alpha, hh[alpha]) for alpha in range(1, N)
                        if hh[alpha]]
    overlap = sum(
        Fraction((alpha & beta).bit_count()) * value ** 2 * bh[beta] ** 2
        for alpha, value in nonzero_selector for beta in range(N)
    )
    source_influence = sum(
        Fraction(beta.bit_count()) * bh[beta] ** 2 for beta in range(N)
    )

    assert alpha_log == 0
    assert overlap == Fraction(1, 2 * N)
    assert source_influence == Fraction(n, 2 * N)
    return omega, overlap, source_influence


def main():
    rows = []
    for n in range(3, 17):
        omega, overlap, source_influence = family(n)
        overlap_ratio = omega / (Decimal(2 * overlap.numerator) /
                                  Decimal(overlap.denominator))
        source_ratio = omega / (Decimal(source_influence.numerator) /
                                 Decimal(source_influence.denominator))
        rows.append((n, omega, overlap_ratio, source_ratio))

    assert all(rows[j + 1][2] > rows[j][2] for j in range(len(rows) - 1))
    print("PASS")
    print("dimensions_checked=3..16")
    print("random_seed=NONE")
    print("n omega overlap_ratio source_ratio")
    for n, omega, overlap_ratio, source_ratio in rows:
        print(n, f"{omega:.18f}", f"{overlap_ratio:.18f}",
              f"{source_ratio:.18f}")
    print("analytic_overlap_ratio_limit=INFINITY")
    print("analytic_source_ratio_limit=8*ln(2)")
    print("8*ln(2)=", +(Decimal(8) * Decimal(2).ln()))


if __name__ == "__main__":
    main()

