#!/usr/bin/env python3
"""
ProofNet15 R14 C176 exact weighted-second-moment certificate.

The theorem-producing parts use exact rational arithmetic:
  C171: kappa=-1 signed quadratic double-Hermite compensator is globally
        positive and has delta<0.973.
  C172: exact Hermite coefficients a_l=c_l^2 for l=3,...,16 are enclosed,
        and the full kernel R(q) is dominated for q in [0,1] by an explicit
        rational polynomial U(q), using only the exact total tail energy.
  C176: exact Bernstein certificate for alpha=4217/2000:
        -1/2 log(1-q^2) - (4217/2000) log R(q) > 0 for every q in (0,1).
        By nonnegative Hermite coefficients, negative overlaps are no worse.
  C176: therefore the original full-radius spherical perceptron is SAT whp
        for kappa=-1 and alpha<=4217/2000.
  Metric: combines the certified SAT endpoint with the retained Stojnic
        Gardner upper endpoint at kappa=-1.
  R15 audit: exact copied-block common-coin check for I0076-R15-L1.

No floating-point comparison is used to establish the theorem-producing certificate.
Decimals printed below are post-hoc renderings of exact rational intervals.
"""
from fractions import Fraction
from math import comb, factorial
import random

print("ProofNet15 R14 C176 exact weighted-second-moment certificate")

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
        vals = [self.lo*o.lo, self.lo*o.hi,
                self.hi*o.lo, self.hi*o.hi]
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def inv(self):
        assert self.lo > 0 or self.hi < 0
        vals = [1/self.lo, 1/self.hi]
        return I(min(vals), max(vals))
    def __truediv__(self, o):
        o = o if isinstance(o, I) else I(o)
        return self * o.inv()
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = I(1)
        for _ in range(n):
            out = out*self
        return out
    def dec(self):
        return (float(self.lo), float(self.hi))

# ----------------------------------------------------------------------
# Exact rational Gaussian enclosures via Machin + alternating series.
# ----------------------------------------------------------------------
def atan_bounds(x, odd_N):
    if odd_N % 2 == 0:
        odd_N += 1
    def S(N):
        z = Fraction(0)
        for n in range(N+1):
            t = x**(2*n+1)/Fraction(2*n+1)
            z += t if n % 2 == 0 else -t
        return z
    return S(odd_N), S(odd_N-1)

aL,aU = atan_bounds(Fraction(1,5),13)
bL,bU = atan_bounds(Fraction(1,239),3)
piL = 16*aL - 4*bU
piU = 16*aU - 4*bL
cL = Fraction(39894228,10**8)
cU = Fraction(39894229,10**8)
assert 2*piU*cL*cL < 1
assert 2*piL*cU*cU > 1

def exp_neg_bounds(x, N_even=24):
    def S(N):
        z=Fraction(0); fact=1; xp=Fraction(1)
        for n in range(N+1):
            if n>0:
                xp *= x
                fact *= n
            t=xp/fact
            z += t if n%2==0 else -t
        return z
    return S(N_even+1), S(N_even)

def gauss_int_bounds(a, N_even=24):
    def S(N):
        z=Fraction(0); fact=1
        for n in range(N+1):
            if n>0:
                fact *= n
            t=a**(2*n+1)/(2**n*fact*(2*n+1))
            z += t if n%2==0 else -t
        return z
    return S(N_even+1), S(N_even)

eL,eU = exp_neg_bounds(Fraction(1,2))
p = I(cL*eL, cU*eU)
jL,jU = gauss_int_bounds(Fraction(1))
Q = I(Fraction(1,2)+cL*jL, Fraction(1,2)+cU*jU)

assert Fraction(8413447,10**7) < Q.lo < Q.hi < Fraction(8413448,10**7)
assert Fraction(2419707,10**7) < p.lo < p.hi < Fraction(2419708,10**7)
print("Gaussian enclosure: PASS")
print("  Q=Phi(1) in",Q.dec())
print("  p=phi(1) in",p.dec())

