from fractions import Fraction
from itertools import product
from math import factorial


def falling(a: int, m: int) -> int:
    out = 1
    for j in range(m):
        out *= a - j
    return out


def simplex_formula(n: int, m: int) -> Fraction:
    """Exact ordered-simplex integral times ordered-tuple count."""
    assert n >= 3 and 1 <= m <= n - 1
    S = [Fraction(j * n, 1) - Fraction(j * (j + 1), 2)
         for j in range(1, m + 1)]
    q = n - 1 - m
    if q == 0:
        integral = Fraction(0, 1)
    else:
        integral = Fraction(1, 1) / S[-1] - Fraction(1, 1) / (S[-1] + q)
        for Sj in S[:-1]:
            integral /= Sj
    return Fraction(falling(n - 1, m) * factorial(m), 1) * integral


def closed_formula(n: int, m: int) -> Fraction:
    """The claimed closed form for E[(H_n)_m]."""
    assert n >= 3 and 1 <= m <= n - 1
    num = Fraction(falling(n - 1, m + 1), 1)
    den = Fraction(m + 1, 1)
    for j in range(1, m + 2):
        den *= Fraction(2 * n - j - 1, 2)
    return num / den


def mean_formula(n: int) -> Fraction:
    return Fraction(n - 2, 2 * n - 3)


def second_factorial_formula(n: int) -> Fraction:
    return Fraction(2 * (n - 3), 3 * (2 * n - 3))


def variance_from_moments(n: int) -> Fraction:
    mu = mean_formula(n)
    return second_factorial_formula(n) + mu - mu * mu


def variance_closed(n: int) -> Fraction:
    return Fraction(7 * n * n - 27 * n + 24, 3 * (2 * n - 3) ** 2)


def limit_factorial(r: int, m: int) -> Fraction:
    """Exact formula for E[(H_r)_m] of the fixed-complement limit variable."""
    total = Fraction(0, 1)
    for ls in product(range(r), repeat=m):
        coeff = Fraction(1, 1)
        for ell in ls:
            coeff *= Fraction(r - ell, factorial(ell))
        L = sum(ls)
        coeff *= Fraction(factorial(r + L - 1), (m + 1) ** (r + L))
        total += coeff
    return total / factorial(r - 1)


checked = 0
for n in range(3, 31):
    for m in range(1, n):
        assert simplex_formula(n, m) == closed_formula(n, m)
        checked += 1
    assert closed_formula(n, 1) == mean_formula(n)
    if n >= 4:
        assert closed_formula(n, 2) == second_factorial_formula(n)
    assert variance_from_moments(n) == variance_closed(n)

for m in range(1, 8):
    assert limit_factorial(1, m) == Fraction(1, m + 1)

print("P0458 r=1 exact falling-factorial self-check")
print(f"closed_vs_simplex_exact_pairs={checked}")
print("n=4: mean=", mean_formula(4), " f2=", second_factorial_formula(4),
      " var=", variance_from_moments(4), sep="")
print("n=10: mean=", mean_formula(10), " f2=", second_factorial_formula(10),
      " var=", variance_from_moments(10), sep="")
print("r=1 limit factorial moments m=1..7:",
      [limit_factorial(1, m) for m in range(1, 8)])
for r in range(1, 5):
    print(f"r={r} limit factorial moments m=1..4:",
          [limit_factorial(r, m) for m in range(1, 5)])
print("ALL_EXACT_CHECKS_PASS")
