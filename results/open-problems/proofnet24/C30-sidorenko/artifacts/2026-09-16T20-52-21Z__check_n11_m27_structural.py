#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import comb

# Exact certificate for C30's structural n=11, m=27 theorem.
# H = K_{5,5} \ C_10 has 10 vertices and 15 edges.
# The theorem proved in the companion report is:
#   hom(H,G) * 11^20 >= 54^15
# for every simple 11-vertex graph G with 27 edges.
#
# This checker validates the finite algebra/combinatorics used by the proof.
# It is not a substitute for the written combinatorial argument.

# Binary cyclic-word classification used for the exact two-symbol contribution.
types = {}
for w in product((0, 1), repeat=5):
    if len(set(w)) < 2:
        continue
    na = nb = nm = 0
    for i in range(5):
        tri = (w[i], w[(i+1) % 5], w[(i+2) % 5])
        if tri == (0, 0, 0):
            na += 1
        elif tri == (1, 1, 1):
            nb += 1
        else:
            nm += 1
    types[(na, nb, nm)] = types.get((na, nb, nm), 0) + 1

expected_types = {
    (0, 0, 5): 10,
    (2, 0, 3): 5,
    (1, 0, 4): 5,
    (0, 1, 4): 5,
    (0, 2, 3): 5,
}
assert types == expected_types
assert sum(types.values()) == 30

# Low-degree deletion branch.
rhs = Fraction(10, 11) ** 20
deletion_ratios = {}
for d in range(4):
    ratio = (Fraction(27-d, 27) ** 15) / rhs
    deletion_ratios[d] = ratio
    assert ratio > 1
assert deletion_ratios[3] == Fraction(
    22573743957964929414654328832,
    19635308465447330474853515625,
)

# Pairwise lower envelope when delta(G) >= 4.
def F(c):
    q = max(4, c)
    return 10*c**5 + 10*q*c**4 + 10*q*q*c**3

F_values = [F(c) for c in range(11)]
increments = [F_values[c] - F_values[c-1] for c in range(1, 11)]
assert F_values[:5] == [0, 210, 2240, 9990, 30720]
assert all(increments[i] >= increments[i-1] for i in range(1, len(increments)))

INF = 10**100

# Independent DP verification of the balanced degree minima:
# 11 integer degrees in [4,10], total degree 54.
dp_pow5 = {(0, 0): 0}
for _ in range(11):
    nxt = {}
    for (k, s), val in dp_pow5.items():
        for d in range(4, 11):
            key = (k+1, s+d)
            nxt[key] = min(nxt.get(key, INF), val + d**5)
    dp_pow5 = nxt
min_degree_fifth_sum = dp_pow5[(11, 54)]
assert min_degree_fifth_sum == 32274

dp_choose2 = {(0, 0): 0}
for _ in range(11):
    nxt = {}
    for (k, s), val in dp_choose2.items():
        for d in range(4, 11):
            key = (k+1, s+d)
            nxt[key] = min(nxt.get(key, INF), val + comb(d, 2))
    dp_choose2 = nxt
min_total_codegree = dp_choose2[(11, 54)]
assert min_total_codegree == 106

# Independent DP verification of the pair-envelope minimum:
# 55 unordered vertex pairs, integer codegrees in [0,10],
# total codegree at least 106. Since F is increasing it suffices to use 106.
dp = {0: 0}
for _ in range(comb(11, 2)):
    nxt = {}
    for s, val in dp.items():
        for c in range(11):
            if s + c <= 106:
                nv = val + F(c)
                if nv < nxt.get(s+c, INF):
                    nxt[s+c] = nv
    dp = nxt
min_pair_sum = dp[106]
assert min_pair_sum == 115080
assert min_pair_sum == 51*F(2) + 4*F(1)

# Source-normalized exact threshold and final margin.
target_num = 54**15
target_den = 11**20
target_ceiling = (target_num + target_den - 1) // target_den
assert target_ceiling == 143898

lower_bound = min_degree_fifth_sum + min_pair_sum
assert lower_bound == 147354
assert lower_bound > target_ceiling
cross_margin = lower_bound * target_den - target_num
assert cross_margin == 2325483985034728958670330
assert cross_margin > 0

print("H_vertices=10")
print("H_edges=15")
print("host_vertices=11")
print("host_edges=27")
print("binary_word_count=30")
print("binary_word_types=", sorted(types.items()))
print("deletion_d3_ratio=", deletion_ratios[3])
print("F_values_0_to_10=", F_values)
print("F_increments_1_to_10=", increments)
print("min_degree_fifth_sum=", min_degree_fifth_sum)
print("min_total_codegree=", min_total_codegree)
print("min_pair_envelope_sum=", min_pair_sum)
print("source_threshold_ceiling=", target_ceiling)
print("structural_lower_bound=", lower_bound)
print("integer_margin=", lower_bound - target_ceiling)
print("cross_multiplication_margin=", cross_margin)
print("ALL_EXACT_CHECKS_PASS")
