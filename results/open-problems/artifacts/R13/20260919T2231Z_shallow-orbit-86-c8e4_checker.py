#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from collections import Counter
from decimal import Decimal, getcontext

getcontext().prec = 50

# R13 exact checker: rooted-tree quotient for the shallow 11-cylinder refinement
# plus a stronger explicit 86-column Boolean-Komlos obstruction.

OLD = Fraction(2830911, 1250000)         # 2.2647288
Q = Fraction(226472999, 100000000)       # 2.26472999
COUNTS = (11,11,6,5,11,5,5,5,5,11,11)

# Only the signs/supports of this exact 11-cylinder base are used.
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

# Integer column prices for the exact primal certificate below.
W = [
42029304774,24346311988,41889094014,41889094014,24346311988,42029304774,
24103457116,17043717977,17311882583,17311882583,24103457116,
17118458717,12194612209,12013869564,8536520935,8708408423,8495088637,
8495088637,5952000757,5923112517,5923112517,17118458717,12194612209,
12013869564,8536520935,8708408423,8495088637,8495088637,5952000757,
5923112517,5923112517,11961415923,8457998311,8457998311,5897251672,
5897251672,12141369429,8499249712,8670386724,5926013784,17043717977,
12141369429,11961415923,8499249712,8670386724,8457998311,8457998311,
5926013784,5897251672,5897251672,12241349570,8569238208,8741784476,
5974812537,12241349570,8569238208,8741784476,5974812537,12241349570,
8569238208,8741784476,5974812537,12241349570,8569238208,8741784476,
5974812537,17043717977,12141369429,11961415923,8499249712,8670386724,
8457998311,8457998311,5926013784,5897251672,5897251672,17043717977,
12141369429,11961415923,8499249712,8670386724,8457998311,8457998311,
5926013784,5897251672,5897251672]
assert len(W) == 86 and min(W) > 0
assert sum(COUNTS) == 86


def tree_aut_perms(depth):
    """Exact leaf permutations induced by automorphisms of complete rooted binary T_depth."""
    if depth == 0:
        return [(0,)]
    sub = tree_aut_perms(depth-1)
    h = 1 << (depth-1)
    out = []
    for p in sub:
        for q in sub:
            out.append(tuple(p[i] for i in range(h)) + tuple(h+q[i] for i in range(h)))
            out.append(tuple(h+q[i] for i in range(h)) + tuple(p[i] for i in range(h)))
    out = list(dict.fromkeys(out))
    return out


def subset_orbits(depth, r):
    n = 1 << depth
    G = tree_aut_perms(depth)
    unseen = set(combinations(range(n), r))
    orbits = []
    while unseen:
        S = min(unseen)
        orb = {tuple(sorted(p[i] for i in S)) for p in G}
        unseen -= orb
        orbits.append((min(orb), len(orb), frozenset(orb)))
    orbits.sort(key=lambda z: z[0])
    return orbits

G2 = tree_aut_perms(2)
G3 = tree_aut_perms(3)
assert len(G2) == 8
assert len(G3) == 128
O5 = subset_orbits(2,1)
O6 = subset_orbits(2,2)
O11 = subset_orbits(3,3)
assert len(O5) == 1 and sorted(x[1] for x in O5) == [4]
assert len(O6) == 2 and sorted(x[1] for x in O6) == [2,4]
assert len(O11) == 3 and sorted(x[1] for x in O11) == [8,16,32]
GLOBAL_CLASSES = len(O11)**5 * len(O6) * len(O5)**5
assert GLOBAL_CLASSES == 486

shape_orbit_counts = []
for k in range(1,17):
    d = k.bit_length()-1
    r = k - (1<<d)
    shape_orbit_counts.append(1 if r == 0 else len(subset_orbits(d,r)))
assert shape_orbit_counts == [1,1,1,1,1,2,1,1,1,3,3,5,3,3,1,1]

REP11 = (0,5,7)
REP6 = (0,2)
REP5 = (0,)
assert any(REP11 in o[2] for o in O11)
assert any(REP6 in o[2] for o in O6)


def template_from_row(row):
    return {j: (1 if a > 0 else -1) for j,a in enumerate(row) if a != 0}


