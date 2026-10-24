"""Small arithmetic checks; the symbolic proofs are in the review packet."""
import json
import math
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = time.monotonic()
gate = json.loads((ROOT / "COMPUTE_GATE.json").read_text(encoding="utf-8"))

raw = []
for n in (1, 2, 4, 8, 16, 64):
    assert n <= gate["max_dimensions"]
    squared = sum(
        ((i == 0 and j == k) + (j == 0 and i == k)
         + (k == 0 and i == j)) ** 2
        for i in range(n) for j in range(n) for k in range(n)
    )
    assert squared == 3 * n + 6
    raw.append({"n": n, "squared_hs_norm": squared})

tilts = []
for theta in (Fraction(0), Fraction(1, 2), Fraction(3, 4), Fraction(9, 10)):
    var = 1 / (1 - theta) ** 2
    tilts.append({"theta": str(theta), "variance": str(var)})
assert tilts[-1]["variance"] == "100"

# At s=1, Y=X+Z has density exp(-y-1/2) Phi(y).
# Simpson quadrature is a numerical diagnostic, not an interval certificate.
lo, hi, intervals = -10.0, 28.0, 38000
assert intervals + 1 <= gate["quadrature_points"]
step = (hi - lo) / intervals
mass = first = second = 0.0
for j in range(intervals + 1):
    y = lo + j * step
    phi = math.exp(-y * y / 2) / math.sqrt(2 * math.pi)
    cdf = math.erfc(-y / math.sqrt(2)) / 2
    lam = phi / cdf
    variance = 1 - y * lam - lam * lam
    density = math.exp(-y - 0.5) * cdf
    weight = 1 if j in (0, intervals) else (4 if j % 2 else 2)
    mass += weight * density
    first += weight * density * variance
    second += weight * density * variance * variance
mass *= step / 3
first *= step / 3
second *= step / 3
assert second > first * first

elapsed = time.monotonic() - started
report = {
    "command": "python -X utf8 verify_obstructions.py",
    "gaussian_raw_moments": raw,
    "exact_exponential_tilt_variances": tilts,
    "regularized_tilt_limit_coefficient": 1 - 2 / math.pi,
    "posterior_factorization_diagnostic": {
        "s": 1,
        "f": "x",
        "quadrature_domain": [lo, hi],
        "points": intervals + 1,
        "density_mass_on_domain": mass,
        "E_A_approx": first,
        "E_A_squared_approx": second,
        "square_E_A_approx": first * first,
        "strict_gap_approx": second - first * first,
        "lhs_to_false_rhs_ratio_approx": second / (first * first),
        "status": "numerical diagnostic; strict positivity proved separately by nonconstant posterior variance"
    },
    "elapsed_seconds": elapsed,
    "within_compute_gate": elapsed <= gate["max_wall_seconds"],
    "full_target_proved": False
}
(ROOT / "MEASUREMENTS.json").write_text(
    json.dumps(report, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(report, indent=2))
if not report["within_compute_gate"]:
    raise RuntimeError("fresh compute gate exceeded")
