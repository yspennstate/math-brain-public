from fractions import Fraction as F
from math import factorial

# HARD7-03 exact omitted-centre-cone certificate.
# Imports only the immutable current four-step rational from the
# 20260919T1623Z checkpoint, then verifies the new cone algebra and
# a strictly improved Chernoff/plateau certificate.

theta = F(723, 1250)
q = F(1) - theta
a = F(2) - theta
b = F(3) - theta

assert F(0) < theta < F(1)
assert q > 0 and a > 0 and b > 0
assert b == a + 1

# A1-maximal cone E3. J0 is the ordinary tilted maximum-cone transform.
J0_direct = F(1)/q - F(2)/a + F(1)/b
J0_closed = F(2)/(q*a*b)
assert J0_direct == J0_closed
assert J0_direct > 0

# J1 = E[e^{theta A1-d}; A1=max], d=A1-max(A_-1,A_0).
# The first expression is the order-cone/spacing integral after
# integrating the lower maximum y; the second is its closed form.
J1_direct = F(2)*(F(1)/(a*a) - F(1)/a + F(1)/b)
J1_closed = F(2)/(a*a*b)
assert J1_direct == J1_closed
assert J1_direct > 0

# M_d=max(B0,B_-1-d). From
# f_M(u)=(1+e^{-d})e^{-u}-2e^{-d}e^{-2u},
# E[e^{-qM_d}] = 1/a - q e^{-d}/(a b).
# Integrating B1>M_d gives q e^{-M_d}/a.
H_const = q/(a*a)
H_exp_coeff = q*q/(a*a*b)
assert H_const > 0 and H_exp_coeff > 0

# Incremental omitted-cone gain for ONE centre adjacent pair.
delta3 = theta/(q*a) * (H_const*J0_direct - H_exp_coeff*J1_direct)
delta3_closed = F(2)*theta*(F(5)-F(3)*theta)/(q*a**5*b**2)
assert delta3 == delta3_closed
assert delta3 > 0

# Two reflected centre pairs; each appears in two fourth-step windows.
DeltaC3 = F(4)*delta3
assert DeltaC3 > 0

# Immutable current four-step value from the 20260919T1623Z checkpoint.
U4_prev = F(
    462207595847970865379094425847318588877127242915039062500000,
    533551258662847599879934006185557225047638076531060575909,
)

# Pair-subtraction improvements enter the four-step recurrence divided by q.
U4_new = U4_prev - DeltaC3/q
assert U4_new < U4_prev

# Exact Chernoff certificate. S32(x)<e^x because all omitted terms are
# positive; therefore S32(x)>U4_new certifies U4_new<e^x.
A_prev = F(292367491, 100000000)
A_new = F(29224277, 10000000)
assert A_new < A_prev
x = F(4)*theta*A_new
S32 = sum(x**k / F(factorial(k)) for k in range(33))
margin = S32 - U4_new
assert margin > 0

L_prev = F(1)/(F(4)*A_prev)
L_new = F(1)/(F(4)*A_new)
assert L_prev == F(25000000, 292367491)
assert L_new == F(2500000, 29224277)
assert L_new > L_prev

print("HARD7-03 exact omitted-centre-cone certificate")
print(f"theta = {theta}")
print(f"q = {q}")
print(f"a = {a}")
print(f"b = {b}")
print(f"J0_direct = {J0_direct}")
print(f"J0_closed = {J0_closed}")
print(f"J1_direct = {J1_direct}")
print(f"J1_closed = {J1_closed}")
print(f"H_const = {H_const}")
print(f"H_exp_coeff = {H_exp_coeff}")
print(f"delta3 = {delta3}")
print(f"DeltaC3 = {DeltaC3}")
print(f"U4_prev = {U4_prev}")
print(f"U4_new = {U4_new}")
print(f"A_prev = {A_prev}")
print(f"A_new = {A_new}")
print(f"x = {x}")
print(f"S32_minus_U4_new = {margin}")
print(f"L_prev = {L_prev}")
print(f"L_new = {L_new}")
print(f"metric_gain = {L_new-L_prev}")
print(f"J0_float = {float(J0_direct):.15f}")
print(f"J1_float = {float(J1_direct):.15f}")
print(f"delta3_float = {float(delta3):.15f}")
print(f"DeltaC3_float = {float(DeltaC3):.15f}")
print(f"U4_new_float = {float(U4_new):.15f}")
print(f"A_new_float = {float(A_new):.15f}")
print(f"S32_minus_U4_new_float = {float(margin):.15e}")
print(f"L_new_float = {float(L_new):.15f}")
print(f"metric_gain_float = {float(L_new-L_prev):.15e}")
print("ALL_EXACT_CHECKS_PASS = True")