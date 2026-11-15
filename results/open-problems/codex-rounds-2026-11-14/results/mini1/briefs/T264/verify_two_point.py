#!/usr/bin/env python3
"""Independent, deterministic checks of the formulas in PROOF.md.

Uses only the standard library, constant working memory, and one thread.
Run from this folder. Output files: verification_data.json and angle_checks.csv.
"""

import csv
import json
import math
import os
import resource
import signal
import sys
import time
from pathlib import Path


assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
assert Path.cwd().resolve() == ROOT
PI = math.pi
TAU = 2 * PI


def rel_error(a, b):
    return abs(a - b) / max(abs(b), 1e-300)


def sphere_risk(theta, d):
    if theta <= PI / 2:
        return (PI - math.sin(theta) + theta * math.cos(theta)) / (
            PI * d * math.sin(theta) ** 2
        )
    return (PI - math.sin(theta) - (PI - theta) * math.cos(theta)) / (PI * d)


def evaluate(theta, x, y, biased=False):
    a = math.cos(theta / 2)
    b = math.sin(theta / 2)
    if biased:
        # Stable evaluation of the actual two affine ReLU units, not the bounds.
        m = b * b * (1 + a * x)
        t = (1 + a * a) * b * y
        denom = 2 * b * b * (1 + a * a)
        return (max(m + t, 0) - max(m - t, 0)) / denom
    if theta <= PI / 2:
        return (max(b * x + a * y, 0) - max(b * x - a * y, 0)) / math.sin(theta)
    return max(a * x + b * y, 0) - max(a * x - b * y, 0)


def circle_risk(theta, biased=False, steps=32768):
    return math.fsum(
        evaluate(theta, math.cos(TAU * (i + 0.5) / steps),
                 math.sin(TAU * (i + 0.5) / steps), biased) ** 2
        for i in range(steps)
    ) / steps


def direct_sphere3_risk(theta, biased=False, n_z=256, n_phi=2048):
    # z is uniform on [-1,1], phi is uniform on [0,2pi].
    # This integrates network values on S^2 without using a kernel formula.
    def terms():
        for k in range(n_z):
            z = -1 + 2 * (k + 0.5) / n_z
            radius = math.sqrt(1 - z * z)
            for i in range(n_phi):
                phi = TAU * (i + 0.5) / n_phi
                value = evaluate(theta, radius * math.cos(phi),
                                 radius * math.sin(phi), biased)
                yield value * value
    return math.fsum(terms()) / (n_z * n_phi)


def simpson(fn, left, right, steps=8192):
    assert steps % 2 == 0
    h = (right - left) / steps
    weighted = math.fsum(
        (4 if i % 2 else 2) * fn(left + i * h)
        for i in range(1, steps)
    )
    return h / 3 * (fn(left) + fn(right) + weighted)


def angle_constant(d):
    return math.gamma(d / 2) / (math.sqrt(PI) * math.gamma((d - 1) / 2))


data = {"angle_checks": [], "sphere3_checks": [], "truncated_means": [],
        "tail_checks": [], "angle_normalizations": []}

