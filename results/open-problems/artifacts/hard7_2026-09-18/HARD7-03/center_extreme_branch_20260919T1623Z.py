from fractions import Fraction as F
from math import factorial

# HARD7-03 exact centre-pair extreme-branch certificate.
# This checker imports only the immutable exact U4_nested rational from the
# 20260919T1523Z checkpoint and verifies the new rational centre correction.

theta = F(723, 1250)
q = F(1) - theta
a = F(2) - theta
b = F(3) - theta

assert F(0) < theta < F(1)
assert q > 0 and a > 0 and b > 0

# First-layer left-extreme transform:
# E[e^{theta A_-1}; A_-1 >= A_0,A_1]
E_A_direct = F(1)/q - F(2)/a + F(1)/b
E_A_closed = F(2)/(q*a*b)
assert E_A_direct == E_A_closed
assert E_A_direct > 0

# Gap transform for B > M=max(B1,B2):
# inner integral over B gives q e^{-M}/a, and M has density
# 2 e^{-m}(1-e^{-m}).
I_B_direct = F(2)*q/a * (F(1)/a - F(1)/b)
I_B_closed = F(2)*q/(a*a*b)
assert I_B_direct == I_B_closed
assert I_B_direct > 0

# Exact monotone-kernel gain from one first-layer extreme event.
delta_left = theta/(q*a) * E_A_direct * I_B_direct
delta_left_closed = F(4)*theta/(q*a**4*b**2)
assert delta_left == delta_left_closed
assert delta_left > 0

# Left and right first-layer extreme events are disjoint a.s. and symmetric.
delta_center_pair = F(2)*delta_left
delta_center_closed = F(8)*theta/(q*a**4*b**2)
assert delta_center_pair == delta_center_closed
assert delta_center_pair > 0

# There are two reflected centre adjacent pairs, each appearing in two
# fourth-step predecessor windows: total multiplicity 4.
DeltaC_center = F(4)*delta_center_pair
DeltaC_closed = F(32)*theta/(q*a**4*b**2)
assert DeltaC_center == DeltaC_closed
assert DeltaC_center > 0

# Immutable prior exact value from
# artifacts/.../exact_nested_pair_kernel_20260919T1523Z.out
U4_nested = F(
    464527332753365031710169245072092857523367477290039062500000,
    533551258662847599879934006185557225047638076531060575909,
)

# Increasing the pair subtraction by DeltaC_center lowers U4 by /q.
U4_new = U4_nested - DeltaC_center/q
assert U4_new < U4_nested

# New exact Chernoff/shape certificate.  S32(x) is a rigorous lower bound
# for exp(x), so S32(4 theta A_new) > U4_new proves
# U4_new < exp(4 theta A_new).
A_old = F(7314597, 2500000)
A_new = F(292367491, 100000000)
assert A_new < A_old
x = F(4)*theta*A_new
S32 = sum(x**k / F(factorial(k)) for k in range(33))
margin = S32 - U4_new
assert margin > 0

L_old = F(1)/(F(4)*A_old)
L_new = F(1)/(F(4)*A_new)
assert L_old == F(625000, 7314597)
assert L_new == F(25000000, 292367491)
assert L_new > L_old

print("HARD7-03 exact centre extreme-branch certificate")
print(f"theta = {theta}")
print(f"q = {q}")
print(f"a = {a}")
print(f"b = {b}")
print(f"E_A_direct = {E_A_direct}")
print(f"E_A_closed = {E_A_closed}")
print(f"I_B_direct = {I_B_direct}")
print(f"I_B_closed = {I_B_closed}")
print(f"delta_left = {delta_left}")
print(f"delta_center_pair = {delta_center_pair}")
print(f"DeltaC_center = {DeltaC_center}")
print(f"U4_nested = {U4_nested}")
print(f"U4_new = {U4_new}")
print(f"A_old = {A_old}")
print(f"A_new = {A_new}")
print(f"x = {x}")
print(f"S32_minus_U4_new = {margin}")
print(f"L_old = {L_old}")
print(f"L_new = {L_new}")
print(f"metric_gain = {L_new-L_old}")
print(f"E_A_float = {float(E_A_direct):.15f}")
print(f"I_B_float = {float(I_B_direct):.15f}")
print(f"delta_left_float = {float(delta_left):.15f}")
print(f"delta_center_pair_float = {float(delta_center_pair):.15f}")
print(f"DeltaC_center_float = {float(DeltaC_center):.15f}")
print(f"U4_new_float = {float(U4_new):.15f}")
print(f"A_new_float = {float(A_new):.15f}")
print(f"S32_minus_U4_new_float = {float(margin):.15e}")
print(f"L_new_float = {float(L_new):.15f}")
print(f"metric_gain_float = {float(L_new-L_old):.15e}")
print("ALL_EXACT_CHECKS_PASS = True")
