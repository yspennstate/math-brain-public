"""Small finite-state diagnostics, not an independent or formal mathematical proof.

Run: python -X utf8 ~/brain_workers/w471/check_lemmas.py
"""
from pathlib import Path
import ctypes
import importlib.util
import json
import math
import os
import shutil
import time

HERE = Path(__file__).resolve().parent

class MemoryStatus(ctypes.Structure):
    _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong),
                ("total_phys", ctypes.c_ulonglong), ("avail_phys", ctypes.c_ulonglong),
                ("total_page", ctypes.c_ulonglong), ("avail_page", ctypes.c_ulonglong),
                ("total_virtual", ctypes.c_ulonglong), ("avail_virtual", ctypes.c_ulonglong),
                ("avail_extended", ctypes.c_ulonglong)]

mem = MemoryStatus()
mem.length = ctypes.sizeof(mem)
memory_ok = bool(ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)))
gate = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "available_memory_bytes": mem.avail_phys if memory_ok else None,
        "free_disk_bytes": shutil.disk_usage(HERE).free,
        "max_spins": 8, "max_states_per_case": 256,
        "uses_gpu": False, "threads": 1, "run_budget_seconds": 90}
gate["admitted"] = (memory_ok and mem.avail_phys >= 128 * 1024**2
                    and gate["free_disk_bytes"] >= 32 * 1024**2)
