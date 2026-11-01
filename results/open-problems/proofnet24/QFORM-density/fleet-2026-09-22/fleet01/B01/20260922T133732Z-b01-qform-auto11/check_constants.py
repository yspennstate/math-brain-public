import math

S3 = (16*math.pi)**(1/3)
C21 = 2*(1 + 1/(1-2**(-1/3)))
C12 = 4*(1 + 1/(1-2**(-1/6)))
C03 = 8.0

delta21 = 1 + 1/3 - 1
# one cross-slope direction means rho=1/2
delta12 = 1/2 + 2/3 - 1

print(f"S3={S3:.15f}")
print(f"C21={C21:.15f}")
print(f"C12={C12:.15f}")
print(f"C03={C03:.15f}")
print(f"delta21={delta21:.15f}")
print(f"delta12={delta12:.15f}")

assert abs(C21 - 11.694644203726147) < 1e-12
assert abs(C12 - 40.663180595304866) < 1e-12
assert delta21 > 0
assert delta12 > 0
print("STATUS=PASS")
