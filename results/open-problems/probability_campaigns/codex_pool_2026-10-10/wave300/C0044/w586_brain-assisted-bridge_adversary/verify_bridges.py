"""Bounded exact checks for C0044 obstruction examples; writes only beside itself."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent


def first_jumps(shared_row: bool, d: int = 3) -> dict:
    # Enumerate conditional path probabilities, then average the row types.
    marginal_x = marginal_y = joint = F(0)
    row_types = (F(1, 4), F(3, 4))
    pairs = [(w, w, F(1, 2)) for w in row_types] if shared_row else [
        (a, b, F(1, 4)) for a, b in product(row_types, repeat=2)
    ]
    for wx, wy, environment_mass in pairs:
        px = [wx] + [(1 - wx) / (2 * d - 1)] * (2 * d - 1)
        py = [wy] + [(1 - wy) / (2 * d - 1)] * (2 * d - 1)
        assert sum(px) == sum(py) == 1
        assert min(px + py) >= F(1, 4 * (2 * d - 1))
        for a, b in product(range(2 * d), repeat=2):
            mass = environment_mass * px[a] * py[b]
            marginal_x += mass * (a == 0)
            marginal_y += mass * (b == 0)
            joint += mass * (a == b == 0)
    return {
        "marginal_x": str(marginal_x), "marginal_y": str(marginal_y),
        "naive_product": str(marginal_x * marginal_y),
        "exact_joint": str(joint),
        "absolute_product_error": str(abs(joint - marginal_x * marginal_y)),
        "conditional_y_given_x": str(joint / marginal_x),
    }


def conditioning_on_nonintersection(d: int = 3) -> dict:
    steps = []
    for i in range(d):
        for sign in (1, -1):
            steps.append(tuple(sign if j == i else 0 for j in range(d)))
    start_y = (2,) + (0,) * (d - 1)
    h = fh = gh = fgh = F(0)
    for a, b in product(steps, repeat=2):
        end_y = tuple(x + y for x, y in zip(start_y, b))
        mass = F(1, (2 * d) ** 2)
        nonintersection = a != end_y
        event_f = a == steps[0]
        event_g = b == steps[1]
        if nonintersection:
            h += mass
            fh += mass * event_f
            gh += mass * event_g
            fgh += mass * event_f * event_g
    return {
        "conditioning_probability": str(h),
        "conditional_f": str(fh / h), "conditional_g": str(gh / h),
        "conditional_joint": str(fgh / h),
        "product_of_conditional_marginals": str(fh * gh / h ** 2),
        "departure_rows": ["0", "2e1"],
        "environment": "deterministic simple symmetric nearest-neighbor law (degenerate iid)",
    }


def cesaro_density_tail(n: int, threshold: int) -> dict:
    # k successes before the first failure. The last state includes all longer runs.
    values = [(F(2 ** (k + 1) - 1, n), F(1, 2 ** (k + 1)))
              for k in range(n - 1)]
    values.append((F(2 ** n - 1, n), F(1, 2 ** (n - 1))))
    assert sum(p for _, p in values) == 1
    mean = sum(v * p for v, p in values)
    assert mean == 1
    tail = sum(v * p for v, p in values if v > threshold)
    return {"N": n, "K": threshold, "mean": str(mean),
            "tail_expectation_exact": str(tail), "tail_expectation": float(tail)}


def main() -> None:
    gate = json.loads((ROOT / "COMPUTE_GATE.json").read_text(encoding="utf-8"))
    started = time.perf_counter()
    shared, fresh = first_jumps(True), first_jumps(False)
    conditioned = conditioning_on_nonintersection()
    assert shared["exact_joint"] == "5/16" and shared["naive_product"] == "1/4"
    assert fresh["exact_joint"] == fresh["naive_product"] == "1/4"
    assert conditioned["conditional_joint"] == "0"
    assert conditioned["product_of_conditional_marginals"] == "1/49"
    density = [cesaro_density_tail(n, 16) for n in (16, 64, 128)]
    result = {
        "command": "python -X utf8 ~/brain_workers/w586/verify_bridges.py",
        "arithmetic": "exact rational enumeration; no Monte Carlo",
        "shared_row": shared, "disjoint_unconditioned_rows": fresh,
        "disjoint_rows_joint_conditioning": conditioned,
        "cesaro_mass_one_not_ui": density,
        "proposed_repair": {
            "rule": "Multiply only after certifying disjoint row dependencies and compatible conditioning; otherwise average the quenched joint or retain a proof gap.",
            "before_unsafe_products": 2, "after_unjustified_products_allowed": 0,
            "correct_disjoint_control_retained": 1,
            "scope": "These three constructed cases only; manual hypothesis repair, not a live-engine benchmark or deployment."
        },
        "elapsed_arithmetic_s": time.perf_counter() - started,
        "checks_passed": True,
    }
    assert result["elapsed_arithmetic_s"] < gate["max_arithmetic_seconds"]
    rendered = json.dumps(result, indent=2)
    assert len(rendered.encode("utf-8")) < gate["max_artifact_bytes"]
    (ROOT / "MEASUREMENTS.json").write_text(rendered, encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
