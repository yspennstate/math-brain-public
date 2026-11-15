"""Exhaustive weighted enumeration of ordered pairs in S_n, 2 <= n <= 5.

Run with all BLAS thread variables set to 1, under nice -n 15.
Permutations are zero-based image tuples; compose(p,q) means p after q.
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


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def cycle_type(p):
    unseen = set(range(len(p)))
    sizes = []
    while unseen:
        j = min(unseen)
        size = 0
        while j in unseen:
            unseen.remove(j)
            size += 1
            j = p[j]
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def sign(p):
    return (-1) ** (len(p) - len(cycle_type(p)))


def subgroup(s, t):
    identity = tuple(range(len(s)))
    group = [identity]
    seen = {identity}
    # Positive generators suffice in a finite group.
    for h in group:
        for g in (s, t):
            hg = compose(h, g)
            if hg not in seen:
                seen.add(hg)
                group.append(hg)
    return group


def regular_adjacency(group, s, t):
    index = {h: i for i, h in enumerate(group)}
    a = np.zeros((len(group), len(group)), dtype=np.int64)
    for i, h in enumerate(group):
        for g in (s, inverse(s), t, inverse(t)):
            a[i, index[compose(h, g)]] += 1
    assert np.array_equal(a, a.T)
    assert np.all(a.sum(axis=1) == 4)
    return a


def natural_adjacency(s, t, signed=False):
    a = np.zeros((len(s), len(s)), dtype=np.int64)
    for g in (s, inverse(s), t, inverse(t)):
        for i, j in enumerate(g):
            a[i, j] += sign(g) if signed else 1
    assert np.array_equal(a, a.T)
    return a


def standard_top(a):
    # Constant vectors have a known eigenvalue, also for the sign twist.
    values = list(np.linalg.eigvalsh(a.astype(float) / 4))
    constant_value = float(a[0].sum()) / 4
    at = min(range(len(values)), key=lambda i: abs(values[i] - constant_value))
    assert abs(values[at] - constant_value) < 1e-10
    del values[at]
    return max(values)


def main():
    start = time.monotonic()
    rows = []
    summaries = []
    witness_candidates = []
    for n in range(2, 6):
        permutations = list(itertools.permutations(range(n)))
        classes = Counter(cycle_type(p) for p in permutations)
        representatives = {}
        for p in permutations:
            representatives.setdefault(cycle_type(p), p)
        nrows = []
        for kind, s in representatives.items():
            for t in permutations:
                group = subgroup(s, t)
                order = len(group)
                family = ("S" if order == math.factorial(n) else
                          "A" if order == math.factorial(n) // 2 and
                          sign(s) == sign(t) == 1 else "other")
                gap = natural_gap = low_gap = None
                min_eigenvalue = 1.0
                if order > 1:
                    a = regular_adjacency(group, s, t)
                    values = np.linalg.eigvalsh(a.astype(float) / 4)
                    assert abs(values[-1] - 1) < 1e-10
                    assert values[-2] < 1 - 1e-8
                    assert abs(values.sum() - np.trace(a) / 4) < 1e-9
                    gap = 1 - float(values[-2])
                    min_eigenvalue = float(values[0])
                    if family in ("S", "A"):
                        top = standard_top(natural_adjacency(s, t))
                        natural_gap = 1 - top
                        low_top = top
                        if family == "S":
                            low_top = max(low_top, (sign(s) + sign(t)) / 2)
                            # At n=2, sign tensor standard is the trivial rep.
                            if n >= 3:
                                low_top = max(low_top, standard_top(
                                    natural_adjacency(s, t, True)))
                        low_gap = 1 - low_top
                        assert natural_gap + 1e-9 >= gap
                        assert low_gap + 1e-9 >= gap
                        if natural_gap - gap > 1e-8:
                            witness_candidates.append({
                                "n": n, "sigma": list(s), "tau": list(t),
                                "order": order, "family": family,
                                "gap": gap, "natural_gap": natural_gap,
                                "low_gap": low_gap,
                                "ratio": natural_gap / gap})
                    if sign(s) == sign(t) == -1:
                        assert abs(min_eigenvalue + 1) < 1e-10
                row = dict(n=n, sigma=" ".join(map(str, s)), tau=" ".join(map(str, t)),
                           weight=classes[kind], order=order, family=family,
                           gap=gap, natural_gap=natural_gap, low_gap=low_gap,
                           min_eigenvalue=min_eigenvalue)
                rows.append(row)
                nrows.append(row)
        assert sum(r["weight"] for r in nrows) == math.factorial(n) ** 2
        counts = Counter()
        for r in nrows:
            counts[r["order"]] += r["weight"]
        summary = {"n": n, "weighted_pairs": math.factorial(n) ** 2,
                   "representative_pairs": len(nrows),
                   "group_order_counts": dict(sorted(counts.items())), "families": {}}
        for family in ("A", "S", "other"):
            selected = [r for r in nrows if r["family"] == family and r["gap"] is not None]
            if not selected:
                continue
            worst = min(selected, key=lambda r: r["gap"])
            item = {"pairs": sum(r["weight"] for r in selected),
                    "min_gap": worst["gap"], "sigma": worst["sigma"], "tau": worst["tau"]}
            if family != "other":
                item["natural_misses"] = sum(r["weight"] for r in selected
                                              if r["natural_gap"] - r["gap"] > 1e-8)
                item["low_misses"] = sum(r["weight"] for r in selected
                                          if r["low_gap"] - r["gap"] > 1e-8)
            summary["families"][family] = item
        summaries.append(summary)
        print(json.dumps(summary, sort_keys=True), flush=True)
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1_000_000_000
        assert time.monotonic() - start < 1100
    with (ROOT / "pairs.csv").open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    witnesses = {}
    for n in range(2, 6):
        candidates = [w for w in witness_candidates if w["n"] == n]
        if candidates:
            witnesses[str(n)] = max(candidates, key=lambda w: w["ratio"])
    result = {"convention": "four-term multiset; one-sided normalized gap; zero-based images",
              "summaries": summaries, "max_ratio_witnesses": witnesses,
              "elapsed_seconds": time.monotonic() - start,
              "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "nice": os.getpriority(os.PRIO_PROCESS, 0)}
    (ROOT / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print("WITNESSES", json.dumps(witnesses, sort_keys=True), flush=True)
    print("elapsed_seconds", result["elapsed_seconds"], "peak_rss_bytes",
          result["peak_rss_bytes"], "nice", result["nice"], flush=True)


if __name__ == "__main__":
    main()
