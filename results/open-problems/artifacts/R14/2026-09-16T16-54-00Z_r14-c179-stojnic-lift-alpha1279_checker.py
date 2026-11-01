#!/usr/bin/env python3
from fractions import Fraction
import hashlib

print("R14-C179 exact partially-lifted Stojnic upper-bound certificate, kappa=-1")

class I:
    def __init__(self, lo, hi=None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self + (-(o if isinstance(o,I) else I(o)))
    def __rsub__(self,o): return I(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0 or self.hi<0
        vals=[1/self.lo,1/self.hi]; return I(min(vals),max(vals))
    def __truediv__(self,o): return self*(o if isinstance(o,I) else I(o)).inv()
    def dec(self): return float(self.lo),float(self.hi)

def atan_bounds(x, odd_N):
    if odd_N%2==0: odd_N+=1
    def S(N):
        s=Fraction(0)
        for n in range(N+1):
            t=x**(2*n+1)/Fraction(2*n+1)
            s += t if n%2==0 else -t
        return s
    return S(odd_N),S(odd_N-1)

aL,aU=atan_bounds(Fraction(1,5),11)
bL,bU=atan_bounds(Fraction(1,239),3)
piL=16*aL-4*bU
piU=16*aU-4*bL
c0L=Fraction(39894228,10**8)
c0U=Fraction(39894229,10**8)
assert 2*piU*c0L*c0L < 1
assert 2*piL*c0U*c0U > 1
print("Gaussian normalization enclosure: PASS")

def exp_neg_bounds(x, N_even=14):
    def S(N):
        s=Fraction(0); xp=Fraction(1); fact=1
        for n in range(N+1):
            if n:
                xp*=x; fact*=n
            term=xp/fact
            s += term if n%2==0 else -term
        return s
    return S(N_even+1),S(N_even)

def gauss_int_bounds(a,N_even=14):
    def S(N):
        s=Fraction(0); fact=1
        for n in range(N+1):
            if n: fact*=n
            term=a**(2*n+1)/(2**n*fact*(2*n+1))
            s += term if n%2==0 else -term
        return s
    return S(N_even+1),S(N_even)

I1L,I1U=gauss_int_bounds(Fraction(1))
Q1L=Fraction(1,2)-c0U*I1U
Q1U=Fraction(1,2)-c0L*I1L
assert 0 < Q1L < Q1U < Fraction(1,2)
print("Q(1) exact enclosure:",float(Q1L),float(Q1U))

c=Fraction(5633,5000)
alpha=Fraction(1279,100)

dU=Fraction(4591,2000)
assert dU*dU > c*c+4
xU=(c+dU)/2
assert xU>1
y=(xU-1)/(xU+1)
N=3
slog=Fraction(0)
for n in range(N+1):
    slog += y**(2*n+1)/Fraction(2*n+1)
tail = y**(2*N+3) / (Fraction(2*N+3)*(1-y*y))
logxU = 2*(slog+tail)
Aup=(dU-c)/4 + logxU/c
assert Aup < Fraction(769,1000)
print("Spherical part bound A(c)<",float(Aup),"<0.769: PASS")

def u_lower(b):
    IbL,IbU=gauss_int_bounds(b)
    QbU=Fraction(1,2)-c0L*IbL
    x=(1-b*b)/2
    eL,eU=exp_neg_bounds(x)
    return Q1L - b*eU*QbU

def P3(u):
    return u + u*u/2 + u*u*u/3

mesh=10000
stop=7600
maxB=None; maxcell=None
minu=None
for j in range(stop):
    a=Fraction(j,mesh)
    b=Fraction(j+1,mesh)
    ul=u_lower(b)
    assert ul>0
    if minu is None or ul<minu: minu=ul
    gamma_lower = c*a*a/(2*(1-a*a))
    B = Fraction(769,1000) - gamma_lower - (alpha/c)*P3(ul)
    if maxB is None or B>maxB:
        maxB=B; maxcell=(a,b,ul)
assert maxB < 0
print("Global scalar-sup cell certificate: PASS")
print(" cells =",stop)
print(" worst cell =",float(maxcell[0]),float(maxcell[1]))
print(" max exact upper bound =",float(maxB))
print(" min u_L =",float(minu))

s0=Fraction(19,25)
tail_bound=Fraction(769,1000)-c*s0*s0/(2*(1-s0*s0))
assert tail_bound<0
print("Tail certificate s>=19/25: PASS",float(tail_bound))

alphaL=Fraction(54299,25000)
width=alpha-alphaL
assert width == Fraction(265451,25000)
print("Metric movement certificate: PASS")
print(" alpha_L =",float(alphaL))
print(" alpha_U_new =",float(alpha))
print(" width_new =",width,"=",float(width))
print("ALL_EXACT_CHECKS_PASS")
