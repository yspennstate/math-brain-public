#!/usr/bin/env python3
"""Exact p=1009 finite dual certificate for P04/I0101.

This is a finite exact certificate for Randomstrasse 2025 Conjecture 27's
inequality at p=1009 only. It does not prove the eventual quantifier.

The frozen nonedge-orbit weights are compressed below only to keep this
artifact compact. Acceptance uses integer arithmetic throughout.
"""
import base64, zlib

P=1009
T=21
DATA="""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"""
CERT_ITEMS=[tuple(map(int,line.split(","))) for line in zlib.decompress(base64.b64decode(DATA)).decode().splitlines()]
CERT={(a,b):w for a,b,w in CERT_ITEMS}
assert len(CERT_ITEMS)==len(CERT)==2664

def is_prime(n):
    if n<2: return False
    q=2
    while q*q<=n:
        if n%q==0: return False
        q+=1
    return True

def legendre_symbol(a,p):
    a%=p
    if a==0: return 0
    v=pow(a,(p-1)//2,p)
    assert v in (1,p-1)
    return 1 if v==1 else -1

def canonical_pair(a,b,p):
    start=tuple(sorted((a,b)))
    seen={start}
    stack=[start]
    while stack:
        u,v=stack.pop()
        for x,y in (((1-u)%p,(1-v)%p),(pow(u,-1,p),pow(v,-1,p))):
            pair=tuple(sorted((x,y)))
            if pair not in seen:
                seen.add(pair); stack.append(pair)
    return min(seen)

def bareiss_positive_leading_minors(M):
    A=[row[:] for row in M]
    n=len(A); prev=1; piv=[]
    for k in range(n-1):
        pivot=A[k][k]
        piv.append(pivot)
        assert pivot>0,("nonpositive leading determinant",k+1,pivot)
        for i in range(k+1,n):
            aik=A[i][k]
            for j in range(i,n):
                num=A[i][j]*pivot-aik*A[k][j]
                assert num%prev==0,("Bareiss nondivisibility",k,i,j)
                val=num//prev
                A[i][j]=val; A[j][i]=val
        prev=pivot
    piv.append(A[n-1][n-1])
    assert piv[-1]>0
    return piv

assert is_prime(P) and P%4==1
V=[x for x in range(P) if legendre_symbol(x,P)==1 and legendre_symbol(x-1,P)==1]
n=len(V)
assert n==(P-5)//4==251
idx={x:i for i,x in enumerate(V)}

A=[[0]*n for _ in range(n)]
edges=0
for i,x in enumerate(V):
    for j in range(i+1,n):
        y=V[j]
        if legendre_symbol(x-y,P)==1:
            A[i][j]=A[j][i]=1; edges+=1
assert edges==15576

rep_counts={}
for i,x in enumerate(V):
    for j in range(i+1,n):
        if A[i][j]==0:
            rep=canonical_pair(x,V[j],P)
            rep_counts[rep]=rep_counts.get(rep,0)+1
assert len(rep_counts)==2664
assert sum(rep_counts.values())==15799
orbit_size_counts={}
for s in rep_counts.values(): orbit_size_counts[s]=orbit_size_counts.get(s,0)+1
assert orbit_size_counts=={1:1,3:60,6:2603}
assert set(rep_counts)==set(CERT)
assert set(CERT.values())=={-5,-4,-3,-2,-1,0,1,2,3}

B=[[0]*n for _ in range(n)]
for i in range(n): B[i][i]=1
for i,x in enumerate(V):
    for j in range(i+1,n):
        w=1 if A[i][j] else CERT[canonical_pair(x,V[j],P)]
        B[i][j]=B[j][i]=w

for i in range(n):
    assert B[i][i]==1
    for j in range(i+1,n):
        if A[i][j]: assert B[i][j]==1

for f in (lambda x:(1-x)%P, lambda x:pow(x,-1,P)):
    perm=[idx[f(x)] for x in V]
    for i in range(n):
        for j in range(n):
            assert B[perm[i]][perm[j]]==B[i][j]

M=[[(T if i==j else 0)-B[i][j] for j in range(n)] for i in range(n)]
pivots=bareiss_positive_leading_minors(M)
assert len(pivots)==n and all(x>0 for x in pivots)
threshold_numerator=4*P-9*T*T
assert threshold_numerator==67>0

seen=set(); vertex_orbit_sizes=[]
for x in V:
    if x in seen: continue
    orb=set(); stack=[x]
    while stack:
        y=stack.pop()
        if y in orb: continue
        orb.add(y)
        stack.extend(((1-y)%P,pow(y,-1,P)))
    seen|=orb; vertex_orbit_sizes.append(len(orb))
assert sorted(vertex_orbit_sizes)==[2,3]+[6]*41

weight_counts={}
for w in CERT.values(): weight_counts[w]=weight_counts.get(w,0)+1

print("P04-I0101-P1009-S3-ORBIT-DUAL=PASS")
print(f"p={P} n={n} edges={edges} nonedges={sum(rep_counts.values())}")
print(f"nonedge_pair_orbits={len(rep_counts)} orbit_size_counts={orbit_size_counts}")
print(f"vertex_orbit_sizes={sorted(vertex_orbit_sizes)}")
print(f"certificate_weight_counts={dict(sorted(weight_counts.items()))}")
print(f"t={T} exact_threshold_numerator_4p_minus_9t2={threshold_numerator}")
print(f"bareiss_positive_leading_minors={len(pivots)}")
print(f"last_leading_determinant_bits={pivots[-1].bit_length()}")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print("SYLVESTER_BAREISS_PD=PASS")
print("THETA_LT_21_LT_2SQRT_P_OVER_3=PASS")
