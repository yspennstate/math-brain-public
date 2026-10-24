from fractions import Fraction
from math import sqrt, pi


def F(x):
    x = Fraction(x)
    return Fraction(57, 32) + Fraction(3, 16) * x - Fraction(39, 32) * x * x


def F_alt(x):
    x = Fraction(x)
    return (Fraction(57) - Fraction(33) * x) / 32 + Fraction(39, 32) * x * (1 - x)


# Exact cone-Hermite polynomial and its rigidity decomposition.
assert all(F(Fraction(k, 17)) == F_alt(Fraction(k, 17)) for k in range(18))
assert F(0) == Fraction(57, 32)
assert F(1) == Fraction(3, 4)
assert F(Fraction(1, 3)) == Fraction(41, 24)
assert F(Fraction(1, 9)) == Fraction(193, 108)

# Three-axis block frame: alpha=(0,0,1), |v|=1.
S_block = 2 * F(0) + F(1)
assert S_block == Fraction(69, 16)
assert S_block / 20 == Fraction(69, 320)  # coefficient in 1/m
assert 3 * S_block / 20 == Fraction(207, 320)  # coefficient in 1/n, n=3m

# Equal-leverage symmetric tetrahedral frame: alpha_j=1/3 and |v_j|^2=3/4.
S_sym_tetra = Fraction(9, 16) * 4 * F(Fraction(1, 3))
assert S_sym_tetra == Fraction(123, 32)
assert S_sym_tetra / 20 == Fraction(123, 640)
assert 4 * S_sym_tetra / 20 == Fraction(123, 160)

# Tetrahedral frame rotated so one row is the negative eigenaxis:
# alpha=(1,1/9,1/9,1/9).
S_ax_tetra = Fraction(9, 16) * (F(1) + 3 * F(Fraction(1, 9)))
assert S_ax_tetra == Fraction(55, 16)
assert S_ax_tetra / 20 == Fraction(11, 64)
assert 4 * S_ax_tetra / 20 == Fraction(11, 16)

# General equal-leverage formula:
# 207/320 + (351/640) mean(alpha(1-alpha)), as coefficient of 1/n.
base_n = Fraction(207, 320)
mix_n = Fraction(351, 640)
assert base_n + mix_n * Fraction(2, 27) == Fraction(11, 16)
assert base_n + mix_n * Fraction(2, 9) == Fraction(123, 160)

# Exact Euclidean Gram determinant for any three vertices of the scaled regular tetrahedron.
G = [
    [Fraction(3, 4), Fraction(-1, 4), Fraction(-1, 4)],
    [Fraction(-1, 4), Fraction(3, 4), Fraction(-1, 4)],
    [Fraction(-1, 4), Fraction(-1, 4), Fraction(3, 4)],
]
detG = (
    G[0][0] * (G[1][1] * G[2][2] - G[1][2] * G[2][1])
    - G[0][1] * (G[1][0] * G[2][2] - G[1][2] * G[2][0])
    + G[0][2] * (G[1][0] * G[2][1] - G[1][1] * G[2][0])
)
assert detG == Fraction(1, 4)

# In the axial orientation, the type-1 row is the negative eigenaxis.
# For the unscaled 3x3 principal block V J V^T:
minority_pivot = Fraction(-3, 4)
principal_det = Fraction(-1, 4)
assert abs(minority_pivot * principal_det) == Fraction(3, 16)

# account04/B18 theorem then yields 4 sqrt(pi) m / 3^(1/4).
partner_prefactor = 2 * sqrt(pi) / (float(Fraction(3, 16)) ** 0.25)
assert abs(partner_prefactor - 4 * sqrt(pi) / (3 ** 0.25)) < 1e-12

print("PASS exact rational identities")
print("F(0)=", F(0), "F(1)=", F(1), "F(1/3)=", F(Fraction(1, 3)), "F(1/9)=", F(Fraction(1, 9)))
print("block: S=", S_block, "coeff 1/m=", S_block / 20, "coeff 1/n=", 3 * S_block / 20)
print("symmetric tetra: S=", S_sym_tetra, "coeff 1/m=", S_sym_tetra / 20, "coeff 1/n=", 4 * S_sym_tetra / 20)
print("axial tetra: S=", S_ax_tetra, "coeff 1/m=", S_ax_tetra / 20, "coeff 1/n=", 4 * S_ax_tetra / 20)
print("UNTF 1/n coefficient = 207/320 + (351/640)*mean(alpha(1-alpha))")
print("tetra Gram det=", detG, "principal det=", principal_det, "minority pivot=", minority_pivot)
print("account04/B18 Schur-pivot prefactor times m=", partner_prefactor)
print("3sqrt(2)=", 3 * sqrt(2))
