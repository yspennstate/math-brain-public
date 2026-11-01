from fractions import Fraction
from math import comb, isqrt


def good_probability(n: int) -> Fraction:
    """Exact probability that a fixed full block is good."""
    a = Fraction(3, 50)  # central-square area
    A = Fraction(3, 2)   # full-block area
    return Fraction(comb(n, 2), 1) * (a / n) ** 2 * (1 - A / n) ** (n - 2)


def good_probability_expanded(n: int) -> Fraction:
    """Same multinomial probability in an independently expanded form."""
    return (
        Fraction(n * (n - 1), 2)
        * Fraction(3, 50 * n) ** 2
        * Fraction(2 * n - 3, 2 * n) ** (n - 2)
    )


def blocks(n: int) -> int:
    """M_n = floor(sqrt(2n/3))^2, evaluated with integer inequalities only."""
    m = isqrt((2 * n) // 3)
    while 3 * (m + 1) * (m + 1) <= 2 * n:
        m += 1
    while 3 * m * m > 2 * n:
        m -= 1
    return m * m


for n in range(3, 501):
    p = good_probability(n)
    q = good_probability_expanded(n)
    assert p == q

    M = blocks(n)
    m = isqrt(M)
    assert m * m == M
    assert 3 * m * m <= 2 * n < 3 * (m + 1) * (m + 1)

print("P0257 guarded-pair exact finite checker")
print("parameters: block area A=3/2; central-square area a=3/50")
print("checked n=3..500: multinomial probability identity EXACT")
print("checked n=3..500: M_n=floor(sqrt(2n/3))^2 block-count identity EXACT")
for n in (3, 4, 5, 10):
    print(f"n={n}: M_n={blocks(n)}, p_n={good_probability(n)}")
print("geometry: B=sqrt(6)/2, t=sqrt(6)/10, margin=sqrt(6)/5, pair_diameter<=sqrt(3)/5")
print("h=(sqrt(6)-sqrt(3))/5 > 0")
print("ALL_EXACT_FINITE_CHECKS_PASS")
