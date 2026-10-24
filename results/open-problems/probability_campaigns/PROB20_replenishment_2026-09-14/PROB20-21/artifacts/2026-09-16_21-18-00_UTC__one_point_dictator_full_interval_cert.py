#!/usr/bin/env python3
"""
PROB20-21 exact/rational certificate for the seven-bit one-point dictator perturbation.

Target special case:
    f(x)=x_1 except f(1,1,1,1,1,1,1)=0
in {0,1} coding (equivalently f~(x)=x_1-2*1_{x=1^7} in {-1,+1} coding).

This checker certifies the remaining middle-noise interval
    alpha in [1/5000, 67/135].
The already archived all-function endpoint theorems cover
    [0,1/5000] and [67/135,1/2].

Proof architecture checked here:
1) Exact posterior reduction to a scalar random variable S with
       S in [a^6,(1-a)^6], E S = 1/64.
2) A strictly concave integrand G_a(s), so E G_a(S) is bounded below
   by the secant through the two support endpoints.
3) For a in [1/5000,37/100], exact rational interval arithmetic proves
   a stronger lower surrogate L(a)>0 on cells of width 1/2000.
   All logarithms are enclosed by rational atanh series with explicit tail.
4) For a in [37/100,67/135], Pinsker + chi-square reduce endpoint
   positivity to two polynomial inequalities. Exact Bernstein coefficients
   prove them on the stronger rho interval [0,13/50].

Standard library only. Every proof-critical numerical inequality is rational.
"""
from fractions import Fraction
from functools import lru_cache
from dataclasses import dataclass
from math import comb

M=6
EPS=Fraction(1,64)
A_LO=Fraction(1,5000)
A_SPLIT=Fraction(37,100)
A_HI=Fraction(67,135)
STEP=Fraction(1,2000)
KLOG=30

# ---------- exact logarithm enclosures ----------
def ln2_bounds():
    t=Fraction(1,3)
    tt=t*t
    p=t
    z=Fraction(0)
    for k in range(KLOG+1):
        if k:
            p*=tt
        z += Fraction(2,2*k+1)*p
    rem=Fraction(2,2*KLOG+3)*p*tt/(1-tt)
    return z,z+rem

LN2_LO,LN2_HI=ln2_bounds()

@lru_cache(maxsize=None)
def ln_bounds(q):
    q=Fraction(q)
    assert q>0
    if q==1:
        return Fraction(0),Fraction(0)
    e=q.numerator.bit_length()-q.denominator.bit_length()
    scale=Fraction(2**e,1) if e>=0 else Fraction(1,2**(-e))
    s=q/scale
    while s<1:
        s*=2; e-=1
    while s>=2:
        s/=2; e+=1
    t=(s-1)/(s+1)
    tt=t*t
    p=t
    z=Fraction(0)
    for k in range(KLOG+1):
        if k:
            p*=tt
        z += Fraction(2,2*k+1)*p
    rem=Fraction(2,2*KLOG+3)*p*tt/(1-tt)
    if e>=0:
        return z+e*LN2_LO, z+rem+e*LN2_HI
    return z+e*LN2_HI, z+rem+e*LN2_LO

