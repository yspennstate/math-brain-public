from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

ASSERTIONS = 0

def check(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
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

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def phi_power_inv(x,p,r):
    x %= p
    if x == 0:
        return 0
    return pow(x, -r, p)

def source_B(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def unordered_splits(labels):
    labels = tuple(labels)
    whole = set(labels)
    for r in range(1,len(labels)):
        for A0 in combinations(labels,r):
            A = set(A0)
            B = whole - A
            ta, tb = tuple(sorted(A)), tuple(sorted(B))
            if ta < tb:
                yield frozenset(A), frozenset(B)

def split_rate(labels,p,r,A):
    labels = tuple(labels)
    A = frozenset(A)
    B = frozenset(set(labels)-set(A))
    total = Fraction(0)
    for u in range(1,p):
        w = Fraction(1,2*u*(p-u))
        for t in range(p):
            red = {ell for ell in labels if phi_power_inv(t+ell,p,r) < u}
            if (A <= red and B.isdisjoint(red)) or (B <= red and A.isdisjoint(red)):
                total += w
    return total

def split_rate_custom_phi(labels,p,perm,A):
    labels = tuple(labels)
    A = frozenset(A)
    B = frozenset(set(labels)-set(A))
    total = Fraction(0)
    for u in range(1,p):
        w = Fraction(1,2*u*(p-u))
        for t in range(p):
            red = {ell for ell in labels if perm[(t+ell)%p] < u}
            if (A <= red and B.isdisjoint(red)) or (B <= red and A.isdisjoint(red)):
                total += w
    return total

# Cubic power-inverse is a permutation on primes p == 2 mod 3, and each pair is separable.
primes = [p for p in range(2,102) if is_prime(p) and p % 3 == 2]
for p in primes:
    values = [phi_power_inv(x,p,3) for x in range(p)]
    check(sorted(values) == list(range(p)), ("permutation",p))
    for a in range(p):
        for b in range(a+1,p):
            separated = False
            for t in range(p):
                va = phi_power_inv(t+a,p,3)
                vb = phi_power_inv(t+b,p,3)
                lo, hi = sorted((va,vb))
                u = max(1,lo+1)
                if u <= p-1 and u <= hi:
                    separated = True
                    break
            check(separated, ("pair-separation",p,a,b))

# Total proposal-clock intensity is H_{p-1}.
for p in primes[:6]:
    total = sum((Fraction(1,2*u*(p-u)) for u in range(1,p) for _ in range(p)), Fraction(0))
    check(total == H(p-1), ("total-clock",p,total,H(p-1)))

# Exact N=4 witness for C071: p=5, r=3.
labels = tuple(range(4))
balanced, singletons = [], []
for A,B in unordered_splits(labels):
    q = split_rate(labels,5,3,A)
    if len(A) == len(B) == 2:
        balanced.append(q)
    elif sorted((len(A),len(B))) == [1,3]:
        singletons.append(q)
balanced.sort()
singletons.sort()
check(balanced == [Fraction(0),Fraction(1,6),Fraction(1,3)], balanced)
check(singletons == [Fraction(1,4),Fraction(1,4),Fraction(5,12),Fraction(5,12)], singletons)
root_total = sum(balanced+singletons, Fraction(0))
check(root_total == Fraction(11,6), root_total)
balanced_total = sum(balanced, Fraction(0))
check(balanced_total == Fraction(1,2), balanced_total)
root_bal_prob = balanced_total/root_total
check(root_bal_prob == Fraction(3,11), root_bal_prob)
check(balanced != [Fraction(1,6)]*3, "source/C070 witness")
check(balanced != [Fraction(0),Fraction(1,4),Fraction(1,4)], "C069 witness")
nz = [x for x in balanced if x]
check(nz[1]/nz[0] == 2, nz)

# Full-ambient aggregate split-size identity for C071 at p=5,11.
for p in [5,11]:
    labels = tuple(range(p))
    bysize = {}
    for A,B in unordered_splits(labels):
        i,j = sorted((len(A),len(B)))
        q = split_rate(labels,p,3,A)
        bysize[(i,j)] = bysize.get((i,j),Fraction(0)) + q
    for (i,j),qtot in bysize.items():
        expected = Fraction(p,i*j)
        check(qtot == expected, ("aggregate",p,i,j,qtot,expected))
        count = comb(p,i)
        check(qtot == count*source_B(i,j), ("aggregate-beta",p,i,j,qtot,count*source_B(i,j)))

# B25 finite audit: for every one of the 5! permutations, the full p=5 aggregate
# split-size hazards are permutation-independent.
p = 5
labels = tuple(range(p))
for perm in permutations(range(p)):
    bysize = {}
    for A,B in unordered_splits(labels):
        i,j = sorted((len(A),len(B)))
        q = split_rate_custom_phi(labels,p,perm,A)
        bysize[(i,j)] = bysize.get((i,j),Fraction(0)) + q
    for (i,j),qtot in bysize.items():
        expected = Fraction(p,i*j)
        check(qtot == expected, ("all-permutations",perm,i,j,qtot,expected))

print("R11-I0054-U050/C071 exact self-check")
print("ASSERTIONS={}".format(ASSERTIONS))
print("N4_singleton_multiset={}".format(",".join(map(str,singletons))))
print("N4_balanced_multiset={}".format(",".join(map(str,balanced))))
print("N4_total_root_rate={}".format(root_total))
print("N4_root_P_2v2={}".format(root_bal_prob))
print("source_C070_N4_balanced_multiset=1/6,1/6,1/6")
print("C069_N4_balanced_multiset=0,1/4,1/4")
print("FULL_AMBIENT_AGGREGATE_P5=1|4:5/4,2|3:5/6")
print("ALL_EXACT_CHECKS_PASS")
