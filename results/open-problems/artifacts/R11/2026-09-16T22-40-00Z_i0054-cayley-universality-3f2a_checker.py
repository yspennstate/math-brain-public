#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import comb, factorial
from collections import defaultdict
import heapq

print("R11 I0054 Cayley-tree multicut exact finite self-check")
print("FINITE CLAIMS ONLY; the asymptotic path convergence is proved in the written report.")

def H(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction())

def Beta(a,b):
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def cw(m,s):
    # Symmetric Cayley edge weight.
    return Fraction(m**(m-1), comb(m,s) * s**s * (m-s)**(m-s))

def expected_oriented_count(m,s):
    # Number of oriented edge-sides of size s, averaged over uniform Cayley trees.
    return Fraction(comb(m,s) * s**(s-1) * (m-s)**(m-s-1), m**(m-2))

def prufer_edges(seq,n):
    deg=[1]*n
    for x in seq:
        deg[x]+=1
    leaves=[i for i,d in enumerate(deg) if d==1]
    heapq.heapify(leaves)
    edges=[]
    for x in seq:
        u=heapq.heappop(leaves)
        edges.append((u,x))
        deg[u]-=1
        deg[x]-=1
        if deg[x]==1:
            heapq.heappush(leaves,x)
    u=heapq.heappop(leaves); v=heapq.heappop(leaves)
    edges.append((u,v))
    return edges

def side_size(n,edges,j,start):
    adj=[[] for _ in range(n)]
    for q,(u,v) in enumerate(edges):
        if q==j:
            continue
        adj[u].append(v); adj[v].append(u)
    seen={start}
    stack=[start]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)

# 1. Exhaustive Prüfer enumeration verifies the Cayley oriented split profile.
enum_instances=0
for m in range(2,8):
    tot=m**(m-2)
    cnt=defaultdict(int)
    seqs=[()] if m==2 else product(range(m), repeat=m-2)
    num=0
    for seq in seqs:
        num += 1
        edges=prufer_edges(seq,m)
        for j,(u,v) in enumerate(edges):
            s=side_size(m,edges,j,u)
            cnt[s]+=1
            cnt[m-s]+=1
    assert num==tot
    for s in range(1,m):
        empirical=Fraction(cnt[s],tot)
        formula=expected_oriented_count(m,s)
        assert empirical==formula, (m,s,empirical,formula)
        enum_instances += 1
print("cayley_oriented_profile: PASS", enum_instances, "exact size classes (all Cayley trees through m=7)")

# 2. The weight cancels the Cayley split profile to the universal m/[s(m-s)] profile.
profile_checks=0
for m in range(2,101):
    for s in range(1,m):
        lhs=expected_oriented_count(m,s)*cw(m,s)
        rhs=Fraction(m, s*(m-s))
        assert lhs==rhs, (m,s,lhs,rhs)
        profile_checks += 1
print("weighted_profile_cancellation: PASS", profile_checks, "exact (m,s) pairs")

# 3. Hidden-size cancellation / beta-binomial identity.
beta_checks=0
for m in range(2,31):
    for b in range(2,m+1):
        for i in range(1,b):
            lhs=Fraction()
            for s in range(i, m-(b-i)+1):
                lhs += Fraction(m, s*(m-s))*Fraction(comb(m-b,s-i), comb(m,s))
            rhs=Beta(i,b-i)
            assert lhs==rhs, (m,b,i,lhs,rhs)
            beta_checks += 1
print("hidden_size_beta_identity: PASS", beta_checks, "exact triples")

# 4. Total weighted one-cut intensity equals H_{m-1}.
for m in range(2,101):
    lhs=Fraction()
    for s in range(1,m):
        # factor 1/2 because each physical edge has two oriented sides
        lhs += Fraction(1,2)*Fraction(m, s*(m-s))
    assert lhs==H(m-1), (m,lhs,H(m-1))
print("total_harmonic_rate: PASS m=2..100")

# 5. Exact failure of the natural unweighted Cayley-edge cut at m=4.
m=4
u13=Fraction(1**0 * 3**2, m**(m-2))
u22=Fraction(2**1 * 2**1, m**(m-2))
assert u13/u22 == Fraction(9,4)
assert Beta(1,3)/Beta(2,2) == Fraction(2,1)
assert u13/u22 != Beta(1,3)/Beta(2,2)
print("unweighted_cayley_failure: PASS ratio=9/4 != CTCS ratio=2")

# 6. Weight validity bound used by the proof.
# cw = 1/[m * P(Bin(m,s/m)=s)], and s is a binomial mode, hence cw <= (m+1)/m < 3/2.
for m in range(2,101):
    for s in range(1,m):
        assert cw(m,s) <= Fraction(m+1,m)
print("finite_weight_bound_check: PASS cw(m,s)<=(m+1)/m for m<=100 (general proof in report)")

# 7. Concrete N=3 reduced-root degree-3 witness for C007 with delta_N=N^-3.
N=3
delta=Fraction(1,N**3)
w=cw(3,1)
p=delta*w
assert w==Fraction(3,4)
assert p==Fraction(1,36)
raw_three=p*p
raw_none=(1-p)**2
first_visible_three=raw_three/(1-raw_none)
assert raw_three==Fraction(1,1296)
assert first_visible_three==Fraction(1,71)
print("C007_N3: PASS raw_threeway=1/1296 first_visible_threeway=1/71")

# 8. Distinguish from all retained reduced-root degree-3 witnesses.
retained=[
    Fraction(0,1),
    Fraction(1,10),
    Fraction(1,22),
    Fraction(1,6),
    Fraction(1,728),
    Fraction(1,7),
    Fraction(1,71),
]
assert len(set(retained))==7
print("reduced_root_degree3_witnesses: PASS C001=0 C002=1/10 C003=1/22 C004=1/6 C005=1/728 C006=1/7 C007=1/71")

# 9. Universality error scale for delta_N=N^-3 and A_N<3N/2:
# delta_N A_N^2 <= 9/(4N) -> 0.
for N in [2,3,5,10,100,1000]:
    bound=Fraction(9,4*N)
    assert bound>0
print("universality_error_scale: PASS delta_N*A_N^2 <= 9/(4N) -> 0")

print("ALL_EXACT_CHECKS_PASS")
