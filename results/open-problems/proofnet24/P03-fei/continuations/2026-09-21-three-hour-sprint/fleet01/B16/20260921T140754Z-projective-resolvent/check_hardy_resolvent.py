from fractions import Fraction
from itertools import product


def mean_interval(q, a, b):
    return (b ** q - a ** q) / (q * (b - a))


def cross_interval(q, r, a, b):
    d = q + r - 1
    return (b ** d - a ** d) / (d * (b - a))


def variance_interval(coeffs, a, b):
    mu = sum(c * mean_interval(q, a, b) for q, c in coeffs.items())
    e2 = sum(
        c * d * cross_interval(q, r, a, b)
        for q, c in coeffs.items()
        for r, d in coeffs.items()
    )
    return e2 - mu * mu, mu


def hardy_square(coeffs):
    # Integral_0^1 |(I-H)m|^2, for m(t)=sum_q a_q t^(q-1).
    b = {q: c * Fraction(q - 1, q) for q, c in coeffs.items()}
    return sum(
        c * d * Fraction(1, q + r - 1)
        for q, c in b.items()
        for r, d in b.items()
    )


def scaled_low_coeffs(coeffs):
    return {q: c * Fraction(1, 2 ** (q - 1)) for q, c in coeffs.items()}


cases = 0
for vals in product(range(-2, 3), repeat=4):
    coeffs = {q: Fraction(v) for q, v in zip((3, 5, 7, 9), vals) if v}
    full_var, full_mean = variance_interval(coeffs, Fraction(0), Fraction(1))
    assert full_var == hardy_square(coeffs), (coeffs, full_var, hardy_square(coeffs))

    low_var, low_mean = variance_interval(coeffs, Fraction(0), Fraction(1, 2))
    high_var, high_mean = variance_interval(coeffs, Fraction(1, 2), Fraction(1))
    assert low_var == hardy_square(scaled_low_coeffs(coeffs)), (coeffs, low_var)

    bridge = sum(
        c * Fraction(1, q) * (1 - Fraction(1, 2 ** (q - 1)))
        for q, c in coeffs.items()
    ) ** 2
    split = Fraction(1, 2) * low_var + Fraction(1, 2) * high_var + bridge
    assert full_var == split, (coeffs, full_var, split)
    assert bridge == Fraction(1, 4) * (low_mean - high_mean) ** 2
    cases += 1

print('PASS')
print('exact_signed_polynomial_cases', cases)
print('degrees_checked', [2, 4, 6, 8])
print('identities', ['hardy_variance', 'dyadic_total_variance', 'low_half_exponential_resolvent'])
