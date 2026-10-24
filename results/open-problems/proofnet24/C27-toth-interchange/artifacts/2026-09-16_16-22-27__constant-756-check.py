from fractions import Fraction
from math import isqrt

D = 10**12


def upper_inv_sqrt(n, den=D):
    """Exact rational q >= 1/sqrt(n), certified by q^2*n >= 1."""
    target = den * den
    a = isqrt(target // n)
    while a * a * n < target:
        a += 1
    while a > 1 and (a - 1) * (a - 1) * n >= target:
        a -= 1
    q = Fraction(a, den)
    assert q * q * n >= 1
    return q


# 1) Exact certificate zeta(3/2) < 21/8.
# For n>=17, decreasing-integral comparison gives
# sum_{n=17}^infty n^{-3/2} <= int_16^infty x^{-3/2} dx = 1/2.
partial16 = sum((upper_inv_sqrt(n) / n for n in range(1, 17)), Fraction(0))
assert partial16 < Fraction(17, 8)
zeta_upper = Fraction(17, 8) + Fraction(1, 2)
assert zeta_upper == Fraction(21, 8)

# 2) For K=2,...,63, certify directly
# S_K/K < 26/25 where
# S_K = sum_{r=1}^{K-1} (K-r)
#       (K^{-1/2} + (4/9) r^{-1/2})^3.
finite = []
for K in range(2, 64):
    qK = upper_inv_sqrt(K)
    S = Fraction(0)
    for r in range(1, K):
        qr = upper_inv_sqrt(r)
        a = qK + Fraction(4, 9) * qr
        S += (K - r) * a**3
    ratio = S / K
    assert ratio < Fraction(26, 25)
    finite.append((K, ratio))
maxK, maxratio = max(finite, key=lambda kv: kv[1])

# 3) For K>=64, the analytic proof in the report gives four terms:
# 1/(2 sqrt K) <= 1/16,
# (4/3K) sum_{r<K}(K-r)r^{-1/2} <= 1/3,
# (16/27 sqrt K) sum_{r<K}(K-r)r^{-1} <= 52/135,
# (64/729K) sum_{r<K}(K-r)r^{-3/2} <= 56/243.
large_K_bound = (
    Fraction(1, 16)
    + Fraction(1, 3)
    + Fraction(52, 135)
    + Fraction(56, 243)
)
assert large_K_bound == Fraction(19663, 19440)
assert large_K_bound < Fraction(26, 25)

# 4) New first-interaction constant.
# Initial shell term: 27*(13/9)^3 = 2197/27.
# Endpoint pre-entry shell: 54 sites, total endpoint rate 12 -> 648.
constant = Fraction(2197, 27) + 648 * Fraction(26, 25)
assert constant == Fraction(509821, 675)
assert constant < 756

# 5) Positive-density corollary: if beta >= (4*756*K)^2,
# then delta = 756*K/sqrt(beta) <= 1/4.
assert 4 * 756 == 3024

print("C27 exact constant checker")
print("partial16_zeta_upper =", partial16)
print("partial16_zeta_upper < 17/8 =", partial16 < Fraction(17, 8))
print("zeta_3_2_upper =", zeta_upper)
print("finite_K_range = 2..63")
print("max_finite_ratio_K =", maxK)
print("max_finite_ratio =", maxratio)
print("max_finite_ratio_decimal =", float(maxratio))
print("finite_gap_to_26_25 =", Fraction(26, 25) - maxratio)
print("large_K_bound =", large_K_bound)
print("large_K_bound_decimal =", float(large_K_bound))
print("large_K_gap_to_26_25 =", Fraction(26, 25) - large_K_bound)
print("first_interaction_constant =", constant)
print("first_interaction_constant_decimal =", float(constant))
print("first_interaction_constant < 756 =", constant < 756)
print("density_threshold_multiplier =", 4 * 756)
print("ALL_EXACT_CHECKS_PASS")
