from fractions import Fraction as F
from math import factorial

A = [
    [43,-25,-25,-25,30],
    [-25,43,-25,-25,30],
    [-25,-25,43,-25,30],
    [-25,-25,-25,43,30],
    [30,30,30,30,32],
]
Q = [[F(x,68) for x in row] for row in A]
I = [[sum(Q[k][i]*Q[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
assert I == [[F(int(i==j)) for j in range(5)] for i in range(5)]
assert all(x != 0 for row in Q for x in row)

lam = [F(x) for x in [1,2,3,4,80]]
C = [[sum(Q[i][k]*lam[k]*Q[j][k] for k in range(5)) for j in range(5)] for i in range(5)]
expected_C = [
    [F(39737,2312),F(36575,2312),F(35725,2312),F(34875,2312),F(17835,1156)],
    [F(36575,2312),F(40349,2312),F(34875,2312),F(34025,2312),F(18345,1156)],
    [F(35725,2312),F(34875,2312),F(40961,2312),F(33175,2312),F(18855,1156)],
    [F(34875,2312),F(34025,2312),F(33175,2312),F(41573,2312),F(19365,1156)],
    [F(17835,1156),F(18345,1156),F(18855,1156),F(19365,1156),F(11365,578)],
]
assert C == expected_C

trace = sum(lam)
p = 5
d = 2
m = trace / p
mu = [C[i][i] for i in range(p)]
l1 = sum(abs(x-m) for x in mu)
assert trace == 90
assert m == 18
assert l1 == F(961,289)
assert sum(mu) == trace

# Rational lower bound on pi from Machin's identity.
x = F(1,5)
atan5_lb = x - x**3/F(3) + x**5/F(5) - x**7/F(7)
atan239_ub = F(1,239)
pi_lb = 16*atan5_lb - 4*atan239_ub
assert pi_lb == F(1231847548,392109375)

# Rational lower bound on e.
e_lb = sum(F(1,factorial(k)) for k in range(7))
assert e_lb == F(1957,720)

# This exact inequality implies phi(1)=1/sqrt(2*pi*e) < 121/500.
phi_upper = F(121,500)
assert 2*pi_lb*e_lb > F(500,121)**2

# Theorem's rational sufficient upper bound for the dense example.
upper = m * (F(d) + 2*p*phi_upper) + l1
assert upper == F(598846,7225)
S2 = F(84)
gap = S2 - upper
assert gap == F(8054,7225)
normalized_gap = gap / trace
assert normalized_gap == F(4027,325125)

print('EXACT_CHECK=PASS')
print('Q_ORTHOGONAL=PASS')
print('Q_ALL_25_ENTRIES_NONZERO=PASS')
print('TRACE=', trace)
print('MEAN_VARIANCE=', m)
print('L1_TO_BARYCENTER=', l1)
print('PI_LOWER=', pi_lb)
print('E_LOWER=', e_lb)
print('PHI1_UPPER=121/500')
print('RATIONAL_IMPLICATION_CHECK=PASS')
print('F_ROT_UPPER=', upper)
print('F_KL_LOWER=', S2)
print('KL_MINUS_ROT_LOWER=', gap)
print('NORMALIZED_KL_MINUS_ROT_LOWER=', normalized_gap)
print('SIGNED_ROT_MINUS_KL_UPPER=', -normalized_gap)
print('COVARIANCE_ROWS=')
for row in C:
    print('  ' + ', '.join(str(x) for x in row))
