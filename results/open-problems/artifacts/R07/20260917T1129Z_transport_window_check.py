from fractions import Fraction

# Exact self-check for the canonical fast-transport moving-window example
# in R07 / Burdzy-Scheutzow Problem 7.8.
#
# epsilon is the unpadded gap edge at the two extreme phases;
# eta is the transfer-padding parameter; h is the padded separation;
# tau is the logarithmic travel time and P the period.

epsilon = Fraction(1, 2)
eta = Fraction(1, 8)
h = epsilon - 2 * eta
tau = Fraction(1, 64)
P = Fraction(1, 1)

# For stationary OU over time tau,
# Y_{t+tau}=exp(-tau/2)Y_t+sqrt(1-exp(-tau)) Z.
# A transition from <= -h to >= h therefore needs
# Z >= h(1+exp(-tau/2))/sqrt(1-exp(-tau)).
# Using 1+exp(-tau/2)>=1 and 1-exp(-tau)<=tau gives z^2 >= h^2/tau.
# Chernoff P(Z>=z)<=exp(-z^2/2) gives kappa=-log(q)/P >= z^2/(2P).

z2_lower = h * h / tau
kappa_lower = z2_lower / (2 * P)

print(f"epsilon = {epsilon}")
print(f"eta = {eta}")
print(f"h = epsilon - 2 eta = {h}")
print(f"tau = {tau}")
print(f"z^2 lower bound = h^2/tau = {z2_lower}")
print(f"kappa lower bound = z^2/(2P) = {kappa_lower}")

assert h == Fraction(1, 4)
assert z2_lower == 4
assert kappa_lower == 2
assert kappa_lower > 1

print("PASS")
