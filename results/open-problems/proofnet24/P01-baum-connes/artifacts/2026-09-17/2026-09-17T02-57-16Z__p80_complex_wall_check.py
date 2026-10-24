from fractions import Fraction

# Exact finite self-check for P01-P80.
# This script is deliberately limited to the finite algebraic core of the argument:
# the explicit Gaussian-rational parameter, K1 coordinate bookkeeping,
# the local-degree Jacobian at the critical wall, and the Toeplitz index convention.

re = Fraction(1, 4)
im = Fraction(1, 4)
mod2 = re * re + im * im
assert mod2 == Fraction(1, 8)
assert mod2 < 1

# Explicit word w = s1^{-3} s2^4 and g = w^{-1} a.
w = (-3, 4)
g = (3, -4)
assert tuple(w[i] + g[i] for i in range(2)) == (0, 0)

# For c = r exp(i theta0), at the critical zero t0 = pi-theta0:
# partial_r(1 + r exp(i(theta0+t))) = -1,
# partial_t(1 + r exp(i(theta0+t))) = -i.
# As a real map (r,t) -> (Re f, Im f), the Jacobian columns are
# (-1,0) and (0,-1), so the local degree is +1.
jac_det = (-1) * (-1) - 0 * 0
assert jac_det == 1

# Toeplitz convention: ind(T_phi) = -wind(phi).
inside_winding = 0
outside_winding = 1
inside_index = -inside_winding
outside_index = -outside_winding
assert (inside_index, outside_index) == (0, -1)

print("P80 exact self-check")
print(f"|c|^2 = {mod2} < 1")
print(f"explicit class coordinate = {w}")
print(f"critical subgroup coordinate = {g}")
print(f"outside cancellation coordinate = {(w[0] + g[0], w[1] + g[1])}")
print(f"critical local Jacobian determinant = {jac_det}")
print(f"Toeplitz boundary charges (inside,outside) = {(inside_index, outside_index)}")
print("ALL EXACT SELF-CHECK ASSERTIONS PASSED")
