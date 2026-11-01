from fractions import Fraction
from decimal import Decimal, getcontext

# C0021 depth-4 one-deviation arithmetic self-check.
# The four continuation values were produced in this run by exact Fraction
# evaluation of the already archived baseline policy pi_0
# (prob1000_lean_20260908/ultracode_20260909/C0021/policy_heur.py),
# after reproducing its certified old U_4 exactly.
#
# This file checks all arithmetic consequences of those exact Bellman values.
# It is a self-check, not an independent audit.

old_U4 = Fraction(20871140813662641, 562949953421312)
old_branch = Fraction(20308190860241329, 562949953421312)

# Baseline-pi_0 cost-to-go after the new second query, for the two outcomes
# from the first-positive one-bit state. The first-negative case is the sign image.
cont_a = Fraction(39081644577912289, 1125899906842624)
cont_b = Fraction(9949379448235949, 281474976710656)

new_branch = 1 + (cont_a + cont_b) / 2
new_U4 = 1 + new_branch
gain = old_U4 - new_U4

assert old_U4 == 1 + old_branch
assert new_branch == Fraction(81130962184541333, 2251799813685248)
assert new_U4 == Fraction(83382761998226581, 2251799813685248)
assert gain == Fraction(101801256423983, 2251799813685248)
assert gain > 0

# Structural B12 checks from the exact one-bit state:
# root posterior before the second query is 17/32 and remains so in expectation.
root_q = Fraction(17, 32)
new_root_q_plus = Fraction(9, 16)
new_root_q_minus = Fraction(1, 2)
assert (new_root_q_plus + new_root_q_minus) / 2 == root_q

# The override is deliberately locally suboptimal for finishing the touched depth-3 child.
local_optimum = Fraction(14747475, 1048576)
local_override = Fraction(14776803, 1048576)
local_sacrifice = local_override - local_optimum
assert local_sacrifice == Fraction(1833, 65536)
assert local_sacrifice > 0

getcontext().prec = 50
D = Decimal
ln3 = D(3).ln()
sigma_upper = (D(4) / D(3)).ln() / ln3

def frac_decimal(x):
    return D(x.numerator) / D(x.denominator)

old_sigma_lower = D(1) - (frac_decimal(old_U4).ln() / D(4)) / ln3
new_sigma_lower = D(1) - (frac_decimal(new_U4).ln() / D(4)) / ln3
old_width = sigma_upper - old_sigma_lower
new_width = sigma_upper - new_sigma_lower
width_gain = old_width - new_width

assert new_sigma_lower > old_sigma_lower
assert new_width < old_width

print("C0021 depth-4 one-deviation arithmetic self-check")
print("old_U4 =", old_U4)
print("old_branch =", old_branch)
print("cont_a =", cont_a)
print("cont_b =", cont_b)
print("new_branch =", new_branch)
print("new_U4 =", new_U4)
print("exact_U4_gain =", gain)
print("local_sacrifice =", local_sacrifice)
print("old_sigma_lower =", old_sigma_lower)
print("new_sigma_lower =", new_sigma_lower)
print("sigma_upper =", sigma_upper)
print("old_width =", old_width)
print("new_width =", new_width)
print("width_gain =", width_gain)
print("ALL_EXACT_ARITHMETIC_CHECKS_PASS")
