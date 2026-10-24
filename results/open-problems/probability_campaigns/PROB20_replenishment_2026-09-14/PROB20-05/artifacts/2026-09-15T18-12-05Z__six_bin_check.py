"""
PROB20-05 exact checker for the six-consecutive-bin theorem.

Verifies:
- run aggregation constants on all 461 indecomposable S_6 permutations;
- exactly two indecomposable patterns have run threshold A/C < 2/5;
- finite global resolutions n=6,...,11 by exact endpoint or integer cell certificates,
  with the sole residual full reversal checked by the exact run formula;
- exact interval inequalities 2H-5G >= 0 for every six-bin block position at
  n=12,...,17;
- symbolic identities for cyclic rotations and the special grouped hard pattern.

SciPy Hungarian matching is used only to FIND balanced assignments.
Successful cell certificates are recomputed with exact integer arithmetic.
"""
import itertools
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import linear_sum_assignment

def consecutive_components(perm):
    n=len(perm); comps=[]; start=0
    for k in range(1,n+1):
        if set(perm[start:k])==set(range(start,k)):
            comps.append((start,k)); start=k
    assert start==n
    return comps

def inverse_perm(perm):
    out=[0]*len(perm)
    for i,j in enumerate(perm): out[j]=i
    return tuple(out)

def maximal_runs(perm):
    m=len(perm); out=[]; j=0
    while j<m:
        st=j; d=j-perm[j]; j+=1
        while j<m and j-perm[j]==d:
            j+=1
        out.append((st,j-st,d))
    return out

def run_constants(perm):
    m=len(perm)
    rr=sorted(maximal_runs(perm),key=lambda z:z[2])
    cum=Fraction(0); A=Fraction(0); S2=0
    for st,ell,d in rr:
        alpha=Fraction(ell,m)
        mu=-1+2*cum+alpha
        A += ell*d*mu
        S2 += ell*ell
        cum += alpha
    C=Fraction(m*m-S2,2)
    return A,C

def psi12(k):
    k=abs(k)
    if k==0: return 8
    if k==1: return 13
    return 12*k

def J_fraction(perm):
    n=len(perm); S=0
    for i in range(n):
        for j in range(n):
            d=i-j; e=perm[i]-perm[j]
            S += abs(d-e)*psi12(d+e)
    return Fraction(S,12*n**4)

def global_perm(n,k,local):
    p=list(range(n))
    for j,v in enumerate(local):
        p[k+j]=k+v
    return tuple(p)

def matching_certificate(perm):
    n=len(perm)
    a=np.array([2*i+1-n for i in range(n)],dtype=np.int64)
    cells=[(r,s) for r in range(n) for s in range(n)]
    labels=[i for i in range(n) for _ in range(n)]
    lab=np.array(labels,dtype=np.int64)
    lab_x=a[lab]
    lab_y=a[np.array([perm[i] for i in labels],dtype=np.int64)]

    M=np.empty((n*n,n*n),dtype=np.int64)
    for rr,(r,s) in enumerate(cells):
        M[rr,:]=a[r]*lab_x+a[s]*lab_y

    rows,cols=linear_sum_assignment(-M)
    counts=[0]*n; W=0
    for rr,cc in zip(rows,cols):
        i=labels[cc]; counts[i]+=1
        r,s=cells[rr]
        W += int(a[r])*int(a[i]) + int(a[s])*int(a[perm[i]])
    assert counts==[n]*n
    return W,15*W-7*n*n*(n*n-1)

def HG_interval(a,b):
    a=sp.Rational(a) if not isinstance(a,sp.Basic) else a
    b=sp.Rational(b) if not isinstance(b,sp.Basic) else b
    L=sp.simplify(b-a)
    mid=sp.simplify((a+b)/2)
    rt2=sp.sqrt(2)
    def Hleft(t): return rt2*sp.Rational(2,3)*t**sp.Rational(3,2)
    def Hright(t): return -rt2*sp.Rational(2,3)*(1-t)**sp.Rational(3,2)
    def Ileft(t):
        return (-t**2/sp.Integer(2)+mid*t
                +rt2*(sp.Rational(2,5)*t**sp.Rational(5,2)
                       -sp.Rational(2,3)*mid*t**sp.Rational(3,2)))
    def Iright(t):
        return (t**2/sp.Integer(2)-mid*t
                -rt2*(sp.Rational(2,3)*(mid-1)*(1-t)**sp.Rational(3,2)
                       +sp.Rational(2,5)*(1-t)**sp.Rational(5,2)))
    Hnum=sp.S(0); Inum=sp.S(0); half=sp.Rational(1,2)
    if a<half:
        x2=b if b<=half else half
        Hnum += Hleft(x2)-Hleft(a)
        Inum += Ileft(x2)-Ileft(a)
    if b>half:
        x1=a if a>=half else half
        Hnum += Hright(b)-Hright(x1)
        Inum += Iright(b)-Iright(x1)
    H=sp.simplify(Hnum/L)
    G=sp.simplify(4*Inum/L**2)
    return H,G

