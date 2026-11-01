#!/usr/bin/env python3
"""Exact verifier for HARD8-05 exponent-four divisor portals.

Standard library only. No floating point is used in any mathematical check.
"""

from collections import Counter
from itertools import product
from math import gcd, isqrt

MAX_N = 4_300_000
RES16 = (3, 5, 7, 9, 11, 13, 15)
CAP16 = (3, 3, 1, 1, 3, 3, 1)

MIN_SUCC16 = (
    (0,0,0,0,0,0,1),
    (0,0,0,0,1,1,0),
    (0,0,1,0,0,2,0),
    (0,0,1,0,2,0,0),
    (0,0,1,1,0,0,0),
    (0,1,0,0,3,0,0),
    (0,1,0,1,1,0,0),
    (0,2,1,0,0,0,0),
    (0,3,0,0,1,0,0),
    (1,0,0,0,0,3,0),
    (1,0,0,1,0,1,0),
    (1,1,0,0,0,0,0),
    (2,0,1,0,0,0,0),
    (3,0,0,0,0,1,0),
)

MAX_FAIL16 = (
    (0,1,1,0,0,1,0),
    (0,1,1,0,1,0,0),
    (0,2,0,0,2,0,0),
    (0,3,0,1,0,3,0),
    (1,0,1,0,0,1,0),
    (1,0,1,0,1,0,0),
    (2,0,0,0,0,2,0),
    (3,0,0,1,3,0,0),
)

MAP16TO20 = {3:3, 5:13, 7:11, 9:9, 11:7, 13:17, 15:19}
RES20 = tuple(MAP16TO20[r] for r in RES16)


def reach_from_signature(sig, modulus=16, residues=RES16, target=15):
    reachable = {1}
    for r, e in zip(residues, sig):
        vals = {pow(r, j, modulus) for j in range(e + 1)}
        reachable = {a * b % modulus for a in reachable for b in vals}
    return target in reachable


def leq(a, b):
    return all(x <= y for x, y in zip(a, b))


def verify_posets():
    all_sigs = list(product(*[range(c + 1) for c in CAP16]))
    succ = [s for s in all_sigs if reach_from_signature(s)]
    fail = [s for s in all_sigs if not reach_from_signature(s)]

    mins = []
    for s in succ:
        minimal = True
        for i, x in enumerate(s):
            if x:
                t = s[:i] + (x - 1,) + s[i+1:]
                if reach_from_signature(t):
                    minimal = False
                    break
        if minimal:
            mins.append(s)

    maxs = []
    for s in fail:
        maximal = True
        for i, cap in enumerate(CAP16):
            if s[i] < cap:
                t = s[:i] + (s[i] + 1,) + s[i+1:]
                if not reach_from_signature(t):
                    maximal = False
                    break
        if maximal:
            maxs.append(s)

    assert tuple(mins) == MIN_SUCC16
    assert tuple(maxs) == MAX_FAIL16

    for s in all_sigs:
        if reach_from_signature(s):
            assert any(leq(m, s) for m in MIN_SUCC16)
        else:
            assert any(leq(s, m) for m in MAX_FAIL16)

        assert reach_from_signature(s, 16, RES16, 15) == \
               reach_from_signature(s, 20, RES20, 19)

    return len(all_sigs), len(succ), len(fail)


