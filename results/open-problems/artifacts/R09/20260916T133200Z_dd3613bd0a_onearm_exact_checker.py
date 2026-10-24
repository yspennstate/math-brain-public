#!/usr/bin/env python3
"""
R09 exact checker: finite-radius one-arm reliability on nearest-neighbor Z^3.

All arithmetic is exact Python integers/Fractions. No simulation.

For r=1,2,3 let U_r(p) = P_p(0 connects to the l1-sphere S_r).
The checker:
  * constructs S_1,S_2,S_3 exactly;
  * derives the exact failure expansion for U_2 and U_3 by conditioning
    layer-by-layer;
  * evaluates U_r(1/2) exactly;
  * independently checks the r=2 union-size formula;
  * exhaustively checks the finite-volume parameter-shift inequality
    for every monotone Boolean function on 3 bits at several rational p,q;
  * certifies a finite configuration showing one arm does not imply a
    robust multi-face/two-arm block crossing.
"""
from itertools import product
from collections import defaultdict
from fractions import Fraction
import hashlib, json

DIRS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

def add(x,y):
    return tuple(x[i]+y[i] for i in range(3))

def l1(x):
    return sum(abs(a) for a in x)

def shell(r):
    return tuple(sorted(
        x for x in product(range(-r,r+1), repeat=3) if l1(x)==r
    ))

S1,S2,S3=shell(1),shell(2),shell(3)
assert (len(S1),len(S2),len(S3))==(6,18,38)

adj12={x:set(add(x,d) for d in DIRS).intersection(S2) for x in S1}
adj23={x:set(add(x,d) for d in DIRS).intersection(S3) for x in S2}
assert all(len(adj12[x])==5 for x in S1)
assert all(len(adj23[x]) in (4,5) for x in S2)

# Failure expansion conditional on the origin being open.
# A term (a,b)->c means c * p^a * (1-p)^b.
fail2=defaultdict(int)
fail3=defaultdict(int)

def opposite_pairs(sel):
    S=set(sel)
    return sum(
        1 for x in S
        if tuple(-z for z in x) in S
    )//2

for mask in range(1<<len(S1)):
    open1=tuple(S1[i] for i in range(len(S1)) if (mask>>i)&1)
    k=len(open1)
    U=set()
    for x in open1:
        U.update(adj12[x])

    # Each selected S1 site has 5 outward S2 neighbours; a non-opposite
    # pair shares exactly one; an opposite pair shares none; no S2 site
    # belongs to more than two such neighbour sets.
    opp=opposite_pairs(open1)
    predicted=5*k-(k*(k-1))//2+opp
    assert len(U)==predicted

    fail2[(k, (6-k)+len(U))]+=1

    Ulist=tuple(sorted(U))
    for tmask in range(1<<len(Ulist)):
        open2=tuple(Ulist[i] for i in range(len(Ulist)) if (tmask>>i)&1)
        ell=len(open2)
        V=set()
        for x in open2:
            V.update(adj23[x])
        # unselected S1 sites are closed; U\open2 are closed;
        # all S3 sites adjacent to open2 are closed.
        fail3[(k+ell, (6-k)+(len(U)-ell)+len(V))]+=1

assert sum(fail2.values())==64
assert sum(fail3.values())==1778881
assert len(fail2)==10
assert len(fail3)==208

expected_fail2={
    (0,6):1,(1,10):6,(2,13):12,(2,14):3,(3,15):8,
    (3,16):12,(4,17):12,(4,18):3,(5,18):6,(6,18):1
}
assert dict(fail2)==expected_fail2

def eval_fail(dist,p):
    q=1-p
    return sum(Fraction(c)*p**a*q**b for (a,b),c in dist.items())

half=Fraction(1,2)
U1=half*(1-(1-half)**6)
U2=half*(1-eval_fail(fail2,half))
U3=half*(1-eval_fail(fail3,half))

assert U1==Fraction(63,128)
assert U2==Fraction(16457991,33554432)
assert U3==Fraction(4517544707082764121,9223372036854775808)
assert U3 < U2 < U1 < 1

# Exact finite-volume passage self-check:
# for every monotone Boolean event A on n=3 coordinates,
# mu_p(A)-mu_q(A) <= 1-(1-(p-q))^n <= n(p-q).
def is_monotone(vals,n):
    for x in range(1<<n):
        for i in range(n):
            if ((x>>i)&1)==0 and vals[x] > vals[x|(1<<i)]:
                return False
    return True

def mu(vals,n,p):
    q=1-p
    out=Fraction(0)
    for x in range(1<<n):
        k=x.bit_count()
        if vals[x]:
            out += p**k*q**(n-k)
    return out

for q,p in [
    (Fraction(1,10),Fraction(1,5)),
    (Fraction(1,3),Fraction(1,2)),
    (Fraction(2,5),Fraction(9,10)),
]:
    for mask in range(1<<(1<<3)):
        vals=tuple((mask>>x)&1 for x in range(1<<3))
        if not is_monotone(vals,3):
            continue
        diff=mu(vals,3,p)-mu(vals,3,q)
        coupling=1-(1-(p-q))**3
        assert diff <= coupling
        assert coupling <= 3*(p-q)

# Exact finite configuration obstruction to "one arm => robust block crossing".
# In Lambda_3, open only 0,e1,2e1,3e1.
L=3
open_line={(i,0,0) for i in range(L+1)}
boundary={
    x for x in product(range(-L,L+1), repeat=3)
    if max(abs(a) for a in x)==L
}
reached_faces=set()
for x in open_line & boundary:
    if x[0]== L: reached_faces.add("+x")
    if x[0]==-L: reached_faces.add("-x")
    if x[1]== L: reached_faces.add("+y")
    if x[1]==-L: reached_faces.add("-y")
    if x[2]== L: reached_faces.add("+z")
    if x[2]==-L: reached_faces.add("-z")
assert open_line & boundary
assert reached_faces=={"+x"}
assert (1,0,0) in open_line
remaining=open_line-{(1,0,0)}
seen={(0,0,0)}
stack=[(0,0,0)]
while stack:
    x=stack.pop()
    for d in DIRS:
        y=add(x,d)
        if y in remaining and y not in seen:
            seen.add(y); stack.append(y)
assert not (seen & boundary)
print("finite one-arm !=> robust multi-face/two-arm crossing obstruction: PASS")

payload={
    "S_sizes":[len(S1),len(S2),len(S3)],
    "fail2_terms":sorted((a,b,c) for (a,b),c in fail2.items()),
    "fail3_terms":sorted((a,b,c) for (a,b),c in fail3.items()),
    "U_half":[
        [U1.numerator,U1.denominator],
        [U2.numerator,U2.denominator],
        [U3.numerator,U3.denominator],
    ],
}
digest=hashlib.sha256(
    json.dumps(payload,separators=(",",":"),sort_keys=True).encode()
).hexdigest()

print("R09 exact finite-radius one-arm checker: PASS")
print("shell sizes:", len(S1), len(S2), len(S3))
print("failure term counts:", len(fail2), len(fail3))
print("raw layer-3 conditional cases:", sum(fail3.values()))
print("U1(1/2) =", U1, "=", float(U1))
print("U2(1/2) =", U2, "=", float(U2))
print("U3(1/2) =", U3, "=", float(U3))
print("strict nesting U3<U2<U1: PASS")
print("3-bit monotone-event parameter-shift exhaustive audit: PASS")
print("certificate_sha256 =", digest)
