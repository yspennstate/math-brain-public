import math

C = 2**(13/4)
assert abs(C - 9.513656920021768) < 1e-12
nested = C * (2048)**0.25
assert abs(nested - 64.0) < 1e-12

for j in range(0, 20001):
    r = math.exp(j * math.log(1e8) / 20000)
    assert 1 + math.log(r) <= 2 * math.sqrt(r) + 1e-12

print(f"main_constant={C:.15f}")
print(f"nested_heavy_constant={nested:.15f}")
print("log_inequality_grid=PASS")
print("STATUS=PASS")
