#!/usr/bin/env python3
"""Independent exact audit of P15-H64-BGS-2060-NEG-01.

Unlike the P15 checker, this audit does not compress difference counts to nine
shift-orbits. It recomputes the full 513-coordinate ordered-difference signature
for every H-invariant candidate and performs the exact meet-in-the-middle test.
"""
from itertools import combinations, combinations_with_replacement
from collections import Counter
import math

v=514; g=81
H=[]; x=1
while x not in H:
    H.append(x); x=(x*g)%v
assert x==1 and len(H)==64 and all(math.gcd(h,v)==1 for h in H)

unseen=set(range(v)); orbits=[]
while unseen:
    a=min(unseen); O=frozenset((a*h)%v for h in H)
    orbits.append(O); unseen-=O
profile=Counter(map(len,orbits))
assert profile==Counter({64:8,1:2})
fixed=sorted(next(iter(O)) for O in orbits if len(O)==1)
large=[O for O in orbits if len(O)==64]
assert fixed==[0,257] and len(large)==8

A=[frozenset().union(*(large[i] for i in I)) for I in combinations(range(8),4)]
B=[]
for I in combinations(range(8),4):
    core=frozenset().union(*(large[i] for i in I))
    for f in fixed: B.append(core|{f})
assert len(A)==70 and len(B)==140

def fullsig(X):
    # 513 actual nonzero shifts, no orbit compression.
    return tuple(sum(1 for x in X if ((x+t)%v) in X) for t in range(1,v))

AS=[fullsig(X) for X in A]
BS=[fullsig(X) for X in B]
pair_sums=set()
for i,j in combinations_with_replacement(range(len(BS)),2):
    pair_sums.add(tuple(a+b for a,b in zip(BS[i],BS[j])))

target=(512,)*(v-1)
hits=[]
for ia,sa in enumerate(AS):
    for ib,sb in enumerate(BS):
        need=tuple(t-a-b for t,a,b in zip(target,sa,sb))
        if need in pair_sums: hits.append((ia,ib))

assert not hits
print('audit_claim=P15-H64-BGS-2060-NEG-01')
print('modulus=',v)
print('H_order=',len(H))
print('orbit_profile=',dict(sorted(profile.items())))
print('fixed_points=',fixed)
print('A_candidates=',len(A))
print('B_candidates=',len(B))
print('signature_coordinates=',v-1)
print('distinct_full_pair_sums=',len(pair_sums))
print('solution_hits=',len(hits))
print('AUDIT PASS: no H64-invariant cyclic BGS family in the stated restricted scope')
