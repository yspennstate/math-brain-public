#!/usr/bin/env python3
"""Exact finite verifier for P04/I0101 at p=4013.

A floating alternating-projection phase is used only to *discover* a rational,
S3-invariant edge-fixed candidate. The discovered orbit weights are rounded to
denominator 64 and then frozen by an exact SHA-256 hash. Acceptance of positive
definiteness is entirely exact: after integer scaling, a rounded Cholesky
factor is checked through an exact integer residual identity and an exact
infinity-norm bound. No floating eigenvalue/sign decision is used in the proof.
"""
from collections import Counter
import hashlib
import numpy as np
from scipy.linalg import eigh

P=4013
T_DISCOVERY=42.0
DISCOVERY_ITERS=80
TNUM=421
TDEN=10
WDEN=64
D=320
SLACK=5
Q=8192

def is_prime(p):
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    d=3
    while d*d <= p:
        if p % d == 0:
            return False
        d += 2
    return True

def legendre(a,p):
    a%=p
    if a==0:
        return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

assert is_prime(P)
assert P % 24 == 5
chiarr=np.zeros(P,dtype=np.int8)
for a in range(1,P):
    chiarr[a]=legendre(a,P)

V=np.array([x for x in range(P) if x not in (0,1)
            and chiarr[x]==1 and chiarr[(x-1)%P]==1],dtype=np.int32)
