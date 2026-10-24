#!/usr/bin/env python3
"""
Exact certificate/checker for HARD8-05 (Erdos-Straus), 2026-09-16.

It implements the Type-II divisor normal form:
for coprime positive integers a,u, if s | (a*n+u) and
    s == -1 (mod 4*a*u),
then with
    q=(a*n+u)/s, t=(s+1)/(4*a*u),
we have
    4/n = 1/(u*q*t) + 1/(a*n*q*t) + 1/(a*n*u*t).

For primes n == 1 (mod 24), we exhaust the a=1 slice through n<=720001
(the range m<=30000 in n=24m+1), recovering the nine small hyperbolic
exceptions.  We then certify the minimum modulator a among a=1,2,3 for
those nine: eight first appear at a=2, while n=102001 first appears at a=3.

No floating-point arithmetic is used in any mathematical check.
"""
from math import gcd, isqrt

LIMIT = 720001
WILD_EXPECTED = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321]

def sieve_primes(N):
    is_p = bytearray(b"\x01") * (N + 1)
    is_p[:2] = b"\x00\x00"
    for p in range(2, isqrt(N) + 1):
        if is_p[p]:
            is_p[p*p:N+1:p] = b"\x00" * (((N - p*p)//p) + 1)
    return [i for i in range(2, N+1) if is_p[i]]

PRIMES = sieve_primes(LIMIT)

def factorint(n):
    out = {}
    x = n
    for p in PRIMES:
        if p*p > x:
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

def divisors_from_factorization(fac):
    ds = [1]
    for p,e in fac.items():
        old = ds[:]
        powp = 1
        add = []
        for _ in range(e):
            powp *= p
            add.extend(d*powp for d in old)
        ds.extend(add)
    return sorted(ds)

def exact_u_bound(n,a):
    # If a Type-II witness has symmetric pair (u,q), choose u<=q.
    # n = 4*u*q*t - (u+q)/a with t>=1 then
    # n >= 4*u^2 - 2*u/a, i.e. 4*a*u^2-2*u-a*n <= 0.
    u = 0
    while 4*a*(u+1)*(u+1) - 2*(u+1) <= a*n:
        u += 1
    return u

def witness(n,a,u):
    if gcd(a,u) != 1:
        return None
    M = a*n + u
    mod = 4*a*u
    for s in divisors_from_factorization(factorint(M)):
        if s % mod != mod - 1:
            continue
        q = M // s
        if (u + q) % a:
            raise AssertionError("congruence should force a | (u+q)")
        t = (s + 1) // mod
        x = u*q*t
        y = a*n*q*t
        z = a*n*u*t
        # Exact cross-multiplied verification.
        assert 4*x*y*z == n*(x*y + x*z + y*z)
        # Normal form relation.
        assert n == 4*u*q*t - (u+q)//a
        return dict(a=a,u=u,s=s,q=q,t=t,x=x,y=y,z=z)
    return None

def exhaustive_for_fixed_a(n,a):
    U = exact_u_bound(n,a)
    for u in range(1,U+1):
        if gcd(a,u) != 1:
            continue
        w = witness(n,a,u)
        if w is not None:
            return w
    return None

def portal_A_factor_test(n):
    # For n == 1 mod 4, M=2n+1 == 3 mod 8.
    # There is a divisor 7 mod 8 iff some prime factor is 5 or 7 mod 8.
    M = 2*n + 1
    fac = factorint(M)
    left = any(d % 8 == 7 for d in divisors_from_factorization(fac))
    right = any(p % 8 in (5,7) for p in fac)
    assert left == right
    return left, fac

def main():
    targets = [p for p in PRIMES if p % 24 == 1 and p <= LIMIT]
    assert len(targets) == 7185

    a1_exceptions = []
    for n in targets:
        if exhaustive_for_fixed_a(n,1) is None:
            a1_exceptions.append(n)
    assert a1_exceptions == WILD_EXPECTED

    print("prime count n=1 mod24 through 720001:", len(targets))
    print("a=1 exceptions:", a1_exceptions)
    print()
    print("n,a,u,s,q,t,x,y,z,U(a=2), factor(2n+1)")
    for n in a1_exceptions:
        minw = None
        mina = None
        for a in (1,2,3):
            w = exhaustive_for_fixed_a(n,a)
            if w:
                mina = a
                minw = w
                break
        assert minw is not None
        if n == 102001:
            assert exhaustive_for_fixed_a(n,2) is None
            assert mina == 3
        else:
            assert mina == 2
        _, fac = portal_A_factor_test(n)
        print(n, mina, minw["u"], minw["s"], minw["q"], minw["t"],
              minw["x"], minw["y"], minw["z"], exact_u_bound(n,2), fac)

    # Seven of the nine are captured by the particularly simple portal
    # (a,u)=(2,1): a divisor s == 7 mod 8 of 2n+1.
    pA = []
    for n in a1_exceptions:
        w = witness(n,2,1)
        if w:
            pA.append(n)
    assert pA == [409,577,5569,9601,23929,329617,712321]
    assert witness(83449,2,3)["s"] == 791
    assert witness(102001,3,5)["s"] == 1319
    print()
    print("portal A captures:", pA)
    print("83449 portal (2,3):", witness(83449,2,3))
    print("102001 portal (3,5):", witness(102001,3,5))
    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
