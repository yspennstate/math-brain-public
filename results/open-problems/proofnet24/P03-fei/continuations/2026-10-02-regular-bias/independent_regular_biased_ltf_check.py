"""Independent finite checks of the regular-LTF known-results corollary.

Truth values and unnormalized Walsh coefficients are integers. Identities are
checked using integers/Fractions. Entropy and theorem inequalities use ordinary
floating point as sanity checks, not proof certificates for the theorem.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb, e, exp, log, log2, sqrt
from pathlib import Path
import json
import random


def transform(a):
    a = list(a)
    width = 1
    while width < len(a):
        for left in range(0, len(a), 2 * width):
            for i in range(left, left + width):
                u, v = a[i], a[i + width]
                a[i], a[i + width] = u + v, u - v
        width *= 2
    return a


report = {
    'scope': 'Finite independent checks, not a proof or novelty certificate',
    'exact_integer_and_fraction_identities': True,
    'threshold_cases': 0,
    'constant_cases': 0,
    'noise_cases': 0,
    'invariance_cases': 0,
    'max_entropy_over_p_sqrt_nL': 0.0,
    'min_indicator_W1_over_p_squared_L': None,
    'max_Imax_over_p_min_one_tau_sqrt_L': 0.0,
    'by_dimension': {},
}
A = 20.5 * sqrt(2) / (1 - exp(-1))
constants = {
    'A': A,
    'within_level': 4 * A / log(2),
    'binary_degree': 4 / log(2) * (sqrt(log(2)) + 1 / sqrt(log(2))),
    'conditional_positive_degree': 8 / (e * log(2) * sqrt(log(2))),
}
constants['total'] = sum(v for k, v in constants.items() if k != 'A')
assert constants['total'] < 283
report['analytic_constants'] = constants


def check(weights, boundary, all_noise=False):
    n = len(weights)
    N = 1 << n
    scores = [sum(w * (2 * ((x >> i) & 1) - 1)
                  for i, w in enumerate(weights)) for x in range(N)]
    f = [1 if s > boundary else -1 for s in scores]
    plus = f.count(1)
    if plus in (0, N):
        assert transform(f)[1:] == [0] * (N - 1)
        report['constant_cases'] += 1
        return
    p = F(min(plus, N - plus), N)
    L = log(1 / float(p))
    coeff = transform(f)
    squared = [x * x for x in coeff]
    assert sum(squared) == N * N
    degree_mass = [sum(squared[s] for s in range(N) if s.bit_count() == k)
                   for k in range(n + 1)]
    q = F(sum(squared[1:]), N * N)
    assert q == 4 * p * (1 - p)
    physical = [F(sum(f[x] != f[x ^ (1 << i)] for x in range(N)), N)
                for i in range(n)]
    I = sum(physical)
    assert I == F(sum(k * mass for k, mass in enumerate(degree_mass)), N * N)
    h = [(v + 1) // 2 for v in f]
    hc = transform(h)
    # Standard Walsh index convention has x_i=-1 at bit 0, hence the minus.
    assert all(-F(hc[1 << i], N) == physical[i] / 2 for i in range(n))
    W1 = F(sum(hc[1 << i] ** 2 for i in range(n)), N * N)
    assert 4 * W1 == sum(v * v for v in physical)
    assert I >= 4 * W1 / max(physical)
    H = sum(F(v, N * N) * log2((N * N) / v) for v in squared if v)
    degree_H = sum(F(v, N * N) * log2((N * N) / v) for v in degree_mass if v)
    level_bound = sum(F(degree_mass[k], N * N) * log2(comb(n, k))
                      for k in range(1, n + 1))
    assert H <= degree_H + level_bound + 1e-10
    assert H <= 300 * float(p) * sqrt(n * L) + 1e-10
    report['max_entropy_over_p_sqrt_nL'] = max(
        report['max_entropy_over_p_sqrt_nL'], H / (float(p) * sqrt(n * L)))
    w1_ratio = float(W1) / (float(p) ** 2 * L)
    old = report['min_indicator_W1_over_p_squared_L']
    report['min_indicator_W1_over_p_squared_L'] = w1_ratio if old is None else min(old, w1_ratio)
    tau = max(abs(w) for w in weights) / sqrt(sum(w * w for w in weights))
    report['max_Imax_over_p_min_one_tau_sqrt_L'] = max(
        report['max_Imax_over_p_min_one_tau_sqrt_L'],
        float(max(physical)) / (float(p) * min(1, tau * sqrt(L))))
    # Tail estimates at real t, with exact rational spectral probabilities.
    for t in (F(1, 2), F(1), F(3, 2), F(n, 2), F(2*n-1, 2)):
        tail = F(sum(m for k, m in enumerate(degree_mass) if k > t), N * N)
        assert float(tail) <= A * float(p) * sqrt(L / float(t)) + 1e-12
    if all_noise or report['threshold_cases'] % 100 == 0:
        for epsilon in (F(1, 2), F(1, 4), F(1, 8), F(1, 16), F(1, 1024)):
            ns = sum(F(m, 2 * N * N) * (1 - (1 - 2 * epsilon) ** k)
                     for k, m in enumerate(degree_mass))
            assert ns <= 2 * p
            assert float(ns) <= 20.5 * float(p) * sqrt(float(epsilon) * L) + 1e-12
            report['noise_cases'] += 1
    if report['threshold_cases'] % 100 == 0:
        flip_mask = N // 3
        changed = [-f[x ^ flip_mask] for x in range(N)]
        assert [v*v for v in transform(changed)] == squared
        assert all(F(sum(changed[x] != changed[x ^ (1 << i)] for x in range(N)), N)
                   == physical[i] for i in range(n))
        report['invariance_cases'] += 1
    report['threshold_cases'] += 1
    report['by_dimension'][str(n)] = report['by_dimension'].get(str(n), 0) + 1


# Exhaustive sorted integer weight vectors (zeros included), every threshold
# behavior, through dimension 6. Coordinate permutations add no new behavior.
for n in range(1, 7):
    for weights in combinations_with_replacement(range(4), n):
        if not any(weights):
            continue
        scores = sorted(set(sum(w * (2 * ((x >> i) & 1) - 1)
                                for i, w in enumerate(weights)) for x in range(1 << n)))
        for boundary in [scores[0] - 1] + scores:
            check(weights, boundary, all_noise=n <= 3)


# Larger dimensions: rare events, irregular weights, zeros, and intermediate
# biases. Integer score thresholds avoid numerical ambiguity at cube ties.
rng = random.Random(314159)
for n in (7, 8, 10, 12):
    families = [tuple([1] * n), tuple(range(1, n + 1)),
                tuple(1 << i for i in range(n)),
                tuple([1000] + [1] * (n - 1)),
                tuple([0] * (n // 2) + [1] * (n - n // 2)),
                tuple(rng.randrange(0, 8) for _ in range(n))]
    for weights in families:
        scores = sorted(set(sum(w * (2 * ((x >> i) & 1) - 1)
                                for i, w in enumerate(weights)) for x in range(1 << n)))
        chosen = {0, 1, len(scores) // 2, len(scores)-2, len(scores)-1}
        chosen.update(rng.randrange(len(scores)) for _ in range(12))
        check(weights, scores[0] - 1)
        for j in sorted(chosen):
            if 0 <= j < len(scores):
                check(weights, scores[j], all_noise=True)


# Deterministic nearuniform vector checks, including negative, zero, and almost
# cancelled coefficients and both sides of the n >= 4A^2 case division.
report['nearuniform_checks'] = 0
for n in (1, 2, 3, 4, 10, 100, 1000):
    vectors = [[F(0)] * n, [F(-1)] * n,
               [F(-999,1000)] * n, [F(-2)] + [F(0)] * (n - 1),
               [F((i % 7) - 3, 10) for i in range(n)]]
    for u in vectors:
        w = [1 + v for v in u]
        if not any(w):
            continue
        bound_A = sqrt(float(sum(v*v for v in u)))
        tau_root_n = float(max(abs(v) for v in w)) * sqrt(n / float(sum(v*v for v in w)))
        assert tau_root_n <= 2 * (1 + bound_A) + 1e-12
        report['nearuniform_checks'] += 1

report['status'] = 'PASS'
out = Path(__file__).with_name('independent_regular_biased_ltf_checks.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
