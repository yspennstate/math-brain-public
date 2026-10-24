from fractions import Fraction
from itertools import combinations
from math import gcd
from functools import lru_cache

K = 14
DEN = K + 1
MAX_SPEED = 20

# ---------- Exact counterexample search at threshold 1/15 ----------

@lru_cache(maxsize=None)
def good_intervals(v):
    # On each period cell m/v <= t <= (m+1)/v, the exact good portion is
    # [(m+1/DEN)/v, (m+1-1/DEN)/v].
    return tuple(
        (Fraction(DEN*m + 1, DEN*v), Fraction(DEN*m + DEN - 1, DEN*v))
        for m in range(v)
    )

def intersect_unions(A, B):
    i = j = 0
    C = []
    while i < len(A) and j < len(B):
        lo = A[i][0] if A[i][0] >= B[j][0] else B[j][0]
        hi = A[i][1] if A[i][1] <= B[j][1] else B[j][1]
        if lo <= hi:
            if C and lo <= C[-1][1]:
                if hi > C[-1][1]:
                    C[-1] = (C[-1][0], hi)
            else:
                C.append((lo, hi))
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return C

def witness_set(vec):
    A = [(Fraction(0), Fraction(1))]
    for v in vec:
        A = intersect_unions(A, good_intervals(v))
        if not A:
            return []
    return A

checked = 0
counterexamples = []
tight = []
for vec in combinations(range(1, MAX_SPEED + 1), K):
    assert gcd(*vec) == 1
    checked += 1
    W = witness_set(vec)
    if not W:
        counterexamples.append(vec)
        break
    if all(a == b for a, b in W):
        tight.append((vec, tuple(a for a, _ in W)))

assert checked == 38760
assert counterexamples == []
assert len(tight) == 1
assert tight[0][0] == tuple(range(1, 15))
assert tight[0][1] == tuple(Fraction(a, 15) for a in (1,2,4,7,8,11,13,14))

# ---------- Exact count of Beck--Everett harmful relation shapes ----------
# For k=14, their concrete theorem gives a harmful relation m.n=0 with
# 0 < ||m||_1 <= 31. Harmful means sum(m_i) is odd; since -a == a mod 2,
# ||m||_1 is odd. Divide by gcd(m): because the gcd is then odd, harmful parity
# is retained. Coordinate permutation and independent speed-sign changes reduce
# a primitive relation to the multiset of its positive absolute coefficients.

@lru_cache(maxsize=None)
def partitions_exact(n, s):
    # Number of partitions of n into exactly s positive parts (order ignored).
    if s == 0:
        return 1 if n == 0 else 0
    if n <= 0 or n < s:
        return 0
    if s == 1:
        return 1
    return partitions_exact(n-1, s-1) + partitions_exact(n-s, s)

def mobius(n):
    x = n
    mu = 1
    p = 2
    while p*p <= x:
        if x % p == 0:
            x //= p
            mu = -mu
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        mu = -mu
    return mu

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def primitive_partition_count(n, s):
    # Möbius inversion over the common gcd of all parts.
    return sum(mobius(d) * partitions_exact(n//d, s)
               for d in divisors(n))

support_counts = {s: 0 for s in range(1, K+1)}
by_norm = {}
for n in range(1, 32, 2):
    c = 0
    for s in range(1, K+1):
        q = primitive_partition_count(n, s)
        assert q >= 0
        support_counts[s] += q
        c += q
    by_norm[n] = c

assert sum(support_counts.values()) == 17575
assert support_counts == {
    1: 1, 2: 106, 3: 437, 4: 994, 5: 1623, 6: 2067, 7: 2276,
    8: 2212, 9: 2016, 10: 1715, 11: 1424, 12: 1129, 13: 894, 14: 681
}
assert by_norm == {
    1: 1, 3: 2, 5: 6, 7: 14, 9: 27, 11: 55, 13: 100, 15: 166,
    17: 292, 19: 477, 21: 745, 23: 1187, 25: 1812, 27: 2708,
    29: 4056, 31: 5927
}
# Support one would say a*n_i=0 with a!=0 and n_i nonzero, impossible.
relation_shapes = sum(support_counts.values()) - support_counts[1]
assert relation_shapes == 17574

# ---------- Exact product-bound scale ----------
# B_14 = (105^13 / 14)^14 = 105^182 / 14^14.
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

num = 105 ** 182
den = 14 ** 14
P = 1
plist = []
p = 37
while P * den < num:
    if is_prime(p):
        plist.append(p)
        P *= p
    p += 1
assert len(plist) == 140
assert plist[-1] == 877
Pprev = P // plist[-1]
assert Pprev * den < num <= P * den

print('EXACT COUNTEREXAMPLE SEARCH')
print('k stationary-moving speeds =', K)
print('total runners =', K+1)
print('threshold = 1/15')
print('max speed =', MAX_SPEED)
print('distinct positive tuples checked =', checked)
print('counterexamples found =', len(counterexamples))
print('tight tuples found =', len(tight))
print('unique tight tuple =', tight[0][0])
print('its exact threshold witness times =', [str(x) for x in tight[0][1]])
print()
print('HARMFUL-RELATION SHAPE COUNT')
print('primitive absolute coefficient partitions, odd l1 <=31, support <=14 =', sum(support_counts.values()))
print('support-one impossible shapes =', support_counts[1])
print('nontrivial relation shapes after permutation/sign normalization =', relation_shapes)
print('support counts =', support_counts)
print('norm counts =', by_norm)
print()
print('PRODUCT-BOUND SCALE')
print('first primes >31 needed for exact product >= B_14 =', len(plist))
print('last such prime =', plist[-1])
print('previous product below threshold =', Pprev * den < num)
print('current product reaches threshold =', P * den >= num)
print('ALL_EXACT_CHECKS_PASS')
