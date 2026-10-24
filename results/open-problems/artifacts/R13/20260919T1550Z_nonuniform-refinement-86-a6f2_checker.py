#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter

# R13 exact checker: 86-column nonuniform refinement-forest Komlos obstruction.
# All acceptance decisions use exact integer/Fraction arithmetic.

Q = Fraction(2264655, 10**6)
OLD = Fraction(22643, 10000)
COUNTS = (11,11,6,5,11,5,5,5,5,11,11)

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

W = [
42076713,24372509,41937194,41937194,24372509,42075364,24130843,17062139,
17329006,17329006,24133197,17138402,11844658,12386641,8288568,8461417,
8758680,8758680,5860903,5860903,5899591,17138402,11844658,12386641,
8288568,8461417,8758680,8758680,5860903,5860903,5899591,11974883,
8294008,8637550,5864749,5864749,12153964,8508023,8679428,5932085,
17064021,11793244,12332886,8252592,8424694,8720671,8720671,5835464,
5835464,5873986,12253457,8577669,8750477,5980644,12253456,8577669,
8750477,5980645,12253456,8577669,8750477,5980644,12253456,8577669,
8750477,5980645,17064750,11793754,12333409,8252949,8425055,8721038,
8721038,5835715,5835715,5874237,17064750,11793754,12333409,8252948,
8425055,8721038,8721038,5835716,5835716,5874238
]
assert len(W) == 86 and min(W) > 0 and sum(W) == 1_000_000_001
assert len(COUNTS) == 11 and sum(COUNTS) == 86


def template_from_row(row):
    return {j: (1 if a > 0 else -1) for j,a in enumerate(row) if a != 0}


def refine_breadth_first(T, leaf_count, next_col):
    # Repeatedly split the shallowest current leaf; ties are broken by current order.
    # A split replaces one cylinder by its two children and uses one fresh coordinate.
    leaves = [(dict(T), 0)]
    for _ in range(leaf_count - 1):
        idx = min(range(len(leaves)), key=lambda i: (leaves[i][1], i))
        parent, depth = leaves.pop(idx)
        col = next_col
        next_col += 1
        plus = dict(parent); plus[col] = 1
        minus = dict(parent); minus[col] = -1
        leaves.insert(idx, (plus, depth + 1))
        leaves.insert(idx + 1, (minus, depth + 1))
    return [T for T,_ in leaves], [d for _,d in leaves], next_col

base = [template_from_row(r) for r in M11]
final = []
depths = []
c = 11
for T,k in zip(base, COUNTS):
    leaves, ds, c = refine_breadth_first(T, k, c)
    final.extend(leaves)
    depths.extend(ds)

assert len(final) == 86
assert c == 86
assert Counter(len(T) for T in final) == Counter({8:44, 7:42})
assert Counter(depths) == Counter({3:39, 4:30, 2:17})


def projectively_compatible(A, B):
    inter = set(A).intersection(B)
    if not inter:
        return True
    ratios = {A[j] * B[j] for j in inter}
    return len(ratios) <= 1

compatible_pairs = []
for i in range(86):
    for j in range(i+1, 86):
        if projectively_compatible(final[i], final[j]):
            compatible_pairs.append((i,j))
assert compatible_pairs == []

# A support of size s occupies projective mass 2^{-(s-1)}.
kraft = sum(Fraction(1, 2**(len(T)-1)) for T in final)
assert kraft == 1

# For each final support S_i, choose normalized positive row magnitudes
# x_ij proportional to 1/W_j. Each row has exact l1 mass one.
loads = [Fraction(0,1) for _ in range(86)]
for T in final:
    S = sorted(T)
    den = sum(Fraction(1, W[j]) for j in S)
    mass = Fraction(0,1)
    for j in S:
        x = Fraction(1, W[j]) / den
        mass += x
        loads[j] += x*x
    assert mass == 1

max_load = max(loads)
worst_col = loads.index(max_load)
scaled = [Q*Q*x for x in loads]
max_scaled = max(scaled)
worst_scaled_col = scaled.index(max_scaled)
slack = 1 - max_scaled
assert worst_col == 41
assert worst_scaled_col == 41
assert slack > 0

improvement = Q - OLD
assert improvement == Fraction(71, 200000)
assert improvement > 0

# Pairwise projective incompatibility plus total projective mass one proves
# that the 86 cylinders partition all projective Boolean sign classes.
# Hence every Boolean signing fully aligns, up to global sign, with exactly
# one row. Since every normalized row has l1 mass one, scaling by Q gives
# discrepancy at least Q for every signing, while the exact load test above
# proves all column Euclidean norms are < 1.

print("R13 nonuniform refinement-forest exact checker")
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
print("R13_NONUNIFORM_REFINEMENT_86_EXACT_PASS")
