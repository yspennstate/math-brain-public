"""Small exact-arithmetic stress checks for the referee report; no dependencies."""

from fractions import Fraction as F
from itertools import product
from math import comb, prod
import json
import os
from pathlib import Path


def evolve(pmf, m):
    sums = {0: F(1)}
    for _ in range(m):
        nxt = {}
        for i, a in sums.items():
            for j, b in pmf.items():
                nxt[i + j] = nxt.get(i + j, F(0)) + a * b
        sums = nxt
    nxt = {}
    for total, mass in sums.items():
        k = max(total - 1, 0)
        nxt[k] = nxt.get(k, F(0)) + mass
    return nxt


def tree_case(m, depth):
    support = (0, 1, max(2, depth + 1))
    weights = (m, 1, 1)
    denominator = sum(weights)
    leaves = m**depth
    survival_weight = 0
    event_weight = [0] * leaves
    configurations = 0
    for indices in product(range(3), repeat=leaves):
        values = [support[i] for i in indices]
        weight = prod(weights[i] for i in indices)
        levels = [values]
        for _ in range(depth):
            row = levels[-1]
            levels.append([
                max(sum(row[i:i + m]) - 1, 0)
                for i in range(0, len(row), m)
            ])
        events = []
        for v, value in enumerate(values):
            if value < depth + 1:
                continue
            index = v
            allowed = True
            for h in range(depth):
                start = (index // m) * m
                if any(levels[h][j] != 0
                       for j in range(start, start + m) if j != index):
                    allowed = False
                    break
                index //= m
            if allowed:
                events.append(v)
                event_weight[v] += weight
        assert len(events) <= 1, (m, depth, values, events)
        assert not events or levels[-1][0] > 0
        if levels[-1][0] > 0:
            survival_weight += weight
        configurations += 1
    law = {k: F(w, denominator) for k, w in zip(support, weights)}
    event_probability = sum(p for k, p in law.items() if k >= depth + 1)
    for _ in range(depth):
        event_probability *= law.get(0, F(0))**(m - 1)
        law = evolve(law, m)
    sample_denominator = denominator**leaves
    assert all(F(w, sample_denominator) == event_probability for w in event_weight)
    assert leaves * event_probability <= F(survival_weight, sample_denominator)
    assert 1 - law.get(0, F(0)) == F(survival_weight, sample_denominator)
    return {"m": m, "depth": depth, "configurations": configurations,
            "survival": str(F(survival_weight, sample_denominator)),
            "sum_path_event_probabilities": str(leaves * event_probability)}


def identities(m):
    p = {0: F(1, 2), 1: F(1, 4), 3: F(1, 4)}
    for _ in range(3):
        nxt = evolve(p, m)
        q = 1 - p[0]
        q_next = 1 - nxt[0]
        assert q_next == 1 - (1 - q)**m - m * p.get(1, 0) * (1 - q)**(m - 1)
        mean = sum(k * a for k, a in p.items())
        mean_next = sum(k * a for k, a in nxt.items())
        assert mean_next == m * mean - 1 + (1 - q)**m
        for s in (F(1, 2), F(1), F(3, 2), F(m)):
            g = sum(s**k * a for k, a in p.items())
            g_next = sum(s**k * a for k, a in nxt.items())
            assert g_next == g**m / s + (1 - 1 / s) * (1 - q)**m
        for k in range(1, max(nxt) + 1):
            remainder = nxt.get(k, 0) - m * (1 - q)**(m - 1) * p.get(k + 1, 0)
            assert 0 <= remainder <= comb(m, 2) * q**2
        p = nxt
    z = F(1, m)
    first_geometric = (m - 1) * z / (1 - z)**2
    second_geometric = (m - 1) * z * (1 + z) / (1 - z)**3
    a = F(4, (m - 1)**2)
    assert first_geometric == F(m, m - 1)
    assert a * first_geometric == F(4 * m, (m - 1)**3)
    return {"m": m, "M1": str(first_geometric), "M2": str(second_geometric),
            "survival_constant": str(a), "first_moment_constant": str(a * first_geometric)}


if __name__ == "__main__":
    result = {
        "priority": os.getpriority(os.PRIO_PROCESS, 0),
        "tree_cases": [tree_case(m, t) for m, t in
                       [(2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2)]],
        "identity_checks": [identities(m) for m in (2, 3, 4)],
        "status": "all exact assertions passed",
    }
    Path("audit_checks.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
