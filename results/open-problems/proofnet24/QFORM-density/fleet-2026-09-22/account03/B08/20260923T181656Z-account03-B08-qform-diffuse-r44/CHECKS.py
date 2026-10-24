from math import sqrt, pi

# Analytic constants from REPORT.md.
C_abstract_d2 = 2.0
C_physical_arms = 2.0 * sqrt(2.0)
arm_floor = 1.0 / (64.0 * sqrt(896.0))
C_r43 = C_physical_arms / sqrt(arm_floor)
C_threshold_stress = C_physical_arms / (1.0 / sqrt(2.0))

assert abs(C_abstract_d2 - 2.0) < 1e-15
assert abs(C_physical_arms - 2.8284271247461903) < 1e-14
assert abs(C_r43 - 123.79753089713084) < 1e-11
assert C_r43 < 124.0
assert abs(C_threshold_stress - 4.0) < 1e-12

# Exact eigenvector check for the scalar 3x3 star block
# S=[[0,1,1],[1,0,0],[1,0,0]].
def matvec(v):
    x, y, z = v
    return (y + z, x, x)

def err(v, lam):
    w = matvec(v)
    return max(abs(w[i] - lam*v[i]) for i in range(3))

rt2 = sqrt(2.0)
assert err((rt2, 1.0, 1.0), rt2) < 1e-14
assert err((-rt2, 1.0, 1.0), -rt2) < 1e-14
assert err((0.0, 1.0, -1.0), 0.0) < 1e-14

# Frequency-integration identity for d=2:
# integral_R min(1,K/t^2) dt = 4 sqrt(K).
for K in (0.03125, 1.0, 17.0, 1e4):
    t0 = sqrt(K)
    exact_split = 2.0 * (t0 + K/t0)
    assert abs(exact_split - 4.0*sqrt(K)) < 1e-12 * max(1.0, exact_split)

print("C_physical_arms=", repr(C_physical_arms))
print("C_r43=", repr(C_r43))
print("C_threshold_stress=", repr(C_threshold_stress))
print("QFORM_B08_R44_CHECK_PASS")
