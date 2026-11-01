from fractions import Fraction
from math import factorial

# HARD10-03 exact arithmetic self-check for NEW-L101.
# This is a validation artifact, not the theorem proof.
#
# Goal: certify the coarse rational inequality
#   epsilon_rep = 1/2 + 1/(16 e log 2) > 53/100
# without floating-point arithmetic.

# e = sum_{k=0}^6 1/k! + tail_{k>=7}.
# For k>=7, consecutive-term ratios are <= 1/8, so
# tail <= (1/7!) * 1/(1-1/8).
e_partial = sum(Fraction(1, factorial(k)) for k in range(7))
e_tail_upper = Fraction(1, factorial(7)) / (1 - Fraction(1, 8))
e_upper = e_partial + e_tail_upper

# ln 2 = 1 - 1/2 + 1/3 - ... .
# Every odd alternating partial sum is an upper bound.
ln2_upper = sum(
    Fraction(1, k) if k % 2 == 1 else -Fraction(1, k)
    for k in range(1, 10)
)

assert e_upper == Fraction(31967, 11760)
assert e_upper < Fraction(11, 4)
assert ln2_upper == Fraction(1879, 2520)
assert ln2_upper < Fraction(3, 4)

# Therefore e log 2 < (11/4)(3/4) = 33/16 < 25/12.
product_coarse_upper = Fraction(11, 4) * Fraction(3, 4)
assert product_coarse_upper == Fraction(33, 16)
assert product_coarse_upper < Fraction(25, 12)

# Hence 1/(16 e log 2) > 1/(16*(25/12)) = 3/100,
# so epsilon_rep > 1/2 + 3/100 = 53/100.
correction_lower = Fraction(3, 100)
epsilon_lower = Fraction(1, 2) + correction_lower
assert epsilon_lower == Fraction(53, 100)

print(f"e_upper={e_upper}")
print(f"ln2_upper={ln2_upper}")
print(f"coarse_product_upper={product_coarse_upper}")
print("coarse_product_upper<25/12: PASS")
print(f"certified_epsilon_rep>{epsilon_lower}")
print("ALL_EXACT_CHECKS_PASS")
