"""Finite checks for the proven Hamming-band FEI theorem.

These checks audit algebra and boundary cases; they do not establish novelty
or the unrestricted FEI conjecture. All random draws have a fixed seed.
"""

import json
import math
from pathlib import Path

import numpy as np


RNG = np.random.default_rng(20261002)
MAX_ERRORS = {}
COUNTS = {"one_layer": 0, "monotone_four_bit": 0, "random_band": 0,
          "random_weighted_ltf": 0, "perturbation": 0, "band_eigenvalue": 0}
MAX_RATIOS = {}


def update_error(name, error):
    MAX_ERRORS[name] = max(MAX_ERRORS.get(name, 0.0), float(abs(error)))


def record_ratio(name, value):
    MAX_RATIOS[name] = max(MAX_RATIOS.get(name, 0.0), float(value))


def cube(n):
    indices = np.arange(1 << n, dtype=np.uint32)
    r = np.array([int(x).bit_count() for x in indices])
    x = 2 * ((indices[:, None] >> np.arange(n)) & 1).astype(int) - 1
    return indices, r, x


def fwht(f):
    a = np.array(f, dtype=float, copy=True)
    m = 1
    while m < len(a):
        blocks = a.reshape(-1, 2 * m)
        left = blocks[:, :m].copy()
        right = blocks[:, m:].copy()
        blocks[:, :m] = left + right
        blocks[:, m:] = left - right
        m *= 2
    return a / len(a)


def entropy(p):
    p = np.asarray(p)
    positive = p > 0
    return float(-np.sum(p[positive] * np.log2(p[positive])))


def H(f):
    return entropy(fwht(f) ** 2)


def I(f, n):
    indices = np.arange(1 << n)
    return sum(float(np.mean((f - f[indices ^ (1 << j)]) ** 2)) / 4
               for j in range(n))


def h2(t):
    if t == 0 or t == 1:
        return 0.0
    return -t * math.log2(t) - (1 - t) * math.log2(1 - t)


def check_perturbation(f, g, n):
    delta = float(np.mean(f != g))
    lhs = H(f)
    rhs = 2 * H(g) + 8 * delta * n
    if delta:
        mass = 1 + 4 * delta
        rhs += 2 * mass * h2(4 * delta / mass)
        pooled = (fwht(g) ** 2 + fwht(f - g) ** 2) / mass
        assert np.all(fwht(f) ** 2 <= 2 * mass * pooled + 1e-12)
        assert lhs <= 2 * mass * entropy(pooled) + 1e-10
    assert lhs <= rhs + 1e-10
    assert lhs <= 2 * H(g) + 32 * delta * n + 1e-10
    COUNTS["perturbation"] += 1


def check_band(f, n, a, b, label):
    indices, r, _ = cube(n)
    f = np.array(f, dtype=float)
    assert np.all(f[r < a] == -1)
    assert np.all(f[r > b] == 1)
    assert all(np.all(f[indices] <= f[indices | (1 << j)]) for j in range(n))
    k = b - a + 1
    assert k >= 1
    q = np.array([np.mean(f[r == s] == 1) for s in range(n + 1)])
    mu = np.diff(np.r_[0.0, q, 1.0])
    assert np.min(mu) >= -1e-14
    assert abs(sum(mu) - 1) < 1e-12
    inf = I(f, n)
    ent = H(f)
    expected_inf = expected_delta = expected_energy = expected_var = 0.0
    gmeans = []
    distances = []
    thresholds = []
    for t, weight in zip(range(-1, n + 1), mu):
        g = np.where(r > t, 1.0, -1.0)
        thresholds.append(g)
        delta = float(np.mean(f != g))
        distances.append(delta)
        gmeans.append(float(np.mean(g)))
        expected_inf += weight * I(g, n)
        expected_delta += weight * delta
        expected_energy += weight * I(f - g, n)
        expected_var += weight * np.var(f - g)
        if weight > 0:
            assert np.all((f - g)[(r < a) | (r > b)] == 0)
            check_perturbation(f, g, n)
    D = np.array([[np.mean(g != h) for h in thresholds] for g in thresholds])
    pair_distance = float(mu @ D @ mu)
    pair_square = float(mu @ (D ** 2) @ mu)
    update_error("random_threshold_influence", expected_inf - inf)
    update_error("random_threshold_disagreement", expected_delta - pair_distance)
    update_error("averaged_variance_identity", expected_var - (4 * expected_delta - 2 * pair_square))
    assert expected_energy <= 4 * inf + 1e-11
    assert expected_var >= 2 * expected_delta - 1e-11
    assert n * expected_delta <= 2 * (k + 1) ** 2 * inf + 1e-11
    assert ent <= (25 + 64 * (k + 1) ** 2) * inf + 1e-11
    if inf:
        record_ratio(label + "_H_over_I", ent / inf)
        record_ratio(label + "_n_mean_delta_over_I", n * expected_delta / inf)
    return q, inf


