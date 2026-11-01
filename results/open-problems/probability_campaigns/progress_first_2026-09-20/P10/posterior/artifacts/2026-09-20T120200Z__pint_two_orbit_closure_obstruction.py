#!/usr/bin/env python3
"""Rigorous obstruction to a two-orbit fixed-law ansatz containing the explicit P10 interior seed at lambda=353/500."""
import itertools
import mpmath as mp
mp.mp.dps=80
iv=mp.iv
ONE=iv.mpf(1); THIRD=ONE/3
s2=iv.sqrt(2); s6=iv.sqrt(6)
lam=iv.mpf(353)/500
p=[(ONE+(s6+s2)/4)/3,
   (ONE+(s2-s6)/4)/3,
   (ONE-s2/2)/3]
perms=list(itertools.permutations(range(3)))

def T(v):
    return [THIRD+lam*(x-THIRD) for x in v]

r=T(p)
vals=[]
for perm in perms:
    s=T([p[i] for i in perm])
    Z=sum((r[i]*s[i] for i in range(3)),iv.mpf(0))
    post=[r[i]*s[i]/Z for i in range(3)]
    S2=sum(((x-THIRD)**2 for x in post),iv.mpf(0))
    vals.append((perm,3*Z,S2))
for row in vals:
    print(row)

# The two 3-cycles are one output S3 orbit.  The other four classes have
# pairwise-disjoint S2 intervals, and S2 is an S3-orbit invariant.
groups=[0,1,2,3,5]
ints=[vals[i][2] for i in groups]
assert not (vals[3][2].b < vals[4][2].a or vals[4][2].b < vals[3][2].a)
for i in range(len(ints)):
    for j in range(i+1,len(ints)):
        assert ints[i].b < ints[j].a or ints[j].b < ints[i].a
print('FIVE_DISTINCT_OUTPUT_ORBITS_PASS')
print('OVERALL_PASS')
