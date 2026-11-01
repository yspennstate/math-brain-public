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

def inactive_dist(N):
    rates=[(s,lam(N,s)) for s in range(1,N) if not active(N,s)]
    R=sum((x for _,x in rates),Fraction(0))
    return [(s,x/R) for s,x in rates],R

def tv(q,u):
    return sum((abs(x-u) for x in q),Fraction(0))/2

def excess(p,d):
    u=Fraction(1,d)
    return sum((x-u for x in p if x>u),Fraction(0))

def output_mass(p,a,d):
    q=[Fraction(0) for _ in range(d)]
    for x,j in zip(p,a):
        q[j]+=x
    return q

def brute_opt_tv(p,d):
    best=None; besta=None
    E=excess(p,d)
    for a in product(range(d),repeat=len(p)):
        q=output_mass(p,a,d)
        v=tv(q,Fraction(1,d))
        check(v>=E,"dual oversized-atom lower bound failed")
        if best is None or v<best or (v==best and a<besta):
            best,besta=v,a
    return best,besta

def floor_sqrt_log2(N):
    r=0
    while 2**((r+1)*(r+1)) <= N:
        r+=1
    return r

def dseq(N):
    return 2**max(1,floor_sqrt_log2(N))

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

# Harmonic identities, active/inactive decomposition, pointwise envelope.
for N in range(2,301):
    total=sum((lam(N,s) for s in range(1,N)),Fraction(0))
    check(total==H(N-1),f"harmonic sum N={N}")
    W=sum((lam(N,s) for s in range(1,N) if active(N,s)),Fraction(0))
    R=sum((lam(N,s) for s in range(1,N) if not active(N,s)),Fraction(0))
    check(W+R==total)
    if R:
        pi,_=inactive_dist(N)
        check(sum((x for _,x in pi),Fraction(0))==1)
    for s in range(1,N):
        check(lam(N,s)<=Fraction(1,min(s,N-s)))

# Exact d_N integer definition: r_N=max{r:2^(r^2)<=N}.
for N in range(2,20001):
    r=floor_sqrt_log2(N)
    check(2**(r*r)<=N)
    check(2**((r+1)*(r+1))>N)
    check(dseq(N)==2**max(1,r))
check(dseq(4)==2)

# Exhaustive finite checks of the U076 dual lower bound.
for N in range(4,12):
    pi,_=inactive_dist(N)
    p=[x for _,x in pi]
    for d in (2,3):
        if d**len(p)<=250000:
            best,a=brute_opt_tv(p,d)
            check(best>=excess(p,d))
            check(sum(output_mass(p,a,d),Fraction(0))==1)

# C092 corrected shadow-refresh finite witness at N=4.
N=4
rates=[lam(4,s) for s in range(1,4)]
check(rates==[Fraction(2,3),Fraction(1,2),Fraction(2,3)])
check([active(4,s) for s in range(1,4)]==[False,True,True])
refresh=lam(4,1) # only inactive shadow clock
check(refresh==Fraction(2,3))

# phase 0: source biases on active marks; phase 1: d=2 shifted compact-logit biases.
p0=[Fraction(1,4),Fraction(1,2),Fraction(3,4)]
p1=[Fraction(1,4),Fraction(2,3),Fraction(3,5)]

def split_rates(ps):
    bal=unb=null=Fraction(0)
    for r,p in zip(rates,ps):
        b,u,n=mask_probs4(p)
        bal += r*b
        unb += r*u
        null += r*n
    return bal,unb,null

a0,u0,n0=split_rates(p0)
a1,u1,n1=split_rates(p1)
check(a0==Fraction(15,32))
check(u0==Fraction(7,8))
check(n0==Fraction(47,96))
check(a1==Fraction(560707,1080000))
check(u1==Fraction(722693,810000))
check(n1==Fraction(1367107,3240000))

# Null ordinary proposals do not affect the phase; shadow refresh takes 0 -> 1.
B1=a1/(a1+u1)
B0=(a0+refresh*B1)/(a0+u0+refresh)
check(B1==Fraction(1682121,4572893))
check(B0==Fraction(313435929,882568349))

source=Fraction(3,11)
c091=Fraction(357573111,981185971)
c090=Fraction(3200871,8926643)
c084=Fraction(1682121,4572893)
check(B0-source==Fraction(800090172,9708251839))
check(B0-c091==Fraction(-8043773879911680,865963682487431879))
check(B0-c090==Fraction(-27056792275632,7878372574622407))
check(B0-c084==Fraction(-11213424,882568349))
check(len({B0,source,c091,c090,c084})==5)

print(f"ASSERTIONS={ASSERTIONS}")
print(f"C092_N4_BALANCED_ROOT={B0}")
print(f"C092_N4_BALANCED_ROOT_DECIMAL={float(B0):.15f}")
print(f"C092_MINUS_CTCS={B0-source}")
print(f"C092_MINUS_C091={B0-c091}")
print(f"C092_MINUS_C090={B0-c090}")
print(f"C092_MINUS_C084={B0-c084}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