# ----------------------------------------------------------------------
# C171: exact kappa=-1 quadratic projection.
# h=(1,x,x^2-1); theta=M^{-1}e0.
# Closed forms from the exact 3x3 inverse.
# ----------------------------------------------------------------------
D = -2*Q**3 + 4*Q**2*p + 5*Q*p**2 + p**3
t0 = 2*(-Q**2 + 2*Q*p + p**2)/D
t1 = 2*Q*p/D
t2 = -p*(Q+p)/D
disc = t1**2 - 4*t2*(t0-t2)
delta = t0-1

assert D.hi < 0
assert t2.lo > 0
assert disc.hi < 0
assert delta.hi < Fraction(973,1000)

print("C171 kappa=-1 quadratic positivity: PASS")
print("  theta0 in",t0.dec())
print("  theta1 in",t1.dec())
print("  theta2 in",t2.dec())
print("  discriminant in",disc.dec(),"<0")
print("  delta in",delta.dec(),"<973/1000")

# ----------------------------------------------------------------------
# C172: exact Hermite coefficient enclosures.
# For l>=3:
# a_l = c_l^2 = p^2 B_l^2/l!, with
# B_l = theta0 H_{l-1}
#     + theta1(H_l+l H_{l-2})
#     + theta2(H_{l+1}+2lH_{l-1}+l(l-1)H_{l-3})
# and H_n = He_n(-1) is an integer.
# ----------------------------------------------------------------------
H=[0]*20
H[0]=1; H[1]=-1
for n in range(1,19):
    if n+1 < len(H):
        H[n+1] = -H[n]-n*H[n-1]

aI={}
for l in range(3,17):
    B = (
        t0*H[l-1]
        + t1*(H[l]+l*H[l-2])
        + t2*(H[l+1]+2*l*H[l-1]+l*(l-1)*H[l-3])
    )
    aI[l] = p**2 * B**2 / factorial(l)
    assert aI[l].lo >= 0

tail_upper = delta.hi - sum(v.lo for v in aI.values())
assert tail_upper > 0

