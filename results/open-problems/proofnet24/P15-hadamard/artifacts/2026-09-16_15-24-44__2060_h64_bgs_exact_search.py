#!/usr/bin/env python3
"""Exact exhaustion of an H64-multiplier-invariant bordered GS family for order 2060.

Target: a cyclic supplementary difference family in Z_514 with block sizes
(256,257,257,257) and total ordered difference multiplicity 512 at every
nonzero shift. Such a family would yield a bordered Goethals-Seidel Hadamard
matrix of order 4*(514+1)=2060.

Restriction certified here: every block is invariant under multiplication by
the order-64 subgroup H=<81> of Z_514^*. This is ONLY a restricted-family
nonexistence theorem, not nonexistence of H(2060).

All calculations use Python integers and exact set membership.
"""
from itertools import combinations, combinations_with_replacement
from collections import Counter
import math

v = 514
g = 81  # 3^4 mod 257; odd lift to Z_514

H = []
x = 1
while x not in H:
    H.append(x)
    x = (x*g) % v
assert x == 1
assert len(H) == 64
assert all(math.gcd(h, v) == 1 for h in H)

unseen = set(range(v))
orbits = []
while unseen:
    a = min(unseen)
    O = {(a*h) % v for h in H}
    orbits.append(tuple(sorted(O)))
    unseen -= O
profile = Counter(map(len, orbits))
assert profile == Counter({64: 8, 1: 2})
fixed = sorted(O[0] for O in orbits if len(O) == 1)
assert fixed == [0,257]
large = [frozenset(O) for O in orbits if len(O) == 64]
assert len(large) == 8

shift_orbits = [O for O in large] + [frozenset({257})]
shift_reps = [min(O) for O in shift_orbits]
assert len(shift_reps) == 9
assert sum(len(O) for O in shift_orbits) == 513

A_candidates = [frozenset().union(*(large[i] for i in I)) for I in combinations(range(8),4)]
B_candidates = []
for I in combinations(range(8),4):
    core = frozenset().union(*(large[i] for i in I))
    for f in fixed:
        B_candidates.append(core | {f})
assert len(A_candidates) == 70 and all(len(X)==256 for X in A_candidates)
assert len(B_candidates) == 140 and all(len(X)==257 for X in B_candidates)

def nu(X,t):
    return sum(1 for x in X if ((x+t) % v) in X)

def sig(X):
    return tuple(nu(X,t) for t in shift_reps)

A_sigs = [sig(X) for X in A_candidates]
B_sigs = [sig(X) for X in B_candidates]

for X in A_candidates[:3] + B_candidates[:3]:
    s = sig(X)
    for j,O in enumerate(shift_orbits):
        vals = {nu(X,t) for t in O}
        assert vals == {s[j]}

pair_sums = {}
for i,j in combinations_with_replacement(range(len(B_sigs)),2):
    s = tuple(B_sigs[i][k] + B_sigs[j][k] for k in range(9))
    pair_sums.setdefault(s, (i,j))

target = (512,)*9
solution = None
for ia,sa in enumerate(A_sigs):
    for ib,sb in enumerate(B_sigs):
        need = tuple(target[k]-sa[k]-sb[k] for k in range(9))
        if need in pair_sums:
            ic,id_ = pair_sums[need]
            solution = (ia,ib,ic,id_)
            break
    if solution is not None:
        break

assert solution is None
print('target_order=2060')
print('cyclic_length_v=', v)
print('multiplier_generator=', g)
print('multiplier_subgroup_order=', len(H))
print('orbit_profile=', dict(sorted(profile.items())))
print('fixed_points=', fixed)
print('nonzero_shift_orbits=', len(shift_orbits))
print('X1_candidate_count=', len(A_candidates))
print('X257_candidate_count=', len(B_candidates))
print('distinct_B_plus_B_signatures=', len(pair_sums))
print('solution_count=0')
print('PROVED: no H64-invariant cyclic BGS difference family (514;256,257,257,257;512)')
print('SCOPE: restricted-family nonexistence only; says nothing about unrestricted H(2060) existence')
