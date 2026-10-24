from fractions import Fraction as Q

# Frozen surface-product route: X_{3,4} contains T_10 square T_14.
d = 10
q = 13
p = Q(4540551, 100000000)
s = 1 - p
u = Q(9261812689, 10000000000)

# Branch pgf map at s=1-p.
F_u = s * (1 - p + p*u) ** (d-1)
contraction_upper = s * p * (d-1)
root_supersolution_margin = u - F_u
activation_lower = 1 - s * (1 - p + p*u) ** d
activation_margin = q * activation_lower - 1

# Clean rational p_u floor from the predecessor's adjacency bound
# R_34 = 2159/250 + 2 sqrt(13), Q_nb = 27.
sqrt13_upper = Q(1803,500)
sqrt13_lower = Q(18,5)
sqrt_upper_margin = sqrt13_upper**2 - 13
sqrt_lower_margin = 13 - sqrt13_lower**2
Rbar = Q(2159,250) + 2*sqrt13_upper
Rlower = Q(2159,250) + 2*sqrt13_lower
Qnb = Q(27,1)
z = Q(10000,719)  # reciprocal of proposed rational p_u floor
P_lower = z*z - Rbar*z + Qnb
above_geometric_mean = z*z - Qnb
discriminant_positive_lower = Rlower*Rlower - 4*Qnb

pu_floor = Q(719,10000)
gap = pu_floor - p

checks = {
    "p_subcritical_vertical_tree": p < Q(1,d-1),
    "global_contraction": contraction_upper < 1,
    "rational_fixed_point_supersolution": root_supersolution_margin > 0,
    "forward_fibre_activation": activation_margin > 0,
    "sqrt13_upper_valid": sqrt_upper_margin > 0,
    "sqrt13_lower_valid": sqrt_lower_margin > 0,
    "nb_discriminant_positive": discriminant_positive_lower > 0,
    "z_above_sqrt_Q": above_geometric_mean > 0,
    "nb_polynomial_positive_at_z": P_lower > 0,
    "certified_gap_positive": gap > 0,
}

print("PROB10-09 TREE-FIBRE FIXED-POINT EXACT CERTIFICATE")
print(f"p={p} decimal={float(p):.12f}")
print(f"u={u} decimal={float(u):.12f}")
print(f"contraction_upper={contraction_upper} decimal={float(contraction_upper):.12f}")
print(f"u_minus_Fu={root_supersolution_margin}")
print(f"u_minus_Fu_decimal={float(root_supersolution_margin):.18e}")
print(f"q_activation_minus_1={activation_margin}")
print(f"q_activation_minus_1_decimal={float(activation_margin):.18e}")
print(f"sqrt13_upper_square_minus_13={sqrt_upper_margin}")
print(f"13_minus_sqrt13_lower_square={sqrt_lower_margin}")
print(f"Rlower_square_minus_108={discriminant_positive_lower}")
print(f"z_square_minus_27={above_geometric_mean}")
print(f"P_Rbar_at_z={P_lower}")
print(f"pu_floor={pu_floor} decimal={float(pu_floor):.12f}")
print(f"gap={gap} decimal={float(gap):.12f}")
for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")
print("ALL_EXACT_CHECKS_PASS" if all(checks.values()) else "EXACT_CHECK_FAILURE")
