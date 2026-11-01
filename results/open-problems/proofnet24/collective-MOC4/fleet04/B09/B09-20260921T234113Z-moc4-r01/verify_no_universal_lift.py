from fractions import Fraction as F
from itertools import permutations

U = [
    [F(492, 625), F(-31, 625), F(-48, 125), F(12, 25)],
    [F(-9, 25), F(12, 25), F(-4, 5), F(0)],
    [F(-36, 125), F(48, 125), F(9, 25), F(4, 5)],
    [F(-256, 625), F(-492, 625), F(-36, 125), F(9, 25)],
]


def gram_entry(i, j):
    return sum(U[k][i] * U[k][j] for k in range(4))


def det2(rows, cols):
    r0, r1 = rows
    c0, c1 = cols
    return U[r0][c0] * U[r1][c1] - U[r0][c1] * U[r1][c0]


def pointwise_value(sigma):
    # 1-based mathematical form:
    # 1[sigma(1)=2] + 1[sigma(2)=4]
    # - 1[sigma({1,3})={2,3}] + 1[sigma({1,4})={3,4}].
    return (
        int(sigma[0] == 1)
        + int(sigma[1] == 3)
        - int({sigma[0], sigma[2]} == {1, 2})
        + int({sigma[0], sigma[3]} == {2, 3})
    )


G = [[gram_entry(i, j) for j in range(4)] for i in range(4)]
I = [[F(int(i == j)) for j in range(4)] for i in range(4)]
assert G == I

P12 = U[0][1] ** 2
P24 = U[1][3] ** 2
M13_23 = det2((0, 2), (1, 2))
Q13_23 = M13_23 ** 2
M14_34 = det2((0, 3), (2, 3))
Q14_34 = M14_34 ** 2
violation = P12 + P24 - Q13_23 + Q14_34

assert P12 == F(961, 390625)
assert P24 == 0
assert M13_23 == F(81, 625)
assert Q13_23 == F(6561, 390625)
assert M14_34 == 0
assert Q14_34 == 0
assert violation == F(-224, 15625)

values = [pointwise_value(sigma) for sigma in permutations(range(4))]
assert min(values) == 0
assert max(values) == 2
assert all(v >= 0 for v in values)

print("orthogonal_exact:", G == I)
print("P12:", P12)
print("P24:", P24)
print("minor_13_23:", M13_23)
print("Q13_23:", Q13_23)
print("minor_14_34:", M14_34)
print("Q14_34:", Q14_34)
print("permutation_inequality_min:", min(values))
print("permutation_inequality_value_counts:", {v: values.count(v) for v in sorted(set(values))})
print("exact_violation:", violation)