@dataclass(frozen=True)
class IV:
    lo: Fraction
    hi: Fraction
    def __post_init__(self):
        assert self.lo<=self.hi
    @staticmethod
    def pt(x):
        return IV(Fraction(x),Fraction(x))
    def __add__(self,o):
        o=o if isinstance(o,IV) else IV.pt(o)
        return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):
        return IV(-self.hi,-self.lo)
    def __sub__(self,o):
        return self+(-(o if isinstance(o,IV) else IV.pt(o)))
    def __rsub__(self,o):
        return (o if isinstance(o,IV) else IV.pt(o))-self
    def __mul__(self,o):
        o=o if isinstance(o,IV) else IV.pt(o)
        v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(v),max(v))
    __rmul__=__mul__
    def reciprocal(self):
        assert not (self.lo<=0<=self.hi)
        x,y=Fraction(1,self.lo),Fraction(1,self.hi)
        return IV(min(x,y),max(x,y))
    def __truediv__(self,o):
        o=o if isinstance(o,IV) else IV.pt(o)
        return self*o.reciprocal()
    def powi(self,n):
        assert n>=0
        if n==0:
            return IV.pt(1)
        if self.lo>=0:
            return IV(self.lo**n,self.hi**n)
        vals=[self.lo**n,self.hi**n]
        if n%2==0 and self.lo<0<self.hi:
            return IV(Fraction(0),max(vals))
        return IV(min(vals),max(vals))
    def log(self):
        assert self.lo>0
        l,_=ln_bounds(self.lo)
        _,u=ln_bounds(self.hi)
        return IV(l,u)

ONE=IV.pt(1)
LN2=IV(LN2_LO,LN2_HI)
G0=IV(*ln_bounds(1-EPS*EPS))*Fraction(1,2)

def entropy_iv(x):
    # exact enclosure of -x log x -(1-x) log(1-x), away from 0/1
    assert x.lo>0 and x.hi<1
    return -(x*x.log()+(ONE-x)*(ONE-x).log())

def capacity_iv(a):
    return LN2-entropy_iv(a)

def kl_bias_iv(z):
    # D(Bern((1+z)/2) || Bern((1+eps)/2))
    ep=IV.pt(EPS)
    return Fraction(1,2)*(
        (ONE+z)*((ONE+z)/(ONE+ep)).log()
        +(ONE-z)*((ONE-z)/(ONE-ep)).log()
    )

def low_surrogate_iv(lo,hi):
    """
    G_a(s)= (1+s)/2 * I(Bern(s/(1+s)); BSC(a))
            - D(Bern((1+s)/2)||Bern((1+eps)/2)).

    Concavity of G and E[S]=eps yield secant weights
       w=(eps-A)/(B-A), A=a^6, B=(1-a)^6.

    Endpoint lower bounds:
      G(A)>=G0=1/2 log(1-eps^2), because A<=eps, MI>=0,
      and KL(z||eps) is maximized at z=0 on z in [0,eps].
      G(B)>=B*C(a)-D_B, because entropy concavity gives
      I(theta;BSC(a)) >= 2 theta C(a).
    Thus defect >= L(a)=G0+w(B*C(a)-D_B-G0).
    """
    a=IV(Fraction(lo),Fraction(hi))
    b=ONE-a
    A=a.powi(6)
    B=b.powi(6)
    num=IV.pt(EPS)-A
    den=B-A
    assert num.lo>0 and den.lo>0
    w=num/den
    LB=B*capacity_iv(a)-kl_bias_iv(B)
    return G0+w*(LB-G0)

# ---------- low/middle compact interval ----------
cell_count=0
min_low=None
min_cell=None
x=A_LO
while x<A_SPLIT:
    y=min(x+STEP,A_SPLIT)
    cert=low_surrogate_iv(x,y)
    assert cert.lo>0, (x,y,cert)
    if min_low is None or cert.lo<min_low:
        min_low=cert.lo
        min_cell=(x,y)
    cell_count+=1
    x=y

# ---------- polynomial helpers ----------
def padd(p,q):
    n=max(len(p),len(q))
    out=[Fraction(0)]*n
    for i,v in enumerate(p): out[i]+=v
    for i,v in enumerate(q): out[i]+=v
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def pneg(p): return [-v for v in p]
def psub(p,q): return padd(p,pneg(q))

