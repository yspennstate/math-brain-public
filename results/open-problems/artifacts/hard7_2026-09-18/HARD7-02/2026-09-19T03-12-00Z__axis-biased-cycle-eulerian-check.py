from itertools import permutations
from fractions import Fraction
from math import factorial

# HARD7-02 run 7 exact finite-core self-check.
# Verifies the cyclic-Eulerian counting identity used for the
# order-biased orientation theorem and the resulting exact I_k(p) coefficients.

def cyclic_ascents(pi):
    k = len(pi)
    return sum(1 for i in range(k) if pi[i] < pi[(i + 1) % k])


def eulerian_table(nmax):
    A = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    A[0][0] = 1
    for n in range(1, nmax + 1):
        for m in range(n):
            left = (n - m) * (A[n - 1][m - 1] if m - 1 >= 0 else 0)
            right = (m + 1) * A[n - 1][m]
            A[n][m] = left + right
    return A


A = eulerian_table(8)
ok = True

print("HARD7-02 exact cyclic-ascent self-check")
print("identity: # {sigma in S_k : cycasc(sigma)=j} = k*A(k-1,j-1)")
for k in range(3, 9):
    counts = {j: 0 for j in range(1, k)}
    for pi in permutations(range(k)):
        counts[cyclic_ascents(pi)] += 1
    expected = {j: k * A[k - 1][j - 1] for j in range(1, k)}
    passed = counts == expected
    ok &= passed
    print(f"k={k}: counts={counts}; pass={passed}")


def I_enum(k, p):
    q = 1 - p
    total = Fraction(0, 1)
    for pi in permutations(range(k)):
        a = cyclic_ascents(pi)
        total += p ** a * q ** (k - a)
    return total / factorial(k)


def I_euler(k, p):
    q = 1 - p
    total = Fraction(0, 1)
    for j in range(1, k):
        total += Fraction(k * A[k - 1][j - 1], factorial(k)) * p ** j * q ** (k - j)
    return total


for p in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
    print(f"p={p}:")
    for k in range(3, 9):
        lhs = I_enum(k, p)
        rhs = I_euler(k, p)
        passed = lhs == rhs
        if p == Fraction(1, 2):
            passed = passed and rhs == Fraction(1, 2**k)
        ok &= passed
        print(f"  k={k}: I_k={rhs}; pass={passed}")

# Coefficient form:
# I_k(p)=p*q^(k-1)/(k-1)! * A_{k-1}(p/q).
# Clearing q denominators, the coefficient of p^j q^(k-j) must be
# A(k-1,j-1)/(k-1)!.
for k in range(3, 9):
    coeff_direct = {
        j: Fraction(k * A[k - 1][j - 1], factorial(k))
        for j in range(1, k)
    }
    coeff_formula = {
        j: Fraction(A[k - 1][j - 1], factorial(k - 1))
        for j in range(1, k)
    }
    passed = coeff_direct == coeff_formula
    ok &= passed
    print(f"k={k}: polynomial-coefficient identity pass={passed}")

print(f"ALL_EXACT_CHECKS_PASS = {ok}")
if not ok:
    raise SystemExit(1)
