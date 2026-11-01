#!/usr/bin/env python3
from fractions import Fraction

print("R14-C182/C183 exact partial-lift extremal certificate, kappa=-1")

class I:
    def __init__(self, lo, hi=None):
        self.lo=Fraction(lo)
        self.hi=Fraction(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-(o if isinstance(o,I) else I(o)))
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
    def __truediv__(self,o): return self*(o if isinstance(o,I) else I(o)).inv()
    def sq(self):
        if self.lo>=0: return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0: return I(self.hi*self.hi,self.lo*self.lo)
        return I(0,max(self.lo*self.lo,self.hi*self.hi))
    def dec(self): return float(self.lo),float(self.hi)

# ---------- exact transcendental enclosures ----------
def atan_bounds(x, odd_N=25):
    if odd_N%2==0: odd_N+=1
    def S(N):
        z=Fraction(0)
        for n in range(N+1):
            t=x**(2*n+1)/Fraction(2*n+1)
            z += t if n%2==0 else -t
        return z
    return S(odd_N),S(odd_N-1)

aL,aU=atan_bounds(Fraction(1,5),25)
bL,bU=atan_bounds(Fraction(1,239),7)
piL=16*aL-4*bU
piU=16*aU-4*bL
c0L=Fraction(39894228040143267793,10**20)
c0U=Fraction(39894228040143267795,10**20)
assert 2*piU*c0L*c0L < 1
assert 2*piL*c0U*c0U > 1
print("Gaussian normalization enclosure: PASS")

def exp_neg_bounds(x,N_even=32):
    x=Fraction(x)
    def S(N):
        z=Fraction(0);xp=Fraction(1);fact=1
        for n in range(N+1):
            if n:
                xp*=x; fact*=n
            t=xp/fact
            z += t if n%2==0 else -t
        return z
    return S(N_even+1),S(N_even)

def gauss_int_bounds(a,N_even=32):
    a=Fraction(a)
    def S(N):
        z=Fraction(0);fact=1
        for n in range(N+1):
            if n: fact*=n
            t=a**(2*n+1)/(2**n*fact*(2*n+1))
            z += t if n%2==0 else -t
        return z
    return S(N_even+1),S(N_even)

def qbar_pt(s):
    iL,iU=gauss_int_bounds(s)
    return I(Fraction(1,2)-c0U*iU, Fraction(1,2)-c0L*iL)

def exph_pt(s):
    x=(1-Fraction(s)**2)/2
    eL,eU=exp_neg_bounds(x)
    return I(eL,eU)

e1L,e1U=exp_neg_bounds(Fraction(1,2))
phi1=I(c0L*e1L,c0U*e1U)
Q1=qbar_pt(Fraction(1))
Phi1=I(1)-Q1

def point_L_Lp(s):
    s=Fraction(s)
    E=exph_pt(s); qb=qbar_pt(s)
    L=Phi1+s*E*qb
    Lp=E*(1+s*s)*qb-s*phi1
    return L,Lp

def log_rat_bounds(x,N=20):
    x=Fraction(x)
    assert x>0
    y=(x-1)/(x+1)
    ay=abs(y)
    S=Fraction(0)
    for n in range(N+1):
        S += y**(2*n+1)/Fraction(2*n+1)
    tail=ay**(2*N+3)/(Fraction(2*N+3)*(1-ay*ay))
    if y>=0:
        return 2*S,2*(S+tail)
    return 2*(S-tail),2*S

def log_iv(X,N=20):
    loL,_=log_rat_bounds(X.lo,N)
    _,hiU=log_rat_bounds(X.hi,N)
    return I(loL,hiU)

# ---------- C182 saddle identities are proved algebraically in the report ----------
# Finite core here checks the nontrivial exact arithmetic/certification steps.
print("C182 stationary algebra: WRITTEN-PROOF-ONLY")

# ---------- exact compact scan proving k(s)=s ell'(s) is unimodal ----------
# Fast lower-degree exact enclosures are ample for the compact K' sign scan.
from functools import lru_cache
@lru_cache(maxsize=None)
def qbar_scan(s):
    iL,iU=gauss_int_bounds(s,N_even=12)
    return I(Fraction(1,2)-c0U*iU, Fraction(1,2)-c0L*iL)
