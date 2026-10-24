#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter

# R13 exact checker: 86-column tie-broken shallow-refinement Komlos obstruction.
# All theorem-acceptance decisions use exact integer/Fraction arithmetic.

Q = Fraction(22647288, 10_000_000)
OLD = Fraction(452931, 200000)
COUNTS = (11,11,6,5,11,5,5,5,5,11,11)
SPLIT_CHOICES = [[0, 1, 0, 1, 3, 5, 0, 7, 4, 2], [0, 1, 0, 3, 0, 3, 2, 1, 4, 7], [0, 0, 2, 2, 0], [0, 0, 2, 2], [0, 1, 0, 2, 0, 5, 2, 7, 5, 3], [0, 0, 2, 1], [0, 0, 2, 0], [0, 1, 0, 0], [0, 1, 0, 3], [0, 0, 2, 3, 0, 2, 4, 0, 4, 9], [0, 1, 0, 3, 1, 0, 4, 1, 8, 6]]

M11 = [
[-41498232,73852706,0,-41498232,0,-42638879,0,0,0,0,0],
[41498232,0,41498232,0,73852706,-42638879,0,0,0,0,0],
[0,0,-26788739,26788739,0,-27525072,47674824,70710678,0,0,0],
[0,0,-26788739,26788739,0,-27525072,47674824,-70710678,0,0,0],
[0,0,-41498232,41498232,0,-42638879,-73852706,0,0,0,0],
[26788739,47674824,0,26788739,0,27525072,0,0,70710678,0,0],
[26788739,47674824,0,26788739,0,27525072,0,0,-70710678,0,0],
[-26788739,0,-26788739,0,47674824,27525072,0,0,0,70710678,0],
[-26788739,0,-26788739,0,47674824,27525072,0,0,0,-70710678,0],
[-42925791,0,42925791,42925791,0,0,0,0,0,0,70710678],
[-42925791,0,42925791,42925791,0,0,0,0,0,0,-70710678],
]

W = [42029287, 24346305, 41889073, 41889073, 24346305, 42029287, 24103469, 17043719, 17311882, 17311882, 24103469, 17118463, 12013870, 12194617, 8536527, 8495089, 8495089, 8708411, 5923113, 5923113, 5952004, 17118463, 12194617, 12013870, 8708411, 8495089, 8536527, 8495089, 5923113, 5923113, 5952004, 11961414, 8457997, 8457997, 5897250, 5897250, 12141372, 8670389, 8499254, 5926014, 17043719, 11961414, 12141372, 8457997, 8670389, 8457997, 8499254, 5897250, 5897250, 5926014, 12241349, 8569242, 8741781, 5974815, 12241349, 8569242, 8741781, 5974815, 12241349, 8741781, 8569242, 5974815, 12241349, 8569242, 8741781, 5974815, 17043719, 11961414, 12141372, 8499254, 8457997, 8457997, 8670389, 5897250, 5897250, 5926014, 17043719, 11961414, 12141372, 8457997, 8670389, 8499254, 8457997, 5926014, 5897250, 5897250]

assert len(W) == 86 and min(W) > 0
assert len(COUNTS) == 11 and sum(COUNTS) == 86
assert len(SPLIT_CHOICES) == 11
assert all(len(ch) == k-1 for ch,k in zip(SPLIT_CHOICES, COUNTS))

def template_from_row(row):
    return {j: (1 if a > 0 else -1) for j,a in enumerate(row) if a != 0}

def refine_by_choices(T, leaf_count, choices, next_col):
    leaves = [(dict(T), 0)]
    for step, idx in enumerate(choices):
        min_depth = min(d for _,d in leaves)
        assert leaves[idx][1] == min_depth
        parent, depth = leaves.pop(idx)
        col = next_col
        next_col += 1
        plus = dict(parent); plus[col] = 1
        minus = dict(parent); minus[col] = -1
        leaves.insert(idx, (plus, depth + 1))
        leaves.insert(idx + 1, (minus, depth + 1))
    assert len(leaves) == leaf_count
    return [T for T,_ in leaves], [d for _,d in leaves], next_col

base = [template_from_row(r) for r in M11]
final = []
depths = []
c = 11
for T,k,ch in zip(base, COUNTS, SPLIT_CHOICES):
    leaves, ds, c = refine_by_choices(T, k, ch, c)
    final.extend(leaves)
    depths.extend(ds)

assert len(final) == 86 and c == 86
assert Counter(depths) == Counter({3:39,4:30,2:17})
assert Counter(len(T) for T in final) == Counter({8:44,7:42})

def projectively_compatible(A, B):
    inter = set(A).intersection(B)
    if not inter:
        return True
    ratios = {A[j] * B[j] for j in inter}
    return len(ratios) <= 1

compatible_pairs = []
for i in range(86):
    for j in range(i+1,86):
        if projectively_compatible(final[i], final[j]):
            compatible_pairs.append((i,j))
assert compatible_pairs == []

kraft = sum(Fraction(1, 2**(len(T)-1)) for T in final)
assert kraft == 1

loads = [Fraction(0,1) for _ in range(86)]
for T in final:
    S = sorted(T)
    den = sum(Fraction(1, W[j]) for j in S)
    row_mass = Fraction(0,1)
    for j in S:
        x = Fraction(1, W[j]) / den
        row_mass += x
        loads[j] += x*x
    assert row_mass == 1

max_load = max(loads)
worst_col = loads.index(max_load)
scaled = [Q*Q*x for x in loads]
max_scaled = max(scaled)
worst_scaled_col = scaled.index(max_scaled)
slack = 1 - max_scaled
assert slack > 0

improvement = Q - OLD
assert improvement == Fraction(369, 5_000_000)
assert improvement > 0

print("R13 tie-broken shallow-refinement exact checker")
print("rows =", len(final))
print("columns =", c)
print("base_leaf_counts =", COUNTS)
print("refinement_depth_distribution =", dict(sorted(Counter(depths).items())))
print("support_size_distribution =", dict(sorted(Counter(len(T) for T in final).items())))
print("projectively_compatible_pairs =", len(compatible_pairs))
print("kraft =", kraft)
print("weight_sum =", sum(W))
print("worst_normalized_load_column =", worst_col)
print("worst_normalized_load_decimal =", float(max_load))
print("worst_scaled_column_norm_sq_decimal =", float(max_scaled))
print("exact_scaled_slack_positive =", slack > 0)
print("scaled_slack_decimal =", float(slack))
print("new_lower_bound =", f"{Q.numerator}/{Q.denominator}", float(Q))
print("old_lower_bound =", f"{OLD.numerator}/{OLD.denominator}", float(OLD))
print("exact_improvement =", f"{improvement.numerator}/{improvement.denominator}", float(improvement))
print("R13_TIEBROKEN_SHALLOW_86_EXACT_PASS")
