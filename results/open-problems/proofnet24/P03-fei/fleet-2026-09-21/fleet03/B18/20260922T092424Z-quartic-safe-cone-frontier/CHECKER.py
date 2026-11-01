from fractions import Fraction as F

# Source-exact strong Numaro witness data imported from the completed source checker.
M2 = F(62098577, 239075328)
L4 = F(211575825297187673, 1628974855061766144)
D_LO = -F(38023735, 10**9)  # rigorous lower endpoint for D^dagger
D_HI = -F(38023734, 10**9)  # rigorous upper endpoint for D^dagger

E2 = 4*M2
E4 = 8*L4
EFF_GAP = E4-E2
assert EFF_GAP == F(16938576520025, 203621856882720768)
assert EFF_GAP > 0

# New pure-quartic candidate.
CDAG = F(3260925607, 500000000)   # 6.521851214
LAM = F(58551, 200000)            # 0.292755
CENTER = CDAG + LAM*F(1,8)
assert CENTER == F(6558445589, 10**9)

# Worst-case certified strong-witness defect after repair.
REPAIRED_LO = D_LO + LAM*L4
assert REPAIRED_LO == F(1437702884772647393, 13574790458848051200000000)
assert REPAIRED_LO > 0

# Two-generator safe-cone frontier: any a,b >= 0 has payment <= E4 * center cost.
# The rigorous lower deficit d > 0.038023734 therefore forces this center floor.
D_MIN = F(38023734, 10**9)
CENTER_FLOOR = CDAG + D_MIN/E4
assert CENTER > CENTER_FLOOR

# The true source deficit is also <0.038023735, giving an upper endpoint for
# the pure-quartic center needed on this single witness.
D_MAX = F(38023735, 10**9)
PURE_Q4_UPPER = CDAG + D_MAX/E4
assert CENTER > PURE_Q4_UPPER

print('PASS')
print('M2', M2, float(M2))
print('L4', L4, float(L4))
print('E2', E2, float(E2))
print('E4', E4, float(E4))
print('E4_minus_E2', EFF_GAP, float(EFF_GAP))
print('lambda_Q', LAM, float(LAM))
print('candidate_center', CENTER, float(CENTER))
print('repaired_strong_witness_lower', REPAIRED_LO, float(REPAIRED_LO))
print('safe_cone_center_floor_from_d_lower', float(CENTER_FLOOR))
print('pure_q4_center_upper_from_d_upper', float(PURE_Q4_UPPER))
print('candidate_minus_pure_q4_upper', float(CENTER-PURE_Q4_UPPER))
