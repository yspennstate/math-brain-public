"""Bounded quadrature checks of INDEPENDENT.md; numbers are not a proof."""
from pathlib import Path
import json
import math
import os
import time

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
root = Path(__file__).resolve().parent
start = time.monotonic()

try:
    from scipy.integrate import quad
    from scipy.special import j0, j1, jv
except ImportError:
    result = {"status": "dependency_unavailable", "proof_status": "unchanged; analytic derivation requires independent review"}
    (root / "numerical_probe.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result))
    raise SystemExit(0)

rows = []
for radius in [2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0]:
    if time.monotonic() - start > 40:
        raise RuntimeError("Compute gate reached; do not expand this experiment")
    for alpha in [0.0, math.pi / 2]:
        angular = math.cos(2 * alpha)
        def integrand(t):
            if t < 1e-4:
                return t * (0.25-angular/8) + t**3 * (-1/64+angular/96)
            return (1-j0(t)-angular*jv(2,t))/t
        integral, err = quad(integrand, 0, radius, epsabs=1e-10, epsrel=1e-10, limit=300)
        variance = integral / (2*math.pi)
        ct = math.exp(-variance/2)
        vtheta = 1/(16*math.pi)
        ctheta = j1(radius)/(8*math.pi*radius)
        c6 = math.exp(-36*(vtheta-ctheta))
        row = {"r": radius, "alpha": alpha, "variance_q": variance, "ct": ct, "ct_times_r_eta": ct*radius**(1/(4*math.pi)), "c6": c6, "c6_plateau": math.exp(-36*vtheta), "quadrature_error": err}
        assert variance >= 0 and 0 < ct <= 1 and 0 < c6 <= 1
        rows.append(row)

effective_exponents = []
for alpha in [0.0, math.pi/2]:
    selected = [row for row in rows if row["alpha"] == alpha]
    last, previous = selected[-1], selected[-2]
    effective_exponents.append(-math.log(last["ct"]/previous["ct"])/math.log(last["r"]/previous["r"]))
assert max(abs(v-1/(4*math.pi)) for v in effective_exponents) < 0.002
assert abs(rows[-1]["c6"]-rows[-1]["c6_plateau"]) < 0.0002

result = {"status": "pass", "model": "aT=1,aL=0,Lambda=1,|q|=1", "rows": rows, "predicted_positional_exponent": 1/(4*math.pi), "effective_exponents_at_largest_radii": effective_exponents, "elapsed_seconds": time.monotonic()-start, "proof_status": "numerical check only; not a particle-gas result", "command": "python -X utf8 ~/brain_workers/w541/numerical_probe.py"}
(root / "numerical_probe.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({key: value for key,value in result.items() if key != "rows"}))
