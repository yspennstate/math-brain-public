import math

# Deterministic arithmetic checks for REPORT.md; these do not constitute the proof.
H = math.sqrt(1536 * math.e**2)
rank1 = math.sqrt(H)
assert abs(H - 106.53445530886934) < 1e-12
assert abs(rank1 - 10.321552950446426) < 1e-12

# Diffuse DPP floor at q0=1/2.
q0 = 0.5
delta_floor = (2 - 3*q0)**3 / 64
assert abs(delta_floor - 1/512) < 1e-18
assert abs(delta_floor**(1/3) - 1/8) < 1e-15
assert abs(1 - 2*delta_floor**(1/3) - 3/4) < 1e-15

# delta^{-1/8} factor in the older Schur-DPP receiver.
factor = (1/delta_floor)**(1/8)
assert abs(factor - 2**(9/8)) < 1e-15

# General leverage-floor formula is nonnegative and at most 1/8 on [0,2/3].
for j in range(1001):
    q = (2/3)*j/1000
    val = (2-3*q)**3/64
    assert -1e-15 <= val <= 1/8 + 1e-15

print('QFORM_B13_R34_PAIR_VOLUME_STABILITY_CHECK_PASS')
print('H=', repr(H))
print('sqrtH=', repr(rank1))
print('delta_floor_q0_half=', repr(delta_floor))
print('d_floor=', repr(delta_floor**(1/3)))
print('dpp_factor=', repr(factor))
