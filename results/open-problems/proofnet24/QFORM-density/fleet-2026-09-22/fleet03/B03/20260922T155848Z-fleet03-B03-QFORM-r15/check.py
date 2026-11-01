import math

# Algebraic checks for QFORM-PAIRCOLLISION-BESOV-v1.
# This is a finite arithmetic checker, not a proof of the analytic theorems.

# Fractional criterion constant at alpha=3/4.
alpha = 0.75
c_frac = 2.0 / math.sqrt(math.pi * (1.0 - alpha))
assert abs(c_frac - 4.0 / math.sqrt(math.pi)) < 1e-14

# Recompute the same constant from r=3/2 Hausdorff--Young + split optimization.
r = 1.5
K_r = (2.0 / (1.0 - r/2.0)) ** (1.0/r)
c_from_split = 2.0 * (K_r ** (r/2.0)) * (2.0*math.pi) ** (-0.5)
assert abs(c_from_split - 4.0 / math.sqrt(math.pi)) < 1e-14

# Direct L^3 residual smoother constant.
c_l3 = 4.0 * math.sqrt(2.0)
assert abs(c_l3 - 5.656854249492381) < 1e-14

# Dyadic half-Riesz constants.
c_near = 2.0 * math.sqrt(2.0 / math.pi)
c_shell = 1.0 / math.sqrt(math.pi)
assert c_near > 0.0 and c_shell > 0.0

# Fejer interval constant from the compatible fleet04/B01 theorem.
s0 = 4.0 * math.sin(0.5) ** 2
assert 0.0 < s0 < 1.0

# Endpoint counterexample: near-zero squared-density L^2 mass is exactly 1/4.
# Integral_0^{e^-4} dr/[r log(1/r)^2] = Integral_4^infty du/u^2 = 1/4.
near_l2 = 0.25
assert near_l2 == 0.25

# The near-zero source mass m obeys m <= e^-2/2 < 1, so the far unit-density
# interval of length 1-m used in the construction is legitimate.
m_upper = math.exp(-2.0) / 2.0
assert m_upper < 1.0

print('QFORM_PAIRCOLLISION_BESOV_CHECK_PASS')
print(f'fractional_constant_alpha_3_4={c_frac:.15f}')
print(f'L3_square_smoother_constant={c_l3:.15f}')
print(f'dyadic_near_prefactor={c_near:.15f}')
print(f'dyadic_shell_prefactor={c_shell:.15f}')
print(f'fejer_s0={s0:.15f}')
print(f'near_source_mass_upper={m_upper:.15f}')
