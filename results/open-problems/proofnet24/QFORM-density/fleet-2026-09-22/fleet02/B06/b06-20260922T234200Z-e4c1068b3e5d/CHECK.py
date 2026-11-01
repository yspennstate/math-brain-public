from fractions import Fraction
from math import sqrt, e


def check(eps):
    inv = 1 / eps
    s2 = inv * inv + eps * eps
    l1 = [inv, Fraction(0), eps, Fraction(0), Fraction(0)]
    l2 = [Fraction(0), inv, Fraction(0), eps, Fraction(0)]

    A = [[Fraction(0) for _ in range(5)] for __ in range(5)]
    for i in range(5):
        for j in range(5):
            A[i][j] = l1[i] * l2[j] + l2[i] * l1[j]
    A[4][4] += 1

    expected = [[Fraction(0) for _ in range(5)] for __ in range(5)]
    expected[0][1] = expected[1][0] = inv * inv
    expected[0][3] = expected[3][0] = 1
    expected[1][2] = expected[2][1] = 1
    expected[2][3] = expected[3][2] = eps * eps
    expected[4][4] = 1

    assert A == expected
    assert sum(x*x for x in l1) == s2
    assert sum(x*x for x in l2) == s2
    assert sum(l1[i]*l2[i] for i in range(5)) == 0

    return s2, 4*sqrt(2*e)/sqrt(float(s2)), 4*sqrt(e)


s2, bound_eps, bound_uniform = check(Fraction(1, 8))
print("QFORM_B06_THIRD_SQUARE_CHECK_PASS")
print("epsilon=1/8")
print("s^2 =", s2)
print("nonzero spectrum = {+", s2, ", -", s2, ", 1}")
print("bound_at_epsilon =", f"{bound_eps:.12f}")
print("uniform_bound_0<epsilon<1 <=", f"{bound_uniform:.12f}")
