#!/usr/bin/env python3
"""Evidence for E0022 candidate checks; no numerical claim about (H)."""
import csv
import json
import math
import os
import resource
from fractions import Fraction
from pathlib import Path

for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 10:
    raise SystemExit("Run with nice priority at least 10")
root = Path(__file__).resolve().parents[1]


def gaussian_parts(x, y, eps):
    return (x + y) ** 2 + eps * (x - y) ** 2, -(x - y)


def ratio(real, imag):
    return abs(imag) / (1.0 + real)


# Independent exact-rational verification of the covariance quadratic form.
exact_checks = 0
for eps in map(Fraction, ("0", "1/100000000", "1/10000", "1")):
    for x in range(-3, 4):
        for y in range(-3, 4):
            q11 = 2 * (1 + eps)
            q12 = 2 * (1 - eps)
            matrix = (q11 * x * x + 2 * q12 * x * y + q11 * y * y) / 2
            assert matrix == (x + y) ** 2 + eps * (x - y) ** 2
            exact_checks += 1

gaussian = []
angular_rows = []
# Offset deliberately misses the exceptional angle. The exact angle is added below.
directions = [math.pi * j / 3600 + 0.000123 for j in range(3600)]
for eps in (0.0, 1e-8, 1e-4, 1.0):
    best = (-1.0, None)
    max_identity_error = 0.0
    for theta in directions:
        ex, ey = math.cos(theta), math.sin(theta)
        a, imag_unit = gaussian_parts(ex, ey, eps)
        assert a > 0
        radius = 1.0 / math.sqrt(a)
        predicted = abs(imag_unit) / (2.0 * math.sqrt(a))
        real, imag = gaussian_parts(radius * ex, radius * ey, eps)
        observed = ratio(real, imag)
        max_identity_error = max(max_identity_error, abs(observed - predicted) / max(1.0, predicted))
        assert math.isclose(observed, predicted, rel_tol=1e-10, abs_tol=1e-10)
        for factor in (0.5, 2.0):
            rr, ii = gaussian_parts(factor * radius * ex, factor * radius * ey, eps)
            assert ratio(rr, ii) <= predicted * (1 + 1e-10) + 1e-10
        angular_rows.append((eps, theta, predicted, radius))
        if predicted > best[0]:
            best = (predicted, theta)
    bound = None if eps == 0 else 1.0 / (2.0 * math.sqrt(eps))
    if bound is not None:
        assert best[0] <= bound * (1 + 1e-10)
    gaussian.append({"epsilon": eps, "offset_grid_directions": len(directions),
                     "largest_grid_ray_supremum": best[0], "at_angle": best[1],
                     "proved_global_supremum": "infinite" if bound is None else bound,
                     "max_relative_radial_identity_error": max_identity_error})

bad_direction = (1 / math.sqrt(2), -1 / math.sqrt(2))
exceptional = []
for radius in (1.0, 100.0, 1e4, 1e6):
    real, imag = gaussian_parts(radius * bad_direction[0], radius * bad_direction[1], 0.0)
    assert real == 0.0
    exceptional.append({"radius": radius, "ratio": ratio(real, imag)})

near_exceptional = []
for delta in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    theta = -math.pi / 4 + delta
    ex, ey = math.cos(theta), math.sin(theta)
    a, imag_unit = gaussian_parts(ex, ey, 0.0)
    direct = abs(imag_unit) / (2 * math.sqrt(a))
    trig = abs(1 / math.tan(delta)) / 2
    assert math.isclose(direct, trig, rel_tol=2e-10)
    near_exceptional.append({"delta": delta, "ray_supremum": direct, "half_cot_delta": trig})

stable = []
radii = [10 ** (-6 + j * 18 / 120) for j in range(121)]
for alpha, drift in ((0.5, True), (0.5, False), (1.0, True), (1.5, True), (2.0, True)):
    if not drift:
        drift_bound = 0.0
    elif alpha == 1:
        drift_bound = math.sqrt(2)
    elif alpha > 1:
        drift_bound = math.sqrt(2) * (alpha - 1) ** ((alpha - 1) / alpha) / alpha
    else:
        drift_bound = None
    upper = None if drift_bound is None else drift_bound + 0.7
    largest = 0.0
    for j in range(720):
        theta = math.pi * j / 720
        ex, ey = math.cos(theta), math.sin(theta)
        for radius in radii:
            x, y = radius * ex, radius * ey
            phase = x + 2 * y
            real = radius ** alpha + 0.7 * (1 - math.cos(phase))
            imag = -(x - y) * drift - 0.7 * math.sin(phase)
            value = ratio(real, imag)
            largest = max(largest, value)
            if upper is not None:
                assert value <= upper * (1 + 1e-12)
    stable.append({"alpha": alpha, "drift_1_minus1": drift,
                   "largest_finite_grid_ratio": largest,
                   "proved_sector_upper_bound": upper,
                   "directions": 720, "radii": len(radii),
                   "radius_min": min(radii), "radius_max": max(radii)})

with (root / "data" / "gaussian_direction_checks.csv").open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(("epsilon", "theta_radians", "ray_sector_supremum", "maximizing_radius"))
    writer.writerows(angular_rows)

result = {"purpose": "finite numerical evidence only; proofs are in REPORT.md",
          "nice_priority": priority, "threads": 1,
          "exact_rational_covariance_checks": exact_checks,
          "gaussian": gaussian, "exact_exceptional_direction": exceptional,
          "near_exceptional": near_exceptional, "stable_plus_compound_poisson": stable,
          "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(root / "data" / "sector_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
