"""Independent exact enumeration of w468/w469 finite-tree claims."""

from fractions import Fraction
import json
from pathlib import Path
import time

gate = json.loads(Path("compute_gate.json").read_text(encoding="utf-8"))
start = time.monotonic()
s = Fraction(3, 5)  # sech(log 3)
r = 1 - s
p = 1 - s * s


def support_weight(mask: int, m: int, present: Fraction) -> Fraction:
    k = mask.bit_count()
    return present**k * (1 - present) ** (m - k)


def first_run(mask: int, m: int) -> int:
    out = 0
    while out < m and mask & (1 << out):
        out += 1
    return out


def last_run(mask: int, m: int) -> int:
    out = 0
    while out < m and mask & (1 << (m - 1 - out)):
        out += 1
    return out


checks = 0
rows = []
for m in range(1, gate["maximum_bridge_edges"] + 1):
    assert 4**m <= gate["maximum_support_pairs_per_case"]
    original = Fraction()
    augmented = Fraction()
    for left in range(1 << m):
        assert time.monotonic() - start < gate["hard_loop_deadline_seconds"]
        for right in range(1 << m):
            if (left | right) == (1 << m) - 1:
                original += support_weight(left, m, r) * support_weight(right, m, r)
            if first_run(left, m) + last_run(right, m) >= m:
                augmented += support_weight(left, m, p) * support_weight(right, m, p)
    assert original == p**m
    checks += 1
    assert augmented == p**m * (1 + m * (1 - p))
    checks += 1
    assert r**m / p**m == (1 + s) ** (-m)
    checks += 1
    rows.append({"m": m, "original": str(original), "augmented": str(augmented)})

print(json.dumps({"status": "PASS", "checks": checks, "cases": len(rows),
                  "supports_per_last_case": 4**gate["maximum_bridge_edges"],
                  "elapsed_seconds": time.monotonic() - start, "rows": rows,
                  "scope": "Finite-tree checks only; no 3D result"}, indent=2))
