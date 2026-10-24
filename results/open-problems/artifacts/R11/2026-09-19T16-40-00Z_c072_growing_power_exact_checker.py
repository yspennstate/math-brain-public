#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial, gcd
from itertools import combinations, product

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def is_prime(n):
    if n < 2: return False
    d=2
    while d*d <= n:
        if n%d==0: return False
        d += 1 if d==2 else 2
    return True

def least_odd_prime_ge(n):
    q=max(3,n)
    while not (q%2==1 and is_prime(q)):
        q += 1
    return q

def least_prime_ge_congruent(n, d, residue=2):
    p=max(n,2)
    while True:
        if is_prime(p) and p%d==residue%d:
            return p
        p+=1

def params(N):
    import math
    d=least_odd_prime_ge(max(3, math.ceil(math.log(N+2))))
    p=least_prime_ge_congruent(max(N,d+1),d,2)
    return d,p

def phi_power(p,d):
    vals=[pow(x,d,p) for x in range(p)]
    check(len(set(vals))==p, f"x^d not permutation p={p},d={d}")
    check(gcd(d,p-1)==1)
    return vals

def phi_invpower(p,r):
    vals=[0]+[pow(x,(-r)%(p-1),p) for x in range(1,p)]
    check(len(set(vals))==p)
    return vals

def beta(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def unordered_split_rates(N,p,phi):
    labels=tuple(range(N))
    full=frozenset(labels)
    rates={}
    seen=set()
    for r in range(1,N):
        for At in combinations(labels,r):
            A=frozenset(At); B=full-A
            key=tuple(sorted((tuple(sorted(A)),tuple(sorted(B)))))
            if key in seen: continue
            seen.add(key)
            rate=Fraction(0)
            for u in range(1,p):
                w=Fraction(1,2*u*(p-u))
                for t in range(p):
                    red=frozenset(l for l in labels if phi[(t+l)%p] < u)
                    if red==A or red==B:
                        rate += w
            rates[key]=rate
    return rates

def by_size(N,rates):
    out={}
    for (A,B),q in rates.items():
        s=tuple(sorted((len(A),len(B))))
        out.setdefault(s,[]).append(q)
    return {s:sorted(v) for s,v in out.items()}

# Parameter checks and permutation checks for a range of finite N.
for N in range(2,41):
    d,p=params(N)
    check(is_prime(d))
    check(d%2==1)
    check(is_prime(p))
    check(p>=N and p>d)
    check(p%d==2%d)
    check(gcd(d,p-1)==1)
    phi_power(p,d)

# Integer finite-difference identity: sharp fixed-degree Fourier obstruction.
for d in range(1,10):
    hs=[(-1)**(d-j)*comb(d,j) for j in range(d+1)]
    for t in range(-10,11):
        lhs=sum(h*pow(t+j,d) for j,h in enumerate(hs))
        check(lhs==factorial(d), f"finite-difference failed d={d},t={t}")

# Exact Fourier nondegeneracy below the degree for two small prime examples.
# A phase sum_j h_j (t+a_j)^d is constant only if h=0 when m<=d.
for d,p,maxm in [(3,11,3),(5,7,5)]:
    for m in range(1,maxm+1):
        offsets=list(range(m))
        for h in product(range(p), repeat=m):
            if all(x==0 for x in h):
                continue
            vals=[]
            for t in range(p):
                vals.append(sum(hj*pow((t+a)%p,d,p) for hj,a in zip(h,offsets))%p)
            check(len(set(vals))>1, f"degenerate phase d={d},p={p},m={m},h={h}")

# C072 finite witness at N=6: d=3, p=11.
N=6
d,p=params(N)
check((d,p)==(3,11))
phi72=phi_power(p,d)
rates72=unordered_split_rates(N,p,phi72)
bs72=by_size(N,rates72)

expected15=[
    Fraction(127,720), Fraction(127,720),
    Fraction(271,1260), Fraction(271,1260), Fraction(271,1260), Fraction(271,1260)
]
expected24=[
    Fraction(0,1), Fraction(1,36), Fraction(1,36),
    Fraction(29,840), Fraction(29,840),
    Fraction(13,336), Fraction(13,336), Fraction(13,336),
    Fraction(7,144), Fraction(7,144),
    Fraction(31,560), Fraction(67,1008), Fraction(419,5040),
    Fraction(151,1680), Fraction(151,1680)
]
expected33=[
    Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1),
    Fraction(1,60), Fraction(1,48), Fraction(29,840), Fraction(43,840),
    Fraction(31,560), Fraction(57,280)
]
check(bs72[(1,5)]==expected15)
check(bs72[(2,4)]==expected24)
check(bs72[(3,3)]==expected33)

# Aggregate exact witnesses.
agg={s:sum(v,Fraction(0)) for s,v in bs72.items()}
check(agg[(1,5)]==Fraction(1019,840))
check(agg[(2,4)]==Fraction(607,840))
check(agg[(3,3)]==Fraction(107,280))
total=sum(agg.values(),Fraction(0))
check(total==Fraction(649,280))
check(agg[(3,3)]/total==Fraction(107,649))

# Source CTCS specified rates are all strictly positive and differ already by zero count.
check(beta(1,5)==Fraction(1,5))
check(beta(2,4)==Fraction(1,20))
check(beta(3,3)==Fraction(1,30))
check(sum(q==0 for q in bs72[(2,4)])==1)

# Compare to C071 cubic reciprocal at same N,p: five 2|4 zeros.
phi71=phi_invpower(11,3)
rates71=unordered_split_rates(6,11,phi71)
bs71=by_size(6,rates71)
check(sum(q==0 for q in bs71[(2,4)])==5)
check(bs71[(2,4)]!=bs72[(2,4)])

# Compare to C070 inverse at N=6,p=7: again five 2|4 zeros.
phi70=phi_invpower(7,1)
rates70=unordered_split_rates(6,7,phi70)
bs70=by_size(6,rates70)
check(sum(q==0 for q in bs70[(2,4)])==5)
check(bs70[(2,4)]!=bs72[(2,4)])

# Exact pair-separation positivity for the finite C072 witness.
for a,b in combinations(range(N),2):
    for t in range(p):
        ra=phi72[(t+a)%p]
        rb=phi72[(t+b)%p]
        check(ra!=rb)
        us=[u for u in range(1,p) if (ra<u) != (rb<u)]
        check(len(us)>=1)

print("C072_GROWING_POWER_EXACT_CHECK")
print(f"assertions={ASSERTIONS}")
print("N6_params=d3_p11")
print("N6_1|5=" + ",".join(str(x) for x in bs72[(1,5)]))
print("N6_2|4=" + ",".join(str(x) for x in bs72[(2,4)]))
print("N6_3|3=" + ",".join(str(x) for x in bs72[(3,3)]))
print(f"N6_aggregate_1|5={agg[(1,5)]}")
print(f"N6_aggregate_2|4={agg[(2,4)]}")
print(f"N6_aggregate_3|3={agg[(3,3)]}")
print(f"N6_total_root_rate={total}")
print(f"N6_balanced_root_probability={agg[(3,3)]/total}")
print(f"N6_zero_count_2|4_C072={sum(q==0 for q in bs72[(2,4)])}")
print(f"N6_zero_count_2|4_C071={sum(q==0 for q in bs71[(2,4)])}")
print(f"N6_zero_count_2|4_C070={sum(q==0 for q in bs70[(2,4)])}")
print("ALL_EXACT_CHECKS_PASS")
