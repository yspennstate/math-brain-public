from fractions import Fraction
from itertools import permutations, combinations
from math import comb, isqrt

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def harmonic(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def blocks(N,b):
    sizes=[]
    pos_to_block={}
    start=0
    r=0
    while start < N:
        s=min(b,N-start)
        sizes.append(s)
        for q in range(start,start+s):
            pos_to_block[q]=r
        start += s
        r += 1
    return sizes,pos_to_block

def kappa(N,sizes):
    if N < 2:
        return Fraction(0)
    return Fraction(sum(s*(s-1) for s in sizes), N*(N-1))

def unordered_split_prob(assign, A, x, pos_to_block):
    A=set(A)
    Ab=set()
    Bb=set()
    for lab,pos in enumerate(assign):
        blk=pos_to_block[pos]
        if lab in A:
            Ab.add(blk)
        else:
            Bb.add(blk)
    if Ab & Bb:
        return Fraction(0)
    ra=len(Ab)
    rb=len(Bb)
    return x**ra * (1-x)**rb + (1-x)**ra * x**rb

def iid_split_prob(m,i,x):
    return x**i*(1-x)**(m-i) + (1-x)**i*x**(m-i)

def micro_rate(N,b,m,A):
    sizes,p2b=blocks(N,b)
    acc=Fraction(0)
    count=0
    for assign in permutations(range(N),m):
        count += 1
        for j in range(1,N):
            x=Fraction(j,N)
            lam=Fraction(N,2*j*(N-j))
            acc += lam * unordered_split_prob(assign,A,x,p2b)
    return acc/count

def iid_rate(N,m,i):
    acc=Fraction(0)
    for j in range(1,N):
        x=Fraction(j,N)
        lam=Fraction(N,2*j*(N-j))
        acc += lam*iid_split_prob(m,i,x)
    return acc

def collision_probability_exact(N,b,m):
    sizes,p2b=blocks(N,b)
    total=0
    bad=0
    for assign in permutations(range(N),m):
        total += 1
        bs=[p2b[pos] for pos in assign]
        if len(set(bs)) < m:
            bad += 1
    return Fraction(bad,total)

def ctcs_rate(i,j):
    num=1
    for a in range(1,i):
        num*=a
    for a in range(1,j):
        num*=a
    den=1
    for a in range(1,i+j):
        den*=a
    return Fraction(num,den)

for N in range(2,10):
    b=max(1,isqrt(N))
    sizes,p2b=blocks(N,b)
    check(sum(sizes)==N, ("sizes",N))
    check(max(sizes)==b, ("max block",N,b,sizes))
    kap=kappa(N,sizes)
    rate=sum((Fraction(N,2*j*(N-j)) for j in range(1,N)), Fraction(0))
    check(rate==harmonic(N-1), ("clock",N,rate,harmonic(N-1)))
    cp=collision_probability_exact(N,b,2)
    check(cp==kap, ("kappa",N,cp,kap))
    ss=Fraction(sum(s*s for s in sizes),N*N)
    maxfrac=Fraction(max(sizes),N)
    check(maxfrac*maxfrac <= ss, ("lower squares",N))
    check(ss <= maxfrac, ("upper squares",N))

for N in range(2,10):
    b=max(1,isqrt(N))
    sizes,_=blocks(N,b)
    kap=kappa(N,sizes)
    q=micro_rate(N,b,2,{0})
    rhs=Fraction(N-1,N)*(1-kap)
    check(q==rhs, ("pair formula",N,q,rhs))

for N in range(2,9):
    b=max(1,isqrt(N))
    sizes,p2b=blocks(N,b)
    kap=kappa(N,sizes)
    for m in range(2,min(4,N)+1):
        cp=collision_probability_exact(N,b,m)
        union=Fraction(comb(m,2))*kap
        check(cp <= union, ("union collision",N,m,cp,union))
        for i in range(1,m):
            qi=iid_rate(N,m,i)
            bound=Fraction(comb(m,2))*kap*Fraction(N-1,N)
            for At in combinations(range(m),i):
                A=set(At)
                qm=micro_rate(N,b,m,A)
                check(abs(qm-qi) <= bound,
                      ("generator bound",N,m,tuple(At),qm,qi,bound))
                check(qm==micro_rate(N,b,m,set(range(i))),
                      ("exchangeability",N,m,tuple(At),qm))
            check(qi>0, ("iid positive",N,m,i))

for N in range(2,8):
    b=max(1,isqrt(N))
    sizes,p2b=blocks(N,b)
    for m in range(2,min(4,N)+1):
        for assign in permutations(range(N),m):
            blks=[p2b[pos] for pos in assign]
            if len(set(blks))==m:
                for i in range(1,m):
                    A=set(range(i))
                    for j in range(1,N):
                        x=Fraction(j,N)
                        check(unordered_split_prob(assign,A,x,p2b)==iid_split_prob(m,i,x),
                              ("no-collision iid",N,m,assign,i,j))

N=4
b=2
single_rates=[micro_rate(N,b,4,{a}) for a in range(4)]
balanced_rates=[
    micro_rate(N,b,4,{0,1}),
    micro_rate(N,b,4,{0,2}),
    micro_rate(N,b,4,{0,3}),
]
check(single_rates == [Fraction(0)]*4, ("N4 singletons",single_rates))
check(balanced_rates == [Fraction(1,4)]*3, ("N4 balanced",balanced_rates))
total=sum(single_rates)+sum(balanced_rates)
check(total==Fraction(3,4), ("N4 total",total))
balanced_prob=sum(balanced_rates)/total
check(balanced_prob==1, ("N4 balanced prob",balanced_prob))
check(balanced_prob != Fraction(3,11), "must differ from CTCS(4) balanced probability")
check(ctcs_rate(1,3)==Fraction(1,3), "CTCS 1|3")
check(ctcs_rate(2,2)==Fraction(1,6), "CTCS 2|2")

for N in [10,25,100,1000,10000]:
    b=max(1,isqrt(N))
    sizes,_=blocks(N,b)
    kap=kappa(N,sizes)
    check(kap <= Fraction(b-1,N-1), ("kappa upper",N,b,kap))
    check(Fraction(b,N) <= Fraction(isqrt(N),N) + Fraction(1,N), ("b scale",N,b))

print("C079 exact checker")
print("assertions =", ASSERTIONS)
print("N4 singleton rates =", [str(q) for q in single_rates])
print("N4 balanced rates =", [str(q) for q in balanced_rates])
print("N4 total root rate =", total)
print("N4 balanced root probability =", balanced_prob)
for N in [4,5,6,7,8,9,10,25,100,1000,10000]:
    b=max(1,isqrt(N))
    sizes,_=blocks(N,b)
    print("N=%d b=%d blocks=%s kappa=%s" % (N,b,sizes if N<=25 else "omitted",kappa(N,sizes)))
print("ALL_EXACT_CHECKS_PASS")
