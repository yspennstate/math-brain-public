"""Exact/self-check artifact for PROB20-05 eight-consecutive-bin theorem.
SciPy is used only to FIND finite assignments; successful certificates are recomputed
with exact integer or Q(sqrt(2)) arithmetic.
"""
import itertools
from collections import defaultdict
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import linear_sum_assignment, milp, LinearConstraint, Bounds

# ---------- displacement-group certificate ----------
def components(p):
    out=[]; s=0
    for k in range(1,len(p)+1):
        if set(p[s:k])==set(range(s,k)): out.append((s,k)); s=k
    return out

def groups(p):
    g=defaultdict(list)
    for j,x in enumerate(p): g[j-x].append(j)
    return [(d,sorted(js)) for d,js in sorted(g.items())]

def B_group(p):
    m=len(p); cum=Fraction(0); B=Fraction(0)
    for d,js in groups(p):
        al=Fraction(len(js),m); mu=-1+2*cum+al
        B += al*d*mu; cum += al
    return B

def F_pieces(p):
    m=len(p); br={Fraction(0),Fraction(1)}; GG=[]
    for d,js in groups(p):
        k=len(js); pcs=[]
        for r,j in enumerate(js):
            lo=Fraction(r,k); hi=Fraction(r+1,k)
            pcs.append((lo,hi,Fraction(2*k),Fraction(2*j-d-m-2*r)))
            br|={lo,hi}
        GG.append((d,js,pcs))
    out=[]; br=sorted(br)
    for a,b in zip(br[:-1],br[1:]):
        mid=(a+b)/2; sl=Fraction(0); ic=Fraction(0)
        for d,js,pcs in GG:
            al=Fraction(len(js),m)
            for lo,hi,s,q in pcs:
                if lo<=mid<hi: sl+=al*s; ic+=al*q; break
        out.append((a,b,sl-Fraction(2*m),ic+Fraction(m)))
    return out

def qmax(A2,A1,A0,a,b):
    cc=[A2*a*a+A1*a+A0,A2*b*b+A1*b+A0]
    if A2<0:
        v=-A1/(2*A2)
        if a<=v<=b: cc.append(A2*v*v+A1*v+A0)
    return max(cc)

def threshold_ok(p,rho):
    B=B_group(p); coeff=2*B/rho; cum=Fraction(0); worst=Fraction(-10**12)
    for a,b,sl,ic in F_pieces(p):
        A2=sl/2; A1=ic; A0=cum-A2*a*a-A1*a
        worst=max(worst,qmax(A2+coeff,A1-coeff,A0,a,b))
        cum += sl*(b*b-a*a)/2+ic*(b-a)
    assert cum==0
    return worst<=0

S8=list(itertools.permutations(range(8)))
inde=[p for p in S8 if max(b-a for a,b in components(p))==8]
assert len(inde)==29093
assert all(threshold_ok(p,Fraction(1,3)) for p in inde)
bad25=[p for p in inde if not threshold_ok(p,Fraction(2,5))]
assert len(bad25)==122

def inv(p):
    q=[0]*len(p)
    for i,j in enumerate(p): q[j]=i
    return tuple(q)
def rc(p):
    m=len(p); return tuple(m-1-p[m-1-i] for i in range(m))
def orb4(p): return {p,inv(p),rc(p),inv(rc(p))}
un=set(bad25); orbs=[]
while un:
    p=next(iter(un)); o=orb4(p)&set(bad25); orbs.append(o); un-=o
assert len(orbs)==32

# ---------- exact triangular block moments ----------
def HGS(a,b):
    a=sp.Rational(a); b=sp.Rational(b); L=b-a; mid=(a+b)/2; rt2=sp.sqrt(2); hh=sp.Rational(1,2)
    HL=lambda x:rt2*sp.Rational(2,3)*x**sp.Rational(3,2)
    HR=lambda x:-rt2*sp.Rational(2,3)*(1-x)**sp.Rational(3,2)
    QL=lambda x:-x+rt2*sp.Rational(2,3)*x**sp.Rational(3,2)
    QR=lambda x:x+rt2*sp.Rational(2,3)*(1-x)**sp.Rational(3,2)
    IL=lambda x:-x*x/2+mid*x+rt2*(sp.Rational(2,5)*x**sp.Rational(5,2)-sp.Rational(2,3)*mid*x**sp.Rational(3,2))
    IR=lambda x:x*x/2-mid*x-rt2*(sp.Rational(2,3)*(mid-1)*(1-x)**sp.Rational(3,2)+sp.Rational(2,5)*(1-x)**sp.Rational(5,2))
    def piece(F1,F2,x,y):
        z=sp.S(0)
        if x<hh: z+=F1(min(y,hh))-F1(x)
        if y>hh: z+=F2(y)-F2(max(x,hh))
        return sp.simplify(z)
    H=sp.simplify(piece(HL,HR,a,b)/L)
    G=sp.simplify(4*piece(IL,IR,a,b)/L**2)
    S=sp.simplify((piece(QL,QR,mid,b)-piece(QL,QR,a,mid))/L)
    return H,G,S

# exact interior bridge n=16,...,23
for n in range(16,24):
    H0,G0,_=HGS(0,sp.Rational(8,n))
    assert sp.simplify(sp.Rational(2,5)*H0-G0)==0
    for k in range(1,n-8):
        H,G,_=HGS(sp.Rational(k,n),sp.Rational(k+8,n))
        assert sp.simplify(H-3*G).is_nonnegative is True

# ---------- endpoint 2 x 8 domino certificates ----------
def allowed_pairs(m=8):
    cells=[(r,c) for r in range(2) for c in range(m)]; pp=[]
    for r in (0,1):
        for a,b in itertools.combinations(range(m),2): pp.append(((r,a),(r,b)))
    for c in range(m): pp.append(((0,c),(1,c)))
    return cells,pp

