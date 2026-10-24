import math
import numpy as np

# Envelope L2 check at Delta=1.
A = 2.0 * math.pi
l2_sq = 4.0 * A
assert abs(l2_sq - 8.0 * math.pi) < 1e-12

# Partner-compiled normalized constant.
partner_constant = 2.0 * math.sqrt(2.0 * math.pi)
assert partner_constant < 5.014

# Direct singleton refinement, not used for the generic partner theorem.
singleton_constant = 2.0 * math.sqrt(math.pi)
assert singleton_constant < 3.545

# Spectrum of Q0=2X1Y1+2X2Y2+Z1^2+Z2^2+Z3^2.
M = np.zeros((7, 7))
M[0, 2] = M[2, 0] = 1.0
M[1, 3] = M[3, 1] = 1.0
for idx in (4, 5, 6):
    M[idx, idx] = 1.0
spec = np.linalg.eigvalsh(M)
expected = np.array([-1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
assert np.max(np.abs(spec - expected)) < 1e-12

# Homogeneity of 2 sqrt(M) Delta^{-1/4}.
def rhs(delta, cap):
    return 2.0 * math.sqrt(cap) * delta ** (-0.25)

base_delta = 3.7
base_cap = 2.4
base = rhs(base_delta, base_cap)
max_scaling_error = 0.0
for c in (0.1, 0.7, 2.0, 13.0):
    scaled = rhs(c * c * base_delta, base_cap / abs(c))
    err = abs(scaled / base - 1.0 / abs(c))
    max_scaling_error = max(max_scaling_error, err)
assert max_scaling_error < 1e-12

print(f"cross_L2_squared_Delta1={l2_sq:.15f}")
print(f"partner_compiled_constant={partner_constant:.15f}")
print(f"singleton_refinement_constant={singleton_constant:.15f}")
print("spectrum=" + ",".join(f"{x:.12f}" for x in spec))
print(f"max_scaling_error={max_scaling_error:.3e}")
print("QFORM_B01_BOUNDED_REMAINDER_L2_CHECK_PASS")
print("STATUS=PASS")
