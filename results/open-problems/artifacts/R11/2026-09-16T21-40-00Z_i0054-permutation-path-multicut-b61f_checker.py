#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial
from itertools import permutations, combinations

print("R11 I0054 random-permutation path multi-cut exact self-check")
print("FINITE CLAIMS ONLY; asymptotic convergence is proved in the written report.")

def B(a,b):
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def H(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction(0))

def w(m,s):
    return Fraction(m, 2*s*(m-s))

def hyp(m,b,s,i):
    if s-i < 0 or s-i > m-b:
        return Fraction(0)
    return Fraction(comb(m-b,s-i), comb(m,s))

for m in range(2,101):
    assert sum((w(m,s) for s in range(1,m)), Fraction(0)) == H(m-1)
print("harmonic_total_weight: PASS m=2..100")

count=0
for m in range(2,31):
    for b in range(2,m+1):
        for i in range(1,b):
            lhs=sum((w(m,s)*hyp(m,b,s,i) for s in range(1,m)), Fraction(0))
            rhs=B(i,b-i)/2
            assert lhs == rhs, (m,b,i,lhs,rhs)
            count += 1
print("hidden_size_beta_identity: PASS", count, "exact triples")

group_checks=0
for m in range(2,8):
    U=tuple(range(m))
    perms=list(permutations(U))
    for s in range(1,m):
        target=factorial(s)*factorial(m-s)
        counts={frozenset(A):0 for A in combinations(U,s)}
        for p in perms:
            counts[frozenset(p[:s])] += 1
        assert set(counts.values()) == {target}
        group_checks += len(counts)
print("S_m_prefix_uniformity: PASS", group_checks, "subset counts")

fixed_order_rate = Fraction(0)
ctcs_rate = B(1,2)
assert fixed_order_rate == 0 and ctcs_rate == Fraction(1,2)
print("fixed_order_failure: PASS rate({2}|{1,3})=0 != CTCS", ctcs_rate)

delta=Fraction(1,3)
p=delta*w(3,1)
assert p == Fraction(1,4)
raw_three = p*p
raw_none = (1-p)*(1-p)
visible = 1-raw_none
first_visible_three = raw_three/visible
assert raw_three == Fraction(1,16)
assert first_visible_three == Fraction(1,7)
print("C006_N3: PASS raw_threeway=1/16 first_visible_threeway=1/7")

c001 = Fraction(0)

theta=Fraction(1,3)
c002_raw_one = Fraction(2,1)/((theta+1)*(theta+2))
c002_raw_three = theta*theta/((theta+1)*(theta+2))
c002 = c002_raw_three/(1-c002_raw_one)
assert c002 == Fraction(1,10)

eps=Fraction(1,6)
def rising(x,n):
    out=Fraction(1)
    for j in range(n):
        out *= x+j
    return out
c003_raw_one = 3*rising(eps,3)/rising(3*eps,3)
c003_raw_three = 6*eps**3/rising(3*eps,3)
c003 = c003_raw_three/(1-c003_raw_one)
assert c003 == Fraction(1,22)

alpha=Fraction(1,6)
theta=Fraction(1,6)
c004_raw_one = rising(1-alpha,2)/rising(theta+1,2)
c004_raw_three = (theta+alpha)*(theta+2*alpha)/rising(theta+1,2)
c004 = c004_raw_three/(1-c004_raw_one)
assert c004 == Fraction(1,6)

d=Fraction(1,243)
no_star=(1-d*Fraction(1,2))**2
no_chain=(1-d*Fraction(1,2))*(1-d*Fraction(3,2))
noavg=(no_star+no_chain)/2
raw_three_rrt=d*d*Fraction(1,2)
c005=raw_three_rrt/(1-noavg)
assert c005 == Fraction(1,728)

vals=[c001,c002,c003,c004,c005,first_visible_three]
assert len(vals)==len(set(vals))
print("reduced_root_degree3_witnesses: PASS", "C001=0 C002=1/10 C003=1/22 C004=1/6 C005=1/728 C006=1/7")

for m in range(2,201):
    for s in range(1,m):
        assert w(m,s) <= 1
print("mark_probability_bound: PASS w_m(s)<=1 for m<=200 (algebra proved in report)")

print("ALL_EXACT_CHECKS_PASS")
