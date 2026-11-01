"""Small exact controls for the continuous kernel and its noise normalization.

No asymptotic experiment, model load, network call, or GPU code is used.
Read the existing governor immediately before these bounded, single-process checks.
"""
import json
import pathlib
import time
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parent


def fresh_gate():
    state_path = pathlib.Path("~/.claude/compute/compute_state.json")
    age = time.time() - state_path.stat().st_mtime
    state = json.loads(state_path.read_text(encoding="utf-8-sig"))
    status = state.get("status", "unknown")
    allowed = 0 <= age <= 600 and status in ("ok", "warn", "retired")
    receipt = {
        "source": str(state_path), "age_seconds": round(age, 3),
        "status": status, "mode": state.get("mode"),
        "cpu_pct": state.get("cpu_pct"),
        "mem_avail_mb": state.get("mem_avail_mb"),
        "reasons": state.get("reasons", []),
        "scope": "one short-lived CPU process; exact rational arithmetic only",
        "max_cases": 300, "max_seconds_after_gate": 5,
        "allowed": allowed,
    }
    (ROOT / "COMPUTE_GATE.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    if not allowed:
        raise RuntimeError("Fresh small-compute gate unavailable; receipt saved, no checks run")
    return receipt


def integrate(poly, lo=F(0), hi=F(1)):
    return sum(c * (hi ** (i + 1) - lo ** (i + 1)) / (i + 1) for i, c in enumerate(poly))


def mul(p, q):
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return result


def capped_mean(a):
    return integrate([F(0), F(1)], F(0), a) + integrate([a], a, F(1))


def direct_cov(a, b):
    # Independent exact piecewise integration of the random variables.
    points = sorted({F(0), a, b, F(1)})
    second = F(0)
    for lo, hi in zip(points, points[1:]):
        mid = (lo + hi) / 2
        p = [a] if mid >= a else [F(0), F(1)]
        q = [b] if mid >= b else [F(0), F(1)]
        second += integrate(mul(p, q), lo, hi)
    return second - capped_mean(a) * capped_mean(b)


def kernel(a, b):
    m, big = min(a, b), max(a, b)
    return m * m / 2 * (big - big * big / 2 - m / 3)


def main():
    gate = fresh_gate()
    start = time.perf_counter()
    thresholds = [F(0), F(1, 128), F(1, 64), F(1, 16), F(1, 4), F(1, 2), F(3, 4), F(1)]
    covariance_checks = 0
    for a in thresholds:
        for b in thresholds:
            assert kernel(a, b) == direct_cov(a, b)
            assert kernel(a, b) >= 0
            covariance_checks += 1

    # T=1+min(U,V): a continuous two-parallel-edge control, not lattice FPP.
    # Direct distribution: min(U,V) has density 2(1-u).
    density = [F(2), F(-2)]
    mean = integrate(mul([F(0), F(1)], density))
    second = integrate(mul([F(0), F(0), F(1)], density))
    direct_variance = second - mean * mean
    assert direct_variance == F(1, 18)

    # Single-coordinate projection g(u)=E_V[min(u,V)].
    projection = [F(0), F(1), F(-1, 2)]
    first_level = integrate(mul(projection, projection)) - integrate(projection) ** 2
    assert first_level == F(1, 45)
    pair_level = direct_variance - 2 * first_level
    assert pair_level == F(1, 90)

    diagonal_average = integrate([F(0), F(0), F(0), F(1, 3), F(-1, 4)])
    # Independently integrate the explicit kernel on 0<=a<=b<=1, then reflect.
    triangle_terms = [(F(1, 2), 2, 1), (F(-1, 4), 2, 2), (F(-1, 6), 3, 0)]
    independent_average = 2 * sum(c / ((i + 1) * (i + j + 2)) for c, i, j in triangle_terms)
    assert diagonal_average == F(1, 30)
    assert independent_average == first_level
    noise_checks = 0
    for rho in (F(0), F(1, 16), F(1, 4), F(3, 4), F(1)):
        from_refresh_coupling = 2 * (rho * diagonal_average + (1 - rho) * independent_average)
        from_orthogonal_levels = 2 * first_level + 2 * rho * pair_level
        assert from_refresh_coupling == from_orthogonal_levels
        noise_checks += 1
    noise_poly = [2 * first_level, 2 * pair_level]
    corrected_integral = integrate(noise_poly)
    assert corrected_integral == direct_variance
    # Deliberately invalid control: resampling e too, without compensating 1/rho.
    wrong_integral = integrate([F(0)] + noise_poly)
    assert wrong_integral != direct_variance
    assert direct_variance - wrong_integral == F(7, 270)
    assert noise_poly[0] == F(2, 45)  # first-order floor persists.

    eta = F(1, 64)
    margin_checks = 0
    for a in thresholds[2:]:
        for b in thresholds[2:]:
            assert kernel(a, b) >= kernel(eta, eta)
            margin_checks += 1
    invalid_bare_overlap_failures = sum(kernel(F(k, 64), F(k, 64)) < F(k, 64) / 12 for k in range(1, 65))
    assert invalid_bare_overlap_failures == 49
    assert kernel(eta, eta) / eta < F(1, 12)

    union_bound_checks = 0
    for n in range(9, 109):
        assert F(16, 3) * F(3, 4) ** n <= F(1, 2)
        assert 2 * eta * eta * n == F(n, 2048)
        assert F(3 * n, 2048) - 2 * eta * eta * n == F(n, 1024)
        union_bound_checks += 1
    assert F(16, 3) * F(3, 4) ** 8 > F(1, 2)
    elapsed = time.perf_counter() - start
    assert elapsed <= 5, "unexpectedly slow exact checks"
    receipt = {
        "command": "python -X utf8 -B ~/brain_workers/w360/verify_math.py",
        "result": "PASS", "elapsed_seconds": round(elapsed, 6),
        "gate_age_seconds": gate["age_seconds"],
        "exact_covariance_pairs": covariance_checks,
        "exact_refresh_couplings": noise_checks,
        "positive_margin_controls": margin_checks,
        "union_bound_constant_checks": union_bound_checks,
        "continuous_toy_variance": str(direct_variance),
        "invalid_normalization_control_error": str(direct_variance - wrong_integral),
        "corrected_normalization_error": str(direct_variance - corrected_integral),
        "first_order_floor": str(noise_poly[0]),
        "deliberately_invalid_bare_overlap_control_failures": invalid_bare_overlap_failures,
        "bare_overlap_control_cases": 64,
        "measurement_scope": "Exact finite controls and proof-constant arithmetic; no asymptotic exponent measurement, deployed recall improvement, or formal proof receipt",
    }
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
