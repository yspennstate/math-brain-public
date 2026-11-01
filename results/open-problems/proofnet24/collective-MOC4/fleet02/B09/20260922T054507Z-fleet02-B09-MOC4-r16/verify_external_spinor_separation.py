#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

S4 = list(permutations(range(4)))
S3 = list(permutations(range(3)))

E = (
    (1,1,1),
    (1,-1,-1),
    (-1,1,-1),
    (-1,-1,1),
)
BITS = ((0,0,0),(0,1,1),(1,0,1),(1,1,0))
PAIR_CLASSES = (
    frozenset((frozenset((0,1)), frozenset((2,3)))),
    frozenset((frozenset((0,2)), frozenset((1,3)))),
    frozenset((frozenset((0,3)), frozenset((1,2)))),
)
PCIDX = {pc:i for i,pc in enumerate(PAIR_CLASSES)}

def rho_of(p):
    out=[]
    for pc in PAIR_CLASSES:
        image=frozenset(frozenset(p[i] for i in S) for S in pc)
        out.append(PCIDX[image])
    return tuple(out)

def pm(p,n):
    return tuple(tuple(F(1) if p[i]==j else F(0) for j in range(n)) for i in range(n))

def mt(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))

def mm(A,B):
    BT=mt(B)
    return tuple(tuple(sum((x*y for x,y in zip(A[i],BT[j])),F(0))
                       for j in range(len(BT))) for i in range(len(A)))

def scale(c,A):
    return tuple(tuple(c*x for x in row) for row in A)

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

EF=tuple(tuple(F(x) for x in row) for row in E)
ET=mt(EF)
J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))

def D_of_P(P):
    return scale(F(1,4),mm(mm(ET,P),EF))

def qpm(R,D):
    return scale(F(1,2),add(R,D)), scale(F(1,2),add(R,scale(F(-1),D)))

def external_vertex(tau,rhop):
    rt=rho_of(tau)
    P=scale(F(1,3),add(J4,scale(F(-1),pm(tau,4))))
    D=D_of_P(P)
    R=add(scale(F(1,3),pm(rt,3)),scale(F(2,3),pm(rhop,3)))
    return P,R,D

def weyl_vertex(tau):
    P=pm(tau,4)
    D=D_of_P(P)
    R=pm(rho_of(tau),3)
    return P,R,D

def gauge_q(P,R,D,r,c):
    qp,qm=qpm(R,D)
    return tuple(tuple(qm[i][j] if (r[i]^c[j])==0 else qp[i][j]
                       for j in range(3)) for i in range(3))

# Build 48 non-Weyl external normalized-Saxl vertices.
EXTERNAL=[]
for tau in S4:
    rt=rho_of(tau)
    ders=[rp for rp in S3 if all(rp[i]!=rt[i] for i in range(3))]
    assert len(ders)==2
    for rp in ders:
        EXTERNAL.append((tau,rp,*external_vertex(tau,rp)))
assert len(EXTERNAL)==48

# Every external singleton determinant gauge has the same exact zero-count
# pattern: one positive perfect matching and the five alternatives meet
# 1,2,2,2,3 zero entries, respectively.
singleton_count=0
patterns=set()
for tau,rp,P,R,D in EXTERNAL:
    for r in BITS:
        for c in BITS:
            Q=gauge_q(P,R,D,r,c)
            prods=[]
            zcounts=[]
            for rho in S3:
                vals=[Q[i][rho[i]] for i in range(3)]
                prod=F(1)
                for v in vals:
                    prod*=v
                prods.append(prod)
                zcounts.append(sum(v==0 for v in vals))
            positives=[x for x in prods if x>0]
            if len(positives)==1:
                singleton_count+=1
                assert positives[0]==F(1,27)
                assert set(x for row in Q for x in row) <= {F(0),F(1,3)}
                patterns.add(tuple(sorted(zcounts)))
assert singleton_count==48*12
assert patterns=={(0,1,2,2,2,3)}

# All 72 outer-polytope vertices have every gaugewise q-entry in [0,1].
qmin=F(1)
qmax=F(0)
outer=[(P,R,D) for _,_,P,R,D in EXTERNAL]
outer += [weyl_vertex(tau) for tau in S4]
assert len(outer)==72
for P,R,D in outer:
    for r in BITS:
        for c in BITS:
            Q=gauge_q(P,R,D,r,c)
            for row in Q:
                for x in row:
                    assert F(0)<=x<=F(1)
                    qmin=min(qmin,x)
                    qmax=max(qmax,x)
assert qmin==0 and qmax==1

# Quantitative determinant-zero separation.
#
# If delta = ||q-q0||_infty <= 1/25 around a singleton external gauge q0,
# the unique external determinant monomial has magnitude at least
# (1/3-delta)^(3/2).  The five alternatives, according to the exact
# zero-count pattern above, have total magnitude at most
# sqrt(delta)(1/3+delta)
# + 3 delta sqrt(1/3+delta)
# + delta^(3/2).
#
# LHS is decreasing and RHS increasing in delta.  At delta=1/25,
# after multiplying by 375, the desired strict inequality is
#
#   110 sqrt(22/75) > 31 + 45 sqrt(28/75).
#
# Both sides are positive.  The first squaring reduces this to
#
#   5497/3 > 2790 sqrt(28/75),
#
# and the second squaring leaves the positive rational margin below.
delta=F(1,25)
first_square_margin = F(110*110*22,75) - (F(31*31) + F(45*45*28,75))
assert first_square_margin==F(5497,3)
second_square_margin = first_square_margin**2 - F(2790*2790*28,75)
assert second_square_margin==F(4062433,9)
assert second_square_margin>0

# Therefore det N=0 is impossible in the closed 1/25 q-infinity ball
# around any of the 48 external vertices in any of its 12 singleton
# gauges.  Since every outer q-coordinate is in [0,1], any convex
# decomposition of a genuine normalized-Saxl functional has coefficient
# lambda_e < 24/25 at a fixed external vertex e.
coefficient_cap = F(24,25)

print("PASS MOC4-EXTERNAL-SPINOR-SEPARATION-v1")
print("external_vertices =",len(EXTERNAL))
print("singleton_gauges_total =",singleton_count)
print("singleton_zero_count_pattern =",next(iter(patterns)))
print("outer_vertices_checked =",len(outer))
print("outer_q_entry_range =",qmin,qmax)
print("delta_certificate =",delta)
print("first_square_margin =",first_square_margin)
print("second_square_margin =",second_square_margin)
print("external_barycentric_coefficient_strict_cap <",coefficient_cap)
print("unique_external_outer_roof_shrink_fraction =",F(1,25))
