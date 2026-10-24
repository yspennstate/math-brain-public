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


# Exact geometric shell used for first entry into B_infty(0,1).
B1 = {(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)}
dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
outer = set()
for x, y, z in B1:
    for dx, dy, dz in dirs:
        w = (x + dx, y + dy, z + dz)
        if w not in B1:
            outer.add(w)
assert len(B1) == 27
assert len(outer) == 54
assert all(max(map(abs, w)) == 2 and sum(abs(c) == 2 for c in w) == 1 for w in outer)

# Rational facts used in the analytic proof.
# sqrt(pi)/4 < 4/9 follows from pi < 22/7 < 256/81.
assert Fraction(22, 7) < Fraction(256, 81)

# ln 2 < 7/10 because exp(7/10) > the first five nonnegative
# Taylor terms below, whose rational sum is >2.
exp_lower = (
    Fraction(1,1) + Fraction(7,10) + Fraction(49,200)
    + Fraction(343,6000) + Fraction(2401,240000)
)
assert exp_lower == Fraction(482921, 240000)
assert exp_lower > 2

# zeta(3/2) < 21/8.
# For n>=17, decreasing-integral comparison gives
# sum_{n=17}^infty n^{-3/2} <= int_16^infty x^{-3/2} dx = 1/2.
partial16 = sum((upper_inv_sqrt(n) / n for n in range(1, 17)), Fraction(0))
assert partial16 < Fraction(17, 8)
zeta_upper = Fraction(17, 8) + Fraction(1, 2)
assert zeta_upper == Fraction(21, 8)

# For K=2,...,63, certify S_K/K < 26/25.
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

# For K>=64 the report proves:
# term1 <=1/16,
# term2 <=1/3,
# term3 <=52/135,
# term4 <=56/243.
large = Fraction(1, 16) + Fraction(1, 3) + Fraction(52, 135) + Fraction(56, 243)
assert large == Fraction(19663, 19440)
assert large < Fraction(26, 25)

# First-interaction constant:
# initial: 27*(13/9)^3 = 2197/27.
# endpoint crossings: total endpoint rate 12 times outer shell 54 =648.
constant = Fraction(2197, 27) + 648 * Fraction(26, 25)
assert constant == Fraction(509821, 675)
assert constant < 756
assert 4 * 756 == 3024

print("C27 exact constant checker v2")
print("B1_size =", len(B1))
print("first_entry_outer_shell_size =", len(outer))
print("22/7 < 256/81 =", Fraction(22, 7) < Fraction(256, 81))
print("exp_0.7_five_term_lower =", exp_lower, ">2 =", exp_lower > 2)
print("partial16_zeta_upper =", partial16)
print("partial16_zeta_upper < 17/8 =", partial16 < Fraction(17, 8))
print("zeta_3_2_upper =", zeta_upper)
print("finite_K_range = 2..63")
print("max_finite_ratio_K =", maxK)
print("max_finite_ratio =", maxratio)
print("max_finite_ratio_decimal =", float(maxratio))
print("finite_gap_to_26_25 =", Fraction(26, 25) - maxratio)
print("large_K_bound =", large)
print("large_K_bound_decimal =", float(large))
print("large_K_gap_to_26_25 =", Fraction(26, 25) - large)
print("first_interaction_constant =", constant)
print("first_interaction_constant_decimal =", float(constant))
print("first_interaction_constant < 756 =", constant < 756)
print("density_threshold_multiplier =", 4 * 756)
print("ALL_EXACT_CHECKS_PASS")
