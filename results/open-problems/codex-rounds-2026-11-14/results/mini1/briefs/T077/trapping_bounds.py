#!/usr/bin/env python3
"""Exact local trapping certificates for adjacent seeds in Z^2 (stdlib only)."""

import itertools
import json
import math
import os
import resource
import signal
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path


def limits():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, priority
    # Bound the whole run, including audit computations.
    signal.alarm(900)
    resource.setrlimit(resource.RLIMIT_CPU, (600, 610))
    # macOS refuses a small address-space limit even for a small resident Python
    # process. Bound this finite enumeration by graph size and check peak RSS.
    print(f"Process nice level: {priority}")
    check_memory()


def check_memory():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else peak * 1024
    if peak_bytes > 512 * 1024 * 1024:
        raise MemoryError("512 MiB guard exceeded")


def box(a, b):
    return tuple((x, y) for x in range(-a, a + 1)
                 for y in range(-b, b + 1) if (x, y) != (0, 0))


TARGETS = frozenset({(1, 0), (-1, 0), (0, 1), (0, -1)})
SEED = (1, 0)


def backward(vertices, rate):
    """Bit-mask dynamic program: success before any birth from the origin."""
    index = {v: i for i, v in enumerate(vertices)}
    adj = [sum(1 << j for j, w in enumerate(vertices)
               if abs(v[0] - w[0]) + abs(v[1] - w[1]) == 1)
           for v in vertices]
    target = sum(1 << index[v] for v in TARGETS)

    @lru_cache(None)
    def solve(mask):
        check_memory()
        k = (target & ~mask).bit_count()
        if not k:
            return F(1)
        transitions = [(i, (adj[i] & mask).bit_count())
                       for i in range(len(vertices)) if not (mask >> i) & 1]
        transitions = [(i, m) for i, m in transitions if m]
        boundary = sum(m for _, m in transitions)
        assert boundary > 0
        return sum((rate * m * solve(mask | (1 << i))
                    for i, m in transitions), F(0)) / (rate * boundary + k)

    result = solve(1 << index[SEED])
    return result, solve.cache_info().currsize


def forward(vertices, rate):
    """Independent set-state implementation, propagating mass from small sets."""
    vertices = frozenset(vertices)
    layer = {frozenset({SEED}): F(1)}
    success, failure, states = F(0), F(0), 0
    while layer:
        next_layer = defaultdict(F)
        for infected, mass in layer.items():
            check_memory()
            states += 1
            missing = TARGETS - infected
            if not missing:
                success += mass
                continue
            # Count directed infected-to-uninfected edges directly by coordinate
            # shifts, rather than using the backward program's adjacency masks.
            counts = Counter()
            for x, y in infected:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    w = (x + dx, y + dy)
                    if w in vertices and w not in infected:
                        counts[w] += 1
            total = rate * sum(counts.values()) + len(missing)
            assert total > 0
            failure += mass * len(missing) / total
            for w, count in counts.items():
                next_layer[infected | {w}] += mass * rate * count / total
        layer = next_layer
    assert success + failure == 1
    return success, states


def cycle_histogram():
    """All 128 choices of left/right front on the punctured 3-by-3 box."""
    histogram = Counter()
    # Cyclic coordinates: (1,0),(1,1),(0,1),(-1,1),(-1,0),
    # (-1,-1),(0,-1),(1,-1). Targets other than the seed are 2,4,6.
    for bits in itertools.product((0, 1), repeat=7):
        infected, left, right = {0}, 0, 0
        counts = [0, 0, 0, 0]
        for side in bits:
            k = len({2, 4, 6} - infected)
            counts[k] += 1
            if side:
                right += 1
                infected.add(right % 8)
            else:
                left += 1
                infected.add((-left) % 8)
        assert len(infected) == 8
        histogram[tuple(counts[1:])] += 1
    assert sum(histogram.values()) == 128
    return histogram


def from_histogram(histogram, rate):
    total = F(0)
    for counts, multiplicity in histogram.items():
        term = F(multiplicity, 128)
        for k, exponent in enumerate(counts, 1):
            term *= (2 * rate / (2 * rate + k)) ** exponent
        total += term
    return total


def moments(vertices):
    """First two moments of sum of target hitting times at competitor rate 1."""
    vertices = frozenset(vertices)

    @lru_cache(None)
    def solve(infected):
        k = len(TARGETS - infected)
        if not k:
            return F(0), F(0)
        counts = Counter()
        for w in vertices - infected:
            for v in infected:
                if abs(w[0] - v[0]) + abs(w[1] - v[1]) == 1:
                    counts[w] += 1
        b = sum(counts.values())
        ea = eb = F(0)
        for w, multiplicity in counts.items():
            a, second = solve(infected | {w})
            ea += F(multiplicity, b) * a
            eb += F(multiplicity, b) * second
        first = F(k, b) + ea
        second = F(2 * k * k, b * b) + F(2 * k, b) * ea + eb
        return first, second

    return solve(frozenset({SEED}))


