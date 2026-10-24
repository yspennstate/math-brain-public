#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def lam(N,s):
    return Fraction(N,2*s*(N-s))

def active(N,s):
    return 2*s >= N and 5*s < 4*N

def rseq(N):
    # floor(sqrt(log_2 N)) in an exact integer form.
    r=0
    while 2**((r+1)*(r+1)) <= N:
        r += 1
    return r

def dseq(N):
    return 2**max(1,rseq(N))

def theta(N):
    return Fraction(1,max(2,rseq(N)))

def inactive_dist(N):
    rates=[(s,lam(N,s)) for s in range(1,N) if not active(N,s)]
    R=sum((x for _,x in rates),Fraction(0))
    return [(s,x/R) for s,x in rates],R

def mask_probs4(p):
    bal=unb=null=Fraction(0)
    for bits in product((0,1),repeat=4):
        r=sum(bits)
        pr=p**r*(1-p)**(4-r)
        if r in (0,4):
            null += pr
        elif r==2:
            bal += pr
        else:
            unb += pr
    check(bal+unb+null==1)
    return bal,unb,null

# 1. Harmonic decomposition and exact effect of uniform thinning.
for N in range(2,401):
    total=sum((lam(N,s) for s in range(1,N)),Fraction(0))
    check(total==H(N-1),f"harmonic sum N={N}")
    W=sum((lam(N,s) for s in range(1,N) if active(N,s)),Fraction(0))
    R=sum((lam(N,s) for s in range(1,N) if not active(N,s)),Fraction(0))
    check(W+R==total)
    if R:
        pi,_=inactive_dist(N)
        check(sum((x for _,x in pi),Fraction(0))==1)
        th=theta(N)
        scaled_total=sum((th*lam(N,s) for s in range(1,N) if not active(N,s)),Fraction(0))
        check(scaled_total==th*R)
        for s,p in pi:
            check((th*lam(N,s))/scaled_total==p,
                  "uniform thinning changed conditional mark law")

# 2. Exact integer schedules used by C093.
for N in range(2,10001):
    r=rseq(N)
    check(2**(r*r)<=N)
    check(2**((r+1)*(r+1))>N)
    check(dseq(N)==2**max(1,r))
    check(theta(N)==Fraction(1,max(2,r)))
    check(0 < theta(N) <= 1)
check(theta(4)==Fraction(1,2))
check(dseq(4)==2)

# 3. Exact seam endpoint observables and active CTCS targets.
def h11(p):
    return 2*p*(1-p)

def h13(p):
    return p*(1-p)**3 + p**3*(1-p)

check(h11(Fraction(1,2))==Fraction(1,2))
check(h11(Fraction(4,5))==Fraction(8,25))
check(h13(Fraction(1,2))==Fraction(1,8))
check(h13(Fraction(4,5))==Fraction(68,625))

# Active source target for 1|1: density cancels to 1 on [1/2,4/5].
check(Fraction(4,5)-Fraction(1,2)==Fraction(3,10))

# Active source target for 1|3: integral of (x^2+(1-x)^2)/2.
def anti13(x):
    return x/Fraction(2) - x*x/Fraction(2) + x*x*x/Fraction(3)
check(anti13(Fraction(4,5))-anti13(Fraction(1,2))==Fraction(21,250))

# 4. Quantitative incompatibility of the two seam weights.
# w11-w13 = 5(80*ell-57)/(81*ell).
# The exact numerator identity after putting both over 81*ell is
# 9(15-16 ell)-4(105-136 ell)=5(80 ell-57).
check(9*15-4*105 == -5*57)
check(-9*16+4*136 == 5*80)

# Strict elementary bounds used in the proof:
# midpoint lower bound 2/3 < log 2, two-panel trapezoid upper bound
# log 2 < 17/24, and 17/24 < 57/80 by 1/240.
check(Fraction(2,3) < Fraction(17,24))
check(Fraction(57,80)-Fraction(17,24)==Fraction(1,240))
# These imply |w11-w13| > 5/243 and the smaller affine slope is
# > 81*(2/3)/5000 = 27/2500. Therefore every w misses at least
# one target by > (1/2)*(5/243)*(27/2500) = 1/9000.
check(Fraction(81,5000)*Fraction(2,3)==Fraction(27,2500))
check(Fraction(1,2)*Fraction(5,243)*Fraction(27,2500)==Fraction(1,9000))

# 5. C093 exact N=4 finite non-equivalence witness.
N=4
rates=[lam(4,s) for s in range(1,4)]
check(rates==[Fraction(2,3),Fraction(1,2),Fraction(2,3)])
check([active(4,s) for s in range(1,4)]==[False,True,True])
# Same hash phases as C092; only shadow traffic is thinned by theta_4=1/2.
p0=[Fraction(1,4),Fraction(1,2),Fraction(3,4)]
p1=[Fraction(1,4),Fraction(2,3),Fraction(3,5)]

def split_rates(ps):
    bal=unb=null=Fraction(0)
    for rr,p in zip(rates,ps):
        b,u,n=mask_probs4(p)
        bal += rr*b
        unb += rr*u
        null += rr*n
    return bal,unb,null

a0,u0,n0=split_rates(p0)
a1,u1,n1=split_rates(p1)
check(a0==Fraction(15,32))
check(u0==Fraction(7,8))
check(n0==Fraction(47,96))
check(a1==Fraction(560707,1080000))
check(u1==Fraction(722693,810000))
check(n1==Fraction(1367107,3240000))

B1=a1/(a1+u1)
refresh=theta(4)*lam(4,1)
B0=(a0+refresh*B1)/(a0+u0+refresh)
check(B1==Fraction(1682121,4572893))
check(refresh==Fraction(1,3))
check(B0==Fraction(259608057,736235773))

source=Fraction(3,11)
c092=Fraction(313435929,882568349)
c091=Fraction(357573111,981185971)
c090=Fraction(3200871,8926643)
c084=Fraction(1682121,4572893)
check(B0-source==Fraction(646981308,8098593503))
check(B0-c092==Fraction(-358829568,142093504189))
check(B0-c091==Fraction(-8534332294131456,722384211815940583))
check(B0-c090==Fraction(-39167290195632,6572113909400039))
check(B0-c084==Fraction(-11213424,736235773))
check(len({B0,source,c092,c091,c090,c084})==6)

# 6. Sample exact growth sanity on two square-log grid points.
# (The asymptotic theta_N R_N -> infinity is proved analytically in the report.)
prev=None
for m in (3,4):
    N=2**(m*m)
    _,R=inactive_dist(N)
    rho=theta(N)*R
    check(theta(N)==Fraction(1,m))
    if prev is not None:
        check(rho>prev)
    prev=rho

print(f"ASSERTIONS={ASSERTIONS}")
print(f"C093_N4_BALANCED_ROOT={B0}")
print(f"C093_N4_BALANCED_ROOT_DECIMAL={float(B0):.15f}")
print(f"C093_MINUS_CTCS={B0-source}")
print(f"C093_MINUS_C092={B0-c092}")
print(f"C093_MINUS_C091={B0-c091}")
print(f"C093_MINUS_C090={B0-c090}")
print(f"C093_MINUS_C084={B0-c084}")
print("SEAM_UNIFORM_RATE_GAP_LOWER_BOUND=1/9000")
print("STATUS=ALL_EXACT_CHECKS_PASS")