@lru_cache(maxsize=None)
def exph_scan(s):
    x=(1-Fraction(s)**2)/2
    eL,eU=exp_neg_bounds(x,N_even=12)
    return I(eL,eU)

# K=L^2 k'.  We show K'<0 on [0,1] by an exact rational cover.
def cell_quant(a,b):
    a=Fraction(a); b=Fraction(b); S=I(a,b)
    # exp(-(1-s^2)/2) increases, Qbar(s) decreases on [0,1]
    E=I(exph_scan(a).lo,exph_scan(b).hi)
    QB=I(qbar_scan(b).lo,qbar_scan(a).hi)
    EQ=E*QB
    L=Phi1+S*EQ
    Lp=E*(I(1)+S*S)*QB-S*phi1
    Lpp=S*(I(3)+S*S)*EQ-(I(2)+S*S)*phi1
    Lppp=(I(3)+I(6)*S*S+(S*S).sq())*EQ-S*(I(5)+S*S)*phi1
    K=L*Lp+S*L*Lpp-S*Lp.sq()
    Kp=I(2)*L*Lpp+S*L*Lppp-S*Lp*Lpp
    return K,Kp

largest_Kp_upper=None
scan_cells=[]
for j in range(89):
    scan_cells.append((Fraction(j,100),Fraction(j+1,100)))
for j in range(890,1000):
    scan_cells.append((Fraction(j,1000),Fraction(j+1,1000)))
for idx,(a,b) in enumerate(scan_cells):
    K,Kp=cell_quant(a,b)
    assert Kp.hi<0, (idx,float(a),float(b),float(Kp.lo),float(Kp.hi))
    if largest_Kp_upper is None or Kp.hi>largest_Kp_upper:
        largest_Kp_upper=Kp.hi
K0,_=cell_quant(Fraction(0),Fraction(0))
K1,_=cell_quant(Fraction(1),Fraction(1))
assert K0.lo>0 and K1.hi<0
print("C182 k-unimodality finite core: PASS")
print("  max cell upper bound for K' =",float(largest_Kp_upper))
print("  K(0) in",K0.dec(),"K(1) in",K1.dec())

# ---------- unique h-max root and alpha_* interval ----------
# g=ell-s log(s) ell'; g=0 iff h=ell/log(s) has stationary point.
def g_iv(s):
    s=Fraction(s)
    L,Lp=point_L_Lp(s)
    ellI=log_iv(L,20)
    logs=I(*log_rat_bounds(s,20))
    ep=Lp/L
    return ellI-s*logs*ep

left=Fraction(58444642236,10**11)
right=Fraction(58444642238,10**11)
gL=g_iv(left); gR=g_iv(right)
assert gL.hi<0
assert gR.lo>0

# s_* lies below the unique k-maximum because K(0.7)>0 exactly.
K07,_=cell_quant(Fraction(7,10),Fraction(7,10))
assert K07.lo>0

# Since k is increasing at s_*, alpha_*=1/k(s_*) is bracketed by endpoints.
Ll,Lpl=point_L_Lp(left)
Lr,Lpr=point_L_Lp(right)
kl=left*(Lpl/Ll)
kr=right*(Lpr/Lr)
alow=kr.inv()
aup=kl.inv()

LOW=Fraction(1278437096209,10**11)   # 12.78437096209
HIGH=Fraction(1278437096216,10**11)  # 12.78437096216
assert alow.lo>LOW
assert aup.hi<HIGH
print("C183 unique partial-lift optimum bracket: PASS")
print("  s_* in",float(left),float(right))
print("  g(left) in",gL.dec())
print("  g(right) in",gR.dec())
print("  alpha_* lower enclosure starts",float(alow.lo))
print("  alpha_* upper enclosure ends",float(aup.hi))
print("  certified:",float(LOW),"< alpha_* <",float(HIGH))

# New rigorous UNSAT endpoint can be any alpha>alpha_*.
alpha_L=Fraction(54299,25000)
alpha_U=HIGH
width=alpha_U-alpha_L
assert width==Fraction(1061241096216,10**11)
assert width < Fraction(10612411,10**6)  # previous 10.612411
print("Metric movement: PASS")
print("  alpha_L =",float(alpha_L))
print("  alpha_U_new =",float(alpha_U))
print("  width_new =",width,"=",float(width))
print("  width_old = 10.612411")
print("ALL_EXACT_CHECKS_PASS")
