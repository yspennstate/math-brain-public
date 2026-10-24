from math import sqrt, pi, erf, exp, factorial
from fractions import Fraction

C = sqrt(6*pi)*erf(sqrt(3/2))
lower = 3*sqrt(2)
rational_ceiling = 97/24
I = 9*exp(-3/2) + (9/4)*C
kappa = I/(20*C)

# Exact elementary inequalities used in the analytic endpoint comparison.
series6 = sum(Fraction(3,2)**k / factorial(k) for k in range(7))
tail7 = Fraction(243,58240)
exp_upper = series6 + tail7
assert exp_upper < Fraction(9,2)
assert Fraction(132,7) < Fraction(1225,64)  # sqrt(6*pi)<35/8 from pi<22/7
assert Fraction(9409,576) < 18              # 97/24 < 3sqrt(2)

# Exact N3 heavy/b-bank pair determinant at one rational diagnostic parameter.
a = Fraction(3,5)
d2 = Fraction(16,25)
m = 100
det_hb = (-a)*(a/Fraction(m,1)) - d2/Fraction(m,1)
assert det_hb == -Fraction(1,m)

assert C < rational_ceiling < lower
assert I > 0 and kappa > 0

print("C_minus =", format(C, ".16f"))
print("97/24 =", format(rational_ceiling, ".16f"))
print("3sqrt2 =", format(lower, ".16f"))
print("Edgeworth_I =", format(I, ".16f"))
print("relative_kappa =", format(kappa, ".16f"))
print("exp(3/2) series upper rational =", exp_upper, float(exp_upper))
print("diagnostic a=3/5,m=100 heavy-b det =", det_hb)
print("PASS QFORM_ONE_HEAVY_N3_KERNEL")
