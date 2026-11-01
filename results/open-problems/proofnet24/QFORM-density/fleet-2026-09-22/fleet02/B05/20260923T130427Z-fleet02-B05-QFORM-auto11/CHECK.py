import math
import random

# Constants in REPORT equations (6.4) and (7.3).
Cstar = 4.0 * math.exp(1.0/8.0) * 2.0**(-0.25) * math.gamma(0.25)
heavy_null_bound = 0.5 + 4.0*Cstar
assert Cstar < 13.819
assert heavy_null_bound < 55.776

# Algebraic shear check.  For orthonormal coefficient columns v,w and z=w+r v,
# G=[[1,r],[r,1+r^2]], det G=1, and (v_j,z_j) G^{-1} (v_j,z_j)^T=v_j^2+w_j^2.
max_error = 0.0
rng = random.Random(20260923)
for _ in range(100000):
    r = rng.uniform(-20.0,20.0)
    v = rng.uniform(-1.0,1.0)
    w = rng.uniform(-1.0,1.0)
    z = w + r*v
    # G^{-1}=[[1+r^2,-r],[-r,1]] because det G=1.
    lhs = (1.0+r*r)*v*v - 2.0*r*v*z + z*z
    rhs = v*v+w*w
    max_error = max(max_error, abs(lhs-rhs))
assert max_error < 1e-10

# Exact Gaussian integral factor in (6.3):
# int_R exp(-eps^2 t^2/2)|t|^{-1/2}dt
# = 2^(1/4) Gamma(1/4) eps^(-1/2).
gaussian_factor = 2.0**0.25 * math.gamma(0.25)

print("QFORM_B05_SLICE_FRESNEL_CHECK_PASS")
print("Cstar=", repr(Cstar))
print("heavy_null_bound=", repr(heavy_null_bound))
print("max_shear_leverage_error=", repr(max_error))
print("gaussian_factor=", repr(gaussian_factor))
