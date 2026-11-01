"""Bounded exact controls for C0047. These are not an infinite-graph proof."""
from __future__ import annotations

import ctypes
import json
import math
import os
import shutil
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class MemoryStatus(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_uint32), ("dwMemoryLoad", ctypes.c_uint32)] + [
        (name, ctypes.c_uint64) for name in (
            "ullTotalPhys", "ullAvailPhys", "ullTotalPageFile", "ullAvailPageFile",
            "ullTotalVirtual", "ullAvailVirtual", "ullAvailExtendedVirtual")]


def fresh_gate():
    """Keep the worker gate's commit floor; add conservative small-check limits."""
    configured = json.loads(Path("~/brain_workers/GATE.json").read_text())
    status = MemoryStatus()
    status.dwLength = ctypes.sizeof(status)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
        raise OSError("GlobalMemoryStatusEx failed")
    gb = 1024 ** 3
    floor = max(6.0, float(configured["commit_floor_gb"]))
    memory = {"available_commit_gb": status.ullAvailPageFile / gb,
              "available_physical_gb": status.ullAvailPhys / gb,
              "disk_free_gb": shutil.disk_usage(ROOT).free / gb,
              "configured_commit_floor_gb": floor,
              "configured_max_running": configured["max_running"]}
    # GetSystemTimes measures aggregate CPU without launching a helper or reading processes.
    def cpu_times():
        vals = [ctypes.c_uint64() for _ in range(3)]
        if not ctypes.windll.kernel32.GetSystemTimes(*(ctypes.byref(v) for v in vals)):
            raise OSError("GetSystemTimes failed")
        return [v.value for v in vals]
    before = cpu_times()
    time.sleep(0.25)
    after = cpu_times()
    idle, kernel, user = [b-a for a, b in zip(before, after)]
    total = kernel + user
    busy = 100 * (1-idle/total) if total else 100.0
    memory["cpu_busy_pct"] = busy
    reasons = []
    if memory["available_commit_gb"] < floor:
        reasons.append("configured commit floor")
    if memory["available_physical_gb"] < 1.0:
        reasons.append("one GB physical headroom")
    if memory["disk_free_gb"] < 2.0:
        reasons.append("two GB disk headroom")
    if busy > 80:
        reasons.append("CPU busy above 80 percent")
    # No workers are spawned, so this check does not add a worker to max_running.
    receipt = {"checked_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "action": "bounded standard-library exact enumeration, <=2048 configurations",
               "new_workers": 0, "GPU": False, "remote_compute": False,
               "metrics": memory, "allowed": not reasons, "reasons": reasons}
    (ROOT / "COMPUTE_GATE.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    return receipt


def component_size(m, mask):
    adj = [[] for _ in range(m)]
    for i in range(m):
        if mask & (1 << i):
            j = (i + 1) % m
            adj[i].append(j)
            adj[j].append(i)
    reached = {0}
    frontier = [0]
    while frontier:
        for v in adj[frontier.pop()]:
            if v not in reached:
                reached.add(v)
                frontier.append(v)
    return len(reached)


def cycle_mean(m, p):
    return 1 + 2 * sum((p**k for k in range(1, m)), Fraction(0)) - (m-1)*p**m


def mean_offspring(m, p, doubled_involution=False):
    exit_probability = 2*p-p*p if doubled_involution else p
    return exit_probability * (cycle_mean(m, p)-1)


def root_interval(m, doubled=False):
    lo, hi = Fraction(0), Fraction(1)
    for _ in range(50):
        mid = (lo+hi)/2
        if mean_offspring(m, mid, doubled) < 1:
            lo = mid
        else:
            hi = mid
    assert mean_offspring(m, lo, doubled) < 1
    assert mean_offspring(m, hi, doubled) > 1
    return {"lower_exact": str(lo), "upper_exact": str(hi),
            "lower_decimal": float(lo), "upper_decimal": float(hi)}


def run_controls():
    started = time.perf_counter()
    controls = []
    configurations = 0
    for m in (3, 5, 7):
        histogram = Counter(component_size(m, mask) for mask in range(1 << m))
        assert sum(histogram.values()) == 1 << m
        for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
            weights = Counter()
            for mask in range(1 << m):
                k = mask.bit_count()
                weights[component_size(m, mask)] += p**k*(1-p)**(m-k)
                configurations += 1
            assert sum(weights.values()) == 1
            actual = sum((size*prob for size, prob in weights.items()), Fraction(0))
            expected = cycle_mean(m, p)
            assert actual == expected, (m, p, actual, expected)
            # Independent second check: condition on X and enumerate the offspring law.
            law = Counter()
            for size, prob in weights.items():
                for k in range(size):
                    law[k] += prob * math.comb(size-1, k)*p**k*(1-p)**(size-1-k)
            assert sum(law.values()) == 1
            actual_mu = sum((k*prob for k, prob in law.items()), Fraction(0))
            assert actual_mu == mean_offspring(m, p)
            controls.append({"m": m, "p": str(p), "cycle_mean": str(actual),
                             "offspring_mean": str(actual_mu), "passed": True})
    # Independent cuts on a path give equality p^2. Overlap refutes the same product.
    p = Fraction(1, 2)
    disjoint_actual = sum(p**mask.bit_count()*(1-p)**(2-mask.bit_count())
                         for mask in range(4) if mask == 3)
    assert disjoint_actual == p*p
    overlapping_actual = p
    assert overlapping_actual > p*p
    # Selecting a known-open edge is not a fresh measurable selection.
    adaptive_actual = 1-(1-p)**2
    assert adaptive_actual > p
    # At m=3, the parallel-edge formula exactly equals the primary paper polynomial+1.
    for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
        assert mean_offspring(3, p, True) == 2*p**5-6*p**4+2*p**3+4*p**2
    # The normalized spectral inverse is >1 on T_3; the corrected bound is <pc.
    rho = 2*math.sqrt(2)/3
    assert 1/rho > 1 and 1/(3*rho) < 0.5
    assert configurations <= 2048
    return {"status": "PASS", "cycle_offspring_controls": controls,
            "cycle_configurations_evaluated": configurations,
            "disjoint_cut_control": str(disjoint_actual),
            "overlap_control": {"actual": str(overlapping_actual), "invalid_product": "1/4"},
            "adaptive_selection_control": {"actual": str(adaptive_actual), "invalid_fresh_law": "1/2"},
            "simple_C2_C5_pc_interval": root_interval(5),
            "parallel_involution_C2_C5_pc_interval": root_interval(5, True),
            "normalization_before": {"normalized_inverse_rho": 1/rho, "nontrivial_reduction": False},
            "normalization_after": {"degree_scaled_inverse": 1/(3*rho), "condition_met_on_T3": False,
                                    "T3_pc": 0.5, "T3_pu": 1},
            "seconds": time.perf_counter()-started,
            "limits": "Finite controls do not verify L3, infinite-graph branching geometry, general current openness, or the parent conjecture."}


if __name__ == "__main__":
    gate = fresh_gate()
    if not gate["allowed"]:
        result = {"status": "NOT_RUN_GATE_DENIED", "reasons": gate["reasons"],
                  "parent_problem_solved": False}
    else:
        result = run_controls()
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
