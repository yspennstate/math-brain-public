"""Independent arithmetic/finite checks for the bounded-path support theorem.

This script has no local imports. Exact integer checks verify physical
influence, upward path depth, and n*min(p,1-p) <= (k+1)^2 I/2. Entropy
and adjacency bounds are additionally checked numerically. Finite checks
do not establish the analytic theorem or research novelty.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


LOGE = math.log2(math.e)
C = 4.0
RNG = np.random.default_rng(2026100209)
COUNTS = dict(exhaustive_families=0, random_structured_families=0,
              explicit_nilpotency=0, adjacency_eigenvalue_checks=0,
              large_n_support_cases=0, large_label_cases=0, k1_cases=0,
              singleton_asymptotic_cases=0, weighted_band_rounding_cases=0)
MAX = dict(entropy_over_I=0.0, entropy_over_path_bound=0.0,
           entropy_over_refined_bound=0.0, energy_over_refined_bound=0.0,
           energy_over_path_bound=0.0, adjacency_over_cosine_bound=0.0)


def integer_fwht_rows(values):
    """Unnormalized exact Walsh transform of all rows."""
    a = np.array(values, dtype=np.int64, copy=True)
    m = a.shape[1]
    width = 1
    while width < m:
        blocks = a.reshape(a.shape[0], -1, 2 * width)
        left = blocks[:, :, :width].copy()
        right = blocks[:, :, width:].copy()
        blocks[:, :, :width] = left + right
        blocks[:, :, width:] = left - right
        width *= 2
    return a


def cube_data(n):
    vertices = np.arange(1 << n, dtype=np.int64)
    ranks = np.array([int(v).bit_count() for v in vertices], dtype=np.int64)
    predecessors = [[v ^ (1 << j) for j in range(n) if v & (1 << j)]
                    for v in range(1 << n)]
    return vertices, ranks, predecessors


def inspect_rows(supports, n, label):
    supports = np.asarray(supports, dtype=bool)
    if supports.ndim == 1:
        supports = supports[None, :]
    rows, m = supports.shape
    assert m == 1 << n
    vertices, ranks, predecessors = cube_data(n)
    size = np.sum(supports, axis=1, dtype=np.int64)
    minority_size = np.minimum(size, m - size)
    depth = np.zeros((rows, m), dtype=np.int64)
    for v in range(m):
        previous = (np.max(depth[:, predecessors[v]], axis=1)
                    if predecessors[v] else np.zeros(rows, dtype=np.int64))
        depth[:, v] = supports[:, v] * (previous + 1)
    k = np.max(depth, axis=1)
    boundary = np.zeros(rows, dtype=np.int64)
    for j in range(n):
        lower = vertices[(vertices & (1 << j)) == 0]
        upper = lower | (1 << j)
        boundary += np.sum(supports[:, lower] != supports[:, upper], axis=1)
    # Physical I = 2*undirected boundary / 2^n. Thus (3) is exactly
    # n*minority_size <= (k+1)^2 * boundary.
    kval = (k + 1) ** 2
    assert np.all(n * minority_size <= kval * boundary)
    nonconstant = (minority_size > 0)
    one_path = (k == 1) & nonconstant
    assert np.all(boundary[one_path] == n * size[one_path])
    COUNTS["k1_cases"] += int(np.count_nonzero(one_path))
    COUNTS["large_label_cases"] += int(np.count_nonzero((size > m / 2) & nonconstant))
    COUNTS["large_n_support_cases"] += int(np.count_nonzero((n >= kval) & nonconstant))
    f = 1 - 2 * supports.astype(np.int64)
    walsh = integer_fwht_rows(f)
    assert np.all(np.sum(walsh ** 2, axis=1) == m * m)
    # Exact Fourier-energy normalization: sum |S| F(S)^2 = m^2 I.
    assert np.all(np.sum(walsh ** 2 * ranks[None, :], axis=1) == 2 * m * boundary)
    spectral = (walsh.astype(float) / m) ** 2
    entropy = np.zeros(rows)
    positive = spectral > 0
    logs = np.zeros_like(spectral)
    logs[positive] = np.log2(spectral[positive])
    entropy = -np.sum(spectral * logs, axis=1)
    inf = 2.0 * boundary / m
    r = minority_size / m
    q = 4 * r * (1 - r)
    binary_entropy = np.zeros(rows)
    inside = (q > 0) & (q < 1)
    binary_entropy[inside] = -q[inside] * np.log2(q[inside]) - (1 - q[inside]) * np.log2(1 - q[inside])
    minor_binary_bound = np.zeros(rows)
    minor_binary_bound[nonconstant] = 4 * r[nonconstant] * np.log2(1 / r[nonconstant])
    assert np.all(binary_entropy <= minor_binary_bound + 3e-11)
    assert np.all(entropy <= 8 * n * r + 3e-11)
    assert np.all(entropy <= C * kval * inf + 3e-11)
    assert np.all(entropy[one_path] <= C * inf[one_path] + 3e-11)
    refined_factor = np.ones(rows)
    refined_factor[nonconstant] = 1 / np.tan(math.pi / (2 * (k[nonconstant] + 1))) ** 2
    assert np.all(entropy <= 4 * refined_factor * inf + 3e-11)
    assert np.all(n * r <= refined_factor * inf / 2 + 3e-11)
    if np.any(nonconstant):
        MAX["entropy_over_I"] = max(MAX["entropy_over_I"],
                                    float(np.max(entropy[nonconstant] / inf[nonconstant])))
        MAX["entropy_over_path_bound"] = max(MAX["entropy_over_path_bound"],
            float(np.max(entropy[nonconstant] / (C * kval[nonconstant] * inf[nonconstant]))))
        MAX["energy_over_path_bound"] = max(MAX["energy_over_path_bound"],
            float(np.max(n * minority_size[nonconstant] / (kval[nonconstant] * boundary[nonconstant]))))
        MAX["entropy_over_refined_bound"] = max(MAX["entropy_over_refined_bound"],
            float(np.max(entropy[nonconstant] / (4 * refined_factor[nonconstant] * inf[nonconstant]))))
        MAX["energy_over_refined_bound"] = max(MAX["energy_over_refined_bound"],
            float(np.max(n * minority_size[nonconstant] / (refined_factor[nonconstant] * boundary[nonconstant]))))
    # Selected explicit matrices independently check the DP/nilpotency bridge.
    choices = list(range(min(rows, 12)))
    if rows > 12:
        choices += RNG.choice(rows, min(12, rows), replace=False).tolist()
    for row in choices:
        if not nonconstant[row]:
            continue
        selected = np.flatnonzero(supports[row]).tolist()
        if len(selected) > 100:
            continue
        pos = {v: j for j, v in enumerate(selected)}
        up = np.zeros((len(selected), len(selected)), dtype=np.int64)
        for v in selected:
            for j in range(n):
                if not v & (1 << j):
                    w = v | (1 << j)
                    if w in pos:
                        up[pos[w], pos[v]] = 1
        assert not np.any(np.linalg.matrix_power(up, int(k[row])))
        assert np.any(np.linalg.matrix_power(up, int(k[row]) - 1))
        COUNTS["explicit_nilpotency"] += 1
        eigen = np.linalg.eigvalsh((up + up.T).astype(float))
        norm = float(np.max(np.abs(eigen)))
        bound = (n + 1) * math.cos(math.pi / (int(k[row]) + 1))
        assert norm <= bound + 3e-11
        if bound > 1e-10:
            MAX["adjacency_over_cosine_bound"] = max(MAX["adjacency_over_cosine_bound"], norm / bound)
        COUNTS["adjacency_eigenvalue_checks"] += 1
    COUNTS[label] += rows


def main():
    dimensions = []
    for n in range(0, 5):
        m = 1 << n
        masks = np.arange(1 << m, dtype=np.uint64)
        supports = ((masks[:, None] >> np.arange(m, dtype=np.uint64)) & 1).astype(bool)
        inspect_rows(supports, n, "exhaustive_families")
        dimensions.append(dict(dimension=n, support_families=len(supports)))
    # Hamming-layer families, random subsets of them, sparse arbitrary
    # families, parity supports, and score-band supports exercise k1,
    # large n >= (k+1)^2, and nonminority label classes separately.
    for n in range(5, 13):
        vertices, ranks, _ = cube_data(n)
        signs = 2 * ((vertices[:, None] >> np.arange(n)) & 1) - 1
        families = []
        families += [(ranks % 2) == parity for parity in (0, 1)]
        for width in range(1, 5):
            lo = max(0, n // 2 - width // 2)
            band = (ranks >= lo) & (ranks < lo + width)
            families.append(band)
            for probability in (0.15, 0.5, 0.9):
                families.append(band & (RNG.random(len(vertices)) < probability))
        for _ in range(12):
            probability = float(RNG.choice([0.02, 0.1, 0.4, 0.6, 0.9]))
            families.append(RNG.random(len(vertices)) < probability)
        # Positive weights [1,2] and short scalar intervals. DP determines
        # the actual path height; the check assumes no unproved score rule.
        for _ in range(8):
            weights = RNG.integers(100, 201, size=n)
            score = signs @ weights
            lo = int(RNG.integers(-200, 201))
            width = int(RNG.integers(1, 601))
            band = (score >= lo) & (score < lo + width)
            families.append(band)
            # Treat the integer attained scores as belonging to the closed
            # interval [lo,lo+width-1], and also arbitrarily remove vertices.
            random_subband = band & (RNG.random(len(vertices)) < 0.7)
            families.append(random_subband)
            for selected_support in (band, random_subband):
                depth = np.zeros(len(vertices), dtype=np.int64)
                for v in range(len(vertices)):
                    previous = [depth[v ^ (1 << j)] for j in range(n) if v & (1 << j)]
                    depth[v] = (1 + max(previous, default=0)) if selected_support[v] else 0
                assert int(np.max(depth)) <= (width - 1) // (2 * int(np.min(weights))) + 1
                COUNTS["weighted_band_rounding_cases"] += 1
        inspect_rows(np.stack(families), n, "random_structured_families")
    singleton_ratios = []
    for n in [1, 2, 3, 4, 8, 16, 32, 64, 128, 256, 512]:
        p = math.ldexp(1.0, -n)
        # log1p avoids losing the empty atom when p is extremely small.
        empty = (1 - 2 * p) ** 2
        empty_entropy = (-empty * 2 * math.log1p(-2 * p) / math.log(2)
                         if n > 1 else 0.0)
        entropy = empty_entropy + 4 * p * (1 - p) * (2 * n - 2)
        ratio = entropy / (2 * n * p)
        assert 0 <= ratio <= 4 + 1e-12
        assert ratio + 1e-12 >= 4 * (1 - p) * (1 - 1 / n)
        singleton_ratios.append(dict(dimension=n, entropy_over_I=ratio))
        COUNTS["singleton_asymptotic_cases"] += 1
    report = dict(status="PASS analytic theorem separately supplied",
                  theorem_constant=C, dimensions=dimensions, counts=COUNTS,
                  singleton_ratios=singleton_ratios,
                  maxima=MAX, entropy_tolerance=3e-11,
                  exact_checks=["physical influence and integer Walsh energy",
                                "longest upward path vertices",
                                "n*minority_size <= (k+1)^2*undirected_boundary",
                                "explicit compressed raising nilpotency on selected families"],
                  refined_theorem="H<=4*cot(pi/(2(k+1)))^2*I",
                  numerical_checks=["Fourier entropy and H<=8*n*minority_probability",
                                    "binary entropy bound h2(4r(1-r))<=4r*log2(1/r)",
                                    "selected adjacency spectral bounds",
                                    "refined cotangent entropy and support energy bounds",
                                    "sharp singleton asymptotic"],
                  scope="Finite validation; no novelty or unrestricted FEI conclusion")
    target = Path(__file__).with_name("bounded_ascending_path_support_checks.json")
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
