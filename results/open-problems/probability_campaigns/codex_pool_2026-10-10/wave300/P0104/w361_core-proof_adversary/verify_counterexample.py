"""Exact finite calculation. No sampling, store access, or nonlocal writes."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import time


def covariance(counts):
    total = sum(counts.values())
    ex = sum(Q(x * c, total) for (x, y), c in counts.items())
    ey = sum(Q(y * c, total) for (x, y), c in counts.items())
    exy = sum(Q(x * y * c, total) for (x, y), c in counts.items())
    var_x = sum(Q(x * x * c, total) for (x, y), c in counts.items()) - ex * ex
    var_y = sum(Q(y * y * c, total) for (x, y), c in counts.items()) - ey * ey
    var_sum = sum(Q((x + y) ** 2 * c, total) for (x, y), c in counts.items()) - (ex + ey) ** 2
    return exy - ex * ey, var_x + var_y, var_sum


def main():
    started = time.perf_counter()
    conditioned = Counter()
    selected = Counter()
    fixed = Counter()
    for x1, x2, y1, y2 in product((1, 2), repeat=4):
        upper = (x1, x2)
        lower = (y1, y2)
        fixed[upper] += 1
        if sum(upper) <= sum(lower):
            conditioned[upper] += 1
            selected[upper] += 1
        else:
            selected[lower] += 1
    cov_cond, additive_cond, actual_cond = covariance(conditioned)
    cov_sel, additive_sel, actual_sel = covariance(selected)
    cov_fixed, additive_fixed, actual_fixed = covariance(fixed)
    assert sum(conditioned.values()) == 11
    assert [conditioned[p] for p in ((1, 1), (1, 2), (2, 1), (2, 2))] == [4, 3, 3, 1]
    assert [selected[p] for p in ((1, 1), (1, 2), (2, 1), (2, 2))] == [7, 4, 4, 1]
    assert cov_cond == Q(-5, 121)
    assert cov_sel == Q(-9, 256)
    assert additive_sel == Q(55, 128)
    assert actual_sel == Q(23, 64)
    assert actual_sel == additive_sel + 2 * cov_sel
    assert actual_cond == additive_cond + 2 * cov_cond
    assert cov_fixed == 0 and actual_fixed == additive_fixed == Q(1, 2)
    total = sum(conditioned.values())
    p1 = Q(sum(c for (x, y), c in conditioned.items() if x == 2), total)
    p2 = Q(sum(c for (x, y), c in conditioned.items() if y == 2), total)
    joint = Q(conditioned[(2, 2)], total)
    assert joint == Q(1, 11) and p1 * p2 == Q(16, 121)
    # Continuous, unique-geodesic control: four iid Exp(1) edges.
    # Given the upper path wins, density is 2 exp(-2(x+y))(1+x+y).
    # Integrals of x^k exp(-2x) are k!/2^(k+1).
    import math
    moment = lambda k: Q(math.factorial(k), 2 ** (k + 1))
    normalization = 2 * (moment(0) ** 2 + 2 * moment(0) * moment(1))
    ex = 2 * (moment(1) * moment(0) + moment(2) * moment(0) + moment(1) ** 2)
    exy = 2 * (moment(1) ** 2 + 2 * moment(2) * moment(1))
    assert normalization == 1 and ex == Q(5, 8) and exy == Q(3, 8)
    assert exy - ex * ex == Q(-1, 64)
    result = {
        "command": "python -X utf8 -B verify_counterexample.py",
        "assignments_checked": 16,
        "conditioned_counts": {str(k): v for k, v in sorted(conditioned.items())},
        "selected_counts": {str(k): v for k, v in sorted(selected.items())},
        "conditional_joint": str(joint),
        "false_independent_product": str(p1 * p2),
        "conditional_covariance": str(cov_cond),
        "selected_covariance": str(cov_sel),
        "baseline_additive_variance": str(additive_sel),
        "corrected_actual_variance": str(actual_sel),
        "baseline_relative_overestimate": str(additive_sel / actual_sel - 1),
        "fixed_path_negative_control_covariance": str(cov_fixed),
        "continuous_unique_path_conditional_covariance": "-1/64",
        "method": "exact rational enumeration and exact gamma integrals; not a formal proof receipt",
        "independent_review": "pending w362",
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    Path("COUNTEREXAMPLE_RECEIPT.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
