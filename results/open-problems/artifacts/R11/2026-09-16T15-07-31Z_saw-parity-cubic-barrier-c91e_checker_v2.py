#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

print("R11 exact self-check: parity-accelerated DCH unfolding + cubic barrier + R14 audit")

# ---------- DCH bridge utilities ----------
def add(a,b): return (a[0]+b[0], a[1]+b[1])

def is_bridge(p):
    ys=[z[1] for z in p]
    return all(y>ys[0] for y in ys[1:]) and ys[-1]==max(ys)

def zigzags(p):
    n=len(p)-1
    ys=[q[1] for q in p]
    out=[]
    for j in range(1,n+1):
        M=max(ys[1:j+1])
        i=max(k for k in range(1,j+1) if ys[k]==M)
        m=min(ys[i:])
        jj=max(k for k in range(i,n+1) if ys[k]==m)
        if jj==j:
            out.append((i,j))
    return tuple(out)

def reflect_h(q,h):
    return (q[0],2*h-q[1])

def unfold_one(p,z):
    i,j=z
    pref=list(p[:i+1])
    cen=[reflect_h(q,p[i][1]) for q in p[i:j+1]]
    out=pref+cen[1:]
    dx=cen[-1][0]-p[j][0]
    dy=cen[-1][1]-p[j][1]
    out += [(q[0]+dx,q[1]+dy) for q in p[j+1:]]
    return tuple(out)

def unfold_all(p):
    zs=zigzags(p)
    q=p
    for z in zs:
        q=unfold_one(q,z)
    return q

def crossings(p):
    cc={}
    for a,b in zip(p,p[1:]):
        if a[1]!=b[1]:
            h=min(a[1],b[1])
            cc[h]=cc.get(h,0)+1
    return cc

# R11-GH-X003: exact 10-step bridge, max crossing 5 -> 3 after one full unfold.
p=((0,0),(0,1),(0,2),(1,2),(1,1),(2,1),(2,2),(3,2),(3,1),(4,1),(4,2))
assert is_bridge(p)
q=unfold_all(p)
assert is_bridge(q)
cp=crossings(p); cq=crossings(q)
assert max(cp.values())==5
assert max(cq.values())==3
assert zigzags(p)==((7,9),(10,10))
assert zigzags(q)==((3,5),(7,7),(9,9),(10,10))
print("X003 exact bridge: PASS; max crossing 5 -> 3")

# Parity identity finite sanity on the explicit source/output.
# For each level below endpoint height, #up - #down = 1, hence total crossings odd.
def parity_certificate(p):
    ymax=p[-1][1]
    for h in range(0,ymax):
        up=down=0
        for a,b in zip(p,p[1:]):
            if a[1]==h and b[1]==h+1: up+=1
            elif a[1]==h+1 and b[1]==h: down+=1
        assert up-down==1
        assert (up+down)%2==1
parity_certificate(p); parity_certificate(q)
print("C005 crossing-parity certificate: PASS")

# R11-GH-C006: optimized current-MultiUnf parameters.
count=0
for den in range(2,401):
    for num in range(1,den):
        if gcd(num,den)!=1: continue
        z=Fraction(num,den)
        if z>Fraction(1,8): continue
        # L = ceil(3/(4z)) = ceil(3 den/(4 num))
        L=(3*den + 4*num - 1)//(4*num)
        a=2*z-Fraction(1,L)
        assert a>0
        d=a/Fraction(2+2*L+12*L*L,1)
        r=d; s=2*d
        # DCH reconstruction ratio is exactly 2.
        ratio=(a-s)/((r+3*L*s)*L)
        assert ratio==2
        assert s<=a
        # Uniform explicit lower bound for z<=1/8.
        assert d>=z**3/Fraction(15,1)
        count+=1
print("C006 optimized parameters: PASS on",count,"reduced rational z values")

