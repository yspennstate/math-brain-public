#!/usr/bin/env python3
"""
Exact verifier for HARD8-05 2026-09-16T10-31-10Z checkpoint.

Standard library only.  It verifies:
  * the saturated-subgroup obstruction for failed divisor portals;
  * the maximal (-1)-avoiding subgroups for several relevant moduli;
  * the explicit modulus-40 six-subgroup classification and budgets;
  * the symbolic reciprocal gcd relation for (2,5)/(5,2) on the finite hard-prime range;
  * the exact minimal portal-depth census for all primes n == 1 (mod 24)
    through 4,300,000, using every ordered coprime pair 1 <= a,u <= 8;
  * exact three-unit-fraction identities for every finite census witness.
No floating point, randomization, solver, or timeout inference is used.
"""
from math import gcd, isqrt
from collections import Counter

LIMIT = 4_300_000
TARGET_MODULI = [16,20,32,40,48,56,60,80,120]

def sieve(n):
    b = bytearray(b"\x01") * (n + 1)
    b[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if b[p]:
            b[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    ps = [i for i in range(2, n + 1) if b[i]]
    return b, ps

IS_PRIME, PRIMES = sieve(LIMIT)
SMALL = [p for p in PRIMES if p <= 7000]
HARD = [p for p in PRIMES if p % 24 == 1]

def factorint(n):
    out = {}
    x = n
    for p in SMALL:
        if p*p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out[p] = e
    if x > 1:
        out[x] = out.get(x, 0) + 1
    z = 1
    for p,e in out.items():
        z *= p**e
    assert z == n
    return out

def units_mod(m):
    return [r for r in range(1,m) if gcd(r,m) == 1]

def order_mod(r,m):
    assert gcd(r,m) == 1
    x = 1
    for k in range(1, 10_000):
        x = (x*r) % m
        if x == 1:
            return k
    raise AssertionError(("order loop", r, m))

def generated_subgroup(m, gens):
    H = {1}
    changed = True
    while changed:
        changed = False
        for x in tuple(H):
            for g in gens:
                y = (x*g) % m
                if y not in H:
                    H.add(y)
                    changed = True
    return frozenset(H)

def all_subgroups(m):
    U = units_mod(m)
    subs = {frozenset({1})}
    changed = True
    while changed:
        changed = False
        for H in tuple(subs):
            for g in U:
                if g not in H:
                    K = generated_subgroup(m, list(H) + [g])
                    if K not in subs:
                        subs.add(K)
                        changed = True
    return sorted(subs, key=lambda H: (len(H), tuple(sorted(H))))

def maximal_avoiding_minus_one(m):
    t = m - 1
    avoid = [H for H in all_subgroups(m) if t not in H]
    return [H for H in avoid if not any(H < K and t not in K for K in avoid)]

def quotient_coset_order(m, K, a):
    x = 1
    for k in range(1, 10_000):
        x = (x*a) % m
        if x in K:
            return k
    raise AssertionError("quotient order")

def verify_maximal_quotient_property(m, K):
    U = units_mod(m)
    idx = len(U) // len(K)
    assert idx & (idx - 1) == 0
    assert max(quotient_coset_order(m,K,a) for a in U) == idx
    order2_cosets = set()
    for a in U:
        if quotient_coset_order(m,K,a) == 2:
            order2_cosets.add(frozenset((a*k) % m for k in K))
    assert len(order2_cosets) == 1
    minus_coset = frozenset(((m-1)*k) % m for k in K)
    assert minus_coset in order2_cosets

def budget(m,K):
    return sum(max(order_mod(r,m)-2, 0) for r in units_mod(m) if r not in K)

def residue_exponents(fac,m):
    E = Counter()
    for p,e in fac.items():
        if gcd(p,m) == 1:
            E[p % m] += e
    return E

def saturated_group(fac,m):
    E = residue_exponents(fac,m)
    sats = [r for r,e in E.items() if e >= order_mod(r,m)-1]
    return generated_subgroup(m,sats), E

def divisor_witness(fac,m,target=None):
    if target is None:
        target = m-1
    dp = {1 % m: 1}
    for p,e in fac.items():
        if gcd(p,m) != 1:
            continue
        powers = [(1,1)]
        rr = 1
        aa = 1
        for _ in range(e):
            rr = (rr * (p % m)) % m
            aa *= p
            powers.append((rr,aa))
        nd = {}
        for r0,d0 in dp.items():
            for rr,aa in powers:
                r = (r0*rr) % m
                nd.setdefault(r, d0*aa)
        dp = nd
        if target in dp:
            return dp[target]
    return dp.get(target)

def portal_certificate(n,a,u):
    N = a*n + u
    m = 4*a*u
    fac = factorint(N)
    s = divisor_witness(fac,m)
    if s is None:
        return None
    assert N % s == 0
    assert s % m == m-1
    q = N // s
    assert (s+1) % m == 0
    t = (s+1)//m
    x = u*q*t
    y = a*n*q*t
    z = a*n*u*t
    assert min(x,y,z) > 0
    assert 4*x*y*z == n*(y*z + x*z + x*y)
    return (s,x,y,z)

TABLE = {}
for m in TARGET_MODULI:
    Ks = maximal_avoiding_minus_one(m)
    rows = []
    for K in Ks:
        verify_maximal_quotient_property(m,K)
        rows.append((len(units_mod(m))//len(K), budget(m,K), tuple(sorted(K))))
    TABLE[m] = rows

EXPECTED_K40 = {
    (1,11,21,31),
    (1,19,29,31),
    (1,3,7,9,21,23,27,29),
    (1,3,9,11,17,19,27,33),
    (1,7,9,11,13,19,23,37),
    (1,9,13,17,21,29,33,37),
}
assert {tuple(sorted(K)) for K in maximal_avoiding_minus_one(40)} == EXPECTED_K40
assert sorted((len(units_mod(40))//len(K), budget(40,K))
              for K in maximal_avoiding_minus_one(40)) == [(2,8)]*4 + [(4,16)]*2

def exhaustive_signature_check(m):
    U = [r for r in units_mod(m) if r != 1]
    caps = [order_mod(r,m)-1 for r in U]
    Ks = maximal_avoiding_minus_one(m)
    checked = 0
    failures = 0

    def rec(i, counts):
        nonlocal checked, failures
        if i == len(U):
            checked += 1
            R = {1}
            for r,e in zip(U,counts):
                vals = [1]
                x = 1
                for _ in range(e):
                    x = (x*r) % m
                    vals.append(x)
                R = {(a*b) % m for a in R for b in vals}
            fail = (m-1) not in R
            if fail:
                failures += 1
                sats = [r for r,e in zip(U,counts) if e >= order_mod(r,m)-1]
                H = generated_subgroup(m,sats)
                assert (m-1) not in H
                covers = [K for K in Ks if H <= K]
                assert covers
                assert any(all(e <= order_mod(r,m)-2
                               for r,e in zip(U,counts) if r not in K)
                           for K in covers)
            return
        for e in range(caps[i]+1):
            counts.append(e)
            rec(i+1,counts)
            counts.pop()
    rec(0,[])
    return checked, failures

SIG16 = exhaustive_signature_check(16)
SIG20 = exhaustive_signature_check(20)
assert SIG16 == (2048,79)
assert SIG20 == (2048,79)

PAIRS = sorted((max(a,u),a,u)
               for a in range(1,9) for u in range(1,9)
               if gcd(a,u) == 1)
DEPTH = Counter()
DEEP = []
for n in HARD:
    found = None
    for J,a,u in PAIRS:
        cert = portal_certificate(n,a,u)
        if cert is not None:
            found = (J,a,u,cert[0])
            break
    assert found is not None
    DEPTH[found[0]] += 1
    if found[0] >= 6:
        DEEP.append((n,found))
assert DEPTH == Counter({1:19162,2:16554,3:1695,4:211,5:82,6:10,7:1,8:1})
assert [x[0] for x in DEEP if x[1][0] == 7] == [345601]
assert [x[0] for x in DEEP if x[1][0] == 8] == [670849]

K40 = maximal_avoiding_minus_one(40)
FAIL40 = Counter()
EXC40 = {(2,5):Counter(), (5,2):Counter()}
for n in HARD:
    N1 = 2*n + 5
    N2 = 5*n + 2
    g = gcd(N1,N2)
    assert g == (7 if n % 7 == 1 else 1)
    assert 5*(N1//g) - 2*(N2//g) == 21//g
    assert gcd(N1//g,N2//g) == 1

    for a,u in ((2,5),(5,2)):
        N = a*n + u
        fac = factorint(N)
        if divisor_witness(fac,40) is not None:
            continue
        FAIL40[(a,u)] += 1
        H,E = saturated_group(fac,40)
        assert 39 not in H
        covers = [K for K in K40 if H <= K]
        assert covers
        eligible = []
        for K in covers:
            if all(E.get(r,0) <= order_mod(r,40)-2
                   for r in units_mod(40) if r not in K):
                exc = sum(E.get(r,0) for r in units_mod(40) if r not in K)
                eligible.append(exc)
        assert eligible
        EXC40[(a,u)][min(eligible)] += 1

assert FAIL40 == Counter({(2,5):24502,(5,2):32991})
assert EXC40[(2,5)] == Counter({0:18118,1:5969,2:388,3:27})
assert EXC40[(5,2)] == Counter({0:27623,1:5276,2:1,3:91})

for n in range(97, 20_000, 120):
    assert (n+3) % 20 == 0
    x=(n+3)//4
    y=n*(n+3)//10
    z=n*(n+3)//2
    assert 4*x*y*z == n*(y*z + x*z + x*y)
    s=2*n+5
    assert s % 40 == 39
    assert (2*n+5) % s == 0

print("hard primes <= 4,300,000:", len(HARD))
print("signature checks m16/m20:", SIG16, SIG20)
print("minimal portal depth counts:", dict(sorted(DEPTH.items())))
print("depth >= 6:", DEEP)
print("m40 failed portal counts:", dict(FAIL40))
print("m40 min-exception distributions:",
      {str(k):dict(sorted(v.items())) for k,v in EXC40.items()})
print("maximal -1-avoiding subgroup summary:")
for m in TARGET_MODULI:
    print(m, TABLE[m])
print("ALL CHECKS PASSED")