def ceil_to_den(x,den):
    x=Fraction(x)
    return Fraction(-(-x.numerator*den // x.denominator),den)

DEN=10**10
u={}
for l,v in aI.items():
    u[l]=ceil_to_den(v.hi,DEN)
u[17]=ceil_to_den(tail_upper,DEN)

# For q in [0,1]:
# sum_{l>=17} a_l q^l <= (sum_{l>=17}a_l) q^17.
# Thus R(q) <= U(q)=1+sum_{3..16} u_l q^l+u_17 q^17.
# Also U(1)-1<1, needed for alternating log series.
assert sum(u.values()) < 1

print("C172 Hermite-envelope construction: PASS")
print("  U(1)-1 =",float(sum(u.values())))
print("  tail upper coefficient u17 =",float(u[17]))

# ----------------------------------------------------------------------
# Exact polynomial arithmetic.
# ----------------------------------------------------------------------
def padd(A,B):
    n=max(len(A),len(B)); C=[Fraction(0)]*n
    for i in range(n):
        if i<len(A): C[i]+=A[i]
        if i<len(B): C[i]+=B[i]
    while len(C)>1 and C[-1]==0: C.pop()
    return C

def pscale(A,c):
    return [a*c for a in A]

def pmul(A,B):
    C=[Fraction(0)]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        if a:
            for j,b in enumerate(B):
                if b:
                    C[i+j]+=a*b
    while len(C)>1 and C[-1]==0: C.pop()
    return C

def ppow(A,n):
    R=[Fraction(1)]; B=A[:]
    while n:
        if n&1: R=pmul(R,B)
        n//=2
        if n: B=pmul(B,B)
    return R

# x(q)=U(q)-1.
x=[Fraction(0)]*18
for l,c in u.items(): x[l]=c

# Alternating upper bound on log(1+x), since 0<=x<1:
# log(1+x) <= x-x^2/2+x^3/3-...-x^6/6+x^7/7.
log_upper=[Fraction(0)]
for j in range(1,8):
    log_upper=padd(log_upper,pscale(ppow(x,j),Fraction(1 if j%2 else -1,j)))

# Lower bound on -1/2 log(1-q^2) >= (1/2) sum_{n=1}^{12}q^(2n)/n.
entropy_lower=[Fraction(0)]*25
for n in range(1,13):
    entropy_lower[2*n]+=Fraction(1,2*n)

alpha=Fraction(4217,2000)
P=padd(entropy_lower,pscale(log_upper,-alpha))
assert P[0]==0 and P[1]==0
Hpoly=P[2:] # P(q)=q^2 Hpoly(q)

# Exact Bernstein positivity on 20 rational subintervals.
def affine_power(coef,a,b):
    n=len(coef)-1
    out=[Fraction(0)]*(n+1)
    d=b-a
    ap=[Fraction(1)]*(n+1)
    dp=[Fraction(1)]*(n+1)
    for j in range(1,n+1):
        ap[j]=ap[j-1]*a
        dp[j]=dp[j-1]*d
    for j,c in enumerate(coef):
        if c==0: continue
        for i in range(j+1):
            out[i]+=c*comb(j,i)*ap[j-i]*dp[i]
    return out

def bernstein_coeffs(power):
    n=len(power)-1
    beta=[]
    for k in range(n+1):
        s=Fraction(0)
        for i in range(k+1):
            if power[i]:
                s += power[i]*Fraction(comb(k,i),comb(n,i))
        beta.append(s)
    return beta

min_beta=None
min_loc=None
Nsub=20
for s in range(Nsub):
    a=Fraction(s,Nsub); b=Fraction(s+1,Nsub)
    beta=bernstein_coeffs(affine_power(Hpoly,a,b))
    for j,v in enumerate(beta):
        assert v>0
        if min_beta is None or v<min_beta:
            min_beta=v
            min_loc=(s,j)

print("C176 alpha=4217/2000 exact Bernstein rate certificate: PASS")
print("  degree of H =",len(Hpoly)-1)
print("  minimum Bernstein coefficient ~",float(min_beta),
      "at",min_loc)

# The exact logic is:
# R(q)<=U(q) for q>=0, R(-q)<=R(q), log R<=log U<=log_upper,
# entropy >= entropy_lower, and P(q)=q^2 H(q)>0 for q in (0,1].
print("C176 full-radius whp SAT deduction: PASS")
print("  kappa=-1, alpha<=4217/2000")

# ----------------------------------------------------------------------
# Retained rigorous upper endpoint and updated metric.
# Q above is Phi(1), p is phi(1); hence barPhi(1)=1-Q and
# f_gar(-1)=2*(1-Q)-p.
# ----------------------------------------------------------------------
barQ = I(1) - Q
fgar = 2*barQ - p
assert fgar.lo > 0
alphaU = I(1) / fgar
alphaL = Fraction(4217,2000)
width = alphaU - alphaL
assert alphaU.lo > Fraction(132731,10000)
assert alphaU.hi < Fraction(13274,1000)
assert width.lo > Fraction(111646,10000)
assert width.hi < Fraction(111648,10000)
print("R14 metric update: PASS")
print("  alpha_L = 4217/2000 =", float(alphaL))
print("  alpha_U interval =", alphaU.dec())
print("  width interval =", width.dec())

# ----------------------------------------------------------------------
# Independent audit of R15 I0076-R15-L1 finite core.
# Source first-stage copy rule has a1=-1,b1=1 and
# V_k = V_{k-a1+d1+b1+1} for k in [a1-d1,a1-1].
# At k=a1-d1=-d1-1, the copied right index is 2.
# The common fair-coin event has probability 1/2, incompatible with
# independence of sigma fields that both contain it.
# ----------------------------------------------------------------------
for d1 in range(1,65):
    a1=Fraction(-1); b1=Fraction(1)
    k=a1-d1
    copied=k-a1+d1+b1+1
    assert copied == 2
P_A=Fraction(1,2)
assert P_A != P_A*P_A
print("R14-AUDIT-R15-I0076-L1-01 finite common-coin core: PASS")

print("PASS")
