#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations, combinations
from math import comb

S4=list(permutations(range(4)))
S3=list(permutations(range(3)))
E=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
BITS=((0,0,0),(0,1,1),(1,0,1),(1,1,0))
BIDX={b:i for i,b in enumerate(BITS)}
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

EF=tuple(tuple(F(x) for x in row) for row in E)
ET=tr(EF)
J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))

def endpoint(sig):
    P=pm(sig,4)
    D=sc(F(1,4),mm(mm(ET,P),EF))
    R=pm(rho_of(sig),3)
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
EXT=[external(*x) for x in EXTERNALS]
END=[endpoint(s) for s in S4]

def padd(a,b):
    n=max(len(a),len(b))
    return tuple((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n))
def psub(a,b):
    return padd(a,tuple(-x for x in b))
def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return tuple(out)
def pscale(c,a):
    return tuple(c*x for x in a)
def affine(x1,x2):
    return (x2,x1-x2)
def bernstein4(a):
    aa=list(a)+[F(0)]*(5-len(a))
    return tuple(sum(aa[j]*F(comb(k,j),comb(4,j)) for j in range(k+1)) for k in range(5))
def smul(v,t):
    ratio=None
    for a,b in zip(v,t):
        if b==0:
            if a!=0: return None
        else:
            r=a/b
            if ratio is None: ratio=r
            elif r!=ratio: return None
    return ratio

T0=(F(1),F(-6),F(13),F(-12),F(4))
T1=(F(0),F(0),F(1),F(-4),F(4))

def edge_annulus_polys(d1,d2):
    P=[[affine(d1[0][i][j],d2[0][i][j]) for j in range(4)] for i in range(4)]
    qp=[[affine(d1[1][i][j],d2[1][i][j]) for j in range(3)] for i in range(3)]
    qm=[[affine(d1[2][i][j],d2[2][i][j]) for j in range(3)] for i in range(3)]
    one=(F(1),)
    out=[]
    for r in BITS:
      for c in BITS:
        B=[[qm[a][b] if (r[a]^c[b])==0 else qp[a][b] for b in range(3)] for a in range(3)]
        t2=psub(one,P[BIDX[r]][BIDX[c]])
        rows=[(F(0),) for _ in range(3)]
        cols=[(F(0),) for _ in range(3)]
        for a in range(3):
            for b in range(3):
                rows[a]=padd(rows[a],B[a][b]); cols[b]=padd(cols[b],B[a][b])
        for a in range(3):
          for b in range(3):
            rr=[i for i in range(3) if i!=a]
            cc=[j for j in range(3) if j!=b]
            x=pmul(psub(t2,rows[a]),psub(t2,cols[b]))
            u=pmul(B[rr[0]][cc[0]],B[rr[1]][cc[1]])
            v=pmul(B[rr[0]][cc[1]],B[rr[1]][cc[0]])
            z=psub(psub(x,u),v)
            f=psub(pmul(z,z),pscale(F(4),pmul(u,v)))
            f=tuple(list(f)+[F(0)]*(5-len(f)))[:5]
            out.append((r,c,a,b,f))
    assert len(out)==144
    return out

def mix(d1,d2,l):
    return tuple(tuple(tuple(l*d1[k][i][j]+(1-l)*d2[k][i][j]
                              for j in range(len(d1[k][0])))
                       for i in range(len(d1[k]))) for k in range(3))

def flatten(d):
    return tuple(x for M in d for row in M for x in row)

def midpoint_weyl_certificate(i,j):
    tau1,r1=EXTERNALS[i]; tau2,r2=EXTERNALS[j]
    rho=rho_of(tau1)
    assert rho_of(tau2)==rho and r1!=r2 and tau1!=tau2
    w={s:F(0) for s in S4}
    for s in S4:
        rs=rho_of(s)
        if rs==rho:
            w[s]+=F(1,6)
        elif rs==r1 or rs==r2:
            w[s]+=F(1,12)
    w[tau1]-=F(1,6); w[tau2]-=F(1,6)
    assert all(v>=0 for v in w.values()) and sum(w.values(),F(0))==1
    target=flatten(mix(EXT[i],EXT[j],F(1,2)))
    end_map={s:END[k] for k,s in enumerate(S4)}
    combo=[]
    for coord in range(len(target)):
        combo.append(sum((w[s]*flatten(end_map[s])[coord] for s in S4),F(0)))
    assert tuple(combo)==target
    return sum(v>0 for v in w.values())

forbidden=0
exceptional=0
support_sizes=set()
for i,j in combinations(range(48),2):
    polys=edge_annulus_polys(EXT[i],EXT[j])
    cert=None
    for rec in polys:
        bc=bernstein4(rec[-1])
        if all(x>=0 for x in bc) and any(x>0 for x in bc):
            cert=rec
            break
    if cert is not None:
        forbidden+=1
        continue
    tau1,r1=EXTERNALS[i]; tau2,r2=EXTERNALS[j]
    assert rho_of(tau1)==rho_of(tau2)
    assert r1!=r2 and tau1!=tau2
    force=False
    for rec in polys:
        if (smul(rec[-1],T0) or F(0))>0 or (smul(rec[-1],T1) or F(0))>0:
            force=True
            break
    assert force
    support_sizes.add(midpoint_weyl_certificate(i,j))
    exceptional+=1

assert forbidden==1056
assert exceptional==72
assert forbidden+exceptional==48*47//2
assert support_sizes=={10}

print("PASS MOC4-EXTERNAL-EXTERNAL-EDGE-PURGE-v1")
print("external_external_edges =",48*47//2)
print("open_edges_annulus_forbidden =",forbidden)
print("exceptional_edges_midpoint_only =",exceptional)
print("exceptional_pattern = same rho_tau, opposite derangements, distinct tau")
print("exceptional_midpoint = explicit Weyl convex combination: two atoms weight 1/6, eight atoms weight 1/12")
print("weyl_certificate_support_size =",sorted(support_sizes))
