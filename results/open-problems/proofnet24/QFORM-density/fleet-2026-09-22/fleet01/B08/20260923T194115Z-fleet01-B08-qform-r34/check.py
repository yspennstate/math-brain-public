import math
import numpy as np

rng = np.random.default_rng(20260923)
N = 5000
violations = 0
max_ratio = 0.0
min_slack = float('inf')
for _ in range(N):
    m = int(rng.integers(4, 80))
    Z = rng.normal(size=(m, 3))
    W, _ = np.linalg.qr(Z, mode='reduced')
    q = W[:, 0]
    U = W[:, 1:]
    d = float(rng.uniform(0.5, 1.0))
    s = math.sqrt(max(0.0, 1.0-d*d))
    a = rng.normal(size=2)
    a /= np.linalg.norm(a)
    a *= s
    r = d*q + U@a
    gamma = math.sqrt((1.0-math.sqrt(1.0-d*d))/2.0)
    for i in range(m):
        h = q[i]**2 + float(U[i]@U[i])
        u = float(np.linalg.norm(U[i]))
        lhs = max(abs(r[i]), u)
        rhs = gamma*math.sqrt(h)
        if lhs + 1e-12 < rhs:
            violations += 1
        if lhs > 0:
            max_ratio = max(max_ratio, rhs/lhs)
        min_slack = min(min_slack, lhs-rhs)

c = math.sqrt(3/20)
beta = 3/math.sqrt(40)
d0 = 0.5
gamma0 = math.sqrt((1-math.sqrt(1-d0*d0))/2)
nu0 = 1/48
cross = beta*gamma0*math.sqrt(nu0)
child_row = c*gamma0*math.sqrt(nu0)
child_piece = child_row/math.sqrt(2)
kappa = c*beta*d0*d0/(2*math.sqrt(c*c*d0*d0+4*beta*beta))
print('QFORM_B08_R34_ROW_CURRENCY_CHECK_PASS' if violations == 0 else 'FAIL')
print('frames', N)
print('violations', violations)
print('max_rhs_over_lhs', repr(max_ratio))
print('min_slack', repr(min_slack))
print('gamma0', repr(gamma0))
print('cross_star_threshold_over_L', repr(cross))
print('child_row_threshold_over_L', repr(child_row))
print('child_diag_or_star_threshold_over_L', repr(child_piece))
print('partner_kappa', repr(kappa))
print('partner_leakage_threshold_over_L', repr(kappa/16))
print('partner_density_constant', repr(23/kappa))
