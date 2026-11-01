import math

# Strict-target witness for the r42 mixed-norm obstruction.
eps = 1.0 / 64.0
lam = math.sqrt(1.0 + eps * eps)
eigs = (-lam, 1.0, lam)
assert min(abs(x) for x in eigs) >= 1.0

# r41/r42 hard collar data for hub H in
# A_eps = [[eps,1,0],[1,-eps,0],[0,0,1]].
q_h = 1.0
rho = 1.0
tau = 0.0
assert q_h >= 63.0 / 64.0
assert eps <= 1.0 / 64.0
assert rho * rho >= 62.0 / 63.0
assert tau <= eps / math.sqrt(63.0)

# Fresnel tail threshold used in the proof:
# |2 int_0^R exp(i u^2)du| >= sqrt(pi)-2/R >= sqrt(pi)/2
# for R >= 4/sqrt(pi), where R=sqrt(t)/2.
R0 = 4.0 / math.sqrt(math.pi)
t0 = 4.0 * R0 * R0
assert abs(t0 - 64.0 / math.pi) < 1e-12
assert math.sqrt(math.pi) - 2.0 / R0 >= math.sqrt(math.pi) / 2.0 - 1e-14

# Source-valid rank-two half-Riesz repair followed by the disjoint Y^2 square.
half_riesz = 128.0 * (1.0 + eps * eps) ** (-0.25)
assert half_riesz <= 128.0

# Designated fleet04/B16 r4 phase-aligned receiver, lambda=nu=K=1.
partner_constant = 8.0 * (math.sqrt(5.0) - 1.0) ** (-0.25)
assert partner_constant < 7.588

print(f"eps={eps:.17g}")
print(f"strict_target_eigenvalues={eigs}")
print(f"fresnel_log_divergence_threshold_t0={t0:.15f}")
print(f"half_riesz_disjoint_square_bound={half_riesz:.15f}")
print(f"fleet04_B16_r4_constant={partner_constant:.15f}")
print("STATUS=PASS")
