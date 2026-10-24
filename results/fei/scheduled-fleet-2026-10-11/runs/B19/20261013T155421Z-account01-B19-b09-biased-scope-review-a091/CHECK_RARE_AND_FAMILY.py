#!/usr/bin/env python3
"""Rigorous intervals for the B09 rare-biased AND lower-bound family."""

from fractions import Fraction as Q


TERMS = 64


def ln_unit_interval(x):
    """Enclose ln(x) for 1 <= x < 2 by the positive atanh series."""
    assert Q(1) <= x < Q(2)
    z = (x - 1) / (x + 1)
    s = Q(0)
    power = z
    for j in range(TERMS):
        s += power / (2 * j + 1)
        power *= z * z
    lo = 2 * s
    rem = 2 * power / ((2 * TERMS + 1) * (1 - z * z))
    return lo, lo + rem


LN2 = ln_unit_interval(Q(3, 2))
# Add ln(4/3) to obtain a sharper rational enclosure of ln 2.
_ln43 = ln_unit_interval(Q(4, 3))
LN2 = (LN2[0] + _ln43[0], LN2[1] + _ln43[1])


def div_pos(num, den):
    vals = (num[0] / den[0], num[0] / den[1],
            num[1] / den[0], num[1] / den[1])
    return min(vals), max(vals)


def log2_interval(x):
    assert x > 0
    exponent = 0
    y = Q(x)
    while y < 1:
        y *= 2
        exponent -= 1
    while y >= 2:
        y /= 2
        exponent += 1
    if y == 1:
        return Q(exponent), Q(exponent)
    z = div_pos(ln_unit_interval(y), LN2)
    return z[0] + exponent, z[1] + exponent


def entropy_interval(probs):
    assert all(x >= 0 for x in probs) and sum(probs) == 1
    lo = hi = Q(0)
    for x in probs:
        if not x:
            continue
        a, b = log2_interval(x)
        lo -= x * b
        hi -= x * a
    return lo, hi


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def scale(c, a):
    vals = c * a[0], c * a[1]
    return min(vals), max(vals)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def gap_interval(p, q):
    # Exact squared product-biased Fourier masses for (-1)^(XY).
    masses = (
        (1 - 2 * p * q) ** 2,
        4 * q * q * p * (1 - p),
        4 * p * p * q * (1 - q),
        4 * p * (1 - p) * q * (1 - q),
    )
    assert sum(masses) == 1
    r = 4 * p * q * (1 - q)
    h_parent = entropy_interval(masses)
    h_residual = entropy_interval((r, 1 - r))
    h_child = entropy_interval((4 * q * (1 - q), (1 - 2 * q) ** 2))
    M = sub(h_parent, h_residual)
    J = sub(h_residual, scale(p, h_child))
    return sub(J, M), masses


def decimal(interval, digits=18):
    factor = 10 ** digits
    lo = interval[0].numerator * factor // interval[0].denominator
    hi = -((-interval[1].numerator * factor) // interval[1].denominator)
    def f(v):
        sign = "-" if v < 0 else ""
        v = abs(v)
        return f"{sign}{v // factor}.{v % factor:0{digits}d}"
    return f(lo), f(hi)


def main():
    q = Q(1, 4)
    rows = []
    for k in (4, 8, 16, 32, 64):
        p = Q(1, 2 ** k)
        gap, masses = gap_interval(p, q)
        scale_pk = p * k  # p log_2(1/p)
        ratio = (gap[0] / scale_pk, gap[1] / scale_pk)
        assert gap[0] > 0
        if k >= 8:
            assert ratio[0] > Q(2, 5)
        rows.append((k, decimal(gap), decimal(ratio)))

    # Formula consistency at the source certificate point p=1/8,q=1/4.
    source_gap, source_masses = gap_interval(Q(1, 8), q)
    assert source_masses == (Q(225, 256), Q(7, 256), Q(3, 256), Q(21, 256))
    assert source_gap[0] > Q(1195, 10000)

    print("B19 A091 rare-AND lower-bound certificate")
    print(f"atanh_terms={TERMS}")
    print(f"source_gap_interval={decimal(source_gap)}")
    print("q=1/4; normalized by p*log2(1/p); predicted limit=1/2")
    for k, gap, ratio in rows:
        print(f"k={k}: gap_interval={gap}, normalized_interval={ratio}")
    print("for k>=8 every displayed normalized lower endpoint exceeds 2/5")
    print("all intervals use exact rational arithmetic and outward bounds")


if __name__ == "__main__":
    main()
