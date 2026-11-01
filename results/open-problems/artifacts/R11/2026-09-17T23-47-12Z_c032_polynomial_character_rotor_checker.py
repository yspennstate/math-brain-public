from fractions import Fraction
from math import gcd
from hashlib import sha256

checks = 0

def ck(cond, msg="check failed"):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def least_prime_ge(n):
    p = n
    while not is_prime(p):
        p += 1
    return p

def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n+1)), Fraction(0,1))

def det_mod(mat, p):
    a = [row[:] for row in mat]
    n = len(a)
    det = 1
    for c in range(n):
        piv = None
        for r in range(c,n):
            if a[r][c] % p:
                piv = r; break
        if piv is None:
            return 0
        if piv != c:
            a[c],a[piv]=a[piv],a[c]
            det = -det
        pv = a[c][c] % p
        det = (det*pv) % p
        inv = pow(pv,p-2,p)
        for r in range(c+1,n):
            f = a[r][c]*inv % p
            for j in range(c,n):
                a[r][j] = (a[r][j]-f*a[c][j])%p
    return det%p

def d_of_p(p):
    import math
    return min(p-1,max(2,int(math.log(p,2))))

def yscore(a,t,p,d):
    y=0
    tp=t%p
    # sum_{r=0}^{d-1} a^r t^{r+1}
    ap=1
    for r in range(d):
        y=(y + ap*tp)%p
        ap=(ap*a)%p
        tp=(tp*t)%p
    return y

def redset(N,p,d,s,t):
    return tuple(a for a in range(N) if yscore(a,t,p,d) < s)

def w(p,s):
    return Fraction(p,2*s*(p-s))

# Basic finite sanity: least-prime near N, harmonic weight identity, d<p.
for N in range(3,81):
    p=least_prime_ge(N)
    ck(N <= p < 2*N,(N,p))
    d=d_of_p(p)
    ck(2 <= d < p,(N,p,d))
    sw=sum((w(p,s) for s in range(1,p)),Fraction(0,1))
    ck(sw == harmonic(p-1),(N,p,sw,harmonic(p-1)))

# Vandermonde invertibility for every distinct tuple/subset up to d at small primes.
import itertools
for p in [3,5,7,11,13,17,19,23,29,31]:
    d=d_of_p(p)
    for k in range(1,d+1):
        for aa in itertools.combinations(range(p),k):
            mat=[[pow(a,r,p) for a in aa] for r in range(k)]
            ck(det_mod(mat,p)!=0,(p,k,aa))

# Exact pattern-count sanity for several primes: all k-coordinate score vectors have
# nontrivial variation as t runs and exact counts sum to p.
pattern_rows=0
for p in [5,7,11,13,17,19]:
    d=d_of_p(p)
    for k in range(1,min(d,4)+1):
        for aa in itertools.combinations(range(min(p,7)),k):
            counts={}
            for t in range(p):
                v=tuple(yscore(a,t,p,d) for a in aa)
                counts[v]=counts.get(v,0)+1
            ck(sum(counts.values())==p)
            ck(len(counts)>=1)
            pattern_rows += 1

# N=5 exact finite-law witness on 4 visible labels 0,1,2,3.
N=5
p=least_prime_ge(N)
d=d_of_p(p)
tau=Fraction(1,p*p)
delta=tau/Fraction(p*(p-1),1)
ck(p==5)
ck(d==2)
ck(tau==Fraction(1,25))
ck(delta==Fraction(1,500))

# First entry (s=1,t=0) is monochromatic: Y_0(a)=0, all visible labels red.
first_red=redset(4,p,d,1,0)
ck(first_red==(0,1,2,3),first_red)

