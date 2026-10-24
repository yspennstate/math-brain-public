#!/usr/bin/env python3
from fractions import Fraction

# R13 exact checker: 86-column refinement-forest Komlos obstruction.
# All acceptance decisions use integer/Fraction arithmetic.

Q = Fraction(22643, 10000)
OLD = Fraction(225925611947, 10**11)

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
424464,237673,425791,424463,240036,414396,240036,162804,160136,162803,
257027,175629,176389,114214,116017,176387,113232,113232,116017,114214,
181745,181745,124189,124189,124726,124726,80762,80762,82881,81184,
124725,124725,80067,80067,80067,80067,82881,81183,80761,80762,
128514,128514,128514,128514,87814,87814,87814,87814,88194,88194,
88194,88194,57107,57107,57107,57107,57786,57406,57406,88194,
88194,88194,88194,56617,56616,56616,56616,56616,56616,56616,
56616,57785,57405,57405,57107,57107,57107,57107,90873,90873,
90873,90873,90873,90873,90873,90873
]
assert len(W) == 86 and sum(W) == 10_000_000 and min(W) > 0

def template_from_row(row):
    return {j: (1 if a > 0 else -1) for j,a in enumerate(row) if a != 0}

def split_all(templates, next_col):
    out = []
    for T in templates:
        U = dict(T); U[next_col] = 1; out.append(U)
        U = dict(T); U[next_col] = -1; out.append(U)
        next_col += 1
    return out, next_col

base = [template_from_row(r) for r in M11]
t1, c = split_all(base, 11)
assert len(t1) == 22 and c == 22
t2, c = split_all(t1, c)
assert len(t2) == 44 and c == 44

# Third layer: leave exactly parents 12 and 29 unsplit; split the other 42.
skip = {12, 29}
final = []
for i,T in enumerate(t2):
    if i in skip:
        final.append(dict(T))
    else:
        U = dict(T); U[c] = 1; final.append(U)
        U = dict(T); U[c] = -1; final.append(U)
        c += 1

assert len(final) == 86
assert c == 86
assert sum(len(T) == 7 for T in final) == 42
assert sum(len(T) == 8 for T in final) == 44

# Two projective cylinders are compatible iff their signs agree up to one
# global sign on every common support coordinate.
def projectively_compatible(A, B):
    inter = set(A).intersection(B)
    if not inter:
        return True
    ratios = {A[j]*B[j] for j in inter}
    return len(ratios) <= 1

compatible_pairs = []
for i in range(86):
    for j in range(i+1,86):
        if projectively_compatible(final[i], final[j]):
            compatible_pairs.append((i,j))
assert compatible_pairs == []

# A support of size s occupies projective mass 2^{-(s-1)}.
kraft = sum(Fraction(1, 2**(len(T)-1)) for T in final)
assert kraft == 1

# Rational row normalization. For each row, choose magnitude proportional
# to W_j^{-1}; normalized row l1 mass is exactly 1.
loads = [Fraction(0,1) for _ in range(86)]
row_mass = []
for T in final:
    den = sum(Fraction(1, W[j]) for j in T)
    mass = Fraction(0,1)
    for j in T:
        x = Fraction(1, W[j]) / den
        mass += x
        loads[j] += x*x
    row_mass.append(mass)
assert all(m == 1 for m in row_mass)

max_load = max(loads)
worst_col = loads.index(max_load)
assert worst_col == 32

scaled_loads = [Q*Q*x for x in loads]
max_scaled = max(scaled_loads)
worst_scaled_col = scaled_loads.index(max_scaled)
assert worst_scaled_col == 32
slack = 1 - max_scaled
assert slack > 0

# The construction improves the preceding exact 86-column obstruction.
improvement = Q - OLD
assert improvement == Fraction(504388053, 10**11)
assert improvement > 0

# Kraft + pairwise incompatibility proves a projective partition; every sign
# class therefore fully aligns with exactly one row template. That row has
# signed magnitude Q because its normalized l1 mass is one.
print("R13 refinement-forest exact checker")
print("rows =", len(final))
print("columns =", c)
print("support_size_7 =", sum(len(T)==7 for T in final))
print("support_size_8 =", sum(len(T)==8 for T in final))
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
print("R13_REFINEMENT_FOREST_86_EXACT_PASS")
