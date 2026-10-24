"""Exact rational self-check for R15 retained F0111 fixed-ray corridor theorem.

This verifies the finite interval core only.  It says nothing about native
Burdzy--Scheutzow Problem 7.2 / I0076 and is not an independent audit.
All endpoints, root brackets, interval operations and logarithm enclosures are
rational Fractions.  Float renderings in the output are summaries only.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from functools import lru_cache
from math import factorial

EPS = F(1,400)
T = F(401,400)
SMIN = F(1,10000)
ROOT_ITERS = 32
BASE_SLABS = 64
MAX_DEPTH = 8
LOG_TERMS = 18

# ---------- scalar functions ----------
def UK(d,s):
    d,s=F(d),F(s)
    return F(29)*(d+1)*(d+s+1)*(d+2*s+1)/(4*(s+1)*(s+2))

def LK(d,s):
    d,s=F(d),F(s)
    P=(d*d*s*s+d*d*s+7*d*s**3+26*d*s**2+32*d*s+12*d
       +9*s**4+51*s**3+109*s**2+103*s+36)
    Q=(d*d*s+d*d+3*d*s*s+6*d*s+4*d+3*s**3+9*s**2+9*s+3)
    return -(d+2*s+1)*P/(2*(d-1)*Q)

def root_bracket(fun,N,s,iters=ROOT_ITERS):
    lo,hi=F(2,5),F(3,5)
    assert fun(lo,s)<N<fun(hi,s)
    for _ in range(iters):
        mid=(lo+hi)/2
        if fun(mid,s)<N:
            lo=mid
        else:
            hi=mid
    assert fun(lo,s)<N<fun(hi,s)
    return lo,hi

# ---------- rational interval arithmetic ----------
@dataclass(frozen=True)
class IV:
    lo:F
    hi:F
    def __post_init__(self):
        assert self.lo<=self.hi
    @staticmethod
    def c(x):
        x=F(x); return IV(x,x)
    def __add__(self,o):
        o=o if isinstance(o,IV) else IV.c(o)
        return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self + -(o if isinstance(o,IV) else IV.c(o))
    def __rsub__(self,o): return IV.c(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,IV) else IV.c(o)
        vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,IV) else IV.c(o)
        assert not (o.lo<=0<=o.hi)
        return self*IV(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return IV.c(o)/self
    def __pow__(self,n):
        if n==0: return IV.c(1)
        if n==2:
            if self.lo<=0<=self.hi:
                return IV(F(0),max(self.lo*self.lo,self.hi*self.hi))
            vals=(self.lo*self.lo,self.hi*self.hi)
            return IV(min(vals),max(vals))
        assert n>0
        out=IV.c(1)
        for _ in range(n): out=out*self
        return out

# ---------- exact logarithm enclosures ----------
def log_unit_bounds(y):
    y=F(y); assert 1<=y<=2
    w=(y-1)/(y+1); w2=w*w
    term=w; partial=F(0)
    for j in range(LOG_TERMS):
        partial += term/F(2*j+1)
        term *= w2
    lo=2*partial
    rem=2*term/F(2*LOG_TERMS+1)/(1-w2)
    return lo,lo+rem

LOG2=log_unit_bounds(F(2))

@lru_cache(maxsize=200000)
def log_point_bounds(x):
    x=F(x); assert x>0
    y=x; m=0
    while y>=2:
        y/=2; m+=1
    while y<1:
        y*=2; m-=1
    ly,uy=log_unit_bounds(y); l2,u2=LOG2
    if m>=0:
        return F(m)*l2+ly,F(m)*u2+uy
    return F(m)*u2+ly,F(m)*l2+uy

def log_iv(a):
    assert a.lo>0
    lo,_=log_point_bounds(a.lo)
    _,hi=log_point_bounds(a.hi)
    return IV(lo,hi)

# ---------- one feasible-corridor slab ----------
def lower_box(N,slo,shi):
    C=F(15 if N==12 else 17)

    # Carried exact monotonicity: both roots d_U(s),d_L(s) decrease in s.
    du_lo,_=root_bracket(UK,N,shi)
    _,dl_hi=root_bracket(LK,N,slo)
    if du_lo>=dl_hi:
        return None

    d=IV(du_lo,dl_hi)
    s=IV(slo,shi)

    # D=1/S=-k/29, written without cancellation-prone k.
    g=2*(1+s)*(2+s)/(F(29)*(1-d*d)*(d+3+3*s)) # D/s
    D=s*g

    UKiv=F(29)*(d+1)*(d+s+1)*(d+2*s+1)/(4*(s+1)*(s+2))
    eta_raw=UKiv-N
    # Feasibility itself gives eta=U_K-N>0.
    eta=IV(max(F(0),eta_raw.lo),max(F(0),eta_raw.hi))

    A=1-C*s
    # Exact mass-defect simplification for the two-heavy second coordinate.
    B=C*s+(1-eta)*D

    assert F(0)<A.lo<=A.hi<F(1)
    assert F(0)<B.lo<=B.hi<F(1)
    assert F(0)<D.lo<=D.hi<F(1)
    # This also certifies S<200000 on the whole post-small-scale corridor.
    assert D.lo>F(1,200000)

    lA=log_iv(A); lB=log_iv(B); lD=log_iv(D)
    E=-(A*lA)-(B*lB)+(D*lD)
    V=A*(lA**2)+B*(lB**2)
    q1=log_iv(A/D)
    q2=log_iv(B/D)
    assert q1.lo>0 and q2.lo>=0

    # Exact simplified U_max/s for each of the two remaining cells.
    if N==12:
        Us=(d+s+1)*(-11*d**2-20*d*s+4*d+4*s**2+34*s+19)/(4*(d+1)**2*(d+3*s+3))
    else:
        Us=(d+s+1)*(-6*d**2-11*d*s+2*d+2*s**2+18*s+10)/(2*(d+1)**2*(d+3*s+3))
    Uhi=max(F(0),Us.hi)*shi

    # Drop the positive eta*D term.  For c_K use the carried exact global
    # scalar bound c_K<21/20 on both cells; the report gives its short proof.
    cbar=F(21,20)
    energy=T*EPS*Uhi*q1.hi*q2.hi
    kloss=T*(1+eta.hi/2)*eta.hi*D.hi*cbar
    lower=EPS*E.lo-(EPS*EPS/F(2))*V.hi-energy-kloss
    return lower

# exp(28)>200000, so D>1/200000 implies log S<28 and
# EPS*log S<7/100.  This makes the previous adaptive-ray extremizer theorem
# applicable pointwise to the fixed ray t=401/400.
exp28_lower=sum(F(28)**j/F(factorial(j)) for j in range(8))
assert exp28_lower>200000
print("FIXED_RAY_RANGE_PASS", exp28_lower-200000)


def certify(N,smax):
    stack=[]
    for i in range(BASE_SLABS):
        lo=SMIN+(smax-SMIN)*i/BASE_SLABS
        hi=SMIN+(smax-SMIN)*(i+1)/BASE_SLABS
        stack.append((lo,hi,0))
    leaves=0; skipped=0; maxdepth=0; worst=None; worst_s=None
    while stack:
        lo,hi,depth=stack.pop()
        lower=lower_box(N,lo,hi)
        if lower is None:
            skipped+=1
            continue
        if lower>0:
            leaves+=1
            maxdepth=max(maxdepth,depth)
            if worst is None or lower<worst:
                worst=lower; worst_s=(lo,hi)
            continue
        if depth>=MAX_DEPTH:
            raise AssertionError(("UNCERTIFIED",N,lo,hi,lower))
        mid=(lo+hi)/2
        stack.append((mid,hi,depth+1))
        stack.append((lo,mid,depth+1))
    assert worst is not None and worst>0
    print("CORRIDOR_PASS",
          "N=",N,
          "leaves=",leaves,
          "skipped=",skipped,
          "maxdepth=",maxdepth,
          "worst_lower_float=",float(worst),
          "worst_num_positive=",worst.numerator>0,
          "worst_num_bits=",worst.numerator.bit_length(),
          "worst_den_bits=",worst.denominator.bit_length(),
          "worst_slo=",worst_s[0],
          "worst_shi=",worst_s[1])

certify(12,F(3601,250000))
certify(13,F(12637,1000000))
print("FULL_REMAINING_N12_N13_CORRIDORS_EXCLUDED_FOR_S_GE_1E_MINUS_4")
print("ALL_EXACT_CHECKS_PASS")
