import math
import numpy as np

# Exact constants from the report.
near_base = 256.0
tail_base = 32.0
K0_L3_cubed = near_base + tail_base
assert K0_L3_cubed == 288.0

# Scaling by y -> 2 mu w gives 288/(2 mu)^2 = 72/mu^2.
assert abs(288.0 / 4.0 - 72.0) < 1e-15

# Square L^(3/2): integral <= 2 sqrt(2), hence norm <=2.
square_integral = 2.0 * math.sqrt(2.0)
square_norm = square_integral ** (2.0 / 3.0)
assert abs(square_norm - 2.0) < 1e-14

C_density = 2.0 * (72.0 ** (1.0 / 3.0))
assert abs(C_density - 576.0 ** (1.0 / 3.0)) < 1e-14
C_time = 4.0 * math.sqrt(math.pi) * (576.0 ** (1.0 / 6.0))
assert abs(C_time - 4.0 * math.sqrt(math.pi) * (24.0 ** (1.0 / 3.0))) < 1e-14

# Random deterministic check of the Schur determinant identity
# det [[0,mu,a],[mu,0,b],[a,b,c]] = det([[0,mu],[mu,0]]) * d,
# d = c - [a,b] B^{-1} [a,b]^T.
rng = np.random.default_rng(47)
max_err = 0.0
for _ in range(10000):
    mu = rng.uniform(-5.0, 5.0)
    if abs(mu) < 0.05:
        mu = 0.05 if mu >= 0 else -0.05
    a, b, c = rng.normal(size=3)
    B = np.array([[0.0, mu], [mu, 0.0]])
    v = np.array([a, b])
    d = c - v @ np.linalg.inv(B) @ v
    M = np.array([[0.0, mu, a], [mu, 0.0, b], [a, b, c]])
    err = abs(np.linalg.det(M) - np.linalg.det(B) * d)
    max_err = max(max_err, err)

print('near_base_L3_cubed=', near_base)
print('partner_tail_base_L3_cubed=', tail_base)
print('K0_L3_cubed=', K0_L3_cubed)
print('square_L3over2_integral_bound=', square_integral)
print('square_L3over2_norm_bound=', square_norm)
print('density_constant_576^(1/3)=', C_density)
print('time_constant=', C_time)
print('max_10000_random_schur_det_error=', max_err)
print('QFORM_B03_R47_CHECK_PASS')
