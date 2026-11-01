#!/usr/bin/env python3
"""Exact checks for B15 bridge-selector obstruction.

This checker uses only integer/Fraction arithmetic for the rare-tribes
valuation-reserve lower bound. It does not attempt to numerically certify FEI.
"""
from fractions import Fraction
from math import comb
import json

def nu2(n: int) -> int:
    if n <= 0:
        raise ValueError("nu2 expects a positive integer")
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r

def parent_R(m: int, w: int) -> Fraction:
    e = Fraction(1, 1 << w)
    q = 1 - e
    return sum(
        Fraction(4 * comb(m, k) * nu2(comb(m, k)), 1)
        * e**k * q**(2*m-k)
        for k in range(1, m+1)
    )

def average_child_R(m: int, w: int) -> Fraction:
    e = Fraction(1, 1 << w)
    q = 1 - e
    return sum(
        Fraction(4 * comb(m-1, k) * nu2(comb(m-1, k)), 1)
        * e**k * q**(2*m-1-k)
        for k in range(1, m)
    )

def influence(m: int, w: int) -> Fraction:
    e = Fraction(1, 1 << w)
    q = 1 - e
    return 2 * e * q**(m-1)

cases = [
    # a, m=2^a+1, w, strict rational lower target
    (1, 3, 12, 3),
    (2, 5, 12, 15),
    (3, 9, 12, 47),
    (4, 17, 16, 127),
    (6, 65, 18, 767),
    (8, 257, 20, 4094),
    (10, 1025, 24, 20000),
]

rows = []
for a, m, w, target in cases:
    assert m == (1 << a) + 1
    rp = parent_R(m, w)
    rc = average_child_R(m, w)
    inf = influence(m, w)
    reserve_loss_ratio = (rc - rp) / inf  # = -Delta_i R / Inf_i
    asymptotic_limit = 2 * (m - 1) * nu2(m - 1)
    assert reserve_loss_ratio > target
    assert reserve_loss_ratio < asymptotic_limit
    # For B = H-R, Delta_i B = Delta_i H - Delta_i R.
    # The exact restriction-entropy identity gives Delta_i H >= 0, hence
    # Delta_i B / Inf_i >= reserve_loss_ratio.
    rows.append({
        "a": a,
        "m": m,
        "w": w,
        "variables": m*w,
        "strict_lower_target": target,
        "reserve_loss_ratio_decimal": f"{float(reserve_loss_ratio):.15f}",
        "asymptotic_limit": asymptotic_limit,
    })

print(json.dumps({
    "status": "PASS",
    "claim_checked": (
        "For T_{2^a+1,w}, -Delta_i R / Inf_i exceeds the listed exact "
        "rational targets; therefore Delta_i(H-R)/Inf_i does as well "
        "because Delta_i H >= 0."
    ),
    "rows": rows,
}, indent=2, sort_keys=True))
