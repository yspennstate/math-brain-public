"""Bounded exact checks for L1, thinning, and the quantitative L3 obstruction.

This is supplementary finite verification, not a proof or formal certificate of C0023.
All output is confined to this worker folder. No networks, stores, GPU, or workers.
"""
from datetime import datetime, timedelta, timezone
from fractions import Fraction as F
import json
from pathlib import Path
import time
import tracemalloc

ROOT = Path(__file__).resolve().parent
START_WALL = time.perf_counter()
START_CPU = time.process_time()
now = datetime.now(timezone.utc)
gate = {
    "scope": "Fresh local gate for user-authorized deterministic proof checks only",
    "created_at": now.isoformat(),
    "expires_at": (now + timedelta(minutes=10)).isoformat(),
    "processes": 1,
    "threads": 1,
    "max_edges_per_enumerated_graph": 8,
    "max_unique_configurations": 600,
    "max_thinning_joint_configurations": 12000,
    "max_cpu_seconds": 20,
    "max_wall_seconds": 90,
    "max_traced_python_bytes": 64 * 1024 * 1024,
    "gpu": False,
    "training": False,
    "external_compute": False,
    "does_not_authorize_other_compute": True,
}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
tracemalloc.start()


def check_gate():
    assert time.process_time() - START_CPU < gate["max_cpu_seconds"], "CPU gate exhausted"
    assert time.perf_counter() - START_WALL < gate["max_wall_seconds"], "wall gate exhausted"
    assert tracemalloc.get_traced_memory()[1] <= gate["max_traced_python_bytes"], "memory gate exhausted"


def connected(edges, mask, source, target):
    adjacency = {}
    for j, (u, v) in enumerate(edges):
        if mask & (1 << j):
            adjacency.setdefault(u, []).append(v)
            adjacency.setdefault(v, []).append(u)
    reached = {source}
    queue = [source]
    for u in queue:
        for v in adjacency.get(u, []):
            if v not in reached:
                reached.add(v)
                queue.append(v)
    return target in reached


GRAPHS = [
    ("path3", [(0, 1), (1, 2), (2, 3)], 0, 3),
    ("diamond", [(0, 1), (1, 3), (0, 2), (2, 3)], 0, 3),
    ("diamond_tail", [(0, 1), (1, 3), (0, 2), (2, 3), (3, 4)], 0, 4),
    ("triangle", [(0, 1), (1, 2), (0, 2)], 0, 2),
    ("complete4", [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], 0, 3),
    ("counterexample_first_block", [(0, 1), (1, 5), (0, 2), (2, 5), (0, 3), (3, 5), (0, 4), (4, 5)], 0, 5),
    ("square_diagonal", [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)], 0, 2),
    ("grid2by3", [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)], 0, 5),
]
parameters = [F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(4, 5)]
unique_configs = 0
weighted_configs = 0
joint_configs = 0
identity_checks = 0
monotonicity_checks = 0
naive_missing_p_failures = 0
per_graph = []

