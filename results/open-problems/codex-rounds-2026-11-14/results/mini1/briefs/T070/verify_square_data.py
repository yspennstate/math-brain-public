#!/usr/bin/env python3
"""Data-only audit: independent CDF comparisons, symmetries, and a hand case."""
import os
os.environ["OMP_NUM_THREADS"] = "1"
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
data = json.loads(Path(__file__).with_name("square_data.json").read_text())
laws = {int(m): list(map(F, v["probabilities"]))
        for m, v in data["laws"].items()}
assert set(laws) == set(range(256))
audits = {a["mask"]: a for a in data["independent_audits"]}
assert set(audits) == set(range(256))
for m, law in laws.items():
    assert sum(law) == 1 and min(law) >= 0
    pi = list(map(F, audits[m]["stable_configuration_law"]))
    assert len(pi) == 16 and sum(pi) == 1 and min(pi) >= 0
    count_law = [sum((pi[s] for s in range(16) if s.bit_count() == k), F(0))
                 for k in range(5)]
    assert count_law == law == list(map(F, audits[m]["clock_fraction_law"]))
    by_cdf = [1-sum(law[:k], F(0)) for k in range(1, 5)]
    assert by_cdf == list(map(F, data["laws"][str(m)]["tails"]))
    assert sum(by_cdf, F(0)) == sum((k*v for k, v in enumerate(law)), F(0))
    assert sum(by_cdf, F(0)) == F(data["laws"][str(m)]["mean"])

comparisons = 0
zero = 0
positive = []
for a, b in product(range(256), repeat=2):
    # Test all covering relations independently of the original bit loop.
    if (a & b) != a or (a ^ b).bit_count() != 1:
        continue
    comparisons += 1
    for k in range(1, 5):
        gap = sum(laws[b][:k], F(0)) - sum(laws[a][:k], F(0))
        assert gap >= 0, (a, b, k, gap)
        zero += (gap == 0)
        if gap > 0:
            positive.append((gap, a, b, k))
assert comparisons == data["comparisons"] == 1024
assert zero == len(data["zero_tail_gaps"])

points = [tuple(p) for p in data["vertices"]]
edges = [tuple(e) for e in data["directed_edges"]]
symmetry_checks = 0
for swap, flipx, flipy in product((False, True), repeat=3):
    perm = []
    for x, y in points:
        if swap:
            x, y = y, x
        if flipx:
            x = 1-x
        if flipy:
            y = 1-y
        perm.append(points.index((x, y)))
    for m in range(256):
        transformed = 0
        for bit, (i, j) in enumerate(edges):
            if m & (1 << bit):
                transformed |= 1 << edges.index((perm[i], perm[j]))
        assert laws[m] == laws[transformed]
        symmetry_checks += 1

# A reciprocal two-site component with jump probabilities 1/4 to its
# neighbor, 3/4 to the sink, and lambda=1. Derived in PROOF.md.
pair = [F(99, 427), F(216, 427), F(112, 427)]
two_pairs = [sum((pair[i]*pair[j] for i in range(3) for j in range(3)
                  if i+j == k), F(0)) for k in range(5)]
cut_vertical = sum(1 << bit for bit, (i, j) in enumerate(edges)
                   if points[i][1] != points[j][1])
assert cut_vertical == 90
assert laws[90] == two_pairs
assert laws[255] == [F(1,16), F(1,4), F(3,8), F(1,4), F(1,16)]

print("256 laws agree with independent clock/Fraction calculations")
print("1024 comparisons; 4096 tail inequalities;", zero,
      "zero gaps;", len(positive), "positive gaps")
print("minimum positive gap and (uncut mask, cut mask, threshold):",
      min(positive))
print("dihedral symmetry checks:", symmetry_checks)
print("two-site law:", list(map(str, pair)))
print("two independent rows (mask 90):", list(map(str, two_pairs)))
assert all(sum(laws[90][:k], F(0))-sum(laws[0][:k], F(0)) > 0
           for k in range(1, 5))
print("square versus two rows tail gaps:",
      [str(sum(laws[90][:k], F(0))-sum(laws[0][:k], F(0)))
       for k in range(1, 5)])
print("baseline stationary density:", F(data["laws"]["0"]["mean"])/4)
print("PASS")
