"""Exact/self-check artifact for PROB20-05 nine-bin finite bridge n=9,...,17.

The script reconstructs the displacement-group rational inequalities, exact triangular
block moments, and exact integer cell certificate. SciPy's Hungarian algorithm is used
only to FIND a balanced cell assignment; every returned score is recomputed as an
integer and only that exact score is used as a certificate.

Runtime is intentionally nontrivial: this is an exhaustive 9! finite check. The report
records split-run results obtained from the same routines.
"""
import itertools
from fractions import Fraction
from collections import defaultdict
import numpy as np
import sympy as sp
from scipy.optimize import linear_sum_assignment

# ---------- exact displacement-group profile ----------
def profile_exact(p):
    m=len(p); g=defaultdict(list)
    for j,x in enumerate(p): g[j-x].append(j)
    gg=sorted(g.items()); cumz=Fraction(0); B=Fraction(0)
    br={Fraction(0),Fraction(1)}; PG=[]
    for d,js in gg:
        k=len(js); al=Fraction(k,m); mu=-1+2*cumz+al
        B += al*d*mu; cumz += al; pcs=[]
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
            _,_,s,q=pcs[r]; sl+=al*s; ic+=al*q
        out.append((a,b,sl-Fraction(2*m),ic+Fraction(m)))
    return B,out

def threshold_ok_profile(prof,rho):
    B,pieces=prof; coeff=2*B/rho; cum=Fraction(0)
    for a,b,sl,ic in pieces:
        A2=sl/2; A1=ic; A0=cum-A2*a*a-A1*a
        qa=A2+coeff; qb=A1-coeff
        vals=[qa*a*a+qb*a+A0,qa*b*b+qb*b+A0]
        if qa<0:
            v=-qb/(2*qa)
            if a<=v<=b: vals.append(qa*v*v+qb*v+A0)
        if max(vals)>0: return False
        cum += sl*(b*b-a*a)/2+ic*(b-a)
    assert cum==0
    return True

# ---------- exact triangular block moments ----------
def HGS(a,b):
    a=sp.Rational(a); b=sp.Rational(b); L=b-a; mid=(a+b)/2
    rt2=sp.sqrt(2); hh=sp.Rational(1,2)
    HL=lambda x: rt2*sp.Rational(2,3)*x**sp.Rational(3,2)
    HR=lambda x: -rt2*sp.Rational(2,3)*(1-x)**sp.Rational(3,2)
    IL=lambda x: -x*x/2+mid*x+rt2*(sp.Rational(2,5)*x**sp.Rational(5,2)-sp.Rational(2,3)*mid*x**sp.Rational(3,2))
    IR=lambda x: x*x/2-mid*x-rt2*(sp.Rational(2,3)*(mid-1)*(1-x)**sp.Rational(3,2)+sp.Rational(2,5)*(1-x)**sp.Rational(5,2))
    def piece(F1,F2,x,y):
        z=sp.S(0)
        if x<hh: z+=F1(min(y,hh))-F1(x)
        if y>hh: z+=F2(y)-F2(max(x,hh))
        return sp.simplify(z)
    H=sp.simplify(piece(HL,HR,a,b)/L)
    G=sp.simplify(4*piece(IL,IR,a,b)/L**2)
    return H,G

# Rational upper bounds used in the finite bridge.
RHOS={
    9:Fraction(7,10),
    10:Fraction(57,100),
    11:Fraction(503,1000),
    12:Fraction(58,125),
    13:Fraction(219,500),
    14:Fraction(211,500),
    15:Fraction(411,1000),
}
EXPECTED_FAIL={9:310662,10:143514,11:68822,12:40129,13:27658,14:20412,15:16785}
EXPECTED_CONFIG={9:310662,10:287028,11:206466,12:160516,13:138290,14:122472,15:117495}

for n,rho in RHOS.items():
    sr=sp.Rational(rho.numerator,rho.denominator)
    for k in range(n-8):
        H,G=HGS(sp.Rational(k,n),sp.Rational(k+9,n))
        assert sp.simplify(sr*H-G).is_nonnegative is True

