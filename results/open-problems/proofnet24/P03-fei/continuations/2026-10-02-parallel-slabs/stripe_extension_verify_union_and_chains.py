"""Finite checks for the union entropy lemma and random-chain identities."""
import itertools
import json
import math
from pathlib import Path

import numpy as np

rng = np.random.default_rng(20261013)
LE = math.log2(math.e)
report = {
    "status": "passed",
    "scope": "finite checks only, no asymptotic or novelty certification",
    "union_cases": 0, "chain_cases": 0, "chain_permutations": 0,
    "maxima": {},
}


def note(name, v):
    report["maxima"][name] = max(float(v), report["maxima"].get(name, -math.inf))


def ft(a):
    a = np.array(a, dtype=float)
    size = a.shape[-1]
    for step in [1 << j for j in range(size.bit_length() - 1)]:
        v = a.reshape(*a.shape[:-1], -1, 2 * step)
        l, r = v[..., :step].copy(), v[..., step:].copy()
        v[..., :step], v[..., step:] = l + r, l - r
    return a / size


def entropy(a):
    use = a > 0
    return float(-a[use] @ np.log2(a[use]))


def influence(f, n):
    idx = np.arange(1 << n)
    return sum(float(np.mean((f - f[idx ^ (1 << j)]) ** 2)) / 4
               for j in range(n))


def union_test(n, assignment, r):
    # Labels 0 denote outside; labels 1,...,r are disjoint components.
    f = np.where(assignment, -1., 1.)
    gs = np.array([np.where(assignment == j, -1., 1.)
                   for j in range(1, r + 1)])
    fh, gh = ft(f), ft(gs)
    Hf = entropy(fh ** 2)
    Hgs = sum(entropy(g ** 2) for g in gh)
    varsum = float(np.sum(1 - gs.mean(axis=1) ** 2))
    bound = r * Hgs + LE * (1 + 1 / math.e) * varsum
    assert Hf <= bound + 1e-12
    assert 1 - f.mean() ** 2 <= varsum + 1e-12
    idx = np.arange(1 << n)
    component_influences = sum(influence(g, n) for g in gs)
    If = influence(f, n)
    crossing_probability = sum(
        float(np.mean((assignment != 0) & (assignment[idx ^ (1 << j)] != 0)
                      & (assignment != assignment[idx ^ (1 << j)])))
        for j in range(n)
    )
    # Every joining edge contributes two component boundaries and zero
    # union boundaries, with the physical influence convention.
    assert abs(component_influences - If - 2 * crossing_probability) < 1e-12
    note("union_entropy_minus_bound", Hf - bound)
    note("union_influence_identity_error",
         abs(component_influences - If - 2 * crossing_probability))
    report["union_cases"] += 1


for n in [1, 2, 3, 4, 5, 6, 8, 10]:
    for r in [1, 2, 3, 5]:
        for _ in range(100):
            probs = rng.dirichlet(np.ones(r + 1) * rng.choice([.1, 1., 10.]))
            assignment = rng.choice(r + 1, 1 << n, p=probs)
            union_test(n, assignment, r)


def chain_test(f, n, chain_indices):
    idx = np.arange(1 << n)
    layer = np.array([int(v).bit_count() for v in idx])
    layer_mass = np.bincount(layer) / (1 << n)
    layer_mean = np.array([float(f[layer == r].mean()) for r in range(n + 1)])
    labels = f[chain_indices]
    gs = labels[:, layer]
    gmean = gs.mean(axis=0)
    assert np.max(np.abs(gmean - layer_mean[layer])) < 1e-12
    boundary_weight = np.array([2 * (n - r) * layer_mass[r] for r in range(n)])
    Ig = np.sum((labels[:, :-1] != labels[:, 1:]) * boundary_weight, axis=1)
    If = influence(f, n)
    assert abs(Ig.mean() - If) < 1e-12
    delta = np.mean(gs != f, axis=1)
    expected_delta = float(np.dot(layer_mass, (1 - layer_mean ** 2) / 2))
    assert abs(delta.mean() - expected_delta) < 1e-12
    d = f - gs
    Id = np.zeros(len(gs))
    for j in range(n):
        Id += np.mean((d - d[:, idx ^ (1 << j)]) ** 2, axis=1) / 4
    assert Id.mean() <= 4 * If + 1e-12
    # Stronger orthogonal-projection identity, beyond the drafted proof.
    symf = layer_mean[layer]
    Isymf = influence(symf, n)
    assert abs(Id.mean() - 2 * (If - Isymf)) < 1e-12
    vard = np.mean(d ** 2, axis=1) - np.mean(d, axis=1) ** 2
    assert vard.mean() >= 2 * delta.mean() - 1e-12
    exceptional = np.array([r for r in range(n + 1)
                            if abs(layer_mean[r]) < 1])
    k = len(exceptional)
    assert np.all(d[:, ~np.isin(layer, exceptional)] == 0)
    assert n * delta.mean() <= 2 * (k + 1) ** 2 * If + 1e-12
    Hf = entropy(ft(f) ** 2)
    assert Hf <= (25 + 64 * (k + 1) ** 2) * If + 1e-12
    note("chain_mean_influence_error", abs(Ig.mean() - If))
    note("chain_mean_disagreement_error", abs(delta.mean() - expected_delta))
    note("projection_dirichlet_identity_error",
         abs(Id.mean() - 2 * (If - Isymf)))
    note("averaged_variance_ratio", vard.mean() / delta.mean() if delta.mean() else 0)
    note("almost_symmetric_entropy_over_influence", Hf / If if If else 0)
    report["chain_cases"] += 1
    report["chain_permutations"] += len(gs)


for n in [1, 2, 3, 4, 5, 6]:
    permutations = list(itertools.permutations(range(n)))
    chain_indices = []
    for permutation in permutations:
        chain = [0]
        for j in permutation:
            chain.append(chain[-1] | (1 << j))
        chain_indices.append(chain)
    chain_indices = np.array(chain_indices)
    layer = np.array([int(v).bit_count() for v in range(1 << n)])
    if n <= 3:
        functions = [2 * ((mask >> np.arange(1 << n)) & 1).astype(float) - 1
                     for mask in range(1 << (1 << n))]
    else:
        functions = []
        for _ in range({4: 200, 5: 100, 6: 40}[n]):
            f = rng.choice([-1., 1.], n + 1)[layer]
            exceptions = rng.choice(n + 1, int(rng.integers(1, n + 2)), replace=False)
            for r in exceptions:
                f[layer == r] = rng.choice([-1., 1.], int(np.sum(layer == r)))
            functions.append(f)
    for f in functions:
        chain_test(f, n, chain_indices)

Path(__file__).with_name("stripe_extension_union_and_chains_verification.json").write_text(
    json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
