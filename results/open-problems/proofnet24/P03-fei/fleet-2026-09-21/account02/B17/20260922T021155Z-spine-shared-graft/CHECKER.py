#!/usr/bin/env python3
"""Exact checker for B17's distinguished-spine shared-graft recurrence.

This verifies the source-core integer Walsh invariants, the exact first
spine-graft improvement, the fixed-point interval, and the numerical
constants used in the analytic contraction proof.  Universal convergence
is proved in REPORT.md; finite computation is not substituted for it.
"""
from fractions import Fraction as F
from functools import lru_cache
from decimal import Decimal, getcontext
getcontext().prec = 100
TERMS = 28

TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
 (TOP,BOT),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
 ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00','fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
 ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
 ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT),
]

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for st in range(0,len(a),2*h):
            for j in range(st,st+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def core_data():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(row),16)^base for row in SLICES[1:]]
    assert all(m.bit_count()==2 for m in masks)
    hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
    a=[-1 if (base>>x)&1 else 1 for x in range(512)]
    for host in hosts:
        for x in host: a[x]=0
    A=fwht(a)
    Q=[]
    for lo,hi in hosts:
        q=[0]*512; q[lo]=1; q[hi]=-1
        Q.append(fwht(q))
    Qsum=[sum(row[s] for row in Q) for s in range(512)]
    assert max(map(abs,A))==114
    assert max(map(abs,Qsum))==18
    assert sum(map(abs,Qsum))==1584
    assert sum(q*q for q in Qsum)==9216
    return A,Qsum

def p2(k): return F(1<<k) if k>=0 else F(1,1<<(-k))
def log_unit(x):
    assert F(1)<=x<=F(2)
    if x==1: return F(0),F(0)
    z=(x-1)/(x+1); z2=z*z; p=z; s=F(0)
    for j in range(TERMS):
        s += p/F(2*j+1); p *= z2
    return 2*s, 2*s+2*p/(F(2*TERMS+1)*(1-z2))

@lru_cache(None)
def log2i(x):
    x=F(x)
    if x<1:
        lo,hi=log2i(1/x); return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<p2(e): e-=1
    m=x/p2(e)
    a,b=log_unit(m); c,d=log_unit(F(2))
    return F(e)+a/d, F(e)+b/c

def phi_i(x):
    x=F(x)
    if not x: return F(0),F(0)
    a,b=log2i(1/x)
    return x*a,x*b

A,Q=core_data()
alpha=F(9,256)
q0=F(133,128)

def K_i(b):
    lo=hi=F(0)
    for a,q in zip(A,Q):
        z=F(a,512)+b*F(q,512)
        p0,p1=phi_i(z*z)
        lo+=p0; hi+=p1
    p0,p1=phi_i(b*b)
    extra=alpha*16*(1-b*b)
    return lo-alpha*p1+extra, hi-alpha*p0+extra

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

# Inherited balanced source-valid F_1.
c1=F(14593,65536)
I1=F(68013,32768)
R1lo=F('6.521850083658612443633672199029299526203969334')
R1hi=F('6.521850083658612443633672199029299526203969335')

# Four-copy distinguished spine, not full fourth self-composition.
S=1+c1+c1**2+c1**3
Isp=1+(I1-1)*S
b=c1**4
I2=F(261,128)+alpha*(Isp-1)
den=I2-1
coef=alpha*(Isp-1)
Klo,Khi=K_i(b)
R2lo=(Klo+coef*R1lo)/den
R2hi=(Khi+coef*R1hi)/den
lam1=q0/den

old_tail_upper=F('6.5218509495533749374651456092951')
assert R2lo > old_tail_upper
assert R2hi-R2lo < F(1,10**26)

# Same singleton map as the inherited full-composition recurrence.
stepc=lambda c:(F(57)+c**4)/256
c2=stepc(c1); c3=stepc(c2)
cL=F(22266585228,10**11)
cU=F(22266585229,10**11)
assert cL<c3<cU
assert stepc(cL)>cL and stepc(cU)<cU

# Recompute a rigorous interval for the limiting forcing level T(c*)=K(c*^4)/q0.
# REPORT.md supplies the analytic |K'(b)|<19 proof on this interval.
bL,bU=cL**4,cU**4
b0=F(245818450862,10**14)
dist=max(abs(b0-bL),abs(b0-bU))
K0lo,K0hi=K_i(b0)
Tlo=F(128,133)*(K0lo-19*dist)
Thi=F(128,133)*(K0hi+19*dist)
assert Tlo > F('6.5218511673423')
assert Thi < F('6.5218511673533')

# Uniform influence/contraction constants used in the analytic all-tail proof.
# If I<=21/10 and c<=1/4, then S(c)<=85/64 and this is the next-I upper bound.
Imax_next=F(261,128)+alpha*F(11,10)*F(85,64)
assert Imax_next < F(21,10)
lambda_min=q0/(Imax_next-1)
assert lambda_min==F(34048,35731)
rho=1-lambda_min
assert rho < F(48,1000)

print("PASS")
print("scope=exact source-core invariants + first spine-graft interval + fixed-point forcing interval")
print("I_spine="+str(dec(Isp)))
print("I_2="+str(dec(I2)))
print("lambda_1="+str(dec(lam1)))
print("R_2_lower="+str(dec(R2lo)))
print("R_2_upper="+str(dec(R2hi)))
print("gain_over_inherited_full_composition_tail_upper="+str(dec(R2lo-old_tail_upper)))
print("c_3="+str(dec(c3)))
print("T_star_lower="+str(dec(Tlo)))
print("T_star_upper="+str(dec(Thi)))
print("lambda_uniform_lower="+str(dec(lambda_min)))
print("R_contraction_uniform_upper="+str(dec(rho)))
print("full_FEI=OPEN_NOT_PROVED")
