from fractions import Fraction
import math


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def T(A):
    return [list(r) for r in zip(*A)]


O = [
    [Fraction(6, 7), Fraction(-2, 7), Fraction(-3, 7)],
    [Fraction(-2, 7), Fraction(3, 7), Fraction(-6, 7)],
    [Fraction(-3, 7), Fraction(-6, 7), Fraction(-2, 7)],
]
J = [[Fraction(1), 0, 0], [0, Fraction(1), 0], [0, 0, Fraction(-1)]]
I3 = [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]

assert mm(T(O), O) == I3
B = mm(mm(T(O), J), O)
expected_B = [
    [Fraction(31, 49), Fraction(-36, 49), Fraction(-12, 49)],
    [Fraction(-36, 49), Fraction(-23, 49), Fraction(-24, 49)],
    [Fraction(-12, 49), Fraction(-24, 49), Fraction(41, 49)],
]
assert B == expected_B
assert mm(B, B) == I3
assert sum(B[i][i] for i in range(3)) == 1

a0 = Fraction(5295, 21952)
c = [1.0, 1.0, 1.0]
a = [1.0, 1.0, 1.0]
extra = sum(ci * (1.0 - math.exp(-6.0 * ai * ai)) / 2.0
            for ci, ai in zip(c, a))
total = float(a0) + extra

assert float(a0) > 0
assert extra > 0
assert total > float(a0)

print("PASS QFORM_RARE_FRAGMENT_FIRST_VARIATION")
print("B =", [[str(x) for x in row] for row in B])
print("a0 =", float(a0))
print("symmetric_extra =", extra)
print("symmetric_total_relative_deficit =", total)
print("3sqrt2 =", 3.0 * math.sqrt(2.0))
