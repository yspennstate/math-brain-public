"""Exact/self-check artifact for PROB20-05 nine-bin large-resolution theorem.

Default run performs exact structural enumeration, exact finite interior checks, and
one exact endpoint-domino certificate per symmetry orbit of the 1730 hard endpoint
permutations. Set FULL_ENDPOINT=1 in the environment to solve/check all 1730 endpoint
MILPs rather than orbit representatives.

SciPy MILP is used only to FIND endpoint domino partitions. Returned partitions are
checked exactly in Q(sqrt(2)).
"""
import itertools, math, os
from collections import defaultdict
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import milp, LinearConstraint, Bounds

def indecomp(p):
    mx=-1
    for k,x in enumerate(p[:-1],start=1):
        mx=max(mx,x)
        if mx==k-1:return False
    return True

def profile_exact(p):
    m=len(p)
    g=defaultdict(list)
    for j,x in enumerate(p): g[j-x].append(j)
    gg=sorted(g.items())
    cumz=Fraction(0); B=Fraction(0); br={Fraction(0),Fraction(1)}; PG=[]
    for d,js in gg:
        k=len(js); al=Fraction(k,m); mu=-1+2*cumz+al
        B += al*d*mu; cumz += al
        pcs=[]
        for r,j in enumerate(js):
            lo=Fraction(r,k); hi=Fraction(r+1,k)
            pcs.append((lo,hi,Fraction(2*k),Fraction(2*j-d-m-2*r)))
            br|={lo,hi}
        PG.append((al,pcs))
    out=[]; br=sorted(br)
    for a,b in zip(br[:-1],br[1:]):
        mid=(a+b)/2; sl=Fraction(0); ic=Fraction(0)
        for al,pcs in PG:
            k=len(pcs); r=min(int(mid*k),k-1)
            lo,hi,s,q=pcs[r]
            assert lo<=mid<hi
            sl+=al*s; ic+=al*q
        out.append((a,b,sl-Fraction(2*m),ic+Fraction(m)))
    return B,out

def threshold_prof(prof,rho):
    B,pieces=prof; coeff=2*B/rho; cum=Fraction(0)
    for a,b,sl,ic in pieces:
        A2=sl/2; A1=ic; A0=cum-A2*a*a-A1*a
        qa=A2+coeff; qb=A1-coeff
        vals=[qa*a*a+qb*a+A0,qa*b*b+qb*b+A0]
        if qa<0:
            v=-qb/(2*qa)
            if a<=v<=b:vals.append(qa*v*v+qb*v+A0)
        if max(vals)>0:return False
        cum += sl*(b*b-a*a)/2+ic*(b-a)
    assert cum==0
    return True

inde=[]; bad13=[]; bad25=[]
for p in itertools.permutations(range(9)):
    if not indecomp(p): continue
    inde.append(p)
    prof=profile_exact(p)
    if not threshold_prof(prof,Fraction(1,3)): bad13.append((p,prof))
    if not threshold_prof(prof,Fraction(2,5)): bad25.append(p)
assert len(inde)==273343
assert len(bad13)==40
assert all(threshold_prof(prof,Fraction(23,72)) for p,prof in bad13)
assert len(bad25)==1730

def HGS(a,b):
    a=sp.Rational(a); b=sp.Rational(b); L=b-a; mid=(a+b)/2; rt2=sp.sqrt(2); hh=sp.Rational(1,2)
    HL=lambda x:rt2*sp.Rational(2,3)*x**sp.Rational(3,2)
    HR=lambda x:-rt2*sp.Rational(2,3)*(1-x)**sp.Rational(3,2)
    IL=lambda x:-x*x/2+mid*x+rt2*(sp.Rational(2,5)*x**sp.Rational(5,2)-sp.Rational(2,3)*mid*x**sp.Rational(3,2))
    IR=lambda x:x*x/2-mid*x-rt2*(sp.Rational(2,3)*(mid-1)*(1-x)**sp.Rational(3,2)+sp.Rational(2,5)*(1-x)**sp.Rational(5,2))
    def piece(F1,F2,x,y):
        z=sp.S(0)
        if x<hh:z+=F1(min(y,hh))-F1(x)
        if y>hh:z+=F2(y)-F2(max(x,hh))
        return sp.simplify(z)
    H=sp.simplify(piece(HL,HR,a,b)/L)
    G=sp.simplify(4*piece(IL,IR,a,b)/L**2)
    return H,G

for n in range(18,29):
    for k in range(1,n-9):
        H,G=HGS(sp.Rational(k,n),sp.Rational(k+9,n))
        assert sp.simplify(sp.Rational(23,72)*H-G).is_nonnegative is True

