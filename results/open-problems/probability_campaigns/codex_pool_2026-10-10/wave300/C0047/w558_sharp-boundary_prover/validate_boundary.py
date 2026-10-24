"""Bounded checks of independent finite consequences; not a theorem prover."""
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = time.monotonic()


def cluster(edges, mask):
    neighbors = {i: set() for i in range(-2, 3)}
    for k, (u, v) in enumerate(edges):
        if mask & (1 << k):
            neighbors[u].add(v)
            neighbors[v].add(u)
    seen = {0}
    pending = [0]
    while pending:
        u = pending.pop()
        for v in neighbors[u] - seen:
            seen.add(v)
            pending.append(v)
    return seen


def quartic(p):
    return 4 * p**4 - 8 * p**3 + 7 * p**2 + 2 * p - 1


short = [(i, i + 1) for i in range(-2, 2)]
long = [(-2, 0), (-1, 1), (0, 2)]
edges = short + long
failures = []
gain_checks = 0
for mask in range(1 << len(edges)):
    nearest = cluster(short, mask)
    enhanced = cluster(edges, mask)
    gain = 0
    for target in (-2, 2):
        long_index = edges.index(tuple(sorted((0, target))))
        near_index = edges.index(tuple(sorted((0, target // 2))))
        event = bool(mask & (1 << long_index)) and not bool(mask & (1 << near_index))
        gain += event
        if event:
            gain_checks += 1
            if target not in enhanced or target in nearest:
                failures.append({"mask": mask, "target": target, "failure": "gain event"})
    if len(enhanced) < len(nearest) + gain:
        failures.append({"mask": mask, "failure": "pointwise cluster gain"})

rayleigh_checks = []
for n in (1, 2, 5, 20, 100):
    length = 2 * n + 3
    boundary_direct = 2 * length
    oriented_internal = 0
    for k in range(1, n + 1):
        boundary_direct += sum(
            (j + k >= length) + (j - k < 0) for j in range(length)
        )
        oriented_internal += 2 * sum(j + k < length for j in range(length))
    boundary_formula = 2 * length + n * (n + 1)
    rayleigh_direct = F(oriented_internal, (2 * n + 2) * length)
    rayleigh_formula = F(n, n + 1) - F(n, 2 * length)
    ok = boundary_direct == boundary_formula and rayleigh_direct == rayleigh_formula
    rayleigh_checks.append({"N": n, "L": length, "boundary": boundary_direct,
                           "rayleigh": str(rayleigh_direct), "passed": ok})
    if not ok:
        failures.append({"N": n, "failure": "boundary / Rayleigh"})

lo, hi = F(0), F(1, 3)
for _ in range(60):
    mid = (lo + hi) / 2
    if quartic(mid) < 0:
        lo = mid
    else:
        hi = mid
assert quartic(lo) < 0 < quartic(hi)
assert quartic(F(29, 100)) > 0
assert 3 * F(1, 3)**2 + 2 * F(1, 3) - 1 == 0

table = [{"N": n, "D": 2 * n + 2, "phi_E_exact": 2,
          "conductance_exact": str(F(1, n + 1)),
          "rho_lower": n / (n + 1),
          "rho_upper": (n - 1 + math.sqrt(3)) / (n + 1),
          "pc_lower": 1 / (2 * n + 1),
          "pc_direct_neighbor_upper": 2 / (1 + math.sqrt(1 + 16 * n)),
          "pu_exact": 1} for n in (1, 2, 5, 20, 100)]

receipt = {
    "command": "python -X utf8 ~/brain_workers/w558/validate_boundary.py",
    "gate_file": str(ROOT / "COMPUTE_GATE.json"),
    "finite_configurations_checked": 1 << len(edges),
    "individual_gain_events_checked": gain_checks,
    "boundary_and_rayleigh_cases": rayleigh_checks,
    "N1_critical_equation_exact_root": "1/3",
    "quartic_upper_bound_root_interval": {"low": str(lo), "high": str(hi)},
    "quartic_upper_bound_root_approx": float((lo + hi) / 2),
    "quartic_at_29_over_100_exact": str(quartic(F(29, 100))),
    "quartic_is_upper_bound_not_actual_pc": True,
    "T4_correct_spectral_criterion_product": 2 * math.sqrt(3) / 3,
    "T4_erroneous_degree_free_product": math.sqrt(3) / 6,
    "table": table,
    "failures": failures,
    "wall_seconds_python_body": time.monotonic() - started,
    "mathematical_proof_completed_by_this_script": False,
    "passed": not failures,
}
if receipt["wall_seconds_python_body"] >= 60:
    raise RuntimeError("bounded local gate expired")
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
raise SystemExit(0 if not failures else 1)
