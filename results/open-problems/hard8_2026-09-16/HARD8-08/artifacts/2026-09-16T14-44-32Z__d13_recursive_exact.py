#!/usr/bin/env python3
"""Exact verifier for HARD8-08 recursive squared-distance-13 G14 alignment search.

All scalar coordinates lie in Q(sqrt(3)); a scalar is (a,b) = a+b*sqrt(3).
This run:
  1. Rebuilds the 505-point first-generation pair-aligned G14 universe W exactly.
  2. Enumerates every exact d^2=13 pair in W.
  3. Aligns each of the four base d^2=13 pairs of G14 to each target d^2=13 pair,
     both endpoint orders and both orientation signs.
  4. Deduplicates copies and builds the second-generation union W2.
  5. Searches all nonzero F_3-linear coordinate forms on W and records those that
     properly 3-color its complete exact unit-distance graph.
  6. Verifies every generated coefficient is 3-integral and evaluates the selected
     color kappa(x,y)=rat(x)+rat(y) mod 3 on the entire generated point set.
     The accompanying report proves algebraically that kappa separates
     *every* exact unit-distance pair in the whole 3-integral field, including cross-copy
     edges not explicitly enumerated here.

No floating-point acceptance test is used.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict
from hashlib import sha256

# ---------- Q(sqrt(3)) arithmetic ----------
def q(a=0,b=0): return (F(a),F(b))
def qadd(x,y): return (x[0]+y[0],x[1]+y[1])
def qsub(x,y): return (x[0]-y[0],x[1]-y[1])
def qneg(x): return (-x[0],-x[1])
def qmul(x,y): return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qdiv_rat(x,r): return (x[0]/r,x[1]/r)
def vadd(A,B): return (qadd(A[0],B[0]),qadd(A[1],B[1]))
def vsub(A,B): return (qsub(A[0],B[0]),qsub(A[1],B[1]))
def smul(s,A): return (qmul(s,A[0]),qmul(s,A[1]))
def dot(A,B): return qadd(qmul(A[0],B[0]),qmul(A[1],B[1]))
def cross(A,B): return qsub(qmul(A[0],B[1]),qmul(A[1],B[0]))
def norm2(A): return dot(A,A)
def dist2(A,B): return norm2(vsub(A,B))
def is_unit(A,B): return dist2(A,B)==(F(1),F(0))

# ---------- scaled exact G14 seed ----------
NAMES=["O","i0","i1","i2","i3","i4","i5","h0","h1","a1","a2","a3","a4","a5"]
P=[
 (q(0),q(0)),
 (q(0,F(1,2)),q(F(1,2))),
 (q(0),q(1)),
 (q(0,-F(1,2)),q(F(1,2))),
 (q(0,-F(1,2)),q(-F(1,2))),
 (q(0),q(-1)),
 (q(0,F(1,2)),q(-F(1,2))),
 (q(0,1),q(0)),
 (q(0,F(1,2)),q(F(3,2))),
 (q(0,1),q(1)),
 (q(0,1),q(2)),
 (q(0,F(1,2)),q(F(5,2))),
 (q(0,F(3,2)),q(F(1,2))),
 (q(0,F(3,2)),q(-F(1,2))),
]
assert len(P)==14 and len(set(P))==14
by_d2=defaultdict(list)
for i,j in combinations(range(14),2):
    d=dist2(P[i],P[j])
    assert d[1]==0 and d[0]>0
    by_d2[d[0]].append((i,j))
expected={F(1):27,F(3):18,F(4):14,F(7):18,F(9):5,F(12):5,F(13):4}
assert {k:len(v) for k,v in by_d2.items()}==expected
BASE_UNIT=by_d2[F(1)]
SRC13=by_d2[F(13)]

# ---------- isometry determined by an ordered equal-length pair ----------
def source_frame(a,b):
    A,B=P[a],P[b]
    u=vsub(B,A); qu=norm2(u)
    assert qu[1]==0 and qu[0]>0
    r=qu[0]
    coeff=[]
    for X in P:
        w=vsub(X,A)
        coeff.append((qdiv_rat(dot(w,u),r),qdiv_rat(cross(u,w),r)))
    return qu,tuple(coeff)

FRAMES={(a,b):source_frame(a,b) for pairs in by_d2.values() for a,b in pairs}

def transform_frame(a,b,C,D,orientation):
    qu,coeff=FRAMES[(a,b)]
    v=vsub(D,C); qv=norm2(v)
    assert qu==qv
    Jv=(qneg(v[1]),v[0])
    out=[]
    for alpha,beta0 in coeff:
        beta=beta0 if orientation>0 else qneg(beta0)
        out.append(vadd(C,vadd(smul(alpha,v),smul(beta,Jv))))
    return tuple(out)

# ---------- first generation, reproducing previous 505-point universe ----------
first={}
raw1=0
for d2v in sorted(by_d2):
    pairs=by_d2[d2v]
    for a,b in pairs:
        for c,d in pairs:
            for cc,dd in ((c,d),(d,c)):
                for ori in (+1,-1):
                    raw1+=1
                    T=transform_frame(a,b,P[cc],P[dd],ori)
                    key=tuple(sorted(T))
                    assert len(key)==14
                    first.setdefault(key,(d2v,a,b,cc,dd,ori))
assert raw1==6556
assert len(first)==518
W=set(P)
for S in first: W.update(S)
W=sorted(W)
assert len(W)==505
widx={p:i for i,p in enumerate(W)}

# complete exact unit graph on W, used for finite linear-color search
W_EDGES=[]
for i,j in combinations(range(len(W)),2):
    if is_unit(W[i],W[j]): W_EDGES.append((i,j))
assert len(W_EDGES)==2008

# exact d^2=13 targets in W
D13=[]
for i,j in combinations(range(len(W)),2):
    if dist2(W[i],W[j])==(F(13),F(0)): D13.append((i,j))
assert len(D13)==1848

# ---------- second generation: only source-pair class d^2=13 ----------
second={}
raw2=0
for a,b in SRC13:
    A,B=P[a],P[b]
    for c,d in D13:
        for cc,dd in ((c,d),(d,c)):
            C,D=W[cc],W[dd]
            for ori in (+1,-1):
                raw2+=1
                T=transform_frame(a,b,C,D,ori)
                key=tuple(sorted(T))
                assert len(key)==14
                second.setdefault(key,(a,b,cc,dd,ori))
assert raw2==29568
assert len(second)==10971
W2=set(W)
for S in second: W2.update(S)
W2=sorted(W2)
assert len(W2)==17056
w2idx={p:i for i,p in enumerate(W2)}

# ---------- reduction modulo 3 for 3-integral rationals ----------
def rmod3(x):
    assert x.denominator % 3 != 0
    n=x.numerator % 3; d=x.denominator % 3
    inv=1 if d==1 else 2
    return (n*inv)%3

def resvec(p):
    # rat(x), sqrt3-coeff(x), rat(y), sqrt3-coeff(y)
    return (rmod3(p[0][0]),rmod3(p[0][1]),rmod3(p[1][0]),rmod3(p[1][1]))

def kappa(p):
    r=resvec(p)
    return (r[0]+r[2])%3

for p in W2:
    for z in p:
        for x in z:
            assert x.denominator%3 != 0

# finite search of all nonzero linear forms F3^4 on the complete W unit graph
RW=[resvec(p) for p in W]
good_forms=[]
for u in product(range(3),repeat=4):
    if u==(0,0,0,0): continue
    ok=True
    for i,j in W_EDGES:
        if sum(u[t]*(RW[i][t]-RW[j][t]) for t in range(4))%3==0:
            ok=False; break
    if ok: good_forms.append(u)
assert len(good_forms)==18
assert (1,0,1,0) in good_forms

# Exact color formula on the full generated point set.  The accompanying report
# proves algebraically that this colors every exact unit-distance pair, including
# cross-copy edges.
COL=[kappa(p) for p in W2]
counts=[COL.count(c) for c in range(3)]
assert counts==[5663,5710,5683]

# Finite consistency: every base unit edge is separated, and every distinct
# second-generation copy has 14 distinct points.
assert all(kappa(P[i])!=kappa(P[j]) for i,j in BASE_UNIT)
assert all(len(S)==14 for S in second)

# deterministic compact hash of the exact point/color set
def fs(x): return f"{x.numerator}/{x.denominator}"
def point_line(p,c):
    return "|".join(fs(v) for z in p for v in z)+f"|{c}"
point_text="\n".join(point_line(p,COL[i]) for i,p in enumerate(W2))+"\n"
point_hash=sha256(point_text.encode()).hexdigest()

print('MODEL_RUNTIME_METADATA_NOT_CHECKED_BY_SCRIPT')
print('BASE_DISTANCE_HIST',' '.join(f'{int(k)}:{len(by_d2[k])}' for k in sorted(by_d2)))
print('FIRST_RAW_ALIGNMENTS',raw1)
print('FIRST_DISTINCT_COPIES',len(first))
print('FIRST_UNION_VERTICES',len(W))
print('FIRST_COMPLETE_UNIT_EDGES',len(W_EDGES))
print('FIRST_D2_13_TARGET_PAIRS',len(D13))
print('SECOND_RAW_D13_ALIGNMENTS',raw2)
print('SECOND_DISTINCT_D13_COPIES',len(second))
print('SECOND_UNION_VERTICES',len(W2))
print('MOD3_LINEAR_FORMS_TESTED',3**4-1)
print('MOD3_GOOD_FORMS',len(good_forms))
print('SELECTED_FORM',(1,0,1,0))
print('SECOND_COLOR_COUNTS',*counts)
print('POINT_COLOR_CERT_SHA256',point_hash)
print('ALL_COEFFICIENTS_3_INTEGRAL',len(W2))
print('ALL_EXACT_D13_CHECKS_PASSED')
