from fractions import Fraction
import math


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def tr(A):
    return [list(x) for x in zip(*A)]


R = [[Fraction(x, 2) for x in row]
     for row in ((1, 1, 1), (1, -1, 1), (1, 1, -1), (1, -1, -1))]
B = [[Fraction(0), Fraction(-1), Fraction(0)],
     [Fraction(-1), Fraction(0), Fraction(0)],
     [Fraction(0), Fraction(0), Fraction(1)]]
I3 = [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]

assert mm(tr(R), R) == I3
assert mm(B, B) == I3

A = mm(mm(R, B), tr(R))
expected = [[Fraction(x, 4) for x in row]
            for row in ((-1, 1, -3, -1),
                        (1, 3, -1, 1),
                        (-3, -1, -1, 1),
                        (-1, 1, 1, 3))]
assert A == expected

p0 = 4 * math.asinh(1)
p_axis = 8 * (math.sqrt(2) - 1)
p_diffuse = 3 * math.sqrt(2)
assert math.pi < p0 < p_diffuse
assert p_axis < p0
assert 4 < p_diffuse

# Independent numerical check of the exact cone integral.
N = 200000
step = (math.pi / 2) / N
quad = 0.0
for k in range(N):
    theta = (k + 0.5) * step
    h = (1 + math.cos(theta)) / math.sqrt(2) + math.sin(theta)
    quad += 1 / h
quad *= 4 * step
assert abs(quad - p0) < 1e-9

# Finite sanity check of the pointwise one-sheet monotonicity formula H_+(r).
for u in (0.0, 0.07, 0.2, 0.6):
    for c in (0.0, 0.2, 0.7, 1.0):
        s = math.sqrt(max(0.0, 1 - c * c))
        rs = [u + j * 0.05 for j in range(20)]
        vals = []
        for r in rs:
            aa = (u + r * c) / math.sqrt(2)
            bb = abs(u - r * c) / math.sqrt(2)
            cc = r * s
            vals.append(aa + max(bb, cc))
        assert all(vals[j + 1] + 1e-14 >= vals[j]
                   for j in range(len(vals) - 1))

print('QFORM_B17_ROT45_CHECK_PASS')
print('p0_rot45 =', repr(p0))
print('p0_axis =', repr(p_axis))
print('3sqrt2 =', repr(p_diffuse))
print('pi =', repr(math.pi))
print('midpoint_integral =', repr(quad))
print('gap_over_axis =', repr(p0 - p_axis))
print('gap_below_3sqrt2 =', repr(p_diffuse - p0))