def gamma_min_mean(k):
    """Integral of P(Gamma(k,1)>t) P(Gamma(8-k,1)>t)."""
    return sum((F(math.comb(i + j, i), 2 ** (i + j + 1))
                for i in range(k) for j in range(8 - k)), F(0))


def rational(x):
    return {"exact": str(x), "decimal": float(x)}


def upper_decimal(x, digits=12):
    """A certified upper decimal, avoiding downward floating-point rounding."""
    scale = 10 ** digits
    rounded = (x.numerator * scale + x.denominator - 1) // x.denominator
    assert F(rounded, scale) >= x
    assert F(rounded - 1, scale) < x
    return f"{rounded // scale}.{rounded % scale:0{digits}d}"


def main():
    limits()
    started = time.monotonic()
    histogram = cycle_histogram()
    cycle_first = sum((F(m, 128) * sum(k * n for k, n in enumerate(ns, 1)) / 2
                       for ns, m in histogram.items()), F(0))
    cycle_second = sum((F(m, 128) *
                        (F(sum(k * n for k, n in enumerate(ns, 1)), 2) ** 2
                         + F(sum(k * k * n for k, n in enumerate(ns, 1)), 4))
                        for ns, m in histogram.items()), F(0))
    gamma_first = sum((gamma_min_mean(k) for k in (2, 4, 6)), F(0))
    assert cycle_first == gamma_first
    rates = [F(1), F(3, 2), F(2), F(3), F(5), F(10), F(100)]
    all_rates = sorted(set(rates + [1 / r for r in rates]))
    results = {
        "model": "Z^2, seeds (0,0) at rate 1 and (1,0) at rate r",
        "meaning": "q_G(r) is a certified lower bound for the origin staying singleton",
        "cycle_histogram_columns": ["n1", "n2", "n3", "multiplicity_out_of_128"],
        "cycle_histogram": [list(ns) + [m] for ns, m in sorted(histogram.items())],
        "cycle_moments_independent": {
            "front_mean": str(cycle_first), "gamma_mean": str(gamma_first),
            "front_second": str(cycle_second)},
        "graphs": {},
    }
    previous = {}
    print("Exact trapping bounds; r = competitor rate / tested-seed rate")
    for name, a, b in (("3x3", 1, 1), ("5x3", 2, 1)):
        vertices = box(a, b)
        assert len(vertices) <= 14
        assert TARGETS <= set(vertices)
        values, max_states = {}, 0
        for r in all_rates:
            q, n = backward(vertices, r)
            q_forward, nf = forward(vertices, r)
            assert q == q_forward
            assert n == nf
            assert 0 < q < 1
            if name == "3x3":
                assert q == from_histogram(histogram, r)
            if previous:
                assert q >= previous[r]
            values[r] = q
            max_states = max(max_states, n)
        mean, second = moments(vertices)
        if name == "3x3":
            assert mean == cycle_first
            assert second == cycle_second
        for r, q in values.items():
            assert q >= 1 - mean / r
            assert q <= 1 - mean / r + second / (2 * r * r)
        assert all(values[x] < values[y] for x, y in zip(all_rates, all_rates[1:]))
        rows = []
        print(f"{name}: vertices={len(vertices)}, evaluated states={max_states}")
        print(f"  area mean={mean}; area second moment={second}")
        for r in rates:
            upper = 1 - values[r] - values[1 / r]
            assert 0 < upper < 1
            rows.append({"r": str(r), "q_r": rational(values[r]),
                         "q_reciprocal": rational(values[1 / r]),
                         "coexistence_upper": rational(upper)})
            print(f"  r={str(r):>4}: upper_ceil={upper_decimal(upper)}; "
                  f"q(r)={float(values[r]):.12f}; q(1/r)={float(values[1/r]):.12f}")
        print(f"  exact upper at r=2: {1 - values[F(2)] - values[F(1, 2)]}")
        results["graphs"][name] = {
            "vertices": vertices, "edges": sum(
                abs(v[0] - w[0]) + abs(v[1] - w[1]) == 1
                for i, v in enumerate(vertices) for w in vertices[i + 1:]),
            "states_evaluated": max_states,
            "area_mean": rational(mean), "area_second_moment": rational(second),
            "rows": rows,
        }
        previous = values
    elapsed = time.monotonic() - started
    results["verification"] = {
        "backward_equals_forward_all_rates": True,
        "cycle_front_enumeration_agrees": True,
        "cycle_gamma_mean_agrees": True,
        "larger_graph_improves_all_rates": True,
        "laplace_taylor_bounds_all_rates": True,
        "elapsed_seconds": elapsed,
        "maxrss_platform_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    Path("trapping_data.json").write_text(json.dumps(results, indent=2) + "\n")
    print("All exact independent checks passed.")
    print(f"Peak RSS: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} platform units")
    print(f"Elapsed seconds: {elapsed:.3f}")
    print("Data: trapping_data.json")


if __name__ == "__main__":
    main()
