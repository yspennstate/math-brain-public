#!/usr/bin/env python3
"""Exact four-variable DNF/Fourier catalog; Python standard library only."""

import csv
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
from collections import Counter
from functools import lru_cache


N = 4
POINTS = 1 << N
FUNCTIONS = 1 << POINTS
FULL = FUNCTIONS - 1
DENOMINATOR = POINTS * POINTS
ROOT = Path(__file__).resolve().parent


def guard():
    if os.environ.get("OMP_NUM_THREADS") != "1":
        raise RuntimeError("Launch with OMP_NUM_THREADS=1")
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 15:
        raise RuntimeError(f"Actual nice {priority} is below 15")
    # No numerical packages, workers, or subprocesses are used.
    # The catalog needs only a few MB. Bound data allocation and wall time.
    old_soft, old_hard = resource.getrlimit(resource.RLIMIT_DATA)
    try:
        resource.setrlimit(resource.RLIMIT_DATA, (min(old_soft, 128 * 1024**2), old_hard))
        print("data_limit_bytes=" + str(resource.getrlimit(resource.RLIMIT_DATA)[0]), flush=True)
    except (ValueError, OSError) as error:
        # Some macOS sandbox profiles reject setrlimit even for a lower soft limit.
        # Fixed arrays have 65,536 entries; the per-function cache is discarded.
        print(f"OS data limit unavailable: {error}; using small fixed arrays and RSS checks", flush=True)
    signal.signal(signal.SIGALRM, lambda *_: sys.exit("20-minute wall limit"))
    signal.alarm(20 * 60)
    print(f"actual_nice={priority}; OMP_NUM_THREADS=1; wall_limit_seconds=1200", flush=True)


def peak_mb():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return rss / (1024**2 if sys.platform == "darwin" else 1024)


def make_cubes():
    """Trit -1 is free; 0/1 requires that value of an assignment bit."""
    cubes = []
    patterns = list(itertools.product((-1, 0, 1), repeat=N))
    lookup = {}
    for pattern in patterns:
        mask = sum(
            1 << a
            for a in range(POINTS)
            if all(v == -1 or ((a >> i) & 1) == v for i, v in enumerate(pattern))
        )
        lookup[pattern] = mask
        cubes.append(mask)
    parents = {}
    for pattern, mask in lookup.items():
        parents[mask] = [
            lookup[pattern[:i] + (-1,) + pattern[i + 1 :]]
            for i, v in enumerate(pattern)
            if v != -1
        ]

    # Independent cube construction by intersecting literal truth sets.
    second = set()
    for fixed in range(1 << N):
        value = fixed
        while True:
            mask = FULL
            for i in range(N):
                if (fixed >> i) & 1:
                    literal = sum(1 << a for a in range(POINTS) if (a >> i) & 1)
                    mask &= literal if (value >> i) & 1 else FULL ^ literal
            second.add(mask)
            if value == 0:
                break
            value = (value - 1) & fixed
    assert set(cubes) == second
    assert len(set(cubes)) == 3**N == 81
    return cubes, lookup, parents


def union_distances(cubes):
    """Shortest path from the empty truth set by OR-ing one cube per edge."""
    distance = [POINTS + 1] * FUNCTIONS
    predecessor = [None] * FUNCTIONS
    distance[0] = 0
    for mask in range(FUNCTIONS):
        candidate = distance[mask] + 1
        for cube in cubes:
            joined = mask | cube
            if candidate < distance[joined]:
                distance[joined] = candidate
                predecessor[joined] = (mask, cube)
    assert max(distance) == 8
    return distance, predecessor


def cover_distance(mask, cubes, parents):
    """Independent fixed-on-set minimum cover, permitting overlapping cubes."""
    if not mask:
        return 0
    # A nonmaximal cube can be expanded without covering a false point.
    prime = [
        c for c in cubes
        if c & mask == c and not any(p & mask == p for p in parents[c])
    ]
    options = [tuple(c for c in prime if (c >> a) & 1) for a in range(POINTS)]

    @lru_cache(None)
    def cover(uncovered):
        if not uncovered:
            return 0
        a = (uncovered & -uncovered).bit_length() - 1
        return 1 + min(cover(uncovered & ~c) for c in options[a])

    return cover(mask)


def walsh(mask):
    values = [1 if (mask >> a) & 1 else -1 for a in range(POINTS)]
    out = values[:]
    step = 1
    while step < POINTS:
        for start in range(0, POINTS, step * 2):
            for j in range(start, start + step):
                u, v = out[j], out[j + step]
                out[j], out[j + step] = u + v, u - v
        step *= 2
    # The transform uses (-1)^(a.S), while x_i=+1 for a_i=1.
    # Multiplying by (-1)^|S| converts to chi_S(x).
    return [v * (-1 if s.bit_count() % 2 else 1) for s, v in enumerate(out)]


def direct_fourier(mask, character_masks):
    # If P is the set chi_S=+1, then sum f*chi_S
    # = 4|F intersect P| - 2|F| - 2|P| + 16.
    return [
        4 * (mask & positive).bit_count()
        - 2 * mask.bit_count() - 2 * positive.bit_count() + POINTS
        for positive in character_masks
    ]


