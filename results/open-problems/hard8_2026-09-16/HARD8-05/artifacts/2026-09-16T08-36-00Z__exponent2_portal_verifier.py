#!/usr/bin/env python3
"""
HARD8-05 exact verifier for the maximal exponent-two portal checkpoint.

Standard library only; all arithmetic is exact integer arithmetic.

Checks:
  1. for multiples of 4 in a finite sanity range, every unit squares to 1
     exactly for divisors of 24;
  2. direct divisor search agrees with the closed support-subgroup criteria
     for all nine portals on every prime n == 1 (mod 24) through 720001;
  3. exact nine-portal coverage counts through 720001 and 4,300,000;
  4. reciprocal gcd/Bezout formulas;
  5. all nine-portal misses through 4,300,000 are solved by the complete
     fixed-a=1 Type-II slice, with the stated minimal-u distribution;
  6. the exact n=2369929, u=91, s=727 certificate;
  7. stated branch-forcing corollaries.
"""
from math import gcd, isqrt
from collections import Counter

XU_LIMIT = 720_001
EXT_LIMIT = 4_300_000
NINE = (
    (1, 1),
    (1, 2), (2, 1),
    (1, 3), (3, 1),
    (1, 6), (6, 1), (2, 3), (3, 2),
)

H6 = {1, 5, 7, 11}
H4 = {1, 5, 13, 17}
H3 = {1, 7, 13, 19}
H12_4 = {1, 5}
H12_3 = {1, 7}

EXPECTED_COUNTS_EXT = {
    (1, 1): 19162,
    (1, 2): 23032,
    (2, 1): 23390,
    (1, 3): 16637,
    (3, 1): 17314,
    (1, 6): 11552,
    (6, 1): 12715,
    (2, 3): 11307,
    (3, 2): 11458,
}
EXPECTED_MIN_U = {
    4: 41,
    5: 35,
    7: 5,
    8: 11,
    9: 8,
    10: 4,
    11: 3,
    12: 3,
    13: 1,
    14: 3,
    17: 2,
    18: 2,
    20: 1,
    37: 2,
    91: 1,
}
EXPECTED_MISSES_XU = [
    3361, 59809, 66529, 67369, 71569, 90841, 96769, 97561,
    101641, 163249, 174169, 196561, 290761, 314161, 317209,
    345601, 384001, 384049, 384841, 388081, 409081, 422041,
    476401, 514201, 522601, 530209, 558721, 585841, 601969,
    608161, 649321, 670849, 686449, 688969, 706729,
]


