"""Small independent numerical checks, not a proof of the infinite-volume claim.

Run only after a fresh approved small-CPU compute gate. No numpy, model loads,
GPU, subprocesses, sockets, or external writes. All output is in this folder.
"""
from __future__ import annotations

import cmath
import itertools
import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
checks = []


def sine_cutoff_check(L: int, energy: float) -> dict:
    d = 3
    theta = math.pi / (L + 1)
    k = math.acos(-energy / (2 * d))
    scale = (2 / (L + 1)) ** (d / 2)
    wave = {
        x: scale * math.prod(math.sin(theta * t) for t in x)
        * cmath.exp(1j * k * sum(x))
        for x in itertools.product(range(1, L + 1), repeat=d)
    }
    residual = {x: -energy * value for x, value in wave.items()}
    for x, value in wave.items():
        for j in range(d):
            for step in (-1, 1):
                y = tuple(t + (step if a == j else 0) for a, t in enumerate(x))
                residual[y] = residual.get(y, 0j) - value
    observed = math.fsum(abs(value) ** 2 for value in residual.values())
    expected = energy ** 2 * (1 - math.cos(theta)) ** 2 + 4 * math.sin(theta) ** 2 * (
        (L - 1) / (L + 1) * d * math.sin(k) ** 2 + d / (L + 1)
    )
    error = abs(observed - expected)
    assert error < 2e-11, (L, energy, observed, expected)
    assert abs(math.fsum(abs(v) ** 2 for v in wave.values()) - 1) < 2e-12
    assert math.sqrt(observed) <= d * theta ** 2 + 2 * math.sqrt(d) * theta + 1e-12
    return {"L": L, "E": energy, "residual_squared": observed,
            "formula_absolute_error": error}


for L in (3, 7, 15):
    for energy in (-6.0, -5.97, 0.0, 2.4, 6.0):
        checks.append(sine_cutoff_check(L, energy))

# A four-site-period torus has a zero free energy at k_j=pi/2.
# Constant potential gives independent scalar Fourier calculations for the
# candidate power identities. This is a boundary sanity check, not an iid proof.
torus_h = [-2 * math.fsum(math.cos(2 * math.pi * a / 4) for a in indices)
           for indices in itertools.product(range(4), repeat=3)]
power_checks = []
for eta in (0.05, 0.1, 0.2):
    coupling = 0.1
    ratio = coupling / eta
    multipliers = [1 / complex(h, -eta) for h in torus_h]
    for n in (0, 1, 4, 8):
        observed = max(abs(r * (-coupling * r) ** n) for r in multipliers)
        expected = ratio ** n / eta
        assert abs(observed / expected - 1) < 2e-12
        power_checks.append({"eta": eta, "lambda": coupling, "order": n,
                             "term_norm": observed, "expected": expected,
                             "ratio": ratio})

result = {
    "status": "PASS",
    "geometry_checks": len(checks),
    "power_checks": len(power_checks),
    "max_geometry_absolute_error": max(c["formula_absolute_error"] for c in checks),
    "elapsed_seconds": time.perf_counter() - started,
    "geometry": checks,
    "powers": power_checks,
    "limitation": "Finite calculations check formulas only. The author proof supplies rare iid cubes, the infinite-volume limit, and necessity of the threshold. No formal proof or ac/GOE result is certified.",
}
output = ROOT / 'MEASUREMENTS.json'
output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if k not in ('geometry', 'powers')}))