def pmul(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def pscale(p,c): return [Fraction(c)*x for x in p]

def ppow(p,n):
    out=[Fraction(1)]
    for _ in range(n):
        out=pmul(out,p)
    return out

def bernstein_coeffs_on_0_scale(power_coeffs,scale):
    # q(scale*s)=sum a_j s^j -> degree-n Bernstein coefficients
    n=len(power_coeffs)-1
    a=[power_coeffs[j]*scale**j for j in range(n+1)]
    out=[]
    for k in range(n+1):
        out.append(sum(
            a[j]*Fraction(comb(k,j),comb(n,j))
            for j in range(k+1)
        ))
    return out

# High-middle endpoint lower bound:
# Pinsker in nats gives I(theta;BSC)>=2*rho^2 theta(1-theta).
# Bernoulli KL <= chi-square gives
#   G_a(z)>=rho^2 z/(1+z) - (z-eps)^2/(1-eps^2).
# Multiply positives:
# P(z,rho)=(1-eps^2)rho^2 z -(1+z)(z-eps)^2.
# Put a=(1-rho)/2 and z=a^6 or (1-a)^6.
# Exact algebra has P=-rho^2 Q(rho)/262144.
# We verify both identities and Q<0 on rho in [0,13/50],
# stronger than the required [1/135,13/50].

t=[Fraction(0),Fraction(1)]
one=[Fraction(1)]
a_poly=[Fraction(1,2),Fraction(-1,2)]   # (1-t)/2
b_poly=[Fraction(1,2),Fraction(1,2)]    # (1+t)/2
rho2=ppow(t,2)
Apoly=ppow(a_poly,6)
Bpoly=ppow(b_poly,6)

def Ppoly(z):
    zme=psub(z,[EPS])
    return psub(
        pscale(pmul(rho2,z),1-EPS*EPS),
        pmul(padd(one,z),ppow(zme,2)),
    )

PA=Ppoly(Apoly)
PB=Ppoly(Bpoly)

# Q coefficient lists, low degree -> high degree, derived from exact expansion.
QA=[
    Fraction(-1755),Fraction(12654),Fraction(-29580),Fraction(24990),
    Fraction(14300),Fraction(-56358),Fraction(70353),Fraction(-62260),
    Fraction(47850),Fraction(-32568),Fraction(18626),Fraction(-8568),
    Fraction(3060),Fraction(-816),Fraction(153),Fraction(-18),Fraction(1)
]
QB=[
    Fraction(-1755),Fraction(-12654),Fraction(-29580),Fraction(-24990),
    Fraction(14300),Fraction(56358),Fraction(70353),Fraction(62260),
    Fraction(47850),Fraction(32568),Fraction(18626),Fraction(8568),
    Fraction(3060),Fraction(816),Fraction(153),Fraction(18),Fraction(1)
]

# Verify the factorization coefficient-by-coefficient.
targetA=pscale(pmul(rho2,QA),Fraction(-1,262144))
targetB=pscale(pmul(rho2,QB),Fraction(-1,262144))
assert PA==targetA
assert PB==targetB

RMAX=Fraction(13,50)
BA=bernstein_coeffs_on_0_scale(QA,RMAX)
BB=bernstein_coeffs_on_0_scale(QB,RMAX)
assert all(c<0 for c in BA)
assert all(c<0 for c in BB)

print("PROB20-21 ONE-POINT DICTATOR PERTURBATION MIDDLE-INTERVAL CERTIFICATE: PASS")
print("special_case","n=7 one-point dictator perturbation")
print("middle_alpha_interval","[1/5000,67/135]")
print("low_subinterval","[1/5000,37/100]")
print("low_cells",cell_count,"step",STEP)
print("low_min_lower_positive",min_low>0)
print("low_min_num_digits",len(str(min_low.numerator)),"den_digits",len(str(min_low.denominator)))
print("low_min_approx",float(min_low),"cell",min_cell)
print("high_subinterval","[37/100,67/135]")
print("rho_polynomial_domain_certified","[0,13/50]")
print("QA_bernstein_max",max(BA),"approx",float(max(BA)))
print("QB_bernstein_max",max(BB),"approx",float(max(BB)))
print("note","Combined with previously archived all-function endpoint coverage [0,1/5000] and [67/135,1/2], this special function is certified for the entire alpha interval.")
