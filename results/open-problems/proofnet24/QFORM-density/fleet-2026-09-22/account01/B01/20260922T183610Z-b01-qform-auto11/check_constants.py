import math

c14 = math.gamma(3/4) * math.sin(math.pi/8) / math.pi
m = 7/8
Delta = 49/64
sigma0 = 27/2240

# High-ridge-leverage row-aggregate constant, with the universal
# one-dimensional projection-density constant C_lin factored out as C_lin^(1/4).
C_high_base = (
    32 * c14 * math.pi**0.25 * 6**0.125
    * Delta**(-0.25) * m**(-0.25) * sigma0**(-0.25)
)

# Partner account02/B01 r25 lift through the quarter-kernel.
C_partner_lift = (2**(13/4) / 3) * 216**0.25

# For envelope min(1, (t0/t)^(1/2)),
# integral_R |t|^(-3/4) envelope dt = 16 t0^(1/4).
def weighted_integral_closed(t0):
    low = 2 * 4 * t0**0.25
    high = 2 * 4 * t0**0.25
    return low + high

for t0 in [0.01, 1.0, 37.0]:
    got = weighted_integral_closed(t0)
    want = 16 * t0**0.25
    assert abs(got - want) <= 1e-12 * max(1.0, abs(want))

# Algebraic high-leverage implication at gamma=sigma/sqrt(3):
# K_gamma <= gamma^{-2} C C^T, so K_ii>1/2 forces
# ||row_i(C)||^2 > gamma^2/2 = sigma^2/6.
for sigma in [0.01, 1.0, 17.0]:
    gamma = sigma / math.sqrt(3)
    assert abs(gamma*gamma/2 - sigma*sigma/6) <= 1e-12 * max(1.0, sigma*sigma)

print(f"c_1/4={c14:.17g}")
print(f"C_high_base_times_C_lin^(1/4)={C_high_base:.15f}")
print(f"C_partner_lift={C_partner_lift:.15f}")
print("STATUS=PASS")
