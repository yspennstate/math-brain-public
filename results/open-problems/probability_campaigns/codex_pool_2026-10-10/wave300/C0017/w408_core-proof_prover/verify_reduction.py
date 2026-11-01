"""Bounded exact-arithmetic audit of the conditional Cardy identification.

This is an algebra check and negative-control experiment, not a formal proof
of stochastic calculus, Cardy's formula, or square-lattice universality.
All writes are confined to this worker folder. No simulation, network or GPU.
"""
from __future__ import annotations

import json
import time
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GOVERNOR = Path("~/.claude/compute/compute_state.json")


def coefficients(x: F, y: F) -> tuple[F, F, F]:
    """Chain-rule derivatives; normalized by the positive factor C'(x/y).

    h is obtained by differentiating log[u^(-2/3)(1-u)^(-2/3)].
    This computes gradient/Hessian entries directly, before taking sums.
    """
    u = x / y
    ux, uy = 1 / y, -x / y**2
    uxx, uxy, uyy = F(0), -1 / y**2, 2 * x / y**3
    h = -F(2, 3) / u + F(2, 3) / (1 - u)
    fx, fy = ux, uy
    fxx = h * ux * ux + uxx
    fxy = h * ux * uy + uxy
    fyy = h * uy * uy + uyy
    D = fx + fy
    D2 = fxx + 2 * fxy + fyy
    A = 2 * fx / x + 2 * fy / y
    return D, D2, A


def fresh_gate() -> dict:
    """Read-only resource receipt for a sub-second, one-thread scalar audit."""
    before = time.time()
    s = json.loads(GOVERNOR.read_text(encoding="utf-8-sig"))
    age = before - GOVERNOR.stat().st_mtime
    if age < -5 or age > 120:
        raise RuntimeError(f"Fresh governor receipt unavailable: age {age:.1f}s")
    # This audit is light local work under COMPUTE_DOCTRINE, not a heavy job.
    # Do not weaken any governor setting or acquire a heavy-compute lease.
    selected = {
        k: s[k] for k in (
            "timestamp", "ts", "distress", "distress_reasons", "cpu_pct",
            "cpu_total_pct", "cpu_percent", "mem_avail_mb", "memory_available_mb",
            "commit_used_pct", "commit_avail_mb", "commit_eff_used_pct",
            "commit_eff_avail_mb", "mode", "status", "reasons", "disk_queue", "hung_windows",
        ) if k in s
    }
    (ROOT / "RESOURCE_GATE.json").write_text(json.dumps({"age_seconds":age,"selected_metrics":selected}, indent=2)+"\n", encoding="utf-8")
    # Respect immediate-distress/critical pressure holds. Throttle warnings
    # restrict this already small audit to one thread and half a CPU second.
    if s.get("distress") or str(s.get("status", "")).lower() == "distress":
        raise RuntimeError("Governor reports distress; scalar audit held")
    numeric = [s.get(k) for k in ("cpu_pct", "mem_avail_mb", "commit_used_pct", "commit_avail_mb")]
    if any(not isinstance(v, (int, float)) for v in numeric):
        raise RuntimeError("Finite local CPU/physical-memory/commit telemetry required")
    if s["cpu_pct"] >= 95 or s["mem_avail_mb"] <= 4096:
        raise RuntimeError("CPU or physical-memory critical pressure; scalar audit held")
    if s["commit_used_pct"] >= 90 or s["commit_avail_mb"] <= 8192:
        raise RuntimeError("Critical commit pressure; scalar audit held")
    if s.get("commit_eff_used_pct", 0) >= 90 or s.get("commit_eff_avail_mb", 999999) <= 8192:
        raise RuntimeError("Critical effective commit pressure; scalar audit held")
    reasons = " ".join(map(str, s.get("reasons", []))).lower()
    if "critical" in reasons or "hung_window" in reasons:
        raise RuntimeError("Governor reports critical/UI pressure; scalar audit held")
    hung = s.get("hung_windows", 0)
    if (isinstance(hung, (int, float)) and hung > 0) or (isinstance(hung, (list, dict)) and hung):
        raise RuntimeError("Hung-window pressure; scalar audit held")
    return {
        "state_path": str(GOVERNOR),
        "read_at_unix": before,
        "age_seconds": age,
        "selected_metrics": selected,
        "work_class": "light-local-scalar-audit",
        "limits": {"threads": 1, "state_triples": 108, "cpu_seconds": 0.5},
        "gpu": False,
        "network": False,
        "services_changed": False,
    }


