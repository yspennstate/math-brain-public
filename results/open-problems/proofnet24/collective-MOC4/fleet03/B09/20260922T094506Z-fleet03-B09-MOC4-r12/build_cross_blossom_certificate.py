#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations
from math import gcd, lcm
import hashlib

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
    return tuple(PCIDX[frozenset(frozenset(p[i] for i in S) for S in pc)] for pc in PAIR_CLASSES)
def pm(p,n):
    return tuple(tuple(F(int(p[i]==j)) for j in range(n)) for i in range(n))
def tr(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))
def mm(A,B):
    BT=tr(B)
    return tuple(tuple(sum((x*y for x,y in zip(A[i],BT[j])),F(0)) for j in range(len(BT))) for i in range(len(A)))
def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def sc(c,A):
    return tuple(tuple(c*A[i][j] for j in range(len(A[0]))) for i in range(len(A)))

EF=tuple(tuple(F(x) for x in row) for row in E); ET=tr(EF)
J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))
def endpoint(sig):
    P=pm(sig,4); D=sc(F(1,4),mm(mm(ET,P),EF)); R=pm(rho_of(sig),3)
    return P,sc(F(1,2),add(R,D)),sc(F(1,2),add(R,sc(F(-1),D)))
def external(tau,rp):
    rt=rho_of(tau)
    P=sc(F(1,3),add(J4,sc(F(-1),pm(tau,4))))
    D=sc(F(1,4),mm(mm(ET,P),EF))
    R=add(sc(F(1,3),pm(rt,3)),sc(F(2,3),pm(rp,3)))
    return P,sc(F(1,2),add(R,D)),sc(F(1,2),add(R,sc(F(-1),D)))

EXTERNALS=[]
for tau in S4:
    rt=rho_of(tau)
    for rp in S3:
        if all(rp[i]!=rt[i] for i in range(3)):
            EXTERNALS.append((tau,rp))
assert len(EXTERNALS)==48
VERT=[endpoint(s) for s in S4]+[external(*x) for x in EXTERNALS]

A=((4,2),(-2,3),(0,-2),(-3,-2))
B=((-4,-4),(0,-2),(1,2),(-3,3))
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cadd(z,w): return (z[0]+w[0],z[1]+w[1])
def prod_for_sig(sig):
    z=(1,0)
    for i in range(4): z=cmul(z,cadd(A[i],B[sig[i]]))
    return z
def line_from_z(z):
    x,y=z
    return (F(x+y),F(-y))
ELINES={s:line_from_z(prod_for_sig(s)) for s in S4}
def ext_line(tau,rp):
    rt=rho_of(tau)
    g1=[ELINES[s] for s in S4 if rho_of(s)==rt]
    g2=[ELINES[s] for s in S4 if rho_of(s)==rp]
    b1=(sum(x[0] for x in g1)/4,sum(x[1] for x in g1)/4)
    b2=(sum(x[0] for x in g2)/4,sum(x[1] for x in g2)/4)
    f=ELINES[tau]
    return (F(2,3)*(b1[0]+b2[0])-F(1,3)*f[0],
            F(2,3)*(b1[1]+b2[1])-F(1,3)*f[1])
EXTLINES=[ext_line(*x) for x in EXTERNALS]
VLINES=[ELINES[s] for s in S4]+EXTLINES
istar=24+EXTERNALS.index(((2,3,0,1),(1,2,0)))
ESTAR=VLINES[istar]
assert ESTAR==(F(740,3),F(-116,3))

