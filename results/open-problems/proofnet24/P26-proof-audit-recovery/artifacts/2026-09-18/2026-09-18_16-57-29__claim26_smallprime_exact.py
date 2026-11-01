#!/usr/bin/env python3
"""Exact finite falsification of the literal small-prime scope of P04 Claim 26.

No floating point is used.  For p=5,29,53 we construct the clean-family sets
V and U_p exactly in F_p, then evaluate the literal strict count bound from
P04-I0101-QUOTIENT-TYPICAL-SPECTRUM-26.  The first two admissible primes show
that the phrase "fewer than [3(p-29)/(32p)] m" is false as written; p=53 is
the first admissible prime for which the bound has a positive right-hand side.
"""
from fractions import Fraction


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    assert r in (1, p - 1)
    return 1 if r == 1 else -1


def J(x: int, p: int) -> int:
    num = pow((x * x - x + 1) % p, 3, p)
    den = (x * x * pow((1 - x) % p, 2, p)) % p
    return (num * pow(den, -1, p)) % p


def check_prime(p: int):
    assert p % 24 == 5
    V = [x for x in range(p)
         if x not in (0, 1) and chi(x, p) == 1 and chi(x - 1, p) == 1]
    U = sorted({J(x, p) for x in V})
    m = len(U)
    assert m == (p - 5) // 24

    T = [[0 if i == j else chi(U[i] - U[j], p)
          for j in range(m)] for i in range(m)]

    # For the only sizes used here, the spectrum is exact by inspection.
    if m == 0:
        N = 0
    elif m == 1:
        assert T == [[0]]
        N = 0
    elif m == 2:
        assert T[0][1] in (-1, 1)
        assert T[1][0] == T[0][1]
        # Spectrum is {+1,-1}; compare squared eigenvalue 1 to 4p/9 exactly.
        N = 2 if Fraction(1, 1) > Fraction(4 * p, 9) else 0
    else:
        raise AssertionError("checker is intentionally scoped to p=5,29,53")

    rhs = Fraction(3 * (p - 29), 32 * p) * m
    literal_strict_bound = Fraction(N, 1) < rhs
    return V, U, m, N, rhs, literal_strict_bound


for p in (5, 29, 53):
    V, U, m, N, rhs, ok = check_prime(p)
    print(f"p={p} V={V} U={U} m={m} N={N} rhs={rhs} strict_claim={ok}")

assert check_prime(5)[5] is False
assert check_prime(29)[5] is False
assert check_prime(53)[5] is True
print("P26-CLAIM26-SMALLPRIME-EXACT: PASS_END")
