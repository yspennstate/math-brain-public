#!/usr/bin/env python3
"""A13: enclosed roots of E|1-eta*A^2|^p = 1, A standard normal.

The certification path uses only the Python standard library.  It combines:
  * exact rational bounds for pi (Machin + alternating-series remainders),
  * exact rational square-root bounds for sqrt(2/pi),
  * directed Decimal arithmetic and widened correctly rounded ln/exp,
  * the proved uniform bound integral_0^infinity |f''| < 140,
  * an exact rational upper bound on the omitted Gaussian tail.

See campaign/reviews/A13.md for the analytic error proof.  This is an
interval-arithmetic computational certificate, conditional on the documented
correct-rounding behavior of Python decimal and ordinary integer arithmetic;
it is not a proof-assistant-verified certificate.  No scipy, mpmath, floating
point quadrature, or Monte Carlo is used in this certification path.
"""

from __future__ import annotations

if not __debug__:
    raise RuntimeError(
        "Certificate checks require assertions enabled; run without -O/-OO "
        "and without PYTHONOPTIMIZE. No certificate was produced."
    )

import argparse
import decimal
import hashlib
import json
import math
from decimal import Context, Decimal as D
from fractions import Fraction as F
from pathlib import Path
import platform
import sys


PRECISION = 40
RADIUS = 10
ROOT_CASES = (
    (99, ("1.10928", "1.10929")),
    (100, ("1.09082", "1.09083")),
    (101, ("1.07272", "1.07273")),
)

DOWN = Context(prec=PRECISION, rounding=decimal.ROUND_FLOOR)
UP = Context(prec=PRECISION, rounding=decimal.ROUND_CEILING)
NEAR = Context(prec=PRECISION, rounding=decimal.ROUND_HALF_EVEN)
EXACT = Context(prec=80, rounding=decimal.ROUND_HALF_EVEN)
EXACT.traps[decimal.Inexact] = True
for context in (DOWN, UP, NEAR, EXACT):
    for signal in (
        decimal.FloatOperation, decimal.Overflow, decimal.Underflow,
        decimal.Subnormal, decimal.InvalidOperation, decimal.DivisionByZero,
    ):
        context.traps[signal] = True


def rational_down(x: F) -> D:
    return DOWN.divide(D(x.numerator), D(x.denominator))


def rational_up(x: F) -> D:
    return UP.divide(D(x.numerator), D(x.denominator))


def atan_reciprocal_bounds(denominator: int, terms: int = 60) -> tuple[F, F]:
    """Exact alternating-series enclosure of atan(1/denominator)."""
    total = sum(
        (F((-1) ** k, (2 * k + 1) * denominator ** (2 * k + 1))
         for k in range(terms)), F(0),
    )
    next_term = F((-1) ** terms,
                  (2 * terms + 1) * denominator ** (2 * terms + 1))
    return min(total, total + next_term), max(total, total + next_term)


def pi_bounds() -> tuple[F, F]:
    """Machin identity pi = 16 atan(1/5) - 4 atan(1/239)."""
    tangent = F(1, 5)
    tangent = 2 * tangent / (1 - tangent * tangent)
    tangent = 2 * tangent / (1 - tangent * tangent)
    assert (tangent - F(1, 239)) / (1 + tangent * F(1, 239)) == 1
    a_lo, a_hi = atan_reciprocal_bounds(5)
    b_lo, b_hi = atan_reciprocal_bounds(239)
    lo, hi = 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo
    assert F(157, 50) < lo < hi < F(22, 7)
    return lo, hi


def sqrt_fraction_bounds(lo: F, hi: F, digits: int = 60) -> tuple[F, F]:
    """Exact enclosing sqrt bounds, using integer square roots only."""
    scale = 10 ** digits
    n_lo = (lo.numerator * scale * scale) // lo.denominator
    n_hi = (hi.numerator * scale * scale) // hi.denominator
    lower = F(math.isqrt(n_lo), scale)
    upper = F(math.isqrt(n_hi) + 1, scale)
    assert lower * lower <= lo <= hi < upper * upper
    return lower, upper


PI_LO, PI_HI = pi_bounds()
C_LO_RAT, C_HI_RAT = sqrt_fraction_bounds(2 / PI_HI, 2 / PI_LO)
C_LO, C_HI = rational_down(C_LO_RAT), rational_up(C_HI_RAT)
assert F(0) < C_LO_RAT < C_HI_RAT < 1


