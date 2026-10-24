from fractions import Fraction
import math

# Exact finite arithmetic checks for the 2026-09-16T18-27-00Z HARD10-03 run.
# This is a self-check of finite constants only; it is not an independent proof audit.

N = math.comb(729, 2)
assert N == 265356

gamma = Fraction(1, 1) - Fraction(1, 3) - 2 * Fraction(1, 8)
assert gamma == Fraction(5, 12)

# Exact sample saturation check of the NEW-L106 recurrence at
# epsilon=1/2, s=9, a=1. Then D=2*a*s^epsilon=6.
# Set sqrt(L0)=4*N*9 so the base-size condition is at equality.
D = Fraction(6, 1)
root_L0 = 4 * N * 9
q0 = D / root_L0
q1_rhs = Fraction(1, root_L0) + N * q0 * q0
target_q1 = D / (3 * root_L0)
assert q1_rhs <= target_q1

print("HARD10-03 exact finite checks")
print(f"C(729,2) = {N}")
print(f"gamma(alpha=1/3, delta=1/8) = {gamma.numerator}/{gamma.denominator}")
print("NEW-L106 sample exact check (epsilon=1/2, s=9, a=1):")
print(f"D = {D}")
print(f"sqrt(L0) = 4*N*9 = {root_L0}")
print(f"q0 = {q0}")
print(f"q1 recurrence RHS = {q1_rhs}")
print(f"target D/sqrt(9 L0) = {target_q1}")
print("q1_rhs <= target: PASS")
print("ALL_EXACT_CHECKS_PASS")
