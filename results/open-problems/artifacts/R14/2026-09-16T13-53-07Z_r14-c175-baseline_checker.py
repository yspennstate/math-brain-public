#!/usr/bin/env python3
from fractions import Fraction

# Exact-rational checker for R14-C175:
# kappa=-1 Gardner/Stojnic upper endpoint
# f_gar(-1)=2 Q(1)-phi(1), alpha_U=1/f_gar(-1).
# All theorem-producing inequalities are exact Fraction comparisons.

class I:
    def __init__(self, lo, hi=None):
        self.lo=Fraction(lo)
        self.hi=Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self + (-(o if isinstance(o,I) else I(o)))
    def __rsub__(self,o): return I(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        xs=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(xs),max(xs))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0 or self.hi<0
        vals=[1/self.lo,1/self.hi]
        return I(min(vals),max(vals))
    def __truediv__(self,o):
        return self*(o if isinstance(o,I) else I(o)).inv()
    def dec(self): return float(self.lo),float(self.hi)

# Machin: pi=16 atan(1/5)-4 atan(1/239), with alternating rational bounds.
def atan_bounds(x, oddN):
    if oddN%2==0: oddN+=1
    def S(N):
        s=Fraction(0)
        for n in range(N+1):
            t=x**(2*n+1)/Fraction(2*n+1)
            s += t if n%2==0 else -t
        return s
    return S(oddN), S(oddN-1) # lower, upper
aL,aU=atan_bounds(Fraction(1,5),13)
bL,bU=atan_bounds(Fraction(1,239),3)
piL=16*aL-4*bU
piU=16*aU-4*bL

# Simple rational enclosure of c=(2 pi)^(-1/2), certified by squaring.
cL=Fraction(39894228,10**8)
cU=Fraction(39894229,10**8)
assert 2*piU*cL*cL < 1
assert 2*piL*cU*cU > 1
c=I(cL,cU)

# Alternating series exp(-1/2).
def exp_neg_bounds(x, Neven=24):
    def S(N):
        s=Fraction(0); xp=Fraction(1); fact=1
        for n in range(N+1):
            if n:
                xp*=x; fact*=n
            term=xp/fact
            s += term if n%2==0 else -term
        return s
    return S(Neven+1),S(Neven)
eL,eU=exp_neg_bounds(Fraction(1,2))
phi=c*I(eL,eU)

# Integral I=int_0^1 exp(-t^2/2) dt by alternating integrated Taylor series.
def gauss_int_bounds(a, Neven=24):
    def S(N):
        s=Fraction(0); fact=1
        for n in range(N+1):
            if n: fact*=n
            term=a**(2*n+1)/(2**n*fact*(2*n+1))
            s += term if n%2==0 else -term
        return s
    return S(Neven+1),S(Neven)
jL,jU=gauss_int_bounds(Fraction(1,1))
J=I(jL,jU)

# Q(1)=1/2 - c*J.
Q=I(Fraction(1,2))-c*J

# Integration by parts:
# int_1^inf (z-1)^2 phi(z) dz
# = [Q + phi] - 2 phi + Q = 2Q-phi.
f=2*Q-phi
assert f.lo > 0
alphaU=f.inv()
width=alphaU-I(2)

# Exact coarse readable enclosures.
assert alphaU.lo > Fraction(13273,1000)
assert alphaU.hi < Fraction(13274,1000)
assert width.lo > Fraction(11273,1000)
assert width.hi < Fraction(11274,1000)

print("R14-C175 exact rational checker: PASS")
print("Q(1) in", Q.dec())
print("phi(1) in", phi.dec())
print("f_gar(-1)=2Q-phi in", f.dec())
print("alpha_U in", alphaU.dec())
print("width alpha_U-2 in", width.dec())
print("CERT: 13.273 < alpha_U < 13.274")
print("CERT: 11.273 < width < 11.274")
print("PASS")
