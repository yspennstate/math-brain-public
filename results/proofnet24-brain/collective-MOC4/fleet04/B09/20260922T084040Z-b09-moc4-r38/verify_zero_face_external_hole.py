#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

S4=list(permutations(range(4)))
S3=list(permutations(range(3)))
E=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
PAIR_CLASSES=(
    frozenset((frozenset((0,1)),frozenset((2,3)))),
    frozenset((frozenset((0,2)),frozenset((1,3)))),
    frozenset((frozenset((0,3)),frozenset((1,2)))),
)
PCIDX={pc:i for i,pc in enumerate(PAIR_CLASSES)}

def rho_of(p):
    out=[]
    for pc in PAIR_CLASSES:
        image=frozenset(frozenset(p[i] for i in S) for S in pc)
        out.append(PCIDX[image])
    return tuple(out)

def pm(p,n):
    return tuple(tuple(F(1) if p[i]==j else F(0) for j in range(n)) for i in range(n))

def tr(A): return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))
def mm(A,B):
    BT=tr(B)
    return tuple(tuple(sum((x*y for x,y in zip(A[i],BT[j])),F(0)) for j in range(len(BT))) for i in range(len(A)))
def add(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def sc(c,A): return tuple(tuple(c*x for x in row) for row in A)
def l1(A,B): return sum(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))
def rows(A): return tuple(sum(row,F(0)) for row in A)
def cols(A): return rows(tr(A))

EF=tuple(tuple(F(x) for x in row) for row in E); ET=tr(EF)
J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))
J3=tuple(tuple(F(1) for _ in range(3)) for _ in range(3))
I3=pm((0,1,2),3)

def D_of_P(P): return sc(F(1,4),mm(mm(ET,P),EF))
def qpm(R,D): return sc(F(1,2),add(R,D)), sc(F(1,2),add(R,sc(F(-1),D)))
def ext(tau,rp):
    rt=rho_of(tau)
    P=sc(F(1,3),add(J4,sc(F(-1),pm(tau,4))))
    D=D_of_P(P)
    R=add(sc(F(1,3),pm(rt,3)),sc(F(2,3),pm(rp,3)))
    return P,R,D

def weyl(sig):
    P=pm(sig,4); D=D_of_P(P); R=pm(rho_of(sig),3)
    return P,R,D

# Canonical aligned external: tau=id, rho'=(123), zero singleton (0,0).
tau=(0,1,2,3); Cperm=(1,2,0); C=pm(Cperm,3)
P0,R0,D0=ext(tau,Cperm)
qp0,qm0=qpm(R0,D0)
assert P0[0][0]==0
assert D0==sc(F(-1,3),I3)
assert qp0==sc(F(1,3),C)
assert qm0==sc(F(1,3),add(I3,C))

# Sharp genuine zero-face Spin(6) channel in this gauge.
# Let N=(I-C)/sqrt(3), M=J/3. We verify all identities after clearing sqrt(3).
# K=I-C = sqrt(3) N.
K=add(I3,sc(F(-1),C))
M=sc(F(1,3),J3)
# K K^T = 3 I - J, so N N^T = I-J/3 and M M^T=J/3.
assert mm(K,tr(K))==add(sc(F(3),I3),sc(F(-1),J3))
assert mm(M,tr(M))==sc(F(1,3),J3)
# Cross identity clears sqrt(3): M K^T + K M^T = 0.
Z=tuple(tuple(F(0) for _ in range(3)) for _ in range(3))
assert add(mm(M,tr(K)),mm(K,tr(M)))==Z
# q^- exactly equals the aligned external anti-linear mass; q^+ is forced rank-one complement.
qm_sharp=qm0
qp_sharp=sc(F(1,9),J3)
assert rows(qm_sharp)==(F(2,3),)*3 and cols(qm_sharp)==(F(2,3),)*3
assert rows(qp_sharp)==(F(1,3),)*3 and cols(qp_sharp)==(F(1,3),)*3
assert l1(qm_sharp,qm0)==0
assert l1(qp_sharp,qp0)==F(4,3)
assert l1(qm_sharp,qm0)+l1(qp_sharp,qp0)==F(4,3)

# Exact cofactor-complement formula q+_{ab}=(1-r_a)(1-c_b).
r=rows(qm_sharp); c=cols(qm_sharp)
for a in range(3):
    for b in range(3):
        assert qp_sharp[a][b]==(1-r[a])*(1-c[b])

