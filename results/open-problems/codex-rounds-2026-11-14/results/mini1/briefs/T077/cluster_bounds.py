#!/usr/bin/env python3
"""Exact confinement bounds allowing a four-site tested region."""

import json
import resource
import time
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

from trapping_bounds import check_memory, limits, rational, upper_decimal


ORIGIN = (0, 0)
SEED = (1, 0)
K = frozenset({ORIGIN, (-1, 0), (0, 1), (0, -1)})
STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def neighbors(v):
    x, y = v
    return {(x + dx, y + dy) for dx, dy in STEPS}


G = tuple(sorted(K | set.union(*(neighbors(v) for v in K)) |
                 {(1, 2), (1, -2), (-2, 1), (-2, -1)}))


def backward(rate):
    index = {v: i for i, v in enumerate(G)}
    kmask = sum(1 << index[v] for v in K)
    adjacency = [sum(1 << index[w] for w in neighbors(v) if w in index)
                 for v in G]
    assert all(neighbors(v) <= set(G) for v in K)

    @lru_cache(None)
    def solve(slow, fast):
        check_memory()
        healthy = ((1 << len(G)) - 1) & ~(slow | fast)
        births = [(i, (adjacency[i] & slow).bit_count(),
                   (adjacency[i] & fast).bit_count())
                  for i in range(len(G)) if (healthy >> i) & 1]
        h = sum(s for _, s, _ in births)
        if not h:
            return F(1)
        b = sum(f for _, _, f in births)
        total = h + rate * b
        result = F(0)
        for i, s, f in births:
            bit = 1 << i
            if f:
                result += rate * f * solve(slow, fast | bit)
            if s and bit & kmask:
                result += s * solve(slow | bit, fast)
            # A tested birth outside K contributes zero.
        return result / total

    q = solve(1 << index[ORIGIN], 1 << index[SEED])
    return q, solve.cache_info().currsize


def forward(rate):
    vertices = frozenset(G)
    layer = {(frozenset({ORIGIN}), frozenset({SEED})): F(1)}
    success, failure, states = F(0), F(0), 0
    while layer:
        next_layer = defaultdict(F)
        for (slow, fast), mass in layer.items():
            check_memory()
            states += 1
            healthy = vertices - slow - fast
            s_rates, f_rates = Counter(), Counter()
            for v in slow:
                for w in neighbors(v) & healthy:
                    s_rates[w] += 1
            if not s_rates:
                success += mass
                continue
            for v in fast:
                for w in neighbors(v) & healthy:
                    f_rates[w] += 1
            total = sum(s_rates.values()) + rate * sum(f_rates.values())
            for w, multiplicity in s_rates.items():
                m = mass * multiplicity / total
                if w in K:
                    next_layer[(slow | {w}, fast)] += m
                else:
                    failure += m
            for w, multiplicity in f_rates.items():
                next_layer[(slow, fast | {w})] += mass * rate * multiplicity / total
        layer = next_layer
    assert success + failure == 1
    return success, states


def connectivity_audit():
    vertices = set(G)
    checks = []
    for deleted in ({ORIGIN}, *({ORIGIN, v} for v in K - {ORIGIN})):
        reached = {SEED}
        while True:
            new = reached | set.union(*(neighbors(v) for v in reached))
            new &= vertices - deleted
            if new == reached:
                break
            reached = new
        assert reached == vertices - deleted
        checks.append(sorted(deleted))
    return checks


def expansion():
    """Exact coefficients of the failure probability in epsilon=1/r, to order 2."""
    vertices = frozenset(G)

    @lru_cache(None)
    def solve(slow, fast):
        check_memory()
        healthy = vertices - slow - fast
        s = {w: len(neighbors(w) & slow) for w in healthy}
        f = {w: len(neighbors(w) & fast) for w in healthy}
        s = {w: n for w, n in s.items() if n}
        f = {w: n for w, n in f.items() if n}
        h, b = sum(s.values()), sum(f.values())
        if not h:
            return F(0), F(0), F(0)
        # Failure = (sum f_v failure_after_fast + epsilon *
        #            [number of forbidden slow edges + sum allowed s_v failure])
        #           / (b + epsilon*h).
        a = [F(0), F(0), F(0)]
        for w, n in f.items():
            child = solve(slow, fast | {w})
            for j in range(3):
                a[j] += n * child[j]
        c = [F(sum(n for w, n in s.items() if w not in K)), F(0), F(0)]
        for w, n in s.items():
            if w in K:
                child = solve(slow | {w}, fast)
                for j in range(3):
                    c[j] += n * child[j]
        if not b:
            return tuple(x / h for x in c)
        answer = []
        for j in range(3):
            numerator = a[j] + (c[j - 1] if j else 0)
            if j:
                numerator -= h * answer[j - 1]
            answer.append(numerator / b)
        return tuple(answer)

    coefficients = solve(frozenset({ORIGIN}), frozenset({SEED}))
    assert coefficients[:2] == (0, 0)
    return coefficients


def main():
    limits()
    started = time.monotonic()
    assert len(G) == 16
    connectivity = connectivity_audit()
    rates = [F(1), F(3, 2), F(2), F(3), F(5), F(10), F(100)]
    values = {}
    max_states = 0
    print("Cluster confinement: tested region K has 4 vertices; graph G has 16")
    for r in sorted(set(rates + [1/r for r in rates])):
        q, n = backward(r)
        qf, nf = forward(r)
        assert q == qf
        assert n == nf
        assert 0 < q < 1
        values[r] = q
        max_states = max(max_states, n)
    coefficients = expansion()
    rows = []
    for r in rates:
        upper = 1 - values[r] - values[1/r]
        assert 0 < upper < 1
        print(f"r={str(r):>4}: upper_ceil={upper_decimal(upper)}; "
              f"q(r)={float(values[r]):.12f}; q(1/r)={float(values[1/r]):.12f}")
        rows.append({"r": str(r), "q_r": rational(values[r]),
                     "q_reciprocal": rational(values[1/r]),
                     "coexistence_upper": rational(upper)})
    print(f"Evaluated states: {max_states}")
    print(f"Failure coefficients in epsilon=1/r: {coefficients}")
    # The elementary global bound uses at most 14 births and slow hazards <=3,6.
    quadratic_constant = math_comb(14, 2) * 3 * 6
    print(f"Elementary bound: P(coexistence) <= {quadratic_constant}/r^2")
    result = {
        "K": sorted(K), "G": G,
        "meaning": "q_G,K(r) lower-bounds finite total tested growth in the full lattice",
        "states_evaluated": max_states,
        "rows": rows,
        "failure_series_coefficients": [str(x) for x in coefficients],
        "elementary_quadratic_constant": quadratic_constant,
        "audit": {"backward_equals_forward_all_rates": True,
                  "connected_complements_checked": connectivity,
                  "elapsed_seconds": time.monotonic() - started,
                  "peak_rss_platform_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
    }
    Path("cluster_data.json").write_text(json.dumps(result, indent=2) + "\n")
    print("All exact forward/backward and connectivity checks passed.")
    print(f"Peak RSS: {result['audit']['peak_rss_platform_units']} platform units")
    print(f"Elapsed seconds: {time.monotonic() - started:.3f}")


def math_comb(n, k):
    # Independent integer arithmetic for the single binomial coefficient used.
    assert k == 2
    return n * (n - 1) // 2


if __name__ == "__main__":
    main()