def score_coeff(p,j,pair):
    m=len(p); (r1,c1),(r2,c2)=pair
    if r1==r2:
        typ='L' if r1==0 else 'H'; z=Fraction((2*c1+1-m)+(2*c2+1-m),2*m)
    else:
        assert c1==c2 and {r1,r2}=={0,1}; typ='F'; z=Fraction(2*c1+1-m,m)
    if typ=='L': Esa,Esb=Fraction(0),Fraction(1,3); Era,Erb=Fraction(0),Fraction(1,5)
    elif typ=='H': Esa,Esb=Fraction(4,3),Fraction(-1,3); Era,Erb=Fraction(4,15),Fraction(2,15)
    else: Esa,Esb=Fraction(2,3),Fraction(0); Era,Erb=Fraction(2,5),Fraction(0)
    q=(j+p[j])+(j-p[j])*z
    return Fraction(1,2)*(q*Esa+2*Era), Fraction(1,2)*(q*Esb+2*Erb)

def endpoint_certificate(p):
    m=8; cells,pairs=allowed_pairs(m); ci={c:i for i,c in enumerate(cells)}
    vars=[]; ex=[]; cost=[]
    for j in range(m):
        for q,pair in enumerate(pairs):
            a,b=score_coeff(p,j,pair); vars.append((j,q,pair)); ex.append((a,b)); cost.append(-(float(a)+float(b)*2**0.5)/m)
    nv=len(vars); A=np.zeros((m+2*m,nv))
    for v,(j,q,pair) in enumerate(vars):
        A[j,v]=1
        for cell in pair: A[m+ci[cell],v]=1
    res=milp(c=np.array(cost),integrality=np.ones(nv),bounds=Bounds(np.zeros(nv),np.ones(nv)),constraints=LinearConstraint(A,np.ones(m+2*m),np.ones(m+2*m)))
    assert res.success
    chosen=[i for i,x in enumerate(res.x) if x>.5]
    assert len(chosen)==m
    assert len({vars[i][0] for i in chosen})==m
    used=[]
    for i in chosen: used+=list(vars[i][2])
    assert sorted(used)==sorted(cells)
    aa=sum(ex[i][0] for i in chosen)/m; bb=sum(ex[i][1] for i in chosen)/m
    sc=sp.Rational(aa.numerator,aa.denominator)+sp.Rational(bb.numerator,bb.denominator)*sp.sqrt(2)
    assert sp.simplify(sc-sp.Rational(16,5)).is_positive is True
    return sp.simplify(sc)

worst=sp.Rational(199,240)-sp.Rational(11,24)*sp.sqrt(2)
assert 199**2-2*110**2==15401>0
for p in bad25:
    sc=endpoint_certificate(p)
    assert sp.simplify(sc-sp.Rational(16,5)-worst).is_nonnegative is True

# ---------- finite bridge n=8,...,15 ----------
def psi12(k):
    k=abs(k)
    if k==0:return 8
    if k==1:return 13
    return 12*k

def Jfrac(p):
    n=len(p); S=0
    for i in range(n):
        for j in range(n):
            d=i-j; e=p[i]-p[j]; S+=abs(d-e)*psi12(d+e)
    return Fraction(S,12*n**4)

def global_perm(n,k,p):
    q=list(range(n))
    for j,x in enumerate(p): q[k+j]=k+x
    return tuple(q)

def cellcert(p):
    n=len(p); a=np.array([2*i+1-n for i in range(n)],dtype=np.int64)
    cells=[(r,s) for r in range(n) for s in range(n)]; labels=[i for i in range(n) for _ in range(n)]
    lab=np.array(labels,dtype=np.int64); lx=a[lab]; ly=a[np.array([p[i] for i in labels],dtype=np.int64)]
    M=np.empty((n*n,n*n),dtype=np.int64)
    for rr,(r,s) in enumerate(cells): M[rr,:]=a[r]*lx+a[s]*ly
    rows,cols=linear_sum_assignment(-M); cnt=[0]*n; W=0
    for rr,cc in zip(rows,cols):
        i=labels[cc]; cnt[i]+=1; r,s=cells[rr]; W+=int(a[r])*int(a[i])+int(a[s])*int(a[p[i]])
    assert cnt==[n]*n
    return 15*W-7*n*n*(n*n-1)

rhos={8:Fraction(7,10),9:Fraction(3,5),10:Fraction(1,2),11:Fraction(23,50),12:Fraction(43,100),13:Fraction(5,12),14:Fraction(41,100),15:Fraction(81,200)}
exp_fail={8:21852,9:10328,10:2128,11:908,12:348,13:226,14:184,15:148}
exp_res={8:36,9:116,10:1722,11:3208,12:1740,13:1356,14:1288,15:1184}
exp_min={8:3456,9:7440,10:10320,11:13620,12:17856,13:21156,14:24480,15:27780}
for n,rho in rhos.items():
    for k in range(n-7):
        H,G,_=HGS(sp.Rational(k,n),sp.Rational(k+8,n))
        assert sp.simplify(sp.Rational(rho.numerator,rho.denominator)*H-G).is_nonnegative is True
    ff=[p for p in inde if not threshold_ok(p,rho)]
    assert len(ff)==exp_fail[n]
    residual=[]
    for k in range(n-7):
        for p in ff:
            gp=global_perm(n,k,p)
            if Jfrac(gp)<Fraction(2,15): residual.append(gp)
    assert len(residual)==exp_res[n]
    mm=min(cellcert(gp) for gp in residual)
    assert mm==exp_min[n] and mm>0

print('EXACT EIGHT-BIN CHECKS PASSED')
