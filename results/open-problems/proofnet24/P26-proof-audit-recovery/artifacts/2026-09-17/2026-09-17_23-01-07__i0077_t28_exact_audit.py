from fractions import Fraction

# P26 independent exact finite-core check for R07/I0077 theorem T28.
# This checks only the canonical rational inequalities. The theorem-sized
# Brownian/OU/FBM argument is audited in the accompanying immutable report.

L = Fraction(6, 1)
eta0 = Fraction(1, 100)
eta1 = Fraction(3, 200)
eta2 = Fraction(1, 50)
s2 = Fraction(3, 4)  # P = log 4 => r=1/2 and s^2=1-r^2=3/4.

assert eta1 - eta0 == Fraction(1, 200)
assert eta2 - eta1 == Fraction(1, 200)
assert 2 * eta2 == Fraction(1, 25)

distance = L / 2 - eta2
assert distance == Fraction(149, 50)

chernoff_exponent = distance * distance / (2 * s2)
assert chernoff_exponent == Fraction(22201, 3750)
assert chernoff_exponent > 5

# e^5 > 1 + 5 + 5^2/2! = 37/2 > 10, hence 2 e^{-5} < 1/5.
taylor_lower = Fraction(1, 1) + 5 + Fraction(25, 2)
assert taylor_lower == Fraction(37, 2)
assert taylor_lower > 10

# Since (s sqrt(2 pi))^2 = 3 pi/2 > 1 (e.g. pi>3),
# the N(mu,s^2) density is <1. Therefore the nearest tooth has mass <1/25.
# Combining it with the non-nearest tail gives Q < 1/25 + 1/5 = 6/25.
q_upper = Fraction(1, 25) + Fraction(1, 5)
assert q_upper == Fraction(6, 25)
assert q_upper < Fraction(1, 4)  # e^{-P}=1/4.
assert Fraction(25, 6) > 4

print("P26-I0077-T28-INDEPENDENT-EXACT-AUDIT: PASS")
print(f"s^2 = {s2}")
print(f"eta1-eta0 = eta2-eta1 = {eta1-eta0}")
print(f"2 eta2 = {2*eta2}")
print(f"L/2-eta2 = {distance}")
print(f"Chernoff exponent = {chernoff_exponent} > 5")
print(f"Taylor lower bound for e^5 = {taylor_lower} > 10")
print(f"Q rational upper envelope = {q_upper} < 1/4 = e^(-P)")
print("ALL_EXACT_CHECKS_PASS")
