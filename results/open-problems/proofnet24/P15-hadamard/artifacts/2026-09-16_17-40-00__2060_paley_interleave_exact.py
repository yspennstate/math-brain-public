#!/usr/bin/env python3
"""Exact restricted Paley/Legendre interleaving search for H(2060).

For v=514, associate to a subset X the sign sequence a=1-2*1_X.
The bordered Goethals--Seidel SDS target
    (514;256,257,257,257;512)
is equivalent to sign-sequence sums (2,0,0,0) and
    sum_i PAF_i(t) = -4  for every nonzero t mod 514.

Let p=257.  L is the +1-at-zero Legendre sequence and M_j=L_{3j},
where 3 is a quadratic nonresidue.  This script exhausts the family in
which each length-514 sequence is obtained by interleaving cyclic shifts
of multiplicative decimations of L.  Since every decimation is either L
or M, and a common shift of both halves does not change periodic
autocorrelation, it suffices to take P,Q in {L,M} and a relative shift d.
The size-256 block has I(P,+shift_d Q); the three size-257 blocks have
I(P,-shift_d Q), up to global negation (which preserves PAF).

All autocorrelations and comparisons use NumPy int64/int16 integer
arithmetic.  Values are bounded by 514, so there is no overflow.  The
bytes keys are an exact serialization of int16 signatures; dictionary
hash collisions are resolved by Python key equality and cannot change
membership.
"""
from collections import Counter
import numpy as np

P=257
N=514

def chi(j):
    if j % P == 0:
        return 1
    e=pow(j % P,(P-1)//2,P)
    assert e in (1,P-1)
    return 1 if e==1 else -1

L=np.array([chi(j) for j in range(P)],dtype=np.int64)
assert pow(3,(P-1)//2,P)==P-1
M=np.array([L[(3*j)%P] for j in range(P)],dtype=np.int64)
assert int(L.sum())==int(M.sum())==1

def paf(a):
    a=np.asarray(a,dtype=np.int64)
    out=np.array([np.dot(a,np.roll(a,-t)) for t in range(len(a))],dtype=np.int64)
    assert np.max(np.abs(out)) <= len(a)
    return out

pL,pM=paf(L),paf(M)
assert np.all(pL[1:]+pM[1:]==-2)

def inter(P0,Q0,sign):
    a=np.empty(N,dtype=np.int64)
    a[0::2]=P0
    a[1::2]=sign*Q0
    return a

bases=(L,M)
A={}
B={}
rawA=rawB=0
for pt,P0 in enumerate(bases):
    for qt,Q0 in enumerate(bases):
        for d in range(P):
            Q=np.roll(Q0,-d)
            aa=inter(P0,Q,+1)
            bb=inter(P0,Q,-1)
            assert int(aa.sum())==2 and int(bb.sum())==0
            sa=paf(aa)[1:].astype(np.int16)
            sb=paf(bb)[1:].astype(np.int16)
            A.setdefault(sa.tobytes(),(pt,qt,d))
            B.setdefault(sb.tobytes(),(pt,qt,d))
            rawA += 1
            rawB += 1

Avec=[(np.frombuffer(k,dtype=np.int16).copy(),m) for k,m in A.items()]
Bvec=[(np.frombuffer(k,dtype=np.int16).copy(),m) for k,m in B.items()]

BB={}
raw_pairs=0
for i,(x,_) in enumerate(Bvec):
    for j in range(i,len(Bvec)):
        s=(x.astype(np.int32)+Bvec[j][0].astype(np.int32)).astype(np.int16)
        BB.setdefault(s.tobytes(),(i,j))
        raw_pairs += 1

target=np.full(N-1,-4,dtype=np.int32)
probes=0
witness=None
for ia,(a,ma) in enumerate(Avec):
    for ib,(b,mb) in enumerate(Bvec):
        need=(target-a.astype(np.int32)-b.astype(np.int32)).astype(np.int16)
        probes += 1
        pair=BB.get(need.tobytes())
        if pair is None:
            continue
        ic,id_=pair
        total=(a.astype(np.int32)+b.astype(np.int32)+
               Bvec[ic][0].astype(np.int32)+Bvec[id_][0].astype(np.int32))
        assert np.all(total==-4)
        witness=(ma,mb,Bvec[ic][1],Bvec[id_][1])
        break
    if witness is not None:
        break

print('target_order=2060')
print('cyclic_length_v=514')
print('paley_prime=257')
print('nonresidue_decimation=3')
print('legendre_sum=1 decimated_sum=1')
print('legendre_pair_nonzero_paf_sum=-2 VERIFIED')
print('raw_A_candidates=',rawA,sep='')
print('raw_zero_sum_candidates=',rawB,sep='')
print('unique_A_paf_signatures=',len(Avec),sep='')
print('unique_zero_sum_paf_signatures=',len(Bvec),sep='')
print('raw_BB_pairs_with_repetition=',raw_pairs,sep='')
print('unique_BB_sum_signatures=',len(BB),sep='')
print('A_plus_B_complement_probes=',probes,sep='')
print('solution_count=',0 if witness is None else 1,sep='')
if witness is not None:
    print('WITNESS_META=',witness)
    raise SystemExit('FOUND_RESTRICTED_SOLUTION')
print('EXACT_ENUMERATION_PASSED')
print('PROVED_RESTRICTED: no Paley-Legendre two-half interleaving quartet in the stated family satisfies the bordered-GS PAF target.')
print('SCOPE: restricted-family nonexistence only; no claim about unrestricted cyclic BGS or H(2060).')
