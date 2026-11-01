#!/usr/bin/env python3
"""Independent P26 exact audit of P04-I0101-P4177-THETAPLUS-FRONTIER-38.

Floating eigensolvers/Cholesky are proposal mechanisms only. All acceptance
conditions are then checked in integer arithmetic. This independently rebuilds
the localized Paley graph, the anharmonic S3 orbit partitions, the rational
certificate and the residual positive-definiteness witness.
"""
import hashlib, math
from collections import Counter
import numpy as np

P=4177; TNUM=4308; TDEN=100
WQ=1024; D=51200; FACQ=1024; SLACK=3072; NITER=35; CLIP=.662
EXPECTED_W='6ad77c617fe574f7c1e2ddbab16566ceed565dd4a6c268c28b37547006a381ee'
EXPECTED_L='3ef38d7cd9c1ce7e25b0568acec6a58bdfbaf3586916f2bd60043d9703e1970c'

def prime(q):
    if q<2: return False
    d=2
    while d*d<=q:
        if q%d==0: return False
        d+=1
    return True

def chi(a):
    a%=P
    if a==0: return 0
    return 1 if pow(a,(P-1)//2,P)==1 else -1

frontier=[q for q in range(4158,4178) if q%4==1 and prime(q)]
assert frontier==[P]
V=[x for x in range(P) if x not in (0,1) and chi(x)==1 and chi(x-1)==1]
n=len(V); assert n==(P-5)//4==1043
idx={x:i for i,x in enumerate(V)}
H=np.zeros((n,n),dtype=np.int8)
for i,x in enumerate(V):
    for j in range(i+1,n):
        if chi(x-V[j])==1: H[i,j]=H[j,i]=1
edges=int(H.sum()//2); nonedges=n*(n-1)//2-edges
assert (edges,nonedges)==(271185,272218)

r=[idx[(1-x)%P] for x in V]
s=[idx[pow(x,-1,P)] for x in V]
seen=set(); vertex_orbits=[]
for i in range(n):
    if i in seen: continue
    O=set(); stack=[i]
    while stack:
        a=stack.pop()
        if a in O: continue
        O.add(a); stack.extend((r[a],s[a]))
    seen|=O; vertex_orbits.append(O)
vc=Counter(map(len,vertex_orbits)); assert vc==Counter({6:173,3:1,2:1})

pair=np.full((n,n),-1,dtype=np.int32); orbits=[]
for i in range(n):
    for j in range(i+1,n):
        if H[i,j] or pair[i,j]>=0: continue
        O=set(); stack=[(i,j)]
        while stack:
            a,b=stack.pop()
            if a>b: a,b=b,a
            if (a,b) in O: continue
            O.add((a,b))
            for perm in (r,s):
                aa,bb=perm[a],perm[b]
                if aa>bb: aa,bb=bb,aa
                stack.append((aa,bb))
        oid=len(orbits); arr=sorted(O)
        for a,b in arr:
            assert H[a,b]==0
            pair[a,b]=pair[b,a]=oid
        orbits.append(arr)
pc=Counter(map(len,orbits)); assert len(orbits)==45501
assert pc==Counter({6:45239,3:261,1:1})
assert 1+3*261+6*45239==nonedges
assert 2+3+6*173==n
assert edges+nonedges==n*(n-1)//2

# Proposal stage, checked by immutable raw-data hashes.
fixed=H.astype(bool); np.fill_diagonal(fixed,True)
B=np.where(fixed,1.0,-1.0)
for _ in range(NITER):
    vals,vec=np.linalg.eigh(B)
    vals=np.minimum(vals,CLIP*math.sqrt(P))
    B=(vec*vals)@vec.T
    B[fixed]=1.0
    B=(B+B.T)/2
candidate_top=float(np.linalg.eigvalsh(B)[-1])
w=np.array([int(np.rint(WQ*B[a][b])) for (a,b), in [(o[0],) for o in orbits]],dtype=np.int64)
whash=hashlib.sha256(w.astype(np.int16).tobytes(order='C')).hexdigest()
assert whash==EXPECTED_W
assert int(w.min())==-1704 and int(w.max())==-257 and int(w.max())<0

DB=np.full((n,n),D,dtype=np.int64)
for oid,O in enumerate(orbits):
    val=(D//WQ)*int(w[oid])
    for a,b in O: DB[a,b]=DB[b,a]=val
assert np.array_equal(DB,DB.T)
assert np.all(np.diag(DB)==D)
assert np.all(DB[H.astype(bool)]==D)
for perm in (r,s):
    assert np.array_equal(DB,DB[np.ix_(perm,perm)])

margin=4*TDEN*TDEN*P-9*TNUM*TNUM
assert margin==50224>0
Mint=np.eye(n,dtype=np.int64)*(D*TNUM//TDEN)-DB
Lf=np.linalg.cholesky(Mint.astype(float)-SLACK*np.eye(n))
Lq=np.rint(FACQ*Lf).astype(np.int64)
maxL=int(np.max(np.abs(Lq)))
assert n*maxL*maxL<2**63
LL=Lq@Lq.T
R=(FACQ*FACQ)*(Mint-SLACK*np.eye(n,dtype=np.int64))-LL
maxentry=int(np.max(np.abs(R)))
maxrowsum=int(np.max(np.sum(np.abs(R),axis=1,dtype=np.int64)))
assert n*maxentry<2**63
bound=SLACK*FACQ*FACQ
assert maxrowsum==465316633 and bound==3221225472 and maxrowsum<bound
lhash=hashlib.sha256(Lq.tobytes(order='C')).hexdigest(); assert lhash==EXPECTED_L
slack=bound-maxrowsum
num=slack; den=FACQ*FACQ*D
assert (num,den)==(2755908839,53687091200)

print('P26-P4177-THETAPLUS-INDEPENDENT-AUDIT=PASS')
print('frontier=[4177]')
print(f'|V2|={n}; edges={edges}; nonedges={nonedges}')
print(f'vertex_orbits={sorted(vc.items())}')
print(f'nonedge_orbits={len(orbits)}; census={sorted(pc.items())}')
print(f'candidate_top_float_NONCERTIFYING={candidate_top:.15g}')
print(f'weight_range=[{int(w.min())},{int(w.max())}]/{WQ}')
print(f'weight_hash={whash}')
print(f'source_margin={margin}')
print(f'maxL={maxL}; n_maxL2={n*maxL*maxL}')
print(f'maxentry_R={maxentry}; n_maxentry_R={n*maxentry}')
print(f'residual_rowsum={maxrowsum}; residual_bound={bound}; residual_slack={slack}')
print(f'Lq_hash={lhash}')
print(f'certified_lambda_min_tIminusB_lower_bound={num}/{den}')
print('THETA_PLUS_DUAL_SIGN=PASS')
print('EXACT_RESIDUAL_PD=PASS')
print('SOURCE_COMPARISON=PASS')
print('END_P26_P4177_AUDIT')