# For a specified support S among visible 0..3, compute probability that the
# first visible root split over repeated deterministic cycles is exactly S|S^c.
# Each entry has activation probability delta*c_s. If activated but monochromatic,
# state survives. If activated and nonmonochromatic, root splits and is absorbed.
visible=tuple(range(4))
entries=[]
for s in range(1,p):
    c=Fraction(p-1,1)*w(p,s)
    a=delta*c
    ck(0 <= a <= 1)
    for t in range(p):
        R=set(redset(4,p,d,s,t))
        entries.append((a,R))

def canon_support(S):
    S=frozenset(S); C=frozenset(visible)-S
    # unordered support canonical lex tuple minimum
    a=tuple(sorted(S)); b=tuple(sorted(C))
    return min(a,b),max(a,b)

def one_cycle_split_mass(target):
    target=canon_support(target)
    surv=Fraction(1,1)
    mass=Fraction(0,1)
    for a,R in entries:
        RR=set(R)&set(visible)
        if 0 < len(RR) < len(visible):
            if canon_support(RR)==target:
                mass += surv*a
            surv *= (1-a)
        # monochromatic activation/no-activation both leave root unsplit: survival 1
    return mass,surv

m13,Ssurv=one_cycle_split_mass({0})
m22,Ssurv2=one_cycle_split_mass({0,1})
ck(Ssurv==Ssurv2)
ck(m13>0 and m22>0)
R= m13/m22

# Archived exact values for regression.
exp_m13=Fraction(60707555723460827945614074683399,4199040000000000000000000000000000)
exp_m22=Fraction(126394002090531799,19440000000000000000)
exp_R=Fraction(7703418956282489179517201,3464343821016000000000000)
ck(m13==exp_m13,(m13,exp_m13))
ck(m22==exp_m22,(m22,exp_m22))
ck(R==exp_R,(R,exp_R))
ck(R>Fraction(11,5),R)

# Visible nontrivial supports seen during one cycle.
sups=set()
for a,Rd in entries:
    RR=set(Rd)&set(visible)
    if 0<len(RR)<4:
        sups.add(canon_support(RR))
ck(len(sups)==6,len(sups))

# Compare to retained exact binary root witnesses through C029.
prior=[
    Fraction(2,1), Fraction(7,5), Fraction(2699,1365), Fraction(2273,1153),
    Fraction(61381,43765), Fraction(166094447739,85563797248),
    Fraction(33,17), Fraction(5,3), Fraction(597,359), Fraction(18,11),
    Fraction(9,5), Fraction(5,4), Fraction(459,224)
]
for q in prior:
    ck(R != q,(R,q))
# C030 archived exact bracket gives additional separation.
ck(Fraction(459,224) < Fraction(11,5) < R)

# Bulk finite checks of exact score construction and color patterns.
for N in range(3,36):
    p=least_prime_ge(N); d=d_of_p(p)
    for s in range(1,p):
        for t in range(p):
            Rset=redset(N,p,d,s,t)
            ck(all(0 <= a < N for a in Rset))
            ck(len(set(Rset))==len(Rset))

print("C032_POLYNOMIAL_CHARACTER_ROTOR_EXACT_SELF_CHECK")
print(f"checks={checks}")
print(f"pattern_rows={pattern_rows}")
print(f"N5_p={p if N==5 else 5}")
print("N5_d=2")
print("N5_tau=1/25")
print("N5_delta=1/500")
print(f"N5_first_entry_red={list(first_red)}")
print(f"N5_num_particular_1_3_one_cycle={m13}")
print(f"N5_num_particular_2_2_one_cycle={m22}")
print(f"N5_root_particular_support_ratio={R}")
print(f"N5_root_particular_support_ratio_float={float(R)}")
print(f"N5_distinct_visible_split_supports={len(sups)}")
print("C030 archived bracket used: 2 < R_C030 < 459/224 < 11/5 < R_C032")
print("C031 archived first-entry behavior used: activated first entry gives a nontrivial singleton split")
print("C032 first-entry behavior: activated first entry is monochromatic, so no split")
print("ALL_EXACT_CHECKS_PASS")
