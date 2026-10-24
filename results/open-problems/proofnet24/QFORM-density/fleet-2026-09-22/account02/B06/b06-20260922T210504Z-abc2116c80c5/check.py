from fractions import Fraction
from math import sqrt, e, pi

eps = Fraction(1, 8)
eps2 = eps * eps
inv_eps2 = 1 / eps2

A = [
    [Fraction(0), inv_eps2, Fraction(0), Fraction(1)],
    [inv_eps2, Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0), eps2],
    [Fraction(1), Fraction(0), eps2, Fraction(0)],
]
l1 = [1 / eps, 0, eps, 0]
l2 = [0, 1 / eps, 0, eps]
m = 1 / eps2 + eps2

def mv(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

assert mv(A, l1) == [m * x for x in l2]
assert mv(A, l2) == [m * x for x in l1]

H = [[A[i][j] for j in (2, 3)] for i in (0, 1)]
G = [[A[i][j] for j in (2, 3)] for i in (2, 3)]
assert H == [[0, 1], [1, 0]]
assert G == [[0, eps2], [eps2, 0]]

c0_sq = Fraction(256, 129) - 1 - Fraction(129, 4064)
assert c0_sq == Fraction(499487, 524256)
c0 = sqrt(float(c0_sq))
residual_gamma_coefficient = 16 * e * sqrt(pi) / c0
square_smoothed_coefficient = 2 * sqrt(2 * residual_gamma_coefficient)

print('QFORM_B06_ONE_SIDED_CHECK_PASS')
print('eps', eps)
print('eigen_nonzero_exact', m, -m)
print('right_block_op_exact', eps2)
print('cross_s2_exact', 1)
print('c0_sq_exact', c0_sq)
print('c0', f'{c0:.12f}')
print('residual_gamma_coefficient', f'{residual_gamma_coefficient:.12f}')
print('square_smoothed_coefficient', f'{square_smoothed_coefficient:.12f}')
