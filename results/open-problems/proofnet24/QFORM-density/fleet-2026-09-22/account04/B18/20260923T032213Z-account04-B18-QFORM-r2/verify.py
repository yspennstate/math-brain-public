import math

def cap(beta):
    return 3 * math.exp((3-beta)/3) * (1-beta)**(-(1-beta)/3)

assert abs(cap(0)-3*math.e) < 1e-12
assert abs(cap(0.5)-3*math.exp(5/6)*2**(1/6)) < 1e-12
assert cap(0.5) < cap(0)

for j in range(10001):
    beta=0.5*j/10000
    assert cap(beta) <= 3*math.e + 1e-12

print(f"3e={3*math.e:.12f}")
print(f"endpoint={cap(0.5):.12f}")
print("PASS")
