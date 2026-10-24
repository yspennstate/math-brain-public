from fractions import Fraction as Q

# Exact calibration for MOC4-MSQR-HIGHER-ORDER-SATURATION-v1.
# Abstract analytic local-max model:
#   F(x,y)=-(y-x^2/2)^2-x^6
#         = -y^2 + x^2 y - x^4/4 - x^6.
# At the origin, A=-D^2F=diag(0,2), z=e_x.
# The quartic Lyapunov-Schmidt gate saturates exactly.

Aplus_yy = Q(1, 2)
ell_y = Q(2)                 # D^3 F[z,z,e_y]
ell_energy = ell_y * Aplus_yy * ell_y
q = Q(-6)                    # D^4 F[z,z,z,z]
quartic_gate = q + 3 * ell_energy

# Optimizing second-order correction y_*=(1/2)A^+ ell = (0,1/2).
y_star_y = Q(1, 2)

# Fifth-order identity:
# D5[z^5] + 20 D4[z^3,y_*] + 60 D3[z,y_*,y_*] = 0.
# Here all three terms vanish.
quintic_identity = Q(0)

# Sixth-order corrected covector
# m(w)=D3[z,y_*,w]+(1/6)D4[z,z,z,w].
# For w=e_x: D3[x,y_*,x]=2*(1/2)=1 and (1/6)D4[x^4]=-1.
# For w=e_y both terms vanish.
m_x = Q(2) * y_star_y + Q(1, 6) * Q(-6)
m_y = Q(0)

# D6[z^6] = -720; all fixed mixed fifth/fourth/third terms in the
# general sixth-order gate vanish for this polynomial, and m=0.
sextic_gate = Q(-720) + 360 * (m_y * Aplus_yy * m_y)

# Direct restriction along the optimized curve y=x^2/2 is F=-x^6.
curve_t6_coefficient = Q(-1)

assert ell_energy == 2
assert quartic_gate == 0
assert quintic_identity == 0
assert (m_x, m_y) == (0, 0)
assert sextic_gate == -720
assert curve_t6_coefficient == -1

print(f"ell_energy={ell_energy}")
print(f"quartic_gate={quartic_gate}")
print(f"quintic_identity={quintic_identity}")
print(f"m=({m_x},{m_y})")
print(f"sextic_gate={sextic_gate}")
print(f"optimized_curve_t6_coefficient={curve_t6_coefficient}")
print("PASS exact higher-order saturation calibration")
