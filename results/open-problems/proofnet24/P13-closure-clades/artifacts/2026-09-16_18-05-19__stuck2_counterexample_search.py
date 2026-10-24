from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
import json

MAXN = 12
SIZES = tuple(range(2, MAXN + 1))


def H(k):
    return sum((Fraction(1, j) for j in range(1, k + 1)), Fraction())


def q(n, i):
    return Fraction(n, 2 * i * (n - i)) / H(n - 1)


for n in range(2, MAXN + 1):
    assert sum((q(n, i) for i in range(1, n)), Fraction()) == 1


@lru_cache(None)
def law(n):
    if n == 1:
        return {tuple([0] * len(SIZES)): Fraction(1)}
    root = [0] * len(SIZES)
    if n in SIZES:
        root[SIZES.index(n)] = 1
    out = defaultdict(Fraction)
    for i in range(1, n):
        for left, pleft in law(i).items():
            for right, pright in law(n - i).items():
                z = tuple(left[k] + right[k] + root[k] for k in range(len(SIZES)))
                out[z] += q(n, i) * pleft * pright
    assert sum(out.values(), Fraction()) == 1
    for z in out:
        assert sum(z[: n - 1]) == n - 1
    return dict(out)


def moments(n):
    dist = law(n)
    mu = [sum((Fraction(z[k]) * p for z, p in dist.items()), Fraction()) for k in range(len(SIZES))]
    cov = [[Fraction() for _ in SIZES] for __ in SIZES]
    for a in range(len(SIZES)):
        for b in range(len(SIZES)):
            cov[a][b] = sum(
                (Fraction(z[a]) - mu[a]) * (Fraction(z[b]) - mu[b]) * p
                for z, p in dist.items()
            )
    return mu, cov


mu_rec = {1: [Fraction() for _ in SIZES]}
cov_rec = {1: [[Fraction() for _ in SIZES] for __ in SIZES]}
mean_checks = cov_checks = row_sum_checks = 0

for n in range(2, MAXN + 1):
    mu = [Fraction(1 if r == n else 0) for r in SIZES]
    for i in range(1, n):
        for a in range(len(SIZES)):
            mu[a] += q(n, i) * (mu_rec[i][a] + mu_rec[n - i][a])
    mu_rec[n] = mu

    direct_mu, direct_cov = moments(n)
    assert mu == direct_mu
    mean_checks += len(SIZES)

    cov = [[Fraction() for _ in SIZES] for __ in SIZES]
    for i in range(1, n):
        for a in range(len(SIZES)):
            for b in range(len(SIZES)):
                cov[a][b] += q(n, i) * (cov_rec[i][a][b] + cov_rec[n - i][a][b])

    g = []
    for i in range(1, n):
        root = [Fraction(1 if r == n else 0) for r in SIZES]
        g.append([root[a] + mu_rec[i][a] + mu_rec[n - i][a] for a in range(len(SIZES))])

    for a in range(len(SIZES)):
        eg_a = sum((q(n, i) * g[i - 1][a] for i in range(1, n)), Fraction())
        for b in range(len(SIZES)):
            eg_b = sum((q(n, i) * g[i - 1][b] for i in range(1, n)), Fraction())
            egab = sum((q(n, i) * g[i - 1][a] * g[i - 1][b] for i in range(1, n)), Fraction())
            cov[a][b] += egab - eg_a * eg_b

    cov_rec[n] = cov
    assert cov == direct_cov
    cov_checks += len(SIZES) ** 2

    for a, r in enumerate(SIZES):
        if r <= n:
            assert sum(cov[a][b] for b, s in enumerate(SIZES) if s <= n) == 0
            row_sum_checks += 1

_, cov4 = moments(4)
i2, i3 = SIZES.index(2), SIZES.index(3)
assert cov4[i2][i3] == Fraction(-24, 121)

print(json.dumps({
    "result": "PASS",
    "scope": "independent exact adversarial recursion search through n=12",
    "arithmetic": "fractions.Fraction only",
    "split_normalization_checks": MAXN - 1,
    "mean_recursion_entries": mean_checks,
    "covariance_recursion_entries": cov_checks,
    "deterministic_covariance_row_sum_checks": row_sum_checks,
    "n4_cov_N2_N3": str(cov4[i2][i3]),
    "state_counts": {str(n): len(law(n)) for n in range(1, MAXN + 1)},
    "note": "SELF-CHECK / COUNTEREXAMPLE SEARCH ONLY; no new theorem claim and not an independent closure audit."
}, indent=2, sort_keys=True))
