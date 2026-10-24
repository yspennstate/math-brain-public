from fractions import Fraction
import sympy as sp

# Exact symbolic self-checks for HARD7-03 general-K path geometry.
K, R, U, D = sp.symbols("K R U D", integer=True)
x = 1 + R + K*D
y = U - D
steps = R + U + D

assert sp.expand(steps - (x - 1 + y - (K-2)*D)) == 0

# A linear coordinate t=a*i+b*j has unit increment on right and up steps
# iff a=b=1. The stretched step then has increment K-1, hence it is also
# unit only for K=2.
a, b = sp.symbols("a b")
sol_ab = sp.solve([sp.Eq(a, 1), sp.Eq(b, 1)], [a, b], dict=True)
assert sol_ab == [{a: 1, b: 1}]
stretched_increment = sp.expand(K*1 - 1)
assert stretched_increment == K - 1
assert sp.solve(sp.Eq(stretched_increment, 1), K) == [2]

# Source level-boundary parametrization:
# G(v)=gamma(1,v), s=v/G(v), g(s)=1/G(v), g(0)=1/G0.
G0, Gv, v, mu = sp.symbols("G0 Gv v mu", nonzero=True)
s = v/Gv
sec = sp.simplify((1/Gv - 1/G0)/s)
assert sp.simplify(sec - (G0-Gv)/(G0*v)) == 0

# Homogeneous supporting line g(s) >= g(0)-K*s/2 converts exactly to
# G_r(v) <= G0*(1+K*v/2).
support_residual = sp.simplify(1 - (Gv/G0 - K*v/2))
assert support_residual == sp.simplify((G0*(1+K*v/2)-Gv)/G0)

# The frozen binary K=2 certificate is unchanged in this run.
L = Fraction(500000, 6578563)
old = Fraction(1, 16)
assert L > old
assert L - old == Fraction(1421437, 105257008)

print("PATH_LENGTH_IDENTITY =", sp.Eq(steps, x - 1 + y - (K-2)*D))
print("UNIT_TIME_STRETCHED_INCREMENT =", stretched_increment)
print("UNIT_TIME_ALL_THREE_STEPS_IFF_K =", 2)
print("BOUNDARY_SECANT =", sec)
print("SUPPORT_RESIDUAL =", support_residual)
print("TRACKED_L =", f"{L.numerator}/{L.denominator}")
print("TRACKED_L_MINUS_1_16 =", f"{(L-old).numerator}/{(L-old).denominator}")
print("ALL_EXACT_CHECKS_PASS = True")
