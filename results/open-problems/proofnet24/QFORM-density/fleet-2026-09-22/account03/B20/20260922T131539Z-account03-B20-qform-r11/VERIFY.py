from fractions import Fraction as F

# Exact calibration for QFORM-TWOLEVEL-LOCALIZED-SQUARE-CASCADE-v1.
# P is the rank-three projection I_4-(1/4)11^T.
n = 4
P = [[F(int(i == j), 1) - F(1, 4) for j in range(n)] for i in range(n)]

a = P[0][0]
assert a == F(3, 4)
T = [[P[i][j] - P[i][0] * P[0][j] / a for j in range(1, n)] for i in range(1, n)]
assert T == [
    [F(2, 3), F(-1, 3), F(-1, 3)],
    [F(-1, 3), F(2, 3), F(-1, 3)],
    [F(-1, 3), F(-1, 3), F(2, 3)],
]

b = T[0][0]
assert b == F(2, 3)
S = [[T[i][j] - T[i][0] * T[0][j] / b for j in range(1, 3)] for i in range(1, 3)]
assert S == [[F(1, 2), F(-1, 2)], [F(-1, 2), F(1, 2)]]

# Rank-one nonzero eigenvalue is the trace.
d = S[0][0] + S[1][1]
assert d == 1
c = F(3, 4)
c2 = F(2, 3)
det_lambda = F(1, 1)
assert abs(a * b * d) == c * c2 * abs(det_lambda) == F(1, 2)

# Exponent bookkeeping after two square-smoothing steps:
# |a|^{-1/2}|b|^{-3/10}|d|^{-1/5}, with |d|=c c2 |detLambda|/(|a b|),
# becomes |a|^{-3/10}|b|^{-1/10}(c c2 |detLambda|)^{-1/5}.
assert F(-1,2) + F(1,5) == F(-3,10)
assert F(-3,10) + F(1,5) == F(-1,10)

print('PASS QFORM-TWOLEVEL-LOCALIZED-SQUARE-CASCADE-v1')
print('a=3/4 b=2/3 d=1 c=3/4 c2=2/3 product=1/2')
