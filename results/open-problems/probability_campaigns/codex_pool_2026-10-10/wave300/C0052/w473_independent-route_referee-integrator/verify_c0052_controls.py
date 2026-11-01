"""Finite diagnostic controls for the C0052 Lee-Yang audit; no store access."""

import json
from math import acos, exp, pi, sqrt


def check(deficit, r):
    lower = 12 / r**4
    upper = 6 / r**2
    assert lower - 1e-12 <= deficit <= upper + 1e-12
    return {"deficit": deficit, "r": r, "lower": lower, "upper": upper}


rows = []
for n in (1, 2, 8, 32):
    rows.append({"case": f"independent_{n}", **check(2 / n, pi * sqrt(n) / 2)})

for beta in (0, 0.2, 1.0):
    q = exp(-2 * beta)
    variance = 4 / (1 + q)
    first_zero = acos(-q) / 2
    rows.append({"case": f"two_spin_beta_{beta}", **check(2 - q, first_zero * sqrt(variance))})

for radius in (1, 2, 8, 32):
    block = (4 * radius + 1) ** 3
    inner = (2 * radius + 1) ** 3
    assert inner * 8 >= block
    assert block >= 64 * radius**3

print(json.dumps({"checks_passed": len(rows) + 8, "controls": rows}, indent=2))
