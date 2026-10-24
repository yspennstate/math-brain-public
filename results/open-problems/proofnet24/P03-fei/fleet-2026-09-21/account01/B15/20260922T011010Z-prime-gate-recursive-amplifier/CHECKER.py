#!/usr/bin/env python3
"""Arithmetic certificate for the fixed 10-input FEI recursive amplifier.

Inputs inherited from the exact account04/B13 gate certificate:
  I(G)=257/128,
  H(G)/(I(G)-1) > 6.4593722816378554.
The analytic composition recurrence is proved in REPORT.md; this script checks
only the finite-depth numerical consequences using high-precision Decimal.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import json

getcontext().prec = 90
A = Fraction(257, 128)
R_LO = Decimal("6.4593722816378554")
BETA_QUOTED = Decimal("6.4547837")
CANDIDATE_CAP = Decimal("6.4559")
READONCE_PROVED = Decimal("6.4573")


def ratio_lower(depth: int) -> Decimal:
    q = Decimal(A.denominator) / Decimal(A.numerator)
    return R_LO * (Decimal(1) - q ** depth)


def main():
    r10 = ratio_lower(10)
    r11 = ratio_lower(11)
    r12 = ratio_lower(12)
    assert r11 > BETA_QUOTED
    assert r11 > CANDIDATE_CAP
    assert r12 > READONCE_PROVED
    # The balanced support-deficit ratio is invariant exactly under composition.
    # This identity is symbolic: H_d=R*(a^d-1), I_d=a^d.
    report = {
        "I_gate_exact": str(A),
        "R_gate_certified_lower": str(R_LO),
        "depth10_H_over_I_lower": str(r10),
        "depth11_H_over_I_lower": str(r11),
        "depth12_H_over_I_lower": str(r12),
        "depth11_minus_beta_quoted_lower": str(r11 - BETA_QUOTED),
        "depth11_minus_candidate_6_4559_lower": str(r11 - CANDIDATE_CAP),
        "depth12_minus_readonce_proved_6_4573_lower": str(r12 - READONCE_PROVED),
        "depth11_leaf_count": 10**11,
        "depth12_leaf_count": 10**12,
        "full_FEI": "OPEN_NOT_PROVED",
        "classification": "CANDIDATE_REFUTED"
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
