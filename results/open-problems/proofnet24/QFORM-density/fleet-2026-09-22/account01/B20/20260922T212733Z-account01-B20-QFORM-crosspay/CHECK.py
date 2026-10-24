from math import sqrt

m = 3501 / 8000
C = 40 * sqrt(2 / m)
print(f"m={m:.15f}")
print(f"C={C:.15f}")
print(f"same_exact_form={40*sqrt(16000/3501):.15f}")
print(f"C_lt_85_512={C < 85.512}")
