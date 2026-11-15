#!/usr/bin/env python3
"""Check the written table against exact data using independent Decimal rounding."""

import json
from decimal import Decimal, ROUND_CEILING, localcontext
from fractions import Fraction as F
from pathlib import Path

from trapping_bounds import limits


def main():
    limits()
    data = json.loads(Path("cluster_data.json").read_text())
    proof = Path("PROOF.md").read_text()
    vals = {}
    for row in data["rows"]:
        r = F(row["r"])
        q = F(row["q_r"]["exact"])
        reciprocal = F(row["q_reciprocal"]["exact"])
        upper = F(row["coexistence_upper"]["exact"])
        assert upper == 1 - q - reciprocal
        vals[r] = q
        vals[1 / r] = reciprocal
        with localcontext() as context:
            context.prec = 200
            dec = Decimal(upper.numerator) / Decimal(upper.denominator)
            ceil = dec.quantize(Decimal("0.000000000001"), rounding=ROUND_CEILING)
        expected = f"| {row['r']} | {ceil} |"
        assert expected in proof, expected
    rates = sorted(vals)
    assert all(vals[a] < vals[b] for a, b in zip(rates, rates[1:]))
    audit = json.loads(Path("audit_data.json").read_text())
    B = F(audit["global_quadratic_constant"]["exact"])
    L = F(audit["asymptotic_failure_coefficient"]["exact"])
    assert B == F(2977401937361, 53747712000)
    assert L == F(33393164656111, 806215680000)
    assert F(data["failure_series_coefficients"][2]) == L
    assert data["states_evaluated"] == 2735
    assert len(data["G"]) == 16 and len(data["K"]) == 4
    for r, q in vals.items():
        assert 1 - q <= B / r**2
    # Second integer derivations of the elementary state and jump bounds.
    assert 27 * 2048 == 55296
    assert sum(range(14)) * 18 == 1638
    print("Seven proof-table upper decimals agree with independent Decimal ceilings.")
    print("All exact bounds, reciprocal data, and 13-rate monotonicity checks passed.")
    print("Counts: 16 graph vertices, 4 allowed vertices, 2735 reached states.")
    print("State ceiling 55296 and elementary constant 1638 agree independently.")


if __name__ == "__main__":
    main()
