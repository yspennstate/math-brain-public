"""Guaranteed rational-grid solver for four-type strictly non-Volterra QSOs.

Standard library only. There is no floating-point search. See agents/065.md
for the rounding, termination, residual-certificate, and bit-complexity proofs.
Input uses the same ten unordered parent pairs as the canonical solver.
CLI rational strings are integers or numerator/denominator strings; exponent
notation is deliberately excluded from the polynomial-size input encoding.

    python3 computations/065_exact_grid_solver.py \
        examples/qso-boundary-operator.json --tolerance 1/100000000

The output's residual certificate is accepted by qso_verify_certificate.py.
That verifier checks the finite certificate, not the iteration's proof.
"""

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import json
from math import lcm
from pathlib import Path
import re

CAP = F(2, 5)
LIPSCHITZ = F(23, 25)
_INTEGER = re.compile(r"[+-]?[0-9]+\Z")
_RATIONAL = re.compile(r"([+-]?[0-9]+)(?:/([0-9]+))?\Z")
_DECIMAL_BASE = 10**9


def require(condition, message):
    if not condition:
        raise ValueError(message)


def _parse_integer(text):
    """Parse without Python's optional decimal integer digit limit."""
    require(type(text) is str and _INTEGER.fullmatch(text) is not None,
            "Expected a decimal integer")
    sign = -1 if text.startswith("-") else 1
    digits = text.lstrip("+-")
    value = 0
    first = len(digits) % 9 or 9
    value = int(digits[:first])
    for start in range(first, len(digits), 9):
        value = value * _DECIMAL_BASE + int(digits[start:start + 9])
    return sign * value


def _integer_text(value):
    """Serialize exact integers without changing a process-wide digit limit."""
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    value = abs(value)
    chunks = []
    while value:
        value, chunk = divmod(value, _DECIMAL_BASE)
        chunks.append(chunk)
    return sign + str(chunks[-1]) + "".join(
        f"{chunk:09d}" for chunk in reversed(chunks[:-1]))


def rational_text(value):
    require(type(value) in (int, F), "An exact integer or Fraction is required")
    value = F(value)
    numerator = _integer_text(value.numerator)
    return numerator if value.denominator == 1 else (
        numerator + "/" + _integer_text(value.denominator))


def exact_input(value):
    """Read explicit rationals, rejecting floats, bools and exponent strings."""
    if type(value) in (int, F):
        return F(value)
    require(type(value) is str, "Use an integer or an exact rational string")
    match = _RATIONAL.fullmatch(value)
    require(match is not None, "Use an integer or numerator/denominator string")
    numerator = _parse_integer(match.group(1))
    denominator = _parse_integer(match.group(2)) if match.group(2) else 1
    require(denominator > 0, "A rational denominator must be positive")
    return F(numerator, denominator)


def _exact_api(value, label):
    require(type(value) in (int, F), label + " must be an integer or Fraction")
    return F(value)


def _reject_json_number(text):
    raise ValueError("JSON floating-point and nonfinite numbers are not allowed")


def _unique_object(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, "Duplicate JSON object key: " + key)
        out[key] = value
    return out


def read_json(text):
    return json.loads(text, parse_int=_parse_integer,
                      parse_float=_reject_json_number,
                      parse_constant=_reject_json_number,
                      object_pairs_hook=_unique_object)


@dataclass(frozen=True)
class _Operator:
    denominator: int
    # Every entry is (i, j, ordered-pair multiplicity, integer coefficient row).
    rows: tuple


