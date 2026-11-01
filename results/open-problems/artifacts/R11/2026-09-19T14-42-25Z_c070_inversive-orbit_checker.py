from fractions import Fraction
from itertools import combinations
from math import factorial

ASSERTIONS = 0

def check(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return n == d
        d += 1
    return True

def next_prime_ge(n):
    p = max(2, n)
    while not is_prime(p):
        p += 1
    return p

def invp(x, p):
    x %= p
    if x == 0:
        return 0
    return pow(x, p-2, p)

def beta_rate(i, j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def canonical_splits(N):
    labels = tuple(range(N))
    out = []
    for r in range(1, N):
        for A in combinations(labels, r):
            if 0 in A:
                out.append(tuple(A))
    return out

def split_rate(N, A):
    p = next_prime_ge(N)
    labels = tuple(range(N))
    SA = set(A)
    SB = set(labels) - SA
    ans = Fraction(0)
    for u in range(1, p):
        c = Fraction(1, 2*u*(p-u))
        for t in range(p):
            red = {ell for ell in labels if invp(t+ell, p) < u}
            if red == SA or red == SB:
                ans += c
    return ans

def all_rates(N):
    return {A: split_rate(N, A) for A in canonical_splits(N)}

for N in range(2, 51):
    p = next_prime_ge(N)
    vals = [invp(x, p) for x in range(p)]
    check(sorted(vals) == list(range(p)), ("inv permutation", N, p))
    for a in range(N):
        for b in range(a+1, N):
            ya, yb = invp(a, p), invp(b, p)
            check(ya != yb, ("pair ranks distinct", N, p, a, b))
            lo, hi = sorted((ya, yb))
            check(lo < hi and 1 <= hi <= p-1, ("separating threshold exists", N, a, b, lo, hi))

small = {}
for N in range(2, 9):
    rr = all_rates(N)
    small[N] = rr
    check(len(rr) == 2**(N-1)-1, ("split count", N, len(rr)))
    check(all(v >= 0 for v in rr.values()), ("nonnegative rates", N))
    for a in range(N):
        for b in range(a+1, N):
            sep = sum(v for A,v in rr.items() if ((a in set(A)) != (b in set(A))))
            check(sep > 0, ("pair positive split rate", N, a, b, sep))

rr4 = small[4]
single4 = sorted(v for A,v in rr4.items() if min(len(A), 4-len(A)) == 1)
bal4 = sorted(v for A,v in rr4.items() if len(A) == 2)
check(single4 == [Fraction(1,3)]*4, ("N4 singleton", single4))
check(bal4 == [Fraction(1,6)]*3, ("N4 balanced", bal4))
c069_bal4 = [Fraction(0), Fraction(1,4), Fraction(1,4)]
check(bal4 != c069_bal4, ("distinct from C069", bal4))

rr5 = small[5]
for A,v in rr5.items():
    i, j = len(A), 5-len(A)
    check(v == beta_rate(i,j), ("N5 CTCS exact", A, v, beta_rate(i,j)))

rr6 = small[6]
by_size6 = {}
for s in (1,2,3):
    by_size6[s] = sorted(v for A,v in rr6.items() if min(len(A),6-len(A)) == s)

expected1 = sorted([Fraction(1,6)]*2 + [Fraction(13,60)]*4)
expected2 = sorted([Fraction(0)]*5 + [Fraction(1,20)]*7 + [Fraction(2,15)]*3)
expected3 = sorted([Fraction(0)]*7 + [Fraction(1,12)]*2 + [Fraction(1,6)])
check(by_size6[1] == expected1, ("N6 1|5 multiset", by_size6[1]))
check(by_size6[2] == expected2, ("N6 2|4 multiset", by_size6[2]))
check(by_size6[3] == expected3, ("N6 3|3 multiset", by_size6[3]))
check(beta_rate(2,4) == Fraction(1,20), "beta24")
check(beta_rate(3,3) == Fraction(1,30), "beta33")
check(any(v == 0 for v in by_size6[2]), "N6 zero 2|4 witness")
check(any(v == 0 for v in by_size6[3]), "N6 zero 3|3 witness")
check(by_size6[2] != [beta_rate(2,4)]*15, "N6 differs from source 2|4")
check(by_size6[3] != [beta_rate(3,3)]*10, "N6 differs from source 3|3")

agg1 = sum(by_size6[1], Fraction(0))
agg2 = sum(by_size6[2], Fraction(0))
agg3 = sum(by_size6[3], Fraction(0))
check((agg1,agg2,agg3) == (Fraction(6,5), Fraction(3,4), Fraction(1,3)),
      ("N6 aggregate classes", agg1,agg2,agg3))
total6 = agg1+agg2+agg3
check(total6 == Fraction(137,60), ("N6 exit", total6))

for N in range(2, 11):
    src_total = Fraction(0)
    for A in canonical_splits(N):
        src_total += beta_rate(len(A), N-len(A))
    harmonic = sum((Fraction(1,r) for r in range(1,N)), Fraction(0))
    check(src_total == harmonic, ("source total", N, src_total, harmonic))

print("R11-I0054-U049/C070 exact self-check")
print("ASSERTIONS={}".format(ASSERTIONS))
print("N4_singleton_multiset={}".format(",".join(str(x) for x in single4)))
print("N4_balanced_multiset={}".format(",".join(str(x) for x in bal4)))
print("C069_N4_balanced_multiset=0,1/4,1/4")
print("N6_1v5_multiset={}".format(",".join(str(x) for x in by_size6[1])))
print("N6_2v4_multiset={}".format(",".join(str(x) for x in by_size6[2])))
print("N6_3v3_multiset={}".format(",".join(str(x) for x in by_size6[3])))
print("N6_aggregate_rates={},{},{}".format(agg1,agg2,agg3))
print("N6_total_exit={}".format(total6))
print("source_beta_2v4={}".format(beta_rate(2,4)))
print("source_beta_3v3={}".format(beta_rate(3,3)))
print("ALL_EXACT_CHECKS_PASS")