# Exhaust every assignment on one exceptional layer for n <= 5.
for n in range(1, 6):
    _, r, _ = cube(n)
    for layer in range(n + 1):
        positions = np.flatnonzero(r == layer)
        for assignment in range(1 << len(positions)):
            f = np.where(r > layer, 1.0, -1.0)
            f[positions] = [1 if assignment >> j & 1 else -1
                            for j in range(len(positions))]
            q, inf = check_band(f, n, layer, layer, "one_layer")
            fraction = float(q[layer])
            p = len(positions) / (1 << n)
            update_error("one_layer_exact_influence", inf - 2 * p *
                         (layer * fraction + (n - layer) * (1 - fraction)))
            g = np.where(r >= layer if fraction > .5 else r > layer, 1.0, -1.0)
            delta = np.mean(f != g)
            assert n * delta <= inf / 2 + 1e-12
            assert I(g, n) <= 2 * inf + 1e-12
            assert H(f) <= 62 * inf + 1e-12
            COUNTS["one_layer"] += 1


# Exhaust all 4-bit truth tables and retain every monotone one.
n = 4
indices, r, _ = cube(n)
for table in range(1 << (1 << n)):
    f = np.array([1 if table >> j & 1 else -1 for j in indices], dtype=float)
    if not all(np.all(f <= f[indices | (1 << j)]) for j in range(n)):
        continue
    a = int(np.min(r[f == 1])) if np.any(f == 1) else n
    b = int(np.max(r[f == -1])) if np.any(f == -1) else 0
    if a > b:
        a = b = max(0, min(n, a))
    check_band(f, n, a, b, "four_bit")
    COUNTS["monotone_four_bit"] += 1


# Explicit band-restricted adjacency matrices, including k=1 and small n.
for n in range(1, 151):
    for k in range(1, min(n + 1, 15) + 1):
        for a in sorted(set([0, max(0, (n - k + 1) // 2), n - k + 1])):
            B = np.zeros((k, k))
            for j in range(k - 1):
                rr = a + j
                B[j, j + 1] = B[j + 1, j] = math.sqrt((n - rr) * (rr + 1))
            eig = float(np.linalg.eigvalsh(B)[-1])
            upper = (n + 1) * math.cos(math.pi / (k + 1))
            assert eig <= upper + 1e-10
            if n >= (k + 1) ** 2:
                assert (n - eig) / 2 >= n / (2 * (k + 1) ** 2) - 1e-10
            COUNTS["band_eigenvalue"] += 1


# Monotone DNF truncated to bands, including bands far into the tails.
for n in [6, 8, 10, 12]:
    indices, r, x = cube(n)
    for repetition in range(24):
        k = 1 + repetition % 4
        a = int(RNG.integers(0, n - k + 2))
        b = a + k - 1
        h = np.zeros(len(r), dtype=bool)
        for _ in range(4):
            mask = int(RNG.integers(1, 1 << n))
            h |= (indices & mask) == mask
        f = np.where((r > b) | ((r >= a) & h), 1.0, -1.0)
        check_band(f, n, a, b, "random_band")
        COUNTS["random_band"] += 1


# Weighted thresholds with L1 deviations fixed and arbitrary bias.
for n in [4, 6, 8, 10, 12, 14]:
    _, r, x = cube(n)
    for amplitude in [.4, 1.0, 1.8, 2.7]:
        for repetition in range(4):
            u = RNG.normal(size=n)
            u *= amplitude / np.sum(abs(u))
            if np.min(1 + u) <= 0:
                continue
            theta = float(RNG.uniform(-n - amplitude, n + amplitude))
            w = 1 + u
            f = np.where(x @ w >= theta, 1.0, -1.0)
            possible = np.flatnonzero(abs(2 * np.arange(n + 1) - n - theta) <= amplitude + 1e-12)
            if len(possible):
                a, b = int(possible[0]), int(possible[-1])
                assert b - a + 1 <= math.floor(amplitude + 1e-12) + 1
                check_band(f, n, a, b, "weighted_ltf")
            else:
                assert all(np.all(f[r == s] == f[r == s][0]) for s in range(n + 1))
                assert H(f) <= 12.04 * I(f, n) + 1e-12
            COUNTS["random_weighted_ltf"] += 1


# The entropy comparison has no monotonicity requirement.
for n in range(1, 11):
    for _ in range(100):
        f = RNG.choice([-1.0, 1.0], size=1 << n)
        g = f.copy()
        disagreements = RNG.random(1 << n) < float(RNG.random())
        g[disagreements] *= -1
        check_perturbation(f, g, n)


report = {"status": "all assertions passed", "seed": 20261002,
          "counts": COUNTS, "maximum_identity_errors": MAX_ERRORS,
          "maximum_observed_ratios": MAX_RATIOS,
          "scope": "finite algebra checks; restricted theorem only; no novelty certification"}
out = Path(__file__).with_name("hamming_band_verification.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
