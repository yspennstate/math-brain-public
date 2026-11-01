from fractions import Fraction as F
from math import factorial

# Retuned parameters
d = F(3757, 50000)
p = F(28503, 10000000)
h = F(8227, 100000)
q = F(11522, 125000)
target = F(1441, 4)

# Elementary upper bounds
sqrt2_ub = F(70711, 50000)
e_ub = F(271829, 100000)
root_ub = F(12849, 10000)  # upper bound for (9/2)^(1/6)
C3_ub = 3 * sqrt2_ub * e_ub * root_ub
pi_ub = F(22, 7)
ln2_ub = F(1733, 2500)
ln5_ub = F(3219, 2000)
ln10_ub = F(2303, 1000)
d_inv_sqrt_ub = F(73, 20)
p_inv_quarter_ub = F(433, 100)
p_inv_sqrt_ub = F(18731, 1000)

# Exact elementary certificates
assert sqrt2_ub**2 > 2
assert root_ub**6 > F(9, 2)
e_series_ub = sum(F(1, factorial(k)) for k in range(11)) + F(12, 11 * factorial(11))
assert e_series_ub < e_ub

# exp(x)>target certificates imply logarithmic upper bounds.
def exp_partial(x, n):
    return sum(x**k / F(factorial(k)) for k in range(n + 1))

assert exp_partial(ln2_ub, 6) > 2
assert exp_partial(ln5_ub, 8) > 5
assert exp_partial(ln10_ub, 9) > 10

# No-pivot coefficient and structural margins
assert q*q > p + d*d
assert 1 - d - h > 0
assert 1 - d - q - 4*h > 0
assert 1 - d - 2*q - 9*h > 0

# Reciprocal coefficient bounds
assert d > F(400, 5329)         # d^(-1/2) < 73/20
assert p > F(100, 433)**4       # p^(-1/4) < 433/100
assert p_inv_sqrt_ub**2 > 1/p   # p^(-1/2) < 18731/1000
assert F(2, 1)/(d*h) < 324      # sqrt(2/(dh)) < 18

A_ub = pi_ub + 8 + 4*ln2_ub + 8*ln5_ub
B_ub = 10 + 4*ln10_ub

bounds = {
    "no_pivot": 2*C3_ub/h,
    "scalar_no_pivot_schur": F(13)*18,
    "scalar_pair_schur": 16*d_inv_sqrt_ub*p_inv_quarter_ub,
    "scalar_scalar_schur": d_inv_sqrt_ub + A_ub/d,
    "definite_pair": pi_ub*p_inv_sqrt_ub,
    "indefinite_pair": B_ub*p_inv_sqrt_ub + F(3, 8),
}

for name, value in bounds.items():
    assert value < target, (name, value, target)

print("PASS")
print("q^2-(p+d^2) =", q*q-(p+d*d))
print("r1 margin =", 1-d-q-4*h)
print("r2 margin =", 1-d-2*q-9*h)
print("C3 upper =", C3_ub, float(C3_ub))
print("A upper =", A_ub, float(A_ub))
print("B upper =", B_ub, float(B_ub))
for name, value in bounds.items():
    print(name, value, float(value), "slack", target-value, float(target-value))
