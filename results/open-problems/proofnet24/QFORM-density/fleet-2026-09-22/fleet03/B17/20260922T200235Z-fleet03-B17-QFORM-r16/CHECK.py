from fractions import Fraction
from math import erf, exp, sqrt

# Exact interval-case value in Lemma 2.1.
d = Fraction(1, 12)
I_interval = d*d - d/Fraction(6,1) + Fraction(1,80)
assert I_interval == Fraction(1,180)

# Exact shell formula: I_shell(a)-1/180 = a^2/12+a/24+1/576 >0 for a>=0.
# Check coefficients and boundary value.
assert Fraction(7,960) - Fraction(1,180) == Fraction(1,576)

# Uniform[-1/2,1/2] exact square variance.
var_square = Fraction(1,80) - Fraction(1,144)
assert var_square == Fraction(1,180)

# Gaussian fourth-mode gap constants.
Phi1 = 0.5*(1.0 + erf(1.0/sqrt(2.0)))
eta = 2.0*(1.0-Phi1)
base = 3.0*sqrt(2.0)
for delta in [1.0, 0.5, 0.25, 0.1]:
    factor = 1.0 - eta*(1.0-exp(-delta/4.0))
    bound = base*factor
    assert 0.0 < factor < 1.0
    print(f"delta={delta:g} eta={eta:.15f} factor={factor:.15f} bound={bound:.15f} gap={base-bound:.15f}")

print("I_interval_min =", I_interval)
print("shell_boundary =", Fraction(7,960))
print("var_uniform_square =", var_square)
print("PASS")
