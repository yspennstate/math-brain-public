#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from collections import Counter
import math


def enumerate_regular_graphs(n,d):
    adj=[0]*n
    rem=[d]*n
    out=[]
    # Vertex-by-vertex canonical recursion: satisfy the least vertex with
    # remaining degree. Each labeled simple graph appears exactly once.
    def rec(v):
        while v<n and rem[v]==0:
            v+=1
        if v==n:
            if all(x==0 for x in rem):
                out.append(tuple(adj))
            return
        need=rem[v]
        cand=[j for j in range(v+1,n) if rem[j]>0 and not (adj[v]>>j)&1]
        if len(cand)<need:
            return
        for js in combinations(cand,need):
            ok=True
            for j in js:
                adj[v]|=1<<j
                adj[j]|=1<<v
                rem[j]-=1
                if rem[j]<0:
                    ok=False
            old=rem[v]
            rem[v]=0
            if ok:
                rec(v+1)
            rem[v]=old
            for j in js:
                rem[j]+=1
                adj[v]&=~(1<<j)
                adj[j]&=~(1<<v)
    rec(0)
    return out


def cut(adj,S):
    n=len(adj)
    mask=sum(1<<i for i in S)
    return sum((adj[i] & ~mask & ((1<<n)-1)).bit_count() for i in S)


def minmax_bis(adj):
    n=len(adj)
    k=n//2
    vals=[]
    # Quotient by complementary bisections: insist 0 in S.
    for tail in combinations(range(1,n),k-1):
        vals.append(cut(adj,(0,)+tail))
    return min(vals),max(vals)


def analyze(n,d):
    gs=enumerate_regular_graphs(n,d)
    pairs=Counter(minmax_bis(g) for g in gs)
    N=len(gs)
    smin=sum(a*c for (a,b),c in pairs.items())
    smax=sum(b*c for (a,b),c in pairs.items())
    amin=Fraction(smin,N)
    amax=Fraction(smax,N)
    delta=(amin+amax)/n-Fraction(d,2)
    return N,pairs,amin,amax,delta


expected={
    (4,3):(1, Fraction(4),Fraction(4),Fraction(1,2)),
    (6,3):(70,Fraction(23,7),Fraction(51,7),Fraction(11,42)),
    (8,3):(19355,Fraction(2064,553),Fraction(5576,553),Fraction(251,1106)),
    (6,4):(15,Fraction(6),Fraction(8),Fraction(1,3)),
}
for key,(Nexp,mnexp,mxexp,dexp) in expected.items():
    n,d=key
    N,pairs,mn,mx,delta=analyze(n,d)
    assert N==Nexp,(key,N,Nexp)
    assert mn==mnexp,(key,mn,mnexp)
    assert mx==mxexp,(key,mx,mxexp)
    assert delta==dexp,(key,delta,dexp)
    print(f"n={n} d={d} graphs={N} avgMin={mn} avgMax={mx} delta={delta} pairs={dict(sorted(pairs.items()))}")

# Complement bijection on n=8 sends 3-regular labeled graphs bijectively to
# 4-regular labeled graphs. For a balanced S,
# cut_{G^c}(S)=n^2/4-cut_G(S), so delta_{8,4}=1/2-delta_{8,3}.
delta84=Fraction(1,2)-Fraction(251,1106)
assert delta84==Fraction(151,553)
print(f"n=8 d=4 via complement bijection delta={delta84}")
print("SMALL_GRAPH_EXACT_CHECKS_PASS")

# Configuration-model pairing identity for a fixed balanced vertex partition.
# There are M=dn/2 half-edges on each side. If k cross-edges occur, then M-k
# must be even. The exact number of perfect pairings realizing k cross-edges is
# C(M,k)^2 k! ((M-k)-1)!!^2
# = M! C(M,k) 2^{-(M-k)} C(M-k,(M-k)/2).
def odd_dfact(r):
    if r <= 0:
        return 1
    z=1
    for t in range(r,0,-2):
        z*=t
    return z


def pairing_count(M,k):
    if k<0 or k>M or (M-k)%2:
        return 0
    return math.comb(M,k)**2*math.factorial(k)*odd_dfact(M-k-1)**2


def pairing_count_alt(M,k):
    if k<0 or k>M or (M-k)%2:
        return 0
    r=M-k
    return math.factorial(M)*math.comb(M,k)*math.comb(r,r//2)//(2**r)


for M in range(2,13):
    counts=[]
    for k in range(M+1):
        a=pairing_count(M,k)
        b=pairing_count_alt(M,k)
        assert a==b,(M,k,a,b)
        counts.append(a)
    assert sum(counts)==odd_dfact(2*M-1),(M,sum(counts),odd_dfact(2*M-1))
    if M%2==0:
        for k in range(0,M+1,2):
            r=M-k
            ak=Fraction(math.comb(k,k//2),2**k)
            ar=Fraction(math.comb(r,r//2),2**r)
            assert Fraction(pairing_count(M,k),pairing_count(M,M-k))==ar/ak
print("PAIRING_REFLECTION_IDENTITY_PASS")
print("ALL_EXACT_CHECKS_PASS")
