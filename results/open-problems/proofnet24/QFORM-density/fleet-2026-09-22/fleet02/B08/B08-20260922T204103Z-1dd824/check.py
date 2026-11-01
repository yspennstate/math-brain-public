from fractions import Fraction
import math

A0 = Fraction(158_518_644_736, 173_076_800_625)
tail_hs2 = Fraction(329, 3_218_176)
x12_near = Fraction(2, 3) - 2*tail_hs2 - tail_hs2*tail_hs2/Fraction(2,1)
bank_exact = A0 * Fraction(2, 3)
bank_top2 = A0 * x12_near

def l3_constant(bank_ratio):
    return 3**(2/3) * 2**(1/3) * float(bank_ratio)**(-1/6)

def linf_constant(bank_ratio):
    return (2**(4/3)+1) * l3_constant(bank_ratio)**(3/4)

assert A0 > Fraction(9,10)
assert x12_near > Fraction(2,3) - Fraction(1,4000)
assert bank_exact > Fraction(61,100)
assert bank_top2 > Fraction(61,100)
assert linf_constant(bank_exact) < 7.712
assert linf_constant(bank_top2) < 7.712

print("A0 =", A0, float(A0))
print("tail_hs2 =", tail_hs2, float(tail_hs2))
print("x1x2_near_lower =", x12_near, float(x12_near))
print("exact_rank2_bank_ratio =", bank_exact, float(bank_exact))
print("near_rank2_top2_bank_ratio =", bank_top2, float(bank_top2))
print("exact_rank2_L3_constant =", l3_constant(bank_exact))
print("exact_rank2_outer_square_Linf_constant =", linf_constant(bank_exact))
print("near_rank2_top2_L3_constant =", l3_constant(bank_top2))
print("near_rank2_top2_outer_square_Linf_constant =", linf_constant(bank_top2))
print("QFORM_B08_DOUBLE_INCIDENT_CHECK_PASS")
