from fractions import Fraction as Q
from math import sqrt


def A3(lam):
    return lam * (
        Q(6, 1) / ((Q(3, 1) - lam) * (Q(9, 1) - lam))
        - Q(4, 1) / (Q(16, 1) - lam)
    )


def K3(theta):
    return (Q(3, 1) + theta) / (theta * (Q(1, 1) - theta))


# A_3(lambda)=lambda a_3(lambda) is increasing on [1,3):
# derivative(first term) >= 27/64 and derivative(second term) <= 64/169.
A3prime_lower = Q(27, 64) - Q(64, 169)
assert A3prime_lower > 0

# Lower-p rectangle: p <= 1/4, hence theta <= p <= 1/4.
L_low = Q(569, 200)
A_low = A3(L_low)
theta_low_max = Q(1, 4)
K_low = K3(theta_low_max)
assert A_low < K_low
F_low = Q(3, 1) + theta_low_max - A_low * theta_low_max * (Q(1, 1) - theta_low_max)
assert F_low > 0
den_low = Q(3, 1) + theta_low_max + L_low
deriv_margin_low = Q(2, 1) * F_low / (den_low * den_low)
assert deriv_margin_low > 0

# Upper-p rectangle: p >= 3/4. Branch addition gives c4/c3 >= 4/5,
# so theta >= (4p)/(5-p) >= 12/17.
L_high = Q(57, 20)
A_high = A3(L_high)
theta_high_min = Q(12, 17)
K_high = K3(theta_high_min)
assert A_high < K_high
F_high = Q(3, 1) + theta_high_min - A_high * theta_high_min * (Q(1, 1) - theta_high_min)
assert F_high > 0
den_high = Q(4, 1) + L_high
deriv_margin_high = Q(2, 1) * F_high / (den_high * den_high)
assert deriv_margin_high > 0

print("A3prime_lower =", A3prime_lower, float(A3prime_lower))
print("LOW")
print("L_low =", L_low, float(L_low))
print("A_low =", A_low, float(A_low))
print("K_low =", K_low, float(K_low))
print("K_low-A_low =", K_low - A_low, float(K_low - A_low))
print("F_low =", F_low, float(F_low))
print("derivative_margin_low =", deriv_margin_low, float(deriv_margin_low))
print("HIGH")
print("L_high =", L_high, float(L_high))
print("A_high =", A_high, float(A_high))
print("theta_high_min =", theta_high_min, float(theta_high_min))
print("K_high =", K_high, float(K_high))
print("K_high-A_high =", K_high - A_high, float(K_high - A_high))
print("F_high =", F_high, float(F_high))
print("derivative_margin_high =", deriv_margin_high, float(deriv_margin_high))

# Decimal context only for the inherited all-mixture limiting root A3(lambda)=7+4*sqrt(3).
def A3_float(x):
    return x * (6 / ((3 - x) * (9 - x)) - 4 / (16 - x))

K_star = 7 + 4 * sqrt(3)
lo, hi = 2.8, 2.83
for _ in range(100):
    mid = (lo + hi) / 2
    if A3_float(mid) < K_star:
        lo = mid
    else:
        hi = mid
print("all_mixture_root_decimal_context =", lo)
print("ALL_EXACT_CHECKS_PASS")
