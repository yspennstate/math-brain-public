"""Independent finite hitting-matrix check of the critical inverse escape formula."""
from datetime import datetime, timedelta, timezone
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import time
root = Path(__file__).resolve().parent
start = time.monotonic()
now = datetime.now(timezone.utc)
gate = {"purpose": "Finite hitting matrices for the critical inverse escape moment", "created_at": now.isoformat(), "expires_at": (now + timedelta(minutes=10)).isoformat(), "max_wall_seconds": 10, "max_environments": 126, "matrix_dimension": 6, "cores": 1, "gpu": False, "random_simulation": False}
(root / "INVERSE_COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")

def solve(matrix, vector):
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

rows = []
count = 0
for height in range(1, 7):
    inverse_mean = F(0)
    for bits in product([False, True], repeat=height):
        ps = [F(3, 4) if bit else F(1, 4) for bit in bits]
        matrix = [[F(i == j) for j in range(height)] for i in range(height)]
        rhs = [F(0)] * height
        for i, p in enumerate(ps):
            if i > 0:
                matrix[i][i - 1] -= 1 - p
            if i + 1 < height:
                matrix[i][i + 1] -= p
            else:
                rhs[i] = p
        hit_probability = solve(matrix, rhs)[0]
        assert 0 < hit_probability <= 1
        probability = F(3, 4) ** sum(bits) * F(1, 4) ** (height - sum(bits))
        inverse_mean += probability / hit_probability
        count += 1
    assert inverse_mean == height + 1
    rows.append({"N": height, "matrix_mean_inverse_crossing_probability": str(inverse_mean), "series_formula": height + 1})
assert count == 126
receipt = {"command": "python -X utf8 ~/brain_workers/w451/verify_inverse_boundary.py", "result": "PASS", "environments": count, "independent_matrix_comparisons": 6, "finite_height_rows": rows, "half_inverse_moment_upper_bound": 4 + 2 * math.sqrt(3), "half_moment_factor": math.sqrt(3) / 2, "elapsed_seconds": time.monotonic() - start, "scope": "Finite exact checks of E[1/a_N]=N+1. Infinite inverse-moment threshold is proved analytically in INVERSE_MOMENT_BOUNDARY.md, not by these finite checks.", "formal_check": False}
assert receipt["elapsed_seconds"] <= gate["max_wall_seconds"]
(root / "INVERSE_MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: receipt[key] for key in ["result", "environments", "independent_matrix_comparisons", "half_inverse_moment_upper_bound", "elapsed_seconds"]}))
