#!/usr/bin/env python3
"""
R03 run33 exact checker: previously uncredited overlap-one sign-relation planes.

Finite scope:
- m=10 binary reduction, p=11.
- Enumerate arbitrary projective +/-1 relation types (s,k), k=min(#plus,#minus).
- Enumerate overlap-one two-line planes, excluding every overlap-one balanced plane
  already credited by run18/run21.
- Compute local affine-slice fiber caps exactly over F_11.
- Apply the proved greedy-basis lower bound to certify exact left modular nullity 2.
- Reclaim the full 11-line C253 slack for these previously uncredited planes.
"""

from itertools import product
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from math import comb
from decimal import Decimal, getcontext

getcontext().prec = 60

M = 10
P = 11

def projective_vectors(dim, p):
    for first in range(dim):
        for tail in product(range(p), repeat=dim-first-1):
            yield (0,)*first + (1,) + tail

def rel_classes(s, k):
    # Orient the overlap coefficient to +1.
    # class tuple: name, number of projective lines on fixed support with
    # overlap in this class, residual #(+1), residual #(-1).
    if 2*k == s:
        return (("even", comb(s-1, k-1), k-1, k),)
    return (
        ("minority", comb(s-1, k-1), k-1, s-k),
        ("majority", comb(s-1, k), s-k-1, k),
    )

@lru_cache(None)
def local_stats(s, k, cls_name, p):
    cls = next(c for c in rel_classes(s,k) if c[0] == cls_name)
    plus, minus = cls[2], cls[3]
    coeff = [1]*plus + [-1]*minus
    assert coeff and p > s
    ans = {}
    for z in (0,1):
        # z + sum coeff_i x_i = 0; eliminate one residual coordinate.
        last = coeff[-1] % p
        inv = pow(last, -1, p)
        other = coeff[:-1]
        pts = []
        for bits in product((0,1), repeat=len(other)):
            rhs = (-z - sum(c*b for c,b in zip(other,bits))) % p
            xlast = (rhs*inv) % p
            if xlast in (0,1):
                pts.append(tuple(bits))
        # Independent Vandermonde count check.
        a = plus
        expected = comb(s-1, a+z) if 0 <= a+z <= s-1 else 0
        assert len(pts) == expected
        if not pts:
            q = 0
        elif len(other) == 0:
            q = len(pts)
        else:
            q = 0
            for u in projective_vectors(len(other), p):
                counts = Counter(sum(ui*xi for ui,xi in zip(u,x)) % p for x in pts)
                q = max(q, max(counts.values()))
        ans[z] = (len(pts), q)
    return ans

def max_balanced(a):
    s,k = a
    return k == s//2

def old_overlap_plane(a,b):
    # run18: both generators in L_m = support-3/max-balanced or support-4/balanced.
    # run21: balanced overlap-one extensions with one generator of support 3 or 4.
    return max_balanced(a) and max_balanced(b) and min(a[0],b[0]) <= 4

def support_order_count(m,s,t):
    # Ordered supports S,T with |S cap T|=1.
    return m * comb(m-1,s-1) * comb(m-s,t-1)

