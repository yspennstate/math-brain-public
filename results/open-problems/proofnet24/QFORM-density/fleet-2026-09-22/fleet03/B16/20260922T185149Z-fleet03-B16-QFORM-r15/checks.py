import math

C_hy = (3/2)**(1/3) / 3**(1/6)
base = 144*math.sqrt(12*math.e)/13
C_l3 = C_hy * base**(2/3)
C_square = 8 / 3**(3/4)
C_bridge = C_square * C_l3**(3/4)
C_stable_example = C_bridge * 2 / math.sqrt(1/4)
C_partner_r1 = 4*math.sqrt(2*math.e) * ((1/2)*(1/4))**(-1/4)

assert C_l3 < 15.14
assert C_bridge < 27
assert C_stable_example < 108
assert C_partner_r1 < 15.69
assert (18/7) > 2
assert (1/math.sqrt(7)+math.sqrt(6)/13)**2 < 1/2

print({
    "C_HY_3_2": C_hy,
    "C_L3": C_l3,
    "C_square": C_square,
    "C_bridge": C_bridge,
    "stable_example": C_stable_example,
    "partner_r1_branch": C_partner_r1,
    "ridge_diag_upper": (1/math.sqrt(7)+math.sqrt(6)/13)**2,
    "theta_times_s_lower": 18/7,
    "status": "PASS",
})
