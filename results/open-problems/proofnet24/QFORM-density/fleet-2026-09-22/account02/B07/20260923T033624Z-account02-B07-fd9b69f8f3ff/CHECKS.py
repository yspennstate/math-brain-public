from fractions import Fraction
from itertools import combinations_with_replacement
import math


def ek(vals, k):
    dp = [Fraction(1)] + [Fraction(0)] * k
    for x in vals:
        x = Fraction(x)
        for j in range(k, 0, -1):
            dp[j] += dp[j - 1] * x
    return dp[k]

checked = 0
for n in range(5, 9):
    for vals0 in combinations_with_replacement(range(1, 6), n):
        vals = tuple(sorted(vals0, reverse=True))
        E3, E4, E5 = ek(vals, 3), ek(vals, 4), ek(vals, 5)
        T3 = sum(vals[3:])
        T4 = sum(vals[4:])
        assert Fraction(T3) * E3 <= 4 * E4
        assert Fraction(T4) * E4 <= 5 * E5
        assert Fraction(T4 * T4) * E3 <= 20 * E5
        checked += 1

th = Fraction(1, 16)
eta = th**6 / Fraction(120 * 3072**2)
kappa = 1 / (256 * math.sqrt(3))
D5 = 5 * math.sqrt(2 * math.e) * float(eta) ** (-0.1) / kappa
STAB = 23 * math.sqrt(12) / (float(th) * kappa)
ANCHOR = float(th) * kappa / (16 * math.sqrt(24))

print(f"spectra_checked={checked}")
print(f"eta_exact={eta.numerator}/{eta.denominator}")
print(f"eta_float={float(eta):.16e}")
print(f"d5_bound_theta_1_16={D5:.12f}")
print(f"stability_bound_theta_1_16={STAB:.12f}")
print(f"biheavy_core_norm_floor={ANCHOR:.16e}")
print("STATUS=QFORM_D5_RANK34_CORE_CHECK_PASS")
