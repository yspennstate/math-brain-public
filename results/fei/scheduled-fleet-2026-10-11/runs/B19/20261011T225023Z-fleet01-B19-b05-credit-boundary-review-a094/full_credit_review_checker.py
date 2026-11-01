#!/usr/bin/env python3
"""Independent B19 review of B05 one-point-defect order-swap credits.

All displayed finite signs use exact Fraction arithmetic plus rigorous
atanh-series bounds for logarithms.  No author code is imported.
"""

from fractions import Fraction as F
from math import isqrt


TERMS = 100


def ln_unit_interval(x):
    """Rigorous interval for ln(x), x rational > 0."""
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
        s = F(0)
        p = z
        for j in range(TERMS):
            s += 2 * p / (2 * j + 1)
            p *= z * z
        rem = 2 * p / ((2 * TERMS + 1) * (1 - z * z))
        return s, s + rem

    lo, hi = base(y)
    l2lo, l2hi = base(F(2))
    if power2 >= 0:
        return lo + power2 * l2lo, hi + power2 * l2hi
    return lo + power2 * l2hi, hi + power2 * l2lo


LN2 = ln_unit_interval(F(2))


def div_interval(x, y):
    vals = (x[0] / y[0], x[0] / y[1], x[1] / y[0], x[1] / y[1])
    return min(vals), max(vals)


def phi(t):
    if t == 0:
        return F(0), F(0)
    lo, hi = ln_unit_interval(t)
    # -t ln(t) / ln(2), using all quotient corners.
    return div_interval((-t * hi, -t * lo), LN2)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[1], x[1] - y[0]


def scale(c, x):
    return (c * x[0], c * x[1]) if c >= 0 else (c * x[1], c * x[0])


def L_packet(a, v):
    q = a * a + v * v
    return sub(add(phi(a * a), phi(v * v)), phi(q))


def Q_packet(a, v):
    q = a * a + v * v
    if q == 0:
        return F(0), F(0)
    # sqrt(t(1-t)) = |a v| / q, so both entropy arguments are rational.
    p = F(1, 2) + abs(a * v) / q
    h = add(phi(p), phi(1 - p))
    return scale(q, sub((F(1), F(1)), h))


def D_packet(a, v):
    return add(L_packet(a, v), Q_packet(a, v))


PACKETS = {"L": L_packet, "Q": Q_packet, "D": D_packet}


def qn_packet(n, kind):
    d = F(1, 1 << n)
    packet = PACKETS[kind]
    empty = packet(-1 + d, d)
    nonempty = scale((1 << n) - 1, packet(d, d))
    return add(empty, nonempty)


def qn_credit(n, kind):
    return sub(qn_packet(n, kind), scale(F(1, 2), qn_packet(n - 1, kind)))


def tensor_packet(a, b, kind):
    A, B = F(1, 1 << a), F(1, 1 << b)
    d = A * B
    packet = PACKETS[kind]
    categories = (
        (1, (-1 + 2*A) * (-1 + 2*B)),
        ((1 << a) - 1, 2*A * (-1 + 2*B)),
        ((1 << b) - 1, (-1 + 2*A) * 2*B),
        (((1 << a) - 1) * ((1 << b) - 1), 4*A*B),
    )
    ans = (F(0), F(0))
    for multiplicity, coefficient in categories:
        ans = add(ans, scale(multiplicity, packet(coefficient - d, d)))
    return ans


def tensor_credit(a, b, factor, kind):
    parent = tensor_packet(a, b, kind)
    child = tensor_packet(a - 1, b, kind) if factor == "A" else tensor_packet(a, b - 1, kind)
    return sub(parent, scale(F(1, 2), child))


def fwht_integer(values):
    a = list(values)
    n = len(a).bit_length() - 1
    for j in range(n):
        step = 1 << j
        for base in range(0, len(a), 2 * step):
            for t in range(step):
                x, y = a[base + t], a[base + t + step]
                a[base + t], a[base + t + step] = x + y, x - y
    return a


def q_value(index, width, offset):
    return 1 if ((index >> offset) & ((1 << width) - 1)) == 0 else -1


def direct_tensor_coefficients(a, b):
    vals = [q_value(x, a, 0) * q_value(x, b, a)
            for x in range(1 << (a + b))]
    raw = fwht_integer(vals)
    N = len(vals)
    return [F(x, N) for x in raw]


def dec(iv):
    return float(iv[0]), float(iv[1])


def main():
    assertions = 0

    # Analytic report handles every n>=3.  These independent intervals cover
    # a broad finite range and all three ledger components.
    for n in range(3, 41):
        for kind in ("L", "Q", "D"):
            iv = qn_credit(n, kind)
            assert iv[1] < 0
            assertions += 1
        if n in (3, 4, 8, 20, 40):
            print(f"q_{n}: L={dec(qn_credit(n,'L'))} "
                  f"Q={dec(qn_credit(n,'Q'))} "
                  f"full={dec(qn_credit(n,'D'))}")

    # Reconstruct the parent and both restricted-child spectra directly from
    # their genuine Boolean truth tables.  These are exactly the three spectra
    # used in the q4 tensor q5 order-swap credits.
    walsh_coefficients = 0
    for a, b in ((4, 5), (3, 5), (4, 4)):
        direct = sorted(direct_tensor_coefficients(a, b))
        A, B = F(1, 1 << a), F(1, 1 << b)
        expected = sorted(
            [(-1 + 2*A) * (-1 + 2*B)]
            + [2*A * (-1 + 2*B)] * ((1 << a) - 1)
            + [(-1 + 2*A) * 2*B] * ((1 << b) - 1)
            + [4*A*B] * (((1 << a) - 1) * ((1 << b) - 1))
        )
        assert direct == expected
        assertions += len(direct)
        walsh_coefficients += len(direct)

    caps = {
        ("A", "L"): F(-22, 100_000),
        ("B", "L"): F(-26, 100_000),
        ("A", "Q"): F(-11, 1_000_000),
        ("B", "Q"): F(-5, 1_000_000),
        ("A", "D"): F(-23, 100_000),
        ("B", "D"): F(-26, 100_000),
    }
    for factor in ("A", "B"):
        for kind in ("L", "Q", "D"):
            iv = tensor_credit(4, 5, factor, kind)
            assert iv[1] < caps[(factor, kind)]
            assertions += 1
            print(f"q4xq5 factor={factor} kind={kind} interval={dec(iv)} "
                  f"certified_upper<{float(caps[(factor,kind)]):.12g}")

    print(f"rigorous_sign_assertions={3*38+6}")
    print(f"exact_tensor_walsh_coefficients={walsh_coefficients}")
    print(f"total_assertions={assertions}")
    print("random_seed=None")
    print("status=PASS")


if __name__ == "__main__":
    main()
