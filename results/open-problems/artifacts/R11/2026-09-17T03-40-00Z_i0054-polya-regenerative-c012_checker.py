#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial
from itertools import permutations

checks = 0

def beta_int(a,b):
    assert a>=1 and b>=1
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def rising(a,n):
    z=1
    for j in range(n):
        z*=a+j
    return z

def polya_pattern_prob(r, stay, peel):
    # A specified color sequence / specified subset assignment in a two-color
    # Polya urn with r initial "stay" balls and 1 initial "peel" ball.
    return Fraction(rising(r,stay)*rising(1,peel), rising(r+1,stay+peel))

def harmonic(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction())

# 1. Exact Polya-urn normalization and beta-mixture identity.
for m in range(2,10):
    n=m-1
    for r in range(1,10):
        tot=Fraction()
        for peel in range(0,n+1):
            stay=n-peel
            p=polya_pattern_prob(r,stay,peel)
            q=Fraction(r,1)*beta_int(r+stay, peel+1)
            assert p==q
            checks += 1
            tot += comb(n,peel)*p
        assert tot==1
        checks += 1

# 2. Harmonic spectral identity in finite beta-integral/telescoping form.
for i in range(1,8):
    for j in range(1,8):
        for R in range(1,20):
            s=sum((beta_int(i+r-1,j+1) for r in range(1,R+1)), Fraction())
            assert s == beta_int(i,j)-beta_int(i+R,j)
            checks += 1

# 3. Hidden-label projected finite-R rate and uniform truncation bound.
def qR(m,b,i,R):
    j=b-i
    assert 1 <= i < b <= m
    target=beta_int(i,j)
    err = Fraction(i,m)*beta_int(i+R,j)
    err += Fraction(j,m)*beta_int(j+R,i)
    if m>b:
        err += Fraction(m-b,m)*(beta_int(j+R+1,i)+beta_int(i+R+1,j))
    return target-err, err

for m in range(2,31):
    for b in range(2,min(m,8)+1):
        for i in range(1,b):
            j=b-i
            for R in range(1,16):
                q,e=qR(m,b,i,R)
                assert q >= 0 and e >= 0
                assert q+e == beta_int(i,j)
                assert e <= Fraction(2,R+1)
                checks += 1

# 4. Check q_R by direct channel summation over anchor categories.
def qR_direct(m,b,i,R):
    j=b-i
    aA=sum((beta_int(i+r-1,j+1) for r in range(1,R+1)), Fraction())
    aC=sum((beta_int(j+r-1,i+1) for r in range(1,R+1)), Fraction())
    hidden=sum((beta_int(j+r,i+1)+beta_int(i+r,j+1) for r in range(1,R+1)), Fraction())
    return Fraction(i,m)*aA + Fraction(j,m)*aC + Fraction(m-b,m)*hidden

for m in range(2,18):
    for b in range(2,min(m,7)+1):
        for i in range(1,b):
            for R in range(1,12):
                q,_=qR(m,b,i,R)
                assert q == qR_direct(m,b,i,R)
                checks += 1

# 5. CTCS total rate from particular unordered split rates.
for b in range(2,40):
    ordered=sum((Fraction(comb(b,i),2)*beta_int(i,b-i) for i in range(1,b)), Fraction())
    assert ordered == harmonic(b-1)
    checks += 1

# 6. Endpoint/singleton tail is the slow O(1/R) obstruction.
for R in range(1,100):
    q,e=qR(2,2,1,R)
    assert e == Fraction(1,R+1)
    checks += 1

# For all non-singleton-vs-non-singleton visible splits, tails are O(R^-2).
for m in range(4,30):
    for b in range(4,min(m,8)+1):
        for i in range(2,b-1):
            j=b-i
            if j<2: continue
            for R in range(2,30):
                _,e=qR(m,b,i,R)
                assert e <= Fraction(4,(R+1)*(R+2))
                checks += 1

# 7. N=3 exact finite non-equivalence witness.
def EU(r,power):
    return Fraction(r,r+power)

def E1mU2(r):
    return Fraction(2,(r+1)*(r+2))

def active_subset_prob(R,delta,J):
    J=set(J)
    p=Fraction(1)
    for r in range(1,R+1):
        a=delta/Fraction(r,1)
        p *= a if r in J else (1-a)
    return p

def cond_no_split(order):
    z=Fraction(1)
    for r in order:
        z*=EU(r,2)
    return z

def cond_degree3(order):
    Eq=Fraction(1)
    Eq2=Fraction(1)
    for r in order:
        Eq*=EU(r,1)
        Eq2*=EU(r,2)
    prob_both_peeled=(1 - 2*Eq + Eq2)
    prob_same_batch=Fraction()
    prior_U2=Fraction(1)
    for r in order:
        prob_same_batch += prior_U2*E1mU2(r)
        prior_U2 *= EU(r,2)
    return prob_both_peeled-prob_same_batch

def exact_n3():
    R=3
    delta=Fraction(1,27)
    p0=Fraction()
    p3=Fraction()
    for mask in range(1<<R):
        J=[r for r in range(1,R+1) if mask & (1<<(r-1))]
        pa=active_subset_prob(R,delta,J)
        if not J:
            p0 += pa
            continue
        ords=list(permutations(J))
        c0=sum((cond_no_split(o) for o in ords),Fraction())/len(ords)
        c3=sum((cond_degree3(o) for o in ords),Fraction())/len(ords)
        p0 += pa*c0
        p3 += pa*c3
    return p0,p3,p3/(1-p0)

p0,p3,root3=exact_n3()
assert p0 == Fraction(3406559,3542940)
assert p3 == Fraction(21521,127545840)
assert root3 == Fraction(21521,4909716)
checks += 3

old = {
    "C001": Fraction(0),
    "C002": Fraction(1,10),
    "C003": Fraction(1,22),
    "C004": Fraction(1,6),
    "C005": Fraction(1,728),
    "C006": Fraction(1,7),
    "C007": Fraction(1,71),
    "C008": Fraction(1,71),
    "C009": Fraction(0),
    "C010": Fraction(0),
    "C011": Fraction(2,105),
}
for name,v in old.items():
    assert root3 != v
    checks += 1

# 8. Verify chosen approximation/error scale decreases on dyadic N.
def coupling_bound_core(N):
    R=N
    delta=Fraction(1,N**3)
    return Fraction(2,R+1) + delta*harmonic(R)**2

vals=[]
for N in [2,4,8,16,32,64,128]:
    vals.append((N,coupling_bound_core(N)))
for (n1,v1),(n2,v2) in zip(vals,vals[1:]):
    assert v2 < v1
    checks += 1

print("C012 harmonic-channel Polya-urn checker")
print(f"checks={checks}")
print(f"N=3 no_visible_split={p0}")
print(f"N=3 raw_degree3={p3}")
print(f"N=3 first_visible_root_degree3={root3} ~= {float(root3):.12g}")
print("dyadic_error_core:")
for N,v in vals:
    print(f"  N={N}: {v} ~= {float(v):.12g}")
print("ALL_EXACT_CHECKS_PASS")
