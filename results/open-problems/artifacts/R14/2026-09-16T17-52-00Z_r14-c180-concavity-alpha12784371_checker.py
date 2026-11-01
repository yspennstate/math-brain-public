#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

print("R14-C180/C181 exact Stojnic scalar-concavity certificate, kappa=-1")

class I:
    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, o): return self + (-(o if isinstance(o, I) else I(o)))
    def __rsub__(self, o): return I(o)-self
    def __mul__(self, o):
        o = o if isinstance(o, I) else I(o)
        vals = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def inv(self):
        assert self.lo > 0 or self.hi < 0
        vals=[1/self.lo,1/self.hi]
        return I(min(vals),max(vals))
    def __truediv__(self,o):
        return self*(o if isinstance(o,I) else I(o)).inv()
    def dec(self): return float(self.lo), float(self.hi)

def atan_bounds(x, odd_N=17):
    if odd_N % 2 == 0: odd_N += 1
    def S(N):
        z=Fraction(0)
        for n in range(N+1):
            t=x**(2*n+1)/Fraction(2*n+1)
            z += t if n%2==0 else -t
        return z
    return S(odd_N), S(odd_N-1)

aL,aU=atan_bounds(Fraction(1,5),17)
bL,bU=atan_bounds(Fraction(1,239),5)
piL=16*aL-4*bU
piU=16*aU-4*bL

c0L=Fraction(398942280401432,10**15)
c0U=Fraction(398942280401433,10**15)
assert 2*piU*c0L*c0L < 1
assert 2*piL*c0U*c0U > 1
print("Gaussian normalization exact enclosure: PASS")

def exp_neg_bounds(x,N_even=24):
    x=Fraction(x)
    def S(N):
        z=Fraction(0); xp=Fraction(1); fact=1
        for n in range(N+1):
            if n:
                xp*=x; fact*=n
            t=xp/fact
            z += t if n%2==0 else -t
        return z
    return S(N_even+1),S(N_even)

def gauss_int_bounds(a,N_even=24):
    a=Fraction(a)
    def S(N):
        z=Fraction(0); fact=1
        for n in range(N+1):
            if n: fact*=n
            t=a**(2*n+1)/(2**n*fact*(2*n+1))
            z += t if n%2==0 else -t
        return z
    return S(N_even+1),S(N_even)

def qbar_interval(s):
    iL,iU=gauss_int_bounds(s)
    return I(Fraction(1,2)-c0U*iU, Fraction(1,2)-c0L*iL)

def exp_h_interval(s):
    x=(1-Fraction(s)**2)/2
    eL,eU=exp_neg_bounds(x)
    return I(eL,eU)

e1L,e1U=exp_neg_bounds(Fraction(1,2))
phi1=I(c0L*e1L,c0U*e1U)
Q1=qbar_interval(Fraction(1))
Phi1=I(1)-Q1
assert (Q1/phi1).hi < Fraction(3,4)
assert piU < Fraction(648,169)
print("Mills endpoint ingredients: PASS; r(1)<3/4 and sqrt(pi/2)<18/13")

# Exact algebra for the comparison T(s)=(2+s^2)/(s(3+s^2)).
s=sp.symbols('s', positive=True)
T=(2+s**2)/(s*(3+s**2))
assert sp.simplify(sp.diff(T,s) + (s**4+3*s**2+6)/(s**2*(s**2+3)**2)) == 0
assert sp.simplify(sp.diff(T,s)-s*T+1 + 6/(s**2*(s**2+3)**2)) == 0
print("C180 comparison-ODE algebra: PASS")

def L_interval(s):
    s=Fraction(s)
    return Phi1 + s*exp_h_interval(s)*qbar_interval(s)

def Lp_interval(s):
    s=Fraction(s)
    return exp_h_interval(s)*(1+s*s)*qbar_interval(s) - s*phi1

c=Fraction(5633,5000)
alpha=Fraction(12784371,10**6)  # 12.784371

def Jp_interval(s):
    s=Fraction(s)
    det=-c*s/(1-s*s)**2
    return I(det)+(alpha/c)*(Lp_interval(s)/L_interval(s))

# Tight exact upper bound on A_c.
target=c*c+4
# Fixed rationals checked by squaring, no floating decision.
dL=Fraction(2295479810410015,10**15)
dU=Fraction(2295479810410016,10**15)
assert dL*dL < target < dU*dU

xU=(c+dU)/2
y=(xU-1)/(xU+1)
N=10
slog=sum(y**(2*n+1)/Fraction(2*n+1) for n in range(N+1))
tail=y**(2*N+3)/(Fraction(2*N+3)*(1-y*y))
logU=2*(slog+tail)
Aup=(dU-c)/4 + logU/c

def neglog_partial(u,m=10):
    u=Fraction(u)
    return sum(u**k/Fraction(k) for k in range(1,m+1))

def F_upper_at(s,m=10):
    s=Fraction(s)
    Lint=L_interval(s)
    uL=1-Lint.hi
    assert 0<uL<1
    gamma=c*s*s/(2*(1-s*s))
    return Aup-gamma-(alpha/c)*neglog_partial(uL,m)

left=Fraction(58443969,10**8)
right=Fraction(58443970,10**8)
jpL=Jp_interval(left)
jpR=Jp_interval(right)
assert jpL.lo > 0
assert jpR.hi < 0
print("C181 unique maximizer bracket: PASS")
print("  s* in", float(left), float(right))
print("  J'(left) in", jpL.dec())
print("  J'(right) in", jpR.dec())

# C180 analytic proof supplies strict concavity. A concave function lies below
# its tangent at left; because s*<=right:
Fleft=F_upper_at(left,10)
tangent_upper=Fleft + jpL.hi*(right-left)
assert tangent_upper < 0
print("C181 global theorem-objective certificate: PASS")
print("  A_c upper =", float(Aup))
print("  F(left) upper =", float(Fleft))
print("  tangent upper at maximizer =", float(tangent_upper))

alphaL=Fraction(54299,25000)
width=alpha-alphaL
assert width == Fraction(10612411,10**6)
print("Metric movement: PASS")
print("  alpha_L =", float(alphaL))
print("  alpha_U =", float(alpha))
print("  width =", width, "=", float(width))
print("ALL_EXACT_CHECKS_PASS")
