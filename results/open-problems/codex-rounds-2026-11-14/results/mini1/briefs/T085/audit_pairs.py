"""Independent full enumeration: no imports from enumerate_pairs.py.

Use a full multiplication table, left multiplication and a shifted Laplacian.
Compare complete eight-decimal gap histograms and representation-miss counts.
"""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
            "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[key] = "1"

import csv
import itertools
import json
import math
import resource
import time
from collections import Counter
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent


def direct(n):
    ps = list(itertools.permutations(range(n)))
    ix = {p: i for i, p in enumerate(ps)}
    m = len(ps)
    # table[a,b] is a after b, generated without the primary composition helper.
    table = np.array([[ix[tuple(a[j] for j in b)] for b in ps] for a in ps])
    inv = [int(np.flatnonzero(table[i] == 0)[0]) for i in range(m)]
    signs = [(-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
             for p in ps]
    hist = Counter()
    counts = Counter()
    miss = Counter()
    minima = {}
    for s in range(m):
        for t in range(m):
            gs = [s, inv[s], t, inv[t]]
            visited = {0}
            frontier = {0}
            while frontier:
                new = {int(table[g, h]) for g in gs for h in frontier} - visited
                visited.update(new)
                frontier = new
            h = sorted(visited)
            size = len(h)
            counts[size] += 1
            if size == 1:
                hist[(size, None)] += 1
                continue
            lookup = {v: i for i, v in enumerate(h)}
            laplacian = np.eye(size) + np.full((size, size), 2 / size)
            for g in gs:
                for i, v in enumerate(h):
                    laplacian[i, lookup[int(table[g, v])]] -= 0.25
            gap = float(np.linalg.eigh(laplacian)[0][0])
            assert gap > 0
            hist[(size, round(gap, 8))] += 1
            fam = ("S" if size == m else "A" if size == m // 2 and
                   signs[s] == signs[t] == 1 else "other")
            minima[fam] = min(minima.get(fam, 10), gap)
            if fam in ("S", "A"):
                nat = np.eye(n) + np.full((n, n), 2 / n)
                for g in gs:
                    for i in range(n):
                        nat[i, ps[g][i]] -= 0.25
                nat_gap = float(np.linalg.eigh(nat)[0][0])
                low_gap = nat_gap
                if fam == "S":
                    low_gap = min(low_gap, 1 - (signs[s] + signs[t]) / 2)
                    if n >= 3:
                        c = (signs[s] + signs[t]) / 2
                        signed = np.eye(n) + np.full((n, n), (1+c) / n)
                        for g in gs:
                            for i in range(n):
                                signed[i, ps[g][i]] -= signs[g] * 0.25
                        low_gap = min(low_gap, float(np.linalg.eigh(signed)[0][0]))
                if nat_gap > gap + 1e-8:
                    miss[fam + "_natural"] += 1
                if low_gap > gap + 1e-8:
                    miss[fam + "_low"] += 1
    return hist, counts, miss, minima


def main():
    start = time.monotonic()
    primary = list(csv.DictReader((ROOT / "pairs.csv").open()))
    output = []
    for n in range(2, 6):
        expected = Counter()
        expected_counts = Counter()
        expected_miss = Counter()
        selected = [r for r in primary if int(r["n"]) == n]
        for r in selected:
            w, size = int(r["weight"]), int(r["order"])
            gap = float(r["gap"]) if r["gap"] else None
            expected[size, round(gap, 8) if gap is not None else None] += w
            expected_counts[size] += w
            if r["natural_gap"] and float(r["natural_gap"]) > gap + 1e-8:
                expected_miss[r["family"] + "_natural"] += w
            if r["low_gap"] and float(r["low_gap"]) > gap + 1e-8:
                expected_miss[r["family"] + "_low"] += w
        hist, counts, miss, minima = direct(n)
        assert sum(hist.values()) == math.factorial(n) ** 2
        assert counts == expected_counts, (n, counts, expected_counts)
        assert hist == expected, (n, hist - expected, expected - hist)
        assert miss == expected_miss, (n, miss, expected_miss)
        item = {"n": n, "all_pairs": sum(hist.values()), "histogram_matches": True,
                "counts_match": True, "miss_counts_match": True,
                "independent_minima": minima, "miss_counts": dict(miss)}
        output.append(item)
        print(json.dumps(item, sort_keys=True), flush=True)
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1_000_000_000
        assert time.monotonic() - start < 1100
    result = {"checks": output, "elapsed_seconds": time.monotonic() - start,
              "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "nice": os.getpriority(os.PRIO_PROCESS, 0)}
    (ROOT / "audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print("elapsed_seconds", result["elapsed_seconds"], "peak_rss_bytes",
          result["peak_rss_bytes"], "nice", result["nice"])


if __name__ == "__main__":
    main()
