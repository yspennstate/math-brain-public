"""Bounded mathematical checks; no Monte Carlo, workers, GPU, or live writes."""
import ctypes
import datetime
from fractions import Fraction as Q
import itertools
import json
import math
from pathlib import Path
import shutil
import time

ROOT = Path(__file__).resolve().parent
start = time.monotonic()

class MemoryStatus(ctypes.Structure):
    _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong),
                ("total_phys", ctypes.c_ulonglong), ("avail_phys", ctypes.c_ulonglong),
                ("total_page", ctypes.c_ulonglong), ("avail_page", ctypes.c_ulonglong),
                ("total_virtual", ctypes.c_ulonglong), ("avail_virtual", ctypes.c_ulonglong),
                ("avail_extended", ctypes.c_ulonglong)]

mem = MemoryStatus()
mem.length = ctypes.sizeof(mem)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
    raise RuntimeError("Fresh memory gate could not be read")
gate = {"checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "free_disk_bytes": shutil.disk_usage(ROOT).free,
        "available_memory_bytes": int(mem.avail_phys),
        "single_thread": True, "gpu": False, "monte_carlo": False,
        "max_n": 8, "max_paths_per_case": 128, "max_wall_seconds": 5,
        "pass": mem.avail_phys >= 16 * 1024**2 and shutil.disk_usage(ROOT).free >= 4 * 1024**2}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2)+"\n", encoding="utf-8")
if not gate["pass"]:
    raise RuntimeError("Fresh compute gate declined the finite check")

def budget():
    if time.monotonic() - start > 5:
        raise RuntimeError("Finite check exhausted its wall-time gate")

def paths(n):
    for steps in itertools.product((0, 1), repeat=n-1):
        x = y = 0
        vertices = [(0, 0)]
        for step in steps:
            x += step
            y += 1-step
            vertices.append((x, y))
        yield vertices

counts = {"projection_identities": 0, "zero_covariances": 0,
          "max_shift_identities": 0, "partition_shift_identities": 0,
          "floor_sums": 0}
for m in range(1, 9):
    budget()
    p = [[Q(1, m) for _ in range(m)] for _ in range(m)]
    q = [[Q(int(i == j))-p[i][j] for j in range(m)] for i in range(m)]
    def mul(a, b):
        return [[sum(a[i][k]*b[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
    assert mul(p, p) == p
    assert mul(q, q) == q
    assert mul(p, q) == [[Q(0) for _ in range(m)] for _ in range(m)]
    counts["projection_identities"] += 3
    for j in range(m):
        # Cov(mean of independent unit Gaussians, g_j - mean).
        assert Q(1, m) - sum(Q(1, m*m) for _ in range(m)) == 0
        counts["zero_covariances"] += 1

for n in range(1, 9):
    pp = list(paths(n))
    assert len(pp) == 2**(n-1)
    layer_sizes = {i: len({v for path in pp for v in path if sum(v) == i}) for i in range(n)}
    assert sum(Q(1, layer_sizes[i]) for i in range(n)) == sum(Q(1, j) for j in range(1, n+1))
    counts["floor_sums"] += 1
    vertices = {v for path in pp for v in path}
    for seed in range(3):
        budget()
        weights = {v: Q(((7*v[0]+11*v[1]+seed*13) % 19)-9, 3) for v in vertices}
        means = {i: sum(weights[v] for v in vertices if sum(v) == i)/layer_sizes[i] for i in range(n)}
        residuals = {v: weights[v] - means[sum(v)] for v in vertices}
        maximum = max(sum(weights[v] for v in path) for path in pp)
        residual_maximum = max(sum(residuals[v] for v in path) for path in pp)
        assert maximum == sum(means.values()) + residual_maximum
        counts["max_shift_identities"] += 1
        # Multiplicative path weights check log-partition shifts without float exponentials.
        positive = {v: Q(2 + ((3*v[0]+5*v[1]+seed) % 7), 3) for v in vertices}
        factors = {i: Q(i+2, i+3) for i in range(n)}
        z = sum(math.prod(positive[v] for v in path) for path in pp)
        shifted_z = sum(math.prod(positive[v]*factors[sum(v)] for v in path) for path in pp)
        assert shifted_z == z*math.prod(factors.values())
        counts["partition_shift_identities"] += 1

exact_baseline = Q(1, 2)
invalid_product = exact_baseline**8
assert exact_baseline > invalid_product
r2_at_1 = 1.5 + math.asin(math.exp(-1))/math.pi
invalid_r2_at_1 = 2*math.exp(-1)
assert r2_at_1 > invalid_r2_at_1
assert 1.5 + math.asin(1)/math.pi == 2
assert abs((1.5 + (math.pi/2-1)/math.pi) - (2-1/math.pi)) < 1e-14

result = {"all_finite_checks_passed": True, "counts": counts,
          "exact_checks": sum(counts.values()),
          "unsafe_candidate_checks_rejected": 2,
          "bernoulIi_shared_event_probability": str(exact_baseline),
          "invalid_product_bound": str(invalid_product),
          "n2_full_overlap_at_ou_time_1": r2_at_1,
          "invalid_exponential_bound_at_1": invalid_r2_at_1,
          "n2_independent_environment_overlap": 1.5,
          "n2_variance": 2-1/math.pi,
          "wall_seconds": time.monotonic()-start,
          "measurement_is_not_independent_review": True,
          "measurement_is_not_formal_proof": True,
          "parent_problem_solved": False,
          "command": "python -X utf8 ~/brain_workers/w493/verify_obstructions.py"}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
