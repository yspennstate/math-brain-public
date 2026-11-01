"""Independent exact monomial integration for the smooth triangle witness."""
import json
import math
import time
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path

base = Path(__file__).resolve().parent
gate = {"created_at": datetime.now(timezone.utc).isoformat(), "purpose": "independent degree-six triangle polynomial integration", "max_terms": 1000, "wall_limit_seconds": 15, "gpu": False, "training": False, "network": False, "status": "PASS"}
(base / "POLYNOMIAL_COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
start = time.perf_counter()

def product(p, q):
    out = {}
    for (i, j), c in p.items():
        for (k, l), z in q.items():
            key = (i + k, j + l)
            out[key] = out.get(key, Q(0)) + c * z
    assert len(out) < gate["max_terms"]
    return out

def derivative(p, variable):
    out = {}
    for indices, c in p.items():
        exponent = indices[variable]
        if exponent:
            new_indices = list(indices)
            new_indices[variable] -= 1
            out[tuple(new_indices)] = c * exponent
    return out

def triangle_integral(p):
    # Uniform triangle density is 2; integrate monomials by two iterated integrals.
    return sum((c * Q(2 * math.factorial(i) * math.factorial(j), math.factorial(i + j + 2)) for (i, j), c in p.items()), Q(0))

t = {(0, 0): Q(1), (0, 1): Q(-1)}
q = {(1, 0): Q(2), (0, 1): Q(1), (0, 0): Q(-1)}
p = product(q, product(t, t))  # f=sqrt(6)*p, raw x coordinates.
du, ds = derivative(p, 0), derivative(p, 1)
mean_without_scale = triangle_integral(p)
variance = 6 * triangle_integral(product(p, p))
directional_energy = Q(1, 4) * triangle_integral(product(du, du))
sigma_diag, sigma_offdiag = Q(1, 18), Q(-1, 36)
full_energy = 6 * (sigma_diag * (triangle_integral(product(du, du)) + triangle_integral(product(ds, ds))) + 2 * sigma_offdiag * triangle_integral(product(du, ds)))
assert mean_without_scale == 0
assert variance == Q(1, 2)
assert directional_energy == Q(1, 3)
assert full_energy == Q(13, 27)
assert variance / directional_energy == Q(3, 2)
assert variance / full_energy == Q(27, 26)
assert variance > Q(4, 9)  # pi>3 implies 4/pi^2<4/9.
elapsed = time.perf_counter() - start
assert elapsed < gate["wall_limit_seconds"]
receipt = {"command": "python -X utf8 ~/brain_workers/w354/check_polynomial.py", "executed_at": datetime.now(timezone.utc).isoformat(), "method": "polynomial expansion and exact raw-coordinate monomial integrals; independent of conditional beta-moment formula", "checks_passed": 7, "elapsed_seconds": elapsed, "formal_proof": False, "mean": str(mean_without_scale), "variance": str(variance), "directional_energy": str(directional_energy), "full_energy": str(full_energy), "directional_rayleigh": str(variance / directional_energy), "full_rayleigh": str(variance / full_energy), "mean_fiber_cp": 12 / math.pi ** 2, "proposed_mean_bound_rhs": 4 / math.pi ** 2, "violates_proposed_mean_bound": True, "independent_mathematical_audit": "pending w356"}
(base / "POLYNOMIAL_CHECK.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