for name, edges, source, target in GRAPHS:
    check_gate()
    m = len(edges)
    assert m <= gate["max_edges_per_enumerated_graph"]
    outcomes = [connected(edges, mask, source, target) for mask in range(1 << m)]
    unique_configs += len(outcomes)
    assert unique_configs <= gate["max_unique_configurations"]
    pivots = []
    for mask, outcome in enumerate(outcomes):
        pivots.append(sum(bool(mask & (1 << j)) and not outcomes[mask ^ (1 << j)] for j in range(m)) if outcome else 0)
        for j in range(m):
            if not mask & (1 << j):
                assert not outcome or outcomes[mask | (1 << j)]
                monotonicity_checks += 1
    for p in parameters:
        f = F(0)
        derivative = F(0)
        open_pivotal_expectation = F(0)
        for mask, outcome in enumerate(outcomes):
            k = mask.bit_count()
            weight = p**k * (1 - p)**(m - k)
            if outcome:
                f += weight
                # Independent computation: differentiate the configuration weight.
                derivative += weight * (F(k) / p - F(m - k) / (1 - p))
            open_pivotal_expectation += weight * pivots[mask]
            weighted_configs += 1
        assert f > 0
        assert open_pivotal_expectation / f == p * derivative / f
        identity_checks += 1
        naive_missing_p_failures += (open_pivotal_expectation / f != derivative / f)
        if name == "counterexample_first_block" and p == F(1, 2):
            assert f == F(175, 256)
            assert open_pivotal_expectation / f == F(216, 175)
    # Exhaust the two-stage coupling independently, including its joint law.
    b, a = F(3, 4), F(3, 8)
    q = a / b
    retained_probability = F(0)
    total_joint_probability = F(0)
    for mask in range(1 << m):
        k = mask.bit_count()
        original_weight = b**k * (1 - b)**(m - k)
        submask = mask
        while True:
            retained_k = submask.bit_count()
            joint_weight = original_weight * q**retained_k * (1 - q)**(k - retained_k)
            total_joint_probability += joint_weight
            if outcomes[submask]:
                retained_probability += joint_weight
            joint_configs += 1
            assert joint_configs <= gate["max_thinning_joint_configurations"]
            if submask == 0:
                break
            submask = (submask - 1) & mask
    direct_probability = sum((a**mask.bit_count() * (1 - a)**(m - mask.bit_count()) for mask, outcome in enumerate(outcomes) if outcome), F(0))
    assert total_joint_probability == 1
    assert retained_probability == direct_probability
    per_graph.append({"name": name, "edges": m, "configurations": len(outcomes), "pivotal_identity_checks": len(parameters), "thinning_joint_configurations": 3**m})


def exp_negative_interval(x, terms=40):
    """Exact rational bounds on exp(-x), by a positive Taylor series and tail."""
    assert x >= 0 and F(terms + 2) > x
    term, partial = F(1), F(1)
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    next_term = term * x / (terms + 1)
    upper = partial + next_term / (1 - x / (terms + 2))
    return 1 / upper, 1 / partial


_, u1 = exp_negative_interval(F(1))
_, u3 = exp_negative_interval(F(3))
_, u4 = exp_negative_interval(F(4))
_, u5 = exp_negative_interval(F(5))
_, u34 = exp_negative_interval(F(3, 4))
theta_lower = 1 - u1 - u4 / (1 - u5)
pivotal_upper = 2 * u34 / ((1 - u1) * (1 - 6 * u3))
assert theta_lower > F(3, 5)
assert pivotal_upper < 3
n = 500
subcritical_bound = n**2 * F(4, 5)**(n + 1)
assert subcritical_bound < F(1, 10**40)
assert theta_lower / subcritical_bound > 10**40
check_gate()
peak = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
result = {
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "command": "python -X utf8 ~/brain_workers/w423/verify.py",
    "status": "PASS",
    "scope": "Finite exact checks and exact rational bounds supplement L1/L3/L4; not a certificate of the infinite-volume target or independent mathematical review.",
    "graphs": len(GRAPHS),
    "unique_configurations": unique_configs,
    "weighted_configurations": weighted_configs,
    "monotonicity_checks": monotonicity_checks,
    "correct_identity_checks": identity_checks,
    "correct_identity_failures": 0,
    "naive_missing_p_identity_failures": naive_missing_p_failures,
    "thinning_law_checks": len(GRAPHS),
    "thinning_joint_configurations": joint_configs,
    "critical_connection_lower_bound": {"certified_comparison": ">3/5", "numerical_display": float(theta_lower)},
    "critical_conditional_bridge_upper_bound": {"certified_comparison": "<3 uniformly over N", "numerical_display": float(pivotal_upper)},
    "connection_at_p_0_4_bound_N500": {"certified_comparison": "<10^-40", "numerical_display": float(subcritical_bound)},
    "critical_to_subcritical_probability_ratio_lower_bound": ">10^40",
    "wall_seconds": round(time.perf_counter() - START_WALL, 6),
    "cpu_seconds": round(time.process_time() - START_CPU, 6),
    "peak_traced_python_bytes": peak,
    "per_graph": per_graph,
}
(ROOT / "measurements.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
