from fractions import Fraction
from math import factorial


def exp_bounds(x, N=8):
    """Rigorous rational bounds for exp(x), x>=0."""
    s = sum(x**k / Fraction(factorial(k)) for k in range(N + 1))
    first = x**(N + 1) / Fraction(factorial(N + 1))
    ratio = x / Fraction(N + 2)
    assert ratio < 1
    return s, s + first / (1 - ratio)


def log_bounds_atanh(x, N=2):
    """Rigorous rational bounds for log(x), x>1, from the atanh series."""
    z = (x - 1) / (x + 1)
    s = sum(Fraction(2) * z**(2*k + 1) / Fraction(2*k + 1) for k in range(N))
    tail = Fraction(2) * z**(2*N + 1) / (Fraction(2*N + 1) * (1 - z*z))
    return s, s + tail


print("R15 F0111 orbit-smoothing / mixed-face exact checker")

a0 = Fraction(16, 45)
b0 = Fraction(2, 25)
c0 = Fraction(21, 100)

L23, U23 = exp_bounds(Fraction(2, 3))
L28, U28 = exp_bounds(Fraction(14, 5))
L155, U155 = exp_bounds(Fraction(31, 20))
L07, U07 = exp_bounds(Fraction(7, 10))

assert L23 > Fraction(25, 13)
assert U23 < Fraction(100, 51)
assert L28 > 16
assert U28 < Fraction(50, 3)
assert U155 < Fraction(100, 21)
assert L07 > 2

assert Fraction(104, 625) > Fraction(121, 800)
assert Fraction(126, 800) > Fraction(121, 800)
hmax_upper = Fraction(29, 45) - Fraction(21, 100) * (1 + Fraction(31, 20))
assert hmax_upper == Fraction(1961, 18000)
assert hmax_upper < Fraction(11, 100)

# alpha_s* = 2/3 - (4/9) log 2 > 16/45 because log 2 < 7/10.
assert Fraction(2, 3) - Fraction(4, 9) * Fraction(7, 10) == a0

# alpha_b* = 5/3 - log(3)/log(2) > 2/25 iff 3^75 < 2^119.
assert 3**75 < 2**119

# beta_sb* = 2/9 > 21/100.
assert Fraction(2, 9) > c0

# Within-orbit smoothing thresholds.
beta_ss = Fraction(13, 45)
assert beta_ss > Fraction(1, 6)

l2L, l2U = log_bounds_atanh(Fraction(2), N=2)
l3L, l3U = log_bounds_atanh(Fraction(3), N=2)
beta_bb_lower = (l3L - Fraction(4, 3) * l2U) / (l2U * l2U)
assert beta_bb_lower > Fraction(1, 6)

print("exp(2/3) bounds:", L23, U23)
print("exp(14/5) bounds:", L28, U28)
print("exp(31/20) upper:", U155, "< 100/21")
print("exp(7/10) lower:", L07, "> 2")
print("hmax rational upper:", hmax_upper, "< 11/100")
print("3^75 < 2^119:", 3**75 < 2**119)
print("beta_sb*=2/9 > 21/100:", Fraction(2, 9) > c0)
print("beta_ss*=13/45 > 1/6:", beta_ss > Fraction(1, 6))
print("log2 interval:", l2L, l2U)
print("log3 interval:", l3L, l3U)
print("beta_bb rigorous lower:", beta_bb_lower)
print("beta_bb lower - 1/6:", beta_bb_lower - Fraction(1, 6))
print("ALL_EXACT_CHECKS_PASS")