def sieve(n):
    bs = bytearray(b"\x01") * (n + 1)
    bs[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if bs[p]:
            bs[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return bs


SMALL_PRIME_MASK = sieve(isqrt(6 * MAX_N + 10) + 2)
TRIAL_PRIMES = [p for p in range(2, len(SMALL_PRIME_MASK)) if SMALL_PRIME_MASK[p]]


def factorint(n):
    out = {}
    x = n
    for p in TRIAL_PRIMES:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out[p] = e
        if x == 1:
            break
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def target_divisor_exists(N, modulus):
    reachable = {1 % modulus}
    for p, e in factorint(N).items():
        if gcd(p, modulus) != 1:
            continue
        vals = []
        cur = 1
        for _ in range(e + 1):
            vals.append(cur)
            cur = cur * (p % modulus) % modulus
        reachable = {a * b % modulus for a in reachable for b in vals}
    return (modulus - 1) % modulus in reachable


def portal_success(n, a, u):
    return target_divisor_exists(a * n + u, 4 * a * u)


def exponent_counter(N, modulus):
    E = Counter()
    for p, e in factorint(N).items():
        E[p % modulus] += e
    return E


def mod16_box_failure(N):
    assert N % 2 == 1
    E = exponent_counter(N, 16)
    if E[15]:
        return False
    boxes = (
        ({5,7,13}, {5:1,13:1}),
        ({5,7,11}, {5:1,11:1}),
        ({5,11}, {5:2,11:2}),
        ({5,9,13}, {}),
        ({3,7,13}, {3:1,13:1}),
        ({3,7,11}, {3:1,11:1}),
        ({3,13}, {3:2,13:2}),
        ({3,9,11}, {}),
    )
    support = {r for r, e in E.items() if e and r != 1}
    return any(
        support <= allowed and all(E[r] <= b for r, b in bounds.items())
        for allowed, bounds in boxes
    )


def mod20_box_failure(N):
    assert gcd(N, 20) == 1
    E = exponent_counter(N, 20)
    if E[19]:
        return False
    boxes = (
        ({13,11,17}, {13:1,17:1}),
        ({13,11,7}, {13:1,7:1}),
        ({13,7}, {13:2,7:2}),
        ({13,9,17}, {}),
        ({3,11,17}, {3:1,17:1}),
        ({3,11,7}, {3:1,7:1}),
        ({3,17}, {3:2,17:2}),
        ({3,9,7}, {}),
    )
    support = {r for r, e in E.items() if e and r != 1}
    return any(
        support <= allowed and all(E[r] <= b for r, b in bounds.items())
        for allowed, bounds in boxes
    )


def special_L_failure(L):
    """Corrected exact failure criterion for L=(5n+1)/2."""
    E = exponent_counter(L, 20)
    support = {r for r, e in E.items() if e and r != 1}
    kernel = support <= {3,7,9}
    even11 = support <= {3,11} and E[3] == 1 and E[11] % 2 == 0
    return kernel or even11


def special_K_failure(n):
    """Corrected exact failure criterion for K=(n+5)/2 by n mod 40."""
    K = (n + 5) // 2
    E = exponent_counter(K, 20)
    support = {r for r, e in E.items() if e and r != 1}
    r = n % 40

    if r == 1:
        return (support <= {3,7,9}) or \
               (support <= {3,11} and E[3] == 1 and E[11] % 2 == 0)

    if r == 9:
        return (support <= {3,7,9}) or \
               (support <= {3,17} and E[3] == 1 and E[17] == 2)

    if r == 17:
        branch_a = support <= {3,11,17} and \
                   E[3] == 1 and E[17] == 1 and E[11] % 2 == 0
        branch_b = support <= {3,7,11} and \
                   E[3] == 1 and E[7] == 1 and E[11] % 2 == 1
        return branch_a or branch_b

    if r == 33:
        return False

    raise AssertionError(("unexpected hard-prime class mod 40", r))


def portal_witness(n, a, u):
    N = a * n + u
    modulus = 4 * a * u
    divisors = [1]
    for p, e in factorint(N).items():
        old = divisors
        divisors = []
        pp = 1
        for _ in range(e + 1):
            divisors.extend(d * pp for d in old)
            pp *= p

    for s in sorted(divisors):
        if s % modulus == modulus - 1:
            q = N // s
            t = (s + 1) // modulus
            x = u * q * t
            y = a * n * q * t
            z = a * n * u * t
            assert 4 * x * y * z == n * (y*z + x*z + x*y)
            return s, q, t, (x, y, z)
    return None


def first_pair(n, J=15):
    for M in range(1, J + 1):
        for a in range(1, M + 1):
            for u in range(1, M + 1):
                if max(a, u) != M or gcd(a, u) != 1:
                    continue
                if portal_success(n, a, u):
                    return a, u
    return None


def main():
    poset_counts = verify_posets()

    primes_mask = sieve(MAX_N)
    hard = [n for n in range(2, MAX_N + 1)
            if primes_mask[n] and n % 24 == 1]
    assert len(hard) == 37716

    for n in hard:
        assert portal_success(n, 1, 4) == (not mod16_box_failure(n + 4))
        assert portal_success(n, 4, 1) == (not mod16_box_failure(4*n + 1))

        assert gcd(n + 4, 4*n + 1) == (5 if n % 5 == 1 else 1)

        K = (n + 5) // 2
        L = (5*n + 1) // 2
        assert gcd(K, L) == 3
        A, B = K // 3, L // 3
        assert gcd(A, B) == 1 and B == 5*A - 4

        assert portal_success(n, 1, 5) == (not mod20_box_failure(K))
        assert portal_success(n, 5, 1) == (not mod20_box_failure(L))
        assert special_K_failure(n) == mod20_box_failure(K)
        assert special_L_failure(L) == mod20_box_failure(L)

        if n % 40 == 33:
            assert K % 20 == 19 and portal_success(n, 1, 5)

    pairs9 = [
        (1,1),(1,2),(2,1),(1,3),(3,1),
        (1,6),(6,1),(2,3),(3,2),
    ]
    miss9 = [n for n in hard
             if not any(portal_success(n, a, u) for a, u in pairs9)]
    assert len(miss9) == 122

    newpairs = [(1,4),(4,1),(1,5),(5,1)]
    counts = {pair: sum(portal_success(n, *pair) for n in miss9)
              for pair in newpairs}
    assert counts == {(1,4):41, (4,1):31, (1,5):58, (5,1):59}

    residual = [
        n for n in miss9
        if not any(portal_success(n, *pair) for pair in newpairs)
    ]
    expected = [
        345601, 670849, 1083289, 1113961, 1672609,
        1740481, 2762761, 2764441, 2914921, 3819481,
    ]
    assert residual == expected

    expected_cert = {
        345601: ((7,2),279),
        670849: ((1,8),319),
        1083289: ((2,5),599),
        1113961: ((6,5),61319),
        1672609: ((3,5),59),
        1740481: ((3,4),3311),
        2762761: ((2,5),119),
        2764441: ((5,2),119),
        2914921: ((4,5),79),
        3819481: ((3,4),143),
    }

    certs = {}
    for n in residual:
        pair = first_pair(n, 15)
        witness = portal_witness(n, *pair)
        assert witness is not None
        certs[n] = (pair, witness[0])
        assert certs[n] == expected_cert[n]

    print("mod16 signatures/success/failure:", poset_counts)
    print("mod20 C4xC2 transfer: OK")
    print("full-range exact box/special-branch checks: OK")
    print("hard-class primes <= 4,300,000:", len(hard))
    print("nine-portal residuals:", len(miss9))
    print("new portal counts:", counts)
    print("thirteen-portal union:", len(hard) - len(residual))
    print("thirteen-portal residuals:", residual)
    print("residual exact certificates:", certs)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
