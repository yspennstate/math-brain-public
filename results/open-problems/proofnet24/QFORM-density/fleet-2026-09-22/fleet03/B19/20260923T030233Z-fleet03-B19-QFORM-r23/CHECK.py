import math

m0 = math.sqrt(1023)/64
H2_const = 4*2**0.25
H4_const = H2_const**0.5
riesz_const = 4*2**0.125
pair_const = 3*2**(25/12)
collar_H2 = H2_const*m0**(-0.5)
collar_H4 = collar_H2**0.5
collar_riesz = 2*collar_H2**0.5
threshold = pair_const*(1/64)**(-1/3)*(1/64)**(-1/6)*(1/4)**(-1/6)
partner = 34*math.sqrt(9)

print(f"m0={m0:.15f}")
print(f"H2_const={H2_const:.15f}")
print(f"H4_const={H4_const:.15f}")
print(f"riesz_const={riesz_const:.15f}")
print(f"pair_const={pair_const:.15f}")
print(f"collar_H2={collar_H2:.15f}")
print(f"collar_H4={collar_H4:.15f}")
print(f"collar_riesz={collar_riesz:.15f}")
print(f"threshold={threshold:.15f}")
print(f"partner={partner:.15f}")
assert collar_H2 < 6.729
assert collar_H4 < 2.594
assert collar_riesz < 5.188
assert pair_const < 12.714
assert threshold < 129
assert partner == 102
print("QFORM_B19_R23_ARBITRARY_HUB_CHECK_PASS")
