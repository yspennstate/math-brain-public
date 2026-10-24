"""Small CPU-only numerical cross-checks; these are not mathematical proofs."""
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
CPU_START = time.process_time()
EVALUATIONS = 0
MAX_EVALUATIONS = 200000
MAX_CPU_SECONDS = 10


def gated(f, x):
    global EVALUATIONS
    EVALUATIONS += 1
    if EVALUATIONS > MAX_EVALUATIONS or time.process_time() - CPU_START > MAX_CPU_SECONDS:
        raise RuntimeError("Fresh scalar compute gate exhausted; no larger run authorized")
    return f(x)


def quad(f, a, b, tol=2e-10):
    fa, fb = gated(f, a), gated(f, b)
    m = (a + b) / 2
    fm = gated(f, m)
    whole = (b - a) * (fa + 4 * fm + fb) / 6

    def rec(a, b, fa, fm, fb, whole, tol, depth):
        m = (a + b) / 2
        l, r = (a + m) / 2, (m + b) / 2
        fl, fr = gated(f, l), gated(f, r)
        left = (m - a) * (fa + 4 * fl + fm) / 6
        right = (b - m) * (fm + 4 * fr + fb) / 6
        err = left + right - whole
        if abs(err) <= 15 * tol:
            return left + right + err / 15
        if depth == 0:
            raise RuntimeError("Scalar quadrature depth gate exhausted")
        return rec(a, m, fa, fl, fm, left, tol / 2, depth - 1) + rec(m, b, fm, fr, fb, right, tol / 2, depth - 1)

    return rec(a, b, fa, fm, fb, whole, tol, 26)


def closed(b, lam):
    c = 1 / (math.pi * b)
    # Rationalized form avoids cancellation when c is small.
    return 2 / lam * math.log1p(c / (2 * (math.sqrt(1 + c) + 1)))


gate = {
    "issued_at_utc": datetime.now(timezone.utc).isoformat(),
    "purpose": "C0056 scalar identity and finite-cavity normalization cross-checks",
    "max_cpu_seconds": MAX_CPU_SECONDS,
    "max_function_evaluations": MAX_EVALUATIONS,
    "max_processes": 1,
    "gpu": False,
    "training": False,
    "formal_proof": False,
}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")

identity_checks = []
for b in [1e-8, 1e-6, 1e-4, 1e-2, 0.1, 1, 10, 100]:
    q = quad(lambda theta: math.log1p(math.cos(theta)**2 / (math.pi * b)), -math.pi / 2, math.pi / 2)
    for lam in [0.1, 1, 2.5]:
        numeric = q / (math.pi * lam)
        exact = closed(b, lam)
        rel = abs(numeric - exact) / max(abs(exact), 1e-15)
        assert rel < 2e-8, (b, lam, numeric, exact, rel)
        assert exact <= math.log1p(1 / (math.pi * b)) / lam + 1e-12
        identity_checks.append({"b": b, "lambda": lam, "numerical_integral": numeric, "formula": exact, "relative_error": rel})

conditional_checks = []
for a in [-3, 0, 0.5, 4]:
    for b in [1e-4, 0.1, 1]:
        lam = 0.7
        lo = math.atan((-lam - a) / b)
        hi = math.atan((lam - a) / b)
        numeric = quad(lambda theta: math.log1p(math.cos(theta)**2 / (math.pi * b)), lo, hi) / (2 * math.pi * lam)
        envelope = closed(b, lam) / 2
        assert 0 <= numeric <= envelope + 1e-9
        conditional_checks.append({"a": a, "b": b, "uniform_site_entropy": numeric, "whole_line_envelope": envelope})

finite_cavity = []
for eta in [1e-2, 1e-4, 1e-6, 1e-8]:
    def integrand(e):
        b = eta * (1 + sum(w / ((d - e)**2 + eta**2) for d, w in [(-2, 1), (0, 2), (3, 3)]))
        return math.log1p(1 / b)
    val = quad(integrand, -1, 0, 2e-8) + quad(integrand, 0, 1, 2e-8)
    finite_cavity.append({"eta": eta, "log_inverse_integral": val, "normalized_by_log_inverse_eta": val / math.log(1 / eta), "limiting_interval_length": 2})
assert all(r["normalized_by_log_inverse_eta"] < 2.01 for r in finite_cavity)
assert finite_cavity[-1]["normalized_by_log_inverse_eta"] > 1.3
assert all(finite_cavity[i + 1]["normalized_by_log_inverse_eta"] > finite_cavity[i]["normalized_by_log_inverse_eta"] for i in range(3))

atomic_counterexample = [{"eta": eta, "sample_entropy_on_R": closed(eta, 1), "annealed_density_bound_lambda_1": 0.5} for eta in [1e-2, 1e-4, 1e-6, 1e-8]]
assert atomic_counterexample[-1]["sample_entropy_on_R"] > atomic_counterexample[0]["sample_entropy_on_R"] + 10

result = {
    "command": "python -X utf8 ~/brain_workers/w480/check_scalar.py",
    "status": "PASS",
    "identity_cases": len(identity_checks),
    "conditional_density_cases": len(conditional_checks),
    "max_identity_relative_error": max(r["relative_error"] for r in identity_checks),
    "function_evaluations": EVALUATIONS,
    "cpu_seconds": time.process_time() - CPU_START,
    "wall_seconds": time.monotonic() - START,
    "identity_checks": identity_checks,
    "conditional_checks": conditional_checks,
    "finite_cavity": finite_cavity,
    "atomic_counterexample": atomic_counterexample,
    "interpretation": "Floating-point numerical checks only; no formal-check receipt and no proof of the unproved infinite-volume bound LG.",
}
(ROOT / "SCALAR_CHECK_RESULTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ["status", "identity_cases", "conditional_density_cases", "max_identity_relative_error", "function_evaluations", "cpu_seconds"]}))
print(json.dumps({"finite_cavity": finite_cavity, "atomic_counterexample": atomic_counterexample}))
