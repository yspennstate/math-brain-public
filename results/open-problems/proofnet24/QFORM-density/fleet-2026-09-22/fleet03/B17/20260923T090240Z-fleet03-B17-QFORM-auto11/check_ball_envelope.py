from math import pi, sqrt, atanh

R = sqrt(3.0) / 2.0
ceiling = sqrt(2.0) * pi * R
target = 3.0 * sqrt(2.0)
partner_tip = 6.0 * sqrt(3.0) * atanh((sqrt(2.0) - 1.0) / sqrt(3.0))

# Analytic strict comparison is pi < 2*sqrt(3); 22/7 supplies a rational certificate.
assert pi < 22.0 / 7.0
assert 22.0 / 7.0 < 2.0 * sqrt(3.0)
assert ceiling < target
assert partner_tip < ceiling

# Endpoint checks for the two exact ball-envelope branches.
def pos_env(s):
    return 2.0 * pi * sqrt((R * R - s) / 2.0)

def neg_env(a):
    return 2.0 * pi * (sqrt((R * R + a) / 2.0) - sqrt(a))

assert abs(pos_env(0.0) - ceiling) < 1e-14
assert abs(neg_env(0.0) - ceiling) < 1e-14
assert abs(pos_env(R * R)) < 1e-14
assert abs(neg_env(R * R)) < 1e-14

# Deterministic grid sanity check of monotonicity; the proof itself is analytic in REPORT.md.
N = 10000
last_p = pos_env(0.0)
last_n = neg_env(0.0)
for k in range(1, N + 1):
    z = (R * R) * k / N
    p = pos_env(z)
    n = neg_env(z)
    assert p <= last_p + 1e-14
    assert n <= last_n + 1e-14
    last_p, last_n = p, n

print("QFORM_B17_BALL_ENVELOPE_CHECK_PASS")
print("R =", R)
print("global 3D rotated-cube ceiling =", ceiling)
print("3sqrt2 obstruction =", target)
print("strict gap =", target - ceiling)
print("partner Householder tip =", partner_tip)
print("ceiling minus partner tip =", ceiling - partner_tip)
