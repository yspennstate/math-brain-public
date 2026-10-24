from fractions import Fraction
from math import factorial

# HARD7-01 exact self-check.
#
# This certifies the finite rational core of the relaxed two-atom angular
# obstruction in the n=p=3 homogeneous cone-mixture reduction.
# It does NOT assert that the two-atom angular law is realizable by a single
# convex homogeneous potential/body pair.
#
# Put L=log(2), v1=L, v2=20L, weights 1/20 and 19/20, and evaluate at
# s=e^(3t)=1.  After removing the irrelevant common factor 1/3, write
# F(s)=sum_i w_i (1-exp(-s v_i))/v_i.
# At s=1:
#   F=A/L, F'=B, F''=-L*C,
# so (1/9)(log F(e^(3t)))''|_{t=0} = L*(P-L*R),
# where P=B/A and R=C/A+P^2.  Hence positivity follows from L<P/R.

w = Fraction(1, 20)
w2 = Fraction(19, 20)
k1, k2 = 1, 20

A = w * (1 - Fraction(1, 2)) / k1 + w2 * (1 - Fraction(1, 2**k2)) / k2
B = w * Fraction(1, 2) + w2 * Fraction(1, 2**k2)
C = w * k1 * Fraction(1, 2) + w2 * k2 * Fraction(1, 2**k2)

P = B / A
R = C / A + P * P
threshold = P / R

# Rigorous elementary upper bound log(2)<7/10:
# exp(7/10) > sum_{j=0}^4 (7/10)^j/j! > 2.
x = Fraction(7, 10)
exp_lower = sum(x**j / factorial(j) for j in range(5))

checks = {
    "A_positive": A > 0,
    "B_positive": B > 0,
    "C_positive": C > 0,
    "threshold_gt_7_10": threshold > Fraction(7, 10),
    "exp_7_10_series_gt_2": exp_lower > 2,
}

print("A =", A)
print("B =", B)
print("C =", C)
print("P =", P)
print("R =", R)
print("P/R =", threshold)
print("10*num - 7*den =", 10 * threshold.numerator - 7 * threshold.denominator)
print("sum_{j=0}^4 (7/10)^j/j! =", exp_lower)
print("series excess over 2 =", exp_lower - Fraction(2))
for key, value in checks.items():
    print(key, "=", value)
print("ALL_EXACT_CHECKS_PASS =", all(checks.values()))

if not all(checks.values()):
    raise SystemExit(1)
