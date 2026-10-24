from fractions import Fraction
from itertools import product, combinations
from math import comb
from functools import lru_cache

ASSERTS=0

def check(c,msg=""):
    global ASSERTS
    ASSERTS+=1
    if not c:
        raise AssertionError(msg)

def beta_prob_tuple(z,x):
    p=Fraction(1)
    for bit in z:
        p *= x if bit else 1-x
    return p

@lru_cache(None)
def avg_law_cached(N,u,r):
    x=Fraction(u,N)
    M=max(x,1-x)
    zs=list(product([0,1], repeat=N))
    Ts=list(combinations(range(N),r))
    out={z:Fraction(0) for z in zs}
    base={z:beta_prob_tuple(z,x) for z in zs}
    for T in Ts:
        for z in zs:
            R=Fraction(1)
            for t in T:
                R *= (Fraction(z[t])-x)/M
            out[z]+=base[z]*(1+R)/len(Ts)
    return tuple(out.items())

@lru_cache(None)
def ref_law_cached(N,u):
    x=Fraction(u,N)
    return tuple((z,beta_prob_tuple(z,x)) for z in product([0,1], repeat=N))

def event_prob_items(items,A,B):
    s=Fraction(0)
    for z,p in items:
        ok1=all(z[a] for a in A) and all(not z[b] for b in B)
        ok2=all(not z[a] for a in A) and all(z[b] for b in B)
        if ok1 or ok2:
            s+=p
    return s

@lru_cache(None)
def rate_cached(N,i,j,r):
    A=tuple(range(i)); B=tuple(range(i,i+j))
    tot=Fraction(0)
    for u in range(1,N):
        x=Fraction(u,N)
        a=Fraction(1,2*(N-1))/(x*(1-x))
        items=ref_law_cached(N,u) if r==0 else avg_law_cached(N,u,r)
        tot += a*event_prob_items(items,A,B)
    return tot

# C059 r=4 laws are honest probability measures and preserve all <4 marginals exactly.
for N in range(4,8):
    for u in range(1,N):
        x=Fraction(u,N)
        items=avg_law_cached(N,u,4)
        d=dict(items)
        check(sum(d.values())==1,("norm",N,u))
        check(min(d.values())>=0,("pos",N,u))
        for k in range(1,4):
            for coords in combinations(range(N),k):
                for patt in product([0,1],repeat=k):
                    q=sum(p for z,p in items if all(z[c]==b for c,b in zip(coords,patt)))
                    q0=Fraction(1)
                    for b in patt:
                        q0*=x if b else 1-x
                    check(q==q0,("marg",N,u,coords,patt))

# Pair normalization and all three-label split rates are exactly the harmonic reference.
for N in range(4,8):
    check(rate_cached(N,1,1,4)==1)
    check(rate_cached(N,1,2,4)==Fraction(1,2))

# U038 odd-support cancellation: r=3 defects cancel exactly after x <-> 1-x pairing.
for N in range(4,8):
    for k in range(2,N+1):
        for i in range(1,k):
            j=k-i
            check(rate_cached(N,i,j,3)==rate_cached(N,i,j,0),("odd",N,i,j))

# U038 quantitative r=4 dual/TV bound on every specified split checked exhaustively.
for N in range(4,8):
    for k in range(4,N+1):
        bd=Fraction(2*comb(k,4),comb(N,4))
        for i in range(1,k):
            j=k-i
            err=abs(rate_cached(N,i,j,4)-rate_cached(N,i,j,0))
            check(err<=bd,("bound",N,i,j,err,bd))

# Closed four-label defect formula.  Direct exhaustive comparison is used for N<=7;
# positivity of the exact closed form is additionally checked through N=20.
for N in range(4,21):
    s=Fraction(0)
    for u in range(1,N):
        x=Fraction(u,N)
        m=min(x,1-x); M=max(x,1-x)
        s += m**3/M
    D=s/Fraction((N-1)*comb(N,4))
    check(D>0)
    if N<=7:
        check(rate_cached(N,1,3,4)==rate_cached(N,1,3,0)-D,("D13",N))
        check(rate_cached(N,2,2,4)==rate_cached(N,2,2,0)+D,("D22",N))

# Frozen-convention finite witness at N=6, including distinction from C057.
N=6
check(rate_cached(N,1,3,4)==Fraction(2029,6750))
check(rate_cached(N,2,2,4)==Fraction(673,3375))
check(rate_cached(N,1,3,0)==Fraction(11,36))
check(rate_cached(N,2,2,0)==Fraction(7,36))
check(rate_cached(N,1,3,0)-rate_cached(N,1,3,4)==Fraction(67,13500))
check(rate_cached(N,2,2,4)-rate_cached(N,2,2,0)==Fraction(67,13500))
# C057 has growing support K_N=6 at N=6, i.e. the r=6 law here.
check(rate_cached(N,1,3,6)==Fraction(11,36))
check(rate_cached(N,2,2,6)==Fraction(7,36))
check(rate_cached(N,1,3,4)!=rate_cached(N,1,3,6))
check(rate_cached(N,2,2,4)!=rate_cached(N,2,2,6))

print("ASSERTIONS",ASSERTS)
print("N6_C059_q13=2029/6750")
print("N6_C059_q22=673/3375")
print("N6_REFERENCE_q13=11/36")
print("N6_REFERENCE_q22=7/36")
print("N6_DEFECT=67/13500")
print("ODD_R3_HARMONIC_PAIRING=CANCELS_EXACTLY_N4_TO_N7")
print("ALL_EXACT_CHECKS_PASS")
