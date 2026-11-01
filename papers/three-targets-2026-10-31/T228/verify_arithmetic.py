#!/usr/bin/env python3
"""Reproduce ten exact rational checks for the T228 nonlinear SGD model.

Run ``python verify_arithmetic.py`` to emit the JSON verification result.
All arithmetic uses fractions.Fraction; no numerical quadrature or floating
point computation is used. These checks verify the displayed arithmetic,
not the analytic hypotheses or the complete mathematical proof.
"""

from fractions import Fraction
import json
import sys


def main():
    F = Fraction
    delta = F(1, 1000)
    eta_low = F(99, 100)
    eta_high = F(101, 100)
    perturbation = 4 * delta + 3 * delta**2 + 2 * delta * (3 + 2 * delta)
    q = F(98, 100) + eta_high * perturbation
    normal_margin = F(97, 100)**2 * 2 * F(157, 50) * F(1359, 500) - 16

    checks = []

    def record(name, actual, relation, expected):
        if relation == "==":
            passed = actual == expected
        elif relation == "<":
            passed = actual < expected
        elif relation == ">":
            passed = actual > expected
        else:
            raise ValueError("Unsupported comparison")
        checks.append({
            "name": name,
            "actual": str(actual),
            "relation": relation,
            "expected": str(expected),
            "passed": passed,
        })

    record("derivative_perturbation", perturbation, "==", F(10007, 10**6))
    record("q", q, "==", F(99010707, 10**8))
    record("q_less_than_one", q, "<", F(1))
    record("margin", 1 - q, "==", F(989293, 10**8))
    record("eta_one_bound", F(97, 100) + perturbation, "==", F(980007, 10**6))
    record("h2_lower", 1 - 2 * eta_low + 3 * eta_low**2, "==", F(19603, 10000))
    record("h2_upper", 1 - 2 * eta_high + 3 * eta_high**2, "==", F(20403, 10000))
    record("normal_rational_margin", normal_margin, "==", F(7532467, 125000000))
    record("normal_rational_margin_positive", normal_margin, ">", F(0))
    record("mixed_label", 3 + 2 * delta, "==", F(1501, 500))

    passed = all(check["passed"] for check in checks)
    result = {
        "title": "T228 exact arithmetic verification",
        "arithmetic": "Python standard-library fractions.Fraction",
        "scope": "Ten displayed rational identities and inequalities; not a full proof verification.",
        "parameters": {
            "delta": str(delta),
            "eta_low": str(eta_low),
            "eta_high": str(eta_high),
        },
        "checks": checks,
        "check_count": len(checks),
        "passed_count": sum(check["passed"] for check in checks),
        "all_exact_checks_pass": passed,
    }
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
