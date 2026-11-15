"""Exact finite checks for subset concentration, old permutation variance and obstructions."""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial
import os
import resource
import signal
import time


def avg(values):
    values = list(values)
    return sum(values, F(0)) / len(values)


def conditional_total(weights, q, prefix):
    # Enumerate all remaining subsets: independent of the closed-form martingale.
    remaining = [i for i in range(len(weights)) if i not in prefix]
    return avg(sum((weights[i] for i in prefix + tail), F(0))
               for tail in combinations(remaining, q - len(prefix)))


def scalar_checks():
    subset_count = prefix_count = cases = old_instances = 0
    for n in range(2, 11):
        populations = {
            "constant": (F(1, n),) * n,
            "point": (F(1),) + (F(0),) * (n - 1),
            "signed": tuple(F((-1) ** i * (i + 1), n * n) for i in range(n)),
        }
        for weights in populations.values():
            mu = avg(weights)
            variance = avg(w * w for w in weights) - mu * mu
            b = max(abs(w) for w in weights)
            for q in range(n + 1):
                vals = []
                for subset in combinations(range(n), q):
                    val = sum((weights[i] for i in subset), F(0)) - q * mu
                    other = sum((weights[i] for i in range(n) if i not in subset), F(0))
                    assert val == -(other - (n - q) * mu)
                    vals.append(val)
                assert len(vals) == comb(n, q)
                assert avg(vals) == 0
                expected_var = F(q * (n - q), n - 1) * variance
                assert avg(v * v for v in vals) == expected_var
                subset_count += len(vals)
                cases += 1
                if n <= 6 and 0 < q < n:
                    for j in range(1, q + 1):
                        for prefix in permutations(range(n), j):
                            before = conditional_total(weights, q, prefix[:-1])
                            after = conditional_total(weights, q, prefix)
                            remaining = [i for i in range(n) if i not in prefix[:-1]]
                            formula = F(n - q, n - j) * (weights[prefix[-1]] - avg(weights[i] for i in remaining))
                            assert after - before == formula
                            assert abs(after - before) <= 2 * b
                            prefix_count += 1
            # Recheck the earlier variance by an independent subset, rather than
            # permutation-prefix, enumeration: a has q plus signs and N-q negatives.
            for q in range(1, n):
                values = []
                sigma_a2 = F(q * (n - q), n * n)
                for subset in combinations(range(n), q):
                    val = sum((weights[i] for i in subset), F(0)) - F(q, n) * sum(weights)
                    values.append(val)
                earlier_formula = sigma_a2 / (n - 1) * (n * sum(w * w for w in weights) - sum(weights) ** 2)
                assert avg(v * v for v in values) == earlier_formula
                old_instances += len(values)
    print(f"PASS subset_cases={cases} subset_instances={subset_count} conditional_prefixes={prefix_count}")
    print(f"PASS earlier_variance_independent_subset_instances={old_instances}")


def matrix_checks():
    matrices = entries = compressed_cases = 0
    for h in range(1, 5):
        n = 2 ** h
        hadamard = [[(-1) ** ((i & j).bit_count() % 2) for j in range(n)] for i in range(n)]
        raw = []
        for i in range(0, n, 2):
            for sign in (1, -1):
                raw.append([(hadamard[i][j] + sign * hadamard[i + 1][j]) // 2 for j in range(n)])
        scale2 = F(2, n)
        for a in range(n):
            assert sum(raw[i][a] ** 2 for i in range(n)) == n // 2
            for b in range(n):
                assert scale2 * sum(raw[i][a] * raw[i][b] for i in range(n)) == (a == b)
        # B is rational although the eigenbasis uses a square-root normalization.
        mat = [[scale2 * sum(raw[i][j] * (j + 1) * raw[l][j] for j in range(n))
                for l in range(n)] for i in range(n)]
        for col in range(n):
            for i in range(n):
                assert sum(mat[i][j] * raw[j][col] for j in range(n)) == (col + 1) * raw[i][col]
                assert abs(n * scale2 * raw[i][col] ** 2 - 1) == 1
                entries += 1
        # Support-based choice has size N/2, mass 1 and relative discrepancy 1.
        support = [i for i in range(n) if raw[i][0]]
        assert len(support) == n // 2
        assert scale2 * sum(raw[i][0] ** 2 for i in support) == 1
        assert F(n, len(support)) - 1 == 1
        matrices += 1
        if n <= 8:
            for columns in ((0, 1), (0, 2)) if n >= 4 else ((0, 1),):
                project_diag = [scale2 * sum(raw[i][a] ** 2 for a in columns) for i in range(n)]
                assert sum(project_diag) == len(columns)
                l2 = n * max(project_diag)
                assert len(columns) <= l2
                for k in range(1, n):
                    for subset in combinations(range(n), k):
                        c = [[scale2 * sum(raw[i][a] * raw[i][b] for i in subset)
                              - F(k, n) * (a == b) for b in columns] for a in columns]
                        t = max(abs(x) for row in c for x in row)
                        # Check every sign direction (1,+/-1)/sqrt 2 exactly.
                        for sign in (1, -1):
                            quadratic = (c[0][0] + c[1][1] + sign * (c[0][1] + c[1][0])) / 2
                            assert abs(quadratic) <= len(columns) * t <= l2 * t
                        compressed_cases += 1
    print(f"PASS Walsh_ensemble_sizes=2,4,8,16 matrices={matrices} eigenvector_coordinates={entries}")
    print(f"PASS repeated_eigenspace_subset_compressions={compressed_cases}")


def main():
    signal.alarm(90)
    resource.setrlimit(resource.RLIMIT_CPU, (80, 80))
    started = time.monotonic()
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, priority
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    print("nice", priority)
    print("OMP_NUM_THREADS", os.environ["OMP_NUM_THREADS"])
    scalar_checks()
    matrix_checks()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert rss < 1_000_000_000
    print("peak_rss_bytes", rss)
    print("elapsed_seconds", round(time.monotonic() - started, 3))


if __name__ == "__main__":
    main()
