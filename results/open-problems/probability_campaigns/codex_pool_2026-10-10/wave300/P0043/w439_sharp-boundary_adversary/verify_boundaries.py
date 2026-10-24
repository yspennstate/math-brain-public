"""Small, deterministic checks; finite checks do not prove infinite-volume limits.

Compute gate: no network or stores; <= 9 edges per enumeration, <= 1,024
enumerated configurations in total, <= 10,000 recurrence steps, 5 seconds CPU.
All output files are inside w439. Run: python -X utf8 verify_boundaries.py
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
started = time.process_time()
MAX_CONFIGS = 1024
configs = 0
checks = []


def check(name, condition, evidence):
    if time.process_time() - started > 5:
        raise RuntimeError("CPU gate exceeded")
    if not condition:
        raise AssertionError((name, evidence))
    checks.append({"name": name, "verdict": "PASS", "evidence": evidence})


def enumerate_event(edges, targets):
    global configs
    if len(edges) > 9 or configs + 2 ** len(edges) > MAX_CONFIGS:
        raise RuntimeError("Enumeration gate exceeded")
    counts = Counter()
    for bits in product((0, 1), repeat=len(edges)):
        configs += 1
        neighbors = {}
        for opened, (a, b) in zip(bits, edges):
            if opened:
                neighbors.setdefault(a, []).append(b)
                neighbors.setdefault(b, []).append(a)
        seen = {0}
        pending = [0]
        while pending:
            for vertex in neighbors.get(pending.pop(), ()):
                if vertex not in seen:
                    seen.add(vertex)
                    pending.append(vertex)
        if seen.intersection(targets):
            counts[sum(bits)] += 1
    return counts


def critical_root(n):
    u = F(1)
    for _ in range(n - 1):
        u -= u * u / 4
    return 1 - (1 - u / 2) ** 3


# Independent graph traversal over every configuration, rather than recursion.
edges_one = [(0, 1), (0, 2), (0, 3)]
counts = enumerate_event(edges_one, {1, 2, 3})
probability = F(sum(counts.values()), 2 ** len(edges_one))
check("critical-root-depth-1", probability == critical_root(1) == F(7, 8), str(probability))

edges_two = edges_one + [(1, 4), (1, 5), (2, 6), (2, 7), (3, 8), (3, 9)]
counts = enumerate_event(edges_two, set(range(4, 10)))
probability = F(sum(counts.values()), 2 ** len(edges_two))
check("critical-root-depth-2", probability == critical_root(2) == F(387, 512), str(probability))

# Enumerate all six bonds in a 2-subdivided 3-arm star; recover its polynomial.
star = [(0, 1), (1, 4), (0, 2), (2, 5), (0, 3), (3, 6)]
counts = enumerate_event(star, {4, 5, 6})
coefficients = [0] * 7
for opened, count in counts.items():
    for j in range(6 - opened + 1):
        coefficients[opened + j] += count * comb(6 - opened, j) * (-1) ** j
check("subdivision-star-polynomial", coefficients == [0, 0, 3, 0, -3, 0, 1], coefficients)
critical_value = 3 * F(1, 2) - 3 * F(1, 2) ** 2 + F(1, 2) ** 3
check("subdivision-critical-radius-L", critical_value == F(7, 8), str(critical_value))

shell_values = [F(3 * 2 ** (k - 1), 2 ** k) for k in range(1, 33)]
check("critical-branch-shell-expectation", all(v == F(3, 2) for v in shell_values), {"shells_checked": 32, "sum": str(sum(shell_values))})
subcritical = [{"p": str(p), "chi": str(1 + 3 * p / (1 - 2 * p))} for p in (F(1, 4), F(49, 100), F(499, 1000), F(4999, 10000))]

# w438's identity, checked with rational p including the endpoint p=1.
patterns = ((), (1,), (2,), (1, 2, 1, 2), (2, 1, 2, 2, 1, 2), (2,) * 8)
for offspring in patterns:
    for p in (F(1, 4), F(1, 2), F(3, 4), F(1)):
        n = len(offspring)
        q = [F(0)] * n + [F(1)]
        for i in range(n - 1, -1, -1):
            # Generating-function recursion, distinct from reciprocal formula.
            q[i] = 1 - (1 - p * q[i + 1]) ** offspring[i]
        means = [F(1)]
        for a in offspring:
            means.append(means[-1] * a * p)
        correction = sum(F(1, 4) / ((1 - p * q[i + 1] / 2) * means[i]) for i, a in enumerate(offspring) if a == 2)
        rhs = 1 / means[n] + correction
        check("w438-reciprocal-" + "".join(map(str, offspring)) + "-p-" + str(p), 1 / q[0] == rhs, {"n": n, "p": str(p)})

# Illustration only: the exact proof of the asymptotic is in INDEPENDENT.md.
u = 1.0
asymptotic = []
for n in range(1, 10001):
    root_probability = 1.5 * u - 0.75 * u * u + 0.125 * u ** 3
    if n in (1, 10, 100, 1000, 10000):
        asymptotic.append({"skeleton_radius": n, "n_times_root_probability": n * root_probability})
    u -= u * u / 4
check("recurrence-stays-positive", 0 < u < 1, {"iterations": 10000, "role": "finite illustration only"})

result = {"command": "python -X utf8 verify_boundaries.py", "passed": len(checks), "failed": 0, "enumerated_configurations": configs, "maximum_edges_enumerated": 9, "cpu_seconds": time.process_time() - started, "checks": checks, "subcritical_susceptibility": subcritical, "asymptotic_illustration": asymptotic, "mathematical_limit_proof": "INDEPENDENT.md", "scope": "Finite exact checks and algebraic consistency; no formal proof receipt or infinite-volume numerical proof."}
(ROOT / "measurements.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: result[key] for key in ("passed", "failed", "enumerated_configurations", "cpu_seconds")}))
print(json.dumps(asymptotic))
