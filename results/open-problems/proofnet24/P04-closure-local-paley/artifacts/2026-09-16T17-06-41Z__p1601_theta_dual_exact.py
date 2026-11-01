#!/usr/bin/env python3
# Exact finite certificate for Randomstrasse Conjecture 27 at p=1601.
# Stdlib only. Candidate weights are in the adjacent .b64 payload.
# All PSD checks use Python arbitrary-precision integers.

import base64, zlib
from pathlib import Path

P=1601
T=26
SCALE=8
PAYLOAD_PATH=Path(__file__).with_name("2026-09-16T17-06-41Z__p1601_theta_dual_weights.b64")

def is_prime(n):
    if n < 2: return False
    q=2
    while q*q <= n:
        if n%q==0: return False
        q += 1
    return True

def bareiss_spd(A):
    A=[row[:] for row in A]
    n=len(A)
    prev=1
    for k in range(n-1):
        pivot=A[k][k]
        assert pivot > 0, ("nonpositive pivot", k)
        for i in range(k+1,n):
            aik=A[i][k]
            for j in range(i,n):
                num=A[i][j]*pivot-aik*A[k][j]
                assert num % prev == 0, ("nonexact Bareiss division",k,i,j)
                v=num//prev
                A[i][j]=v
                A[j][i]=v
        prev=pivot
    assert A[-1][-1] > 0
    return A[-1][-1].bit_length()

assert is_prime(P) and P%4==1
qr={(x*x)%P for x in range(1,P)}
V=[x for x in range(P) if x in qr and (x-1)%P in qr]
n=len(V)
assert n==(P-5)//4==399
idx={x:i for i,x in enumerate(V)}
tau=[idx[(1-x)%P] for x in V]
fixed=[i for i,j in enumerate(tau) if i==j]
assert len(fixed)==1

payload=PAYLOAD_PATH.read_text().strip()
raw=zlib.decompress(base64.b64decode(payload))
assert len(raw)==10000
weights=[]
for c in raw:
    weights.extend((c>>4,c&15))
assert len(weights)==20000 and min(weights)>=1 and max(weights)<=15

B=[[0]*n for _ in range(n)]
for i in range(n):
    B[i][i]=SCALE*(T-1)
for i in range(n):
    for j in range(i+1,n):
        if (V[i]-V[j])%P in qr:
            B[i][j]=B[j][i]=-SCALE

seen=set()
pos=0
for i in range(n):
    for j in range(i+1,n):
        if (V[i]-V[j])%P in qr or (i,j) in seen:
            continue
        q=weights[pos]; pos+=1
        a,b=sorted((tau[i],tau[j]))
        assert (V[a]-V[b])%P not in qr
        B[i][j]=B[j][i]=q
        B[a][b]=B[b][a]=q
        seen.add((i,j)); seen.add((a,b))
assert pos==20000

edge_pairs=nonedge_pairs=0
for i in range(n):
    for j in range(i+1,n):
        if (V[i]-V[j])%P in qr:
            edge_pairs+=1
            assert B[i][j]==-SCALE
        else:
            nonedge_pairs+=1
            assert (i,j) in seen and 1<=B[i][j]<=15
        assert B[tau[i]][tau[j]]==B[i][j]

pairs=[]
used=set(fixed)
for i in range(n):
    if i in used: continue
    j=tau[i]
    a,b=sorted((i,j))
    assert a!=b and a not in used and b not in used
    pairs.append((a,b))
    used.add(a); used.add(b)
assert len(pairs)==199 and len(used)==399

# Integer congruence basis: fixed vector and e_i+e_tau(i) form the even block;
# e_i-e_tau(i) form the odd block. tau-invariance makes cross blocks zero.
E=[[0]*200 for _ in range(200)]
O=[[0]*199 for _ in range(199)]
f=fixed[0]
E[0][0]=B[f][f]
for a,(i,ti) in enumerate(pairs):
    E[0][a+1]=E[a+1][0]=B[f][i]+B[f][ti]
    for b,(j,tj) in enumerate(pairs):
        E[a+1][b+1]=B[i][j]+B[i][tj]+B[ti][j]+B[ti][tj]
        O[a][b]=B[i][j]-B[i][tj]-B[ti][j]+B[ti][tj]
        cross=B[i][j]-B[i][tj]+B[ti][j]-B[ti][tj]
        assert cross==0

ebits=bareiss_spd(E)
obits=bareiss_spd(O)

# Exact source comparison T <= (2/3)sqrt(P).
lhs=9*T*T
rhs=4*P
assert lhs <= rhs

print(f"P={P}")
print(f"LOCALIZATION_N={n}")
print(f"TAU_FIXED_VERTICES={len(fixed)}")
print(f"TAU_TWO_CYCLES={len(pairs)}")
print(f"TAU_NONEDGE_ORBITS={pos}")
print(f"EDGE_PAIRS={edge_pairs}")
print(f"NONEDGE_PAIRS={nonedge_pairs}")
print(f"DUAL_T={T}")
print(f"SCALE={SCALE}")
print(f"THRESHOLD_SQUARED_CHECK={lhs}<={rhs}")
print("EVEN_BLOCK_DIM=200")
print("ODD_BLOCK_DIM=199")
print("EVEN_BAREISS_SPD=PASS")
print("ODD_BAREISS_SPD=PASS")
print(f"EVEN_FINAL_PIVOT_BITS={ebits}")
print(f"ODD_FINAL_PIVOT_BITS={obits}")
print("CERTIFICATE=PASS")