# Directly search the planar atomic dictionary, including the two exposed atoms.
angles = [0.001, 0.02, 0.3, 0.8, PI / 2, 2.0, 2.8, 3.13]
max_quadrature_error = 0.0
max_pricing_gap = 0.0
for theta in angles:
    a, b = math.cos(theta / 2), math.sin(theta / 2)
    interpolation_error = max(
        abs(evaluate(theta, a, b) - 1),
        abs(evaluate(theta, a, -b) + 1),
        abs(evaluate(theta, a, b, True) - 1),
        abs(evaluate(theta, a, -b, True) + 1),
    )
    assert interpolation_error < 1e-11
    measured_price = max(
        abs(max(a * math.cos(TAU * i / 65536) + b * math.sin(TAU * i / 65536), 0)
            - max(a * math.cos(TAU * i / 65536) - b * math.sin(TAU * i / 65536), 0))
        for i in range(65536)
    )
    exact_price = math.sin(theta) if theta < PI / 2 else 1.0
    pricing_gap = (exact_price - measured_price) / exact_price
    assert -1e-11 <= pricing_gap < 2e-4
    max_pricing_gap = max(max_pricing_gap, pricing_gap)
    direct = circle_risk(theta)
    formula = sphere_risk(theta, 2)
    err = rel_error(direct, formula)
    max_quadrature_error = max(max_quadrature_error, err)
    assert err < 1e-7
    direct_b = circle_risk(theta, True)
    lower = 1 / (8 * math.sin(theta / 2) ** 2)
    upper = 4 * lower
    assert lower * (1 - 1e-10) <= direct_b <= upper * (1 + 1e-10)
    # Scan a disk, checking the bias bound where m can be smallest.
    pointwise_violation = 0.0
    for radius in (0.0, 0.25, 0.8, 1.0):
        for i in range(1024):
            phi = TAU * (i + 0.5) / 1024
            x, y = radius * math.cos(phi), radius * math.sin(phi)
            actual = abs(evaluate(theta, x, y, True))
            linear = abs(y / b)
            pointwise_violation = max(pointwise_violation,
                                      0.5 * linear - actual, actual - linear)
    assert pointwise_violation < 1e-10
    data["angle_checks"].append({
        "theta": theta, "interpolation_error": interpolation_error,
        "price_grid": measured_price, "price_exact": exact_price,
        "risk_circle": direct, "risk_formula_d2": formula,
        "risk_bias_circle": direct_b, "relative_risk_error": err,
        "pointwise_bias_violation": pointwise_violation,
    })

# A separate three-dimensional surface quadrature checks the 1/d normalization.
for theta in (0.02, 0.37, 2.0):
    direct = direct_sphere3_risk(theta)
    formula = sphere_risk(theta, 3)
    assert rel_error(direct, formula) < 3e-5, (theta, direct, formula, rel_error(direct, formula))
    biased = direct_sphere3_risk(theta, True)
    lower = 1 / (12 * math.sin(theta / 2) ** 2)
    assert lower * (1 - 3e-5) <= biased <= 4 * lower * (1 + 3e-5)
    data["sphere3_checks"].append({"theta": theta, "direct": direct,
                                  "formula": formula, "direct_bias": biased,
                                  "relative_error": rel_error(direct, formula)})

# The angular normalizer is checked independently by the sine-integral recurrence.
sine_integrals = {2: PI, 3: 2.0}
for d in range(2, 9):
    if d >= 4:
        sine_integrals[d] = (d - 3) / (d - 2) * sine_integrals[d - 2]
    gamma_value = angle_constant(d)
    recurrence_value = 1 / sine_integrals[d]
    assert rel_error(gamma_value, recurrence_value) < 2e-15
    data["angle_normalizations"].append({"d": d, "gamma": gamma_value,
                                          "recurrence": recurrence_value})

# Conditional opposite-label means, integrating in log(theta).
for d in (2, 3, 4, 5):
    previous = None
    for eps in (1e-1, 1e-2, 1e-3, 1e-4):
        def transformed(v):
            theta = math.exp(v)
            return (theta * angle_constant(d) * math.sin(theta) ** (d - 2)
                    * sphere_risk(theta, d))
        mean = simpson(transformed, math.log(eps), math.log(PI), 16384)
        row = {"d": d, "epsilon": eps, "conditional_truncated_mean": mean}
        if d == 2:
            row["epsilon_times_mean"] = eps * mean
        if d == 3 and previous is not None:
            row["increment_per_log10"] = (mean - previous) / math.log(10)
        data["truncated_means"].append(row)
        previous = mean

# Check closed finite means against the original-angle integral and omitted cap.
data["finite_conditional_means"] = []
for d, exact_mean in ((4, 3 / 8 + 1 / (3 * PI) - 13 / (9 * PI * PI)),
                      (5, 55 / 256)):
    # Restore the omitted acute cap to the independently computed log-angle integral.
    row = next(row for row in data["truncated_means"]
               if row["d"] == d and row["epsilon"] == 1e-4)
    cap = simpson(lambda t: angle_constant(d) / (PI * d)
                  * math.sin(t) ** (d - 4)
                  * (PI - math.sin(t) + t * math.cos(t)), 0, 1e-4, 512)
    restored = row["conditional_truncated_mean"] + cap
    assert abs(restored - exact_mean) < 1e-7
    data["finite_conditional_means"].append({"d": d, "quadrature": restored,
                                            "exact": exact_mean,
                                            "absolute_error": abs(restored - exact_mean)})

