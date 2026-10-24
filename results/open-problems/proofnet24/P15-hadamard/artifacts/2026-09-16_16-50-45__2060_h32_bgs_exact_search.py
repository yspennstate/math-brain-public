#!/usr/bin/env python3
"""Exact H32-multiplier-invariant bordered-Goethals-Seidel search for H(2060).

Target cyclic supplementary difference family in Z_514:
  block sizes (256,257,257,257), total ordered difference multiplicity 512
  at each nonzero shift.
Restriction: each block invariant under H=<393> <= Z_514^*, |H|=32.

The final meet-in-middle uses a linear hash modulo 2^64 as a necessary filter only.
If exact signatures satisfy A+B1+B2+B3=target, their hashes necessarily satisfy
h(A)+h(B1)+h(B2)+h(B3)=h(target) mod 2^64. Therefore zero hash matches is an
exact certificate of zero signature matches; hash collisions could only produce false
positives, never false negatives.
"""
from itertools import combinations
from collections import Counter
import math
import numpy as np

v=514
g=393
ALL=(1<<v)-1
H=[]
x=1
while x not in H:
    H.append(x)
    x=(x*g)%v
assert x==1 and len(H)==32 and all(math.gcd(h,v)==1 for h in H)

unseen=set(range(v))
orbits=[]
while unseen:
    a=min(unseen)
    O=frozenset((a*h)%v for h in H)
    orbits.append(O)
    unseen-=O
profile=Counter(map(len,orbits))
assert profile==Counter({32:16,1:2})
fixed=sorted(next(iter(O)) for O in orbits if len(O)==1)
assert fixed==[0,257]
large=[O for O in orbits if len(O)==32]
assert len(large)==16

shift_orbits=large+[frozenset({257})]
reps=[min(O) for O in shift_orbits]
assert len(reps)==17 and sum(map(len,shift_orbits))==513
large_masks=[sum(1<<a for a in O) for O in large]

def rotl(mask,t):
    t%=v
    return ((mask<<t)&ALL)|(mask>>(v-t)) if t else mask

def sig(mask):
    return tuple((mask & rotl(mask,(-t)%v)).bit_count() for t in reps)

combos=list(combinations(range(16),8))
assert len(combos)==12870
A=[]
B=[]
for I in combos:
    m=0
    for i in I:
        m|=large_masks[i]
    assert m.bit_count()==256
    A.append(m)
    B.append(m|(1<<fixed[0]))
    B.append(m|(1<<fixed[1]))
assert all(m.bit_count()==257 for m in B)

As=[sig(m) for m in A]
Bs=[sig(m) for m in B]
for mask,S in [(A[0],As[0]),(A[-1],As[-1]),(B[0],Bs[0]),(B[-1],Bs[-1])]:
    for j,O in enumerate(shift_orbits):
        vals={(mask & rotl(mask,(-t)%v)).bit_count() for t in O}
        assert vals=={S[j]}

Au=np.array(sorted(set(As)),dtype=np.int16)
Bu=np.array(sorted(set(Bs)),dtype=np.int16)
assert Au.shape==(6470,17)
assert Bu.shape==(6563,17)

# Linear hash modulo 2^64. Exact signature equality necessarily implies hash equality.
base=np.uint64(1315423911)
coeff=np.empty(17,dtype=np.uint64)
coeff[0]=np.uint64(1)
with np.errstate(over='ignore'):
    for j in range(1,17):
        coeff[j]=coeff[j-1]*base
    hA=(Au.astype(np.uint64)*coeff).sum(axis=1,dtype=np.uint64)
    hB=(Bu.astype(np.uint64)*coeff).sum(axis=1,dtype=np.uint64)
    hT=(np.full(17,512,dtype=np.uint64)*coeff).sum(dtype=np.uint64)

m=len(hB)
pair_count=m*(m+1)//2
pairs=np.empty(pair_count,dtype=np.uint64)
pos=0
with np.errstate(over='ignore'):
    for i in range(m):
        k=m-i
        pairs[pos:pos+k]=hB[i]+hB[i:]
        pos+=k
assert pos==pair_count==21539766
pairs.sort()

match=0
query_count=len(hA)*len(hB)
with np.errstate(over='ignore'):
    for ha in hA:
        needs=np.subtract(np.subtract(hT,ha,dtype=np.uint64),hB,dtype=np.uint64)
        idx=np.searchsorted(pairs,needs)
        good=idx<len(pairs)
        ids=np.nonzero(good)[0]
        if ids.size:
            match += sum(1 for ii in ids if pairs[idx[ii]]==needs[ii])
assert query_count==42462610 and match==0

print('target_order=2060')
print('cyclic_length_v=',v)
print('multiplier_generator=',g)
print('multiplier_subgroup_order=',len(H))
print('orbit_profile=',dict(sorted(profile.items())))
print('fixed_points=',fixed)
print('nonzero_shift_orbits=',len(shift_orbits))
print('A_candidate_count=',len(A))
print('B_candidate_count=',len(B))
print('unique_A_signature_count=',len(Au))
print('unique_B_signature_count=',len(Bu))
print('B_pair_hash_count=',pair_count)
print('A_times_B_hash_queries=',query_count)
print('hash_match_count=',match)
print('solution_count=0')
print('PROVED: no H32-invariant cyclic BGS difference family (514;256,257,257,257;512)')
print('SCOPE: restricted-family nonexistence only; says nothing about unrestricted H(2060) existence')
