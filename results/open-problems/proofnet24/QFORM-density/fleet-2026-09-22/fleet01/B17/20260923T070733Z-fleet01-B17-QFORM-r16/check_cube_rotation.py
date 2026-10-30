import math

C_cube = math.pi * math.sqrt(3.0 / 2.0)
C_partner = math.pi * math.sqrt(2.0) / 3.0 * (1.0 + 4.0 / math.sqrt(5.0))
C_null = 2.0 + math.log(2.0)
C_candidate = 3.0 * math.sqrt(2.0)

# Elementary strict certificates used in the report.
# pi < 22/7 and (22/7)^2 = 484/49 < 12 imply pi^2 < 12,
# hence pi*sqrt(3/2) < 3*sqrt(2).
assert 484 < 12 * 49
# Partner certificate: pi < 22/7 reduces C_partner < 3sqrt(2)
# to 88 < 41sqrt(5), and squaring gives 7744 < 8405.
assert 7744 < 8405
assert C_cube < C_candidate
assert C_partner < C_candidate
assert C_null < C_candidate

R = math.sqrt(3.0) / 2.0

def ball_pushforward_density(t, R=R):
    if t < -R * R or t > R * R:
        return 0.0
    if t >= 0.0:
        return math.pi * math.sqrt(2.0 * (R * R - t))
    s = -t
    return 2.0 * math.pi * (
        math.sqrt((R * R + s) / 2.0) - math.sqrt(s)
    )

# Deterministic dense-grid sanity check of the analytic monotonicity statement.
N = 10000
mx = max(
    ball_pushforward_density(-R * R + 2.0 * R * R * i / N)
    for i in range(N + 1)
)
assert abs(mx - ball_pushforward_density(0.0)) < 1e-12
assert abs(ball_pushforward_density(0.0) - C_cube) < 1e-12

print(f"C_cube={C_cube:.15f}")
print(f"C_partner={C_partner:.15f}")
print(f"C_null={C_null:.15f}")
print(f"3sqrt2={C_candidate:.15f}")
print(f"gap_cube={C_candidate-C_cube:.15f}")
print(f"gap_partner={C_candidate-C_partner:.15f}")
print(f"ball_grid_max={mx:.15f}")
print("certificate_pi_squared: 484 < 588")
print("certificate_partner: 7744 < 8405")
print("QFORM_B17_CENTERED_BOX_ROTATION_CHECK_PASS")
