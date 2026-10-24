from fractions import Fraction
import math
import json


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def log2_binom(n: int, k: int) -> float:
    return sum(math.log2(n - j) - math.log2(j + 1) for j in range(k))


# Exact product obstruction for Theorem B13-BLOCK-LAPLACE-01.
n = 64
q = Fraction(1, n)
s = Fraction(1, 2)
lhs = Fraction(127, 128) ** 63
rhs = Fraction(1, 4)  # (1/64)^(1/3)
bernoulli_lower = Fraction(65, 128)
assert lhs >= bernoulli_lower > rhs

# Abstract clustered-law diagnostic showing that the singleton first-moment
# corollary alone is insufficient. This is NOT claimed Boolean.
n_cluster = 4096
L = 7
mean_size = Fraction(1, 1)
q_cluster = Fraction(1, n_cluster)
conditional_other_mean = L - 1
required_other_mean = 0.5 * math.log2(n_cluster)
assert conditional_other_mean == required_other_mean
cluster_entropy = h2(1.0 / L) + log2_binom(n_cluster, L) / L

out = {
    "status": "PASS",
    "product_obstruction": {
        "n": n,
        "q": "1/64",
        "s": "1/2",
        "lhs_exact": "(127/128)^63",
        "lhs_decimal": float(lhs),
        "bernoulli_lower_bound": "65/128",
        "rhs_exact": "1/4",
        "exact_chain": "(127/128)^63 >= 65/128 > 1/4",
    },
    "clustered_relaxation": {
        "boolean_claim": False,
        "n": n_cluster,
        "L": L,
        "mean_size": float(mean_size),
        "marginal_q": "1/4096",
        "conditional_other_mean": conditional_other_mean,
        "required_singleton_mean_bound": required_other_mean,
        "entropy_bits": cluster_entropy,
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
