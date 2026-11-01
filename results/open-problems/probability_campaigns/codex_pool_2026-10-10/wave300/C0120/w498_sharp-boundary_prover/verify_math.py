"""Small deterministic geometry and analytic-formula checks, not a proof oracle."""
import argparse
import json
import math
import time
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def vertex_weight(x, y):
    return math.sin(17 * x + 29 * y + 0.31) + math.cos(11 * x - 7 * y + 0.19)


def enumerate_strip(r):
    scores = []
    paths = []
    for steps in product((0, 1), repeat=2 * r):
        x = y = 0
        path = [(0, 0)]
        allowed = True
        for direction in steps:
            if direction == 0:
                x += 1
            else:
                y += 1
            path.append((x, y))
            if abs(x - y) > 1:
                allowed = False
                break
        if allowed and (x, y) == (r, r):
            paths.append(path)
            scores.append(sum(vertex_weight(*v) for v in path))
    return paths, scores


def strip_dynamic_program(r):
    values = {(0, 0): vertex_weight(0, 0)}
    for t in range(1, 2 * r + 1):
        for x in range(max(0, t - r), min(r, t) + 1):
            y = t - x
            if abs(x - y) > 1:
                continue
            previous = [values[v] for v in ((x - 1, y), (x, y - 1)) if v in values]
            if previous:
                values[x, y] = vertex_weight(x, y) + max(previous)
    return values[r, r]


def strip_factorization(r):
    junctions = sum(vertex_weight(k, k) for k in range(r + 1))
    diamonds = sum(max(vertex_weight(k + 1, k), vertex_weight(k, k + 1))
                   for k in range(r))
    return junctions + diamonds


def simpson(function, left, right, intervals=512):
    h = (right - left) / intervals
    middle = sum((4 if k % 2 else 2) * function(left + k * h)
                 for k in range(1, intervals))
    return h * (function(left) + function(right) + middle) / 3


def formula_row(r):
    s = 1.0 / r
    rho = math.exp(-s)
    # atan2 avoids cancellation for very small s; it equals arccos(exp(-s)).
    q = math.atan2(math.sqrt(-math.expm1(-2 * s)), rho) / math.pi
    log_same = r * math.log1p(-q)
    vertices = 2 * r + 1
    variance = (2 - 1 / math.pi) * r + 1
    return {"diamonds": r, "vertices": vertices, "ou_time": s,
            "mismatch_probability": q, "identical_path_probability": math.exp(log_same),
            "log_identical_path_probability": log_same,
            "expected_normalized_overlap": 1 - r * q / vertices,
            "exact_variance": variance, "variance_per_vertex": variance / vertices}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate-receipt", required=True)
    args = parser.parse_args()
    gate_path = Path(args.gate_receipt).resolve()
    if ROOT != gate_path.parent:
        raise ValueError("gate receipt must be in this worker folder")
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    if not gate.get("allowed", False):
        raise RuntimeError("Compute gate did not permit this bounded verification")
    gate_time = datetime.fromisoformat(gate["observed_at"])
    age = (datetime.now(timezone.utc) - gate_time).total_seconds()
    if age < 0 or age > 120:
        raise RuntimeError("Compute gate receipt is not fresh (120 seconds maximum)")

    begin = time.perf_counter()
    checks = []
    errors = []
    # Independent exhaustive paths, dynamic programming, and diamond formula.
    # At most 4096 candidate words; no random sampling, worker pool or model load.
    for r in range(1, 7):
        paths, scores = enumerate_strip(r)
        assert len(paths) == 2 ** r
        assert all(len(p) == 2 * r + 1 for p in paths)
        common = set.intersection(*(set(p) for p in paths))
        assert common == {(k, k) for k in range(r + 1)}
        exact = strip_factorization(r)
        dynamic = strip_dynamic_program(r)
        error = max(abs(max(scores) - exact), abs(dynamic - exact))
        assert error < 1e-11
        errors.append(error)
        checks.append({"check": "strip_geometry_and_maximum", "r": r,
                       "allowed_paths": len(paths), "max_absolute_error": error})
    # Two independent variance calculations: half-normal moment algebra vs
    # the source's OU overlap integral, using u=cos(theta).
    angle_integral = simpson(lambda theta: theta * math.sin(theta), 0, math.pi / 2)
    integral_variance = 1 - angle_integral / math.pi
    moment_variance = 1 - 1 / math.pi
    variance_error = abs(integral_variance - moment_variance)
    assert variance_error < 1e-10
    checks.append({"check": "half_normal_variance_vs_overlap_integral",
                   "absolute_error": variance_error, "value": moment_variance})
    # Angular sector counting checks the bivariate sign-disagreement formula.
    angular_points = 4096
    for s in (0.0, 0.01, 0.1, 1.0, 10.0):
        rho = math.exp(-s)
        noise = math.sqrt(-math.expm1(-2 * s))
        mismatches = 0
        for k in range(angular_points):
            theta = (k + 0.5) * 2 * math.pi / angular_points
            original = math.cos(theta)
            perturbed = rho * original + noise * math.sin(theta)
            mismatches += (original > 0) != (perturbed > 0)
        numeric = mismatches / angular_points
        formula = math.atan2(noise, rho) / math.pi
        error = abs(numeric - formula)
        assert error <= 2 / angular_points
        checks.append({"check": "angular_sign_disagreement", "ou_time": s,
                       "absolute_error": error, "angular_points": angular_points})

    output = {
        "command": "python -X utf8 ~/brain_workers/w498/verify_math.py --gate-receipt ~/brain_workers/w498/COMPUTE_GATE.json",
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "gate_receipt": str(gate_path),
        "scope": "deterministic indexing/geometry checks and evaluations of proved formulas; not a formal proof or independent review",
        "checks_passed": len(checks), "checks": checks,
        "maximum_geometry_error": max(errors),
        "overlap_integral_variance_error": variance_error,
        "formula_rows": [formula_row(r) for r in (100, 10000, 1000000)],
        "asymptotic_variance_per_vertex": 1 - 1 / (2 * math.pi),
        "elapsed_seconds": time.perf_counter() - begin,
        "gpu_or_model_loads": 0,
    }
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks_passed": len(checks),
                      "maximum_geometry_error": max(errors),
                      "overlap_integral_variance_error": variance_error,
                      "formula_rows": output["formula_rows"],
                      "elapsed_seconds": output["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