def sieve(N):
    isprime = bytearray(b"\x01") * (N + 1)
    isprime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(N) + 1):
        if isprime[p]:
            start = p * p
            isprime[start:N + 1:p] = b"\x00" * (((N - start) // p) + 1)
    primes = [i for i in range(2, N + 1) if isprime[i]]
    return isprime, primes


ISPRIME, PRIMES = sieve(EXT_LIMIT)
SMALL = [p for p in PRIMES if p <= isqrt(6 * EXT_LIMIT + 10)]


def factor_exp(n):
    out = []
    x = n
    for p in SMALL:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out.append((p, e))
    if x > 1:
        out.append((x, 1))
    return out


def prime_support(n):
    return [p for p, _ in factor_exp(n)]


def divisors(n):
    ds = [1]
    for p, e in factor_exp(n):
        old = ds[:]
        pe = 1
        for _ in range(e):
            pe *= p
            ds.extend(d * pe for d in old)
    return ds


def direct_fire(n, a, u):
    m = 4 * a * u
    N = a * n + u
    return any(d % m == m - 1 for d in divisors(N))


def closed_failure(n, a, u):
    au = a * u
    N = a * n + u
    if au == 1:
        assert (a, u) == (1, 1)
        assert N % 2 == 0 and (N // 2) % 2 == 1
        return all(p % 4 == 1 for p in prime_support(N // 2))
    if au == 2:
        return all(p % 8 in (1, 3) for p in prime_support(N))
    if au == 3:
        assert N % 4 == 0 and (N // 4) % 2 == 1
        O = N // 4
        supp = {p % 12 for p in prime_support(O)}
        assert n % 48 in (1, 25)
        if n % 48 == 25:
            return supp <= H12_3
        return (supp <= H12_4) or (supp <= H12_3)
    if au == 6:
        supp = {p % 24 for p in prime_support(N)}
        if a + u == 5:
            return (supp <= H6) or (supp <= H4)
        assert a + u == 7
        return (supp <= H6) or (supp <= H3)
    raise AssertionError((a, u))


def closed_fire(n, a, u):
    return not closed_failure(n, a, u)


def exact_u_bound_a1(n):
    # largest u satisfying 4u^2 - 2u <= n
    u = (1 + isqrt(1 + 4 * n)) // 4
    while 4 * (u + 1) * (u + 1) - 2 * (u + 1) <= n:
        u += 1
    while 4 * u * u - 2 * u > n:
        u -= 1
    return u


def min_u_a1(n):
    U = exact_u_bound_a1(n)
    for u in range(1, U + 1):
        mod = 4 * u
        for s in divisors(n + u):
            if s % mod == mod - 1:
                return u, s
    return None


def subgroup_mod(residues, m):
    H = {1}
    changed = True
    residues = set(residues)
    while changed:
        changed = False
        for x in list(H):
            for r in residues:
                y = (x * r) % m
                if y not in H:
                    H.add(y)
                    changed = True
    return H


def verify_abstract_group_claims():
    for m in range(4, 241, 4):
        units = [x for x in range(1, m) if gcd(x, m) == 1]
        exp2 = all((x * x) % m == 1 for x in units)
        assert exp2 == (24 % m == 0), m

    # Exhaust support subsets for mod 8, 12, 24 classifications.
    U8 = [1, 3, 5, 7]
    for mask in range(1 << len(U8)):
        S = {U8[i] for i in range(len(U8)) if (mask >> i) & 1}
        H = subgroup_mod(S, 8)
        if 3 in H:
            assert (7 not in H) == (S <= {1, 3})

    U12 = [1, 5, 7, 11]
    for mask in range(1 << len(U12)):
        S = {U12[i] for i in range(len(U12)) if (mask >> i) & 1}
        H = subgroup_mod(S, 12)
        if 7 in H:
            assert (11 not in H) == (S <= {1, 7})
        if 1 in H:
            predicted = (S <= {1, 5}) or (S <= {1, 7})
            assert (11 not in H) == predicted

    U24 = [1, 5, 7, 11, 13, 17, 19, 23]
    for mask in range(1 << len(U24)):
        S = {U24[i] for i in range(len(U24)) if (mask >> i) & 1}
        H = subgroup_mod(S, 24)
        if 5 in H:
            assert (23 not in H) == ((S <= H6) or (S <= H4))
        if 7 in H:
            assert (23 not in H) == ((S <= H6) or (S <= H3))


def verify_reciprocal_identities(n):
    assert gcd(n + 2, 2 * n + 1) == 3
    A = (n + 2) // 3
    B = (2 * n + 1) // 3
    assert gcd(A, B) == 1 and 2 * A - B == 1

    g5 = gcd(2 * n + 3, 3 * n + 2)
    expected5 = 5 if n % 5 == 1 else 1
    assert g5 == expected5
    A = (2 * n + 3) // g5
    B = (3 * n + 2) // g5
    assert gcd(A, B) == 1 and 3 * A - 2 * B == 5 // g5

    g35 = gcd(n + 6, 6 * n + 1)
    expected35 = (5 if n % 5 == 4 else 1) * (7 if n % 7 == 1 else 1)
    assert g35 == expected35
    A = (n + 6) // g35
    B = (6 * n + 1) // g35
    assert gcd(A, B) == 1 and 6 * A - B == 35 // g35


def branch_sets_7(N):
    supp = {p % 24 for p in prime_support(N)}
    ans = set()
    if supp <= H6:
        ans.add("H6")
    if supp <= H3:
        ans.add("H3")
    return ans


def main():
    verify_abstract_group_claims()

    xu = [p for p in PRIMES if p <= XU_LIMIT and p % 24 == 1]
    ext = [p for p in PRIMES if p <= EXT_LIMIT and p % 24 == 1]
    assert len(xu) == 7185
    assert len(ext) == 37716

    # Direct-vs-closed verification in Xu's complete range.
    for n in xu:
        verify_reciprocal_identities(n)
        for a, u in NINE:
            assert direct_fire(n, a, u) == closed_fire(n, a, u), (n, a, u)

    misses_xu = [n for n in xu if not any(closed_fire(n, a, u) for a, u in NINE)]
    assert misses_xu == EXPECTED_MISSES_XU
    assert len(misses_xu) == 35

    counts = {pair: 0 for pair in NINE}
    misses = []
    for n in ext:
        verify_reciprocal_identities(n)
        fired = False
        for pair in NINE:
            f = closed_fire(n, *pair)
            counts[pair] += int(f)
            fired = fired or f
        if not fired:
            misses.append(n)

    assert counts == EXPECTED_COUNTS_EXT, counts
    assert len(misses) == 122
    assert len(ext) - len(misses) == 37594

    # Branch-forcing consequences.
    for n in misses:
        b1 = branch_sets_7(n + 6)
        b2 = branch_sets_7(6 * n + 1)
        assert b1 and b2
        if n % 5 == 4:
            assert b1 == {"H6"} and b2 == {"H6"}
        if n % 11 == 5:
            assert b1 == {"H6"}
        if n % 11 == 9:
            assert b2 == {"H6"}

    mus = []
    for n in misses:
        got = min_u_a1(n)
        assert got is not None, n
        mus.append((n, got[0], got[1]))

    dist = Counter(u for _, u, _ in mus)
    assert dict(sorted(dist.items())) == EXPECTED_MIN_U, dist
    hard = [row for row in mus if row[1] == 91]
    assert hard == [(2369929, 91, 727)], hard
    n, u, s = hard[0]
    assert (n + u) % s == 0
    assert s % (4 * u) == 4 * u - 1

    print("abstract exponent-two group checks: OK")
    print("Xu hard-class count:", len(xu))
    print("Xu nine-portal union:", len(xu) - len(misses_xu))
    print("Xu nine-portal misses:", len(misses_xu))
    print("extended hard-class count:", len(ext))
    print("portal counts:", counts)
    print("extended nine-portal union:", len(ext) - len(misses))
    print("extended nine-portal misses:", len(misses))
    print("minimal-u distribution on misses:", dict(sorted(dist.items())))
    print("maximal observed minimal-u certificate:", hard[0])
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
