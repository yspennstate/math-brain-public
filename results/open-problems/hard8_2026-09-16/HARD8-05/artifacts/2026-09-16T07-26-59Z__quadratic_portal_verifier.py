#!/usr/bin/env python3
"""
HARD8-05 exact verifier for the 2026-09-16T07-26-59Z checkpoint.

No floating-point arithmetic and no third-party packages are used.

Checks:
1. the support-subgroup classification of divisor residues modulo 24;
2. the N==5 mod 24 and N==7 mod 24 failure subgroup classifications;
3. direct divisor search vs. the closed factor-support criteria for every
   prime n == 1 mod 24 through 720001;
4. exact coverage counts for portals (a,u)=(2,1) and (6,1);
5. the complete fixed-a=1 Type-II search for every prime n == 1 mod 24
   through 4,300,000;
6. the twelve exact a=1 exceptions in that range;
7. repair of all twelve by (2,1) or (6,1), with exact Egyptian-fraction
   cross-multiplication checks.
"""
from array import array
from math import isqrt

XU_LIMIT = 720_001
EXT_LIMIT = 4_300_000
FACTOR_LIMIT = 6 * XU_LIMIT + 10

WILD_XU = [
    409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321
]
A1_EXCEPTIONS_EXT = [
    409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321,
    1134241, 1724209, 1726201,
]

U24 = {1, 5, 7, 11, 13, 17, 19, 23}
H_MINUS6 = {1, 5, 7, 11}
H_MINUS4 = {1, 5, 13, 17}
H_MINUS3 = {1, 7, 13, 19}


def build_spf(N):
    """Linear sieve, compact 32-bit SPF array."""
    spf = array("I", [0]) * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        si = spf[i]
        for p in primes:
            v = p * i
            if v > N or p > si:
                break
            spf[v] = p
    return spf, primes


SPF, PRIMES = build_spf(FACTOR_LIMIT)


def is_prime(n):
    return n >= 2 and n <= FACTOR_LIMIT and SPF[n] == n


