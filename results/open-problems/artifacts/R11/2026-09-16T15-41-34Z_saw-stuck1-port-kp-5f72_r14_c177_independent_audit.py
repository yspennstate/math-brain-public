#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
import sympy as sp

print("R11 independent exact audit of R14-C177")

# ---- symbolic moment-normalization identity ----
Q,p=sp.symbols("Q p", nonzero=True)
D=-2*Q**3+4*Q**2*p+5*Q*p**2+p**3
theta=sp.Matrix([
    2*(-Q**2+2*Q*p+p**2)/D,
    2*Q*p/D,
    -p*(Q+p)/D,
])
# For h=(1,z,z^2-1) on {z>=-1}, exact Gaussian integration gives:
M=sp.Matrix([
    [Q,       p,      -p],
    [p,     Q-p,     2*p],
    [-p,    2*p, 2*Q-2*p],
])
res=[sp.factor(x) for x in (M*theta-sp.Matrix([1,0,0]))]
assert res==[0,0,0]
print("symbolic moment constraints: PASS")

# ---- exact rational interval machinery ----
class I:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
        assert self.lo<=self.hi
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
        vals=[1/self.lo,1/self.hi]
        return I(min(vals),max(vals))
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I(o); return self*o.inv()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        ans=I(1); base=self
        while n:
            if n&1: ans=ans*base
            base=base*base; n//=2
        return ans

def atan_bounds(x,N_even):
    # alternating Taylor: odd truncation is lower, even truncation upper
    if N_even%2: N_even+=1
    def S(N):
        s=Fraction()
        for n in range(N+1):
            t=x**(2*n+1)/Fraction(2*n+1)
            s += t if n%2==0 else -t
        return s
    return S(N_even+1),S(N_even)

# Machin pi = 16 atan(1/5)-4 atan(1/239)
aL,aU=atan_bounds(Fraction(1,5),16)
bL,bU=atan_bounds(Fraction(1,239),4)
piL,piU=16*aL-4*bU,16*aU-4*bL

# Independent decimal rationals bracketing 1/sqrt(2*pi), verified by squaring.
cL=Fraction(3989422804,10**10)
cU=Fraction(3989422805,10**10)
assert 2*piU*cL*cL < 1 < 2*piL*cU*cU

def exp_neg_bounds(x,N_even=30):
    def S(N):
        s=Fraction(); term=Fraction(1)
        for n in range(N+1):
            if n: term=term*x/n
            s += term if n%2==0 else -term
        return s
    return S(N_even+1),S(N_even)

def gaussian_integral_0_1_bounds(N_even=30):
    # integral_0^1 exp(-x^2/2) dx
    def S(N):
        return sum((Fraction(1,2**n*factorial(n)*(2*n+1)) if n%2==0
                    else -Fraction(1,2**n*factorial(n)*(2*n+1)))
                   for n in range(N+1))
    return S(N_even+1),S(N_even)

eL,eU=exp_neg_bounds(Fraction(1,2))
jL,jU=gaussian_integral_0_1_bounds()
P=I(cL*eL,cU*eU) # phi(1)
QQ=I(Fraction(1,2)+cL*jL,Fraction(1,2)+cU*jU) # Phi(1)

DD=-2*QQ**3+4*QQ**2*P+5*QQ*P**2+P**3
t0=2*(-QQ**2+2*QQ*P+P**2)/DD
t1=2*QQ*P/DD
t2=-P*(QQ+P)/DD
disc=t1**2-4*t2*(t0-t2)
delta=t0-1
assert DD.hi<0 and t2.lo>0 and disc.hi<0
assert delta.hi < Fraction(973,1000)
print("positive feasible weight + delta<0.973: PASS")

# ---- independent Hermite envelope through degree 40 ----
H=[0]*64
H[0]=1; H[1]=-1
for n in range(1,len(H)-1):
    H[n+1]=-H[n]-n*H[n-1]

aI={}
for ell in range(3,41):
    B=(t0*H[ell-1]
       +t1*(H[ell]+ell*H[ell-2])
       +t2*(H[ell+1]+2*ell*H[ell-1]+ell*(ell-1)*H[ell-3]))
    ai=P**2*B**2/factorial(ell)
    assert ai.lo>=0
    aI[ell]=ai

tail_upper=delta.hi-sum(v.lo for v in aI.values())
assert tail_upper>0
DEN=10**13
def ceil_den(x):
    x=Fraction(x)
    return Fraction(-(-x.numerator*DEN//x.denominator),DEN)
u={ell:ceil_den(v.hi) for ell,v in aI.items()}
u[41]=ceil_den(tail_upper)
assert sum(u.values())<1
print("degree-40 Hermite majorant + tail at degree 41: PASS")

coeff=[Fraction(0)]*42
for ell,val in u.items(): coeff[ell]=val
def Uminus(q):
    s=coeff[41]
    for ell in range(40,2,-1):
        s=s*q+coeff[ell]
    return s*q**3
def L7(x):
    s=Fraction(); xp=x
    for j in range(1,8):
        s += (Fraction(1,j) if j%2 else -Fraction(1,j))*xp
        xp*=x
    return s
def Em(q,m):
    q2=q*q; xp=q2; s=Fraction()
    for n in range(1,m+1):
        s+=xp/Fraction(2*n); xp*=q2
    return s

alpha=Fraction(271,125)

# core 0<q<=1/20
core=Fraction(1,2)-alpha*Fraction(973,1000)*Fraction(1,20)
assert core>0
print("core rate margin: PASS",float(core))

# Independent mesh: different from R14's 3220-cell mesh.
# [0.05,.70] mesh 1/2000; [.70,.90] mesh 1/50000; [.90,.99] mesh 1/2000.
minlb=None; mincell=None; checked=0
def scan(start,end,den,label):
    global minlb,mincell,checked
    for k in range(start,end):
        a=Fraction(k,den); b=Fraction(k+1,den)
        x=Uminus(b)
        assert 0<=x<1
        lb=Em(a,12)-alpha*L7(x)
        assert lb>0,(label,k,float(lb))
        checked+=1
        if minlb is None or lb<minlb:
            minlb=lb; mincell=(label,k,den)
scan(100,1400,2000,"A")
scan(35000,45000,50000,"B")
scan(1800,1980,2000,"C")
print("independent middle mesh: PASS",checked,"cells",
      "min",float(minlb),"at",mincell)

# endpoint q>=.99: log 2 < .7 and -1/2 log(1-q^2) >= E20(.99)
x=Fraction(7,10)
exp_lower=sum(x**n/Fraction(factorial(n)) for n in range(5))
assert exp_lower>2
endpoint=Em(Fraction(99,100),20)-alpha*Fraction(7,10)
assert endpoint>0
print("endpoint rate margin: PASS",float(endpoint))

print("R11-AUDIT-R14-C177-20260916 = PASS")
print("PASS")
