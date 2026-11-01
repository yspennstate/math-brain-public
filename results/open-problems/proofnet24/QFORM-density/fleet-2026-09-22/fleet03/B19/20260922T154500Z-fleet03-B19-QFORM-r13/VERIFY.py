from fractions import Fraction
import math

try:
    from math import gamma
except ImportError:
    raise

delta0 = Fraction(9, 280)
eta = delta0 / 4
tau = 3 * delta0 / 8
m = Fraction(7, 8)

assert eta == Fraction(9, 1120)
assert tau == Fraction(27, 2240)

C_G = math.exp(0.5) * (2 ** 0.25) * gamma(0.25) / math.sqrt(2 * math.pi)
L_diag = 2 * math.sqrt(2 / float(eta))
C_diag = 4 * float(m) ** (-0.75) * math.sqrt(L_diag)
K_rank = math.sqrt(math.e * math.pi) * math.sqrt(2 / float(delta0))
L_rank = C_G * K_rank
C_rank = 4 * float(m) ** (-0.75) * math.sqrt(L_rank)

assert C_G < 3
assert L_diag < 31.553
assert C_diag < 25
assert L_rank < 65.372
assert C_rank < 36

print(f"delta0={delta0}")
print(f"eta={eta}")
print(f"forced_cross_tau={tau}")
print(f"C_G={C_G:.15f}")
print(f"L_diag={L_diag:.15f}")
print(f"C_diag={C_diag:.15f}")
print(f"K_rank={K_rank:.15f}")
print(f"L_rank={L_rank:.15f}")
print(f"C_rank={C_rank:.15f}")
print("QFORM_B19_CRITICAL_VALUE_SPLICE_CONSTANTS_PASS")
