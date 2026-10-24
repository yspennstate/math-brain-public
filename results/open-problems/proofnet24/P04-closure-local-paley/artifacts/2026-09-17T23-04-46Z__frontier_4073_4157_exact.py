#!/usr/bin/env python3
"""Exact P04/I0101 finite verifier for one frontier prime.

Usage: python p04_frontier_case_exact.py P TNUM
Allowed (P,TNUM): (4073,425),(4093,426),(4129,428),(4133,428),(4153,429),(4157,429).
Here t=TNUM/10. Floating spectral projection and Cholesky only PROPOSE integer
data. Acceptance is exact integer arithmetic: graph/orbit identities, fixed dual
entries, S3 invariance, exact source-threshold comparison, and a strict residual
row-sum positive-definiteness bound.
"""
import sys, math, hashlib
from collections import Counter
import numpy as np

CASES={
 (4073,425):("0062c93dbeebff8d1f41f7ff7a1faaad426c99a1061d8e09b96e46d5cf3cf7a0",
             "e7965df53997e70be542c6d57f76fc23b2e75967c432f5c56c4985124ce8a457"),
 (4093,426):("32a99872d07f4bec73c5608639acb38e784520475c789dc8c8bb48d901820143",
             "f80b583793377182ef5385028948b3e135c6401b01451e2c761dc144c3a2a6c5"),
 (4129,428):("cab00a56285f1a61ec085a4da4e655797d02605e4c9b75a972d16b9c6b8be55b",
             "f8f8bdcf8ad13da4d4d305e6efb5ed159f09a50f017b4fcdbe84313b8509e93d"),
 (4133,428):("dcfb4e107dcb302a6e97a0fc4fdfc4753893f4a2804892cf8fe0a678179869ef",
             "5a8a3b552b8226890258371533b3ceac758de6d52fc326ce8a9797124d1c81d2"),
 (4153,429):("5648296513c593cc962bd85dc2963424cd11868626f5d1a2268f81725e087e11",
             "d64f1b2527b785f5c51a081fbc3c514fd58b341aeded01b9cececafec878a9e3"),
 (4157,429):("d4056969d5f314e7043f5e0e9a03de7abd9bf912892403e686fab5ba1f1a8463",
             "884fbf55cd8c1ced67633e49bed568aa236413c5c5ab960ced7445e92097a851"),
}
P=int(sys.argv[1]); TNUM=int(sys.argv[2]); TDEN=10
assert (P,TNUM) in CASES
WQ=1024; D=5120; FACQ=1024; SLACK_I=512; NITER=35; CLIP_RATIO=.662

def isprime(p):
    if p<2:return False
    d=2
    while d*d<=p:
        if p%d==0:return False
        d+=1
    return True

frontier=[q for q in range(4058,4158) if q%4==1 and isprime(q)]
assert frontier == [4073,4093,4129,4133,4153,4157]

