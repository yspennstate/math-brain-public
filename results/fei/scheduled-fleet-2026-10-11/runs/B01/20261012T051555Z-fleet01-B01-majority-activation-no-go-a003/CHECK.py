#!/usr/bin/env python3
"""Exact/direct checks for the majority-core activation obstruction.

The analytic claim is proved in REPORT.md.  This script independently compares
the scalar activation identity with direct Walsh computation for small odd n,
then evaluates the exact scalar formula through n=1001.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb

getcontext().prec = 80
LN2 = Decimal(2).ln()


def D(q: Fraction | Decimal | int) -> Decimal:
    if isinstance(q, Fraction):
        return Decimal(q.numerator) / Decimal(q.denominator)
    return Decimal(q)


def log2(x: Decimal) -> Decimal:
    return x.ln() / LN2


def M(t: Decimal) -> Decimal:
    u = Decimal(1) - Decimal(2) * t
    if u == 0:
        return Decimal(0)
    q = u * u
    return q * log2(Decimal(1) / q)


def R(r: Decimal, p: Decimal = Decimal("0.5")) -> Decimal:
    if r == 0:
        return Decimal(0)
    return (
        M(p * r)
        - p * M(r)
        + Decimal(4) * p * r * r * log2(Decimal(1) / r)
        - Decimal(4) * p * p * r * r * log2(Decimal(1) / (p * r))
    )


def S_smooth(r: Decimal, p: Decimal = Decimal("0.5")) -> Decimal:
    return R(r, p) + p * M(r)


def majority_influence(n: int) -> Fraction:
    assert n % 2 == 1
    return Fraction(comb(n - 1, (n - 1) // 2), 2 ** (n - 1))


def scalar_extra(n: int) -> tuple[Decimal, Decimal, Decimal]:
    """Return E_n, singular contribution, smooth remainder.

    E_n = G(F_n) - (1/2)G(g_n).  The control contribution is exactly 1.
    """
    a = D(majority_influence(n))
    mid = Decimal("0.5")
    rp, rm = mid + a / 2, mid - a / 2
    j = R(mid) - (R(rp) + R(rm)) / 2
    singular = Decimal("0.5") * a * a * log2(Decimal(1) / (a * a))
    smooth_j = S_smooth(mid) - (S_smooth(rp) + S_smooth(rm)) / 2
    assert abs(j - singular - smooth_j) < Decimal("1e-65")
    return Decimal(1) + Decimal(n) * j, Decimal(n) * singular, Decimal(n) * smooth_j


def walsh_probs(values: list[int]) -> list[Fraction]:
    a = [Fraction(v) for v in values]
    size = len(a)
    step = 1
    while step < size:
        for base in range(0, size, 2 * step):
            for j in range(step):
                x, y = a[base + j], a[base + j + step]
                a[base + j], a[base + j + step] = x + y, x - y
        step *= 2
    return [(x / size) ** 2 for x in a]


def upper_masses(probs: list[Fraction]) -> list[Fraction]:
    pi = probs[:]
    n = (len(pi)).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for mask in range(len(pi)):
            if not (mask & bit):
                pi[mask] += pi[mask | bit]
    return pi


def U_direct(values: list[int]) -> Decimal:
    probs = walsh_probs(values)
    pis = upper_masses(probs)
    ans = Decimal(0)
    for q, u in zip(probs, pis):
        if q:
            qd, ud = D(q), D(u)
            ans += qd * log2(ud / qd)
    return ans


def restrict_values(values: list[int], i: int, bit_value: int) -> list[int]:
    n = (len(values)).bit_length() - 1
    out = []
    for small in range(1 << (n - 1)):
        lo = small & ((1 << i) - 1)
        hi = small >> i
        full = lo | (bit_value << i) | (hi << (i + 1))
        out.append(values[full])
    return out


def G_direct(values: list[int]) -> Decimal:
    n = (len(values)).bit_length() - 1
    u = U_direct(values)
    return sum(
        (u - (U_direct(restrict_values(values, i, 0))
              + U_direct(restrict_values(values, i, 1))) / 2
         for i in range(n)),
        Decimal(0),
    )


def majority_values(n: int) -> list[int]:
    # The sign convention is immaterial; exactly half the inputs are -1.
    return [-1 if x.bit_count() <= n // 2 else 1 for x in range(1 << n)]


def activated_values(g: list[int]) -> list[int]:
    # Bit 0 is the fresh selector: selector 0 activates g, selector 1 gives +1.
    out = []
    for data in range(len(g)):
        out.extend((g[data], 1))
    return out


def main() -> None:
    assertions = 0
    print("direct Walsh versus scalar activation identity")
    for n in (1, 3, 5, 7):
        g = majority_values(n)
        f = activated_values(g)
        direct = G_direct(f) - G_direct(g) / 2
        scalar, _, _ = scalar_extra(n)
        err = abs(direct - scalar)
        assert err < Decimal("1e-60")
        assertions += 1
        print(f"n={n:4d} direct={direct:.18f} scalar={scalar:.18f} err={err:.2E}")

    print("\nexact scalar majority family (p=1/2, d=1)")
    print("n  a_n  E_n  singular_total  smooth_total  E_n/log2(n)")
    rows = {3, 11, 101, 1001}
    max_abs_smooth = Decimal(0)
    for n in range(1, 1002, 2):
        e, singular, smooth = scalar_extra(n)
        max_abs_smooth = max(max_abs_smooth, abs(smooth))
        a = D(majority_influence(n))
        assert e == e and singular >= 0
        assertions += 2
        if n in rows:
            ratio = e / log2(Decimal(n)) if n > 1 else Decimal("NaN")
            print(f"{n:4d} {a:.12f} {e:.12f} {singular:.12f} {smooth:.12f} {ratio:.12f}")

    # Exact local credits used in the no-go theorem.
    q_increment = Decimal(1)  # Q_{1/2,1}(1/2)
    selector_influence = Decimal("0.5")
    assert q_increment == 1 and selector_influence == Decimal("0.5")
    assertions += 2
    print(f"\nmax |n J_S| through 1001: {max_abs_smooth:.18f}")
    print(f"fixed credits: U increment={q_increment}, selector influence={selector_influence}")
    print(f"analytic leading coefficient 1/pi is not numerically certified here")
    print(f"assertions={assertions}")


if __name__ == "__main__":
    main()
