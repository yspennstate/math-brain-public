"""Independent audit checks; does not import the author's checker.

Truth tables are indexed by bit masks, with bit 1 meaning a positive input.
Chain and boundary identities use integer arithmetic. Entropy checks use
double precision and report their largest residual explicitly.
"""

from itertools import permutations, product
from math import comb, factorial, log2, e, lcm
import json
from pathlib import Path

import numpy as np


def cube_data(n):
    size = 1 << n
    weights = np.array([x.bit_count() for x in range(size)], dtype=int)
    lower, upper = [], []
    for x in range(size):
        for i in range(n):
            if not (x >> i) & 1:
                lower.append(x)
                upper.append(x | (1 << i))
    chains = []
    for permutation in permutations(range(n)):
        chain = [0]
        for i in permutation:
            chain.append(chain[-1] | (1 << i))
        chains.append(chain)
    return weights, np.array(lower), np.array(upper), np.array(chains)


def entropy_tables(values):
    coeff = values.astype(float).copy()
    width = 1
    while width < coeff.shape[1]:
        block = coeff.reshape(coeff.shape[0], -1, 2 * width)
        first = block[:, :, :width].copy()
        second = block[:, :, width:].copy()
        block[:, :, :width] = first + second
        block[:, :, width:] = first - second
        width *= 2
    coeff /= coeff.shape[1]
    probability = coeff**2
    logarithms = np.zeros_like(probability)
    nonzero = probability > 0
    logarithms[nonzero] = np.log2(1 / probability[nonzero])
    return np.sum(probability * logarithms, axis=1)


