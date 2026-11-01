#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

S4=list(permutations(range(4)))
S3=list(permutations(range(3)))
IDX4={p:i for i,p in enumerate(S4)}
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
def sc(c,A): return tuple(tuple(c*A[i][j] for j in range(len(A[0]))) for i in range(len(A)))
EF=tuple(tuple(F(x) for x in row) for row in E)
ET=tr(EF)
J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))

def ext(tau,rp):
    rt=rho_of(tau)
    P=sc(F(1,3),add(J4,sc(F(-1),pm(tau,4))))
    D=sc(F(1,4),mm(mm(ET,P),EF))
    R=add(sc(F(1,3),pm(rt,3)),sc(F(2,3),pm(rp,3)))
    qp=sc(F(1,2),add(R,D))
    qm=sc(F(1,2),add(R,sc(F(-1),D)))
    return P,R,D,qp,qm

def gauge_B(P,qp,qm,r,c):
    B=tuple(tuple(qm[i][j] if (r[i]^c[j])==0 else qp[i][j] for j in range(3)) for i in range(3))
    p=P[BIDX[r]][BIDX[c]]
    return F(1)-p,B

def amp_violations(P,qp,qm):
    out=[]
    for rho in S3:
        for delta in BITS:
            vals=[]
            for a in range(3):
                vals.append((qm if delta[a]==0 else qp)[a][rho[a]])
            ps=[]
            for r in BITS:
                c=[0]*3
                for a in range(3):
                    c[rho[a]]=r[a]^delta[a]
                ps.append(P[BIDX[r]][BIDX[tuple(c)]])
            pstar=max(ps)
            if tuple(vals)==(F(1,3),)*3 and pstar==F(1,3):
                out.append((rho,delta,tuple(vals),pstar))
    return out

def cofactor_zero_rhs_violations(P,qp,qm):
    out=[]
    for r in BITS:
        for c in BITS:
            t2,B=gauge_B(P,qp,qm,r,c)
            rs=[sum(row,F(0)) for row in B]
            cs=[sum(B[i][j] for i in range(3)) for j in range(3)]
            for i in range(3):
                for j in range(3):
                    rr=[x for x in range(3) if x!=i]
                    cc=[x for x in range(3) if x!=j]
                    p1=B[rr[0]][cc[0]]*B[rr[1]][cc[1]]
                    p2=B[rr[0]][cc[1]]*B[rr[1]][cc[0]]
                    lhs=(t2-rs[i])*(t2-cs[j])
                    if lhs>0 and p1==0 and p2==0:
                        out.append((r,c,i,j,t2,rs[i],cs[j],lhs))
    return out

externals=[]
for tau in S4:
    rt=rho_of(tau)
    der=[rp for rp in S3 if all(rp[i]!=rt[i] for i in range(3))]
    assert len(der)==2
    for rp in der:
        P,R,D,qp,qm=ext(tau,rp)
        av=amp_violations(P,qp,qm)
        cv=cofactor_zero_rhs_violations(P,qp,qm)
        assert len(av)==4
        assert len(cv)==24
        assert all(x[2]==(F(1,3),)*3 and x[3]==F(1,3) for x in av)
        assert all((x[4],x[5],x[6],x[7])==(F(2,3),F(1,3),F(1,3),F(1,9)) for x in cv)
        externals.append((tau,rp))
assert len(externals)==48

A=((4,2),(-2,3),(0,-2),(-3,-2))
Bspec=((-4,-4),(0,-2),(1,2),(-3,3))
ETA=(1,-1)
def cmul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cadd(z,w): return (z[0]+w[0],z[1]+w[1])
def sval(sig):
    z=(1,0)
    for i in range(4):
        z=cmul(z,cadd(A[i],Bspec[sig[i]]))
    z=cmul(ETA,z)
    return F(z[0])
f={p:sval(p) for p in S4}
M=max(f.values())
def ext_value(tau,rp):
    rt=rho_of(tau)
    s1=sum((f[p] for p in S4 if rho_of(p)==rt),F(0))
    s2=sum((f[p] for p in S4 if rho_of(p)==rp),F(0))
    return (s1+s2-2*f[tau])/6
ev=sorted((ext_value(t,r),t,r) for t,r in externals)
E1,topt,ropt=ev[-1]
E2=max(M,ev[-2][0])
assert M==F(240)
assert E1==F(740,3)
assert E2==F(240)
assert topt==(2,3,0,1)
assert ropt==(1,2,0)

poly=lambda x: 12*x*x-4*x+F(1,9)
assert poly(F(3,100))>0
assert poly(F(31,1000))<0

print("PASS MOC4-EXTERNAL-SPINOR-SEPARATION-v2")
print("external_vertices_checked =",len(externals))
print("partner_amplitude_violations_per_external = 4")
print("partner_amplitude_pattern = q=(1/3,1/3,1/3), p_star=1/3")
print("cofactor_zero_rhs_violations_per_external = 24")
print("cofactor_deficit_pattern = t2=2/3,row=1/3,col=1/3,lhs=1/9,rhs=0")
print("robust_radius_exact = (3-sqrt(6))/18")
print("robust_radius_bracket = (3/100,31/1000)")
print("structured_endpoint_max =",M)
print("structured_external_max =",E1)
print("structured_second_outer_max =",E2)
print("structured_unique_external_tau =",topt)
print("structured_unique_external_rhop =",ropt)
print("atomic_cap_support_bound = (6630+10*sqrt(6))/27")
