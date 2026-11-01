#!/usr/bin/env python3
"""Exact checks for the B17 fixed-order moment-credit barrier.

Uses only Python standard library exact integer/Fraction arithmetic for the
factorial moments and analytic live-current lower bound.  Floating output is
for display only.
"""

from fractions import Fraction
import json


def falling(n: int, k: int) -> int:
    if k < 0:
        return 0
    if k > n:
        return 0
    out = 1
    for j in range(k):
        out *= n - j
    return out


def spectral_factorial_moment(D: int, k: int) -> Fraction:
    """M_k for the exact four-point Boolean source in the report."""
    if D < 4 or k < 1:
        raise ValueError("require D>=4 and k>=1")
    N = 1 << D
    term = Fraction(falling(D - 3, k), 1 << k)
    if k >= 1:
        term += Fraction(k * falling(D - 3, k - 1), 1 << (k - 1))
    if k >= 2:
        term += Fraction(
            (k * (k - 1) // 2) * falling(D - 3, k - 2),
            1 << (k - 2),
        )
    return Fraction(16, N) * term


def influence(D: int) -> Fraction:
    return Fraction(8 * (D - 1), 1 << D)


def halfband_current_lower_bound(D: int) -> Fraction:
    """Consumed fleet02 theorem; valid for D>=128."""
    if D < 128:
        raise ValueError("analytic lower bound is used only for D>=128")
    return Fraction(7, 3145728 * (D - 1) ** 3)


def first_unit_weight_crossing(D: int) -> int:
    target = halfband_current_lower_bound(D)
    for k in range(1, D + 1):
        if spectral_factorial_moment(D, k) >= target:
            return k
    raise AssertionError("no crossing found")


def main() -> None:
    # Exact normalization check.
    for D in (8, 16, 32, 128, 256):
        assert spectral_factorial_moment(D, 1) == influence(D)

    rows = []
    for D in (128, 256, 512, 1024):
        k = first_unit_weight_crossing(D)
        target = halfband_current_lower_bound(D)
        below = spectral_factorial_moment(D, k - 1) if k > 1 else Fraction(0)
        at = spectral_factorial_moment(D, k)
        assert below < target <= at
        rows.append(
            {
                "D": D,
                "current_lower_bound_display": float(target),
                "first_unit_weight_crossing_order": k,
                "moment_before_display": float(below),
                "moment_at_crossing_display": float(at),
            }
        )

    d128 = {
        str(k): float(spectral_factorial_moment(128, k))
        for k in (1, 2, 3, 4, 8, 12, 14, 15)
    }

    out = {
        "schema_version": 1,
        "exact_checks": {
            "M1_equals_influence": True,
            "crossing_bracketing": True,
        },
        "D128_selected_moments_display": d128,
        "crossings": rows,
        "interpretation": (
            "Finite displays support the exact formula; the asymptotic proof in "
            "REPORT.md does not depend on numerical extrapolation."
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
