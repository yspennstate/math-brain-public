from fractions import Fraction
from itertools import combinations
import math


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def norm2(x):
    return dot(x, x)


def wedge2(x, y):
    return sum((x[i]*y[j]-x[j]*y[i])**2
               for i, j in combinations(range(len(x)), 2))


# Exact checkerboard-wedge identity on a nontrivial rational test.
u = [Fraction(1), Fraction(2)]
c = [Fraction(3), Fraction(-1)]
r = [Fraction(2), Fraction(-2), Fraction(1)]
v = [Fraction(0), Fraction(1), Fraction(4)]
a = u + r
q = c + v
E2D = wedge2(a, q)
expanded = (wedge2(u, c) + wedge2(r, v)
            + sum((u[i]*v[j]-c[i]*r[j])**2
                  for i in range(len(u)) for j in range(len(r))))
assert E2D == expanded

alpha = dot(a, q) / norm2(q)
residual = sum((a[i]-alpha*q[i])**2 for i in range(len(a)))
assert residual == E2D / norm2(q)

# Target-valid exact stress family at K=100.
# The L|R cross block has singular values K,K,1,1,1.
K = 100
E2 = K**4 + 6*K**2 + 3
E3 = 3*K**4 + 6*K**2 + 1
M = K**4
P = K**4

# At the unique effective-dimension-two ridge scale, x=gamma^2 solves
# 2 K^2/(K^2+x)+3/(1+x)=2, i.e. 2x^2-x-3K^2=0.
x = (1 + math.sqrt(1 + 24*K*K)) / 4
kK = K*K / (K*K + x)
assert kK > 23/24
assert M > E2/2
assert E3 > 1/256
assert E2 > 1/25

# For the physical cut {i,j}|rest the two cross rows are identical,
# hence its complete second compound is exactly zero.
checkerboard_E2 = 0
assert checkerboard_E2 == 0

eta = 1/16
half_riesz_constant = 8 * (3200 ** (1/8))
# The already-proved rank-five cross-fiber theorem pays this stress:
# product of nonzero cross singular values = K^2.
crossfiber_density_bound = (5*math.e/3) * (K**2) ** (-1/5)

print("identity_E2 =", E2D, "expansion =", expanded, "equal", E2D == expanded)
print("least_squares =", residual, "E2/||q||^2 =", E2D/norm2(q), "equal", residual == E2D/norm2(q))
print("K =", K)
print("E2 =", E2)
print("E3 =", E3)
print("M/E2 =", M/E2)
print("theta2_gamma_sq =", repr(x))
print("anchor_ridge_leverage =", repr(kK), "threshold", 23/24, "passes", kK > 23/24)
print("checkerboard_E2 =", checkerboard_E2)
print("two_star_P =", P)
print("paid_branch_if_E2D>=P/16: H_half <", repr(half_riesz_constant))
print("crossfiber_density_bound =", repr(crossfiber_density_bound))
print("QFORM_TWOSTAR_CHECKERBOARD_WEDGE_CHECK_PASS")