def analytic_constants() -> dict:
    """Check all rational inequalities used by the analytic error proof."""
    b, gaussian_mass_bound = F(101, 100), F(13, 10)
    assert PI_HI / 2 < gaussian_mass_bound ** 2
    assert 2 * b < F(3, 2) ** 2
    derivative_terms = (
        F(12),
        8 * b * b * gaussian_mass_bound,
        4 * b * gaussian_mass_bound * (2 + b),
        8 * b * gaussian_mass_bound * (2 + 3 * b),
        gaussian_mass_bound * (4 + 8 * b + 18 * b * b),
    )
    derivative_bound = sum(derivative_terms, F(0))
    assert derivative_bound == F(6541351, 50000) < 140
    e_partial = sum((F(1, math.factorial(k)) for k in range(7)), F(0))
    assert e_partial > F(1359, 500) > F(8, 3)
    first_moment_square_bound = F(16) / (2 * F(157, 50) * F(1359, 500))
    assert first_moment_square_bound < F(97, 100) ** 2
    assert F(97, 100) + F(1, 100) == F(98, 100) < 1
    h2_min = 1 - 2 * F(99, 100) + 3 * F(99, 100) ** 2
    assert h2_min == F(19603, 10000) > 1
    # For x >= 10, |1-eta*x^2|^p <= 2*x^4. Integration by parts
    # and the Mills bound give tail <= 2*(R^3+3R+3/R)*exp(-R^2/2).
    # e > 8/3 then supplies the following wholly rational upper bound.
    tail_bound = 2 * (F(RADIUS ** 3) + 3 * RADIUS + F(3, RADIUS)) \
        * F(3, 8) ** (RADIUS ** 2 // 2)
    assert tail_bound < F(1, 10 ** 17)
    return {
        "derivative_L1_bound_exact": str(derivative_bound),
        "derivative_L1_bound_used": "140",
        "normalized_tail_bound_exact": str(tail_bound),
        "normalized_tail_bound_up": str(rational_up(tail_bound)),
        "pi_interval": [str(rational_down(PI_LO)), str(rational_up(PI_HI))],
        "normalizer_interval": [str(C_LO), str(C_HI)],
        "rational_fallback": {
            "pi_lower": "157/50",
            "e_lower": "1359/500",
            "e_lower_verified_by_partial_sum": str(e_partial),
            "(4/sqrt(2*pi*e))^2_upper": str(first_moment_square_bound),
            "h_eta(1)_strict_upper": "49/50",
            "h_eta(2)_lower": str(h2_min),
            "conclusion": "1 < alpha_eta < 2 for every eta in [99/100,101/100]",
        },
    }


CONSTANTS = analytic_constants()
TAIL_UP = D(CONSTANTS["normalized_tail_bound_up"])


def enclosing_exp(y_lo: D, y_hi: D) -> tuple[D, D]:
    # Decimal.exp is correctly rounded to nearest, regardless of the context's
    # rounding selector. Widen one representable number in each direction.
    low = NEAR.next_minus(NEAR.exp(y_lo))
    high = NEAR.next_plus(NEAR.exp(y_hi))
    return low, high


def certify_values(eta_numerator: int, p_strings: tuple[str, ...],
                   grid_denominator: int) -> list[dict]:
    """Enclose h_eta(p) for all requested p on the same rational mesh."""
    assert 99 <= eta_numerator <= 101
    q = grid_denominator
    assert q >= 10 and str(q)[0] == "1" and set(str(q)[1:]) == {"0"}
    ps = tuple(D(s) for s in p_strings)
    assert all(D(1) < p <= D(2) for p in ps)
    steps = RADIUS * q
    delta = EXACT.divide(D(1), D(q))
    error = rational_up(F(140, 8 * q * q))
    sums_lo, sums_hi = [D(0) for _ in ps], [D(0) for _ in ps]

    for i in range(steps + 1):
        # These arguments are exact terminating rationals. Inexact is trapped
        # in EXACT, so a later mesh change cannot silently break exactness.
        x2_half = EXACT.divide(D(i * i), D(2 * q * q))
        u_numerator = abs(100 * q * q - eta_numerator * i * i)
        u = EXACT.divide(D(u_numerator), D(100 * q * q))
        if u == 1:
            # ln(1)=0 exactly. Widening zero would manufacture a subnormal
            # endpoint at the context's minimum exponent, unnecessarily.
            log_lo = log_hi = D(0)
        elif u:
            log_near = NEAR.ln(u)
            log_lo = NEAR.next_minus(log_near)
            log_hi = NEAR.next_plus(log_near)
        for j, p in enumerate(ps):
            if not u:
                f_lo = f_hi = D(0)
            else:
                y_lo = DOWN.subtract(DOWN.multiply(p, log_lo), x2_half)
                y_hi = UP.subtract(UP.multiply(p, log_hi), x2_half)
                f_lo, f_hi = enclosing_exp(y_lo, y_hi)
            if i == 0 or i == steps:
                f_lo = DOWN.divide(f_lo, D(2))
                f_hi = UP.divide(f_hi, D(2))
            sums_lo[j] = DOWN.add(sums_lo[j], f_lo)
            sums_hi[j] = UP.add(sums_hi[j], f_hi)

    results = []
    for p_string, total_lo, total_hi in zip(p_strings, sums_lo, sums_hi):
        trap_lo = DOWN.multiply(delta, total_lo)
        trap_hi = UP.multiply(delta, total_hi)
        normalized_lo = DOWN.multiply(C_LO, trap_lo)
        normalized_hi = UP.multiply(C_HI, trap_hi)
        # sqrt(2/pi) < 1, so the unnormalized quadrature error is also a
        # valid normalized error. The omitted tail is positive.
        h_lo = DOWN.subtract(normalized_lo, error)
        h_hi = UP.add(UP.add(normalized_hi, error), TAIL_UP)
        assert h_lo > 0
        results.append({
            "p": p_string,
            "h_interval": [str(h_lo), str(h_hi)],
            "h_minus_one_interval": [
                str(DOWN.subtract(h_lo, D(1))),
                str(UP.subtract(h_hi, D(1))),
            ],
            "normalized_trapezoid_interval": [str(normalized_lo), str(normalized_hi)],
            "normalized_rounding_width_up": str(UP.subtract(normalized_hi, normalized_lo)),
            "quadrature_error_up": str(error),
            "tail_error_up": str(TAIL_UP),
            "nodes": steps + 1,
        })
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--grid-denominator", type=int, default=10000)
    parser.add_argument("--proof", type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / "proofs" / "T228_EXPLICIT_CLOSURE.md")
    args = parser.parse_args()
    proof_hash = hashlib.sha256(args.proof.read_bytes()).hexdigest()
    result = {
        "status": "CERTIFIED_IF_ALL_ASSERTIONS_PASS",
        "method": "directed Decimal intervals plus analytic L1 trapezoid and rational tail bounds",
        "source_proof": str(args.proof.resolve()),
        "source_proof_sha256": proof_hash,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "decimal_version": decimal.__version__,
        "libmpdec_version": decimal.__libmpdec_version__,
        "decimal_precision": PRECISION,
        "rounding_contract": "https://docs.python.org/3.12/library/decimal.html",
        "radius": RADIUS,
        "grid_denominator": args.grid_denominator,
        "constants": CONSTANTS,
        "cases": [],
    }
    # An independent exact Gaussian moment catches normalization or mesh
    # errors: for eta=1, h_eta(2)=1-2+3=2.
    calibration = certify_values(100, ("2",), 1000)[0]
    assert D(calibration["h_interval"][0]) <= 2 <= D(calibration["h_interval"][1])
    result["calibration"] = {"eta": "1", "exact_h": "2", **calibration}
    for eta_num, bracket in ROOT_CASES:
        values = certify_values(eta_num, bracket, args.grid_denominator)
        assert D(values[0]["h_interval"][1]) < 1, (eta_num, "lower-root sign", values[0])
        assert D(values[1]["h_interval"][0]) > 1, (eta_num, "upper-root sign", values[1])
        eta = EXACT.divide(D(eta_num), D(100))
        result["cases"].append({
            "eta": str(eta), "strict_root_bracket": list(bracket),
            "bracket_width": str(EXACT.subtract(D(bracket[1]), D(bracket[0]))),
            "endpoint_certificates": values,
        })
        print(f"Certified eta={eta}: {bracket[0]} < alpha < {bracket[1]}", file=sys.stderr)
    assert hashlib.sha256(args.proof.read_bytes()).hexdigest() == proof_hash, "Source proof changed during run"
    result["status"] = "PASS"
    payload = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    else:
        sys.stdout.write(payload)


if __name__ == "__main__":
    main()
