import math
import numpy as np

# Deterministic arithmetic check for QFORM-FRACTIONAL-VOLUME-BL-v1.
theta = 3.0/4.0
K = theta**(-theta) * (1.0-theta)**(-(1.0-theta))
gamma = 3.0*theta/2.0
Ctheta = math.e * (gamma/(gamma-1.0)) * K**(-1.0/(6.0*theta))
Co0 = Ctheta * 256.0**(1.0/6.0)
alpha_gate = 1.0/(2.0*theta)
joint_floor = 2.0*alpha_gate - 1.0
packet_floor = (1.0/256.0) * joint_floor / 4.0
matching_floor = packet_floor / 36.0

# Check the scalar interpolation inequality 1+x >= K_theta x^theta
# on a broad log grid; its exact minimizer is theta/(1-theta)=3.
xs = np.logspace(-8, 8, 200001)
ratios = (1.0 + xs)/(xs**theta)
k = int(np.argmin(ratios))

print(f"theta={theta:.17g}")
print(f"alpha_gate={alpha_gate:.17g}")
print(f"K_theta={K:.17g}")
print(f"grid_min_ratio={ratios[k]:.17g}")
print(f"grid_argmin={xs[k]:.17g}")
print(f"theoretical_argmin={theta/(1.0-theta):.17g}")
print(f"C_theta_sharp={Ctheta:.17g}")
print(f"O0_density_bound={Co0:.17g}")
print(f"joint_mass_fraction={joint_floor:.17g}")
print(f"two_anchor_packet_floor={packet_floor:.17g}")
print(f"two_anchor_packet_reciprocal={1.0/packet_floor:.17g}")
print(f"matching_product_floor={matching_floor:.17g}")
print(f"matching_product_reciprocal={1.0/matching_floor:.17g}")
