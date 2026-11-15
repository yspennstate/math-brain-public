#!/usr/bin/env python3
"""Exact arithmetic check of the energy-kernel identities in REPORT.md."""
import json
from fractions import Fraction as F
from pathlib import Path

checks = 0
for lam in (F(1), F(2), F(10), F(1000)):
    for r in (F(0), F(1, 10), F(1), F(2), F(10000)):
        for im in (F(-100), F(0), F(1, 10), F(10000)):
            b2 = (1 + r) ** 2 + im ** 2
            d1 = (lam + r) ** 2 + im ** 2
            d2 = lam ** 2 + b2
            assert 2 * d1 - d2 == lam ** 2 - 1 + (4 * lam - 2) * r + r ** 2 + im ** 2
            assert 2 * d2 - d1 == (lam - r) ** 2 + 4 * r + im ** 2 + 2
            assert d2 / 2 <= d1 <= 2 * d2
            assert r / d1 <= (1 + r) / b2
            checks += 1
result = {"exact_rational_energy_identity_cases": checks, "all_passed": True,
          "purpose": "Arithmetic check of E/F identities; analytic proof is in REPORT.md."}
root = Path(__file__).resolve().parents[1]
(root / "data" / "energy_identity_checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
