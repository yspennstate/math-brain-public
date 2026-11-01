"""Exact arithmetic comparison, not a simulation or a proof certificate."""
from fractions import Fraction
import json
from pathlib import Path
import time

root = Path(__file__).resolve().parent
started = time.perf_counter()
rows = []
geometry_checks = 0
for r in (0, 1, 2, 4, 10):
    s = r + 1
    old = Fraction(1, 64 ** (s * s))
    new = Fraction(1, 64 ** 4 * s * s)
    # Enumerate square-tile intervals independently of the closed-form distance.
    first = [(x, y) for x in range(s) for y in range(s)]
    for z in ((2, 0), (0, 2), (2, 2), (-2, 0)):
        second = [(s*z[0]+x, s*z[1]+y) for x in range(s) for y in range(s)]
        distance = min(max(abs(a[0]-b[0]), abs(a[1]-b[1])) for a in first for b in second)
        if distance <= r:
            raise AssertionError((r, z, distance))
        geometry_checks += 1
    rows.append({"r": r, "old_threshold": float(old), "candidate_threshold": float(new),
                 "candidate_to_old_ratio": float(new/old),
                 "candidate_exact": str(new), "old_exact": str(old)})
alpha = Fraction(1, 8)
contour_union_bound = alpha / (1-alpha)**2
positive_probability_bound = 1 - Fraction(1, 64**4) - contour_union_bound
assert contour_union_bound == Fraction(8, 49)
assert positive_probability_bound > 0
r_two = rows[2]
assert r_two["candidate_to_old_ratio"] == float(Fraction(64**5, 9))
result = {"command": "python -X utf8 ~/brain_workers/w430/measure_bridge.py",
          "rows": rows, "tile_distance_checks": geometry_checks,
          "contour_union_bound_exact": str(contour_union_bound),
          "positive_probability_bound_exact": str(positive_probability_bound),
          "positive_probability_bound": float(positive_probability_bound),
          "r2_example_bad_marginal": 1e-9,
          "r2_example_passes_old": 1e-9 <= r_two["old_threshold"],
          "r2_example_passes_candidate": 1e-9 <= r_two["candidate_threshold"],
          "elapsed_seconds": round(time.perf_counter()-started, 6),
          "limitation": "Finite arithmetic and geometric checks do not prove the contour theorem, establish critical blocks, or replace independent review."}
(root / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