CHAMBERS=[
    (F(-5,157),F(0),(F(240),F(-248)),(0,2,1,3)),
    (F(0),F(1,10),(F(240),F(8)),(3,0,1,2)),
    (F(1,10),F(8,65),(F(236),F(48)),(1,3,2,0)),
]
def ev(line,t): return line[0]+line[1]*t
for left,right,Mline,sig in CHAMBERS:
    assert ELINES[sig]==Mline
    for t in (left,right,(left+right)/2):
        M=ev(Mline,t)
        assert M==max(ev(ELINES[s],t) for s in S4)
    for j,line in enumerate(VLINES):
        if j==istar: continue
        assert ev(line,left)<=ev(Mline,left)
        assert ev(line,right)<=ev(Mline,right)
    assert ev(ESTAR,left)>=ev(Mline,left)
    assert ev(ESTAR,right)>=ev(Mline,right)
    mid=(left+right)/2
    assert ev(ESTAR,mid)>ev(Mline,mid)
assert ev(ESTAR,F(-5,157))==ev(CHAMBERS[0][2],F(-5,157))
assert ev(ESTAR,F(8,65))==ev(CHAMBERS[-1][2],F(8,65))

def forms(data):
    P,qp,qm=data
    T=F(1)-P[0][0]
    rows=[sum(row,F(0)) for row in qm]
    cols=[sum((qm[i][j] for i in range(3)),F(0)) for j in range(3)]
    return (T-rows[0],T-cols[0],qm[1][1],qm[2][2],qm[1][2],qm[2][1])
Z=[forms(v) for v in VERT]
zstar=Z[istar]
def cofactor_F(z):
    a,b,c,d,e,f=z
    return (a*b-c*d-e*f)**2-4*c*d*e*f
assert cofactor_F(zstar)==F(1,81)

def numerator_vectors(Mline,t):
    M=ev(Mline,t); E=ev(ESTAR,t)
    out=[zstar]
    for j in range(72):
        if j==istar: continue
        v=ev(VLINES[j],t)
        out.append(tuple((M-v)*zs+(E-M)*zj for zs,zj in zip(zstar,Z[j])))
    assert len(out)==72
    return out

N0=numerator_vectors(CHAMBERS[1][2],F(0))
N1=numerator_vectors(CHAMBERS[1][2],F(1,10))
for t,Mline in ((F(-5,157),CHAMBERS[0][2]),(F(8,65),CHAMBERS[2][2])):
    M=ev(Mline,t); E=ev(ESTAR,t)
    assert E==M
    for j in range(72):
        if j==istar: continue
        v=ev(VLINES[j],t)
        target=tuple((M-v)*zs for zs in zstar)
        actual=tuple((M-v)*zs+(E-M)*zj for zs,zj in zip(zstar,Z[j]))
        assert actual==target
        assert M-v>=0

def primitive(row):
    den=1
    for x in row: den=lcm(den,x.denominator)
    ints=[int(x*den) for x in row]
    g=0
    for x in ints: g=gcd(g,abs(x))
    if g==0:
        return tuple(ints)
    return tuple(x//g for x in ints)

PV=[primitive(row) for row in N0]+[primitive(row) for row in N1]
assert len(PV)==144
payload="\n".join(",".join(str(x) for x in row) for row in PV)+"\n"
digest=hashlib.sha256(payload.encode()).hexdigest()
with open("certificate_vectors.inc","w",encoding="utf-8") as f:
    f.write("// generated by build_cross_blossom_certificate.py\n")
    f.write("// sha256 of raw comma-separated vectors: "+digest+"\n")
    for row in PV:
        f.write("    {"+",".join(str(x) for x in row)+"},\n")

print("PASS MOC4-B09-SUPPORT-CHAMBER-BUILDER-v1")
print("danger_interval = [-5/157, 8/65]")
print("endpoint_roof_chambers = [-5/157,0]:240-248t ; [0,1/10]:240+8t ; [1/10,8/65]:236+48t")
print("dangerous_external_line = 740/3-(116/3)t")
print("dangerous_external_label = tau=(2,3,0,1), rho'=(1,2,0)")
print("dangerous_vertex_cofactor = 1/81")
print("nontrivial_knot_vector_sets = 2 x 72")
print("certificate_vector_sha256 =",digest)
