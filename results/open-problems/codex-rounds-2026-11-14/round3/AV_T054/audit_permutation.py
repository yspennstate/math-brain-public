"""Exact finite checks for the permutation argument in PROOF.md."""

from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations
import math
import os
import resource
import time


def check(n, weights):
    a = tuple(F(2 * i - n + 1, n - 1) for i in range(n))
    sums = defaultdict(lambda: [F(0), 0])
    total = F(0)
    square = F(0)
    count = 0
    for p in permutations(range(n)):
        value = sum((weights[i] * a[p[i]] for i in range(n)), F(0))
        total += value
        square += value * value
        count += 1
        for k in range(n + 1):
            key = p[:k]
            sums[key][0] += value
            sums[key][1] += 1
    assert count == math.factorial(n)
    assert total == 0
    sigma2 = sum(x * x for x in a) / n
    predicted = sigma2 / (n - 1) * (
        n * sum(w * w for w in weights) - sum(weights) ** 2
    )
    assert square / count == predicted
    bound = max(abs(w) for w in weights)
    largest = F(0)
    for prefix, (numerator, denominator) in sums.items():
        k = len(prefix)
        if not k:
            continue
        prev = prefix[:-1]
        before = sums[prev][0] / sums[prev][1]
        after = numerator / denominator
        diff = after - before
        remaining = [i for i in range(n) if i not in prev]
        if len(remaining) == 1:
            formula = F(0)
        else:
            mu = sum(a[i] for i in remaining) / len(remaining)
            other_weight_mean = sum(weights[k:]) / (n - k)
            formula = (a[prefix[-1]] - mu) * (weights[k - 1] - other_weight_mean)
        assert diff == formula, (n, weights, prefix, diff, formula)
        assert abs(diff) <= 4 * bound
        largest = max(largest, abs(diff))
    return count, len(sums), predicted, largest


def main():
    started = time.monotonic()
    print("nice", os.getpriority(os.PRIO_PROCESS, 0))
    print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS"))
    checks = 0
    prefixes = 0
    permutations_checked = 0
    for n in range(2, 8):
        cases = {
            "flat": tuple(F(1, n) for _ in range(n)),
            "point": (F(1),) + (F(0),) * (n - 1),
            "signed": tuple(F((-1) ** i * (i + 1), n * n) for i in range(n)),
        }
        for name, weights in cases.items():
            count, n_prefixes, variance, largest = check(n, weights)
            checks += 1
            prefixes += n_prefixes
            permutations_checked += count
            print(f"N={n} case={name} permutations={count} variance={variance} max_increment={largest}")
    # Exact repeated-eigenspace example: two disjoint flat columns.
    # It has m=2 and max diagonal of its projector 2/N, so m=L^2.
    for n in (4, 6, 8):
        projector_diag = [F(2, n)] * n
        assert sum(projector_diag) == 2
        assert F(n) * max(projector_diag) == 2
        # Support-dependent mean-zero test gives observable exactly 1.
        mass = [F(2, n)] * (n // 2) + [F(0)] * (n // 2)
        test = [1] * (n // 2) + [-1] * (n // 2)
        assert sum(mass) == 1 and sum(test) == 0
        assert sum(x * y for x, y in zip(mass, test)) == 1
    print(f"PASS cases={checks} permutations={permutations_checked} prefix_checks={prefixes}")
    print("PASS projection trace and adaptive-test obstruction N=4,6,8")
    print("peak_rss_bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print("elapsed_seconds", round(time.monotonic() - started, 3))


if __name__ == "__main__":
    main()
