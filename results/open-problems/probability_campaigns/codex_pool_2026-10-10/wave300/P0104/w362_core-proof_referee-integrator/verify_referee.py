"""Exact, bounded proof reproduction; no sampling, training, or external writes."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import time

BASE = Path(__file__).resolve().parent
started = time.perf_counter()
states = list(product((1, 2), repeat=4))
values = {w: min(w[0] + w[1], w[2] + w[3]) for w in states}
selected = []
conditioned = []
for w in states:
    upper = w[0] + w[1] <= w[2] + w[3]
    costs = w[:2] if upper else w[2:]
    selected.append(costs)
    if upper:
        conditioned.append(w[:2])

def covariance(pairs):
    size = len(pairs)
    ex = F(sum(a for a, b in pairs), size)
    ey = F(sum(b for a, b in pairs), size)
    exy = F(sum(a * b for a, b in pairs), size)
    return exy - ex * ey

def variance(items):
    size = len(items)
    return F(sum(v * v for v in items), size) - F(sum(items), size) ** 2

assert covariance(conditioned) == -F(5, 121)
assert covariance(selected) == -F(9, 256)
assert variance(list(values.values())) == F(23, 64)
naive = variance([a for a, b in selected]) + variance([b for a, b in selected])
assert naive == F(55, 128)

# A second independent calculation: Walsh expansion of the square's passage time.
def walsh(w, mask):
    answer = 1
    for i in range(4):
        if mask & (1 << i):
            answer *= 1 if w[i] == 2 else -1
    return answer

coeff = {s: F(sum(values[w] * walsh(w, s) for w in states), 16) for s in range(16)}
mass = {k: sum((coeff[s] ** 2 for s in range(1, 16) if s.bit_count() == k), F(0)) for k in range(1, 5)}
direct_variance = variance(list(values.values()))
assert sum(mass.values(), F(0)) == direct_variance

covariance_checks = []
mean = F(sum(values.values()), 16)
for retain in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
    moment = F(0)
    for w in states:
        for v in states:
            transition = F(1, 16)
            for i in range(4):
                transition *= (1 + retain) / 2 if w[i] == v[i] else (1 - retain) / 2
            moment += transition * values[w] * values[v]
    actual = moment - mean ** 2
    spectral = sum((amount * retain ** k for k, amount in mass.items()), F(0))
    assert actual == spectral
    covariance_checks.append({"retention": str(retain), "direct_covariance": str(actual), "spectral_covariance": str(spectral)})

gradient_energy = F(0)
for i in range(4):
    for w in states:
        for replacement in (1, 2):
            v = list(w)
            v[i] = replacement
            gradient_energy += F((values[tuple(v)] - values[w]) ** 2, 64)
assert gradient_energy == sum((k * amount for k, amount in mass.items()), F(0))

receipt = {
    "command": "python -X utf8 ~/brain_workers/w362/verify_referee.py",
    "kind": "exact finite proof reproduction, not an FPP simulation or formal proof certificate",
    "assignments": 16,
    "conditioning_cases": len(conditioned),
    "conditional_counts": {str(k): v for k, v in sorted(Counter(conditioned).items())},
    "selected_counts": {str(k): v for k, v in sorted(Counter(selected).items())},
    "conditional_covariance": str(covariance(conditioned)),
    "selected_covariance": str(covariance(selected)),
    "before_naive_selected_cost_variance": str(naive),
    "after_exact_selected_cost_variance": str(direct_variance),
    "naive_absolute_error": str(naive - direct_variance),
    "corrected_absolute_error": "0",
    "spectral_variance_mass_by_order": {str(k): str(v) for k, v in mass.items()},
    "gradient_energy": str(gradient_energy),
    "covariance_checks": covariance_checks,
    "all_checks_pass": True,
    "elapsed_seconds": time.perf_counter() - started,
    "scope": "Only the square example and finite-product identities; no asymptotic crossover evidence."
}
(BASE / "REFEREE_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
