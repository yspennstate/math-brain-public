#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

S4=list(permutations(range(4)))
S3=list(permutations(range(3)))
E=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
BITS=((0,0,0),(0,1,1),(1,0,1),(1,1,0))
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

def tr(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))

def mm(A,B):
    BT=tr(B)
    return tuple(tuple(sum((x*y for x,y in zip(A[i],BT[j])),F(0))
                       for j in range(len(BT))) for i in range(len(A)))

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))

def sc(c,A):
    return tuple(tuple(c*x for x in row) for row in A)

EF=tuple(tuple(F(x) for x in row) for row in E)
ET=tr(EF)
J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))

def D_of_P(P):
    return sc(F(1,4),mm(mm(ET,P),EF))

def qpm(R,D):
    return sc(F(1,2),add(R,D)), sc(F(1,2),add(R,sc(F(-1),D)))

def ext(tau,rp):
    rt=rho_of(tau)
    P=sc(F(1,3),add(J4,sc(F(-1),pm(tau,4))))
    D=D_of_P(P)
    R=add(sc(F(1,3),pm(rt,3)),sc(F(2,3),pm(rp,3)))
    return P,R,D

def weyl(sig):
    P=pm(sig,4)
    D=D_of_P(P)
    R=pm(rho_of(sig),3)
    return P,R,D

def cadd(z,w):
    return (z[0]+w[0],z[1]+w[1])

def cmul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])

def endpoint(a,b,sig):
    z=(F(1),F(0))
    for i in range(4):
        z=cmul(z,cadd(a[i],b[sig[i]]))
    return z

def L(z):
    return z[1]-F(1,40)*z[0]

def external_value(f,tau,rp):
    rt=rho_of(tau)
    Bt=sum((f[p] for p in S4 if rho_of(p)==rt),F(0))/4
    Bp=sum((f[p] for p in S4 if rho_of(p)==rp),F(0))/4
    return F(2,3)*(Bt+Bp)-F(1,3)*f[tau]

def gauge_qplus(qp,qm,ii,jj):
    r=BITS[ii]; c=BITS[jj]
    return tuple(tuple(qp[a][b] if (r[a]^c[b])==0 else qm[a][b]
                       for b in range(3)) for a in range(3))

def matsum(A):
    return sum((x for row in A for x in row),F(0))

# Exact account01/B07 structured stress datum.
a=[(F(-174,100),F(93,100)),(F(95,100),F(23,100)),
   (F(44,100),F(-179,100)),(F(59,100),F(38,100))]
b=[(F(-149,100),F(118,100)),(F(-44,100),F(-104,100)),
   (F(101,100),F(83,100)),(F(-78,100),F(63,100))]
f={p:L(endpoint(a,b,p)) for p in S4}
M=max(f.values())
assert M==F(3654300159,1000000000)
assert [p for p in S4 if f[p]==M]==[(2,1,3,0)]

EX=[]
for tau in S4:
    rt=rho_of(tau)
    ders=[rp for rp in S3 if all(rp[k]!=rt[k] for k in range(3))]
    assert len(ders)==2
    for rp in ders:
        P,R,D=ext(tau,rp)
        qp,qm=qpm(R,D)
        EX.append((tau,rp,P,R,D,qp,qm,external_value(f,tau,rp)))

Emax=max(v[-1] for v in EX)
bad=[v for v in EX if v[-1]==Emax]
assert len(bad)==1
bad=bad[0]
bad_tau,bad_rp=bad[0],bad[1]
assert bad_tau==(3,2,1,0) and bad_rp==(2,0,1)
assert Emax==F(2969983423,800000000)
eps=Emax-M
assert eps==F(232716479,4000000000)

print("PASS source stress reconstruction")
print("M =",M)
print("bad_external =",bad_tau,bad_rp)
print("external_excess =",eps)

for ii in range(4):
    jj=bad_tau[ii]
    allowed=[]
    for sig in S4:
        if sig[ii]!=jj:
            _,R,D=weyl(sig)
            qp,qm=qpm(R,D)
            allowed.append(("weyl",sig,None,gauge_qplus(qp,qm,ii,jj),f[sig]))
    for tau,rp,P,R,D,qp,qm,val in EX:
        if tau[ii]==jj:
            allowed.append(("ext",tau,rp,gauge_qplus(qp,qm,ii,jj),val))
    assert len(allowed)==30
    assert all(matsum(v[3])==1 for v in allowed)

    badq=gauge_qplus(bad[5],bad[6],ii,jj)
    matching=[(r,c) for r in range(3) for c in range(3) if badq[r][c]==F(1,3)]
    assert len(matching)==3
    assert all(sum(1 for r,c in matching if r==rr)==1 for rr in range(3))
    assert all(sum(1 for r,c in matching if c==cc)==1 for cc in range(3))
    Cmap={r:c for r,c in matching}

    cost=[[None]*3 for _ in range(3)]
    for typ,tau,rp,q,hv in allowed:
        if typ!="weyl":
            continue
        nz=[(r,c,q[r][c]) for r in range(3) for c in range(3) if q[r][c]]
        if len(nz)==1 and nz[0][2]==1:
            r,c,_=nz[0]
            d=M-hv
            if cost[r][c] is None or d<cost[r][c]:
                cost[r][c]=d
    assert all(cost[r][c] is not None and cost[r][c]>=0
               for r in range(3) for c in range(3))

    min_slack=None
    for typ,tau,rp,q,hv in allowed:
        if typ=="ext" and tau==bad_tau and rp==bad_rp:
            continue
        assert hv<=M
        d=M-hv
        bill=sum(cost[r][c]*q[r][c] for r in range(3) for c in range(3))
        slack=d-bill
        assert slack>=0
        min_slack=slack if min_slack is None else min(min_slack,slack)

    cp=[[cost[r][Cmap[k]] for k in range(3)] for r in range(3)]
    cross=[cp[r][k]*cp[k][r] for r in range(3) for k in range(r+1,3)]
    minprod=min(cross)
    margin=4*minprod-9*eps*eps
    assert minprod>0 and margin>0

    print("zero_singleton =",(ii,jj))
    print("matching =",matching)
    print("cost_matrix =",tuple(tuple(row) for row in cost))
    print("safe_atom_min_dual_slack =",min_slack)
    print("cross_products =",tuple(cross))
    print("min_cross_product =",minprod)
    print("exact_square_margin_4minprod_minus_9eps2 =",margin)

print("PASS MOC4-ZERO-FACE-RANKONE-RECIPROCAL-PAYMENT-v1 stress closure")
