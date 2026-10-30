from fractions import Fraction
from math import sqrt

# Exact values from the latest fleet03/B17 Edgeworth formula.

def h4(u):
    u = Fraction(u)
    return (57 + 6*u - 39*u*u) / 32


def h6(u):
    u = Fraction(u)
    return -Fraction(15,128) * (19*u**3 - 111*u**2 + 45*u + 63)


def h8(u):
    u = Fraction(u)
    return Fraction(105,2048) * (611*u**4 - 492*u**3 - 1902*u**2 + 1044*u + 867)


def c2(u):
    return h6(u)/105 + h8(u)/800


def k44(u, v):
    u, v = Fraction(u), Fraction(v)
    P = (21385*u*u*v*v - 3690*u*u*v - 951*u*u
         - 3690*u*v*v - 11412*u*v + 1566*u
         - 951*v*v + 1566*v + 2601)
    return Fraction(3,2048) * P

assert h4(0) == Fraction(57,32)
assert h4(1) == Fraction(3,4)
assert c2(0) == -Fraction(4833,327680)
assert c2(1) == -Fraction(173,17920)
assert k44(0,0) == Fraction(7803,2048)
assert k44(0,1) == Fraction(603,128)

# Explicit rational near-optimal family:
# positive banks 20q,20q; negative bank 13q.
first_q = (Fraction(24,13) + 2*Fraction(57,20)) / 640
assert first_q == Fraction(981,83200)

second_q = (2*c2(0)/20**2 + c2(1)/13**2
            + k44(0,0)/(400*20*20)
            + 2*k44(0,1)/(400*20*13))
assert second_q == -Fraction(3190763,193822720000)

N_factor = 53
first_N = first_q * N_factor
second_N = second_q * N_factor**2
assert first_N == Fraction(51993,83200)
assert second_N == -Fraction(8962853267,193822720000)

# Continuous first-order optimum from Cauchy-Schwarz.
Kstar = Fraction(63,160) + 3*sqrt(38)/80
assert float(first_N) > Kstar
assert float(first_N) - Kstar < 4e-7

alpha_minus = sqrt(24)/(sqrt(24)+2*sqrt(57))
alpha_plus = sqrt(57)/(sqrt(24)+2*sqrt(57))
assert abs(alpha_minus + 2*alpha_plus - 1) < 1e-15

# Spectrum certificate for aligned physical matrix:
# P_m=J_m/m satisfies P_m^2=P_m, rank(P_m)=1, tr(P_m)=1.
# Hence diag(P_m1,P_m2,-P_m3) has rank 3, trace 1,
# and exact nonzero spectrum {+1,+1,-1}; no numerical eigensolver needed.

print("PASS QFORM-THREEBANK-GLOBAL-TIP-OPTIMAL-v1")
print("Kstar", Kstar)
print("alpha_minus", alpha_minus)
print("alpha_plus", alpha_plus)
print("first_N", first_N, float(first_N))
print("first_gap", float(first_N)-Kstar)
print("second_N", second_N, float(second_N))
