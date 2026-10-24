"""Bounded exact diagnostics; not a proof certificate or stochastic experiment."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
NOW = datetime.now(timezone.utc)
GATE = {
    "purpose": "Exact finite-chain checks of C0041 boundary formulas",
    "created_at": NOW.isoformat(),
    "expires_at": (NOW + timedelta(minutes=10)).isoformat(),
    "max_wall_seconds": 60,
    "max_environments": 504,
    "max_matrix_dimension": 7,
    "gpu": False,
    "training": False,
    "random_simulation": False,
    "cores": 1,
    "permission_basis": "Assigned small, fresh-gated mathematical diagnostics only",
}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(GATE, indent=2) + "\n", encoding="utf-8")


def solve(matrix, vector):
    """Exact Gaussian elimination for the finite I-Q hitting-time equations."""
    a = [row[:] + [v] for row, v in zip(matrix, vector)]
    n = len(a)
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        divisor = a[k][k]
        a[k] = [x / divisor for x in a[k]]
        for i in range(n):
            if i != k:
                factor = a[i][k]
                a[i] = [x - factor * y for x, y in zip(a[i], a[k])]
    return [row[-1] for row in a]


def reflected_crossing(ps):
    # States -L,...,0; -L reflects deterministically right; 1 is absorbing.
    n = len(ps) + 1
    matrix = [[F(i == j) for j in range(n)] for i in range(n)]
    matrix[0][1] -= 1
    for i, p in enumerate(ps, start=1):
        matrix[i][i - 1] -= 1 - p
        if i + 1 < n:
            matrix[i][i + 1] -= p
    return solve(matrix, [F(1)] * n)[-1]


rows = []
environments = 0
for a in [F(1, 2), F(3, 5), F(3, 4), F(4, 5)]:
    m = (1 - a) * 3 + a / 3
    A = (1 - a) * 4 + a * F(4, 3)
    for length in range(1, 7):
        total = F(0)
        weight = F(0)
        for good in product([False, True], repeat=length):
            if time.monotonic() - START > GATE["max_wall_seconds"]:
                raise RuntimeError("fresh compute gate wall limit reached")
            ps = [F(3, 4) if b else F(1, 4) for b in good]
            probability = a ** sum(good) * (1 - a) ** (length - sum(good))
            total += probability * reflected_crossing(ps)
            weight += probability
            environments += 1
        expected = A * sum(m ** k for k in range(length)) + m ** length
        assert weight == 1
        assert total == expected, (a, length, total, expected)
        rows.append({"a": str(a), "L": length, "matrix_mean": str(total), "formula_mean": str(expected)})

assert environments == 504
critical = [{"L": length, "lower_bound": 2 * length + 1} for length in [1, 2, 4, 6, 32, 100]]
families = []
for d in [2, 3, 8]:
    kappa = F(1, 4 * d)
    for exponent in [0, 4, 10, 20]:
        epsilon = kappa / 2 ** exponent
        b = F(1, 2 * d)
        probs = [b + epsilon, b - epsilon] + [b] * (2 * d - 2)
        assert sum(probs) == 1 and min(probs) >= kappa
        families.append({"d": d, "kappa": str(kappa), "epsilon": str(epsilon), "speed": str(2 * epsilon), "crossing_mean": str(1 / (2 * epsilon))})
    for p in [F(1, 4), F(3, 4)]:
        layered = [p / 2, (1 - p) / 2] + [F(1, 4 * (d - 1))] * (2 * d - 2)
        assert sum(layered) == 1
        assert min(layered) == min(F(1, 8), F(1, 4 * (d - 1)))

a = F(3, 4)
covariance = a - a * a
assert covariance == F(3, 16)
mean_layer_drift = a * F(1, 4) + (1 - a) * F(-1, 4)
assert mean_layer_drift == F(1, 8)
same_site_rho_square = a / 9 + (1 - a) * 9
distinct_site_rho_product = (a / 3 + (1 - a) * 3) ** 2
assert same_site_rho_square == F(7, 3)
assert distinct_site_rho_product == 1

receipt = {
    "command": "python -X utf8 ~/brain_workers/w451/verify_boundary.py",
    "result": "PASS",
    "environment_count": environments,
    "matrix_formula_comparisons": len(rows),
    "critical_lower_bounds": critical,
    "homogeneous_family": families,
    "layered_covariance": str(covariance),
    "raw_mean_layer_drift": str(mean_layer_drift),
    "same_site_rho_square": str(same_site_rho_square),
    "distinct_site_rho_product": str(distinct_site_rho_product),
    "elapsed_seconds": time.monotonic() - START,
    "scope": "Exact finite rational calculations; does not prove transience, SLLNs, or the parent conjecture",
    "formal_check": False,
    "finite_matrix_rows": rows,
}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: receipt[key] for key in ["result", "environment_count", "matrix_formula_comparisons", "layered_covariance", "raw_mean_layer_drift", "elapsed_seconds"]}))
