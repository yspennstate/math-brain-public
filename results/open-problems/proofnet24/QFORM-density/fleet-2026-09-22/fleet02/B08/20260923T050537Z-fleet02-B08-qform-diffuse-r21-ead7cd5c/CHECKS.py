from fractions import Fraction
from math import e, sqrt

h = Fraction(163, 250)
q = 2 * float(h)
anchor_fraction = 2 * float(h) - 1
nested_fraction = anchor_fraction / 2

# c2414... fractional three-volume theorem, threshold alpha_i <= q/2 = h.
Cfrac = 3 * e / ((3 - 2*q) * sqrt(q))

# fleet03/B08 r27 anchored self-matched theorem after Z_anchor>(2h-1)Z3,
# with Z3>=zeta^6 and anchor row/column norm <= zeta.
Cself = 10 * sqrt(e) * (2 * anchor_fraction) ** (-1/5)
Crouter = max(Cfrac, Cself)

beta = (3/16) * sqrt(3/5)
zeta0 = beta
zeta1 = beta / (14400 ** (1/6))
zeta2 = (beta / 120) / (225 ** (1/6))

# e5f71... D5 constants used in the actual k=1,k=2 tail branches.
K5 = 5 * sqrt(2*e) * (225/37) ** (1/10)
k1_D5 = K5 / (beta * (1/8) ** (3/5))
c4 = ((1-1/225)*(1-2/225)*(1-3/225))/24
K4 = 5 * sqrt(2*e) * c4 ** (-1/10)
k2_D5_first = K4 / (beta * (1/8) ** (4/5))
k2_D5_second = K5 / (beta/120)

assert q < 1.5
assert abs(anchor_fraction - 38/125) < 1e-15
assert abs(nested_fraction - 19/125) < 1e-15
assert Cfrac < 18.218 and Cself < 18.218
assert Crouter/zeta0 < 126
assert Crouter/zeta1 < 619
assert Crouter/zeta2 < 37122
assert k1_D5 < 335
assert k2_D5_first < 584
assert k2_D5_second < 11539

print('QFORM_B08_R21_CHECK_PASS')
print(f'h={float(h):.12f}')
print(f'q={q:.12f}')
print(f'anchor_fraction={anchor_fraction:.12f}')
print(f'nested_fraction={nested_fraction:.12f}')
print(f'fractional_constant={Cfrac:.12f}')
print(f'selfmatch_constant={Cself:.12f}')
print(f'router_constant={Crouter:.12f}')
print(f'beta_over_L={beta:.15f}')
print(f'zeta0_over_L={zeta0:.15f}')
print(f'zeta1_over_L={zeta1:.15f}')
print(f'zeta2_over_L={zeta2:.15f}')
print(f'router_k0_over_L={Crouter/zeta0:.12f}')
print(f'router_k1_over_L={Crouter/zeta1:.12f}')
print(f'router_k2_over_L={Crouter/zeta2:.12f}')
print(f'k1_D5_over_L={k1_D5:.12f}')
print(f'k2_D5_first_over_L={k2_D5_first:.12f}')
print(f'k2_D5_second_over_L={k2_D5_second:.12f}')
