from fractions import Fraction
import math
import random

beta0 = Fraction(289, 15984)
b = float(beta0)
eta0 = math.sqrt(191) * b / 16
theta0 = eta0 / 2
corollary_coefficient = 3 * 2**(2/3) * theta0**(-2/3)
partner_coefficient = 256 / b

print('beta0 =', b)
print('eta0 =', eta0)
print('theta0 =', theta0)
print('rank1-two-star coefficient =', corollary_coefficient)
print('partner pair-area coefficient =', partner_coefficient)

assert corollary_coefficient < 120.992
assert partner_coefficient < 14158.838

# Exact rank-one crossing shear check.
# For B=[[d,q],[p,sigma]] of rank one, d*sigma=p*q and
# sigma (y2+q/sigma*y1)(z2+p/sigma*z1)=y^T B z.
random.seed(20260923)
max_err = 0.0
checks = 0
for _ in range(10000):
    u = [random.uniform(-3, 3), random.uniform(-3, 3)]
    v = [random.uniform(-3, 3), random.uniform(-3, 3)]
    d = u[0] * v[0]
    q = u[0] * v[1]
    p = u[1] * v[0]
    sigma = u[1] * v[1]
    if abs(sigma) < 1e-8:
        continue
    y1, y2, z1, z2 = [random.uniform(-2, 2) for _ in range(4)]
    lhs = d*y1*z1 + q*y1*z2 + p*y2*z1 + sigma*y2*z2
    rhs = sigma * (y2 + (q/sigma)*y1) * (z2 + (p/sigma)*z1)
    max_err = max(max_err, abs(lhs-rhs))
    checks += 1

print('rank-one shear checks =', checks)
print('max absolute shear error =', max_err)
assert max_err < 1e-10

# Integral identity used after the |t|^{-3/2} characteristic-function bound:
# integral_R min(1,K |t|^{-3/2}) dt = 6 K^{2/3}.
for K in [0.01, 0.1, 1.0, 3.7, 100.0]:
    t0 = K**(2/3)
    exact_from_split = 2*t0 + 4*K/(math.sqrt(t0))
    target = 6*K**(2/3)
    assert abs(exact_from_split-target) <= 1e-12 * max(1.0, target)

print('QFORM_B11_R44_ANYPIVOT_RANKONE_TENSOR_CHECK_PASS')
