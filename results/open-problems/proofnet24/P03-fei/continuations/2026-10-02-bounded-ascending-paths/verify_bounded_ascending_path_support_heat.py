#!/usr/bin/env python3
"""Independent checks of the bounded-upward-path FEI proof.

No imports from the author's checker or any research helper.  Counting
identities are integer-exact; entropy/operator norm checks are separately
labeled floating-point supplements to the written analytic audit.
"""
import json
import math
from pathlib import Path
import random
import numpy as np


def walsh_int(values):
    a = np.array(values, dtype=np.int64)
    step = 1
    while step < len(a):
        blocks = a.reshape(-1, 2 * step)
        left = blocks[:, :step].copy()
        right = blocks[:, step:].copy()
        blocks[:, :step] = left + right
        blocks[:, step:] = left - right
        step *= 2
    return a


stats = dict(supports=0, nonconstant=0, large_dimension=0,
             nonminority_supports=0, k_one=0, not_k_sperner=0,
             matrix_checks=0, dilation_checks=0,
             exact_walsh_checks=0, numeric_entropy_checks=0)
worst_energy_ratio = 0.0
worst_entropy_ratio = 0.0
examples = []


def inspect(e, n, label, matrix=False):
    global worst_energy_ratio, worst_entropy_ratio
    size = 1 << n
    assert len(e) == size
    e = np.asarray(e, dtype=np.int64)
    count = int(e.sum())
    dp = np.zeros(size, dtype=np.int64)
    chain = np.zeros(size, dtype=np.int64)
    k = 0
    # Numeric bitmask order is a topological order for the inclusion DAG.
    # dp uses only adjacent predecessors. chain uses EVERY smaller subset.
    for vertex in range(size):
        if not e[vertex]:
            continue
        pred = [vertex ^ (1 << i) for i in range(n) if vertex >> i & 1]
        dp[vertex] = 1 + max((int(dp[t]) for t in pred), default=0)
        k = max(k, int(dp[vertex]))
        if n <= 8:
            t = (vertex - 1) & vertex
            best = 0
            while t:
                best = max(best, int(chain[t]))
                t = (t - 1) & vertex
            if vertex:
                best = max(best, int(chain[0]))
            chain[vertex] = best + 1
    boundary = 0
    for i in range(n):
        step = 1 << i
        blocks = e.reshape(-1, 2 * step)
        boundary += int(np.count_nonzero(blocks[:, :step] != blocks[:, step:]))
    # Every undirected crossing edge is counted precisely once above.
    f = 1 - 2 * e
    a = walsh_int(f)
    assert int(np.dot(a, a)) == size * size
    energy_num = sum(mask.bit_count() * int(v) ** 2
                     for mask, v in enumerate(a))
    assert energy_num == 2 * boundary * size
    stats['supports'] += 1
    stats['exact_walsh_checks'] += 1
    if 0 < count < size:
        stats['nonconstant'] += 1
        minority = min(count, size - count)
        square = (k + 1) ** 2
        assert n * minority <= square * boundary
        stats['nonminority_supports'] += int(count > size // 2)
        stats['large_dimension'] += int(n >= square)
        if k == 1:
            assert boundary == n * count
            assert n * minority <= boundary
            stats['k_one'] += 1
        if n <= 8 and int(chain.max()) > k:
            stats['not_k_sperner'] += 1
        probs = np.square(a.astype(float) / size)
        positive = probs[probs > 0]
        entropy = float(-np.dot(positive, np.log2(positive)))
        influence = 2 * boundary / size
        # Root's subsequently derived sharper minority entropy estimate.
        constant = 4
        # Independent supplement: root's dimension-free cotangent refinement.
        refined_constant = 4 / math.tan(math.pi / (2 * (k + 1))) ** 2
        target = refined_constant * influence
        assert entropy <= target + 1e-10
        r = minority / size
        assert entropy <= 8 * n * r + 1e-10
        q = 4 * r * (1 - r)
        binary_entropy = (0 if q in (0, 1) else
                          -q * math.log2(q) - (1 - q) * math.log2(1 - q))
        assert binary_entropy <= 4 * r * math.log2(1 / r) + 1e-10
        worst_energy_ratio = max(worst_energy_ratio, n * minority / (square * boundary))
        worst_entropy_ratio = max(worst_entropy_ratio, entropy / target)
        stats['numeric_entropy_checks'] += 1
        if matrix:
            support = [v for v in range(size) if e[v]]
            pos = {v: i for i, v in enumerate(support)}
            u = np.zeros((len(support), len(support)), dtype=np.int64)
            for v in support:
                for i in range(n):
                    if not (v >> i & 1):
                        above = v | (1 << i)
                        if above in pos:
                            u[pos[above], pos[v]] = 1
            power = np.eye(len(support), dtype=np.int64)
            for _ in range(k):
                power = power @ u
            assert not power.any()
            if k > 1:
                assert np.linalg.matrix_power(u, k - 1).any()
            adjacency = u + u.T
            ev = np.linalg.eigvalsh(adjacency.astype(float))
            norm = float(max(abs(ev[0]), abs(ev[-1])))
            operator_bound = (n + 1) * math.cos(math.pi / (k + 1))
            assert norm <= operator_bound + 2e-10
            # The indicator's adjacency form equals twice its internal edges.
            internal = int(u.sum())
            assert boundary == n * count - 2 * internal
            stats['matrix_checks'] += 1
        if label.startswith('explicit:'):
            examples.append(dict(label=label, n=n, support_size=count,
                                 minority_size=minority, path_vertices=k,
                                 inclusion_chain_members=int(chain.max()) if n <= 8 else None,
                                 undirected_boundary=boundary,
                                 entropy_numeric=entropy))


for n in range(5):
    size = 1 << n
    for mask in range(1 << size):
        e = [(mask >> v) & 1 for v in range(size)]
        inspect(e, n, 'exhaustive', matrix=n <= 3 and mask % 7 == 0)

rng = random.Random(828416)
for n in range(5, 11):
    size = 1 << n
    for density in (0.03, 0.15, 0.4, 0.5, 0.6, 0.85, 0.97):
        for j in range(5):
            inspect([int(rng.random() < density) for _ in range(size)], n,
                    'random', matrix=n <= 7 and j == 0)
    # These have much longer inclusion chains than induced ascending paths.
    for modulus, selected in ((2, {0}), (3, {0, 1}), (4, {0, 1, 2})):
        inspect([int(v.bit_count() % modulus in selected) for v in range(size)],
                n, f'explicit:rank residues mod{modulus}', matrix=n <= 7)
    # An edge-free family spanning every Hamming rank is not required to
    # consist of a single rank or to be an antichain.
    inspect([int(v.bit_count() % 2 == 0 and ((v * 104729 + 17) % 19 < 13))
             for v in range(size)], n, 'explicit:thinned even ranks', matrix=n <= 7)
    inspect([int(v.bit_count() < n - 1) for v in range(size)], n,
            'explicit:nonminority downset', matrix=n <= 7)

for n in (12, 16):
    for modulus, selected in ((2, {0}), (3, {0, 1}), (4, {0, 1, 2})):
        inspect([int(v.bit_count() % modulus in selected) for v in range(1 << n)],
                n, f'explicit:large rank residues mod{modulus}')

# Independently check the dilation identities on general nonnormal
# contractions, not merely raising matrices from the Boolean cube.
for dimension in range(1, 10):
    for sample in range(3):
        arr = np.array([[complex(rng.random() - .5, rng.random() - .5)
                         if i < j else 0.0 for j in range(dimension)]
                        for i in range(dimension)], dtype=complex)
        norm = float(np.linalg.norm(arr, 2))
        t = arr / max(1.0, 1.1 * norm)
        defect = np.eye(dimension) - t.conj().T @ t
        eigenvalues, eigenvectors = np.linalg.eigh(defect)
        assert min(eigenvalues) > -1e-12
        d = (eigenvectors * np.sqrt(np.maximum(eigenvalues, 0))) @ eigenvectors.conj().T
        v = np.vstack([d @ np.linalg.matrix_power(t, j) for j in range(dimension)])
        backward = np.zeros((dimension * dimension, dimension * dimension), dtype=complex)
        for j in range(dimension - 1):
            backward[j * dimension:(j + 1) * dimension,
                     (j + 1) * dimension:(j + 2) * dimension] = np.eye(dimension)
        assert np.max(abs(v.conj().T @ v - np.eye(dimension))) < 1e-11
        assert np.max(abs(v @ t - backward @ v)) < 1e-11
        for phase in np.linspace(0, 2 * math.pi, 19, endpoint=False):
            realpart = (np.exp(1j * phase) * t + np.exp(-1j * phase) * t.conj().T) / 2
            tested_radius = float(np.linalg.eigvalsh(realpart)[-1])
            assert tested_radius <= np.linalg.norm(t, 2) * math.cos(math.pi / (dimension + 1)) + 1e-11
        stats['dilation_checks'] += 1

report = dict(status='PASS', independently_implemented=True, counts=stats,
              worst_exact_support_energy_ratio_float=worst_energy_ratio,
              worst_numeric_entropy_ratio=worst_entropy_ratio,
              examples=examples,
              exact_checks=['integer Walsh Parseval', 'integer physical influence normalization',
                            'n*minority_size <= (k+1)^2*boundary_edges',
                            'k=1: boundary_edges=n*support_size',
                            'compressed raising matrix powers', 'internal-edge identity'],
              numeric_supplements=['Fourier entropy', 'compressed adjacency eigenvalues',
                                   'general nilpotent contraction dilation identities',
                                   'sampled numerical radii'],
              limitations='Finite checks supplement the analytic proof; no novelty or universal proof inferred.')
out = Path(__file__).with_name('bounded_ascending_path_support_heat_checks.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(dict(status=report['status'], counts=stats,
                     worst_numeric_entropy_ratio=worst_entropy_ratio), indent=2))
