#!/usr/bin/env python3
"""Exact verifier for P04/I0101 at p=4013.

Floating alternating projections generate a rational S3-orbit candidate and
floating Cholesky generates an integer witness factor Lq.  Neither floating
stage is accepted as evidence. Acceptance is exclusively by exact integer
identities and exact row-sum bounds; no floating eigenvalue/sign decision is
used in the proof.
"""
from pathlib import Path
from collections import Counter
import hashlib
import numpy as np

P=4013
TNUM=421
TDEN=10
WQ=1024
D=5120              # lcm(TDEN,WQ)
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
assert P % 24 == 5

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

V=[x for x in range(P) if x not in (0,1)
   and legendre(x,P)==1 and legendre(x-1,P)==1]
n=len(V)
assert n==(P-5)//4==1002
idx={x:i for i,x in enumerate(V)}
A=np.zeros((n,n),dtype=np.int8)
for i,x in enumerate(V):
    for j in range(i+1,n):
        if legendre(x-V[j],P)==1:
            A[i,j]=A[j,i]=1
edges=int(A.sum()//2)
nonedges=n*(n-1)//2-edges
assert edges==250260
assert nonedges==251241

# Anharmonic S3 generators.
pr=np.array([idx[(1-x)%P] for x in V],dtype=np.int32)
ps=np.array([idx[pow(x,-1,P)] for x in V],dtype=np.int32)
# p=5 mod 24 => free vertex action, hence 167 six-orbits.
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
assert len(vertex_orbits)==167
assert Counter(map(len,vertex_orbits))==Counter({6:167})

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
assert len(orbits)==41998
assert Counter(map(len,orbits))==Counter({6:41749,3:249})
assert sum(map(len,orbits))==nonedges

# Candidate generation for the rational nonedge orbit weights.
# This floating stage is not accepted as evidence: it only proposes integers.
# Start at the natural sign completion (fixed diagonal/edges +1, nonedges -1),
# alternate spectral clipping at cap 42 with projection back to the fixed affine
# space for exactly 80 steps, then round one representative per S3 orbit to
# denominator WQ.  The resulting rational matrix is accepted only by the exact
# integer positive-definiteness test below.
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
assert int(weights.min())==-1736
assert int(weights.max())==-253
weight_hash=hashlib.sha256(weights.astype(np.int16).tobytes(order="C")).hexdigest()
assert weight_hash=="30963a61f43d52a7c4120bfc0e2ac38657d64c0dcddc03508cd9e34afb34c1c8"

# DB = D * B is integer.  Diagonal and edges are exactly 1 in B,
# while nonedge orbit oid gets weights[oid]/WQ.
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

# Exact source-threshold comparison:
# (421/10)^2 < 4*4013/9 iff 9*421^2 < 400*4013.
threshold_margin=400*P-9*TNUM*TNUM
assert threshold_margin==10031>0

# Mint = D * ((421/10) I - B), exactly integer.
diag_scaled=D*TNUM//TDEN
assert diag_scaled==215552
Mint=np.eye(n,dtype=np.int64)*diag_scaled-DB
assert np.array_equal(Mint,Mint.T)

# Candidate generation only.  Exact acceptance is below.
# We leave SLACK_I * I before Cholesky, round FACQ*L, then certify
# the residual by an exact infinity-norm bound.
Lf=np.linalg.cholesky(Mint.astype(float)-SLACK_I*np.eye(n))
Lq=np.rint(FACQ*Lf).astype(np.int64)
maxL=int(np.max(np.abs(Lq)))
dot_safety=n*maxL*maxL
assert dot_safety<2**63
LL=Lq@Lq.T
Rnum=(FACQ*FACQ)*(Mint-SLACK_I*np.eye(n,dtype=np.int64))-LL
maxentry=int(np.max(np.abs(Rnum)))
assert n*maxentry<2**63
maxrowsum=int(np.max(np.sum(np.abs(Rnum),axis=1,dtype=np.int64)))

# Exact identity:
# Mint=(Lq/FACQ)(Lq/FACQ)^T + SLACK_I*I + Rnum/FACQ^2.
# Symmetric R gives ||R||_2 <= ||R||_infty.  Therefore
# maxrowsum < SLACK_I*FACQ^2 proves Mint >> 0 exactly.
pd_bound=SLACK_I*FACQ*FACQ
assert maxrowsum<pd_bound
pd_slack=pd_bound-maxrowsum

print("P04-I0101-P4013-S3-ORBIT-DUAL=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"edges={edges}")
print(f"nonedges={nonedges}")
print(f"vertex_orbits={len(vertex_orbits)}")
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
print(f"Lq_sha256={hashlib.sha256(Lq.tobytes(order='C')).hexdigest()}")
print("EXACT_RESIDUAL_PD=PASS")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print("THETA_LT_421_OVER_10_LT_2SQRT_P_OVER_3=PASS")
