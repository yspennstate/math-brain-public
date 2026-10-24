"""Exact-arithmetic sanity check; the asymptotic proof is in the Markdown file."""

from fractions import Fraction
import json
from pathlib import Path
import time

gate = json.loads(Path("compute_gate_endpoint.json").read_text(encoding="utf-8"))
tau = Fraction(4, 5)
rho = Fraction(2, 5)
start = time.monotonic()
rows = []
for m in (3, 6, 9, 12):
    depth = m * m
    assert m <= gate["maximum_m"] and depth <= gate["maximum_binary_depth"]
    assert time.monotonic() - start < gate["hard_loop_deadline_seconds"]
    bush = sum((2 * tau) ** h for h in range(depth + 1))
    handle = sum(tau**j for j in range(1, m + 1))
    mixed = sum(tau**j * rho ** (m - j) for j in range(1, m + 1))
    k = (bush * rho**m + mixed) / (bush + handle)
    ratio = k / tau**m
    bound = Fraction(1, 2) ** m + 4 * Fraction(5, 8) ** depth * Fraction(5, 4) ** m
    assert ratio <= bound
    rows.append({"m": m, "H": depth, "ratio_float": float(ratio),
                 "bound_float": float(bound)})
print(json.dumps({"status": "PASS", "cases": len(rows),
                  "elapsed_seconds": time.monotonic() - start,
                  "rows": rows, "scope": "Finite sanity check, not asymptotic proof"}, indent=2))
