#!/usr/bin/env python3
"""Exact finite verifier for P04/I0101 at p=4001.

The adjacent .b64 file freezes the integer S3-orbit weights. Floating Cholesky
is used only to generate a rational candidate factor. Acceptance of positive
definiteness is by an exact integer residual identity and exact row-sum bound;
no floating eigenvalue/sign decision is used in the proof.
"""
from pathlib import Path
from collections import Counter
import base64, zlib, hashlib
import numpy as np

P=4001
T=42
Q=8192
DATA=Path(__file__).with_name("2026-09-16T22-15-37Z__p4001_weights.b64")

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

V=[x for x in range(P) if x not in (0,1)
   and legendre(x,P)==1 and legendre(x-1,P)==1]
n=len(V)
assert n==(P-5)//4==999
idx={x:i for i,x in enumerate(V)}
A=np.zeros((n,n),dtype=np.int8)
for i,x in enumerate(V):
    for j in range(i+1,n):
        if legendre(x-V[j],P)==1:
            A[i,j]=A[j,i]=1
edges=int(A.sum()//2)
nonedges=n*(n-1)//2-edges
assert edges==248901 and nonedges==249600

pr=np.array([idx[(1-x)%P] for x in V],dtype=np.int32)
ps=np.array([idx[pow(x,-1,P)] for x in V],dtype=np.int32)
pair_id=-np.ones((n,n),dtype=np.int32)
orbits=[]
for i in range(n):
    for j in range(i+1,n):
        if A[i,j] or pair_id[i,j]>=0: continue
        seen=set(); stack=[(i,j)]
        while stack:
            a,b=stack.pop()
            if a>b: a,b=b,a
            if (a,b) in seen: continue
            seen.add((a,b))
            for perm in (pr,ps):
                aa,bb=int(perm[a]),int(perm[b])
                if aa>bb: aa,bb=bb,aa
                stack.append((aa,bb))
        oid=len(orbits); arr=[]
        for a,b in seen:
            assert A[a,b]==0
            pair_id[a,b]=pair_id[b,a]=oid
            arr.append((a,b))
        orbits.append(arr)
assert len(orbits)==41728
assert Counter(map(len,orbits))==Counter({6:41472,3:256})

raw=zlib.decompress(base64.b64decode(DATA.read_text().strip().encode()))
assert len(raw)==len(orbits)
assert hashlib.sha256(raw).hexdigest()=="2dad79c5191441524cb2e81daf93c91fe52848cf0686143a43236cfd4bbd12b8"
weights=np.frombuffer(raw,dtype=np.uint8).astype(np.int16)-128
assert Counter(map(int,weights))==Counter({-4:42,-3:1206,-2:9102,-1:18649,0:11101,1:1597,2:31})

B=np.ones((n,n),dtype=np.int64)
for i in range(n):
    for j in range(i+1,n):
        if not A[i,j]:
            oid=int(pair_id[i,j]); assert oid>=0
            B[i,j]=B[j,i]=int(weights[oid])
assert np.array_equal(B,B.T)
assert np.all(np.diag(B)==1)
assert np.all(B[A.astype(bool)]==1)
for perm in (pr,ps):
    assert np.array_equal(B,B[np.ix_(perm,perm)])

threshold_margin=4*P-9*T*T
assert threshold_margin==128>0
M=T*np.eye(n,dtype=np.int64)-B
assert np.array_equal(M,M.T)

# Candidate generation only; leave 1/4 I of exact slack.
Lf=np.linalg.cholesky(M.astype(float)-0.25*np.eye(n))
Lq=np.rint(Q*Lf).astype(np.int64)
maxL=int(np.max(np.abs(Lq)))
dot_safety=n*maxL*maxL
assert dot_safety<2**63
LL=Lq@Lq.T
Rnum=4*Q*Q*M-Q*Q*np.eye(n,dtype=np.int64)-4*LL
maxentry=int(np.max(np.abs(Rnum)))
assert n*maxentry<2**63
maxrowsum=int(np.max(np.sum(np.abs(Rnum),axis=1,dtype=np.int64)))

# Exact identity:
# M=(Lq/Q)(Lq/Q)^T + (1/4)I + Rnum/(4Q^2).
# Symmetry gives ||R||_2 <= ||R||_infty.  Thus maxrowsum<Q^2
# makes (1/4)I+R positive definite, hence M positive definite.
assert maxrowsum<Q*Q
slack=Q*Q-maxrowsum
assert slack==5977116
assert maxentry==372156
assert maxL==52294
assert hashlib.sha256(Lq.tobytes(order="C")).hexdigest()=="f22e8df94f2f16c78f2e811603e98fb87d4041f50327655531b54403c2f2ee5a"

print("P04-I0101-P4001-S3-ORBIT-DUAL=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"edges={edges}")
print(f"nonedges={nonedges}")
print(f"nonedge_orbits={len(orbits)}")
print(f"orbit_size_census={sorted(Counter(map(len,orbits)).items())}")
print(f"weight_census={sorted(Counter(map(int,weights)).items())}")
print(f"T={T}")
print(f"threshold_margin_4p_minus_9T2={threshold_margin}")
print(f"Q={Q}")
print(f"max_abs_Lq={maxL}")
print(f"dot_product_safety_bound={dot_safety}")
print(f"max_abs_Rnum={maxentry}")
print(f"max_row_abs_sum_Rnum={maxrowsum}")
print(f"exact_PD_slack_Q2_minus_rowsum={slack}")
print("EXACT_RESIDUAL_PD=PASS")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print("THETA_LT_42_LT_2SQRT_P_OVER_3=PASS")
