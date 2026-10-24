from math import sqrt, pi, gamma

# Exact stress matrix numerically checked.
r2 = sqrt(2.0)
B = [
    [0.5, -0.5, -1.0/r2],
    [-0.5, 0.5, -1.0/r2],
    [-1.0/r2, -1.0/r2, 0.0],
]
B2 = [[sum(B[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
err = max(abs(B2[i][j] - (1.0 if i == j else 0.0)) for i in range(3) for j in range(3))
assert err < 1e-12

G = gamma(1.25)
C_tip = 2.0**(11.0/6.0)*sqrt(3.0)/sqrt(pi)*G**(2.0/3.0)
C_global = 2.0**(13.0/6.0)*sqrt(3.0)/sqrt(pi)*G**(2.0/3.0)
C_logconvex = 2.0**(11.0/6.0)*sqrt(3.0)*pi**(-1.0/3.0)
target = 3.0*sqrt(2.0)
assert C_tip < C_global < C_logconvex < target

# Rational certificate used after Gamma log-convexity and Archimedes' pi lower bound.
assert 1342683 > 1290496   # (669 sqrt(3))^2 > 1136^2

C8 = sqrt(pi)*gamma(7.5)/gamma(8.0)
CJ = 1.0 + 2.0**(9.0/4.0)*C8
assert C8 > 0.0 and CJ < 5.0

print('PASS QFORM_TWO_HEAVY_ONE_DIFFUSE_GLOBAL')
print('B2_error=', repr(err))
print('C_tip=', repr(C_tip))
print('C_global=', repr(C_global))
print('C_logconvex_upper=', repr(C_logconvex))
print('three_sqrt_two=', repr(target))
print('actual_gap=', repr(target-C_global))
print('analytic_logconvex_gap=', repr(target-C_logconvex))
print('C8=', repr(C8))
print('CJ=', repr(CJ))