# ---- S6 structure ----
S6=list(itertools.permutations(range(6)))
indecomp=[p for p in S6 if max(b-a for a,b in consecutive_components(p))==6]
assert len(indecomp)==461

hardA=(1,3,0,5,2,4)
hardB=(2,0,4,1,5,3)
assert inverse_perm(hardA)==hardB

bad=[]
for p in indecomp:
    A,C=run_constants(p)
    if 5*A < 2*C:
        bad.append((p,A,C))
assert bad==[
    (hardA,Fraction(17,3),Fraction(15)),
    (hardB,Fraction(17,3),Fraction(15)),
]

# ---- generic cyclic rotations ----
m,r=sp.symbols("m r", positive=True)
Ccyc=sp.simplify((m**2-((m-r)**2+r**2))/2)
Acyc=sp.simplify(
    (m-r)*(-r)*(-r/m)
    +r*(m-r)*((m-r)/m)
)
assert sp.simplify(Ccyc-r*(m-r))==0
assert sp.simplify(Acyc-r*(m-r))==0

# ---- special grouped transport for hardA ----
t=sp.symbols("t", real=True)
Rm2_lo=-2+4*t; Rm2_hi=4*t
Rm1=-5+2*t
Rp1=3+2*t
Rp2_lo=-4+4*t; Rp2_hi=-2+4*t
R0=12*t-6
Rbar_lo=sp.simplify(sp.Rational(1,3)*Rm2_lo+sp.Rational(1,6)*Rm1+
                    sp.Rational(1,6)*Rp1+sp.Rational(1,3)*Rp2_lo)
Rbar_hi=sp.simplify(sp.Rational(1,3)*Rm2_hi+sp.Rational(1,6)*Rm1+
                    sp.Rational(1,6)*Rp1+sp.Rational(1,3)*Rp2_hi)
assert sp.expand(Rbar_lo-R0)==sp.expand(sp.Rational(11,3)-sp.Rational(26,3)*t)
assert sp.expand(Rbar_hi-R0)==sp.expand(5-sp.Rational(26,3)*t)
Bscore=(sp.Rational(1,3)*(-2)*sp.Rational(-2,3)
        +sp.Rational(1,6)*(-1)*sp.Rational(-1,6)
        +sp.Rational(1,6)*(1)*sp.Rational(1,6)
        +sp.Rational(1,3)*(2)*sp.Rational(2,3))
assert Bscore==sp.Rational(17,18)
assert sp.Rational(17)-39*sp.Rational(2,5)==sp.Rational(7,5)

# ---- finite bridge n=6,...,11 ----
summary={}
cell_mins={}
uncertified=[]
for n in range(6,12):
    endpoint_count=0; cell_count=0; minmargin=None
    for k in range(n-5):
        for local in indecomp:
            gp=global_perm(n,k,local)
            J=J_fraction(gp)
            if J>=Fraction(2,15):
                endpoint_count+=1
                continue
            W,margin=matching_certificate(gp)
            if margin>=0:
                cell_count+=1
                minmargin=margin if minmargin is None else min(minmargin,margin)
            else:
                uncertified.append((n,k,local,J,W,margin))
    summary[n]=(endpoint_count,cell_count)
    cell_mins[n]=minmargin

assert len(uncertified)==1
n,k,local,J,W,margin=uncertified[0]
assert (n,k,local,margin)==(6,0,(5,4,3,2,1,0),-240)
A,C=run_constants(local)
assert A==Fraction(35,3) and C==Fraction(15)
assert A*Fraction(2,3)-C*Fraction(7,15)==Fraction(7,9)>0

# ---- exact interval bridge n=12,...,17 ----
ratio_mins={}
for n in range(12,18):
    vals=[]
    for k in range(n-5):
        H,G=HG_interval(sp.Rational(k,n),sp.Rational(k+6,n))
        d=sp.factor(2*H-5*G)
        assert d.is_nonnegative is True
        vals.append((k,d))
    ratio_mins[n]=min(vals,key=lambda z:float(sp.N(z[1],30)))

print("EXACT SIX-BIN CHECKS PASSED")
print("indecomposable S6:",len(indecomp))
print("only A/C<2/5:",bad)
print("n=6..11 endpoint/cell summary:")
for n in range(6,12):
    print(n,summary[n],"min cell margin",cell_mins[n])
print("sole endpoint/cell residual:",uncertified[0])
print("n=12..17 exact minima of 2H-5G:")
for n in range(12,18):
    print(n,ratio_mins[n][0],sp.factor(ratio_mins[n][1]))