def dnf_witness(mask, predecessor, inverse):
    result = []
    while mask:
        before, cube = predecessor[mask]
        result.append(list(inverse[cube]))
        mask = before
    return result


def main():
    guard()
    started = time.monotonic()
    cubes, lookup, parents = make_cubes()
    inverse = {mask: pattern for pattern, mask in lookup.items()}
    distance, predecessor = union_distances(cubes)
    print(f"cubes={len(cubes)}; union_DP_complete; max_minimum_terms={max(distance)}", flush=True)
    character_masks = [
        sum(
            1 << a for a in range(POINTS)
            if sum(1 for i in range(N) if (s >> i) & 1 and not (a >> i) & 1) % 2 == 0
        )
        for s in range(POINTS)
    ]
    # exact_tail[t][m] is the worst numerator among functions requiring exactly t terms.
    exact_tail = [[-1] * (POINTS + 1) for _ in range(9)]
    exact_witness = [[None] * (POINTS + 1) for _ in range(9)]
    histogram = Counter()
    spectrum_histogram = Counter()
    with (ROOT / "functions.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["truth_mask_hex", "minimum_terms"] + [f"fourier_numerator_{s:04b}" for s in range(POINTS)])
        for mask in range(FUNCTIONS):
            t = distance[mask]
            second = cover_distance(mask, cubes, parents)
            assert t == second, (mask, t, second)
            coeffs = walsh(mask)
            assert coeffs == direct_fourier(mask, character_masks), mask
            squares = sorted((c * c for c in coeffs), reverse=True)
            assert sum(squares) == DENOMINATOR, mask
            histogram[t] += 1
            spectrum_histogram[tuple(squares)] += 1
            writer.writerow([f"{mask:04x}", t] + coeffs)
            tail = DENOMINATOR
            for m in range(POINTS + 1):
                if tail > exact_tail[t][m]:
                    exact_tail[t][m] = tail
                    exact_witness[t][m] = mask
                if m < POINTS:
                    tail -= squares[m]
            if mask and mask % 16384 == 0:
                assert peak_mb() < 512, "RSS exceeds the conservative 512 MiB guard"
                print(f"checked_functions={mask}; peak_RSS_MiB={peak_mb():.2f}", flush=True)

    envelope = []
    with (ROOT / "tail_envelope.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["term_budget", "retained", "worst_tail_numerator", "denominator", "witness_truth_mask_hex", "witness_minimum_terms", "witness_terms_json"])
        for t in range(9):
            tails = []
            for m in range(POINTS + 1):
                d = max(range(t + 1), key=lambda j: exact_tail[j][m])
                tail = exact_tail[d][m]
                mask = exact_witness[d][m]
                terms = dnf_witness(mask, predecessor, inverse)
                union = 0
                for pattern in terms:
                    union |= lookup[tuple(pattern)]
                assert union == mask and len(terms) == distance[mask]
                assert tail == DENOMINATOR - sum(sorted((c*c for c in walsh(mask)), reverse=True)[:m])
                writer.writerow([t, m, tail, DENOMINATOR, f"{mask:04x}", distance[mask], json.dumps(terms)])
                tails.append(tail)
            assert all(tails[m] >= tails[m + 1] for m in range(POINTS))
            envelope.append(tails)

    # Full exact spectral types, with multiplicity, as a second compact view.
    with (ROOT / "spectral_types.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["multiplicity"] + [f"sorted_square_numerator_{i}" for i in range(POINTS)])
        for squares, count in sorted(spectrum_histogram.items()):
            writer.writerow([count] + list(squares))
    assert sum(histogram.values()) == FUNCTIONS
    assert sum(spectrum_histogram.values()) == FUNCTIONS
    sampled = {}
    for t in range(2, 9):
        sampled[t] = {}
        for denominator in (2, 4, 8, 16, 32, 64, 128, 256):
            # All comparisons exact: tail/256 <= 1/denominator.
            sampled[t][f"1/{denominator}"] = next(m for m, tail in enumerate(envelope[t]) if tail * denominator <= DENOMINATOR)
    hashes = {}
    for filename in ("functions.csv", "tail_envelope.csv", "spectral_types.csv"):
        hashes[filename] = hashlib.sha256((ROOT / filename).read_bytes()).hexdigest()
    summary = {
        "n": N,
        "functions": FUNCTIONS,
        "consistent_terms": len(cubes),
        "fourier_denominator": POINTS,
        "weight_denominator": DENOMINATOR,
        "minimum_terms_histogram": dict(sorted(histogram.items())),
        "number_of_sorted_squared_spectral_types": len(spectrum_histogram),
        "minimum_sparsity_worst_case": sampled,
        "at_most_term_budget_tail_numerators": envelope,
        "independent_minimum_cover_checks": FUNCTIONS,
        "independent_fourier_checks": FUNCTIONS,
        "parseval_checks": FUNCTIONS,
        "envelope_witness_checks": 9 * 17,
        "actual_nice": os.getpriority(os.PRIO_PROCESS, 0),
        "peak_RSS_MiB": round(peak_mb(), 3),
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "sha256": hashes,
    }
    (ROOT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2), flush=True)
    print("PASS: complete enumeration and both independent audits", flush=True)


if __name__ == "__main__":
    main()