r=1/sp.sqrt(10)
R=sp.simplify(2*(1-r)*(r**2+3*r+1)/(5*(1+r)*(r**2+r+1)))
assert sp.simplify(R-(sp.Rational(374,1665)+8*sp.sqrt(10)/333))==0
assert Fraction(421,4440)**2-10*Fraction(8,333)**2==Fraction(15437,4795200)
assert sp.Rational(9,29)<sp.Rational(23,72)

def inv(p):
    q=[0]*len(p)
    for i,j in enumerate(p):q[j]=i
    return tuple(q)
def rc(p):
    m=len(p);return tuple(m-1-p[m-1-i] for i in range(m))
def orb4(p):return {p,inv(p),rc(p),inv(rc(p))}
un=set(bad25); reps=[]
while un:
    p=next(iter(un)); o=orb4(p)&un; reps.append(p);un-=o
assert len(reps)==436

def allowed_pairs(m=9):
    cells=[(r,c) for r in range(2) for c in range(m)];pairs=[]
    for rr in (0,1):
        for a,b in itertools.combinations(range(m),2):pairs.append(((rr,a),(rr,b)))
    for c in range(m):pairs.append(((0,c),(1,c)))
    return cells,pairs

def score_coeff(p,j,pair):
    m=len(p);(r1,c1),(r2,c2)=pair
    if r1==r2:
        typ='L' if r1==0 else 'H'
        z=Fraction((2*c1+1-m)+(2*c2+1-m),2*m)
    else:
        assert c1==c2;typ='F';z=Fraction(2*c1+1-m,m)
    if typ=='L':
        Esa,Esb=Fraction(0),Fraction(1,3);Era,Erb=Fraction(0),Fraction(1,5)
    elif typ=='H':
        Esa,Esb=Fraction(4,3),Fraction(-1,3);Era,Erb=Fraction(4,15),Fraction(2,15)
    else:
        Esa,Esb=Fraction(2,3),Fraction(0);Era,Erb=Fraction(2,5),Fraction(0)
    q=Fraction(j+p[j])+Fraction(j-p[j])*z
    return Fraction(1,2)*(q*Esa+2*Era),Fraction(1,2)*(q*Esb+2*Erb)

cells,pairs=allowed_pairs(9);ci={c:i for i,c in enumerate(cells)}
vars_base=[(j,q,pair) for j in range(9) for q,pair in enumerate(pairs)]
A=np.zeros((27,len(vars_base)))
for v,(j,q,pair) in enumerate(vars_base):
    A[j,v]=1
    for cell in pair:A[9+ci[cell],v]=1
constraint=LinearConstraint(A,np.ones(27),np.ones(27))
bounds=Bounds(np.zeros(len(vars_base)),np.ones(len(vars_base)))
integrality=np.ones(len(vars_base))

def endpoint_certificate(p):
    exact=[];cost=[];rt2=math.sqrt(2)
    for j,q,pair in vars_base:
        aa,bb=score_coeff(p,j,pair); exact.append((aa,bb));cost.append(-(float(aa)+float(bb)*rt2)/9)
    res=milp(c=np.array(cost),integrality=integrality,bounds=bounds,constraints=constraint)
    assert res.success
    chosen=[i for i,x in enumerate(res.x) if x>.5]
    assert len(chosen)==9
    assert len({vars_base[i][0] for i in chosen})==9
    used=[]
    for i in chosen:used+=list(vars_base[i][2])
    assert sorted(used)==sorted(cells)
    aa=sum((exact[i][0] for i in chosen),Fraction())/9
    bb=sum((exact[i][1] for i in chosen),Fraction())/9
    margin=sp.Rational(aa.numerator,aa.denominator)+sp.Rational(bb.numerator,bb.denominator)*sp.sqrt(2)-sp.Rational(18,5)
    assert margin.is_positive is True
    return margin

targets=bad25 if os.environ.get('FULL_ENDPOINT')=='1' else reps
best=None
for p in targets:
    z=endpoint_certificate(p)
    if best is None or float(sp.N(z))<float(sp.N(best)):best=z
if os.environ.get('FULL_ENDPOINT')=='1':
    expected=sp.Rational(383,405)-sp.Rational(5,9)*sp.sqrt(2)
    assert sp.simplify(best-expected)==0
    assert Fraction(383,405)**2-2*Fraction(5,9)**2==Fraction(45439,164025)

print('EXACT NINE-BIN LARGE-RESOLUTION CHECKS PASSED')
print('indecomposable S9:',len(inde))
print('fail 1/3:',len(bad13))
print('fail 2/5:',len(bad25))
print('endpoint symmetry orbits:',len(reps))
print('checked endpoint certificates:',len(targets))
print('minimum checked endpoint margin:',best)
