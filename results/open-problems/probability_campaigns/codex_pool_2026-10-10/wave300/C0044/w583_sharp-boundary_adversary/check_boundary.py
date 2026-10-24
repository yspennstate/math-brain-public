"""Small exact checks; these verify algebra and a killed-chain BVP, not C0044."""
from fractions import Fraction as F
from pathlib import Path
import json
import time

base = Path(__file__).resolve().parent
started = time.perf_counter()
gate = {"cpu_seconds_limit": 15, "dimensions": [3, 4, 7, 10], "kappa_fractions_of_max": ["1/8", "1/2", "9/10", "99/100"], "states": "-40..40", "max_killed_interval_halfwidth": 16, "gpu": False, "external_dependencies": False}
harmonic_checks = 0
bvp_checks = 0
examples = []

def h(k, ratio):
    return 1 - ratio**k / 2 if k >= 0 else ratio**(-k) / 2

def solve_killed(halfwidth, p, q, c):
    # Thomas elimination of c*u(k)-right(k)*u(k+1)-left(k)*u(k-1)=0,
    # with independent Dirichlet values u(-L)=0, u(L)=1.
    keys = list(range(-halfwidth + 1, halfwidth))
    diag, upper, rhs, lower = [], [], [], []
    for k in keys:
        right, left = (p, q) if k > 0 else (q, p) if k < 0 else (c/2, c/2)
        diag.append(c)
        upper.append(-right)
        lower.append(-left)
        rhs.append(right if k == halfwidth-1 else F(0))
    for i in range(1, len(keys)):
        multiplier = lower[i] / diag[i-1]
        diag[i] -= multiplier * upper[i-1]
        rhs[i] -= multiplier * rhs[i-1]
    values = [F(0)] * len(keys)
    values[-1] = rhs[-1] / diag[-1]
    for i in reversed(range(len(keys)-1)):
        values[i] = (rhs[i] - upper[i]*values[i+1]) / diag[i]
    return dict(zip(keys, values))

for d in gate["dimensions"]:
    for factor in map(F, gate["kappa_fractions_of_max"]):
        kappa = factor / (2*d)
        c = 1 - 2*(d-1)*kappa
        p, q = c-kappa, kappa
        ratio = q/p
        assert 0 < ratio < 1
        assert p+q+2*(d-1)*kappa == 1
        assert min(p, q, c/2) >= kappa
        for k in range(-40, 41):
            right, left = (p, q) if k > 0 else (q, p) if k < 0 else (c/2, c/2)
            residual = right*h(k+1, ratio)+left*h(k-1, ratio)+(1-c)*h(k, ratio)-h(k, ratio)
            assert residual == 0, (d, kappa, k, residual)
            assert 0 < h(k, ratio) < 1
            assert h(k, ratio)+h(-k, ratio) == 1
            harmonic_checks += 1
        for halfwidth in (2, 5, 16):
            killed = solve_killed(halfwidth, p, q, c)
            for k, value in killed.items():
                predicted = (h(k, ratio)-h(-halfwidth, ratio))/(h(halfwidth, ratio)-h(-halfwidth, ratio))
                assert predicted == value
                assert abs(value-h(k, ratio)) <= ratio**halfwidth/(2*(1-ratio**halfwidth))
                bvp_checks += 1
        examples.append({"d": d, "kappa": str(kappa), "ratio": str(ratio), "h_minus_40": float(h(-40, ratio)), "h_zero": str(h(0, ratio)), "h_plus_40": float(h(40, ratio))})
        assert time.perf_counter()-started < gate["cpu_seconds_limit"]

result = {"status": "PASS", "command": "python -X utf8 ~/brain_workers/w583/check_boundary.py", "fresh_compute_gate": gate, "environments_checked": len(examples), "exact_harmonic_checks": harmonic_checks, "independent_exact_killed_bvp_checks": bvp_checks, "max_exact_residual": "0", "elapsed_seconds": time.perf_counter()-started, "examples": examples, "limits": "Finite exact verification is not an independent referee review or a formal proof receipt; no parent problem solved."}
(base / "measurements.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k != "examples"}, indent=2))
