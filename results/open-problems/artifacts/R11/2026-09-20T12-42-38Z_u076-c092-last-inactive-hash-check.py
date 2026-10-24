#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import isqrt

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def lam(N,s):
    return Fraction(N, 2*s*(N-s))

def active(N,s):
    return 2*s >= N and 5*s < 4*N  # s/N in [1/2,4/5)

def harmonic_raw(N):
    total = H(N-1)
    out = [lam(N,s)/total for s in range(1,N)]
    check(sum(out, Fraction(0)) == 1, f"raw marks do not sum to 1 at N={N}")
    return out

def inactive_dist(N):
    rates = [(s,lam(N,s)) for s in range(1,N) if not active(N,s)]
    R = sum((x for _,x in rates), Fraction(0))
    return [(s,x/R) for s,x in rates], R

def tv(q,u):
    return sum((abs(x-u) for x in q), Fraction(0))/2

def excess(p,d):
    u=Fraction(1,d)
    return sum((x-u for x in p if x>u), Fraction(0))

def output_mass(p, assn, d):
    q=[Fraction(0) for _ in range(d)]
    for x,j in zip(p,assn):
        q[j]+=x
    return q

def brute_opt_tv(p,d):
    best=None
    besta=None
    for a in product(range(d), repeat=len(p)):
        q=output_mass(p,a,d)
        val=tv(q,Fraction(1,d))
        if best is None or val<best or (val==best and a<besta):
            best,besta=val,a
        # U076 dual lower bound for every deterministic hash
        check(val >= excess(p,d), "oversized-atom lower bound failed")
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
    for bits in product((0,1), repeat=4):
        r=sum(bits)
        pr=(p**r)*((1-p)**(4-r))
        if r in (0,4):
            null += pr
        elif r==2:
            bal += pr
        else:
            unb += pr
    check(bal+unb+null == 1)
    return bal,unb,null

# 1. Harmonic clock identities and elementary conditional-distribution facts.
for N in range(2,201):
    check(sum((lam(N,s) for s in range(1,N)), Fraction(0)) == H(N-1),
          f"harmonic clock identity failed N={N}")
    raw=harmonic_raw(N)
    check(all(x>0 for x in raw))
    if N>=4:
        pi,R=inactive_dist(N)
        check(sum((x for _,x in pi), Fraction(0)) == 1)
        check(R > 0)
        # lambda_s <= 1/min(s,N-s)
        for s in range(1,N):
            check(lam(N,s) <= Fraction(1,min(s,N-s)))

# 2. Exact integer alphabet schedule d_N=2^max(1,floor sqrt(log_2 N)).
for N in range(2,10001):
    r=floor_sqrt_log2(N)
    check(2**(r*r) <= N)
    check(2**((r+1)*(r+1)) > N)
    check(dseq(N) == 2**max(1,r))
# exact anchor
check(dseq(4)==2)

# 3. Dual oversized-atom bound under exhaustive deterministic hashes
# for several exact harmonic inactive-mark laws.
for N in range(4,11):
    pi,_=inactive_dist(N)
    p=[x for _,x in pi]
    for d in (2,3):
        # Keep exhaustive search small but nontrivial.
        if d**len(p) <= 200000:
            best,a=brute_opt_tv(p,d)
            check(best >= excess(p,d))
            q=output_mass(p,a,d)
            check(sum(q,Fraction(0))==1)

# 4. Finite N=4 C092 certificate from direct 16-mask enumeration.
N=4
raw=harmonic_raw(N)
check(raw == [Fraction(4,11), Fraction(3,11), Fraction(4,11)])
check([active(N,s) for s in range(1,N)] == [False,True,True])

# Incoming memory I (stored inactive mark 1): h_4(1)=1, d=2, b=1.
# s=2 has shifted log-odds 0 + log 2 -> p=2/3.
# s=3 has log-odds log 3 + log 2 mod log 4 = log(3/2) -> p=3/5.
pI=[Fraction(1,4), Fraction(2,3), Fraction(3,5)]
# Incoming memory A uses the declared fallback J=0.
pA=[Fraction(1,4), Fraction(1,2), Fraction(3,4)]

def aggregate(ps):
    bal=unb=tI=tA=Fraction(0)
    for idx,p in enumerate(ps):
        b,u,n=mask_probs4(p)
        w=raw[idx]
        bal += w*b
        unb += w*u
        if idx==0:
            tI += w*n
        else:
            tA += w*n
    check(bal+unb+tI+tA==1)
    return bal,unb,tI,tA

aI,uI,tII,tIA=aggregate(pI)
aA,uA,tAI,tAA=aggregate(pA)

check(aI == Fraction(560707,1980000))
check(uI == Fraction(722693,1485000))
check(tII == Fraction(41,352))
check(tIA == Fraction(21101,185625))
check(aA == Fraction(45,176))
check(uA == Fraction(21,44))
check(tAI == Fraction(41,352))
check(tAA == Fraction(53,352))

# Solve the two-state absorbing equations:
# B_I=aI+tII B_I+tIA B_A; B_A=aA+tAI B_I+tAA B_A.
det=(1-tII)*(1-tAA)-tIA*tAI
check(det>0)
BI=(aI*(1-tAA)+tIA*aA)/det
BA=((1-tII)*aA+tAI*aI)/det
check(BI == Fraction(563725059,1541504863))
check(BA == Fraction(541298211,1541504863))

source=Fraction(3,11)
c091=Fraction(357573111,981185971)
c090=Fraction(3200871,8926643)
check(BI-source == Fraction(1576461060,16956553493))
check(BI-c091 == Fraction(1918429907408496,1512502945803876973))
check(BI-c090 == Fraction(98014139511264,13760463594764909))
check(BI != source and BI != c091 and BI != c090)

print(f"ASSERTIONS={ASSERTIONS}")
print(f"C092_N4_BALANCED_ROOT={BI}")
print(f"C092_N4_BALANCED_ROOT_DECIMAL={float(BI):.15f}")
print(f"C092_MINUS_CTCS={BI-source}")
print(f"C092_MINUS_C091={BI-c091}")
print(f"C092_MINUS_C090={BI-c090}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
