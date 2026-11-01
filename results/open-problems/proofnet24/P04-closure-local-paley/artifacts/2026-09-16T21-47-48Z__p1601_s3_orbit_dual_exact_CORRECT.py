#!/usr/bin/env python3
"""Canonical exact p=1601 dual certificate for P04/I0101.

This finite certificate proves the Randomstrasse101 Conjecture-27 inequality
at p=1601 only; it does not prove the eventual quantifier.

The certificate stores one integer weight for each S3-orbit of unordered
nonedges, ordered by the lexicographically least pair in that orbit. All
acceptance tests below are integer/exact.
"""
from collections import Counter, deque
import base64, hashlib, zlib

P=1601
T=26
OFFSET=8
ORBIT_WEIGHTS_ZLIB_B64="""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"""
EXPECTED_RAW_SHA256="f7be291c7b1d2f21f1313708fd6e70039b174b7ed32930d71bee563ebb046f3f"

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    q=3
    while q*q<=n:
        if n%q==0: return False
        q+=2
    return True

def chi(a):
    a%=P
    if a==0: return 0
    v=pow(a,(P-1)//2,P)
    assert v in (1,P-1)
    return 1 if v==1 else -1

assert is_prime(P) and P%4==1
V=[x for x in range(P) if x not in (0,1) and chi(x)==chi(x-1)==1]
assert len(V)==399==(P-5)//4
idx={x:i for i,x in enumerate(V)}
n=len(V)
A=[[0]*n for _ in range(n)]
nonedges=[]
edges=0
for i,x in enumerate(V):
    for j in range(i+1,n):
        if chi(x-V[j])==1:
            A[i][j]=A[j][i]=1
            edges+=1
        else:
            nonedges.append((i,j))
assert edges==39501 and len(nonedges)==39900

def r(x): return (1-x)%P
def s(x): return pow(x,-1,P)
def cp(i,j): return (i,j) if i<j else (j,i)

# Verify the actual graph automorphisms.
for x in V:
    assert r(x) in idx and s(x) in idx
for i,x in enumerate(V):
    for j in range(i+1,n):
        a=A[i][j]
        for f in (r,s):
            ni,nj=idx[f(x)],idx[f(V[j])]
            assert A[ni][nj]==a

# Deterministically enumerate S3-orbits of unordered nonedges.
unseen=set(nonedges)
orbit_records=[]
while unseen:
    seed=min(unseen)
    q=deque([seed])
    orb=set()
    while q:
        i,j=q.popleft()
        pair=cp(i,j)
        if pair in orb: continue
        orb.add(pair)
        x,y=V[pair[0]],V[pair[1]]
        for f in (r,s):
            ni,nj=idx[f(x)],idx[f(y)]
            npair=cp(ni,nj)
            assert npair in unseen or npair in orb
            if npair not in orb:
                q.append(npair)
    rep=min(orb)
    orbit_records.append((rep,tuple(sorted(orb))))
    unseen.difference_update(orb)
orbit_records.sort(key=lambda z:z[0])
assert len(orbit_records)==6700
orbit_size_counts=Counter(len(orb) for rep,orb in orbit_records)
assert orbit_size_counts==Counter({6:6600,3:100})

raw=zlib.decompress(base64.b64decode(ORBIT_WEIGHTS_ZLIB_B64))
assert hashlib.sha256(raw).hexdigest()==EXPECTED_RAW_SHA256
assert len(raw)==len(orbit_records)
orbit_weights=[int(b)-OFFSET for b in raw]
assert Counter(orbit_weights)==Counter({-6: 2, -5: 27, -4: 120, -3: 431, -2: 1299, -1: 2229, 0: 1898, 1: 640, 2: 52, 3: 2})

pair_weight={}
for (rep,orb),w in zip(orbit_records,orbit_weights):
    for pair in orb:
        pair_weight[pair]=w
assert len(pair_weight)==len(nonedges)
assert Counter(pair_weight.values())==Counter({-6: 12, -5: 162, -4: 711, -3: 2556, -2: 7731, -1: 13302, 0: 11310, 1: 3804, 2: 303, 3: 9})

# Exact conserved anharmonic sign multiset on nonedge pairs.
class_counts=Counter()
for i,j in nonedges:
    x,y=V[i],V[j]
    sig=tuple(sorted((chi(x*y-1),chi(x*y-x-y),chi(x+y-1))))
    class_counts[sig]+=1
assert class_counts==Counter({(-1, -1, -1): 5154, (-1, -1, 0): 147, (-1, -1, 1): 14748, (-1, 1, 1): 14856, (0, 1, 1): 153, (1, 1, 1): 4842})

# Edge-fixed dual matrix.
B=[[0]*n for _ in range(n)]
for i in range(n): B[i][i]=1
for i in range(n):
    for j in range(i+1,n):
        v=1 if A[i][j] else pair_weight[(i,j)]
        B[i][j]=B[j][i]=v

# Full S3 invariance of certificate.
for i,x in enumerate(V):
    for j,y in enumerate(V):
        assert B[idx[r(x)]][idx[r(y)]]==B[i][j]
        assert B[idx[s(x)]][idx[s(y)]]==B[i][j]

# M=T I-B. Symmetric Bareiss pivots are leading principal determinants.
M=[[(T if i==j else 0)-B[i][j] for j in range(n)] for i in range(n)]
def symmetric_bareiss_leading_dets(M):
    X=[row[:] for row in M]
    N=len(X); prev=1; out=[]
    for k in range(N-1):
        pivot=X[k][k]
        assert pivot>0,(k,pivot)
        out.append(pivot)
        for i in range(k+1,N):
            aik=X[i][k]
            for j in range(i,N):
                num=X[i][j]*pivot-aik*X[k][j]
                assert num%prev==0
                val=num//prev
                X[i][j]=X[j][i]=val
        prev=pivot
    assert X[N-1][N-1]>0
    out.append(X[N-1][N-1])
    return out

leading=symmetric_bareiss_leading_dets(M)
assert len(leading)==399 and all(v>0 for v in leading)
margin=4*P-9*T*T
assert margin==320>0

print("P04-I0101-P1601-S3-ORBIT-DUAL=PASS")
print(f"p={P} n={n} edges={edges} nonedges={len(nonedges)}")
print(f"nonedge_pair_orbit_size_counts={dict(sorted(orbit_size_counts.items()))}")
print(f"orbit_weight_counts={dict(sorted(Counter(orbit_weights).items()))}")
print(f"pair_weight_counts={dict(sorted(Counter(pair_weight.values()).items()))}")
print(f"anharmonic_sign_class_counts={dict(sorted(class_counts.items()))}")
print(f"t={T} exact_threshold_numerator_4p_minus_9t2={margin}")
print(f"bareiss_positive_leading_minors={len(leading)}")
print(f"final_determinant_digits={len(str(leading[-1]))}")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print("ANHARMONIC_INVARIANT_COUNTS=PASS")
print("SYLVESTER_BAREISS_PD=PASS")
print("THETA_LT_26_LT_2SQRT_P_OVER_3=PASS")
