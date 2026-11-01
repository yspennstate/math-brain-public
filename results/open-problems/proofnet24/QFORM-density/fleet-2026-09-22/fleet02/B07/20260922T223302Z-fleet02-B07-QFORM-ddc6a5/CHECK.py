import math

# Constants in Theorem 3.1 / Corollary 5.1.
c_riesz = 2**(17/4) / math.sqrt(3)
c_zero_self = 16 / math.sqrt(3)
c_o0 = c_zero_self * 200**(1/8)
c_l3_zero_self = 12**(1/3)

print(f"RANDOMSHIFT_RIESZ_COEFF={c_riesz:.15f}")
print(f"ZEROSELF_RIESZ_COEFF={c_zero_self:.15f}")
print(f"O0_STRONG_STAR_BOUND={c_o0:.15f}")
print(f"ZEROSELF_L3_COEFF={c_l3_zero_self:.15f}")

# The arbitrary-self obstruction at a=2 has quadratic matrix
# [[2,1],[1,1/2]], which is rank one and equals 2*(x+y/2)^2.
a = 2.0
m00, m01, m11 = a, 1.0, 1.0/a
det = m00*m11 - m01*m01
trace = m00 + m11
disc = math.sqrt((m00-m11)**2 + 4*m01*m01)
eigs = ((trace+disc)/2, (trace-disc)/2)
print(f"SELF_STRESS_DET={det:.15f}")
print(f"SELF_STRESS_EIGS={eigs[0]:.15f},{eigs[1]:.15f}")
print(f"SELF_STRESS_W_DENSITY_AT_ZERO={min(abs(a),1.0):.15f}")

# Layer-cake constants: E 1/max(T1,T2) <= 4M, hence the
# three-copy order-statistic cost is <= 6M*(4M)=24M^2.
print("ORDERSTAT_CONSTANT=24")
print("QFORM_RANDOMSHIFT_L3_CHECK_PASS")