def refine_canonical(T, k, extra_choice, next_col):
    d = k.bit_length()-1
    leaves = [dict(T)]
    for _ in range(d):
        new = []
        for parent in leaves:
            col = next_col; next_col += 1
            plus = dict(parent); plus[col] = 1
            minus = dict(parent); minus[col] = -1
            new.extend([plus, minus])
        leaves = new
    r = k - (1<<d)
    assert len(extra_choice) == r
    if r:
        selected = set(extra_choice)
        new = []
        for idx,parent in enumerate(leaves):
            if idx in selected:
                col = next_col; next_col += 1
                plus = dict(parent); plus[col] = 1
                minus = dict(parent); minus[col] = -1
                new.extend([plus,minus])
            else:
                new.append(parent)
        leaves = new
    assert len(leaves) == k
    return leaves, next_col


def projectively_compatible(A,B):
    inter = set(A).intersection(B)
    if not inter:
        return True
    ratios = {A[j]*B[j] for j in inter}
    return len(ratios) <= 1

base = [template_from_row(r) for r in M11]
for i,j in combinations(range(11),2):
    assert not projectively_compatible(base[i],base[j])
assert sum(Fraction(1,2**(len(T)-1)) for T in base) == 1

reps11 = [o[0] for o in O11]
reps6 = [o[0] for o in O6]
checked_classes = 0
for combo11 in product(range(3), repeat=5):
    for idx6 in range(2):
        final=[]; c=11; p11=0
        for T,k in zip(base,COUNTS):
            if k==11:
                choice=reps11[combo11[p11]]; p11+=1
            elif k==6:
                choice=reps6[idx6]
            else:
                choice=REP5
            leaves,c=refine_canonical(T,k,choice,c)
            final.extend(leaves)
        assert c==86 and len(final)==86
        assert Counter(len(T) for T in final)==Counter({7:42,8:44})
        assert sum(Fraction(1,2**(len(T)-1)) for T in final)==1
        for i,j in combinations(range(86),2):
            assert not projectively_compatible(final[i],final[j])
        checked_classes += 1
assert checked_classes == GLOBAL_CLASSES

final=[]; c=11
for T,k in zip(base,COUNTS):
    choice = REP11 if k==11 else REP6 if k==6 else REP5
    leaves,c=refine_canonical(T,k,choice,c)
    final.extend(leaves)
assert len(final)==86 and c==86
assert Counter(len(T) for T in final)==Counter({7:42,8:44})
assert sum(Fraction(1,2**(len(T)-1)) for T in final)==1
for i,j in combinations(range(86),2):
    assert not projectively_compatible(final[i],final[j])

loads=[Fraction(0,1) for _ in range(86)]
for T in final:
    S=sorted(T)
    den=sum(Fraction(1,W[j]) for j in S)
    row_mass=Fraction(0,1)
    for j in S:
        x=Fraction(1,W[j])/den
        row_mass += x
        loads[j] += x*x
    assert row_mass == 1
scaled=[Q*Q*x for x in loads]
max_scaled=max(scaled)
worst_col=scaled.index(max_scaled)
slack=1-max_scaled
assert slack>0
improvement=Q-OLD
assert improvement==Fraction(119,100000000)
assert improvement>0

def dec(fr):
    return Decimal(fr.numerator)/Decimal(fr.denominator)

print('R13_SHALLOW_ORBIT_86_EXACT_PASS')
print('Aut_T2_size =',len(G2))
print('Aut_T3_size =',len(G3))
print('k5_orbits =',len(O5),'orbit_sizes =',sorted(x[1] for x in O5))
print('k6_orbits =',len(O6),'orbit_sizes =',sorted(x[1] for x in O6))
print('k11_orbits =',len(O11),'orbit_sizes =',sorted(x[1] for x in O11))
print('shape_orbit_counts_k1_to_k16 =',shape_orbit_counts)
print('global_fixed_count_topology_classes =',GLOBAL_CLASSES)
print('global_classes_exactly_checked =',checked_classes)
print('canonical_support_distribution =',dict(sorted(Counter(len(T) for T in final).items())))
print('canonical_kraft =',sum(Fraction(1,2**(len(T)-1)) for T in final))
print('canonical_projectively_compatible_pairs = 0')
print('worst_scaled_column =',worst_col)
print('worst_scaled_column_norm_sq =',dec(max_scaled))
print('exact_scaled_slack_positive =',slack>0)
print('scaled_slack =',dec(slack))
print('old_lower_bound =',OLD,float(OLD))
print('new_lower_bound =',Q,float(Q))
print('exact_improvement =',improvement,float(improvement))