# n=16,17 interior positions are below the inherited universal S9 threshold 23/72.
for n in (16,17):
    for k in range(1,n-9):
        H,G=HGS(sp.Rational(k,n),sp.Rational(k+9,n))
        assert sp.simplify(sp.Rational(23,72)*H-G).is_positive is True
    rho=sp.Rational(81,200) if n==16 else sp.Rational(201,500)
    for k in (0,n-9):
        H,G=HGS(sp.Rational(k,n),sp.Rational(k+9,n))
        assert sp.simplify(rho*H-G).is_positive is True

# ---------- global symmetries and cell certificate ----------
def global_perm(n,k,p):
    q=list(range(n))
    for j,x in enumerate(p): q[k+j]=k+x
    return tuple(q)

def inv(p):
    q=[0]*len(p)
    for i,j in enumerate(p): q[j]=i
    return tuple(q)

def rc(p):
    n=len(p)
    return tuple(n-1-p[n-1-i] for i in range(n))

def canon4(p):
    return min(p,inv(p),rc(p),inv(rc(p)))

def cell_margin(p):
    n=len(p)
    a=np.arange(1-n,n,2,dtype=np.int64)
    labels=np.repeat(np.arange(n),n)
    rr=np.repeat(np.arange(n),n); ss=np.tile(np.arange(n),n)
    lx=a[labels]
    ly=a[np.array([p[i] for i in labels],dtype=np.int64)]
    M=a[rr,None]*lx[None,:]+a[ss,None]*ly[None,:]
    rows,cols=linear_sum_assignment(-M)
    # Exact recomputation of the returned assignment. We do NOT need to trust optimality.
    cnt=[0]*n; W=0
    for r,c in zip(rows,cols):
        lab=int(labels[c]); cnt[lab]+=1
        W += int(M[r,c])
    assert cnt==[n]*n
    return 15*W-7*n*n*(n*n-1)

ALL9=list(itertools.permutations(range(9)))
PROFILES={p:profile_exact(p) for p in ALL9}

# n=9,...,15 exact finite bridge.
expected_negative={
    9:set(),
    10:{(0,1,2,3,4,5,6,7,9,8)},
    11:set(),
    12:{(0,1,2,3,4,5,6,7,8,9,11,10)},
    13:{(0,1,2,3,4,5,6,7,8,9,10,12,11)},
    14:{(0,1,2,3,4,5,6,7,8,9,10,11,13,12)},
    15:{(0,1,2,3,4,5,6,7,8,9,10,11,12,14,13)},
}
expected_n9_min=60
for n,rho in RHOS.items():
    bad=[p for p in ALL9 if not threshold_ok_profile(PROFILES[p],rho)]
    assert len(bad)==EXPECTED_FAIL[n]
    configs=[global_perm(n,k,p) for p in bad for k in range(n-8)]
    assert len(configs)==EXPECTED_CONFIG[n]
    if n==9:
        margins=[cell_margin(q) for q in configs]
        assert min(margins)==expected_n9_min
        assert all(x>=0 for x in margins)
    else:
        reps={canon4(q) for q in configs}
        neg={q for q in reps if cell_margin(q)<0}
        assert neg==expected_negative[n]

# n=16,17: only endpoint blocks require finite work after the 23/72 interior theorem.
for n,rho,expected_count,adj in [
    (16,Fraction(81,200),15093,(1,0)+tuple(range(2,16))),
    (17,Fraction(201,500),14323,(1,0)+tuple(range(2,17))),
]:
    bad=[p for p in ALL9 if not threshold_ok_profile(PROFILES[p],rho)]
    assert len(bad)==expected_count
    # Left endpoint; inversion preserves that endpoint. Right endpoint follows by 180 rotation.
    reps={min(global_perm(n,0,p),inv(global_perm(n,0,p))) for p in bad}
    neg={q for q in reps if cell_margin(q)<0}
    assert neg=={adj}

print('EXACT NINE-BIN FINITE-BRIDGE CHECKS PASSED')
