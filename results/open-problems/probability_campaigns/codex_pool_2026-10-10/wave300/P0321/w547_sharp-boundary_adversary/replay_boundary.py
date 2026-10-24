"""Bounded deterministic quadrature checks; these do not prove P0321."""
from __future__ import annotations
import json
import ctypes
import math
import os
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

def save(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

def main():
    import psutil
    policies = []
    for path in [Path('~/brain_workers/GATE.json'),
                 Path('~/primary_directive/GATE.json')]:
        if path.exists():
            policies.append({"path": str(path), "policy": json.loads(path.read_text(encoding='utf-8-sig'))})
    commit_floor = max([6.0] + [float(x['policy'].get('commit_floor_gb', 6.0)) for x in policies])
    class MemoryStatus(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong)] + [
            (name, ctypes.c_ulonglong) for name in
            ['ullTotalPhys', 'ullAvailPhys', 'ullTotalPageFile', 'ullAvailPageFile',
             'ullTotalVirtual', 'ullAvailVirtual', 'ullAvailExtendedVirtual']]
    memory = MemoryStatus()
    memory.dwLength = ctypes.sizeof(memory)
    api_ok = bool(ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)))
    gate = {
        "sampled_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kind": "fresh local admission snapshot for bounded deterministic CPU quadrature",
        "cpu_percent": psutil.cpu_percent(interval=0.25),
        "available_memory_bytes": psutil.virtual_memory().available,
        "commit_available_bytes": int(memory.ullAvailPageFile) if api_ok else None,
        "global_gate_policies": policies,
        "limits": {"cpu_percent_below": 75, "available_memory_at_least_bytes": 2 * 1024**3,
                   "numeric_work_wall_seconds": 60, "blas_threads": 1,
                   "commit_headroom_at_least_gb": commit_floor,
                   "largest_dense_array_elements": 16384, "gpu": False,
                   "new_workers_or_background_processes": 0},
    }
    gate["admitted"] = (gate["cpu_percent"] < 75 and
                        gate["available_memory_bytes"] >= 2 * 1024**3 and api_ok and
                        memory.ullAvailPageFile >= commit_floor * 1024**3)
    save("COMPUTE_GATE.json", gate)
    if not gate["admitted"]:
        save("MEASUREMENTS.json", {"status": "SKIPPED_FRESH_RESOURCE_GATE", "gate": gate,
                                  "proof_role": "Analytic proof remains separate from numerical checking."})
        print("SKIPPED_FRESH_RESOURCE_GATE")
        return 0
    started = time.perf_counter()
    import numpy as np
    from scipy.integrate import quad
    from scipy.special import j0, j1, jv
    deadline = started + 60
    rows = []

    def require_time():
        if time.perf_counter() > deadline:
            save("MEASUREMENTS.json", {"status": "STOPPED_AT_NUMERIC_TIME_GATE", "rows": rows})
            raise RuntimeError("60 second numeric-work gate reached")

    # Independent radial/Bessel integration, T=mu=a=Lambda=|G|=1.
    def kernel(t, sign, angle):
        c = math.cos(2 * angle)
        if abs(t) < 0.001:
            return t*t*(0.25 + sign*c/8) + t**4*(-1/64 - sign*c/96)
        return 1 - j0(t) + sign*c*jv(2, t)

    def radial(r, p, angle):
        require_time()
        tr, etr = quad(lambda q: kernel(q*r, -1, angle)/q,
                      0, 1, epsabs=2e-9, epsrel=2e-9, limit=1200)
        lo, elo = quad(lambda q: q**(1-p)*kernel(q*r, 1, angle),
                      0, 1, epsabs=2e-9, epsrel=2e-9, limit=1200)
        return (tr + lo)/(4*math.pi), (etr + elo)/(4*math.pi)

    # Separate full two-dimensional quadrature at modest distances, using
    # projector components directly rather than the Bessel reduction.
    qnodes, qweights = np.polynomial.legendre.leggauss(128)
    q = (qnodes + 1)/2
    qw = qweights/2
    phi = 2*math.pi*(np.arange(128)+0.5)/128
    def direct(r, p, angle):
        require_time()
        phase = r*q[:, None]*np.cos(phi)[None, :]
        one_minus_cos = 2*np.sin(phase/2)**2
        tr = np.sin(phi-angle)**2 / q[:, None]**2
        lo = np.cos(phi-angle)**2 / q[:, None]**p
        return float(np.sum(qw[:, None]*q[:, None]*one_minus_cos*(tr+lo))
                     * (2*math.pi/128)/(2*math.pi)**2)

    discrepancies = []
    for p in [0.0, 1.0, 1.9, 2.0]:
        for angle in [0.0, math.pi/2]:
            for r in [0.5, 2.0, 8.0]:
                value, err = radial(r, p, angle)
                other = direct(r, p, angle)
                discrepancies.append(abs(value-other))
                rows.append({"check": "independent_projector_vs_bessel", "p": p,
                             "angle": angle, "r": r, "minus_log_CG": value,
                             "direct_minus_log_CG": other, "absolute_difference": abs(value-other),
                             "quad_error_estimate": err})
    slope_rows = []
    for p in [1.0, 1.9, 1.999, 2.0]:
        lo, errlo = radial(512, p, 0.0)
        hi, errhi = radial(1024, p, 0.0)
        slope = (hi-lo)/math.log(2)
        target = (1 + int(p == 2))/(4*math.pi)
        result = {"p": p, "r_low": 512, "r_high": 1024,
                  "finite_distance_log_slope": slope, "fixed_p_asymptotic_exponent": target,
                  "minus_log_CG_high": hi,
                  "exponential_rate_proxy_high": hi/1024,
                  "quad_error_estimate_sum": errlo+errhi}
        slope_rows.append(result)
        rows.append({"check": "endpoint_slope", **result})
        save("MEASUREMENTS.json", {"status": "RUNNING", "rows": rows})
    orient_limit = math.exp(-9/(4*math.pi))
    orientation = [{"r": r, "C6": math.exp(-9/(4*math.pi)*(1-2*j1(r)/r)),
                    "limit": orient_limit} for r in [16, 64, 256, 1024]]
    checks = {
        "24_independent_2d_radial_pairs": len(discrepancies) == 24,
        "independent_quadrature_absolute_error_below_2e_6": max(discrepancies) < 2e-6,
        "p1_log_slope_within_0_003_of_etaT": abs(slope_rows[0]["finite_distance_log_slope"]-1/(4*math.pi)) < 0.003,
        "p2_log_slope_within_0_003_of_etaT_etaL": abs(slope_rows[-1]["finite_distance_log_slope"]-1/(2*math.pi)) < 0.003,
        "near_endpoint_finite_distance_slope_differs_from_fixed_p_limit": slope_rows[2]["finite_distance_log_slope"] > 1.8/(4*math.pi),
        "orientational_plateau_within_0_001_at_r1024": abs(orientation[-1]["C6"]-orient_limit) < 0.001,
    }
    result = {"status": "PASS" if all(checks.values()) else "FAIL", "gate": gate,
              "command": "python -X utf8 ~/brain_workers/w547/replay_boundary.py",
              "fixed_parameters": {"T": 1, "mu": 1, "a": 1, "Lambda": 1, "G_norm": 1},
              "checks": checks, "max_independent_quadrature_absolute_difference": max(discrepancies),
              "slopes": slope_rows, "orientation": orientation,
              "elapsed_numeric_wall_seconds": time.perf_counter()-started,
              "rows": rows, "proof_role": "Finite numerical regression only; does not prove asymptotics, Riesz correspondence, or P0321."}
    save("MEASUREMENTS.json", result)
    print(json.dumps({k: result[k] for k in ["status", "checks", "max_independent_quadrature_absolute_difference", "slopes", "orientation", "elapsed_numeric_wall_seconds"]}, indent=2))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
