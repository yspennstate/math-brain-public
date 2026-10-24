from itertools import combinations
from math import comb, log
from fractions import Fraction


def C(n, k):
    if k < 0 or k > n:
        return 0
    return comb(n, k)


def formula_count(U, A, S):
    """S-subsets avoiding every one of A disjoint marked pairs."""
    return sum(C(A, r) * (2 ** r) * C(U - 2 * A, S - r)
               for r in range(A + 1))


def brute_count(U, A, S):
    pairs = [{2 * i, 2 * i + 1} for i in range(A)]
    good = 0
    for T in combinations(range(U), S):
        TT = set(T)
        if all(not p.issubset(TT) for p in pairs):
            good += 1
    return good


def finite_bound_fraction(U, A, S):
    # (U+1) * [1 - (S/U)^2]^A, kept exactly rational.
    return Fraction((U + 1) * (U * U - S * S) ** A,
                    (U * U) ** A)


checked_brute = 0
for U in range(2, 10):
    for A in range(0, U // 2 + 1):
        for S in range(0, U + 1):
            f = formula_count(U, A, S)
            b = brute_count(U, A, S)
            assert f == b, (U, A, S, f, b)
            checked_brute += 1

checked_bound = 0
for U in range(2, 41):
    for A in range(0, U // 2 + 1):
        for S in range(0, U + 1):
            num = formula_count(U, A, S)
            den = C(U, S)
            lhs = Fraction(num, den)
            rhs = finite_bound_fraction(U, A, S)
            assert lhs <= rhs, (U, A, S, lhs, rhs)
            checked_bound += 1

print("BRUTE_FORMULA_CASES =", checked_brute)
print("EXACT_BOUND_CASES =", checked_bound)
for U, A, S in [(8, 2, 3), (10, 3, 4), (12, 4, 5),
                (20, 6, 8), (1000, 200, 300)]:
    num = formula_count(U, A, S)
    den = C(U, S)
    rhs = finite_bound_fraction(U, A, S)
    print("CASE", U, A, S)
    print("  count =", num)
    print("  total =", den)
    print("  probability =", float(Fraction(num, den)))
    print("  finite_bound =", float(rhs))
    if num:
        print("  exact_rate_per_U =", -log(num / den) / U)
    if rhs < 1:
        print("  certified_bound_rate_per_U =", -log(float(rhs)) / U)

# Symbolic identity used in the proof:
# z=S/(U-S), so (1+2z)/(1+z)^2 = 1-(S/U)^2.
for U in range(2, 30):
    for S in range(1, U):
        z = Fraction(S, U - S)
        lhs = (1 + 2 * z) / (1 + z) ** 2
        rhs = 1 - Fraction(S * S, U * U)
        assert lhs == rhs

print("ALL_EXACT_CHECKS_PASS = True")