n=len(V)
assert n==(P-5)//4==1002
idx={int(x):i for i,x in enumerate(V)}
diff=(V[:,None]-V[None,:])%P
C=chiarr[diff]
A=(C==1)
N=(C==-1)
np.fill_diagonal(A,False)
np.fill_diagonal(N,False)
edges=int(A.sum()//2)
nonedges=n*(n-1)//2-edges
assert edges==250260 and nonedges==251241

# Exact anharmonic S3 action on V2.
pr=np.array([idx[(1-int(x))%P] for x in V],dtype=np.int32)
ps=np.array([idx[pow(int(x),-1,P)] for x in V],dtype=np.int32)
ident=np.arange(n,dtype=np.int32)
perms=[ident]
changed=True
while changed:
    changed=False
    for a in list(perms):
        for gen in (pr,ps):
            c=gen[a]
            if not any(np.array_equal(c,b) for b in perms):
                perms.append(c); changed=True
assert len(perms)==6
for perm in perms:
    assert np.array_equal(A,A[np.ix_(perm,perm)])

# p == 5 mod 24 has no exceptional vertex orbit: 167 regular six-orbits.
seen=set(); vertex_orbit_sizes=[]
for i in range(n):
    if i in seen:
        continue
    orb={int(perm[i]) for perm in perms}
    seen |= orb
    vertex_orbit_sizes.append(len(orb))
assert Counter(vertex_orbit_sizes)==Counter({6:167})

# Enumerate unordered nonedge pair orbits in a deterministic order.
pair_id=-np.ones((n,n),dtype=np.int32)
orbits=[]
for i in range(n):
    for j in range(i+1,n):
        if A[i,j] or pair_id[i,j]>=0:
            continue
        orb=set()
        for perm in perms:
            a,b=int(perm[i]),int(perm[j])
            if a>b:
                a,b=b,a
            orb.add((a,b))
        oid=len(orbits)
        arr=sorted(orb)
        for a,b in arr:
            assert not A[a,b]
            pair_id[a,b]=pair_id[b,a]=oid
        orbits.append(arr)
assert len(orbits)==41998
assert Counter(map(len,orbits))==Counter({6:41749,3:249})
assert sum(map(len,orbits))==nonedges

# DISCOVERY ONLY: alternating metric projections at the slightly stronger
# heuristic cap 42, starting from I+C. All exact proof obligations begin only
# after the orbit weights have been rounded and hash-frozen below.
B=np.eye(n,dtype=np.float64)+C.astype(np.float64)
for _ in range(DISCOVERY_ITERS):
    vals,vecs=eigh(B,subset_by_value=(T_DISCOVERY,np.inf),driver="evr")
    if len(vals)==0:
        break
    Z=(vecs*(vals-T_DISCOVERY))@vecs.T
    B[N]-=Z[N]
    B=(B+B.T)/2

Bavg=sum(B[np.ix_(perm,perm)] for perm in perms)/6.0
weights=[]
for orb in orbits:
    w=int(np.rint(WDEN*np.mean([Bavg[a,b] for a,b in orb])))
    weights.append(w)
weights=np.array(weights,dtype=np.int64)
assert int(weights.min())==-108 and int(weights.max())==-16
weight_bytes=weights.astype("<i2").tobytes(order="C")
assert hashlib.sha256(weight_bytes).hexdigest()=="3def86d7d3f7332e88c6113fffe32c659442f8be684a10ed3263590207e24434"

# From here on the candidate is exact. B has diagonal/edge value 1 and
# nonedge value weights[orbit]/64. Scale by D=lcm(10,64)=320.
Bnum=np.full((n,n),D,dtype=np.int64)
for oid,orb in enumerate(orbits):
    val=5*int(weights[oid])  # 320*(w/64)
    for a,b in orb:
        Bnum[a,b]=Bnum[b,a]=val
assert np.array_equal(Bnum,Bnum.T)
assert np.all(np.diag(Bnum)==D)
assert np.all(Bnum[A]==D)
for perm in (pr,ps):
    assert np.array_equal(Bnum,Bnum[np.ix_(perm,perm)])

# t=421/10 is strictly below 2 sqrt(p)/3:
# 4p/9 - t^2 = (400p - 9*421^2)/900 = 10031/900 > 0.
threshold_num=400*P-9*TNUM*TNUM
assert threshold_num==10031>0

DT=D*TNUM//TDEN
assert DT==13472 and D*TNUM % TDEN==0
Mnum=DT*np.eye(n,dtype=np.int64)-Bnum
assert np.array_equal(Mnum,Mnum.T)

# Candidate factor generation only; exact acceptance is the residual check.
Lf=np.linalg.cholesky(Mnum.astype(float)-SLACK*np.eye(n))
Lq=np.rint(Q*Lf).astype(np.int64)
maxL=int(np.max(np.abs(Lq)))
dot_safety=n*maxL*maxL
assert dot_safety<2**63
LL=Lq@Lq.T
Rnum=Q*Q*(Mnum-SLACK*np.eye(n,dtype=np.int64))-LL
maxentry=int(np.max(np.abs(Rnum)))
assert n*maxentry<2**63
maxrowsum=int(np.max(np.sum(np.abs(Rnum),axis=1,dtype=np.int64)))

# Exact identity:
# Mnum = (Lq/Q)(Lq/Q)^T + SLACK*I + Rnum/Q^2.
# Since Rnum is symmetric, ||Rnum||_2 <= ||Rnum||_infty=maxrowsum.
# maxrowsum < SLACK*Q^2 proves Mnum positive definite.
assert maxrowsum < SLACK*Q*Q
residual_slack=SLACK*Q*Q-maxrowsum
assert maxL==939298
assert maxentry==1800259
assert maxrowsum==286611012
assert residual_slack==48933308
assert hashlib.sha256(Lq.tobytes(order="C")).hexdigest()=="db4780f8cbe80bf2c494d908f3a7aaa28b40ef8bec661b05c04adb72f11ebb35"

print("P04-I0101-P4013-S3-ORBIT-DUAL=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"edges={edges}")
print(f"nonedges={nonedges}")
print(f"vertex_orbit_size_census={sorted(Counter(vertex_orbit_sizes).items())}")
print(f"nonedge_orbits={len(orbits)}")
print(f"nonedge_orbit_size_census={sorted(Counter(map(len,orbits)).items())}")
print(f"weight_range={int(weights.min())}..{int(weights.max())} over denominator {WDEN}")
print(f"weight_sha256={hashlib.sha256(weight_bytes).hexdigest()}")
print(f"t={TNUM}/{TDEN}")
print(f"threshold_numerator_400p_minus_9Tnum2={threshold_num}")
print(f"Q={Q}")
print(f"SLACK_scaled={SLACK}")
print(f"max_abs_Lq={maxL}")
print(f"dot_product_safety_bound={dot_safety}")
print(f"max_abs_Rnum={maxentry}")
print(f"max_row_abs_sum_Rnum={maxrowsum}")
print(f"exact_residual_slack={residual_slack}")
print("EXACT_RESIDUAL_PD=PASS")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print("FREE_VERTEX_ORBITS_5MOD24=PASS")
print("THETA_LT_421_OVER_10_LT_2SQRT_P_OVER_3=PASS")