def leg(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

assert isprime(P) and P%4==1
V=[x for x in range(P) if x not in (0,1) and leg(x,P)==1 and leg(x-1,P)==1]
n=len(V); assert n==(P-5)//4
idx={x:i for i,x in enumerate(V)}
A=np.zeros((n,n),dtype=np.int8)
for i,x in enumerate(V):
    for j in range(i+1,n):
        if leg(x-V[j],P)==1:A[i,j]=A[j,i]=1
edges=int(A.sum()//2); nonedges=n*(n-1)//2-edges
pr=np.array([idx[(1-x)%P] for x in V],dtype=np.int32)
ps=np.array([idx[pow(x,-1,P)] for x in V],dtype=np.int32)

seen=set(); vos=[]
for i in range(n):
    if i in seen:continue
    o=set(); st=[i]
    while st:
        a=st.pop()
        if a in o:continue
        o.add(a); st += [int(pr[a]),int(ps[a])]
    seen|=o; vos.append(o)
vc=Counter(map(len,vos)); assert sum(k*v for k,v in vc.items())==n

pair=-np.ones((n,n),dtype=np.int32); orbs=[]
for i in range(n):
    for j in range(i+1,n):
        if A[i,j] or pair[i,j]>=0:continue
        o=set(); st=[(i,j)]
        while st:
            a,b=st.pop()
            if a>b:a,b=b,a
            if (a,b) in o:continue
            o.add((a,b))
            for perm in (pr,ps):
                aa,bb=int(perm[a]),int(perm[b])
                if aa>bb:aa,bb=bb,aa
                st.append((aa,bb))
        oid=len(orbs); arr=sorted(o)
        for a,b in arr:
            assert A[a,b]==0
            pair[a,b]=pair[b,a]=oid
        orbs.append(arr)
pc=Counter(map(len,orbs)); assert sum(map(len,orbs))==nonedges

# Floating proposal only.
fixed=A.astype(bool); np.fill_diagonal(fixed,True)
B=np.where(fixed,1.,-1.)
for _ in range(NITER):
    vals,vec=np.linalg.eigh(B)
    vals=np.minimum(vals,CLIP_RATIO*math.sqrt(P))
    B=(vec*vals)@vec.T
    B[fixed]=1.
    B=(B+B.T)/2
candidate_top=float(np.linalg.eigvalsh(B)[-1])
weights=np.array([int(np.rint(WQ*B[arr[0][0],arr[0][1]])) for arr in orbs],dtype=np.int64)
whash=hashlib.sha256(weights.astype(np.int16).tobytes(order="C")).hexdigest()
assert whash==CASES[(P,TNUM)][0]

DB=np.full((n,n),D,dtype=np.int64)
for oid,arr in enumerate(orbs):
    v=(D//WQ)*int(weights[oid])
    for a,b in arr:DB[a,b]=DB[b,a]=v
assert np.array_equal(DB,DB.T)
assert np.all(np.diag(DB)==D)
assert np.all(DB[A.astype(bool)]==D)
for perm in (pr,ps):assert np.array_equal(DB,DB[np.ix_(perm,perm)])

# Exact source threshold t < 2 sqrt(P)/3.
margin=4*TDEN*TDEN*P-9*TNUM*TNUM
assert margin>0
assert (D*TNUM)%TDEN==0
Mint=np.eye(n,dtype=np.int64)*(D*TNUM//TDEN)-DB
assert np.array_equal(Mint,Mint.T)

# Floating factor proposal, then exact residual acceptance.
Lf=np.linalg.cholesky(Mint.astype(float)-SLACK_I*np.eye(n))
Lq=np.rint(FACQ*Lf).astype(np.int64)
maxL=int(np.max(np.abs(Lq))); assert n*maxL*maxL<2**63
LL=Lq@Lq.T
R=(FACQ*FACQ)*(Mint-SLACK_I*np.eye(n,dtype=np.int64))-LL
maxentry=int(np.max(np.abs(R))); assert n*maxentry<2**63
maxrowsum=int(np.max(np.sum(np.abs(R),axis=1,dtype=np.int64)))
pdbound=SLACK_I*FACQ*FACQ
assert maxrowsum<pdbound
lhash=hashlib.sha256(Lq.tobytes(order="C")).hexdigest()
assert lhash==CASES[(P,TNUM)][1]

print(f"P04-I0101-P{P}-S3-ORBIT-DUAL=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"edges={edges}")
print(f"nonedges={nonedges}")
print(f"vertex_orbit_size_census={sorted(vc.items())}")
print(f"nonedge_orbits={len(orbs)}")
print(f"orbit_size_census={sorted(pc.items())}")
print(f"candidate_top_float_NONCERTIFYING={candidate_top:.15g}")
print(f"weight_numerator_range=[{int(weights.min())},{int(weights.max())}]/{WQ}")
print(f"weight_raw_sha256={whash}")
print(f"t={TNUM}/{TDEN}")
print(f"threshold_margin_4den2p_minus_9num2={margin}")
print(f"max_row_abs_sum_Rnum={maxrowsum}")
print(f"exact_PD_bound={pdbound}")
print(f"exact_PD_slack={pdbound-maxrowsum}")
print(f"Lq_sha256={lhash}")
print("EXACT_RESIDUAL_PD=PASS")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print(f"THETA_LT_{TNUM}_OVER_{TDEN}_LT_2SQRT_P_OVER_3=PASS")
