"""Independent finite checks for bounded-coordinate gluing and slab centers.

Influences, character permutations and Chow-square bounds use integer truth
tables/Walsh numerators. Entropies are numerical verification only.
"""
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


def walsh(f):
    a = np.array(f, dtype=np.int64).copy()
    for j in range(len(a).bit_length() - 1):
        v = a.reshape(-1, 2 << j)
        left, right = v[:, :1 << j].copy(), v[:, 1 << j:].copy()
        v[:, :1 << j], v[:, 1 << j:] = left + right, left - right
    return a


def H(f):
    a = walsh(f).astype(float) ** 2 / len(f) ** 2
    a = a[a > 0]
    return float(-a @ np.log2(a))


def flip_counts(f):
    idx = np.arange(len(f))
    return [int(np.sum(f != f[idx ^ (1 << j)]))
            for j in range(len(f).bit_length() - 1)]


def h2(p):
    if p == 0 or p == 1:
        return 0.
    return -p * math.log2(p) - (1-p) * math.log2(1-p)


def char(n, T):
    return np.array([(-1) ** ((s & T).bit_count()) for s in range(1 << n)],
                    dtype=np.int64)


def restrictions(f, n, coords):
    other = [i for i in range(n) if i not in coords]
    for fixed in range(1 << len(coords)):
        arr = []
        for free in range(1 << len(other)):
            idx = sum(((fixed >> j) & 1) << i for j, i in enumerate(coords))
            idx |= sum(((free >> j) & 1) << i for j, i in enumerate(other))
            arr.append(f[idx])
        yield np.array(arr, dtype=np.int64)


report = {"status": "passed", "finite_checks_only": True,
          "generic_functions": 0, "generic_pivots": 0,
          "slab_cases": 0, "character_checks": 0, "max_high_count": 0,
          "max_entropy_over_center": 0., "exact_budget_failures": [],
          "local_minimum_probe": []}


# Exhaust every Boolean truth table through four variables.
for n in range(5):
    size = 1 << n
    idx = np.arange(size)
    for mask in range(1 << size):
        f = np.array([1 if (mask >> x) & 1 else -1 for x in range(size)],
                     dtype=np.int64)
        counts = flip_counts(f)
        influence = sum(counts) / size
        minority = min(int(np.sum(f == 1)), int(np.sum(f == -1))) / size
        isoperimetry = 2 * minority * math.log2(1 / minority) if minority else 0.
        assert influence + 1e-12 >= isoperimetry
        for j, count in enumerate(counts):
            alpha = count / size
            assert alpha <= 2 * minority + 1e-12
            assert h2(alpha) <= 2 * influence + 1e-12
            minus, plus = list(restrictions(f, n, [j]))
            delta = H(f) - (H(minus) + H(plus)) / 2
            assert delta <= 2 * h2(alpha) + 1e-12
            assert delta <= 4 * influence + 1e-12
            report["generic_pivots"] += 1
        report["generic_functions"] += 1


