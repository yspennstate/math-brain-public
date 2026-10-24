"""Deterministic controls for ATTEMPT.md; no numerical result is a proof audit."""
from __future__ import annotations

import cmath
import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
receipts: list[dict] = []


def require(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


# Explicitly independent fair signs; enumerate only eight small exact pair laws.
variance_controls = []
q_vertex = 6.0
sign_amplitude = math.pi / (2.0 * q_vertex)
for shells in range(1, 9):
    values = [sign_amplitude * sum(1 if mask & (1 << j) else -1 for j in range(shells))
              for mask in range(1 << shells)]
    mean = math.fsum(values) / len(values)
    variance = math.fsum((value - mean) ** 2 for value in values) / len(values)
    vertex = sum(cmath.exp(1j * q_vertex * value) for value in values) / len(values)
    gaussian_vertex = math.exp(-0.5 * q_vertex ** 2 * variance)
    require(abs(variance - sign_amplitude ** 2 * shells) < 1e-13, "C1 variance")
    require(abs(vertex) < 1e-13, "C1 exact zero up to roundoff")
    require(gaussian_vertex > 0, "C1 falsely predicts a positive Gaussian vertex")
    variance_controls.append({"shells": shells, "variance": variance,
                              "actual_vertex_abs": abs(vertex),
                              "variance_only_prediction": gaussian_vertex})
receipts.append({"check": "C1", "cases": len(variance_controls),
                 "max_actual_vertex_abs": max(row["actual_vertex_abs"] for row in variance_controls),
                 "details": variance_controls})

# Positive circular densities, with an independently evaluated TV integral.
grid_size = 4096
step = 2.0 * math.pi / grid_size
fourier_terms = 12
circular_controls = []
for first_mode in (0.25, 0.125, 0.03125):
    before, after, differences, first_before, first_after = [], [], [], [], []
    imaginary_after = []
    for j in range(grid_size):
        angle = (j + 0.5) * step
        p_density = (1.0 + 2.0 * math.fsum(
            first_mode ** (n * n) * math.cos(n * angle)
            for n in range(1, fourier_terms + 1))) / (2.0 * math.pi)
        q_density = p_density - first_mode * math.cos(angle) / math.pi
        before.append(p_density)
        after.append(q_density)
        differences.append(abs(p_density - q_density))
        first_before.append(p_density * math.cos(angle))
        first_after.append(q_density * math.cos(angle))
        imaginary_after.append(q_density * math.sin(angle))
    p_mass = math.fsum(before) * step
    q_mass = math.fsum(after) * step
    p_vertex = math.fsum(first_before) * step
    q_first_vertex = complex(math.fsum(first_after) * step, math.fsum(imaginary_after) * step)
    tv = 0.5 * math.fsum(differences) * step
    exact_tv = 2.0 * first_mode / math.pi
    tail = first_mode ** ((fourier_terms + 1) ** 2) / (1.0 - first_mode ** (2 * fourier_terms + 3))
    analytic_q_min = (1.0 - 2.0 * first_mode ** 4 / (1.0 - first_mode ** 2)) / (2.0 * math.pi)
    require(abs(p_mass - 1.0) < 1e-12 and abs(q_mass - 1.0) < 1e-12, "C2 normalization")
    require(abs(p_vertex - first_mode) < 1e-12 and abs(q_first_vertex) < 1e-12, "C2 Fourier cancellation")
    require(min(after) >= analytic_q_min - tail / math.pi - 1e-12, "C2 positivity")
    require(abs(tv / exact_tv - 1.0) < 2e-6, "C2 independent TV integral")
    circular_controls.append({"first_mode_before": p_vertex, "first_mode_after_abs": abs(q_first_vertex),
                              "density_min_after": min(after), "analytic_density_lower_bound": analytic_q_min,
                              "measured_tv": tv, "exact_tv": exact_tv,
                              "tv_relative_error": abs(tv / exact_tv - 1.0),
                              "discarded_fourier_tail_bound": tail})
receipts.append({"check": "C2", "cases": len(circular_controls), "grid_size": grid_size,
                 "details": circular_controls})

# Gaussian plus explicitly independent rare signs on dyadic scales. The finite
# product is valid ONLY for this toy law; it is not applied to dependent defects.
eta = 0.2
spike_amplitude = 0.1
activity_total_bound = 0.1  # sum_{j>=0} 0.05 * 2^(-j)
variance_error_bound = spike_amplitude ** 2 * activity_total_bound
higher_cumulant_bound = 2.0 * activity_total_bound * (math.cosh(q_vertex * spike_amplitude) - 1.0)
log_error_bound = q_vertex ** 2 * variance_error_bound / 2.0 + higher_cumulant_bound
toy_controls = []
for shells in range(10, 37):
    radius = 2.0 ** shells
    probabilities = [0.05 * 2.0 ** (-j) for j in range(shells)]
    factors = [1.0 - prob + prob * math.cos(q_vertex * spike_amplitude) for prob in probabilities]
    correction = math.prod(factors)
    vertex = radius ** (-eta) * correction
    variance = (2.0 * eta / q_vertex ** 2) * math.log(radius) + spike_amplitude ** 2 * math.fsum(probabilities)
    require(math.exp(-log_error_bound) <= correction <= math.exp(log_error_bound), "L1 toy vertex bounds")
    require(abs(variance - (2.0 * eta / q_vertex ** 2) * math.log(radius)) <= variance_error_bound + 1e-14,
            "L1 toy variance remainder")
    leading_amplitude = 0.7
    microscopic_error = 0.01 * radius ** (-eta - 0.3)
    microscopic_correlation = leading_amplitude * vertex - microscopic_error
    threshold = (2.0 * 0.01 * math.exp(log_error_bound) / leading_amplitude) ** (1.0 / 0.3)
    if radius >= max(2.0, threshold):
        require(microscopic_correlation >= 0.5 * leading_amplitude * math.exp(-log_error_bound) * radius ** (-eta),
                "L3 insertion-error threshold")
    toy_controls.append({"shells": shells, "radius": radius, "scaled_vertex": correction,
                         "microscopic_correlation": microscopic_correlation})
receipts.append({"check": "L1/L3-toy", "cases": len(toy_controls),
                 "lower_scaled_vertex_bound": math.exp(-log_error_bound),
                 "upper_scaled_vertex_bound": math.exp(log_error_bound),
                 "min_measured_scaled_vertex": min(row["scaled_vertex"] for row in toy_controls),
                 "max_measured_scaled_vertex": max(row["scaled_vertex"] for row in toy_controls),
                 "details": toy_controls})

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
required = {"id", "statement", "assumptions", "source", "proof_or_counterexample",
            "independent_reviewer", "remaining_gap", "status", "review_status"}
for claim in claims:
    require(required <= set(claim), "claim ledger completeness")
    require(claim["status"] != "independently checked proof" or claim["review_status"] != "pending",
            "pending review cannot count as an independent proof")
require(len({claim["id"] for claim in claims}) == len(claims), "unique claim IDs")
elapsed = time.perf_counter() - started
require(elapsed < 60, "fresh compute gate")
result = {"command": "python -X utf8 verify_transfer.py", "date": "2026-10-10", "agent": "w540",
          "passed": True, "classification": "deterministic controls; not a Riesz phase proof or independent audit",
          "claim_rows": len(claims), "counterexample_cases": 11, "positive_toy_cases": 27,
          "elapsed_seconds": elapsed, "checks": receipts}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: result[key] for key in ("passed", "claim_rows", "counterexample_cases", "positive_toy_cases", "elapsed_seconds")}))
