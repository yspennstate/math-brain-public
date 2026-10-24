from fractions import Fraction as F
from itertools import permutations

U = [
    [F(0), F(3,5), F(16,25), F(-12,25)],
    [F(-69,325), F(-192,325), F(48,65), F(16,65)],
    [F(48,65), F(16,65), F(69,325), F(192,325)],
    [F(16,25), F(-12,25), F(0), F(-3,5)],
]

I = [[F(int(r == c)) for c in range(4)] for r in range(4)]
G = [[sum(U[r][k] * U[c][k] for k in range(4)) for c in range(4)] for r in range(4)]
assert G == I

P = [[z*z for z in row] for row in U]
x = {i: P[i][0] for i in (1,2,3)}
y = {j: P[0][j] for j in (1,2,3)}
assert sum(x.values()) == 1
assert sum(y.values()) == 1

C = {
    (1,1): 0, (1,2): 2, (1,3): 1,
    (2,1): 1, (2,2): 0, (2,3): 2,
    (3,1): 2, (3,2): 1, (3,3): 0,
}

def ell(sigma):
    return (
        int(sigma[1] == 3) + int(sigma[2] == 1) + int(sigma[3] == 2)
        - int(sigma[1] == 2) - int(sigma[2] == 3) - int(sigma[3] == 1)
    )

pointwise = []
for sigma in permutations(range(4)):
    if sigma[0] == 0:
        continue
    i = sigma.index(0)
    j = sigma[0]
    v = ell(sigma) + C[(i,j)]
    assert v >= 0
    pointwise.append(v)

L = P[1][3] + P[2][1] + P[3][2] - P[1][2] - P[2][3] - P[3][1]
anchor = (
    y[1]*x[2] + 2*y[1]*x[3]
    + 2*y[2]*x[1] + y[2]*x[3]
    + y[3]*x[1] + 2*y[3]*x[2]
)
necessary_lhs = L + anchor
assert necessary_lhs == -F(121344,2640625)

print("PASS MOC4-ZERO-ANCHOR-MARGINAL-LIFT-v1 exact refutation")
print("orthogonal = true")
print("sum_x =", sum(x.values()))
print("sum_y =", sum(y.values()))
print("permutations_checked =", len(pointwise))
print("pointwise_values =", sorted(set(pointwise)))
print("signed_singleton_L =", L)
print("anchor_cost =", anchor)
print("necessary_lhs =", necessary_lhs)
print("violation_gap =", -necessary_lhs)