def class_certificate(m,p,a,b,ca,cb):
    s,k=a; t,l=b
    free = m-(s+t-1)
    A=local_stats(s,k,ca[0],p)
    B=local_stats(t,l,cb[0],p)
    A0,qA0=A[0]; A1,qA1=A[1]
    B0,qB0=B[0]; B1,qB1=B[1]
    h=(A0*B0+A1*B1)*(2**free)
    caps=[
        (qA0*B0+qA1*B1)*(2**free),
        (qB0*A0+qB1*A1)*(2**free),
        max(A0*B0,A1*B1)*(2**free),
    ]
    if free:
        assert h % 2 == 0
        caps.append(h//2)
    Q=max(caps)

    # dim(V^perp)=m-2. Every j-space contains <=2^j Boolean points;
    # every proper subspace is contained in a hyperplane meeting C_V in <=Q points.
    basis=1
    for j in range(m-2):
        f=h-min(2**j,Q)
        if f <= 0:
            return 0,(h,Q,0,0,A,B)
        basis *= f

    # After m-2 basis columns, add two distinct nonzero unused Boolean columns.
    tail=max(0,h-m+1)*max(0,h-m)
    return basis*tail,(h,Q,basis,tail,A,B)

def aggregate_pair(m,p,a,b):
    s,k=a; t,l=b
    ordered_supports=support_order_count(m,s,t)
    planes_all=0
    planes_positive=0
    E=0
    class_rows=[]
    for ca in rel_classes(s,k):
        for cb in rel_classes(t,l):
            eper,info=class_certificate(m,p,a,b,ca,cb)
            mult=ordered_supports*ca[1]*cb[1]
            planes_all += mult
            if eper:
                planes_positive += mult
            E += mult*eper
            class_rows.append((ca[0],cb[0],mult,eper,info))
    if a==b:
        assert planes_all%2==0 and planes_positive%2==0 and E%2==0
        planes_all//=2
        planes_positive//=2
        E//=2
    return planes_all,planes_positive,E,class_rows

types=[(s,k) for s in range(3,M+1) for k in range(1,s//2+1)]

# Regression: the balanced s=3/4 versus t>=5 overlap-one family from run27.
run27_planes=0
for s in (3,4):
    a=(s,s//2)
    for t in range(5,M+1):
        if s<t and s+t-1<=M:
            b=(t,t//2)
            run27_planes += aggregate_pair(M,P,a,b)[0]
assert run27_planes == 1524600

entries=[]
for ia,a in enumerate(types):
    for b in types[ia:]:
        if a[0]+b[0]-1 > M:
            continue
        if old_overlap_plane(a,b):
            continue
        nall,npos,E,rows=aggregate_pair(M,P,a,b)
        if E:
            entries.append((a,b,nall,npos,E,rows))

assert len(entries) == 33
total_planes_all=sum(e[2] for e in entries)
total_planes_positive=sum(e[3] for e in entries)
total_E=sum(e[4] for e in entries)

assert total_planes_all == 4927890
assert total_planes_positive == 4905750
assert total_E == 4460180826038468846968800

# These planes were absent from retained M2. An exact-nullity-2 matrix formerly
# paid all p+1 projective null lines and should pay 1, so reclaim p=11.
correction = Fraction(P*total_E, 2**(M*M-M-1))  # 2^(m+1-m^2) = 2^-89
assert correction == Fraction(
    1533187158950723666145525,
    19342813113834066795298816,
)

baseline=Fraction(
    2040049312230419145475474052475,
    3893950064978720571728592896,
)
new=baseline-correction
assert new == Fraction(
    32635850599847726046678930103575,
    62303201039659529147657486336,
)

def dec(q):
    return Decimal(q.numerator)/Decimal(q.denominator)

print("R03 RUN33 EXACT CHECK")
print("run27 balanced-overlap regression planes =",run27_planes)
print("new type pairs =",len(entries))
print("new overlap-one planes enumerated =",total_planes_all)
print("new overlap-one planes with positive exact-corank certificate =",total_planes_positive)
print("new exact-corank-2 matrices lower bound E =",total_E)
print("full previously-uncredited exact-nullity-2 slack =",P)
print("normalized correction =",correction)
print("normalized correction decimal =",dec(correction))
print("old r11 upper =",dec(baseline))
print("new r11 upper =",new)
print("new r11 upper decimal =",dec(new))
print("ALL NEW TYPE PAIRS BY CERTIFIED MATRIX COUNT")
for a,b,nall,npos,E,_ in sorted(entries,key=lambda x:x[4],reverse=True):
    print(a,b,"planes_all",nall,"planes_positive",npos,"E",E)
print("SELF-CHECK PASS")
