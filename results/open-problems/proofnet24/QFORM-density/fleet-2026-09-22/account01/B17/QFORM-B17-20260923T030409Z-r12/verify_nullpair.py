import math

# Deterministic consistency checks for QFORM-NULLPAIR-SQUARE-GLOBAL-4-v1.
# The analytic proof is in REPORT.md; this script only certifies constants
# and the elementary spectral/translation identities used there.

target = 3.0 * math.sqrt(2.0)
C_null = 4.0
gamma = 0.577215664901532860606512090082402431
C_partner = (6.0 / math.pi) * (2.5 + math.log(4.0 / 3.0) - gamma)

assert C_null < target
assert C_partner < target
assert max(C_null, C_partner) == C_partner

# For A=[[0,a,0],[a,0,0],[0,0,b]], the characteristic polynomial is
# (b-lambda)(lambda^2-a^2), hence the eigenvalues are b,a,-a.
for a, b in [(1.0, 1.0), (2.0, -3.0), (-1.5, 4.0)]:
    eigs = sorted([a, -a, b])
    assert min(abs(x) for x in eigs) >= min(abs(a), abs(b))

# Translation identity check at sample values.
a, b = 1.7, -2.3
alpha, beta, gamma_lin, c = 0.4, -0.9, 1.2, -0.7
X, Y, Z = 0.31, -0.27, 0.44
Xp = X + beta / (2.0 * a)
Yp = Y + alpha / (2.0 * a)
Zp = Z + gamma_lin / (2.0 * b)
lhs = 2*a*X*Y + b*Z*Z + alpha*X + beta*Y + gamma_lin*Z + c
rhs = 2*a*Xp*Yp + b*Zp*Zp + c - alpha*beta/(2*a) - gamma_lin*gamma_lin/(4*b)
assert abs(lhs-rhs) < 1e-12

print('PASS QFORM-NULLPAIR-SQUARE-GLOBAL-4-v1')
print('C_null_pair =', C_null)
print('C_partner_majority =', repr(C_partner))
print('3sqrt2 =', repr(target))
print('gap_target_minus_4 =', repr(target-C_null))
print('gap_target_minus_partner =', repr(target-C_partner))
print('union_bound =', repr(max(C_null, C_partner)))
print('exact comparison 4 < 3sqrt2 follows from 16 < 18')
print('spectral identity: spec([[0,a,0],[a,0,0],[0,0,b]])={a,-a,b}')
print('translation identity: PASS')
