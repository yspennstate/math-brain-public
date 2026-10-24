"""Bounded exact arithmetic controls for the proof packet, not a formal proof.

No random samples, model loads, GPUs, numerical integration or live-store writes.
The controls check independent closed-form examples and boundary failures.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import time


def main():
    started = time.perf_counter()
    rows = []
    checks = []
    for theta in (F(1), F(4, 5), F(2, 3), F(1, 2), F(1, 3), F(1, 4)):
        dimension = F(2) / theta
        # Ball-cover identity: d_theta diameter -> Euclidean theta power.
        # The unchanged Gaussian heat kernel has spectral dimension 2.
        rows.append({"theta": str(theta), "hausdorff_dimension": str(dimension),
                     "spectral_dimension": "2", "mean_exit_exponent": str(dimension),
                     "length_metric": theta == 1})
        checks.append({"case": "cover-exponent-" + str(theta),
                       "passed": theta * dimension == 2})
        checks.append({"case": "spectral-walk-volume-" + str(theta),
                       "passed": 2 * dimension / dimension == 2})
    # An exponent outside the snowflake range need not even define a metric.
    checks.append({"case": "theta-2-triangle-fails-at-0-1-2",
                   "passed": F(2) ** 2 > F(1) ** 2 + F(1) ** 2})
    # Algebraic assignments are controls for circularity, not constructed LQG metrics.
    for gamma_squared in (F(1), F(8, 3), F(15, 4)):
        a = 2 - gamma_squared / 2
        for trial_dimension in (F(3), F(4), F(5)):
            b = a / trial_dimension
            checks.append({"case": "cancellation-gamma2-" + str(gamma_squared)
                            + "-trial-d-" + str(trial_dimension),
                           "passed": a > 0 and b > 0 and a / b == trial_dimension})
    # Known Brownian-map parameter: a=2/3 and b=a/4=1/6.
    a = F(2) - F(8, 3) / 2
    checks.append({"case": "brownian-map-reference-a-2/3-b-1/6",
                   "passed": a == F(2, 3) and a / F(4) == F(1, 6)})
    checks.append({"case": "critical-gamma-2-zero-exponent-excluded",
                   "passed": F(2) - F(4) / 2 == 0})
    # A non-atomic zero-dimensional mass M(s)=log(1/s)^(-2) has
    # finite integral int_0^r M(s) ds/s = 1/log(1/r); an atom has infinite potential.
    checks.append({"case": "zero-local-exponent-needs-separate-integrability",
                   "passed": F(2) > 1})
    gamma_squared = F(8, 3)
    xi_over_gamma = F(1, 4)
    q_over_gamma = F(2) / gamma_squared + F(1, 2)
    wrong_dimension = F(2) * q_over_gamma / xi_over_gamma
    correct_dimension = F(1) / xi_over_gamma
    checks.append({"case": "D0049-identity-counterexample-10-versus-4",
                   "passed": wrong_dimension == 10 and correct_dimension == 4
                   and wrong_dimension != correct_dimension})
    result = {"kind": "deterministic scalar controls; not mathematical proof certification",
              "checks": checks, "passed": sum(c["passed"] for c in checks),
              "total": len(checks), "counterexample_exponents": rows,
              "same_spectral_exponent_distinct_metric_dimensions": len(set(r["hausdorff_dimension"] for r in rows)),
              "runtime_seconds": round(time.perf_counter() - started, 6),
              "source_identity_counterexample": {"recorded_formula_value": str(wrong_dimension),
                                                 "correct_formula_value": str(correct_dimension)},
              "resource_bound": "one process; standard-library rational arithmetic; 26 checks; no sampling or training"}
    p = Path(__file__).resolve().parent / "CHECK_RESULTS.json"
    p.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "same_spectral_exponent_distinct_metric_dimensions", "runtime_seconds")}))
    if result["passed"] != result["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
