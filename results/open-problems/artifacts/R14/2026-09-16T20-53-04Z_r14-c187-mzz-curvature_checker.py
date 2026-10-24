#!/usr/bin/env python3
from fractions import Fraction

print("R14-C187 exact curvature obstruction for MZZ second-moment lower bound at kappa=-1")

class I:
    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, o):
        return self + (-(o if isinstance(o, I) else I(o)))
    def __rsub__(self, o):
        return I(o) - self
    def __mul__(self, o):
        o = o if isinstance(o, I) else I(o)
        vals = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def inv(self):
        assert self.lo > 0 or self.hi < 0
        vals = [1/self.lo, 1/self.hi]
        return I(min(vals), max(vals))
    def __truediv__(self, o):
        return self * (o if isinstance(o, I) else I(o)).inv()
    def dec(self):
        return float(self.lo), float(self.hi)

def atan_bounds(x, odd_N):
    x = Fraction(x)
    if odd_N % 2 == 0:
        odd_N += 1
    def S(N):
        z = Fraction(0)
        for n in range(N+1):
            t = x**(2*n+1) / Fraction(2*n+1)
            z += t if n % 2 == 0 else -t
        return z
    return S(odd_N), S(odd_N-1)

aL,aU = atan_bounds(Fraction(1,5), 17)
bL,bU = atan_bounds(Fraction(1,239), 5)
piL = 16*aL - 4*bU
piU = 16*aU - 4*bL

c0L = Fraction(398942280401432, 10**15)
c0U = Fraction(398942280401433, 10**15)
assert 2*piU*c0L*c0L < 1
assert 2*piL*c0U*c0U > 1
print("Gaussian normalization enclosure: PASS")

def exp_neg_bounds(x, N_even=28):
    x = Fraction(x)
    def S(N):
        z=Fraction(0); xp=Fraction(1); fact=1
        for n in range(N+1):
            if n:
                xp *= x
                fact *= n
            t = xp/fact
            z += t if n%2==0 else -t
        return z
    return S(N_even+1), S(N_even)

def gauss_int_bounds(a, N_even=28):
    a = Fraction(a)
    def S(N):
        z=Fraction(0); fact=1
        for n in range(N+1):
            if n:
                fact *= n
            t = a**(2*n+1) / (2**n * fact * (2*n+1))
            z += t if n%2==0 else -t
        return z
    return S(N_even+1), S(N_even)

def Phi_pos_interval(a):
    jL,jU = gauss_int_bounds(a)
    return I(Fraction(1,2)+c0L*jL, Fraction(1,2)+c0U*jU)

def phi_interval(a):
    x = a*a/Fraction(2)
    eL,eU = exp_neg_bounds(x)
    return I(c0L*eL,c0U*eU)

def root_function_interval(c):
    c = Fraction(c)
    a = 1-c
    return c*Phi_pos_interval(a) - phi_interval(a)

cL = Fraction(5189,10000)
cU = Fraction(5190,10000)
FL = root_function_interval(cL)
FU = root_function_interval(cU)
assert FL.hi < 0
assert FU.lo > 0
print("MZZ c* root bracket: PASS")
print("  F(0.5189) in", FL.dec())
print("  F(0.5190) in", FU.dec())
print("  using MZZ uniqueness: 0.5189 < c* < 0.5190")

curv_ceil = Fraction(1,1)/(cL*cL)
assert curv_ceil < Fraction(3714,1000)
print("Curvature ceiling: PASS")
print("  1/(0.5189)^2 =", float(curv_ceil), "< 3.714")

jL,jU = gauss_int_bounds(Fraction(1))
Phi_minus1 = I(Fraction(1,2)-c0U*jU, Fraction(1,2)-c0L*jL)
assert Phi_minus1.hi < Fraction(1,4)
print("MZZ LP lower bound comparison: PASS")
print("  Phi(-1) in", Phi_minus1.dec(), "< 1/4")
print("  therefore delta_lin(-1)=1/Phi(-1) > 4 > 3.714 > delta_lb(-1)")

alpha_L = Fraction(630297437506, 10**11)
alpha_U = Fraction(1278437096216, 10**11)
width = alpha_U-alpha_L
assert width == Fraction(64813965871, 10**10)
print("Metric unchanged: PASS")
print("  alpha_L =", float(alpha_L))
print("  alpha_U =", float(alpha_U))
print("  width =", width, "=", float(width))

print("ALL_EXACT_CHECKS_PASS")