(HERE / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
if not gate["admitted"]:
    raise SystemExit("Fresh compute gate declined these small diagnostics; receipt saved.")
if importlib.util.find_spec("numpy") is None:
    raise SystemExit("numpy is unavailable; no dependency installation is attempted.")
for env_name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[env_name] = "1"
import numpy as np

started = time.monotonic()
rows = []
receipt = HERE / "FINITE_CONTROLS.jsonl"

def save(row):
    rows.append(row)
    with receipt.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")

def check_bounds(variance, fourth_cumulant, y1):
    r = math.sqrt(variance) * y1
    deficit = -fourth_cumulant / variance**2
    lower, upper = 12 / r**4, 6 / r**2
    assert lower <= deficit + 1e-8, (lower, deficit)
    assert deficit <= upper + 1e-8, (deficit, upper)
    assert 0 < deficit <= 2 + 1e-8
    return {"variance": variance, "fourth_cumulant": fourth_cumulant,
            "y1": y1, "r": r, "B": deficit, "B_lower": lower, "B_upper": upper}

for count in (1, 2, 8, 64, 1024):
    row = check_bounds(float(count), -2.0 * count, math.pi / 2)
    row.update(case=f"independent-{count}", method="exact analytical control", spins=count,
               factorization_variance_error=0.0, factorization_cumulant_error=0.0)
    save(row)

for count in (8, 64, 1024):
    # Raw zeros approach zero, while normalized zeros escape and B approaches zero.
    scale = float(count)
    row = check_bounds(count * scale**2, -2 * count * scale**4, math.pi / (2 * scale))
    row.update(case=f"scaled-independent-{count}", method="exact analytical control",
               spins=count, scale=scale, warning="raw zero tending to zero is insufficient",
               factorization_variance_error=0.0, factorization_cumulant_error=0.0)
    save(row)

cube_edges = [(i, i ^ (1 << axis)) for i in range(8) for axis in range(3)
              if not (i & (1 << axis))]
graphs = [
    ("edge", 2, [(0, 1)], [0, 1]),
    ("odd-path", 3, [(0, 1), (1, 2)], [0, 1, 2]),
    ("square", 4, [(0, 1), (1, 2), (2, 3), (3, 0)], list(range(4))),
    ("cube", 8, cube_edges, list(range(8))),
    ("cube-plane-marginal", 8, cube_edges, [0, 1, 2, 3]),
]

for beta in (0.1, 0.3, 0.7):
    for name, count, edges, observed in graphs:
        assert time.monotonic() - started < 90, "Diagnostic run budget exceeded"
        m = len(observed)
        records = []
        for bits in range(1 << count):
            spins = [1 if bits & (1 << j) else -1 for j in range(count)]
            energy = sum(spins[i] * spins[j] for i, j in edges)
            s = sum(spins[i] for i in observed)
            records.append((math.exp(beta * energy), s))
        partition = sum(weight for weight, _ in records)
        probabilities = [(weight / partition, s) for weight, s in records]
        coefficients = np.zeros(m + 1)
        for p, s in probabilities:
            coefficients[(s + m) // 2] += p
        assert np.max(np.abs(coefficients - coefficients[::-1])) < 1e-12
        variance = sum(p * s**2 for p, s in probabilities)
        fourth_cumulant = sum(p * s**4 for p, s in probabilities) - 3 * variance**2
        roots = np.roots(coefficients[::-1])
        unit_error = float(np.max(np.abs(np.abs(roots) - 1)))
        assert unit_error < 1e-7, unit_error
        positive = [root for root in roots if root.imag > 1e-7]
        real = [root for root in roots if abs(root.imag) <= 1e-7]
        assert all(abs(root.real + 1) < 1e-7 for root in real)
        assert 2 * len(positive) + len(real) == m
        c = [1 / math.sin(float(np.angle(root)) / 2)**2 for root in positive]
        # Exact finite trigonometric factorization: cosh(h)^q times
        # product[1 + c_j sinh(h)^2], including the odd root at -1.
        variance_formula = len(real) + 2 * sum(c)
        cumulant_formula = -2 * len(real) + 8 * sum(c) - 12 * sum(x*x for x in c)
        v_error = abs(variance_formula - variance) / max(1.0, abs(variance))
        k_error = abs(cumulant_formula - fourth_cumulant) / max(1.0, abs(fourth_cumulant))
        assert v_error < 1e-7, v_error
        assert k_error < 1e-7, k_error
        y1 = min(abs(float(np.angle(root))) / 2 for root in roots)
        row = check_bounds(variance, fourth_cumulant, y1)
        subgaussian_error = 0.0
        for t in (-3, -2, -1, -0.5, 0.5, 1, 2, 3):
            mgf = sum(p * math.exp(t * s / math.sqrt(variance)) for p, s in probabilities)
            excess = math.log(mgf) - t*t/2
            subgaussian_error = max(subgaussian_error, excess)
            assert excess < 1e-10, excess
        row.update(case=f"{name}-beta-{beta}", method="complete finite-state enumeration and polynomial roots",
                   spins=count, observed_spins=m, states=1 << count, beta=beta,
                   factorization_variance_error=v_error, factorization_cumulant_error=k_error,
                   unit_circle_error=unit_error, subgaussian_log_excess=subgaussian_error)
        save(row)

geometry = []
for radius in (1, 2, 3, 4, 8, 16, 64, 128):
    outer, inner = (4*radius + 1)**3, (2*radius + 1)**3
    assert 8 * inner >= outer
    assert outer >= 64 * radius**3
    coefficient = outer / (256 * radius**3)
    assert coefficient >= 0.25
    geometry.append({"R": radius, "N": outer, "inner": inner,
                     "g_to_B_coefficient_at_xi_equal_R": coefficient})

summary = {"status": "PASS", "finite_or_analytical_cases": len(rows),
           "enumerated_cases": sum("states" in row for row in rows),
           "enumerated_states_total": sum(row.get("states", 0) for row in rows),
           "geometry_cases": len(geometry), "failed_assertions": 0,
           "max_relative_variance_error": max(row["factorization_variance_error"] for row in rows),
           "max_relative_cumulant_error": max(row["factorization_cumulant_error"] for row in rows),
           "seconds": time.monotonic() - started,
           "command": "python -X utf8 ~/brain_workers/w471/check_lemmas.py",
           "scope": "Finite diagnostic controls only; not a proof or review of the critical 3D zero bound",
           "geometry": geometry}
(HERE / "MEASUREMENTS.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps({k:v for k,v in summary.items() if k != "geometry"}))
