import math

p = 9/4
q = p/(p-1)
assert abs(q - 9/5) < 1e-15

# The three exhaustive E2 characteristic-envelope branches.
C_case1 = (2*p*math.exp(0.5))**(1/q)
C_case2 = (2*p*math.sqrt(2))**(1/q)
C_case3 = (6*q/(3*q-5))**(1/q) * math.exp(5/(12*q)) * 2**(-1/(3*q))
C_E2 = max(C_case1, C_case2, C_case3)
assert C_E2 < 7

# Generalized dependent-square compiler at p=9/4, q=9/5.
C_square = 2 / math.sqrt(1-q/2)
assert abs(C_square - 2*math.sqrt(10)) < 1e-12
C_SchurE2 = C_square * 7**(q/2)
assert C_SchurE2 < 36.45

# Apply E2 > L^4/135000 to the aligned survivor.
C_aligned_lp = 7 * 135000**(5/36)
C_aligned_smallball = C_aligned_lp * 2**(5/9)
assert C_aligned_lp < 36.12
assert C_aligned_smallball < 53.08

# Designated partner family: a=L and E2(L H_R)=L^4.
# New compiler gives C_SchurE2/L; designated partner gives 7.251/L.
assert C_SchurE2 / 7.251 < 5.03

print(f"p={p:.12f}")
print(f"q={q:.12f}")
print(f"C_case1={C_case1:.15f}")
print(f"C_case2={C_case2:.15f}")
print(f"C_case3={C_case3:.15f}")
print(f"C_E2_9_4={C_E2:.15f}")
print(f"C_square={C_square:.15f}")
print(f"C_SchurE2={C_SchurE2:.15f}")
print(f"C_aligned_lp={C_aligned_lp:.15f}")
print(f"C_aligned_centered_smallball={C_aligned_smallball:.15f}")
print(f"partner_sharp=7.251000000000000")
print(f"new_to_partner_ratio={C_SchurE2/7.251:.15f}")
print("QFORM_B08_R32_CHECK_PASS")
