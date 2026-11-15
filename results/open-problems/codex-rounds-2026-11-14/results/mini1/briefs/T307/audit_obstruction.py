"""Exact, small checks of the constants in PROOF.md; standard library only."""

import json
import math
import os
import resource
from fractions import Fraction as F
from pathlib import Path


def cap_limit(which, ceiling):
    soft, hard = resource.getrlimit(which)
    finite = [v for v in (soft, hard, ceiling) if v != resource.RLIM_INFINITY]
    cap = min(finite)
    resource.setrlimit(which, (cap, cap))


cap_limit(resource.RLIMIT_CPU, 30)


def clip(a):
    return max(F(-1), min(F(1), a))


mu, radius = F(1, 2), F(1, 16)
target_lo, target_hi = mu - radius, mu + radius
dilation_gap = 2 * target_lo - target_hi
unsaturated_bound = dilation_gap**2 / 5
saturated_bound = (1 - target_hi)**2
assert (target_lo, target_hi) == (F(7, 16), F(9, 16))
assert dilation_gap == F(5, 16)
assert unsaturated_bound == F(5, 256)
assert saturated_bound == F(49, 256)
assert unsaturated_bound < saturated_bound

# Independent scalar derivation: minimize distance from clipped predictions
# to the target interval in each coordinate, rather than completing a square.
def interval_distance(a):
    return max(target_lo - a, F(0), a - target_hi)


best = None
best_a = None
identity_checks = 0
grid_checks = 0
for j in range(-512, 513):
    a = F(j, 256)
    value = interval_distance(clip(a)) ** 2 + interval_distance(clip(2 * a)) ** 2
    if best is None or value < best:
        best, best_a = value, a
    assert value >= unsaturated_bound
    grid_checks += 1
    for u in (target_lo, mu, target_hi):
        for v in (target_lo, mu, target_hi):
            lhs = (a - u) ** 2 + (2 * a - v) ** 2
            rhs = 5 * (a - (u + 2 * v) / 5) ** 2 + (2 * u - v) ** 2 / 5
            assert lhs == rhs
            clipped_loss = (clip(a) - u) ** 2 + (clip(2 * a) - v) ** 2
            assert clipped_loss >= unsaturated_bound
            identity_checks += 1
assert best == unsaturated_bound and best_a == F(5, 16)

# The Gaussian exponent estimate uses 2h > 1, so the exponent is < (5/8)^2.
gaussian_exponent_upper = (F(1, 16) + F(9, 16)) ** 2
assert gaussian_exponent_upper == F(25, 64) < 1
assert 1 - math.exp(-1) > 0.5

# Compare the product b_d * |E| * (5/256) with the displayed C_d.
constants = {}
for dimension in (1, 2, 3, 5):
    density_floor = math.exp(-1) * (2 * math.pi) ** (-dimension / 2)
    region_volume = (32 * math.sqrt(dimension)) ** (-dimension) / 4
    product_constant = density_floor * region_volume * float(unsaturated_bound)
    displayed_constant = 5 * math.exp(-1) / (
        1024 * (32 * math.sqrt(2 * math.pi * dimension)) ** dimension
    )
    assert math.isclose(product_constant, displayed_constant, rel_tol=1e-14)
    constants[str(dimension)] = {
        "product": product_constant,
        "displayed": displayed_constant,
        "dilation_jacobian": 2 ** (dimension + 1),
    }

result = {
    "status": "PASS",
    "priority_nice": os.getpriority(os.PRIO_PROCESS, 0),
    "omp_num_threads": os.environ.get("OMP_NUM_THREADS"),
    "grid_count": grid_checks,
    "exact_identity_and_clipping_checks": identity_checks,
    "scalar_grid_minimum": str(best),
    "scalar_minimizer": str(best_a),
    "saturated_error_bound": str(saturated_bound),
    "gaussian_exponent_upper": str(gaussian_exponent_upper),
    "peak_rss_platform_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "cpu_seconds": resource.getrusage(resource.RUSAGE_SELF).ru_utime,
    "constants": constants,
    "note": "Finite checks supplement the proof; they do not establish the continuous theorem.",
}
data_path = Path(__file__).resolve().parent / "audit_data.json"
data_path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