def _compile_operator(data):
    require(type(data) is dict and type(data.get("pairs")) is list,
            "Input must be an object with a pairs list")
    require(len(data["pairs"]) == 10, "Exactly ten parent pairs are required")
    rational_rows = {}
    for row in data["pairs"]:
        require(type(row) is dict, "Every parent-pair row must be an object")
        i, j = row.get("i"), row.get("j")
        require(type(i) is int and type(j) is int and 0 <= i <= j < 4,
                "Parent indices must satisfy 0 <= i <= j < 4")
        require((i, j) not in rational_rows, "Duplicate parent pair")
        raw = row.get("p")
        require(type(raw) is list and len(raw) == 4,
                "Each parent pair needs four coefficients")
        p = tuple(exact_input(v) for v in raw)
        require(min(p) >= 0 and sum(p) == 1,
                "Each coefficient row must be exactly stochastic")
        require(p[i] == p[j] == 0, "Parental offspring is forbidden")
        rational_rows[i, j] = p
    denominator = lcm(*(v.denominator for p in rational_rows.values() for v in p))
    rows = tuple((i, j, 1 if i == j else 2,
                  tuple(v.numerator * (denominator // v.denominator) for v in p))
                 for (i, j), p in sorted(rational_rows.items()))
    return _Operator(denominator, rows)


def _canonical_operator(operator):
    return {"pairs": [{"i": i, "j": j,
                       "p": [rational_text(F(c, operator.denominator)) for c in row]}
                      for i, j, _, row in operator.rows]}


def equiprobable_input():
    return {"pairs": [{"i": i, "j": j,
                       "p": [rational_text(F(1, 4 - len({i, j})))
                             if k not in (i, j) else "0" for k in range(4)]}
                      for i in range(4) for j in range(i, 4)]}


def _largest_remainder(scaled_numerators, denominator, grid):
    """Round four nonnegative scaled coordinates whose sum is grid."""
    quotient_remainders = [divmod(a, denominator) for a in scaled_numerators]
    counts = [q for q, _ in quotient_remainders]
    remaining = grid - sum(counts)
    if not (sum(scaled_numerators) == grid * denominator and
            min(scaled_numerators) >= 0 and 0 <= remaining < 4):
        raise ArithmeticError("Largest-remainder input invariant failed")
    order = sorted(range(4), key=lambda i: (-quotient_remainders[i][1], i))
    for i in order[:remaining]:
        counts[i] += 1
    return tuple(counts)


def round_capped(y, grid):
    """Exact largest-remainder rounding of a point of K_(2/5).

    Public helper: grid must be a positive integer divisible by five;
    coordinates must be integers or Fractions. Lower indices break ties.
    """
    require(type(grid) is int and grid > 0 and grid % 5 == 0,
            "Grid denominator must be a positive multiple of five")
    require(type(y) in (tuple, list) and len(y) == 4,
            "A capped point needs four coordinates")
    y = tuple(_exact_api(v, "Coordinate") for v in y)
    require(min(y) >= 0 and sum(y) == 1 and max(y) <= CAP,
            "Input must lie exactly in K_(2/5)")
    denominator = lcm(*(v.denominator for v in y))
    scaled = tuple(grid * v.numerator * (denominator // v.denominator) for v in y)
    counts = _largest_remainder(scaled, denominator, grid)
    if max(counts) > 2 * grid // 5:
        raise ArithmeticError("Rounding failed to preserve the cap")
    return tuple(F(n, grid) for n in counts)


def grid_plan(tolerance):
    """Return a guaranteed denominator and iteration limit, using no logs."""
    tolerance = _exact_api(tolerance, "Tolerance")
    require(tolerance > 0, "Tolerance must be positive")
    a, b = tolerance.numerator, tolerance.denominator
    grid = 20 * max(1, (75 * b + a - 1) // a)
    # k is the least nonnegative integer with 2**k >= 60/tolerance.
    ceiling_ratio = (60 * b + a - 1) // a
    k = max(0, (ceiling_ratio - 1).bit_length())
    # (23/25)**9 <= 1/2, checked as the integer inequality in agents/065.md.
    limit = 9 * k
    transient = F(2, 1 << k)
    floor = F(50, grid)
    return {"grid": grid, "halving_blocks": k, "iteration_limit": limit,
            "transient_l1_upper": transient,
            "accumulated_rounding_l1_upper": floor,
            "factor_five_residual_upper_at_limit": 15 * (transient + floor)}


def _evaluate_numerators(operator, counts):
    """Return S with V(counts/N) = S/(D*N*N)."""
    out = [0, 0, 0, 0]
    for i, j, multiplicity, row in operator.rows:
        weight = multiplicity * counts[i] * counts[j]
        for k, coefficient in enumerate(row):
            out[k] += coefficient * weight
    return tuple(out)


def _rounded_step(operator, counts, grid, evaluated=None):
    d = operator.denominator
    evaluated = _evaluate_numerators(operator, counts) if evaluated is None else evaluated
    scaled = tuple(3 * d * grid * n + 2 * s for n, s in zip(counts, evaluated))
    result = _largest_remainder(scaled, 5 * d * grid, grid)
    if max(result) > 2 * grid // 5:
        raise ArithmeticError("Exact averaged iteration left the invariant cap")
    return result


def _certificate(operator, counts, grid, residual, tolerance, step, plan):
    x = tuple(F(n, grid) for n in counts)
    radius = min(F(2), 5 * residual)
    return {
        "certificate_schema": "four-type-qso-residual-v1",
        "operator": _canonical_operator(operator), "cap": "2/5",
        "candidate": [rational_text(v) for v in x],
        "exact_residual_l1": rational_text(residual),
        "certified_error_l1_upper": rational_text(radius),
        "coordinate_intervals": [[rational_text(max(F(0), v - radius / 2)),
                                  rational_text(min(CAP, v + radius / 2))] for v in x],
        "certificate_basis": "FOUR_TYPE_UNIQUENESS.md equation (10), q=2/5; agents/065.md",
        "arithmetic": "exact integers and rational arithmetic throughout",
        "requested_tolerance": rational_text(tolerance), "tolerance_met": radius <= tolerance,
        "exact_grid_iterations": step,
        "exact_grid_plan": {
            "grid_denominator": _integer_text(grid),
            "candidate_grid_numerators": [_integer_text(n) for n in counts],
            "initial_point": ["1/4"] * 4,
            "averaging_weight": "2/5", "contraction_factor": "23/25",
            "one_step_rounding_l1_upper": rational_text(F(4, grid)),
            "accumulated_rounding_l1_upper": rational_text(plan["accumulated_rounding_l1_upper"]),
            "guaranteed_iteration_limit": plan["iteration_limit"],
            "transient_l1_upper_at_limit": rational_text(plan["transient_l1_upper"]),
            "factor_five_residual_upper_at_limit": rational_text(plan["factor_five_residual_upper_at_limit"]),
            "stopping_rule": "5 * exact_residual_l1 <= requested_tolerance"
        }
    }


def solve(data, tolerance=F(1, 10**8)):
    """Return a certificate within a proved finite limit for every valid input.

    data is a ten-pair operator dictionary; coefficient values are integers,
    Fractions, or explicit rational strings. tolerance is a positive integer
    or Fraction. There is no precision knob or discretionary step cutoff.
    """
    tolerance = _exact_api(tolerance, "Tolerance")
    plan = grid_plan(tolerance)
    operator = _compile_operator(data)
    grid, d = plan["grid"], operator.denominator
    counts = (grid // 4,) * 4
    value_denominator = d * grid * grid
    for step in range(plan["iteration_limit"] + 1):
        evaluated = _evaluate_numerators(operator, counts)
        residual = F(sum(abs(s - d * grid * n) for s, n in zip(evaluated, counts)),
                     value_denominator)
        if 5 * residual <= tolerance:
            return _certificate(operator, counts, grid, residual, tolerance, step, plan)
        if step < plan["iteration_limit"]:
            counts = _rounded_step(operator, counts, grid, evaluated)
    # In exact arithmetic this branch is unreachable for validated inputs.
    raise ArithmeticError("The proved iteration limit did not certify the tolerance")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--tolerance", default="1/100000000")
    args = parser.parse_args()
    try:
        data = read_json(args.input.read_text()) if args.input else equiprobable_input()
        record = solve(data, exact_input(args.tolerance))
    except (ValueError, TypeError, ArithmeticError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