def run() -> dict:
    gate = fresh_gate()
    start_wall, start_cpu = time.perf_counter(), time.process_time()
    valid_kappa6 = wrong_kappa_single = wrong_kappa_two = drift_checks = 0
    triples = list(product(
        [F(1, 2), F(1), F(2), F(3)],
        [F(1, 3), F(1), F(2)],
        [F(1, 4), F(1), F(2)],
        [F(1), F(7, 5), F(11, 7)],
    ))
    assert len({(x*s, (x+a)*s, (x+a+b)*s) for x,a,b,s in triples}) == 108
    min_separation = None
    for index, (x0, gap1, gap2, scale) in enumerate(triples):
        x, y1, y2 = x0 * scale, (x0 + gap1) * scale, (x0 + gap1 + gap2) * scale
        D1, D21, A1 = coefficients(x, y1)
        D2, D22, A2 = coefficients(x, y2)
        s1, s2 = 1 / x + 1 / y1, 1 / x + 1 / y2
        assert D1 > 0 and D2 > 0 and s1 > s2
        assert A1 + 3 * D21 == A2 + 3 * D22 == 0
        assert D21 / (2 * D1) == -s1 / 3
        assert D22 / (2 * D2) == -s2 / 3
        det = (-D1) * (D22 / 2) - (-D2) * (D21 / 2)
        assert det == D1 * D2 * (s2 - s1) / 3 and det != 0
        min_separation = s1 - s2 if min_separation is None else min(min_separation, s1 - s2)
        valid_kappa6 += 1
        for kappa in [F(0), F(1), F(2), F(4), F(8)]:
            beta = (6 - kappa) * s1 / 3
            first = A1 - beta * D1 + kappa * D21 / 2
            second = A2 - beta * D2 + kappa * D22 / 2
            assert first == 0
            assert second != 0
            assert second / D2 == (6 - kappa) * (1 / y2 - 1 / y1) / 3
            wrong_kappa_single += 1
            wrong_kappa_two += 1
        # Solve signed-measure coefficients for arbitrary test residual densities.
        r1, r2 = F(index - 10, 7), F(12 - index, 11)
        dq = 3 * (r2 - r1) / (s1 - s2)
        dv = (s2 * r1 - s1 * r2) / (s1 - s2)
        assert -dv - s1 * dq / 3 == r1
        assert -dv - s2 * dq / 3 == r2
        drift_checks += 1
        if time.process_time() - start_cpu > 0.5:
            raise RuntimeError("Scalar audit exceeded its half-second CPU gate")

    errors = []
    for n in [2, 4, 8, 16]:
        values = [F((-1)**k, n) for k in range(n * n + 1)]
        variation = sum(abs(values[k + 1] - values[k]) for k in range(n * n))
        supnorm = max(map(abs, values))
        assert supnorm == F(1, n) and variation == 2 * n
        errors.append({"n": n, "supnorm": str(supnorm), "total_variation": str(variation)})

    # The two possible signs give symmetric marginals but conditional drift.
    increments = [F(z) * (F(3) - F(1)) for z in [-1, 1]]
    assert sum(increments) == 0 and all(i != 0 for i in increments)
    result = {
        "status": "PASS",
        "command": "python -X utf8 ~/brain_workers/w408/verify_reduction.py",
        "gate": gate,
        "state_triples": len(triples),
        "valid_kappa6_states": valid_kappa6,
        "incorrect_kappa_controls": wrong_kappa_single,
        "single_equation_incorrect_accepts": wrong_kappa_single,
        "two_equation_incorrect_accepts": 0,
        "two_equation_incorrect_rejects": wrong_kappa_two,
        "residual_measure_identities_checked": drift_checks,
        "min_normalized_separation": str(min_separation),
        "small_error_variation_counterexamples": errors,
        "marginal_symmetry_counterexample_states": 2,
        "wall_seconds": time.perf_counter() - start_wall,
        "cpu_seconds": time.process_time() - start_cpu,
        "mathematical_scope": "finite exact algebra and counterexamples only",
        "formal_theorem_check": None,
        "square_lattice_cardy_input_proved": False,
        "full_target_solved": False,
    }
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    try:
        print(json.dumps(run(), indent=2))
    except RuntimeError as exc:
        receipt = {"status":"HELD", "reason":str(exc), "tested_states":0,
                   "full_target_solved":False, "improvement_claim":False,
                   "command":"python -X utf8 ~/brain_workers/w408/verify_reduction.py"}
        (ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
        print(json.dumps(receipt, indent=2))
        raise SystemExit(2)
