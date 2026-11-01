from fractions import Fraction
from functools import lru_cache
from collections import defaultdict

MAX_M = 6
MAX_N = 10
SIZES = tuple(range(2, MAX_M + 1))


def H(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def q(n, i):
    # Critical beta-splitting root split probability q(n,i).
    return Fraction(n, 1) / (2 * H(n - 1) * i * (n - i))


for n in range(2, MAX_N + 1):
    assert sum((q(n, i) for i in range(1, n)), Fraction(0)) == 1


@lru_cache(None)
def distribution(n):
    """Exact law of (N_2,...,N_MAX_M) in DTCS(n)."""
    if n == 1:
        return {tuple(0 for _ in SIZES): Fraction(1)}
    out = defaultdict(Fraction)
    root = tuple(1 if r == n else 0 for r in SIZES)
    for i in range(1, n):
        qi = q(n, i)
        for left, pl in distribution(i).items():
            for right, pr in distribution(n - i).items():
                z = tuple(left[k] + right[k] + root[k] for k in range(len(SIZES)))
                out[z] += qi * pl * pr
    assert sum(out.values(), Fraction(0)) == 1
    return dict(out)


def direct_mean(n, r):
    idx = SIZES.index(r)
    return sum((Fraction(v[idx]) * p for v, p in distribution(n).items()), Fraction(0))


def direct_cov(n, r, s):
    ir, is_ = SIZES.index(r), SIZES.index(s)
    mr, ms = direct_mean(n, r), direct_mean(n, s)
    return sum(
        ((Fraction(v[ir]) - mr) * (Fraction(v[is_]) - ms) * p for v, p in distribution(n).items()),
        Fraction(0),
    )


# Independent mean recursion, including the deterministic root-clade toll 1_{n=r}.
mu = {r: {1: Fraction(0)} for r in SIZES}
mean_checks = 0
for n in range(2, MAX_N + 1):
    for r in SIZES:
        mu[r][n] = Fraction(1 if n == r else 0) + sum(
            (q(n, i) * (mu[r].get(i, Fraction(0)) + mu[r].get(n - i, Fraction(0))) for i in range(1, n)),
            Fraction(0),
        )
        assert mu[r][n] == direct_mean(n, r)
        mean_checks += 1


@lru_cache(None)
def occupation(n, j):
    """Exact HD-chain occupation probability a(n,j)."""
    if n < j:
        return Fraction(0)
    if n == j:
        return Fraction(1)
    return sum(
        (Fraction(1, 1) / (H(n - 1) * (n - i)) * occupation(i, j) for i in range(1, n)),
        Fraction(0),
    )


occupation_checks = 0
for n in range(2, MAX_N + 1):
    for r in SIZES:
        # Source identity E N_n(r) = n a(n,r)/r.
        assert Fraction(r, n) * mu[r][n] == occupation(n, r)
        occupation_checks += 1


# Independent normalized covariance recursion and Green/occupation representation.
eta = {}
crec = {}
covariance_recursion_checks = 0
green_checks = 0
for n in range(1, MAX_N + 1):
    for r in SIZES:
        for s in SIZES:
            if n == 1:
                eta[n, r, s] = Fraction(0)
                crec[n, r, s] = Fraction(0)
                continue
            gr = [mu[r].get(i, Fraction(0)) + mu[r].get(n - i, Fraction(0)) for i in range(1, n)]
            gs = [mu[s].get(i, Fraction(0)) + mu[s].get(n - i, Fraction(0)) for i in range(1, n)]
            egr = sum((q(n, i) * gr[i - 1] for i in range(1, n)), Fraction(0))
            egs = sum((q(n, i) * gs[i - 1] for i in range(1, n)), Fraction(0))
            eprod = sum((q(n, i) * gr[i - 1] * gs[i - 1] for i in range(1, n)), Fraction(0))
            eta[n, r, s] = (eprod - egr * egs) / n
            inherited = sum(
                (Fraction(1, 1) / (H(n - 1) * (n - i)) * crec[i, r, s] for i in range(1, n)),
                Fraction(0),
            )
            crec[n, r, s] = inherited + eta[n, r, s]
            assert crec[n, r, s] == direct_cov(n, r, s) / n
            covariance_recursion_checks += 1

            green = sum((occupation(n, j) * eta[j, r, s] for j in range(2, n + 1)), Fraction(0))
            assert green == crec[n, r, s]
            green_checks += 1


# Counterexample-first witness at n=4: N_2 and N_3 are not independent.
assert q(4, 1) == Fraction(4, 11)
assert q(4, 2) == Fraction(3, 11)
assert q(4, 3) == Fraction(4, 11)
assert direct_mean(4, 2) == Fraction(14, 11)
assert direct_mean(4, 3) == Fraction(8, 11)
assert direct_cov(4, 2, 3) == Fraction(-24, 121)

print("EXACT DTCS CLADE-COVARIANCE CHECK")
print(f"max_clade_coordinate={MAX_M}")
print(f"max_tree_size={MAX_N}")
print(f"root_split_normalizations_checked={MAX_N-1}")
print(f"mean_recursion_checks={mean_checks}")
print(f"occupation_mean_identity_checks={occupation_checks}")
print(f"covariance_recursion_checks={covariance_recursion_checks}")
print(f"green_representation_checks={green_checks}")
print("state_counts_by_n=" + ",".join(f"{n}:{len(distribution(n))}" for n in range(1, MAX_N + 1)))
print("n=4 split law: q(4,1)=4/11, q(4,2)=3/11, q(4,3)=4/11")
print("n=4 E[N_2]=14/11")
print("n=4 E[N_3]=8/11")
print("n=4 Cov(N_2,N_3)=-24/121")
print("n=4 independence_ansatz=REFUTED")
print("ALL EXACT CHECKS PASSED")