def check_chains():
    results = []
    rng = np.random.default_rng(2026100207)
    for n in range(1, 7):
        size = 1 << n
        layers, lo, hi, chains = cube_data(n)
        counts = np.array([comb(n, r) for r in range(n + 1)])
        common_denominator = lcm(*counts.tolist())
        edge_counts = counts[:-1] * np.arange(n, 0, -1)
        total = (1 << size) if n <= 4 else 2000
        chain_count = factorial(n)
        maximal_fei_ratio = 0.0
        maximum_mean_disagreement_ratio = 0.0
        max_variance_residual = 0
        num_nonsymmetric = []
        for start in range(0, total, 64):
            take = min(64, total - start)
            if n <= 4:
                ids = np.arange(start, start + take, dtype=np.uint64)
                positive = ((ids[:, None] >> np.arange(size, dtype=np.uint64)) & 1).astype(bool)
            else:
                positive = rng.integers(0, 2, size=(take, size)).astype(bool)
                # Add constant and rare-event cases at the start.
                if start == 0:
                    positive[0] = False
                    positive[1] = True
                    positive[2] = False
                    positive[2, 0] = True
                    positive[3] = True
                    positive[3, -1] = False
            truth = 2 * positive.astype(np.int64) - 1
            boundary = np.sum(positive[:, lo] != positive[:, hi], axis=1)
            chain_labels = positive[:, chains]
            weighted_changes = np.sum(
                (chain_labels[:, :, :-1] != chain_labels[:, :, 1:]) * edge_counts,
                axis=(1, 2),
            )
            assert np.array_equal(weighted_changes, chain_count * boundary)
            layer_positive = np.stack(
                [np.sum(positive[:, layers == r], axis=1) for r in range(n + 1)],
                axis=1,
            )
            comparator = chain_labels[:, :, layers]
            # Support: on every constant layer, every comparator has that label.
            for r in range(n + 1):
                constant = (layer_positive[:, r] == 0) | (layer_positive[:, r] == counts[r])
                if np.any(constant):
                    assert np.all(comparator[constant][:, :, layers == r] == positive[constant][:, None, layers == r])
            disagreement = np.sum(comparator != positive[:, None, :], axis=(1, 2))
            delta_marginal = sum(
                2 * chain_count * layer_positive[:, r] * (counts[r] - layer_positive[:, r]) // counts[r]
                for r in range(n + 1)
            )
            assert np.array_equal(disagreement, delta_marginal)
            f_mean_numerator = np.sum(truth, axis=1)
            g_mean_numerator = np.sum((2 * chain_labels.astype(np.int64) - 1) * counts, axis=2)
            assert np.array_equal(np.sum(g_mean_numerator, axis=1), chain_count * f_mean_numerator)
            mean_square = np.sum((g_mean_numerator - f_mean_numerator[:, None]) ** 2, axis=1)
            # Var_Pi(E g) <= 2 E delta, with denominator N^2 * n!.
            variance_residual = mean_square - 2 * size * disagreement
            assert np.all(variance_residual <= 0)
            max_variance_residual = max(max_variance_residual, int(np.max(variance_residual)))
            difference = truth[:, None, :] - (2 * comparator.astype(np.int64) - 1)
            quadratic_edges = np.sum((difference[:, :, lo] - difference[:, :, hi]) ** 2, axis=(1, 2))
            # E I(d) <= 4 I(f); all terms share denominator 2*N*n!.
            assert np.all(quadratic_edges <= 16 * chain_count * boundary)
            # The stronger symmetrization bound also holds in every case.
            assert np.all(quadratic_edges <= 8 * chain_count * boundary)
            exceptional_mask = (layer_positive != 0) & (layer_positive != counts)
            exceptional = np.sum(exceptional_mask, axis=1)
            run_length = np.zeros(take, dtype=int)
            current_run = np.zeros(take, dtype=int)
            for r in range(n + 1):
                current_run = np.where(exceptional_mask[:, r], current_run + 1, 0)
                run_length = np.maximum(run_length, current_run)
            h_scaled = 2 * layer_positive * (common_denominator // counts) - common_denominator
            h_energy_numerator = np.sum(edge_counts * np.diff(h_scaled, axis=1) ** 2, axis=1)
            # D = I(f)-I(P_sym f), denominator 2*N*common_denominator^2.
            defect_numerator = 4 * common_denominator**2 * boundary - h_energy_numerator
            assert np.all(defect_numerator >= 0)
            assert np.array_equal(common_denominator**2 * quadratic_edges, 2 * chain_count * defect_numerator)
            assert np.all(2 * n * common_denominator**2 * disagreement <= (run_length + 1) ** 2 * chain_count * defect_numerator)
            isolated = run_length == 1
            assert np.array_equal(2 * n * common_denominator**2 * disagreement[isolated], chain_count * defect_numerator[isolated])
            symmetric = run_length == 0
            assert np.all(defect_numerator[symmetric] == 0)
            assert np.all(disagreement[symmetric] == 0)
            assert np.all(n * disagreement <= 4 * chain_count * (exceptional + 1) ** 2 * boundary)
            nonconstant = boundary > 0
            if np.any(nonconstant):
                ratios = n * disagreement[nonconstant] / (2 * chain_count * boundary[nonconstant])
                maximum_mean_disagreement_ratio = max(maximum_mean_disagreement_ratio, float(np.max(ratios)))
                entropy = entropy_tables(truth)
                influence = 2 * boundary / size
                maximal_fei_ratio = max(maximal_fei_ratio, float(np.max(entropy[nonconstant] / influence[nonconstant])))
                assert np.all(entropy <= (25 + 64 * (exceptional + 1) ** 2) * influence + 1e-11)
                defect = defect_numerator / (2 * size * common_denominator**2)
                assert np.all(entropy <= 24.08 * influence + 32 * (run_length + 1) ** 2 * defect + 1e-11)
                assert np.all(entropy[isolated] <= 24.08 * influence[isolated] + 32 * defect[isolated] + 1e-11)
            num_nonsymmetric.extend(exceptional.tolist())
        results.append({
            "dimension": n,
            "functions": total,
            "exhaustive": n <= 4,
            "chain_count": chain_count,
            "max_variance_residual_integer": max_variance_residual,
            "max_n_mean_disagreement_over_influence": maximum_mean_disagreement_ratio,
            "max_entropy_over_influence": maximal_fei_ratio,
            "exceptional_layer_counts_seen": sorted(set(num_nonsymmetric)),
        })
    return results


def check_unions():
    results = []
    rng = np.random.default_rng(2026100208)
    entropy_constant = log2(e) * (1 + 1 / e)
    for n, r in [(1, 3), (2, 3), (3, 3), (4, 5), (6, 7)]:
        size = 1 << n
        _, lo, hi, _ = cube_data(n)
        exhaustive = n <= 3
        assignments = (r + 1) ** size if exhaustive else 5000
        max_entropy_residual = -float("inf")
        no_joining_edge_cases = 0
        joining_edge_cases = 0
        for start in range(0, assignments, 256):
            take = min(256, assignments - start)
            if exhaustive:
                ids = np.arange(start, start + take, dtype=np.int64)
                labels = np.stack([(ids // ((r + 1) ** x)) % (r + 1) for x in range(size)], axis=1)
            else:
                labels = rng.integers(0, r + 1, size=(take, size))
                if start == 0:
                    labels[0] = 0
                    labels[1] = 1
                    labels[2] = 0
                    labels[2, 0] = 1
            components = labels[:, None, :] == np.arange(1, r + 1)[None, :, None]
            union = labels > 0
            component_truth = 1 - 2 * components.astype(int)
            union_truth = 1 - 2 * union.astype(int)
            component_entropy = entropy_tables(component_truth.reshape(-1, size)).reshape(take, r)
            union_entropy = entropy_tables(union_truth)
            probability = np.mean(components, axis=2)
            variance = 4 * probability * (1 - probability)
            residual = union_entropy - r * np.sum(component_entropy, axis=1) - entropy_constant * np.sum(variance, axis=1)
            max_entropy_residual = max(max_entropy_residual, float(np.max(residual)))
            assert np.all(residual <= 1e-11)
            component_boundary = np.sum(components[:, :, lo] != components[:, :, hi], axis=(1, 2))
            union_boundary = np.sum(union[:, lo] != union[:, hi], axis=1)
            joining = np.sum((labels[:, lo] > 0) & (labels[:, hi] > 0) & (labels[:, lo] != labels[:, hi]), axis=1)
            # Exact cancellation formula: each joining edge is counted twice.
            assert np.array_equal(component_boundary - union_boundary, 2 * joining)
            assert np.array_equal(component_boundary[joining == 0], union_boundary[joining == 0])
            no_joining_edge_cases += int(np.sum(joining == 0))
            joining_edge_cases += int(np.sum(joining > 0))
        results.append({
            "dimension": n,
            "components": r,
            "assignments": assignments,
            "exhaustive": exhaustive,
            "max_entropy_residual": max_entropy_residual,
            "no_joining_edge_cases": no_joining_edge_cases,
            "joining_edge_cases": joining_edge_cases,
        })
    return results


def check_noncontiguous_adjacency():
    max_residual = -float("inf")
    cases = 0
    for n in range(1, 13):
        # Exact layer-restricted cube adjacency top eigenvalue occurs in the
        # symmetric sector; verify all layer subsets, including separated ones.
        for bits in range(1, 1 << (n + 1)):
            retained = [r for r in range(n + 1) if (bits >> r) & 1]
            k = len(retained)
            longest_run, current_run = 0, 0
            last = -2
            for r in retained:
                current_run = current_run + 1 if r == last + 1 else 1
                longest_run = max(longest_run, current_run)
                last = r
            matrix = np.zeros((k, k))
            for j in range(k - 1):
                r = retained[j]
                if retained[j + 1] == r + 1:
                    matrix[j, j + 1] = matrix[j + 1, j] = ((n - r) * (r + 1)) ** 0.5
            largest = float(np.linalg.eigvalsh(matrix)[-1])
            bound = (n + 1) * np.cos(np.pi / (longest_run + 1))
            residual = largest - bound
            max_residual = max(max_residual, residual)
            assert residual <= 1e-10
            if n >= (longest_run + 1) ** 2:
                assert n - largest >= n / (longest_run + 1) ** 2 - 1e-10
            cases += 1
    return {"layer_subsets": cases, "max_adjacency_residual": max_residual}


def check_weighted_crossing_layers():
    rng = np.random.default_rng(2026100209)
    cases = 0
    attained_endpoint_cases = 0
    for n in range(1, 11):
        size = 1 << n
        cube = np.array([[2 * ((x >> i) & 1) - 1 for i in range(n)] for x in range(size)])
        layers = np.array([x.bit_count() for x in range(size)])
        for trial in range(300):
            integer_weights = np.maximum(1, 10 + rng.integers(-3, 4, size=n))
            score = cube @ integer_weights
            deviation_numerator = int(np.sum(np.abs(integer_weights - 10)))
            m = int(rng.integers(1, 6))
            # Every crossing is an attained score; endpoints are not ignored.
            crossings = np.unique(rng.choice(score, size=m, replace=True))
            m = len(crossings)
            interval_labels = rng.integers(0, 2, size=m + 1)
            endpoint_labels = rng.integers(0, 2, size=m)
            labels = interval_labels[np.searchsorted(crossings, score, side="right")]
            for j, crossing in enumerate(crossings):
                labels[score == crossing] = endpoint_labels[j]
            eligible = np.zeros(n + 1, dtype=bool)
            for crossing in crossings:
                one_crossing = np.abs(10 * (2 * np.arange(n + 1) - n) - crossing) <= deviation_numerator
                assert np.sum(one_crossing) <= deviation_numerator // 10 + 1
                eligible |= one_crossing
            nonsymmetric = np.array([np.min(labels[layers == r]) != np.max(labels[layers == r]) for r in range(n + 1)])
            assert np.all(~nonsymmetric | eligible)
            assert np.sum(nonsymmetric) <= m * (deviation_numerator // 10 + 1)
            cases += 1
            attained_endpoint_cases += 1
    return {"cases": cases, "all_crossings_attained": attained_endpoint_cases}


if __name__ == "__main__":
    report = {
        "status": "PASS",
        "independent": True,
        "chain_checks": check_chains(),
        "union_checks": check_unions(),
        "noncontiguous_adjacency": check_noncontiguous_adjacency(),
        "weighted_crossing_layer_checks": check_weighted_crossing_layers(),
        "limits": "Finite checks support, but do not replace, the analytic audit; novelty is not assessed.",
    }
    path = Path(__file__).with_name("independent_union_chain_checks.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
