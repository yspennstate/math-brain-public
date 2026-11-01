from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
import hashlib
import json
import sys
import time

MAX_N = 14
SIZES = tuple(range(2, MAX_N + 1))


def H(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def q(n, i):
    return Fraction(n, 1) / (2 * H(n - 1) * i * (n - i))


for n in range(2, MAX_N + 1):
    assert sum((q(n, i) for i in range(1, n)), Fraction(0)) == 1


@lru_cache(None)
def law(n):
    """Exact law of the full padded clade-count vector (N_2,...,N_MAX_N)."""
    if n == 1:
        return {tuple(0 for _ in SIZES): Fraction(1)}
    out = defaultdict(Fraction)
    root = tuple(1 if r == n else 0 for r in SIZES)
    for i in range(1, n):
        qi = q(n, i)
        for left, pl in law(i).items():
            for right, pr in law(n - i).items():
                z = tuple(left[k] + right[k] + root[k] for k in range(len(SIZES)))
                out[z] += qi * pl * pr
    assert sum(out.values(), Fraction(0)) == 1
    # Every rooted full binary tree with n leaves has exactly n-1 internal clades.
    for z in out:
        assert sum(z[: max(0, n - 1)]) == n - 1
        assert all(v == 0 for v in z[max(0, n - 1):])
    return dict(out)


def direct_means_and_cov(n):
    dist = law(n)
    means = {}
    for r in range(2, MAX_N + 1):
        idx = r - 2
        means[r] = sum((Fraction(z[idx]) * p for z, p in dist.items()), Fraction(0))
    cov = {}
    for r in range(2, MAX_N + 1):
        ir = r - 2
        for s in range(2, MAX_N + 1):
            is_ = s - 2
            cov[r, s] = sum(
                (
                    (Fraction(z[ir]) - means[r])
                    * (Fraction(z[is_]) - means[s])
                    * p
                    for z, p in dist.items()
                ),
                Fraction(0),
            )
    return means, cov


# Independent mean recursion.
mu = {r: {1: Fraction(0)} for r in SIZES}
mean_checks = 0
for n in range(2, MAX_N + 1):
    dmean, _ = direct_means_and_cov(n)
    for r in SIZES:
        mu[r][n] = Fraction(1 if n == r else 0) + sum(
            (
                q(n, i)
                * (mu[r].get(i, Fraction(0)) + mu[r].get(n - i, Fraction(0)))
                for i in range(1, n)
            ),
            Fraction(0),
        )
        assert mu[r][n] == dmean[r]
        mean_checks += 1


@lru_cache(None)
def occupation(n, j):
    if n < j:
        return Fraction(0)
    if n == j:
        return Fraction(1)
    return sum(
        (
            Fraction(1, 1) / (H(n - 1) * (n - i)) * occupation(i, j)
            for i in range(1, n)
        ),
        Fraction(0),
    )


occupation_checks = 0
for n in range(1, MAX_N + 1):
    for r in SIZES:
        lhs = Fraction(r, n) * mu[r].get(n, Fraction(0))
        assert lhs == occupation(n, r)
        occupation_checks += 1


# Normalized covariance recurrence C_{rs}(n)=Cov/n and exact Green representation.
eta = {}
crec = {}
cov_checks = 0
green_checks = 0
support_checks = 0
row_sum_checks = 0

for n in range(1, MAX_N + 1):
    _, dcov = direct_means_and_cov(n)
    for r in SIZES:
        for s in SIZES:
            if n == 1:
                eta[n, r, s] = Fraction(0)
                crec[n, r, s] = Fraction(0)
                continue

            gr = [
                mu[r].get(i, Fraction(0)) + mu[r].get(n - i, Fraction(0))
                for i in range(1, n)
            ]
            gs = [
                mu[s].get(i, Fraction(0)) + mu[s].get(n - i, Fraction(0))
                for i in range(1, n)
            ]
            er = sum((q(n, i) * gr[i - 1] for i in range(1, n)), Fraction(0))
            es = sum((q(n, i) * gs[i - 1] for i in range(1, n)), Fraction(0))
            ep = sum(
                (q(n, i) * gr[i - 1] * gs[i - 1] for i in range(1, n)),
                Fraction(0),
            )
            eta[n, r, s] = (ep - er * es) / n

            if n < max(r, s):
                assert eta[n, r, s] == 0
                support_checks += 1

            inherited = sum(
                (
                    Fraction(1, 1) / (H(n - 1) * (n - i)) * crec[i, r, s]
                    for i in range(1, n)
                ),
                Fraction(0),
            )
            crec[n, r, s] = inherited + eta[n, r, s]
            assert crec[n, r, s] == dcov[r, s] / n
            cov_checks += 1

            green = sum(
                (occupation(n, j) * eta[j, r, s] for j in range(2, n + 1)),
                Fraction(0),
            )
            assert green == crec[n, r, s]
            green_checks += 1

    # Deterministic total internal-clade count: sum_{s=2}^n N_n(s)=n-1.
    for r in range(2, n + 1):
        assert sum((dcov[r, s] for s in range(2, n + 1)), Fraction(0)) == 0
        row_sum_checks += 1


# Counterexample-first witness at n=4.
dmean4, dcov4 = direct_means_and_cov(4)
assert q(4, 1) == Fraction(4, 11)
assert q(4, 2) == Fraction(3, 11)
assert q(4, 3) == Fraction(4, 11)
assert dmean4[2] == Fraction(14, 11)
assert dmean4[3] == Fraction(8, 11)
assert dcov4[2, 3] == Fraction(-24, 121)

payload = {
    "result": "PASS",
    "arithmetic": "fractions.Fraction exact rational arithmetic only",
    "max_tree_size": MAX_N,
    "full_coordinate_set": [2, MAX_N],
    "root_split_normalizations_checked": MAX_N - 1,
    "mean_recursion_checks": mean_checks,
    "occupation_mean_identity_checks": occupation_checks,
    "covariance_recursion_checks": cov_checks,
    "green_representation_checks": green_checks,
    "eta_support_zero_checks": support_checks,
    "deterministic_covariance_row_sum_checks": row_sum_checks,
    "state_counts_by_n": {str(n): len(law(n)) for n in range(1, MAX_N + 1)},
    "n4_witness": {
        "q4": ["4/11", "3/11", "4/11"],
        "E_N2": "14/11",
        "E_N3": "8/11",
        "Cov_N2_N3": "-24/121",
        "independence_ansatz": "REFUTED",
    },
    "python_version": sys.version.split()[0],
}
print(json.dumps(payload, indent=2, sort_keys=True))
print("ALL FULL-BLOCK EXACT CHECKS PASSED")
