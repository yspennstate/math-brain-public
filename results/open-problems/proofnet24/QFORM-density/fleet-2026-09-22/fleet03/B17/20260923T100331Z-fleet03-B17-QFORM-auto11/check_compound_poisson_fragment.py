from fractions import Fraction
import math


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


O = [
    [Fraction(6, 7), Fraction(-2, 7), Fraction(-3, 7)],
    [Fraction(-2, 7), Fraction(3, 7), Fraction(-6, 7)],
    [Fraction(-3, 7), Fraction(-6, 7), Fraction(-2, 7)],
]
J = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(-1)],
]
I = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)],
]

assert matmul(transpose(O), O) == I
B = matmul(matmul(transpose(O), J), O)
expected_B = [
    [Fraction(31, 49), Fraction(-36, 49), Fraction(-12, 49)],
    [Fraction(-36, 49), Fraction(-23, 49), Fraction(-24, 49)],
    [Fraction(-12, 49), Fraction(-24, 49), Fraction(41, 49)],
]
assert B == expected_B
assert matmul(B, B) == I
assert sum(B[i][i] for i in range(3)) == 1
assert det3(B) == -1


def poisson_quadratic_laplace(lam, a):
    p = math.exp(-lam)
    total = p
    k = 0
    while k < 500:
        k += 1
        p *= lam / k
        total += p * math.exp(-6.0 * a * a * k * k)
        if k > lam + 20 and p < 1e-18:
            break
    return total


f = poisson_quadratic_laplace(1.0, 1.0)
three_sqrt_two = 3.0 * math.sqrt(2.0)
cone_tip_bound = (three_sqrt_two / 2.0) * (1.0 + f ** 3)
partner_deficit = 5295.0 / 21952.0

assert 0.0 < f < 1.0
assert cone_tip_bound < three_sqrt_two
assert partner_deficit > 0.0

print("O^T O = identity")
print("B =", [[str(x) for x in row] for row in B])
print("B^2 = identity")
print("trace B =", sum(B[i][i] for i in range(3)))
print("det B =", det3(B))
print("F(1,1) =", repr(f))
print("cone_tip_bound_three_banks =", repr(cone_tip_bound))
print("3sqrt2 =", repr(three_sqrt_two))
print("gap =", repr(three_sqrt_two - cone_tip_bound))
print("partner deficit =", repr(partner_deficit))
print("PASS QFORM-B17-COMPOUND-POISSON-FRAGMENT-CHECK")
