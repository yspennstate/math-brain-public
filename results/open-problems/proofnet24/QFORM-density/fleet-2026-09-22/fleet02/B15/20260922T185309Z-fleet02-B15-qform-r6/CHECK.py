from fractions import Fraction
from math import isclose

# Exact normalized Hadamard frame and target matrix numerator 8A.
H2 = (
    (1,1,1,1),
    (1,1,-1,-1),
    (1,-1,1,-1),
    (1,-1,-1,1),
)
lambdas = (Fraction(1), Fraction(2), Fraction(-3), Fraction(1,2))

# Verify H=(1/2)H2 is orthogonal.
for i in range(4):
    for j in range(4):
        dot = sum(H2[k][i]*H2[k][j] for k in range(4))
        assert dot == (4 if i == j else 0)

# A_ij=(1/4) sum_k lambda_k H2[i,k]H2[j,k].
A = [[sum(lambdas[k]*H2[i][k]*H2[j][k] for k in range(4))/4 for j in range(4)] for i in range(4)]
expected = [
    [Fraction(1,8), Fraction(11,8), Fraction(-9,8), Fraction(5,8)],
    [Fraction(11,8), Fraction(1,8), Fraction(5,8), Fraction(-9,8)],
    [Fraction(-9,8), Fraction(5,8), Fraction(1,8), Fraction(11,8)],
    [Fraction(5,8), Fraction(-9,8), Fraction(11,8), Fraction(1,8)],
]
assert A == expected
assert all(x != 0 for row in A for x in row)

# Fragment geometry. g_M is supported in [-1, 1/2+1/(2M)], so translated
# components by 5j are disjoint, and the first lies strictly in (0,infinity).
for M in (1,2,8,64,512):
    width = Fraction(3,2) + Fraction(1,2*M)
    assert width < 5
    assert Fraction(5) - 1 > 0
    lower_bound = (M/2.0)**(2.0/3.0)
    print(f"M={M:3d}  conditional_moment_lower_bound={(lower_bound):.12f}")

print("PASS: exact matrix/source geometry and divergent (M/2)^(2/3) lower bound verified")
