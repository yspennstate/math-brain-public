from fractions import Fraction as F

O = [
    [F(6,7), -F(2,7), -F(3,7)],
    [-F(2,7), F(3,7), -F(6,7)],
    [-F(3,7), -F(6,7), -F(2,7)],
]
J = [F(1), F(1), F(-1)]

def gram(M):
    return [[sum(M[k][i]*M[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]

assert gram(O) == [[F(i == j) for j in range(3)] for i in range(3)]
B = [[sum(O[k][i]*J[k]*O[k][j] for k in range(3))
      for j in range(3)] for i in range(3)]
assert B == [
    [F(31,49), -F(36,49), -F(12,49)],
    [-F(36,49), -F(23,49), -F(24,49)],
    [-F(12,49), -F(24,49), F(41,49)],
]
assert all(x != 0 for row in B for x in row)
assert [[sum(B[i][k]*B[k][j] for k in range(3)) for j in range(3)]
        for i in range(3)] == [[F(i == j) for j in range(3)] for i in range(3)]

u = [O[2][j]**2 for j in range(3)]
sum_u2 = sum(x*x for x in u)
A4 = F(27,8) - F(13,8)*sum_u2
H4avg = F(3) + F(3,4)*A4
coefficient = H4avg/F(20)
assert u == [F(9,49), F(36,49), F(4,49)]
assert sum_u2 == F(199,343)
assert A4 == F(3337,1372)
assert H4avg == F(26475,5488)
assert coefficient == F(5295,21952)
assert F(5295,21952) > F(69,320)

print("orthogonality, dense B, involution, and Edgeworth coefficient: PASS")
print("rotated coefficient =", coefficient, float(coefficient))
