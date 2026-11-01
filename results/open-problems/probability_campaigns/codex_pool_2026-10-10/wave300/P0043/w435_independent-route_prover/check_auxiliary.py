"""Small independent sanity checks; these are not a proof of P0043."""
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
start = time.monotonic()
gate = {
    "created_at": datetime.now(timezone.utc).isoformat(),
    "worker": "w435", "purpose": "P0043 auxiliary exact and deterministic checks",
    "max_seconds_after_python_start": 45, "max_threads": 1,
    "max_enumerated_configurations": 12000, "max_tree_depth": 4096,
    "network": False, "gpu": False, "training": False,
    "outputs": ["COMPUTE_GATE.json", "MEASUREMENTS.json"],
}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")

count = 0
checks = 0
def tick(n=0):
    global count
    count += n
    assert count <= gate["max_enumerated_configurations"]
    assert time.monotonic() - start < gate["max_seconds_after_python_start"]

def mass(bits, p):
    k = sum(bits)
    return p**k * (1-p)**(len(bits)-k)

# Two length-three paths with exactly one shared edge, on a five-edge graph.
paths = ((0, 1, 2), (0, 3, 4))
def reaches(bits):
    return any(all(bits[e] for e in path) for path in paths)

exact = []
for q in (F(1, 4), F(1, 2), F(3, 4)):
    mean = second = surv = F(0)
    for bits in product((0, 1), repeat=5):
        tick(1)
        probability = mass(bits, q)
        y = sum(F(int(all(bits[e] for e in path)), 2) * q**-3 for path in paths)
        mean += probability*y
        second += probability*y*y
        surv += probability*int(reaches(bits))
    assert mean == 1
    assert second == (q**-3 + q**-1)/2
    assert surv == 2*q**3-q**5
    assert surv >= 1/second
    checks += 4
    exact.append({"q": str(q), "mean": str(mean), "second": str(second),
                  "survival": str(surv), "second_moment_lower_bound": str(1/second)})

# Enumerate the host and thinning independently; compare with direct pq retention.
compositions = []
states = list(product((0, 1), repeat=5))
for p in (F(1, 4), F(1, 2), F(3, 4)):
    for r in (F(1, 4), F(1, 2), F(3, 4)):
        probability = F(0)
        for host in states:
            for thin in states:
                tick(1)
                if reaches(tuple(a*b for a, b in zip(host, thin))):
                    probability += mass(host, p)*mass(thin, r)
        q = p*r
        assert probability == 2*q**3-q**5
        checks += 1
        compositions.append({"p": str(p), "r": str(r), "survival": str(probability)})

# Independently group the common-prefix energy by square levels.
energy_checks = []
for kmax in (1, 2, 4, 8, 16, 32, 63):
    depth = (kmax+1)**2-1
    assert depth <= gate["max_tree_depth"]
    energy = F(1) + sum((F(1, 2**isqrt(n)) for n in range(1, depth+1)), F(0))/2
    exact_tail = F(2*kmax+5, 2**(kmax+1))
    assert energy+exact_tail == F(7, 2)
    checks += 1
    energy_checks.append({"depth": depth, "energy": str(energy), "remaining_tail": str(exact_tail)})

# Deterministic finite-depth survival recursion; independent of ray counting.
tree = []
with localcontext() as ctx:
    ctx.prec = 80
    for depth in (16, 64, 256, 1024, 4096):
        for p in (Decimal("0.49"), Decimal("0.5"), Decimal("0.51")):
            s = Decimal(1)
            for n in range(depth, 0, -1):
                b = 4 if isqrt(n)**2 == n else 2
                s = 1-(1-p*s)**b
            expectation = (2*p)**depth * Decimal(2)**isqrt(depth)
            assert 0 <= s <= min(Decimal(1), expectation) + Decimal("1e-65")
            if p == Decimal("0.5"):
                assert s >= Decimal(2)/7
            checks += 1 + int(p == Decimal("0.5"))
            tick()
            tree.append({"p": str(p), "depth": depth, "root_survival": str(s),
                         "expected_open_level_size": str(expectation)})

# Quantitative finite-cut version of the square-lattice obstruction.
cutsets = []
for nmax in (16, 256, 4096):
    tick()
    resistance = sum(1/(8*n+4) for n in range(nmax))
    cutsets.append({"square_boundaries": nmax, "unit_flow_energy_lower_bound": resistance,
                    "I_at_r_half_lower_bound": 1+resistance})

result = {
    "status": "PASS", "mathematical_scope": "auxiliary sanity checks, not P0043 proof or infinite-limit numerical certification",
    "checks_passed": checks, "enumerated_configurations": count,
    "elapsed_seconds": time.monotonic()-start,
    "finite_path_exact_checks": exact, "thinning_composition_checks": compositions,
    "square_generation_energy_checks": energy_checks,
    "finite_depth_survival_recursion": tree, "square_lattice_cutset_bounds": cutsets,
    "command": "python -X utf8 ~/brain_workers/w435/check_auxiliary.py",
}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("status", "checks_passed", "enumerated_configurations", "elapsed_seconds")}))
print(json.dumps({"critical_depth_4096": next(x for x in tree if x["depth"] == 4096 and x["p"] == "0.5")}))