# R11-GH-X004 exact cubic barrier algebra for the present worst-case certificate.
# Here a0=2z-1/L is the lower bound on short-zigzag density supplied
# by the coarse disjoint-length estimate used in this compiler.
# For x=zL>1/2,
# (2 - 1/x)/(12x^2) <= 8/81 iff
# 32 x^3 - 54 x + 27 = (2x+3)(4x-3)^2 >=0.
for den in range(2,401):
    for num in range(1,den):
        x=Fraction(num,den)
        if x<=Fraction(1,2): continue
        lhs=32*x**3-54*x+27
        rhs=(2*x+3)*(4*x-3)**2
        assert lhs==rhs and lhs>=0
print("X004 cubic-barrier factorization: PASS")

# Polynomial-vs-double-exponential class survives parity acceleration.
# A Case-2 pass lowers k by 2 for k>=3, while SAB^2=SAB^1 by parity.
# Thus the exact worst-case number of Case-2 passes from cap k0 is floor((k0-1)/2).
for k0 in range(2,60):
    stages=(k0-1)//2
    remaining=k0-2*stages
    assert remaining in (1,2)
    assert stages==0 if k0==2 else stages>=1
    # For large k0 this is still Theta(k0), hence 3^stages is exponential in k0.
    if k0>=5:
        assert stages>= (k0-2)//2
print("Parity acceleration exact stage-count arithmetic: PASS")

# ---------- Independent exact R14-C175 audit ----------
# Recompute f(-1)=2 Q(1)-phi(1) with independent rational interval arithmetic.
class Intv:
    def __init__(self,lo,hi=None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=o if isinstance(o,Intv) else Intv(o)
        return Intv(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return Intv(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-(o if isinstance(o,Intv) else Intv(o)))
    def __mul__(self,o):
        o=o if isinstance(o,Intv) else Intv(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return Intv(min(vals),max(vals))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0
        return Intv(1/self.hi,1/self.lo)

# Machin pi = 16 atan(1/5)-4 atan(1/239).
def atan_alt_bounds(x,N_even_terms=16):
    # S_N with terms n=0..N. Even N gives upper, odd N lower.
    def S(N):
        s=Fraction(0)
        for n in range(N+1):
            term=x**(2*n+1)/Fraction(2*n+1)
            s += term if n%2==0 else -term
        return s
    return S(N_even_terms+1), S(N_even_terms)

aL,aU=atan_alt_bounds(Fraction(1,5),16)
bL,bU=atan_alt_bounds(Fraction(1,239),4)
piL=16*aL-4*bU
piU=16*aU-4*bL

# Independently certify c=(2pi)^(-1/2) using decimal rationals and squaring.
cL=Fraction(398942280,10**9)
cU=Fraction(398942281,10**9)
assert 2*piU*cL*cL < 1
assert 2*piL*cU*cU > 1
c=Intv(cL,cU)

# Alternating exp(-1/2).
def expm_bounds(N=30):
    x=Fraction(1,2)
    def S(N):
        s=Fraction(0); term=Fraction(1)
        for n in range(N+1):
            if n:
                term *= x/Fraction(n)
            s += term if n%2==0 else -term
        return s
    return S(N+1),S(N)
eL,eU=expm_bounds(30)
phi=c*Intv(eL,eU)

# J=int_0^1 exp(-t^2/2)dt alternating integrated series.
def J_bounds(N=30):
    def S(N):
        s=Fraction(0); fact=1
        for n in range(N+1):
            if n: fact*=n
            term=Fraction(1, 2**n*fact*(2*n+1))
            s += term if n%2==0 else -term
        return s
    return S(N+1),S(N)
jL,jU=J_bounds(30)
Q=Intv(Fraction(1,2))-c*Intv(jL,jU)
f=2*Q-phi
assert f.lo>0
alpha=f.inv()
width=alpha-Intv(2)
assert alpha.lo>Fraction(13273,1000)
assert alpha.hi<Fraction(13274,1000)
assert width.lo>Fraction(11273,1000)
assert width.hi<Fraction(11274,1000)
print("R14-C175 independent exact audit: PASS")
print("  alpha_U interval:", float(alpha.lo), float(alpha.hi))
print("  width interval:", float(width.lo), float(width.hi))
print("PASS")
