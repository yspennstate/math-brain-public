#!/usr/bin/env python3
"""Exact P04/I0101 frontier verifier at p=4177.

Floating spectral projection and Cholesky are proposal mechanisms only.
Acceptance is exact integer arithmetic: graph/orbit identities, fixed theta
dual entries, S3 invariance, theta-plus sign constraints, exact comparison
with (2/3)sqrt(p), and a strict integer residual PD bound.

This checker verifies every admissible prime p == 1 mod 4 in (4157,4177].
"""
import math, hashlib
from collections import Counter
import numpy as np

CASES={
    4177:(4308,"6ad77c617fe574f7c1e2ddbab16566ceed565dd4a6c268c28b37547006a381ee","3ef38d7cd9c1ce7e25b0568acec6a58bdfbaf3586916f2bd60043d9703e1970c")
}
TDEN=100
WQ=1024
D=51200
FACQ=1024
SLACK_I=3072
NITER=35
CLIP_RATIO=.662

def isprime(p):
    if p<2: return False
    d=2
    while d*d<=p:
        if p%d==0: return False
        d+=1
    return True

def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

frontier=[q for q in range(4158,4178) if q%4==1 and isprime(q)]
assert frontier==list(CASES)

print("P04/I0101 exact frontier checker: (4157,4177]")
print(f"frontier={frontier}")

for P in frontier:
    TNUM, expected_whash, expected_lhash = CASES[P]
    V=[x for x in range(P) if x not in (0,1) and leg(x,P)==1 and leg(x-1,P)==1]
    n=len(V)
    assert n==(P-5)//4
    idx={x:i for i,x in enumerate(V)}

    H=np.zeros((n,n),dtype=np.int8)
    for i,x in enumerate(V):
        for j in range(i+1,n):
            if leg(x-V[j],P)==1:
                H[i,j]=H[j,i]=1
    edges=int(H.sum()//2)
    nonedges=n*(n-1)//2-edges

    pr=np.array([idx[(1-x)%P] for x in V],dtype=np.int32)
    ps=np.array([idx[pow(x,-1,P)] for x in V],dtype=np.int32)

    seen=set(); vos=[]
    for i in range(n):
        if i in seen: continue
        o=set(); st=[i]
        while st:
            a=st.pop()
            if a in o: continue
            o.add(a); st += [int(pr[a]),int(ps[a])]
        seen |= o; vos.append(o)
    vc=Counter(map(len,vos))
    assert sum(k*v for k,v in vc.items())==n

    pair=-np.ones((n,n),dtype=np.int32); orbs=[]
    for i in range(n):
        for j in range(i+1,n):
            if H[i,j] or pair[i,j]>=0: continue
            o=set(); st=[(i,j)]
            while st:
                a,b=st.pop()
                if a>b: a,b=b,a
                if (a,b) in o: continue
                o.add((a,b))
                for perm in (pr,ps):
                    aa,bb=int(perm[a]),int(perm[b])
                    if aa>bb: aa,bb=bb,aa
                    st.append((aa,bb))
            oid=len(orbs); arr=sorted(o)
            for a,b in arr:
                assert H[a,b]==0
                pair[a,b]=pair[b,a]=oid
            orbs.append(arr)
    pc=Counter(map(len,orbs))
    assert sum(map(len,orbs))==nonedges

    fixed=H.astype(bool)
    np.fill_diagonal(fixed,True)
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
    assert whash==expected_whash
    assert int(weights.max())<0

    DB=np.full((n,n),D,dtype=np.int64)
    for oid,arr in enumerate(orbs):
        v=(D//WQ)*int(weights[oid])
        for a,b in arr:
            DB[a,b]=DB[b,a]=v
    assert np.array_equal(DB,DB.T)
    assert np.all(np.diag(DB)==D)
    assert np.all(DB[H.astype(bool)]==D)
    for perm in (pr,ps):
        assert np.array_equal(DB,DB[np.ix_(perm,perm)])

    margin=4*TDEN*TDEN*P-9*TNUM*TNUM
    assert margin>0
    assert (D*TNUM)%TDEN==0
    Mint=np.eye(n,dtype=np.int64)*(D*TNUM//TDEN)-DB

    Lf=np.linalg.cholesky(Mint.astype(float)-SLACK_I*np.eye(n))
    Lq=np.rint(FACQ*Lf).astype(np.int64)
    maxL=int(np.max(np.abs(Lq)))
    assert n*maxL*maxL < 2**63
    LL=Lq@Lq.T
    R=(FACQ*FACQ)*(Mint-SLACK_I*np.eye(n,dtype=np.int64))-LL
    maxentry=int(np.max(np.abs(R)))
    assert n*maxentry < 2**63
    maxrowsum=int(np.max(np.sum(np.abs(R),axis=1,dtype=np.int64)))
    pdbound=SLACK_I*FACQ*FACQ
    assert maxrowsum<pdbound
    lhash=hashlib.sha256(Lq.tobytes(order="C")).hexdigest()
    assert lhash==expected_lhash

    print()
    print(f"P04-I0101-P{P}-S3-ORBIT-THETAPLUS=PASS")
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
    print("SZEGEDY_THETA_PLUS_SIGN=PASS")
    print("SOURCE_THETA_BOUND=PASS")

print()
print("FRONTIER_INTERVAL=(4157,4177]")
print(f"FRONTIER_ADMISSIBLE_PRIMES={frontier}")
print("FRONTIER_ALL_EXACT_CERTIFIED=PASS")
print("FRONTIER_ALL_THETA_PLUS_CERTIFIED=PASS")
print("COMPLETE_RETAINED_CERTIFIED_DOMAIN=[149,257,1009,4001,4013,4021,4049,4057,4073,4093,4129,4133,4153,4157,4177]")
print("FROZEN_METRIC_BEFORE=4157")
print("FROZEN_METRIC_AFTER=4177")
print("SOURCE_ASYMPTOTIC_STATEMENT_PROVED=NO")
print("FINITE_EVIDENCE_ONLY=YES")
