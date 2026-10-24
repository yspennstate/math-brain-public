#!/usr/bin/env python3
"""Exact verifier for P04/I0101 at p=4021.

Floating alternating projections generate a rational S3-orbit candidate and
floating Cholesky generates an integer witness factor Lq. Neither floating
stage is accepted as evidence. Acceptance is exclusively by exact integer
identities and exact row-sum bounds; no floating eigenvalue/sign decision is
used in the proof.
"""
from collections import Counter
import hashlib
import numpy as np

P=4021
TNUM=421
TDEN=10
WQ=1024
D=5120
FACQ=1024
SLACK_I=256

def is_prime_trial(p):
    if p < 2: return False
    d=2
    while d*d <= p:
        if p % d == 0: return False
        d += 1
    return True

assert is_prime_trial(P)
assert P % 4 == 1
assert P % 24 == 13

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

V=[x for x in range(P) if x not in (0,1)
   and legendre(x,P)==1 and legendre(x-1,P)==1]
n=len(V)
assert n==(P-5)//4==1004
idx={x:i for i,x in enumerate(V)}
A=np.zeros((n,n),dtype=np.int8)
for i,x in enumerate(V):
    for j in range(i+1,n):
        if legendre(x-V[j],P)==1:
            A[i,j]=A[j,i]=1
edges=int(A.sum()//2)
nonedges=n*(n-1)//2-edges
assert edges==251346
assert nonedges==252160

pr=np.array([idx[(1-x)%P] for x in V],dtype=np.int32)
ps=np.array([idx[pow(x,-1,P)] for x in V],dtype=np.int32)

seen=set(); vertex_orbits=[]
for i in range(n):
    if i in seen: continue
    orb=set(); stack=[i]
    while stack:
        a=stack.pop()
        if a in orb: continue
        orb.add(a)
        stack += [int(pr[a]),int(ps[a])]
    seen |= orb
    vertex_orbits.append(orb)
assert len(vertex_orbits)==168
assert Counter(map(len,vertex_orbits))==Counter({6:167,2:1})

pair_id=-np.ones((n,n),dtype=np.int32)
orbits=[]
for i in range(n):
    for j in range(i+1,n):
        if A[i,j] or pair_id[i,j]>=0: continue
        orb=set(); stack=[(i,j)]
        while stack:
            a,b=stack.pop()
            if a>b: a,b=b,a
            if (a,b) in orb: continue
            orb.add((a,b))
            for perm in (pr,ps):
                aa,bb=int(perm[a]),int(perm[b])
                if aa>bb: aa,bb=bb,aa
                stack.append((aa,bb))
        oid=len(orbits)
        arr=sorted(orb)
        for a,b in arr:
            assert A[a,b]==0
            pair_id[a,b]=pair_id[b,a]=oid
        orbits.append(arr)
assert len(orbits)==42155
assert Counter(map(len,orbits))==Counter({6:41899,3:255,1:1})
assert sum(map(len,orbits))==nonedges

# Candidate generation only.
fixed=A.astype(bool); np.fill_diagonal(fixed,True)
Bcand=np.where(fixed,1.0,-1.0)
for _ in range(80):
    evals,evecs=np.linalg.eigh(Bcand)
    evals=np.minimum(evals,42.0)
    Bcand=(evecs*evals)@evecs.T
    Bcand[fixed]=1.0
    Bcand=(Bcand+Bcand.T)/2
weights=np.array([int(np.rint(WQ*Bcand[arr[0][0],arr[0][1]]))
                  for arr in orbits],dtype=np.int64)
assert len(weights)==len(orbits)
assert int(weights.min())==-2291
assert int(weights.max())==-250
weight_hash=hashlib.sha256(weights.astype(np.int16).tobytes(order="C")).hexdigest()
assert weight_hash=="faaafced786af680fff61ea1aae21cb8f1fe6d9724a171db3d44d9b968128fc2"

DB=np.full((n,n),D,dtype=np.int64)
for oid,arr in enumerate(orbits):
    v=(D//WQ)*int(weights[oid])
    for a,b in arr:
        DB[a,b]=DB[b,a]=v
assert np.array_equal(DB,DB.T)
assert np.all(np.diag(DB)==D)
assert np.all(DB[A.astype(bool)]==D)
for perm in (pr,ps):
    assert np.array_equal(DB,DB[np.ix_(perm,perm)])

threshold_margin=400*P-9*TNUM*TNUM
assert threshold_margin==13231>0

diag_scaled=D*TNUM//TDEN
assert diag_scaled==215552
Mint=np.eye(n,dtype=np.int64)*diag_scaled-DB
assert np.array_equal(Mint,Mint.T)

# Floating Cholesky proposes Lq only; exact acceptance follows.
Lf=np.linalg.cholesky(Mint.astype(float)-SLACK_I*np.eye(n))
Lq=np.rint(FACQ*Lf).astype(np.int64)
maxL=int(np.max(np.abs(Lq)))
dot_safety=n*maxL*maxL
assert maxL==469452
assert dot_safety==221266721025216
assert dot_safety<2**63
LL=Lq@Lq.T
Rnum=(FACQ*FACQ)*(Mint-SLACK_I*np.eye(n,dtype=np.int64))-LL
maxentry=int(np.max(np.abs(Rnum)))
maxrowsum=int(np.max(np.sum(np.abs(Rnum),axis=1,dtype=np.int64)))
assert maxentry==830980
assert maxrowsum==140368754
assert n*maxentry<2**63

pd_bound=SLACK_I*FACQ*FACQ
assert pd_bound==268435456
assert maxrowsum<pd_bound
pd_slack=pd_bound-maxrowsum
assert pd_slack==128066702
lq_hash=hashlib.sha256(Lq.tobytes(order='C')).hexdigest()
assert lq_hash=="b1671dd508503e21cb22ed1710a49eaf73a88f4f336052eadf5361c7be540b28"

print("P04-I0101-P4021-S3-ORBIT-DUAL=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"edges={edges}")
print(f"nonedges={nonedges}")
print(f"vertex_orbits={len(vertex_orbits)}")
print(f"vertex_orbit_size_census={sorted(Counter(map(len,vertex_orbits)).items())}")
print(f"nonedge_orbits={len(orbits)}")
print(f"orbit_size_census={sorted(Counter(map(len,orbits)).items())}")
print(f"weight_denominator={WQ}")
print(f"weight_numerator_min={int(weights.min())}")
print(f"weight_numerator_max={int(weights.max())}")
print(f"weight_raw_sha256={weight_hash}")
print(f"t={TNUM}/{TDEN}")
print(f"threshold_margin_400p_minus_9Tnum2={threshold_margin}")
print(f"D={D}")
print(f"FACQ={FACQ}")
print(f"SLACK_I={SLACK_I}")
print(f"max_abs_Lq={maxL}")
print(f"dot_product_safety_bound={dot_safety}")
print(f"max_abs_Rnum={maxentry}")
print(f"max_row_abs_sum_Rnum={maxrowsum}")
print(f"exact_PD_bound={pd_bound}")
print(f"exact_PD_slack={pd_slack}")
print(f"Lq_sha256={lq_hash}")
print("EXACT_RESIDUAL_PD=PASS")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print("THETA_LT_421_OVER_10_LT_2SQRT_P_OVER_3=PASS")