def factor_spf(n):
    assert 1 <= n <= FACTOR_LIMIT
    out = {}
    while n > 1:
        p = SPF[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out


def factor_trial(n):
    out = {}
    x = n
    for p in PRIMES:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out[p] = e
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def factorint(n):
    if n <= FACTOR_LIMIT:
        return factor_spf(n)
    return factor_trial(n)


def divisors(fac):
    ds = [1]
    for p, e in fac.items():
        old = ds[:]
        pp = 1
        for _ in range(e):
            pp *= p
            ds.extend(d * pp for d in old)
    return ds


def has_divisor_residue(N, mod, target):
    target %= mod
    return any(d % mod == target for d in divisors(factorint(N)))


def subgroup_generated_mod24(residues):
    H = {1}
    changed = True
    residues = set(residues)
    while changed:
        changed = False
        for a in list(H):
            for r in residues:
                v = (a * r) % 24
                if v not in H:
                    H.add(v)
                    changed = True
    return H


def verify_abstract_subgroup_classification():
    units = sorted(U24)

    assert all((u * u) % 24 == 1 for u in units)

    for mask in range(1 << len(units)):
        supp = {units[i] for i in range(len(units)) if (mask >> i) & 1}
        H = subgroup_generated_mod24(supp)

        if 5 in H:
            predicted_miss = (supp <= H_MINUS6) or (supp <= H_MINUS4)
            actual_miss = 23 not in H
            assert predicted_miss == actual_miss, (supp, H, "total 5")

        if 7 in H:
            predicted_miss = (supp <= H_MINUS6) or (supp <= H_MINUS3)
            actual_miss = 23 not in H
            assert predicted_miss == actual_miss, (supp, H, "total 7")


def portal_A_classification(n):
    # (a,u)=(2,1), modulus 8, N=2n+1 == 3 mod 8.
    fac = factorint(2 * n + 1)
    return not all(p % 8 in (1, 3) for p in fac)


def portal_D_classification(n):
    # (a,u)=(6,1), modulus 24, N=6n+1 == 7 mod 24.
    fac = factorint(6 * n + 1)
    support = {p % 24 for p in fac}
    miss = (support <= H_MINUS6) or (support <= H_MINUS3)
    return not miss


def exact_u_bound_a1(n):
    # 4u^2 - 2u <= n.
    u = (1 + isqrt(1 + 4 * n)) // 4
    while 4 * (u + 1) * (u + 1) - 2 * (u + 1) <= n:
        u += 1
    while 4 * u * u - 2 * u > n:
        u -= 1
    return u


def exhaustive_a1(n):
    """Complete fixed-a=1 Type-II search by the proved finite u bound."""
    U = exact_u_bound_a1(n)
    for u in range(1, U + 1):
        M = n + u
        mod = 4 * u
        if has_divisor_residue(M, mod, mod - 1):
            return True
    return False


def portal_certificate(n, a):
    """u=1 factor portal certificate, choosing the smallest suitable s."""
    M = a * n + 1
    mod = 4 * a
    for s in sorted(divisors(factorint(M))):
        if s % mod != mod - 1:
            continue
        q = M // s
        t = (s + 1) // mod
        x = q * t
        y = a * n * q * t
        z = a * n * t
        assert 4 * x * y * z == n * (x * y + x * z + y * z)
        return (s, q, t, x, y, z)
    return None


def main():
    verify_abstract_subgroup_classification()

    xu_targets = [
        n for n in range(2, XU_LIMIT + 1)
        if is_prime(n) and n % 24 == 1
    ]
    assert len(xu_targets) == 7185

    for n in xu_targets:
        direct_A = has_divisor_residue(2 * n + 1, 8, 7)
        direct_D = has_divisor_residue(6 * n + 1, 24, 23)
        assert direct_A == portal_A_classification(n)
        assert direct_D == portal_D_classification(n)

    A_count = sum(portal_A_classification(n) for n in xu_targets)
    D_count = sum(portal_D_classification(n) for n in xu_targets)
    both_count = sum(
        portal_A_classification(n) and portal_D_classification(n)
        for n in xu_targets
    )
    union_count = sum(
        portal_A_classification(n) or portal_D_classification(n)
        for n in xu_targets
    )
    assert (A_count, D_count, both_count, union_count) == (4307, 2192, 1263, 5236)

    xu_a1_exceptions = [n for n in xu_targets if not exhaustive_a1(n)]
    assert xu_a1_exceptions == WILD_XU

    for n in WILD_XU:
        assert portal_A_classification(n) or portal_D_classification(n)
        if portal_A_classification(n):
            assert portal_certificate(n, 2) is not None
        if portal_D_classification(n):
            assert portal_certificate(n, 6) is not None

    ext_targets = [
        n for n in range(2, EXT_LIMIT + 1)
        if is_prime(n) and n % 24 == 1
    ]
    assert len(ext_targets) == 37716
    ext_exceptions = [n for n in ext_targets if not exhaustive_a1(n)]
    assert ext_exceptions == A1_EXCEPTIONS_EXT

    cert_rows = []
    for n in ext_exceptions:
        A = portal_A_classification(n)
        D = portal_D_classification(n)
        assert A or D
        certA = portal_certificate(n, 2) if A else None
        certD = portal_certificate(n, 6) if D else None
        cert_rows.append((n, A, D, certA, certD))

    print("abstract subgroup classification: OK")
    print("Xu hard-class prime count:", len(xu_targets))
    print("portal A count:", A_count)
    print("portal D count:", D_count)
    print("both portals:", both_count)
    print("portal union:", union_count)
    print("paired misses:", len(xu_targets) - union_count)
    print("Xu a=1 exceptions:", xu_a1_exceptions)
    print("extended hard-class prime count:", len(ext_targets))
    print("extended a=1 exceptions:", ext_exceptions)
    print("certificates:")
    for row in cert_rows:
        print(row)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
