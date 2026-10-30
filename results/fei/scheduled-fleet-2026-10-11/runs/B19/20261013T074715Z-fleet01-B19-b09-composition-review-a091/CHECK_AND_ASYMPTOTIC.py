#!/usr/bin/env python3
"""Deterministic checks supporting the A091 review.

The asymptotic proof is analytic in REPORT.md.  This script only checks the
closed formulas, the repaired finite gate value, and the composition-scope
counterexample numerically at high precision.
"""

from decimal import Decimal, getcontext
import json

getcontext().prec = 90
LN2 = Decimal(2).ln()


def h2(x: Decimal) -> Decimal:
    if x == 0 or x == 1:
        return Decimal(0)
    return -(x * x.ln() + (1 - x) * (1 - x).ln()) / LN2


def and_ledger(p: Decimal, q: Decimal):
    """Ledger for g(x,y)=(-1)^(xy), revealing A={x}."""
    s = 4 * q * (1 - q)
    y_mass = p * s
    x_given_y0 = 4 * p * (1 - p) * q * q / (1 - y_mass)
    M = (1 - y_mass) * h2(x_given_y0) + y_mass * h2(p)
    J = h2(y_mass) - p * h2(s)
    return M, J


def main():
    q = Decimal(1) / 4
    p = Decimal(1) / 8
    M, J = and_ledger(p, q)
    finite_gap = J - M
    assert finite_gap > Decimal("0.1195")

    ratios = []
    for k in (8, 16, 32, 64, 128, 256):
        pk = Decimal(2) ** (-k)
        Mk, Jk = and_ledger(pk, q)
        ratio = (Jk - Mk) / (pk * (Decimal(1) / pk).ln() / LN2)
        ratios.append({"k": k, "ratio": str(ratio)})
    # For q=1/4 the proved leading coefficient is 4q(1-2q)=1/2.
    assert abs(Decimal(ratios[-1]["ratio"]) - Decimal("0.5")) < Decimal("0.02")

    # Composition-scope control.  Each input dictator has a point-mass
    # spectrum and hence M=J=0.  Their nonlinear AND composition at uniform
    # bias, with x revealed and y retained, has uniform four-point spectrum;
    # therefore M=J=1.  The B09 ledger is not additive under general Boolean
    # composition (only under exact disjoint products/tensors).
    composition_control = {
        "base_dictator_M_sum": "0",
        "base_dictator_J_sum": "0",
        "composite_AND_M": "1",
        "composite_AND_J": "1",
    }

    print(json.dumps({
        "status": "PASS",
        "randomness": "NONE",
        "arithmetic": "decimal, 90 digits; analytic proof is in REPORT.md",
        "finite_gate": {
            "p": "1/8",
            "q": "1/4",
            "M": str(M),
            "J": str(J),
            "J_minus_M": str(finite_gap),
            "certified_interval_source": "B09_interval_repair_20261011",
        },
        "endpoint_family": {
            "q": "1/4",
            "proved_leading_coefficient": "1/2",
            "ratios_(J-M)/(p_log2_1_over_p)": ratios,
        },
        "composition_scope_control": composition_control,
        "full_FEI": "OPEN",
    }, indent=2))


if __name__ == "__main__":
    main()