rng = np.random.default_rng(20261002)
for n in range(2, 11):
    idx = np.arange(1 << n)
    signs = np.array([[1 if s & (1 << j) else -1 for j in range(n)]
                      for s in idx], dtype=np.int64)
    weight_lists = [np.ones(n, dtype=np.int64)]
    weight_lists += [rng.integers(1, 25, n) for _ in range(35)]
    for weights in weight_lists:
        scores = signs @ weights
        attained = np.unique(scores)
        intervals = [(s, s) for s in attained] if np.all(weights == 1) else []
        for _ in range(12):
            a, b = sorted(rng.choice(attained, 2, replace=True))
            intervals.append((a, b))
        for a, b in intervals:
            f = np.where((scores >= a) & (scores <= b), -1, 1)
            h1, h2cross = np.where(scores >= a, 1, -1), np.where(scores > b, 1, -1)
            counts = flip_counts(f)
            c1, c2 = flip_counts(h1), flip_counts(h2cross)
            assert all(c <= x+y for c, x, y in zip(counts, c1, c2))
            assert sum(c*c for c in c1) <= len(f) ** 2
            assert sum(c*c for c in c2) <= len(f) ** 2
            assert sum(c*c for c in counts) <= 4 * len(f) ** 2
            high = [j for j, c in enumerate(counts) if 2*c > len(f)]
            T = sum(1 << j for j in high)
            assert len(high) <= 15
            centered = f * char(n, T)
            center_num = sum(min(c, len(f)-c) for c in counts)
            assert sum(flip_counts(centered)) == center_num
            assert np.array_equal(walsh(centered), walsh(f)[idx ^ T])
            leaves = list(restrictions(centered, n, high))
            avg_H = sum(H(leaf) for leaf in leaves) / len(leaves)
            avg_I = sum(sum(flip_counts(leaf)) / len(leaf) for leaf in leaves) / len(leaves)
            centered_I = center_num / len(f)
            assert avg_I <= centered_I + 1e-12
            assert H(centered) <= avg_H + 4 * len(high) * centered_I + 1e-11
            if not center_num:
                assert np.count_nonzero(walsh(f)) == 1
            else:
                report["max_entropy_over_center"] = max(
                    report["max_entropy_over_center"], H(f) / centered_I)
            report["max_high_count"] = max(report["max_high_count"], len(high))
            characters = range(1 << n) if n <= 6 else [
                int(rng.integers(0, 1 << n)) for _ in range(4)]
            for U in characters:
                mod = f * char(n, U)
                expected = [len(f)-c if U & (1 << j) else c
                            for j, c in enumerate(counts)]
                assert flip_counts(mod) == expected
                assert sum(expected) >= center_num
                assert np.array_equal(walsh(mod), walsh(f)[idx ^ U])
                report["character_checks"] += 1
            report["slab_cases"] += 1


# Exact failures of a comparison I-Var <= constant * J.
for n in [2, 4]:
    signs = np.array([[1 if s & (1 << j) else -1 for j in range(n)]
                      for s in range(1 << n)])
    f = np.where(signs.sum(axis=1) == 0, -1, 1)
    counts, N = flip_counts(f), len(f)
    I = Fraction(sum(counts), N)
    V = 1 - Fraction(int(f.sum()), N) ** 2
    J = Fraction(sum(min(c, N-c) for c in counts), N)
    report["exact_budget_failures"].append({
        "dimension": n, "influences": [str(Fraction(c, N)) for c in counts],
        "I_minus_V": str(I-V), "center_J": str(J),
        "H_numerical": H(f)})
    if n == 2:
        assert I-V == 1 and J == 0


# Probe a tempting but unneeded local min-influence inequality. All weights
# and truth-table scores are integers; interval endpoints are half-integers.
for N in range(3, 20, 2):
    n, size = N+1, 1 << (N+1)
    idx = np.arange(size, dtype=np.uint64)
    remaining = np.array([2*s.bit_count()-N for s in range(1 << N)], dtype=np.int64)
    fminus = np.where((-N+2*remaining > -N+.5) &
                     (-N+2*remaining < N+.5), -1, 1)
    fplus = np.where((N+2*remaining > -N+.5) &
                    (N+2*remaining < N+.5), -1, 1)
    f = np.concatenate([fminus, fplus])
    alpha = Fraction(int(np.sum(fminus != fplus)), 1 << N)
    assert alpha == 1-Fraction(1, 1 << N)
    delta = H(f) - (H(fminus)+H(fplus))/2
    report["local_minimum_probe"].append({
        "remaining_bits": N, "pivot_weight": N, "remaining_weight": 2,
        "alpha_exact": str(alpha), "delta_H_numerical": delta,
        "delta_over_min_numerical": delta / float(1-alpha)})


out = Path(__file__).with_name("parity_slab_center_heat_checks.json")
out.write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