# Zero-face allowed outer vertices: 18 Weyl with sigma(0)!=0 and 12 aligned external tau(0)=0.
allowed=[]
for sig in S4:
    if sig[0]!=0:
        _,R,D=weyl(sig); qp,qm=qpm(R,D); allowed.append(("weyl",sig,None,qp,qm))
for tt in S4:
    if tt[0]==0:
        rt=rho_of(tt)
        ders=[rp for rp in S3 if all(rp[i]!=rt[i] for i in range(3))]
        assert len(ders)==2
        for rp in ders:
            _,R,D=ext(tt,rp); qp,qm=qpm(R,D); allowed.append(("ext",tt,rp,qp,qm))
assert len(allowed)==30
# Every normalized full channel has total mass 3; diameter bound <=6 is attained in allowed set.
maxdist=F(0)
for _,_,_,qp,qm in allowed:
    assert sum(rows(qp),F(0))+sum(rows(qm),F(0))==3
    d=l1(qp,qp0)+l1(qm,qm0)
    maxdist=max(maxdist,d)
assert maxdist==6
# Stronger sharp coefficient cap: if lambda0 is the coefficient of v0 in any
# zero-face outer decomposition, each of the three positive q+ entries of v0
# gives lambda0/3 <= p_i s_{C(i)}. Cauchy implies min_i p_i s_{C(i)}<=1/9,
# hence lambda0<=1/3. The explicit sharp genuine point attains 1/3.
coefficient_cap=F(1,3)
# Exact decomposition of the sharp genuine full-channel point.
sharp_weights={4:F(1,9),11:F(1,9),12:F(1,9),18:F(1,3),24:F(1,3)}
def lincomb(which):
    out=[[F(0) for _ in range(3)] for __ in range(3)]
    for idx,w in sharp_weights.items():
        A=allowed[idx][which]
        for i in range(3):
            for j in range(3): out[i][j]+=w*A[i][j]
    return tuple(tuple(row) for row in out)
assert sum(sharp_weights.values(),F(0))==1
assert lincomb(3)==qp_sharp
assert lincomb(4)==qm_sharp
assert sharp_weights[18]==coefficient_cap

# Exact grid sanity check for the analytic probability lemma used in the proof.
# For p,s in Delta_2, the q+ term is p tensor s and the q- L1 term dominates
# max(||p-u||_1,||s-u||_1). Verify the resulting lower bound on a rational grid.
def prob_grid(n):
    for a in range(n+1):
        for b in range(n+1-a):
            yield (F(a,n),F(b,n),F(n-a-b,n))

def outer(p,s): return tuple(tuple(p[i]*s[j] for j in range(3)) for i in range(3))
def v_l1(x,y): return sum(abs(a-b) for a,b in zip(x,y))
u=(F(1,3),)*3
mn=None; arg=None
for p in prob_grid(12):
    for s in prob_grid(12):
        lower=l1(outer(p,s),qp0)+max(v_l1(p,u),v_l1(s,u))
        if mn is None or lower<mn:
            mn=lower; arg=(p,s)
assert mn==F(4,3)

# Partner stress excess: new single-external cap leaves at most 1/3 of that excess when runner-up is M.
partner_excess=F(232716479,4000000000)
remaining=F(1,3)*partner_excess

print("PASS MOC4-ZERO-FACE-ALIGNED-EXTERNAL-ONE-THIRD-CAP-v1")
print("canonical_qplus_external =",qp0)
print("canonical_qminus_external =",qm0)
print("sharp_qminus_distance =",l1(qm_sharp,qm0))
print("sharp_qplus_distance =",l1(qp_sharp,qp0))
print("sharp_full_channel_distance =",l1(qm_sharp,qm0)+l1(qp_sharp,qp0))
print("zero_face_allowed_outer_vertices =",len(allowed))
print("allowed_full_channel_diameter_from_v0 =",maxdist)
print("single_aligned_external_coefficient_cap =",coefficient_cap)
print("sharp_decomposition_weights =",sharp_weights)
print("grid_denominator = 12")
print("grid_min_analytic_lower_bound =",mn)
print("grid_min_arg =",arg)
print("partner_stress_original_excess =",partner_excess)
print("partner_stress_remaining_excess_bound =",remaining)
