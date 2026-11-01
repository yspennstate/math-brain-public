"""Small gated reproduction of ATTEMPT.md L6; standard library only."""
from __future__ import annotations

import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LAM = math.sqrt(2.0)
SQRT2 = math.sqrt(2.0)
NORMAL = 1.0 / math.sqrt(2.0 * math.pi)
GATE = json.loads((ROOT / "compute_gate.json").read_text(encoding="utf-8"))
START = time.perf_counter()
EVALUATIONS = 0


def posterior(y: float) -> tuple[float, float, float]:
    global EVALUATIONS
    EVALUATIONS += 1
    if EVALUATIONS > GATE["max_posterior_evaluations"]:
        raise RuntimeError("fresh gate's evaluation budget exhausted")
    if EVALUATIONS % 1000 == 0 and time.perf_counter() - START > GATE["max_runtime_seconds"]:
        raise RuntimeError("fresh gate's runtime budget exhausted")
    y0 = abs(y)
    pos, neg = y0 - LAM, y0 + LAM
    cdf_pos = 0.5 * math.erfc(-pos / SQRT2)
    cdf_neg = 0.5 * math.erfc(neg / SQRT2)
    pdf_pos = NORMAL * math.exp(-pos * pos / 2.0)
    pdf_neg = NORMAL * math.exp(-neg * neg / 2.0)
    ratio = math.exp(2.0 * LAM * y0)
    norm = cdf_pos + ratio * cdf_neg
    first = (pos * cdf_pos + pdf_pos + ratio * (neg * cdf_neg - pdf_neg)) / norm
    second = ((pos * pos + 1.0) * cdf_pos + pos * pdf_pos
              + ratio * ((neg * neg + 1.0) * cdf_neg - neg * pdf_neg)) / norm
    variance = second - first * first
    density_y = (LAM / 2.0) * math.exp(-LAM * y0 + LAM * LAM / 2.0) * norm
    return math.copysign(first, y), variance, density_y


def simpson(fn, lo: float, hi: float, steps: int) -> float:
    assert steps > 0 and steps % 2 == 0
    delta = (hi - lo) / steps
    total = fn(lo) + fn(hi)
    total += math.fsum((4.0 if k % 2 else 2.0) * fn(lo + delta * k)
                      for k in range(1, steps))
    return total * delta / 3.0


def weighted_ratio(location: float, s_steps: int, g_steps: int) -> float:
    def weight(s):
        return 0.0 if s <= 0.0 or s >= 1.0 else math.exp(-2.0 / (s * (1.0 - s)) - LAM * s)
    normalizer = simpson(lambda z: NORMAL * math.exp(-z*z/2), -8.0, 8.0, g_steps)
    denominator = simpson(weight, 0.0, 1.0, s_steps)
    def integrand(s):
        w = weight(s)
        if w == 0.0:
            return 0.0
        inner = simpson(lambda z: posterior(location+s+z)[1] * NORMAL * math.exp(-z*z/2),
                        -8.0, 8.0, g_steps) / normalizer
        return w * inner
    return simpson(integrand, 0.0, 1.0, s_steps) / denominator


def posterior_direct_quadrature(y: float) -> float:
    # Independent integration in the completed-square coordinate, not the truncated-normal formula.
    center = y - LAM
    def base(z):
        x = center + z
        factor = 1.0 if x >= 0.0 else math.exp(2.0 * LAM * x)
        return math.exp(-z*z/2.0) * factor
    mass = simpson(base, -12.0, 12.0, 4000)
    mean = simpson(lambda z: z * base(z), -12.0, 12.0, 4000) / mass
    second = simpson(lambda z: z*z * base(z), -12.0, 12.0, 4000) / mass
    return second - mean*mean


def main() -> None:
    rows = [{"y": y, "posterior_variance_over_t": posterior(y)[1]}
            for y in (0.0, 2.0, 4.0, 6.0, 8.0, 10.0)]
    checks = [{"y": y, "absolute_formula_vs_quadrature_error":
               abs(posterior(y)[1] - posterior_direct_quadrature(y))} for y in (0.0, 2.0, 6.0)]
    mean_a = simpson(lambda y: posterior(y)[1] * posterior(y)[2], -20.0, 20.0, 2000)
    mass_y = simpson(lambda y: posterior(y)[2], -20.0, 20.0, 2000)
    ratios = [{"L": location, "ratio": weighted_ratio(location, 40, 80)}
              for location in (0.0, 2.0, 4.0, 6.0, 8.0)]
    refined = weighted_ratio(6.0, 80, 160)
    refinement_error = abs(refined - next(row["ratio"] for row in ratios if row["L"] == 6.0))
    assert max(row["absolute_formula_vs_quadrature_error"] for row in checks) < 2e-6
    assert abs(mass_y - 1.0) < 2e-6
    assert mean_a <= 0.5 + 2e-6
    assert ratios[-1]["ratio"] > 0.99
    assert refinement_error < 2e-6
    receipt = {
        "task": "P0017 weighted-covariance shortcut", "gate": GATE,
        "command": "python -X utf8 measure_laplace.py",
        "unweighted_E_A": mean_a, "mmse_upper_bound": 0.5,
        "observation_density_integral_on_minus20_20": mass_y,
        "posterior_variances": rows, "weighted_ratios": ratios,
        "formula_cross_checks": checks, "L6_refined_ratio": refined,
        "L6_refinement_difference": refinement_error,
        "posterior_evaluations": EVALUATIONS, "elapsed_seconds": time.perf_counter()-START,
        "status": "floating-point reproduction; analytic proof is ATTEMPT.md L6",
        "KLS_proved": False,
    }
    (ROOT / "LAPLACE_MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
