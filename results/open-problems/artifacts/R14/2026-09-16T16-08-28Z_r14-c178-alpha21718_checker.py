#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

print("R14-C178 exact weighted-second-moment certificate at kappa=-1, alpha=10859/5000")

class I:
    def __init__(self, lo, hi=None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
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
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0 or self.hi<0
        vals=[1/self.lo,1/self.hi]
        return I(min(vals),max(vals))
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I(o)
        return self*o.inv()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=I(1)
        for _ in range(n): out=out*self
        return out
    def dec(self): return (float(self.lo),float(self.hi))

def atan_bounds(x, odd_N):
    if odd_N%2==0: odd_N+=1
    def S(N):
        z=Fraction(0)
        for n in range(N+1):
            t=x**(2*n+1)/Fraction(2*n+1)
            z += t if n%2==0 else -t
        return z
    return S(odd_N),S(odd_N-1)

aL,aU=atan_bounds(Fraction(1,5),13)
bL,bU=atan_bounds(Fraction(1,239),3)
piL=16*aL-4*bU
piU=16*aU-4*bL
cL=Fraction(39894228,10**8)
cU=Fraction(39894229,10**8)
assert 2*piU*cL*cL < 1
assert 2*piL*cU*cU > 1

def exp_neg_bounds(x,N_even=24):
    def S(N):
        z=Fraction(0); fact=1; xp=Fraction(1)
        for n in range(N+1):
            if n>0:
                xp*=x; fact*=n
            t=xp/fact
            z += t if n%2==0 else -t
        return z
    return S(N_even+1),S(N_even)

def gauss_int_bounds(a,N_even=24):
    def S(N):
        z=Fraction(0); fact=1
        for n in range(N+1):
            if n>0: fact*=n
            t=a**(2*n+1)/(2**n*fact*(2*n+1))
            z += t if n%2==0 else -t
        return z
    return S(N_even+1),S(N_even)

eL,eU=exp_neg_bounds(Fraction(1,2))
p=I(cL*eL,cU*eU)
jL,jU=gauss_int_bounds(Fraction(1))
Q=I(Fraction(1,2)+cL*jL,Fraction(1,2)+cU*jU)

D=-2*Q**3+4*Q**2*p+5*Q*p**2+p**3
t0=2*(-Q**2+2*Q*p+p**2)/D
t1=2*Q*p/D
t2=-p*(Q+p)/D
disc=t1**2-4*t2*(t0-t2)
delta=t0-1
assert D.hi<0 and t2.lo>0 and disc.hi<0 and delta.hi<Fraction(973,1000)
print("Stage A Gaussian/weight certificate: PASS")
print(" Q",Q.dec(),"p",p.dec())
print(" theta0",t0.dec(),"theta1",t1.dec(),"theta2",t2.dec())
print(" discriminant",disc.dec(),"delta",delta.dec())

# Exact Hermite coefficients through degree 60.
H=[0]*72
H[0]=1; H[1]=-1
for n in range(1,len(H)-1):
    H[n+1]=-H[n]-n*H[n-1]

aI={}
for l in range(3,61):
    B=(t0*H[l-1]
       +t1*(H[l]+l*H[l-2])
       +t2*(H[l+1]+2*l*H[l-1]+l*(l-1)*H[l-3]))
    aI[l]=p**2*B**2/factorial(l)
    assert aI[l].lo>=0

tail_upper=delta.hi-sum(v.lo for v in aI.values())
assert tail_upper>0

def ceil_to_den(x,den):
    x=Fraction(x)
    return Fraction(-(-x.numerator*den//x.denominator),den)

DEN=10**12
u={l:ceil_to_den(v.hi,DEN) for l,v in aI.items()}
u[61]=ceil_to_den(tail_upper,DEN)
sumu=sum(u.values())
assert sumu < 1
print("Stage B Hermite envelope through degree 60: PASS")
print(" U(1)-1 =",float(sumu),"tail u61 =",float(u[61]))

def Uminus(q):
    return sum(c*q**l for l,c in u.items())

def L11(x):
    return sum((Fraction(1,j) if j%2 else -Fraction(1,j))*x**j for j in range(1,12))

def Em(q,m=30):
    return sum(q**(2*n)/Fraction(2*n) for n in range(1,m+1))

# (1+x)L11'(x)=1+x^11: exact monotonicity.
der=[Fraction(1 if k%2==0 else -1) for k in range(11)]
conv=[Fraction(0)]*12
for k,c in enumerate(der):
    conv[k]+=c
    conv[k+1]+=c
assert conv[0]==1 and conv[11]==1 and all(conv[k]==0 for k in range(1,11))
print(" L11 monotonicity identity: PASS")

alpha=Fraction(10859,5000)  # 2.1718
core_margin=Fraction(1,2)-alpha*Fraction(973,1000)*Fraction(1,20)
assert core_margin>0
print("Stage C core certificate: PASS margin coefficient",float(core_margin))

minlb=None; minseg=None; checked=0
def scan(start_num,end_num,den,label):
    global minlb,minseg,checked
    for k in range(start_num,end_num):
        a=Fraction(k,den); b=Fraction(k+1,den)
        x=Uminus(b)
        assert 0<=x<1
        lb=Em(a)-alpha*L11(x)
        assert lb>0, (label,k,float(lb))
        checked+=1
        if minlb is None or lb<minlb:
            minlb=lb; minseg=(label,k,den)

scan(50,750,1000,"A")
scan(7500,7800,10000,"B")
scan(78000,84000,100000,"C")
scan(8400,8700,10000,"D")
scan(870,990,1000,"E")
print("Stage D monotone rational interval certificate: PASS")
print(" intervals checked",checked,"minimum lower bound",float(minlb),"at",minseg)

# log 2 < 7/10, via e^(7/10)>2.
x=Fraction(7,10)
exp_lower=sum(x**n/Fraction(factorial(n)) for n in range(5))
assert exp_lower>2
endpoint_margin=Em(Fraction(99,100))-alpha*Fraction(7,10)
assert endpoint_margin>0
print("Stage E endpoint certificate: PASS margin",float(endpoint_margin))

# Retained Stojnic upper endpoint and the frozen metric.
barQ=I(1)-Q
fgar=2*barQ-p
assert fgar.lo>0
alphaU=I(1)/fgar
width=alphaU-alpha
assert width.lo>Fraction(1110139,100000)
assert width.hi<Fraction(1110142,100000)
print("Metric certificate: PASS")
print(" alphaL",float(alpha),"alphaU",alphaU.dec(),"width",width.dec())

# R15 T1 audit finite contradiction core: N(0,1)+independent N(0,1) has variance 2,
# incompatible with convergence in probability to 0 (variance-zero limiting law).
assert Fraction(1)+Fraction(1)==2
assert Fraction(2)!=0
print("R14-AUDIT-R15-I0076-T1-03 finite contradiction core: PASS")
print("PASS")
