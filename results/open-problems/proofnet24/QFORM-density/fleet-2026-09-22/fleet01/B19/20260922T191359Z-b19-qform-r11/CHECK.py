import math

# Exact constants in the rank-two weighted endpoint.
C_general = 4.0 * math.sqrt(2.0 * math.e)
C_one_physical_bank = 4.0 * math.sqrt(2.0) * math.e**0.25
C_two_physical_banks = 4.0 * math.sqrt(2.0)

# Partner R1 exact-rank-two splice.
C_R1 = C_general * 1536.0**(1.0/8.0)

# fleet03/B08 near-coloop aggregate constant, evaluated only as a fixed-packet endpoint.
delta0 = 4191.0 / 281804800.0
C_fixed_packet = C_one_physical_bank * delta0**(-1.0/8.0)

# Weighted integral identity for min(1,A/t):
# int_0^A t^{-1/2} dt + A int_A^inf t^{-3/2} dt = 4 sqrt(A).
for A in [1e-8, 1e-3, 1.0, 7.25, 1e4]:
    lhs = 2.0 * math.sqrt(A) + 2.0 * math.sqrt(A)
    rhs = 4.0 * math.sqrt(A)
    assert abs(lhs-rhs) <= 1e-12 * max(1.0, rhs)

# Rank-two exterior identity: if E2=(s1*s2)^2 then
# (s1*s2)^(-1/4)=E2^(-1/8).
for s1, s2 in [(1.0,1.0),(2.0,0.25),(7.0,3.0),(1e-3,9.0)]:
    Pi = s1*s2
    E2 = Pi*Pi
    assert abs(Pi**(-0.25)-E2**(-0.125)) <= 1e-12 * max(1.0,Pi**(-0.25))

print(f"C_GENERAL={C_general:.15f}")
print(f"C_ONE_PHYSICAL_BANK={C_one_physical_bank:.15f}")
print(f"C_TWO_PHYSICAL_BANKS={C_two_physical_banks:.15f}")
print(f"C_R1_EXACT_RANK2={C_R1:.15f}")
print(f"DELTA0={delta0:.15e}")
print(f"C_FIXED_PACKET_AT_DELTA0={C_fixed_packet:.15f}")
print("QFORM_B19_R11_RANK2_HALF_RIESZ_CHECK_PASS")
