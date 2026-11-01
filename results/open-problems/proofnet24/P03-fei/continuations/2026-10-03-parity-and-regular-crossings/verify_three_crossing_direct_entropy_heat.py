#!/usr/bin/env python3
"""Independent exact checks of direct three-crossing route checkpoints.

No research helper imports.  Huge tiny-noise cubes are checked by exact
score-grid certificates, NOT enumerated. Entropies/logarithms are labeled
numeric separately from rational/integer counting assertions.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, log2
import json
from pathlib import Path
import random


def fwht(values):
    a = list(values)
    width = 1
    while width < len(a):
        for j in range(0, len(a), 2 * width):
            for k in range(j, j + width):
                left, right = a[k], a[k + width]
                a[k], a[k + width] = left + right, left - right
        width *= 2
    return a


def entropy_num(walsh, size):
    return sum(-(v / size) ** 2 * log2((v / size) ** 2)
               for v in walsh if v)


counts = dict(exhaustive_tree_functions=0, extra_lacunary_functions=0,
              exact_tree_covariance_checks=0, exact_local_split_checks=0,
              full_retention_grids=0, dyadic_error_certificates=0,
              direct_majority_coefficients=0, halfspace_budget_truth_tables=0,
              halfspace_budget_vertices=0)
tree_examples = []


@lru_cache(None)
def tree_metrics(n, mask):
    size = 1 << n
    values = tuple(1 if (mask >> v) & 1 else -1 for v in range(size))
    walsh = fwht(values)
    assert sum(v * v for v in walsh) == size * size
    boundary = sum(values[v] != values[v | (1 << i)]
                   for i in range(n) for v in range(size) if not v & (1 << i))
    influence = F(2 * boundary, size)
    mean = F(sum(values), size)
    variance = 1 - mean * mean
    entropy = entropy_num(walsh, size)
    nonconstant = mask not in (0, (1 << size) - 1)
    if not nonconstant:
        return (influence, mean, variance, entropy, 0, F(0), (0,) * n)
    half = size // 2
    lower_mask = mask & ((1 << half) - 1)
    upper_mask = mask >> half
    left = tree_metrics(n - 1, lower_mask)
    right = tree_metrics(n - 1, upper_mask)
    left_nonconstant = left[2] > 0
    right_nonconstant = right[2] > 0
    branch = left_nonconstant and right_nonconstant
    budget = max(left[4], right[4]) + int(branch)
    alpha = F(sum(values[v] != values[v + half] for v in range(half)), half)
    assert influence == alpha + (left[0] + right[0]) / 2
    cov = F(sum(values[v] * values[v + half] for v in range(half)), half) - left[1] * right[1]
    tree_cov = cov + (left[5] + right[5]) / 2
    assert tree_cov <= budget * variance
    reads = tuple(left[6][j] + right[6][j] for j in range(n - 1)) + (1,)
    changes = sum(values[v] != values[v + 1] for v in range(size - 1))
    assert budget <= changes - 1
    assert max(reads) <= changes
    increment = entropy - (left[3] + right[3]) / 2
    assert increment <= 4 * float(influence) + 5e-12
    if not branch:
        assert increment <= 8 * float(alpha) + 5e-12
    assert entropy <= (8 + 4 * budget) * float(influence) + 5e-12
    prior_constant = 4 * log2(3) + 2 + 2 * budget * log2(3)
    assert entropy <= prior_constant * float(influence) + 5e-12
    assert entropy <= (4 * changes + 4) * float(influence) + 5e-12
    counts['exact_tree_covariance_checks'] += 1
    counts['exact_local_split_checks'] += 1
    return influence, mean, variance, entropy, budget, tree_cov, reads


for n in range(5):
    for mask in range(1 << (1 << n)):
        tree_metrics(n, mask)
        counts['exhaustive_tree_functions'] += 1

rng = random.Random(101732)
for n in range(5, 11):
    size = 1 << n
    for m in range(1, 6):
        for _ in range(10):
            cuts = sorted(rng.sample(range(1, size), m))
            values = [1 if sum(v >= cut for cut in cuts) % 2 == 0 else -1
                      for v in range(size)]
            mask = sum(1 << v for v, value in enumerate(values) if value == 1)
            metrics = tree_metrics(n, mask)
            assert metrics[4] <= m - 1
            assert max(metrics[6]) <= m
            counts['extra_lacunary_functions'] += 1
            if m == 3:
                tree_examples.append(dict(n=n, cuts=cuts, branching_budget=metrics[4],
                                          influence=str(metrics[0]), entropy_numeric=metrics[3]))

# Exact rational grids witnessing every component in BOTH pivot branches.
grid_examples = []
for n in range(3, 104, 2):
    w = n + 1
    k = 2 * n ** 6
    small = F(3 * w, k)
    assert w > 1 > small > 0
    cuts = (-w, 2, w)
    step = 2 * small
    assert step < 1
    assert cuts[1] - cuts[0] <= 2 * w
    assert cuts[2] - cuts[1] <= 2 * w
    for z in (-1, 1):
        origin = F(w * z - n - 3 * w)
        targets = (origin, F(cuts[0] + cuts[1], 2),
                   F(cuts[1] + cuts[2], 2), origin + step * k)
        witnesses = []
        for component, target in enumerate(targets):
            quotient = (target - origin) / step
            r = min(k, max(0, quotient.numerator // quotient.denominator))
            score = origin + step * r
            if component == 0:
                assert score < cuts[0]
            elif component == 3:
                assert score > cuts[2]
            else:
                assert cuts[component - 1] < score < cuts[component]
            # Every score has odd numerator over denominator n^6.
            numerator = (w * z - n) * n ** 6 + 3 * w * (r - n ** 6)
            assert numerator % 2
            assert score == F(numerator, n ** 6)
            witnesses.append(dict(component=component, positive_tiny_coordinates=r,
                                  score=str(score)))
        counts['full_retention_grids'] += 1
        if n in (3, 15, 51, 103):
            grid_examples.append(dict(N=n, pivot=z, total_tiny_coordinates=k,
                                      witnesses=witnesses))
    if n >= 15:
        b = n ** 4 // 72
        d = n ** 4 // 36
        dimension = n + k + 1
        assert b >= 3 * n * n
        assert d >= 6 * n * n
        assert d >= 2 * b
        assert dimension + b <= 3 * n ** 6
        assert 3 * n ** 6 <= 1 << (2 + 6 * n)
        assert 3 * n * n >= 8 * n + 5
        # 2*omega/eps <= 2^(N+3-B)*(M+B) <= eps, EXACTLY.
        assert dimension + b <= 1 << (b - 2 * n - 3)
        # 2*d_tail/eps <= 2^(N+2-D) <= eps.
        assert d >= 2 * n + 2
        counts['dyadic_error_certificates'] += 1

# Independently reconstruct predecessor majority coefficients from truth
# values, then compare the rational level formula in the analytic proof.
for n in range(3, 16, 2):
    d = (n - 1) // 2
    values = [1 if 2 * v.bit_count() > n else -1 for v in range(1 << n)]
    transform = fwht(values)
    for mask, coefficient in enumerate(transform):
        degree = mask.bit_count()
        physical = F(coefficient * (-1) ** degree, 1 << n)
        if degree % 2 == 0:
            expected = F(0)
        else:
            ell = (degree - 1) // 2
            expected = (-1) ** ell * F(comb(2 * d, d), 4 ** d) * F(comb(d, ell), comb(2 * d, 2 * ell))
        assert physical == expected
        counts['direct_majority_coefficients'] += 1

# A three-crossing point-hole witness to unbounded signed-halfspace budget.
halfspace_examples = []
for n in range(2, 14, 2):
    a = 2 * n + 4
    scale = 1 << n
    weights = [scale + (1 << (n - i)) for i in range(1, n + 1)]
    fine_v = (1 << (n // 2)) - 1
    t_int = sum(weights[i] * (1 if fine_v >> i & 1 else -1) for i in range(n))
    cuts_int = (0, a * scale + t_int - 1, a * scale + t_int + 1)
    values, thresholds = [], [[], [], []]
    for vertex in range(1 << (n + 2)):
        xmask = vertex & (scale - 1)
        y1 = 1 if vertex >> n & 1 else -1
        y2 = 1 if vertex >> (n + 1) & 1 else -1
        score = a * scale * y1 + 2 * a * scale * y2
        score += sum(weights[i] * (1 if xmask >> i & 1 else -1) for i in range(n))
        assert score not in cuts_int
        hs = [1 if score > cut else -1 for cut in cuts_int]
        for j in range(3):
            thresholds[j].append(hs[j])
        f = hs[0] - hs[1] + hs[2]
        expected = y2 - 2 * int(y1 == -1 and y2 == 1 and xmask == fine_v)
        assert f in (-1, 1) and f == expected
        values.append(f)
    def influence(vals):
        dim = n + 2
        return F(2 * sum(vals[v] != vals[v | (1 << i)]
                         for i in range(dim) for v in range(len(vals)) if not v & (1 << i)), len(vals))
    actual = influence(values)
    budget = sum(map(influence, thresholds))
    majority = F(n * comb(n, n // 2), scale)
    assert actual == 1 + F(n, 2 * scale)
    assert budget == 3 + majority / 2
    walsh = fwht(values)
    point_denominator = 1 << (n + 2)
    physical_pivot_mask = 1 << (n + 1)
    assert abs(walsh[physical_pivot_mask]) == point_denominator - 2
    assert all(abs(v) == 2 for j, v in enumerate(walsh) if j != physical_pivot_mask)
    entropy = entropy_num(walsh, len(values))
    assert entropy <= 2 * float(actual) + 1e-12
    halfspace_examples.append(dict(N=n, influence=str(actual), threshold_budget=str(budget),
                                   budget_ratio=str(budget / actual), entropy_numeric=entropy))
    counts['halfspace_budget_truth_tables'] += 1
    counts['halfspace_budget_vertices'] += len(values)

report = dict(status='PASS', counts=counts,
              exact_checks=['tree influence recursion', 'tree covariance <= b*variance',
                            'lexicographic crossing descent and read count',
                            'both-branch rational score-grid component witnesses',
                            'endpoint numerator parity',
                            'all N tested explicit dyadic continuity bounds',
                            'majority coefficient formula via direct integer Walsh transform',
                            'three-crossing halfspace-budget influence/spectrum formulas'],
              numeric_supplements=['tree entropy/local split inequalities',
                                   'point-hole entropy bound'],
              grid_examples=grid_examples, tree_three_crossing_examples=tree_examples,
              halfspace_budget_examples=halfspace_examples,
              limitations='No huge tiny-coordinate truth cube enumeration; analytic proof establishes infinite families. Lacunary qualitative FEI already known; full nearby-three-crossing FEI open.')
path = Path(__file__).with_name('three_crossing_direct_entropy_heat_checks.json')
path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(dict(status=report['status'], counts=counts), indent=2))
