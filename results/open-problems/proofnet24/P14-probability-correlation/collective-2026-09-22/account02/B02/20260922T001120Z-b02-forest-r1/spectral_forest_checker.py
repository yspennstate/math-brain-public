from fractions import Fraction
from itertools import combinations
from math import comb


def is_forest(n, edges, mask):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, (u, v) in enumerate(edges):
        if not ((mask >> i) & 1):
            continue
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def stats(n, edges):
    m = len(edges)
    forests = [mask for mask in range(1 << m) if is_forest(n, edges, mask)]
    Z = len(forests)
    S1 = sum(mask.bit_count() for mask in forests)
    S2 = sum(mask.bit_count() ** 2 for mask in forests)
    Ze = [0] * m
    Zef = {}
    for mask in forests:
        for i in range(m):
            if (mask >> i) & 1:
                Ze[i] += 1
        for i in range(m):
            if not ((mask >> i) & 1):
                continue
            for j in range(i + 1, m):
                if (mask >> j) & 1:
                    Zef[i, j] = Zef.get((i, j), 0) + 1
    return Z, S1, S2, Ze, Zef


total_graphs = 0
total_pairs = 0
factor2_failures = 0
size_variance_failures = 0
target_negative_gaps = 0

for n in range(2, 6):
    all_edges = list(combinations(range(n), 2))
    for gmask in range(1 << len(all_edges)):
        edges = [all_edges[i] for i in range(len(all_edges)) if (gmask >> i) & 1]
        total_graphs += 1
        Z, S1, S2, Ze, Zef = stats(n, edges)
        # Var(|F|) <= E|F|, the one-variable Hessian consequence of log-concavity.
        if Z * S2 - S1 * S1 > Z * S1:
            size_variance_failures += 1
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                total_pairs += 1
                zij = Zef.get((i, j), 0)
                delta = Ze[i] * Ze[j] - Z * zij
                if delta < 0:
                    target_negative_gaps += 1
                # Spectral Rayleigh PSD gives |Delta_ij| <= Z_i Z_j, hence
                # Z Z_ij <= 2 Z_i Z_j even without the desired Delta_ij >= 0.
                if Z * zij > 2 * Ze[i] * Ze[j]:
                    factor2_failures += 1

# K3 exact test of a tempting but false-as-necessity Schur-complement route.
n = 3
edges = [(0, 1), (0, 2), (1, 2)]
Z, S1, S2, Ze, Zef = stats(n, edges)
i, j = 0, 1
p = Fraction(Ze[i], Z)
EK = Fraction(S1, Z)
EK2 = Fraction(S2, Z)
varK = EK2 - EK * EK
sum_kxe = Fraction(0, 1)
for mask in range(1 << len(edges)):
    if is_forest(n, edges, mask) and ((mask >> i) & 1):
        sum_kxe += Fraction(mask.bit_count(), Z)
c = sum_kxe - EK * p
s = Fraction(len(edges), 1) - EK - varK
schur_lhs = 2 * (c / p) ** 2

# Exact cancellation of fixed-size negative covariance by size mixing on a tree.
m = 4
weights = [Fraction(comb(m, k), 2**m) for k in range(m + 1)]
mean_cond_cov = sum(
    (weights[k] * Fraction(-k * (m - k), m * m * (m - 1)) for k in range(m + 1)),
    Fraction(0, 1),
)
varKtree = Fraction(m, 4)
mix_cov = varKtree / Fraction(m * m, 1)

print(f"TOTAL_GRAPHS={total_graphs}")
print(f"TOTAL_EDGE_PAIRS={total_pairs}")
print(f"FACTOR2_FAILURES={factor2_failures}")
print(f"SIZE_VARIANCE_FAILURES={size_variance_failures}")
print(f"TARGET_NEGATIVE_GAPS={target_negative_gaps}")
print(f"K3_Z={Z} K3_ZE={Ze[i]} K3_ZEF={Zef[i,j]} K3_DELTA={Ze[i]*Ze[j]-Z*Zef[i,j]}")
print(f"K3_EK={EK} K3_VARK={varK} K3_COV_K_XE={c} K3_YDIAG={s}")
print(f"K3_SCHUR_SUFFICIENT_LHS={schur_lhs} K3_SCHUR_SUFFICIENT_RHS={s} HOLDS={schur_lhs >= s}")
print(f"TREE_M4_EXPECTED_CONDITIONAL_COV={mean_cond_cov}")
print(f"TREE_M4_SIZE_MIXING_COV={mix_cov}")
print(f"TREE_M4_TOTAL_COV={mean_cond_cov + mix_cov}")
