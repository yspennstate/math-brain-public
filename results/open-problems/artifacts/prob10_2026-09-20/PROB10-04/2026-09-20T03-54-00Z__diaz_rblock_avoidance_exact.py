from itertools import combinations
from math import comb, log
from fractions import Fraction


def poly_mul(a, b, maxdeg=None):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if maxdeg is None or i + j <= maxdeg:
                out[i + j] += x * y
    if maxdeg is not None and len(out) > maxdeg + 1:
        out = out[:maxdeg + 1]
    return out


def block_count_formula(U, r, A, S):
    # [z^S] (((1+z)^r-z^r)^A (1+z)^(U-rA)).
    base = [comb(r, j) for j in range(r)]
    p = [1]
    for _ in range(A):
        p = poly_mul(p, base, S)
    tail = [comb(U - r * A, j)
            for j in range(min(U - r * A, S) + 1)]
    p = poly_mul(p, tail, S)
    return p[S] if S < len(p) else 0


def block_count_brute(U, r, A, S):
    blocks = [set(range(r * i, r * (i + 1))) for i in range(A)]
    good = 0
    for T in combinations(range(U), S):
        TT = set(T)
        if all(not block.issubset(TT) for block in blocks):
            good += 1
    return good


brute_cases = 0
for U in range(2, 11):
    for r in range(2, min(5, U + 1)):
        for A in range(0, U // r + 1):
            for S in range(0, U + 1):
                f = block_count_formula(U, r, A, S)
                b = block_count_brute(U, r, A, S)
                assert f == b, (U, r, A, S, f, b)
                brute_cases += 1

bound_cases = 0
for U in range(2, 31):
    for r in range(2, min(7, U + 1)):
        for A in range(0, U // r + 1):
            for S in range(0, U + 1):
                num = block_count_formula(U, r, A, S)
                den = comb(U, S)
                lhs = Fraction(num, den)
                # (U+1) [1-(S/U)^r]^A, exactly rational.
                rhs = Fraction((U + 1) * (U ** r - S ** r) ** A,
                               (U ** r) ** A)
                assert lhs <= rhs, (U, r, A, S, lhs, rhs)
                bound_cases += 1

print("BRUTE_RBLOCK_FORMULA_CASES =", brute_cases)
print("EXACT_RBLOCK_BOUND_CASES =", bound_cases)
for U, r, A, S in [
    (12, 3, 3, 5),
    (20, 4, 4, 8),
    (30, 5, 5, 12),
    (100, 3, 20, 30),
    (1000, 3, 200, 300),
]:
    num = block_count_formula(U, r, A, S)
    den = comb(U, S)
    rhs = Fraction((U + 1) * (U ** r - S ** r) ** A,
                   (U ** r) ** A)
    print("CASE", U, r, A, S)
    print("  probability =", float(Fraction(num, den)))
    print("  finite_bound =", float(rhs))
    if num:
        print("  exact_rate_per_U =", -log(num / den) / U)
    # The polynomial prefactor log(U+1)/U vanishes.  This is the
    # asymptotic exponent supplied directly by the finite bound when
    # A/U and S/U stay fixed.
    a = A / U
    p = S / U
    print("  asymptotic_bound_rate_per_U =", -a * log(1 - p ** r))

# Check the algebra at the coefficient-bound saddle:
# z=S/(U-S), z/(1+z)=S/U.
for U in range(2, 30):
    for S in range(1, U):
        z = Fraction(S, U - S)
        for r in range(2, 7):
            lhs = (((1 + z) ** r - z ** r) / (1 + z) ** r)
            rhs = 1 - Fraction(S ** r, U ** r)
            assert lhs == rhs

print("ALL_EXACT_RBLOCK_CHECKS_PASS = True")
