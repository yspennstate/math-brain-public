#!/usr/bin/env python3
"""Independent insertion integrals and global quadratic certificate."""

import json
import resource
import time
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

from cluster_bounds import G, K, ORIGIN, SEED, neighbors
from trapping_bounds import check_memory, limits, rational, upper_decimal


V = frozenset(G)


def closure_failure(slow, fast):
    """Zero-order failure after unrestricted fast growth, then slow-only growth."""
    reached = set(fast)
    while True:
        new = reached | set.union(*(neighbors(v) for v in reached))
        new &= V - slow
        if new == reached:
            break
        reached = new
    return F(bool(V - slow - reached - K))


@lru_cache(None)
def backward_insertions(slow, fast):
    """Two positive integrals: all second births, and zero-order failure ones."""
    check_memory()
    healthy = V - slow - fast
    fast_rates = {w: len(neighbors(w) & fast) for w in healthy}
    slow_rates = {w: len(neighbors(w) & slow) for w in healthy}
    b = sum(fast_rates.values())
    h = sum(slow_rates.values())
    if not h:
        return F(0), F(0)
    assert b > 0  # complements after zero or one slow births are connected
    total, leading = F(0), F(0)
    for w, m in fast_rates.items():
        if m:
            x, y = backward_insertions(slow, fast | {w})
            total += m * x
            leading += m * y
    for w, m in slow_rates.items():
        if not m:
            continue
        if len(slow) == 1:
            assert w in K
            x, y = backward_insertions(slow | {w}, fast)
            total += m * x
            leading += m * y
        else:
            assert len(slow) == 2
            total += m
            leading += m * (1 if w not in K else closure_failure(slow | {w}, fast))
    return total / b, leading / b


def forward_insertions():
    """Propagate occupation weights, not probabilities, with at most one insertion."""
    layer = {(frozenset({ORIGIN}), frozenset({SEED})): F(1)}
    total, leading = F(0), F(0)
    while layer:
        nxt = defaultdict(F)
        for (slow, fast), weight in layer.items():
            check_memory()
            healthy = V - slow - fast
            s, f = Counter(), Counter()
            for v in slow:
                for w in neighbors(v):
                    if w in healthy:
                        s[w] += 1
            if not s:
                continue
            for v in fast:
                for w in neighbors(v):
                    if w in healthy:
                        f[w] += 1
            b = sum(f.values())
            assert b
            for w, m in f.items():
                nxt[(slow, fast | {w})] += weight * F(m, b)
            for w, m in s.items():
                insertion_weight = weight * F(m, b)
                if len(slow) == 1:
                    assert w in K
                    nxt[(slow | {w}, fast)] += insertion_weight
                else:
                    total += insertion_weight
                    # Recompute connectivity independently as a simple stack walk.
                    if w not in K:
                        leading += insertion_weight
                    else:
                        deleted = slow | {w}
                        reached = set(fast)
                        stack = list(fast)
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                z = (x + dx, y + dy)
                                if z in V and z not in deleted and z not in reached:
                                    reached.add(z)
                                    stack.append(z)
                        if any(z not in reached and z not in deleted for z in V - K):
                            leading += insertion_weight
        layer = nxt
    return total, leading


def main():
    limits()
    started = time.monotonic()
    backward = backward_insertions(frozenset({ORIGIN}), frozenset({SEED}))
    forward = forward_insertions()
    assert backward == forward
    quadratic, leading = backward
    cluster = json.loads(Path("cluster_data.json").read_text())
    assert str(leading) == cluster["failure_series_coefficients"][2]
    assert 0 < leading < quadratic < 1638
    for row in cluster["rows"]:
        r = F(row["r"])
        failure = 1 - F(row["q_r"]["exact"])
        assert failure <= quadratic / (r * r)
    print(f"Global quadratic constant B = {quadratic} = {float(quadratic):.12f}")
    print(f"Certified upper decimal for B: {upper_decimal(quadratic)}")
    print(f"Leading failure coefficient L = {leading} = {float(leading):.12f}")
    print("B and L independently agree between backward and forward insertion integrals.")
    print("L also agrees with the separate exact rational-series recurrence.")
    print("All stored rate values satisfy failure <= B/r^2.")
    print(f"Backward insertion states: {backward_insertions.cache_info().currsize}")
    result = {
        "global_quadratic_constant": rational(quadratic),
        "asymptotic_failure_coefficient": rational(leading),
        "independent_backward_forward_agree": True,
        "series_recurrence_agrees": True,
        "all_stored_rates_obey_global_bound": True,
        "backward_states": backward_insertions.cache_info().currsize,
        "elapsed_seconds": time.monotonic() - started,
        "peak_rss_platform_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    Path("audit_data.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"Elapsed seconds: {time.monotonic() - started:.3f}")
    print(f"Peak RSS: {result['peak_rss_platform_units']} platform units")


if __name__ == "__main__":
    main()
