"""Purposeful exact checks for the new grid algorithm; writes only 065_* files."""

from fractions import Fraction as F
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


solver = load("worker065_grid_solver", HERE / "065_exact_grid_solver.py")
verifier = load("worker065_independent_verifier", HERE / "qso_verify_certificate.py")


def require(test, message):
    if not test:
        raise AssertionError(message)


def l1(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


def rejected(call):
    try:
        call()
    except (ValueError, TypeError, ArithmeticError) as exc:
        return type(exc).__name__ + ": " + str(exc)
    raise AssertionError("Invalid exact-grid input was accepted")


def boundary_input():
    offspring = (1, 2, 1, 1, 2, 0, 2, 0, 0, 0)
    return {"pairs": [{"i": i, "j": j, "p": [int(k == out) for k in range(4)]}
                      for (i, j), out in zip(
                          ((i, j) for i in range(4) for j in range(i, 4)), offspring)]}


def interior_input():
    """Symmetric in 1,2,3, with exact fixed point (1/3,2/9,2/9,2/9)."""
    rows = []
    for i in range(4):
        for j in range(i, 4):
            allowed = [k for k in range(4) if k not in (i, j)]
            p = [F(0)] * 4
            if 0 in (i, j):
                for k in allowed:
                    p[k] = F(1, len(allowed))
            else:
                p[0] = F(3, 4)
                for k in allowed:
                    if k != 0:
                        p[k] = F(1, 4 * (len(allowed) - 1))
            rows.append({"i": i, "j": j, "p": [solver.rational_text(v) for v in p]})
    return {"pairs": rows}


def run():
    rounding = []
    for label, grid, y, expected in [
        ("cap coordinate has zero remainder while a positive tie is rounded", 20,
         [F(2, 5), F(9, 40), F(9, 40), F(3, 20)],
         [F(2, 5), F(1, 4), F(1, 5), F(3, 20)]),
        ("sharp four-coordinate rounding error", 20,
         [F(7, 40), F(9, 40), F(11, 40), F(13, 40)],
         [F(1, 5), F(1, 4), F(1, 4), F(3, 10)]),
        ("coarsest permitted grid", 5, [F(1, 4)] * 4,
         [F(2, 5), F(1, 5), F(1, 5), F(1, 5)]),
    ]:
        actual = solver.round_capped(y, grid)
        error = l1(actual, y)
        require(list(actual) == expected, label)
        require(sum(actual) == 1 and min(actual) >= 0 and max(actual) <= F(2, 5),
                "Rounding lost an exact state invariant")
        require(error <= F(2, grid), "Sharp rounding upper bound failed")
        rounding.append({"case": label, "grid": grid,
                         "output": [str(v) for v in actual], "rounding_error_l1": str(error)})
    require(F(rounding[1]["rounding_error_l1"]) == F(2, 20),
            "The asserted sharp rounding example was not sharp")
    unaligned = solver._largest_remainder((12, 6, 6, 6), 5, 6)
    require(unaligned == (3, 1, 1, 1) and F(unaligned[0], 6) > F(2, 5),
            "The nonaligned-grid cap counterexample failed")

    boundary = boundary_input()
    operator = solver._compile_operator(boundary)
    P = verifier.read_operator(boundary)
    fixed = [F(1, 3), F(1, 3), F(1, 3), F(0)]
    counts, grid = (8, 8, 4, 0), 20
    max_rounding_error = F(0)
    for _ in range(12):
        x = tuple(F(n, grid) for n in counts)
        # Independent Fraction evaluator versus the cleared-denominator engine.
        vx = verifier.evaluate(P, x)
        tx = tuple((3 * a + 2 * b) / 5 for a, b in zip(x, vx))
        counts_next = solver._rounded_step(operator, counts, grid)
        y = tuple(F(n, grid) for n in counts_next)
        require(y == solver.round_capped(tx, grid), "Integer step differs from exact T then rounding")
        require(sum(y) == 1 and min(y) >= 0 and max(y) <= F(2, 5), "Step left K")
        require(l1(y, fixed) <= F(23, 25) * l1(x, fixed) + F(4, grid),
                "Rounded contraction recurrence failed at the exact boundary oracle")
        max_rounding_error = max(max_rounding_error, l1(y, tx))
        counts = counts_next

    interior = interior_input()
    tiny = solver.equiprobable_input()
    delta = F(1, 10**400)
    tiny["pairs"][0]["p"][1] = solver.rational_text(F(1, 3) + delta)
    tiny["pairs"][0]["p"][2] = solver.rational_text(F(1, 3) - delta)
    P_tiny = verifier.read_operator(tiny)
    require(l1(verifier.evaluate(P_tiny, [F(1, 4)] * 4), [F(1, 4)] * 4) == delta / 8,
            "Tiny-coefficient perturbation residual is not delta/8")

    cases = []
    specifications = [
        ("boundary", boundary, F(7, 10**40), fixed),
        ("interior", interior, F(1, 10**45), [F(1, 3)] + [F(2, 9)] * 3),
        ("tiny_perturbation", tiny, F(1, 10**420), None),
    ]
    for name, data, epsilon, oracle in specifications:
        record = solver.solve(data, epsilon)
        checked = verifier.verify_certificate(record, data)
        plan = record["exact_grid_plan"]
        n = solver._parse_integer(plan["grid_denominator"])
        require(n % 20 == 0 and n >= F(1500, 1) / epsilon, "Grid plan is too coarse")
        require(record["exact_grid_iterations"] <= plan["guaranteed_iteration_limit"],
                "Iteration exceeded the proved horizon")
        require(solver.exact_input(plan["factor_five_residual_upper_at_limit"]) <= epsilon,
                "The a priori proof budget exceeds epsilon")
        require(5 * checked["residual"] <= epsilon and record["tolerance_met"],
                "The exact residual stopping rule failed")
        actual_error = None
        if oracle is not None:
            require(verifier.evaluate(verifier.read_operator(data), oracle) == oracle,
                    "Claimed rational oracle is not fixed")
            actual_error = l1(checked["candidate"], oracle)
            require(actual_error <= checked["radius"], "Certificate misses exact oracle")
            for interval, value in zip(record["coordinate_intervals"], oracle):
                require(F(interval[0]) <= value <= F(interval[1]), "Interval misses exact oracle")
            require(any((v * n).denominator != 1 for v in oracle),
                    "Intended off-grid oracle unexpectedly belongs to the grid")
            require(checked["residual"] > 0, "Off-grid oracle received zero residual")
        else:
            require(checked["candidate"] != [F(1, 4)] * 4 and checked["residual"] > 0,
                    "The exact solver discarded the tiny perturbation")
        certificate_path = HERE / ("065_" + name + "_certificate.json")
        certificate_path.write_text(json.dumps(record, indent=2) + "\n")
        cases.append({"case": name, "tolerance": solver.rational_text(epsilon),
                      "grid_bits": n.bit_length(), "grid_mod_9": n % 9,
                      "iterations": record["exact_grid_iterations"],
                      "guaranteed_iteration_limit": plan["guaranteed_iteration_limit"],
                      "exact_actual_error_l1": None if actual_error is None else str(actual_error),
                      "exact_residual_l1": str(checked["residual"]),
                      "certified_error_l1_upper": str(checked["radius"]),
                      "candidate": record["candidate"],
                      "certificate": str(certificate_path.relative_to(ROOT))})

    # A binary-rational input may have over 4300 decimal digits. The new parser,
    # formatter and integer-only horizon computation must not inherit Python's
    # default decimal-conversion ceiling. This exact-zero oracle exits at step 0.
    huge_epsilon = F(1, 10**4400)
    huge_record = solver.solve(solver.equiprobable_input(), huge_epsilon)
    require(huge_record["exact_grid_iterations"] == 0 and
            huge_record["exact_residual_l1"] == "0", "Large-bit exact-zero oracle failed")
    require(solver.exact_input(huge_record["requested_tolerance"]) == huge_epsilon,
            "Large rational text did not round trip")
    huge_grid = solver._parse_integer(huge_record["exact_grid_plan"]["grid_denominator"])
    require(huge_grid == 1500 * 10**4400, "Large-bit grid planning failed")
    previous_limit = sys.get_int_max_str_digits() if hasattr(sys, "get_int_max_str_digits") else None
    try:
        # Only the existing independent verifier needs this runtime adjustment.
        if previous_limit is not None:
            sys.set_int_max_str_digits(0)
        verifier.verify_certificate(huge_record, solver.equiprobable_input())
    finally:
        if previous_limit is not None:
            sys.set_int_max_str_digits(previous_limit)

    rejections = {
        "float_tolerance": rejected(lambda: solver.solve(boundary, 0.01)),
        "boolean_tolerance": rejected(lambda: solver.solve(boundary, True)),
        "zero_tolerance": rejected(lambda: solver.solve(boundary, F(0))),
        "unaligned_grid": rejected(lambda: solver.round_capped([F(2, 5)] + [F(1, 5)] * 3, 6)),
        "json_float": rejected(lambda: solver.read_json('{"value": 0.0}')),
        "exponent_string": rejected(lambda: solver.exact_input("1e-400")),
    }
    cli_input = HERE / "065_boundary_operator.json"
    cli_input.write_text(json.dumps(boundary, indent=2) + "\n")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    cli = subprocess.run([sys.executable, str(HERE / "065_exact_grid_solver.py"),
                          str(cli_input), "--tolerance", "1/100000000"],
                         capture_output=True, text=True, env=env, check=False)
    require(cli.returncode == 0, "Exact-grid CLI failed: " + cli.stderr)
    cli_record = json.loads(cli.stdout)
    verifier.verify_certificate(cli_record, boundary)
    cli_certificate = HERE / "065_cli_certificate.json"
    cli_certificate.write_text(cli.stdout)
    cli_verify = subprocess.run([sys.executable, str(HERE / "qso_verify_certificate.py"),
                                 str(cli_certificate), "--operator", str(cli_input)],
                                capture_output=True, text=True, env=env, check=False)
    require(cli_verify.returncode == 0, "Independent verifier CLI failed: " + cli_verify.stderr)

    files = ["FOUR_TYPE_UNIQUENESS.md", "SOLVER_USAGE.md", "agents/008.md", "agents/026.md",
             "computations/qso_verify_certificate.py", "computations/065_exact_grid_solver.py",
             "computations/065_verify_exact_grid_solver.py"]
    result = {
        "status": "All purposeful exact-grid checks passed",
        "python_version": sys.version,
        "dependency_sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in files},
        "rounding_checks": rounding,
        "unaligned_grid_counterexample": {"input": ["2/5", "1/5", "1/5", "1/5"],
                                          "grid": 6, "output": ["1/2", "1/6", "1/6", "1/6"]},
        "fraction_step_comparison": {"steps": 12, "grid": 20,
                                     "maximum_rounding_l1_error": str(max_rounding_error)},
        "certified_examples": cases,
        "large_integer_encoding_check": {"tolerance_denominator_decimal_digits": 4401,
                                         "grid_bits": huge_grid.bit_length(),
                                         "iterations": 0,
                                         "guaranteed_iteration_limit": huge_record["exact_grid_plan"]["guaranteed_iteration_limit"],
                                         "independently_verified": True,
                                         "existing_verifier_decimal_limit_temporarily_disabled": previous_limit is not None},
        "new_boundary_rejections": rejections,
        "cli": {"solver_exit_status": cli.returncode, "verifier_exit_status": cli_verify.returncode,
                "verifier_output": json.loads(cli_verify.stdout)},
    }
    output = HERE / "065_exact_grid_results.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"],
                      "cases": [{key: case[key] for key in ("case", "iterations", "guaranteed_iteration_limit", "grid_bits")}
                                for case in cases],
                      "result_file": str(output.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    run()
