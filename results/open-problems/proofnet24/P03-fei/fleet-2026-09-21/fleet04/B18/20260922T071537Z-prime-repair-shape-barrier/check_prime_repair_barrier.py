from decimal import Decimal, getcontext

getcontext().prec = 80

d = Decimal("0.0176114199558017537894958865691")
d_coarse = Decimal("0.017611")
alpha = Decimal(1121) / Decimal(1024)
center = Decimal("6.521851214")

threshold = d / alpha
coarse_threshold = d_coarse / alpha
A_if_B_zero = d * Decimal(256) / Decimal(57)
B_if_A_zero = d
residual_E_001 = d - alpha * Decimal("0.01")

assert alpha == Decimal("1.0947265625")
assert threshold > Decimal("0.0160875")
assert center + coarse_threshold > Decimal("6.5379383362")
assert A_if_B_zero > Decimal("0.0790969")
assert residual_E_001 > Decimal("0.00666415")

print("PASS")
print("alpha", alpha)
print("source_threshold", threshold)
print("coarse_threshold", coarse_threshold)
print("source_center_bound", center + threshold)
print("coarse_center_bound", center + coarse_threshold)
print("A_if_B_zero", A_if_B_zero)
print("B_if_A_zero", B_if_A_zero)
print("weighted_defect_if_E_0.01", residual_E_001)