# Tail constants: solve the risk threshold, then integrate the angular cap.
for d in (2, 3, 4, 5):
    alpha = (d - 1) / 2
    predicted = angle_constant(d) / (2 * (d - 1) * d ** alpha)
    for threshold in (1e4, 1e6, 1e8):
        lo, hi = 1e-12, 0.1
        for _ in range(70):
            mid = (lo + hi) / 2
            if sphere_risk(mid, d) > threshold:
                lo = mid
            else:
                hi = mid
        cutoff = (lo + hi) / 2
        cap = simpson(lambda t: angle_constant(d) * math.sin(t) ** (d - 2),
                      0.0, cutoff, 512)
        measured = 0.5 * cap * threshold ** alpha
        assert rel_error(measured, predicted) < 3e-5
        data["tail_checks"].append({"d": d, "threshold": threshold,
                                     "scaled_unconditional_tail": measured,
                                     "predicted_constant": predicted,
                                     "relative_error": rel_error(measured, predicted)})

# Leading coefficient with and without biases, using direct network integration.
data["singular_coefficients"] = []
for theta in (0.1, 0.01, 0.001):
    direct = circle_risk(theta)
    direct_b = circle_risk(theta, True)
    data["singular_coefficients"].append({
        "theta": theta, "homogeneous_2theta2R": 2 * theta * theta * direct,
        "biased_2theta2R": 2 * theta * theta * direct_b,
    })
assert abs(data["singular_coefficients"][-1]["homogeneous_2theta2R"] - 1) < 1e-5
assert abs(data["singular_coefficients"][-1]["biased_2theta2R"] - 1) < 1e-3

# Independently integrate the radial multiplier, rather than using an antiderivative.
radial = math.fsum((1 + (i + 0.5) / 10000) ** 2 for i in range(10000)) / 10000
assert abs(radial - 7 / 3) < 1e-8
data["radial_multiplier"] = {"midpoint_quadrature": radial, "exact": 7 / 3}

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == "darwin" else 1024 * rss
assert rss_bytes < 1_000_000_000
data["resources"] = {"elapsed_seconds": time.monotonic() - started,
                     "peak_rss_bytes": rss_bytes,
                     "nice": os.getpriority(os.PRIO_PROCESS, 0),
                     "OMP_NUM_THREADS": os.environ["OMP_NUM_THREADS"]}

(ROOT / "verification_data.json").write_text(json.dumps(data, indent=2) + "\n")
with (ROOT / "angle_checks.csv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(data["angle_checks"][0]))
    writer.writeheader()
    writer.writerows(data["angle_checks"])

print("PASS: interpolation, explicit dual pricing, and planar atom grid")
print(f"Maximum relative gap below exact dual price: {max_pricing_gap:.6g}")
print(f"Maximum relative circle-risk error: {max_quadrature_error:.6g}")
print("PASS: independent S^2 surface quadrature and bias pointwise bounds")
print("PASS: gamma normalizers equal sine-integral recurrence, d=2..8")
print("Conditional opposite-label truncated squared risks:")
for row in data["truncated_means"]:
    print(f"  d={row['d']} epsilon={row['epsilon']:.0e} mean={row['conditional_truncated_mean']:.10g}")
print("PASS: unconditional risk-tail constants, d=2..5, thresholds=1e4,1e6,1e8")
for row in data["finite_conditional_means"]:
    print(f"PASS: d={row['d']} opposite-label mean: quadrature={row['quadrature']:.12g}, "
          f"exact={row['exact']:.12g}")
for row in data["singular_coefficients"]:
    print(f"theta={row['theta']:g}: 2*theta^2*R={row['homogeneous_2theta2R']:.10g}, "
          f"with_bias={row['biased_2theta2R']:.10g}")
print(f"PASS: annulus radial multiplier {radial:.12g}, exact 7/3={7/3:.12g}")
print("All assertions passed. Data: verification_data.json, angle_checks.csv")
print(f"Resources: {data['resources']}")
