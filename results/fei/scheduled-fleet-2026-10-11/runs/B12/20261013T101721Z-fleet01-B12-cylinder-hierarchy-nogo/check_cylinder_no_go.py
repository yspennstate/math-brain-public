#!/usr/bin/env python3
"""Exact/numerical audit of the unbounded dummy-cylinder hierarchy no-go."""

from decimal import Decimal, getcontext
from fractions import Fraction
import json

getcontext().prec = 90


def fwht(vals):
    a = [Fraction(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def phi(q):
    if q == 0:
        return Decimal(0)
    x = Decimal(q.numerator) / Decimal(q.denominator)
    return x * (Decimal(1) / x).ln()


def eraw(vals):
    return sum(phi(c * c) for c in fwht(vals))


def influence_by_coordinate(vals):
    n = len(vals).bit_length() - 1
    ans = []
    for bit in range(n):
        val = sum((Fraction(vals[x]) - Fraction(vals[x ^ (1 << bit)])) ** 2
                  for x in range(len(vals))) / (4 * len(vals))
        ans.append(val)
    return ans


def local_base():
    # z in F_2^3, source support {000,001,010}; selector is the high bit.
    support = {0, 1, 2}
    s = [int(z in support) for z in range(8)]
    d, a0, f = [], [], []
    for selector in (0, 1):
        x = 1 if selector == 0 else -1
        for z in range(8):
            dv = selector * s[z]
            d.append(dv)
            a0.append(x + dv)
            f.append(x + 2 * dv)
    omega = eraw(f) - eraw(a0) - eraw(d)
    return d, omega


def add_free_bits(vals, count):
    # New high bits; function is independent of them.
    return vals * (1 << count)


def restrict_high_bit(vals, value):
    half = len(vals) // 2
    return vals[:half] if value == 0 else vals[half:]


def main():
    d0, omega = local_base()
    infs = influence_by_coordinate(d0)
    total_i = sum(infs)
    if total_i != Fraction(1, 4):
        raise AssertionError(total_i)

    # Exact positivity certificate:
    # 128 Omega = 169 ln 13 - 45 ln 3 - 100 ln 5 - 256 ln 2.
    lhs = 13 ** 169
    rhs = 3 ** 45 * 5 ** 100 * 2 ** 256
    if not lhs > rhs:
        raise AssertionError("integer positivity certificate failed")
    exact_formula = (
        Decimal(169) * Decimal(13).ln()
        - Decimal(45) * Decimal(3).ln()
        - Decimal(100) * Decimal(5).ln()
        - Decimal(256) * Decimal(2).ln()
    ) / Decimal(128)
    if abs(exact_formula - omega) > Decimal("1e-80"):
        raise AssertionError((exact_formula, omega))

    checks = []
    for depth in range(1, 9):
        lifted = add_free_bits(d0, depth)
        lifted_infs = influence_by_coordinate(lifted)
        if sum(lifted_infs) != total_i:
            raise AssertionError(("influence changed", depth))
        if any(x != 0 for x in lifted_infs[-depth:]):
            raise AssertionError(("dummy direction nonzero", depth))
        cur = lifted
        for _ in range(depth):
            left = restrict_high_bit(cur, 0)
            right = restrict_high_bit(cur, 1)
            if left != right:
                raise AssertionError(("dummy restriction changed source", depth))
            cur = left
        if cur != d0:
            raise AssertionError(("terminal source mismatch", depth))
        weighted_charge = Decimal(depth) * omega
        ratio = weighted_charge / (
            Decimal(total_i.numerator) / Decimal(total_i.denominator)
        )
        checks.append({
            "depth": depth,
            "weighted_charge": str(+weighted_charge),
            "charge_over_root_influence": str(+ratio),
        })

    out = {
        "status": "PASS",
        "base_support": [0, 1, 2],
        "base_dimension": 3,
        "base_source_class": "three distinct parallel point cosets",
        "base_Omega": str(+omega),
        "base_influence": str(total_i),
        "exact_positivity_certificate": "13^169 > 3^45 5^100 2^256",
        "integer_margin_digits": len(str(lhs - rhs)),
        "depths_checked": [1, 8],
        "depth_8": checks[-1],
        "general_identity": "sum_internal w_v Omega_v = L Omega_0; I(root)=1/4",
        "consequence": "ratio = 4 L Omega_0 -> infinity",
        "randomness": "none",
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
